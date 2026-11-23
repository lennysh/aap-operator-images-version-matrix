#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r'''
---
module: aap_operator_index_discover
short_description: Discover which Red Hat operator index tags (v<major>.<minor>) exist
description:
  - Probes C(<registry>/<index_repository>:v<major>.<minor>) tags with C(skopeo inspect),
    starting at I(min_version) and walking forward one minor at a time.
  - After I(max_misses) consecutive missing minors it moves to the next major (C(<major+1>.0)).
    Discovery stops when a whole major yields no tags.
  - Listing every tag in the index repository is far too slow (thousands of tags), so tags
    are probed directly instead.
  - A registry or authentication error (anything other than C(manifest unknown)) fails the
    module, so an outage cannot quietly shrink the list of indexes that get scanned.
version_added: "1.1.0"
options:
  min_version:
    description: First index version to probe (e.g. C(4.11)).
    required: true
    type: str
  exclude:
    description: Versions to leave out of the result even when they exist.
    required: false
    type: list
    elements: str
    default: []
  max_misses:
    description: Consecutive missing minors before moving on to the next major.
    required: false
    type: int
    default: 2
  registry:
    description: Container registry host.
    required: false
    type: str
    default: registry.redhat.io
  index_repository:
    description: Operator index repository path within the registry.
    required: false
    type: str
    default: redhat/redhat-operator-index
author:
  - lennysh
'''

EXAMPLES = r'''
- name: Discover operator index versions
  aap_operator_index_discover:
    min_version: "4.11"
  register: discovered
'''

RETURN = r'''
versions:
  description: Index versions that exist, oldest first (e.g. C(["4.11", "4.12"])).
  type: list
  returned: always
digests:
  description: Map of version to the tag's current manifest digest.
  type: dict
  returned: always
probed:
  description: Number of tags probed.
  type: int
  returned: always
'''

import subprocess
import time

from ansible.module_utils.basic import AnsibleModule

ATTEMPTS = 3


def probe(image):
    """Return (digest, None) if the tag exists, (None, None) if missing, (None, err) on error."""
    cmd = ["skopeo", "inspect", "--no-tags", "--format", "{{.Digest}}", "docker://%s" % image]
    err = ""
    for attempt in range(ATTEMPTS):
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode == 0:
            return proc.stdout.strip(), None
        err = " ".join(proc.stderr.split()) or "rc=%d" % proc.returncode
        if "manifest unknown" in err:
            return None, None
        time.sleep(2 * (attempt + 1))
    return None, err


def parse_version(text):
    major, minor = str(text).split(".", 1)
    return int(major), int(minor)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            min_version=dict(type="str", required=True),
            exclude=dict(type="list", elements="str", default=[]),
            max_misses=dict(type="int", default=2),
            registry=dict(type="str", default="registry.redhat.io"),
            index_repository=dict(type="str", default="redhat/redhat-operator-index"),
        ),
        supports_check_mode=True,
    )
    p = module.params
    try:
        major, minor = parse_version(p["min_version"])
    except ValueError:
        module.fail_json(msg="min_version must look like <major>.<minor>, got %r" % p["min_version"])
    exclude = set(str(v) for v in p["exclude"])
    base = "%s/%s" % (p["registry"], p["index_repository"])

    versions, digests, probed = [], {}, 0
    while True:
        misses, major_found = 0, False
        while misses < max(1, p["max_misses"]):
            version = "%d.%d" % (major, minor)
            digest, err = probe("%s:v%s" % (base, version))
            probed += 1
            if err:
                module.fail_json(
                    msg="Could not check %s:v%s (is the registry login valid?): %s" % (base, version, err),
                    versions=versions, digests=digests, probed=probed,
                )
            if digest:
                major_found, misses = True, 0
                if version not in exclude:
                    versions.append(version)
                    digests[version] = digest
            else:
                misses += 1
            minor += 1
        if not major_found:
            break
        major, minor = major + 1, 0

    if not versions:
        module.fail_json(msg="No operator index tags found at or above v%s in %s" % (p["min_version"], base))
    module.exit_json(changed=False, versions=versions, digests=digests, probed=probed)


if __name__ == "__main__":
    main()
