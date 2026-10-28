# `aap-operator.v2.4.0-0.1784076997`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1784076997` |
| **Build date** | 2026-07-15 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1777401109`](./aap-operator.v2.4.0-0.1777401109.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:97663555a04f7c9f82a6dfb5c6d54f19e7a4b9c38f3f44803079422b2a3d0b99` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.34 | 1783932150 | 2026-07-14 | `sha256:538fa03eea43` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-14 | `sha256:0661d2bd9013` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1783932150 | 2026-07-14 | `sha256:8df44ddda9ba` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-14 | `sha256:5ece686710e5` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1784003828 | 2026-07-14 | `sha256:e5e823d1b034` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1783932150 | 2026-07-14 | `sha256:30d181eabfa6` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1783932150 | 2026-07-14 | `sha256:ac9f5e5a5104` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1783932150 | 2026-07-14 | `sha256:ac9f5e5a5104` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1783932150 | 2026-07-14 | `sha256:ac9f5e5a5104` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1783932150 | 2026-07-14 | `sha256:76cc04d7ca6e` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-14 | `sha256:a89471222df7` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1784003828 | 2026-07-14 | `sha256:8ff75ee46e8e` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1783932150 | 2026-07-14 | `sha256:f7ee9943d40e` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-14 | `sha256:69d19cd8c6eb` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-14 | `sha256:7143bbdd4dc7` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1783932150 | 2026-07-14 | `sha256:4b492183884a` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-07-14 | `sha256:97663555a04f` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202606181908.p2.g9308e7f.assembly.stream.el8 | 2026-06-18 | `sha256:5a6d17face86` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1784003696 | 2026-07-14 | `sha256:867820c0cc6c` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1784003696 | 2026-07-14 | `sha256:867820c0cc6c` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1784003696 | 2026-07-14 | `sha256:867820c0cc6c` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1784003696 | 2026-07-14 | `sha256:867820c0cc6c` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1782830420 | 2026-06-30 | `sha256:809190fdfa9d` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1782830420 | 2026-06-30 | `sha256:809190fdfa9d` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1782830420 | 2026-06-30 | `sha256:809190fdfa9d` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1783932150 | 2026-07-13 | `sha256:578b23895314` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1783932150 | 2026-07-13 | `sha256:578b23895314` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1783932150 | 2026-07-13 | `sha256:578b23895314` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:0661d2bd9013757c47d4eb5e14aef872522b5c1ba1d927156d74d1ea6d3e8ab4
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:538fa03eea43fa5734e8992e2f7d79c24b892cba0bed2eb7996c8df7192170ae
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:5ece686710e5dccf16bfa5f3c5a51b9d43996763adb8ed889671bf3ba8b65c18
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:8df44ddda9ba054d2744f7acd23f74b45795b87fd73a0ac609f5480bec07896d
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:e5e823d1b034bb80b391338e68acdbbd9e7080b5427bba8f527f1b71ab6a7458
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:30d181eabfa6b273014510484ba311ff2d1862435b6a086bb8f98bdbb64deecd
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:ac9f5e5a51047ba901ee514eab2f1d273c5d9b5de584ed50b86b08b9744b2ca1
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:a89471222df71436662c9bed248600d8d7bb0601d47609ee794c175a662ec558
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:76cc04d7ca6e99ebe9832a1e56828bb371f23f5138646159502b1ec8a73b06e0
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:8ff75ee46e8e5c5b09f16d63ebccd38af48cc72e422e78e56c3450ac26b2bc45
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:69d19cd8c6ebfa532c5239d654dd8c014843281ca9501e8a35562fca37de24a3
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:f7ee9943d40e25ac15531fe5c84e9c1cc57ddc493958dee32c4d0f138719938a
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:7143bbdd4dc7b388946c108ef304c835b6e3b5ca0af1fa6a3f478edd721f8936
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:4b492183884afb66c6b8a7f1ffdbcea76192c1ca6ecd9a3e357a7daf46bb520b
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:97663555a04f7c9f82a6dfb5c6d54f19e7a4b9c38f3f44803079422b2a3d0b99
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:5a6d17face86396d44f40fec23c6af622ea53f83073369ace4f7560dc11ef6f4
registry.redhat.io/rhel8/postgresql-15@sha256:867820c0cc6cdf67b4fc6525b53a567ab69f8e2742dafacc91ef0024ea6f3e12
registry.redhat.io/rhel8/redis-6@sha256:809190fdfa9dd21fd9526f9b7ef78634e98cda29d730fc9b76f7c0682b5e250d
registry.redhat.io/ubi8/ubi-minimal@sha256:578b238953144445a9b5bb2487eb1d95df4886f98d1f73c4a070b27535f51688
```

</details>
