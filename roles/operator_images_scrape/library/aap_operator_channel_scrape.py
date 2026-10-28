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
  - Use in an Ansible loop over OCP index tags for live progress.
version_added: "1.0.0"
options:
  ocp_version:
    description: OCP operator index tag (e.g. 4.18).
    required: true
    type: str
  channels:
    description: OLM channel names to dump.
    required: true
    type: list
    elements: str
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
channels_found:
  description: Requested channels present in this index.
  type: list
  returned: always
channels_missing:
  description: Requested channels absent from this index.
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
import json
import os
import re
import shutil
import subprocess
import tempfile

import yaml

from ansible.module_utils.basic import AnsibleModule


def version_key(version):
    return tuple(int(p) for p in str(version).split(".") if p.isdigit())


def csv_epoch(csv_name):
    """Trailing build timestamp of CSV names like aap-operator.v2.6.0-0.1777410689."""
    match = re.search(r"-0\.(\d{10})$", csv_name)
    return int(match.group(1)) if match else None


def extract_package_catalog(module, ocp_version, package, registry, cache_dir, refresh):
    """Return path to <cache>/ocp-<ver>/<package>, pulling the index if needed."""
    ocp_dir = os.path.join(cache_dir, "ocp-%s" % ocp_version)
    pkg_dir = os.path.join(ocp_dir, package)
    if os.path.isdir(pkg_dir) and not refresh:
        return pkg_dir, "cached"

    image = "%s/redhat/redhat-operator-index:v%s" % (registry, ocp_version)
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
        tmp_dir = tempfile.mkdtemp(dir=cache_dir if os.path.isdir(cache_dir) else None)
        cp = subprocess.run(
            "podman cp %s:/configs/%s - | tar -x -C %s" % (container_id, package, tmp_dir),
            shell=True,
            capture_output=True,
            text=True,
        )
        subprocess.run(["podman", "rm", "-v", container_id], capture_output=True)
        extracted = os.path.join(tmp_dir, package)
        if cp.returncode != 0 or not os.path.isdir(extracted):
            module.warn("Package %s not found in %s" % (package, image))
            status = "package_not_found"
        else:
            shutil.rmtree(pkg_dir, ignore_errors=True)
            os.makedirs(ocp_dir, exist_ok=True)
            shutil.move(extracted, pkg_dir)
        shutil.rmtree(tmp_dir, ignore_errors=True)

    # Index images are large; do not leave them in local storage.
    subprocess.run(["podman", "rmi", image], capture_output=True)
    return (pkg_dir if status == "ok" else None), status


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
            if epoch else ""
        ),
        "replaces": entry.get("replaces") or "",
        "skip_range": entry.get("skipRange") or "",
        "skips": entry.get("skips") or [],
        "bundle_image": bundle.get("image") or "",
        "ocp_indexes": [ocp_version],
        "images": bundle_images(bundle),
    }
    return record


def write_record(path, record):
    """Merge ocp_indexes with an existing file; write only on change."""
    existing = None
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as fp:
            existing = yaml.safe_load(fp) or {}
        merged = set(existing.get("ocp_indexes") or []) | set(record["ocp_indexes"])
        record["ocp_indexes"] = sorted(merged, key=version_key)
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
            channels=dict(type="list", elements="str", required=True),
            channels_dir=dict(type="path", required=True),
            index_cache_dir=dict(type="path", required=True),
            refresh_index=dict(type="bool", default=True),
            package_name=dict(type="str", default="ansible-automation-platform-operator"),
            registry=dict(type="str", default="registry.redhat.io"),
        ),
        supports_check_mode=False,
    )
    p = module.params
    os.makedirs(p["index_cache_dir"], exist_ok=True)

    pkg_dir, status = extract_package_catalog(
        module, p["ocp_version"], p["package_name"], p["registry"],
        p["index_cache_dir"], p["refresh_index"],
    )
    result = dict(
        changed=False,
        ocp_version=p["ocp_version"],
        index_status=status,
        channels_found=[],
        channels_missing=list(p["channels"]),
        csvs_seen=0,
        csvs_written=[],
    )
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

    for channel in p["channels"]:
        ch = channels.get(channel)
        if ch is None:
            continue
        result["channels_found"].append(channel)
        result["channels_missing"].remove(channel)
        for entry in ch.get("entries") or []:
            bundle = bundles.get(entry.get("name"))
            if bundle is None:
                module.warn("Bundle %s listed in %s but not in catalog" % (entry.get("name"), channel))
                continue
            result["csvs_seen"] += 1
            record = build_record(p["package_name"], channel, entry, bundle, p["ocp_version"])
            path = os.path.join(p["channels_dir"], channel, "vars", "%s.yml" % record["csv_name"])
            if write_record(path, record):
                result["csvs_written"].append(path)

    result["changed"] = bool(result["csvs_written"])
    module.exit_json(**result)


if __name__ == "__main__":
    main()
