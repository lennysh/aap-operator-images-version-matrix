# `aap-operator.v2.4.0-0.1758080293`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1758080293` |
| **Build date** | 2025-09-17 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1755833968`](./aap-operator.v2.4.0-0.1755833968.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:40b961a28ea9761c052a5cd17d2452fb72ea4786a92e13a0a1b589c7de31bf26` |
| **Seen in OCP operator indexes** | 4.12–4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.25 | 3 | 2025-09-16 | `sha256:04fb5cb6b0d7` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 181 | 2025-09-16 | `sha256:5253c9fd587f` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 44 | 2025-09-16 | `sha256:bfd13d6b39c5` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 181 | 2025-09-16 | `sha256:5b957031609c` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 42 | 2025-09-16 | `sha256:d229d4e09b2b` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 965 | 2025-09-17 | `sha256:7670e41037f0` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1088 | 2025-09-17 | `sha256:f1384eb558f7` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1088 | 2025-09-17 | `sha256:f1384eb558f7` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1088 | 2025-09-17 | `sha256:f1384eb558f7` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.5 | 3 | 2025-09-16 | `sha256:7ae8db2b5d12` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 181 | 2025-09-16 | `sha256:3c28a1326ecb` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 3 | 2025-09-17 | `sha256:6ff1f602f0d9` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 18 | 2025-09-16 | `sha256:cccb4db08735` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 50 | 2025-09-16 | `sha256:e20106a8a04a` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 177 | 2025-09-16 | `sha256:b120e6a5ef37` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 217 | 2025-09-17 | `sha256:e14286dc9605` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2800 | 2025-09-17 | `sha256:40b961a28ea9` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202508061316.p2.g9308e7f.assembly.stream.el8 | 2025-08-06 | `sha256:6a9e10a4aad5` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1756313707 | 2025-08-27 | `sha256:b70af4767a5b` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1756253827 | 2025-08-27 | `sha256:72ee6edb5cc4` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1756253827 | 2025-08-27 | `sha256:72ee6edb5cc4` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1756253827 | 2025-08-27 | `sha256:72ee6edb5cc4` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1756195339 | 2025-08-26 | `sha256:43dde01be4e9` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1756195339 | 2025-08-26 | `sha256:43dde01be4e9` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1756195339 | 2025-08-26 | `sha256:43dde01be4e9` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:5253c9fd587ff2ca94d251f2b5fc7f284080adc5eb64643df5299beb2015592f
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:04fb5cb6b0d7c79cf5d4b754fe917224ddfcb2b9a4994462db404c833ed69483
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:5b957031609c8aabf7575e675bc636c1152babc9564d503802301aff4642a404
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:bfd13d6b39c5ec3a67adbafb05a0482328f0b9b97a517b45c093f6c35a3a92d3
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:d229d4e09b2b788d1ba3413ea7ec15374bd1613d507c285ac1ddc10570b9473f
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:7670e41037f023e3fc6ee95d2342787a80077273ab8d30ba6804029ff05b4edc
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:f1384eb558f7da1e4a35d51408b3cf5a5a9be08f4d50503f473b26909bc246fc
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:3c28a1326ecb7495952a5bb8be13b0972a4378af82611b0b9d990c5fa9fa82c3
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:7ae8db2b5d12b619f40db1e581db1e982a695bc1a29a2628222fff09e7c25249
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:6ff1f602f0d9cad201b3addb65acc570a9d527de005ca85fc861d3cb98138710
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:e20106a8a04abd568a4c56861cea39ae444c0bd204bc807ac01f1705e12937d3
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:cccb4db08735551c697a7b2cbf75812f34500e691f9cdbaea02b30edea292e47
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:b120e6a5ef376662b4324f0458eae31627087dc91fc613788143bc3954a15318
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:e14286dc9605be3a8c6cb144d0b2e3f3bb3211129005009e7566ea6c16c91f52
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:40b961a28ea9761c052a5cd17d2452fb72ea4786a92e13a0a1b589c7de31bf26
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:6a9e10a4aad59f7e01dac0407641e9cb5cd5b8ed21f62ea4b2271f8aede4cbec
registry.redhat.io/rhel8/postgresql-15@sha256:b70af4767a5b34c4a67761aa28bee72b4f9cd1ce31245596640371f670d0dbba
registry.redhat.io/rhel8/redis-6@sha256:72ee6edb5cc470104fd29e0ee0876ee5e811b6aac03f0ee2e946a2aad24304e6
registry.redhat.io/ubi8/ubi-minimal@sha256:43dde01be4e94afd22d8d95ee8abcc9f610b4e50aff5bcc141b558c74d4c68b5
```

</details>
