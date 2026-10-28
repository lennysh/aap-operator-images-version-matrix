#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: aap_image_labels
short_description: Resolve version labels for every image digest referenced by channel CSV vars files
description:
  - Collects every image digest from C(<channels_dir>/*/vars/*.yml).
  - Runs C(skopeo inspect) (no pull) for digests not yet in I(labels_file) and stores
    the C(version), C(release), and build date labels so the markdown can show real
    component versions instead of bare digests.
  - Digests are immutable, so resolved entries are never re-inspected.
version_added: "1.0.0"
options:
  channels_dir:
    description: Root directory holding C(<channel>/vars/*.yml) files.
    required: true
    type: path
  labels_file:
    description: YAML cache mapping image digest (C(sha256:...)) to labels.
    required: true
    type: path
  workers:
    description: Parallel skopeo inspections.
    required: false
    type: int
    default: 8
  retry_failed:
    description:
      - Re-inspect digests that failed on a previous run.
      - Digests the registry reports as C(manifest unknown) are marked permanent and never retried.
    required: false
    type: bool
    default: true
author:
  - lennysh
'''

EXAMPLES = r'''
- name: Resolve image version labels for new digests
  aap_image_labels:
    channels_dir: "{{ playbook_dir }}/channels"
    labels_file: "{{ playbook_dir }}/data/image_labels.yml"
'''

RETURN = r'''
total:
  description: Digests in the labels file after this run.
  type: int
  returned: always
inspected:
  description: Digests inspected this run.
  type: int
  returned: always
failed_refs:
  description: Image refs whose inspection failed this run.
  type: list
  returned: always
'''

import glob
import json
import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

import yaml

from ansible.module_utils.basic import AnsibleModule

ATTEMPTS = 3


def collect_refs(channels_dir):
    """Map digest -> repository@digest (first repository seen is used to inspect)."""
    refs = {}
    for path in glob.glob(os.path.join(channels_dir, "*", "vars", "*.yml")):
        with open(path, "r", encoding="utf-8") as fp:
            record = yaml.safe_load(fp) or {}
        for img in record.get("images") or []:
            if img.get("digest"):
                refs.setdefault(img["digest"], "%s@%s" % (img["repository"], img["digest"]))
    return refs


def inspect(item):
    """Return (digest, labels) for one repository@digest (amd64 for manifest lists)."""
    digest, ref = item
    cmd = [
        "skopeo", "inspect", "--no-tags",
        "--override-os", "linux", "--override-arch", "amd64",
        "docker://%s" % ref,
    ]
    err = ""
    for attempt in range(ATTEMPTS):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            data = json.loads(proc.stdout)
            labels = data.get("Labels") or {}
            return digest, {
                "image": ref,
                "version": labels.get("version") or "",
                "release": labels.get("release") or "",
                "build_date": labels.get("build-date") or data.get("Created") or "",
                "component": labels.get("com.redhat.component") or "",
                "vcs_ref": labels.get("vcs-ref") or "",
            }
        err = " ".join(proc.stderr.split()) or "rc=%d" % proc.returncode
        if "manifest unknown" in err:
            # Digest was removed from the registry; retrying will not help.
            return digest, {"image": ref, "error": "manifest unknown", "permanent": True}
        time.sleep(2 * (attempt + 1))
    return digest, {"image": ref, "error": err}


def main():
    module = AnsibleModule(
        argument_spec=dict(
            channels_dir=dict(type="path", required=True),
            labels_file=dict(type="path", required=True),
            workers=dict(type="int", default=8),
            retry_failed=dict(type="bool", default=True),
        ),
        supports_check_mode=False,
    )
    p = module.params

    labels = {}
    if os.path.exists(p["labels_file"]):
        with open(p["labels_file"], "r", encoding="utf-8") as fp:
            labels = yaml.safe_load(fp) or {}

    refs = collect_refs(p["channels_dir"])
    todo = sorted(
        (digest, ref) for digest, ref in refs.items()
        if digest not in labels or (
            p["retry_failed"] and "error" in labels[digest] and not labels[digest].get("permanent")
        )
    )

    failed = []
    with ThreadPoolExecutor(max_workers=max(1, p["workers"])) as pool:
        for digest, info in pool.map(inspect, todo):
            labels[digest] = info
            if "error" in info:
                failed.append(info["image"])

    changed = bool(todo)
    if changed:
        os.makedirs(os.path.dirname(p["labels_file"]), exist_ok=True)
        with open(p["labels_file"], "w", encoding="utf-8") as fp:
            fp.write("---\n")
            yaml.safe_dump(dict(sorted(labels.items())), fp, sort_keys=False, width=1000)

    for digest, info in labels.items():
        if info.get("image") in failed:
            module.warn("Label lookup failed for %s: %s" % (info["image"], info["error"]))

    module.exit_json(changed=changed, total=len(labels), inspected=len(todo), failed_refs=failed)


if __name__ == "__main__":
    main()
