#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: aap_operator_channel_scrape
short_description: Dump container images for every CSV in AAP operator channels from one operator index
description:
  - Pulls (or reuses a cached extract of) one Red Hat operator index tag and reads the
    file-based catalog for the AAP operator package.
  - For every CSV in each requested channel, writes C(<channels_dir>/<channel>/vars/<csv>.yml)
    with the bundle's relatedImages (plus deployment/env images when the catalog embeds
    the full CSV).
  - Existing vars files are merged so C(ocp_indexes) accumulates every index tag the CSV
    has been observed in. CSVs that disappear from an index are never deleted.
  - Channels are either the explicit I(channels) list or, when that is empty, every channel
    in the index whose name matches I(channel_pattern) (minus I(channel_exclude)).
  - When I(skip_unchanged) is set, the index tag's digest and the channel selection are
    remembered in I(state_file); if neither changed since the last successful scrape the
    index is not pulled at all.
  - Use in an Ansible loop over OCP index tags for live progress.
version_added: "1.0.0"
options:
  ocp_version:
    description: OCP operator index tag (e.g. 4.18).
    required: true
    type: str
  channels:
    description:
      - OLM channel names to dump.
      - Leave empty to dump every channel matching I(channel_pattern).
    required: false
    type: list
    elements: str
    default: []
  channel_pattern:
    description: Regex (re.search) selecting channels to dump when I(channels) is empty.
    required: false
    type: str
    default: "^stable-"
  channel_min_version:
    description:
      - Skip channels whose AAP version (first C(<major>.<minor>) in the name, e.g. C(stable-2.4)
        -> C(2.4)) is lower than this. Channels without a version in the name are kept.
      - Only applies when I(channels) is empty. Leave empty to keep every version.
    required: false
    type: str
    default: ""
  channel_exclude:
    description: Channel names never dumped, even when they match I(channel_pattern).
    required: false
    type: list
    elements: str
    default: []
  channels_dir:
    description: Output root; files go to C(<channels_dir>/<channel>/vars/).
    required: true
    type: path
  index_cache_dir:
    description: Directory for extracted package catalogs, one C(ocp-<version>) dir per tag.
    required: true
    type: path
  refresh_index:
    description: Re-pull the index even when a cached extract exists.
    required: false
    type: bool
    default: true
  index_digest:
    description:
      - Current manifest digest of the index tag, if already known (e.g. from discovery).
      - Looked up with C(skopeo inspect) when empty.
    required: false
    type: str
    default: ""
  skip_unchanged:
    description: Skip indexes whose digest and channel selection match I(state_file).
    required: false
    type: bool
    default: true
  state_file:
    description: YAML file remembering the last successfully scraped digest per index tag.
    required: false
    type: path
  index_repository:
    description: Operator index repository path within the registry.
    required: false
    type: str
    default: redhat/redhat-operator-index
  package_name:
    description: OLM package name in the operator index.
    required: false
    type: str
    default: ansible-automation-platform-operator
  registry:
    description: Container registry host.
    required: false
    type: str
    default: registry.redhat.io
author:
  - lennysh
'''

EXAMPLES = r'''
- name: Dump channel images from operator index
  aap_operator_channel_scrape:
    ocp_version: "4.18"
    channels:
      - stable-2.6
      - stable-2.6-cluster-scoped
    channels_dir: "{{ playbook_dir }}/channels"
    index_cache_dir: "{{ playbook_dir }}/.cache/operator-index"
'''

RETURN = r'''
index_status:
  description: One of C(ok), C(cached), C(unchanged), C(pull_failed), C(create_failed), C(package_not_found).
  type: str
  returned: always
channels_found:
  description: Dumped channels present in this index.
  type: list
  returned: always
channels_missing:
  description: Requested channels absent from this index.
  type: list
  returned: always
channels_available:
  description: Every channel for the package in this index (configured or not).
  type: list
  returned: always
csvs_seen:
  description: Number of CSV entries processed across found channels.
  type: int
  returned: always
csvs_written:
  description: Vars files created or updated.
  type: list
  returned: always
