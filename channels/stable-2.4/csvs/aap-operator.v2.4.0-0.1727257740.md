# `aap-operator.v2.4.0-0.1727257740`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1727257740` |
| **Build date** | 2024-09-25 |
| **Previous CSV** | — |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:d3f6ca185cc1abb53f35e936c71d2c9d6a8d8576bedeb8a10b4179e02213bfa3` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.12 | 4 | 2024-09-20 | `sha256:98b9aff840f5` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 154 | 2024-09-20 | `sha256:0d48a2d75a4a` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 21 | 2024-09-20 | `sha256:eb735a785082` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 154 | 2024-09-20 | `sha256:5081c6adad86` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 19 | 2024-09-20 | `sha256:826f9ba32d50` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 732 | 2024-09-20 | `sha256:68c599ebc855` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 808 | 2024-09-26 | `sha256:5a9ca02037b8` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 808 | 2024-09-26 | `sha256:5a9ca02037b8` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 808 | 2024-09-26 | `sha256:5a9ca02037b8` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 24 | 2024-09-20 | `sha256:fd259c077d3c` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 152 | 2024-09-25 | `sha256:a1ff1512eb70` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 23 | 2024-09-20 | `sha256:9572294dc5d2` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.240919 | 2 | 2024-09-24 | `sha256:319323e37969` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 21 | 2024-09-20 | `sha256:6f03d3155a1d` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 145 | 2024-09-20 | `sha256:a9a2fdb874a6` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 189 | 2024-09-26 | `sha256:16bb1e59bab1` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2045 | 2024-09-26 | `sha256:d3f6ca185cc1` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202408260908.p0.ge8e8c84.assembly.stream.el8 | 2024-08-27 | `sha256:f6c37678f1eb` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 204 | 2024-09-17 | `sha256:32a658416c4c` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 204 | 2024-09-17 | `sha256:32a658416c4c` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 204 | 2024-09-17 | `sha256:32a658416c4c` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 204 | 2024-09-17 | `sha256:32a658416c4c` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 203 | 2024-09-17 | `sha256:218f7fa2458c` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 203 | 2024-09-17 | `sha256:218f7fa2458c` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 203 | 2024-09-17 | `sha256:218f7fa2458c` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:0d48a2d75a4aee210e166ce99facc8d27d984c4bd11dab93d2f6da0631bc5a79
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:98b9aff840f58896508617cd7cdb4cc40da309b1121d9392e095b3c429f71019
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:5081c6adad86097bf58a68ae039e1dee6b106b80e61f1922789251d03a869cb4
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:eb735a785082acf3c93ece284704d670a322e160b9d78b455ffacc48cfdb6905
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:826f9ba32d5001fcc0f09a83dd465cb5ad9d26abe30313b31ca5c64163290bef
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:68c599ebc8557464597da0c72f3a34c7710dfdde44733a788396990ae327cd5f
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:5a9ca02037b8f44d190e11dfb82bfeb54217f370f2c5eaa9e0ca61c9b27f7d7e
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:a1ff1512eb70051e2c3b54437fa32c109a3d955438a897deaf69b4996c1ae199
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:fd259c077d3c1d9b58636b875d106bf1436ae7452d6ad9be746a2f14d5bf50c0
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:9572294dc5d229d40551108f6d60005997bb7ea02cdd51e1c71339cb58e0525f
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:6f03d3155a1d8f1d39d4780d2f1fb16a1fc1e38764db5c5095dceb06247a1d7e
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:319323e37969cce7f5f711272fb4989f6d7705dfc2416492f37a7a68a4f2c0af
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:a9a2fdb874a6f264de4458de0fd6ac5c7fa94b7ae674230927e8af8c9e122abc
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:16bb1e59bab1f951a26193d6b7488489252a20d05d35ae2e02ece15356191383
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:d3f6ca185cc1abb53f35e936c71d2c9d6a8d8576bedeb8a10b4179e02213bfa3
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:f6c37678f1eb3279e603f63d2a821b72394c52d25c2ed5058dc29d4caa15d504
registry.redhat.io/rhel8/postgresql-13@sha256:32a658416c4cef3c9a2a476d844f11b3d43e72de0b04f51ce9fab6e9f3918131
registry.redhat.io/rhel8/redis-6@sha256:218f7fa2458c274cc34f79190423e0aba03027f55ef6b3334d916951a668b7b7
registry.redhat.io/ubi8/ubi-minimal@sha256:7583ca0ea52001562bd81a961da3f75222209e6192e4e413ee226cff97dbd48c
```

</details>
