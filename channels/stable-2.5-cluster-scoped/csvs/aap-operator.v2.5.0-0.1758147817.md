# `aap-operator.v2.5.0-0.1758147817`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1758147817` |
| **Build date** | 2025-09-17 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1755835623`](./aap-operator.v2.5.0-0.1755835623.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:961aa224525116fd575cff3a37a6465e9c652ee446927dd2bd03249b29469472` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.20 | 13 | 2025-09-17 | `sha256:3a989f148648` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 194 | 2025-09-17 | `sha256:8d8182e3a87c` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.13 | 7 | 2025-09-17 | `sha256:aed3973eb953` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 190 | 2025-09-17 | `sha256:07aa7e257d04` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.13 | 2 | 2025-09-17 | `sha256:9ab35e80a617` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 969 | 2025-09-17 | `sha256:41f944eb1450` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1091 | 2025-09-17 | `sha256:52d2c73fa201` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1091 | 2025-09-17 | `sha256:52d2c73fa201` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1091 | 2025-09-17 | `sha256:52d2c73fa201` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 72 | 2025-09-17 | `sha256:789d55f355fa` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250924 | 1 | 2025-09-17 | `sha256:697343aaea15` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 254 | 2025-09-17 | `sha256:43e731b9a435` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.8 | 1 | 2025-09-17 | `sha256:9f2867603b97` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 193 | 2025-09-17 | `sha256:503fc7a20e2d` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.8 | 1 | 2025-09-17 | `sha256:e96832efcc03` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250924 | 1 | 2025-09-17 | `sha256:9a37c9739c48` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250924 | 1 | 2025-09-17 | `sha256:ac0de2b7d354` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 148 | 2025-09-17 | `sha256:acc0fcd509ee` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 146 | 2025-09-17 | `sha256:74be9182723b` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 202 | 2025-09-17 | `sha256:ace1d2ab49ba` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1649 | 2025-09-17 | `sha256:961aa2245251` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202508061316.p2.g9308e7f.assembly.stream.el8 | 2025-08-06 | `sha256:6a9e10a4aad5` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1756253827 | 2025-08-27 | `sha256:72ee6edb5cc4` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1756253827 | 2025-08-27 | `sha256:72ee6edb5cc4` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1756253827 | 2025-08-27 | `sha256:72ee6edb5cc4` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1756253827 | 2025-08-27 | `sha256:72ee6edb5cc4` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1756195339 | 2025-08-26 | `sha256:43dde01be4e9` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1756195339 | 2025-08-26 | `sha256:43dde01be4e9` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1756195339 | 2025-08-26 | `sha256:43dde01be4e9` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:8d8182e3a87c55eacc222e71df4a9bf7a2e51102d913a5824cc91e36056d4249
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:3a989f148648a5a62e687058ec3ca772fa22aa10faec89453626d2b17b3fd9c2
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:07aa7e257d04ae0eda6fcaa4af9121f1aece439231fce4f924e6467da91f0022
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:aed3973eb953dda3571260dcf1b33bc7dcbc18c41e3350b8c361b7e635fb9527
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:9ab35e80a6172018ed3f5cd179e0bcb6befc1378583d9e73c3a64a7cf9e8050f
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:41f944eb1450db56c3b14fc7baece8f148d5f10886a57bad730bec60fb28ac04
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:52d2c73fa2015af5f1b9a88ee48085c7c7bab44330fc9f95914f48b58e4b48bc
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:789d55f355fa0d90f9509a912d199123bfc5a4041930a72a8fd4ed1d819f0d84
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:43e731b9a435b3a412108170b4b39e6b6215be51d362a9f03c33fa412e97da53
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:697343aaea153ab22d7efa8f1bb5aed37a55cbb353fc206f4a355e8b878ae418
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:503fc7a20e2dd7de2cb55b9be5f97efa0d2b31f054ce326f23f3a11b4d683e64
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:9f2867603b9747c2fe37862c2c5efac4a4530902f323a8bf7cc0717de4cdb5aa
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:e96832efcc03c6754031cb70f56c808135f62d1b80a882dd6d6fc9e1a4cfc69b
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:9a37c9739c488ccf211ec5efc6debb045223d508c9cb3fa5a8256eca98ff2f0c
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:acc0fcd509eeac46db307ab744dd0a0c26770a93e495cf2ec0ccb61a91c6fbc5
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:ac0de2b7d354eb0c15a6c12861a4de3577a982c84af661fbab25517d8105c085
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:74be9182723b41f87b3d13b3d86b6a9049bba88e2902cc9453264aa8a0f584e4
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:ace1d2ab49ba5ff9f11ab18e8edce27c9e73ae7298bf7335569fa1740a44899b
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:961aa224525116fd575cff3a37a6465e9c652ee446927dd2bd03249b29469472
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:6a9e10a4aad59f7e01dac0407641e9cb5cd5b8ed21f62ea4b2271f8aede4cbec
registry.redhat.io/rhel8/postgresql-15@sha256:b70af4767a5b34c4a67761aa28bee72b4f9cd1ce31245596640371f670d0dbba
registry.redhat.io/rhel8/redis-6@sha256:72ee6edb5cc470104fd29e0ee0876ee5e811b6aac03f0ee2e946a2aad24304e6
registry.redhat.io/ubi8/ubi-minimal@sha256:43dde01be4e94afd22d8d95ee8abcc9f610b4e50aff5bcc141b558c74d4c68b5
```

</details>