'''

import base64
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile

import yaml

from ansible.module_utils.basic import AnsibleModule

# Bump when the vars file format or scrape logic changes so unchanged indexes are re-read.
SCRAPE_FORMAT = 3


def version_key(version):
    return tuple(int(p) for p in str(version).split(".") if p.isdigit())


def csv_epoch(csv_name):
    """Trailing build timestamp of CSV names like aap-operator.v2.6.0-0.1777410689."""
    match = re.search(r"-0\.(\d{10})$", csv_name)
    return int(match.group(1)) if match else None


def index_digest(image):
    """Current manifest digest of an image tag, or "" if it can't be read."""
    proc = subprocess.run(
        ["skopeo", "inspect", "--no-tags", "--format", "{{.Digest}}", "docker://%s" % image],
        capture_output=True, text=True,
    )
    return proc.stdout.strip() if proc.returncode == 0 else ""


def copy_out(container_id, src, dest_dir):
    """podman cp <container>:<src> into dest_dir via a tar stream (no shell)."""
    proc = subprocess.Popen(
        ["podman", "cp", "%s:%s" % (container_id, src), "-"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    try:
        with tarfile.open(fileobj=proc.stdout, mode="r|") as tar:
            for member in tar:
                # Only plain files/dirs, and never outside dest_dir.
                target = os.path.realpath(os.path.join(dest_dir, member.name))
                if not target.startswith(os.path.realpath(dest_dir) + os.sep):
                    continue
                if member.isdir() or member.isfile():
                    tar.extract(member, dest_dir, set_attrs=False)
    except tarfile.TarError as exc:
        proc.kill()
        proc.wait()
        return "tar: %s" % exc
    finally:
        proc.stdout.close()
    stderr = proc.stderr.read().decode("utf-8", "replace").strip()
    proc.stderr.close()
    return stderr if proc.wait() != 0 else ""


def extract_package_catalog(module, image, ocp_version, package, cache_dir, refresh):
    """Return path to <cache>/ocp-<ver>/<package>, pulling the index if needed."""
    ocp_dir = os.path.join(cache_dir, "ocp-%s" % ocp_version)
    pkg_dir = os.path.join(ocp_dir, package)
    if os.path.isdir(pkg_dir) and not refresh:
        return pkg_dir, "cached"

    pull = subprocess.run(["podman", "pull", "-q", image], capture_output=True, text=True)
    if pull.returncode != 0:
        module.warn("Failed to pull %s: %s" % (image, pull.stderr.strip()))
        return None, "pull_failed"

    status = "ok"
    create = subprocess.run(["podman", "create", image], capture_output=True, text=True)
    if create.returncode != 0:
        module.warn("Failed to create container for %s: %s" % (image, create.stderr.strip()))
        status = "create_failed"
    else:
        container_id = create.stdout.strip()
        tmp_dir = tempfile.mkdtemp(dir=cache_dir)
        err = copy_out(container_id, "/configs/%s" % package, tmp_dir)
        subprocess.run(["podman", "rm", "-v", container_id], capture_output=True)
        extracted = os.path.join(tmp_dir, package)
        if err or not os.path.isdir(extracted):
            module.warn("Package %s not found in %s %s" % (package, image, err))
            status = "package_not_found"
        else:
            shutil.rmtree(pkg_dir, ignore_errors=True)
            os.makedirs(ocp_dir, exist_ok=True)
            shutil.move(extracted, pkg_dir)
        shutil.rmtree(tmp_dir, ignore_errors=True)

    # Index images are large; do not leave them in local storage.
    subprocess.run(["podman", "rmi", image], capture_output=True)
    return (pkg_dir if status == "ok" else None), status


def load_state(path):
    if path and os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fp:
            return yaml.safe_load(fp) or {}
    return {}


def save_state(path, state):
    if not path:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = "%s.tmp" % path
    with open(tmp, "w", encoding="utf-8") as fp:
        yaml.safe_dump(state, fp, sort_keys=True, default_flow_style=False)
    os.replace(tmp, path)


def selection_fingerprint(params):
    """Hash of everything besides the index digest that affects what gets written."""
    key = repr((
        SCRAPE_FORMAT, params["package_name"], sorted(params["channels"]),
        params["channel_pattern"], params["channel_min_version"], sorted(params["channel_exclude"]),
        os.path.realpath(params["channels_dir"]),
    ))
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def channel_version(channel):
    match = re.search(r"(\d+)\.(\d+)", channel)
    return (int(match.group(1)), int(match.group(2))) if match else None


def select_channels(available, explicit, pattern, exclude, min_version=""):
    if explicit:
        return list(explicit)
    regex = re.compile(pattern)
    floor = channel_version(min_version) if min_version else None
    return [
        c for c in sorted(available)
        if regex.search(c) and c not in exclude
        and not (floor and channel_version(c) and channel_version(c) < floor)
    ]


def load_fbc_docs(pkg_dir):
    """Parse every JSON stream / YAML document under a package catalog dir."""
    docs = []
    decoder = json.JSONDecoder()
    for root, _, files in os.walk(pkg_dir):
        for fname in sorted(files):
            if not fname.endswith((".json", ".yaml", ".yml")):
                continue
            with open(os.path.join(root, fname), "r", encoding="utf-8") as fp:
                text = fp.read()
            try:
                idx, parsed = 0, []
                while True:
                    while idx < len(text) and text[idx].isspace():
                        idx += 1
                    if idx >= len(text):
                        break
                    obj, idx = decoder.raw_decode(text, idx)
                    parsed.append(obj)
                docs.extend(parsed)
            except ValueError:
                docs.extend(d for d in yaml.safe_load_all(text) if isinstance(d, dict))
    return docs


def split_image(ref):
    """Split repo[:tag][@digest] into (repository, tag, digest)."""
    digest = ""
    if "@" in ref:
        ref, digest = ref.split("@", 1)
    tag = ""
    last = ref.rsplit("/", 1)[-1]
    if ":" in last:
        ref, tag = ref.rsplit(":", 1)
    return ref, tag, digest


def embedded_csv(bundle):
    for prop in bundle.get("properties") or []:
        if prop.get("type") != "olm.bundle.object":
            continue
        try:
            obj = json.loads(base64.b64decode((prop.get("value") or {}).get("data") or ""))
        except (ValueError, TypeError):
            continue
        if obj.get("kind") == "ClusterServiceVersion":
            return obj
    return None


def bundle_images(bundle):
    """relatedImages plus deployment/env images from an embedded CSV (if any)."""
    rows, seen = [], set()

    def add(name, image, source):
        image = (image or "").strip()
        if not image or (name, image) in seen:
            return
        seen.add((name, image))
        repository, tag, digest = split_image(image)
        rows.append({
            "name": name or "",
            "image": image,
            "repository": repository,
            "tag": tag,
            "digest": digest,
            "source": source,
        })

    for item in bundle.get("relatedImages") or []:
        add(item.get("name"), item.get("image"), "relatedImages")

    csv = embedded_csv(bundle) or {}
    spec = csv.get("spec") or {}
    for item in spec.get("relatedImages") or []:
        add(item.get("name"), item.get("image"), "relatedImages")
    for dep in ((spec.get("install") or {}).get("spec") or {}).get("deployments") or []:
        dep_name = dep.get("name") or "deployment"
        pod_spec = ((dep.get("spec") or {}).get("template") or {}).get("spec") or {}
        for kind in ("containers", "initContainers"):
            for container in pod_spec.get(kind) or []:
                cname = container.get("name") or kind
                add("%s/%s" % (dep_name, cname), container.get("image"), "csv-deployment")
                for env in container.get("env") or []:
                    if "IMAGE" in (env.get("name") or "").upper():
                        add(env.get("name"), env.get("value"), "csv-env")

    rows.sort(key=lambda r: (r["source"] != "relatedImages", r["repository"], r["name"]))
    return rows


def bundle_version(bundle):
    for prop in bundle.get("properties") or []:
        if prop.get("type") == "olm.package":
            return (prop.get("value") or {}).get("version") or ""
    return ""


def created_at(bundle):
    """YYYY-MM-DD from the embedded CSV's createdAt annotation, if present."""
    csv = embedded_csv(bundle) or {}
    value = ((csv.get("metadata") or {}).get("annotations") or {}).get("createdAt") or ""
    match = re.match(r"\d{4}-\d{2}-\d{2}", str(value))
    return match.group(0) if match else ""


def build_record(package, channel, entry, bundle, ocp_version):
    name = entry["name"]
    epoch = csv_epoch(name)
    record = {
        "csv_name": name,
        "package": package,
        "channel": channel,
        "operator_version": bundle_version(bundle),
        "build_date": (
            datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).strftime("%Y-%m-%d")
            if epoch else created_at(bundle)
        ),
        "replaces": entry.get("replaces") or "",
        "skip_range": entry.get("skipRange") or "",
        "skips": entry.get("skips") or [],
        "bundle_image": bundle.get("image") or "",
        "ocp_indexes": [ocp_version],
        "images": bundle_images(bundle),
    }
    return record


def write_record(path, record, ocp_version):
    """Merge with an existing file; write only on change.

    ocp_indexes accumulates every index the CSV was seen in. Indexes can disagree on the
    other fields (e.g. `replaces`), so those always come from the newest index the CSV was
    seen in. That keeps the result the same no matter which indexes this run scanned.
    """
    existing = None
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fp:
            existing = yaml.safe_load(fp) or {}
        seen = existing.get("ocp_indexes") or []
        merged = sorted(set(seen) | set(record["ocp_indexes"]), key=version_key)
        newest_seen = max(seen, key=version_key) if seen else None
        if newest_seen and version_key(newest_seen) > version_key(ocp_version):
            record = dict(existing)
        record["ocp_indexes"] = merged
    if existing == record:
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fp:
        fp.write("---\n")
        yaml.safe_dump(record, fp, sort_keys=False, default_flow_style=False, width=1000)
    return True


def main():
    module = AnsibleModule(
        argument_spec=dict(
            ocp_version=dict(type="str", required=True),
            channels=dict(type="list", elements="str", default=[]),
            channel_pattern=dict(type="str", default="^stable-"),
            channel_min_version=dict(type="str", default=""),
            channel_exclude=dict(type="list", elements="str", default=[]),
            channels_dir=dict(type="path", required=True),
            index_cache_dir=dict(type="path", required=True),
            refresh_index=dict(type="bool", default=True),
            index_digest=dict(type="str", default=""),
            skip_unchanged=dict(type="bool", default=True),
            state_file=dict(type="path"),
            index_repository=dict(type="str", default="redhat/redhat-operator-index"),
            package_name=dict(type="str", default="ansible-automation-platform-operator"),
            registry=dict(type="str", default="registry.redhat.io"),
        ),
        supports_check_mode=False,
    )
    p = module.params
    if p["channel_min_version"] and not channel_version(p["channel_min_version"]):
        module.fail_json(msg="channel_min_version must look like <major>.<minor>, got %r" % p["channel_min_version"])
    try:
        re.compile(p["channel_pattern"])
    except re.error as exc:
        module.fail_json(msg="Invalid channel_pattern %r: %s" % (p["channel_pattern"], exc))
    os.makedirs(p["index_cache_dir"], exist_ok=True)

    ver = p["ocp_version"]
    tag_ref = "%s/%s:v%s" % (p["registry"], p["index_repository"], ver)
    digest = p["index_digest"] or index_digest(tag_ref)
    fingerprint = selection_fingerprint(p)
    state = load_state(p["state_file"])
    prev = state.get(ver) or {}

    result = dict(
        changed=False,
        ocp_version=ver,
        index_digest=digest,
        index_status="",
        channels_found=[],
        channels_missing=list(p["channels"]),
        channels_available=[],
        csvs_seen=0,
        csvs_written=[],
    )

    if (p["skip_unchanged"] and digest and prev.get("digest") == digest
            and prev.get("fingerprint") == fingerprint):
        result.update(
            index_status="unchanged",
            channels_available=prev.get("channels_available") or [],
            channels_found=prev.get("channels_found") or [],
        )
        result["channels_missing"] = [c for c in p["channels"] if c not in result["channels_found"]]
        module.exit_json(**result)

    # Pull by digest so the catalog read matches the digest recorded in the state file.
    image = "%s/%s@%s" % (p["registry"], p["index_repository"], digest) if digest else tag_ref
    pkg_dir, status = extract_package_catalog(
        module, image, ver, p["package_name"], p["index_cache_dir"], p["refresh_index"],
    )
    result["index_status"] = status
    if pkg_dir is None:
        module.exit_json(**result)

    docs = load_fbc_docs(pkg_dir)
    bundles = {
        d.get("name"): d for d in docs
        if d.get("schema") == "olm.bundle" and d.get("package") == p["package_name"]
    }
    channels = {
        d.get("name"): d for d in docs
        if d.get("schema") == "olm.channel" and d.get("package") == p["package_name"]
    }

    result["channels_available"] = sorted(channels)
    wanted = select_channels(
        channels, p["channels"], p["channel_pattern"], p["channel_exclude"], p["channel_min_version"],
    )
    for channel in wanted:
        ch = channels.get(channel)
        if ch is None:
            continue
        result["channels_found"].append(channel)
        if channel in result["channels_missing"]:
            result["channels_missing"].remove(channel)
        for entry in ch.get("entries") or []:
            bundle = bundles.get(entry.get("name"))
            if bundle is None:
                module.warn("Bundle %s listed in %s but not in catalog" % (entry.get("name"), channel))
                continue
            result["csvs_seen"] += 1
            record = build_record(p["package_name"], channel, entry, bundle, ver)
            path = os.path.join(p["channels_dir"], channel, "vars", "%s.yml" % record["csv_name"])
            if write_record(path, record, ver):
                result["csvs_written"].append(path)

    # Only remember freshly pulled indexes: a cached extract may be older than `digest`.
    if status == "ok" and digest:
        state[ver] = {
            "digest": digest,
            "fingerprint": fingerprint,
            "channels_available": result["channels_available"],
            "channels_found": result["channels_found"],
        }
        save_state(p["state_file"], state)

    result["changed"] = bool(result["csvs_written"])
    module.exit_json(**result)


if __name__ == "__main__":
    main()
