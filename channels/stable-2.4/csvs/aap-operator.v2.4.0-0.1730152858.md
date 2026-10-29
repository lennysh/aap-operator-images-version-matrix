# `aap-operator.v2.4.0-0.1730152858`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1730152858` |
| **Build date** | 2024-10-28 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1727257740`](./aap-operator.v2.4.0-0.1727257740.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:50d213e6a395435febfa7628b7181790d9f3fc81f811b7860cba1b96d072d3bd` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.12 | 6 | 2024-10-28 | `sha256:4cb01cf3fe5c` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 156 | 2024-10-28 | `sha256:30f0e3e42a9a` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 23 | 2024-10-28 | `sha256:3a7c4f791707` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 156 | 2024-10-28 | `sha256:81e0c71bbc52` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 21 | 2024-10-28 | `sha256:faf1cf6ac2fd` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 759 | 2024-10-28 | `sha256:204525a7026a` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 825 | 2024-10-28 | `sha256:980ef985e4a2` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 825 | 2024-10-28 | `sha256:980ef985e4a2` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 825 | 2024-10-28 | `sha256:980ef985e4a2` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 26 | 2024-10-28 | `sha256:f6a6e5cc6040` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 155 | 2024-10-28 | `sha256:ec0ab494b08a` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 25 | 2024-10-28 | `sha256:97950e08c536` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.240919 | 4 | 2024-10-28 | `sha256:87bcff7fb32c` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 23 | 2024-10-28 | `sha256:ad4470b18a95` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 147 | 2024-10-28 | `sha256:217065542bf1` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 191 | 2024-10-28 | `sha256:e856958a2580` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2118 | 2024-10-28 | `sha256:50d213e6a395` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202409240105.p0.ge8e8c84.assembly.stream.el8 | 2024-09-24 | `sha256:e34f91215898` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 205 | 2024-10-04 | `sha256:8e24215f2a9b` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 205 | 2024-10-04 | `sha256:8e24215f2a9b` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 205 | 2024-10-04 | `sha256:8e24215f2a9b` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 205 | 2024-10-04 | `sha256:8e24215f2a9b` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:30f0e3e42a9aa63bec04b248d67393d343617dfd1ab680be97d4e91c1f1fccab
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:4cb01cf3fe5ce644f8504be0195b17244ea9231e6948e6bb8963bdeaa6116965
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:81e0c71bbc52dd03eff96981a87eda335ac3d7d6a09eb28c9449ee85d8b7f6c4
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:3a7c4f791707d348bbe226298beec690b2cfd8b84bebeb841e2ffda798099990
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:faf1cf6ac2fd63b4859b3dcd3b7369c9490c0398732afd46fb0f7d8571bb07e9
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:204525a7026aea8133cd5205d41dc9e6c205bb198ed171b03531f0f99f86c9c2
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:980ef985e4a28423b8d64666f103c20ab5aa6fc35719145103aaf2adc9755cda
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:ec0ab494b08a759683d8d72e35a4f66eefd242ce557e7a79c549c3c9ee24a5cc
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:f6a6e5cc6040d64a42b6172eaa25c23cba463b165339171e35d9cfa60c0f1b38
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:97950e08c536637ef5897384400e393ea6eec9a66fd17c5160bbd1e51ae7269c
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:ad4470b18a95441ff3fd61b10501e0132146fbe376d2ad91fbfdcbe5ec69236d
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:87bcff7fb32c559667752861df79e62d86e6705855583fe90f99ac24c7d0b2a1
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:217065542bf1feae307cb3841974b8cba0df8d272bcbbd308ea909c69a4442a7
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:e856958a2580fa0d27be9667aeb85c5c8360872df9e930b70dce7caf91ae6d3c
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:50d213e6a395435febfa7628b7181790d9f3fc81f811b7860cba1b96d072d3bd
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:e34f912158985525f6efb3c4b675f20854fc677c867d12fe3cd2e971309428dc
registry.redhat.io/rhel8/postgresql-13@sha256:8e24215f2a9b2fec9e93512913cfcf50ebd39b7e74a35d854bfe22454a8a30e5
registry.redhat.io/rhel8/redis-6@sha256:e76f07cdcbba8faa2ad7e5637045f28197037a68edfb82be23dc331f06beeeca
registry.redhat.io/ubi8/ubi-minimal@sha256:7583ca0ea52001562bd81a961da3f75222209e6192e4e413ee226cff97dbd48c
```

</details>
