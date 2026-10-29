# `aap-operator.v2.4.0-0.1750878254`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1750878254` |
| **Build date** | 2025-06-25 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1749069693`](./aap-operator.v2.4.0-0.1749069693.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:d4c1df74974cfee738ca29ce541d6bafc421e3ca062d7e61c9901b8c7643d3cd` |
| **Seen in OCP operator indexes** | 4.12–4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.24 | 1 | 2025-06-25 | `sha256:45afcbfa6f15` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 177 | 2025-06-25 | `sha256:06e590c8de0d` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 40 | 2025-06-25 | `sha256:1b4d8b230db9` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 177 | 2025-06-25 | `sha256:b59082f91995` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 38 | 2025-06-25 | `sha256:a9aa2d324e01` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 933 | 2025-06-25 | `sha256:6239a00d64e6` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1045 | 2025-06-25 | `sha256:b75ba4a5874f` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1045 | 2025-06-25 | `sha256:b75ba4a5874f` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1045 | 2025-06-25 | `sha256:b75ba4a5874f` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.4 | 2 | 2025-06-25 | `sha256:d0fd71aab7d6` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 177 | 2025-06-25 | `sha256:c991d049bc32` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.4 | 2 | 2025-06-25 | `sha256:e5408b80cae2` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 13 | 2025-06-25 | `sha256:8d57f7b5720f` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 46 | 2025-06-25 | `sha256:8e36d54f8b21` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 173 | 2025-06-25 | `sha256:6d7ee75503c1` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 213 | 2025-06-25 | `sha256:cf56f54e3dc7` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2625 | 2025-06-25 | `sha256:d4c1df74974c` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202504220035.p0.g9308e7f.assembly.stream.el8 | 2025-04-22 | `sha256:bb84ead43704` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749685126 | 2025-06-11 | `sha256:3ee676ec769c` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749685126 | 2025-06-11 | `sha256:3ee676ec769c` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749685126 | 2025-06-11 | `sha256:3ee676ec769c` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295.1749680713 | 2025-06-11 | `sha256:fceb1f445ccd` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295.1749680713 | 2025-06-11 | `sha256:fceb1f445ccd` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295.1749680713 | 2025-06-11 | `sha256:fceb1f445ccd` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:06e590c8de0d9044325678c1b4113fe61f19340e6431f498d01ab1e246678f7d
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:45afcbfa6f155086b0f5f9fed7d5282bd654caac615b59dc7efe0e85b187a645
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:b59082f919953f13888d3bf863a86e5ff3a11b145156a0247cc0bc05d29063a2
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:1b4d8b230db9dedd1f56628b7d11a694946dfe425c9ec0a52fa965adcc79fe8b
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:a9aa2d324e01b0ad80595b1c2bd14c2c8c1c111627cd6209f3c936ccb6561803
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:6239a00d64e6b30439f21a66a34cf3e4676e36dac8f6a21f380840c709025c12
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:b75ba4a5874f607f7a1bde706038cd718c48d50afde77417dd756d9b81e9f03d
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:c991d049bc32a7240ce4a6449157c4cc6e6d5ef85bc098508032e97310b0400b
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:d0fd71aab7d6432ecbbc74170e1cd4e99bf0eee945933b587e217c40baa4e126
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:e5408b80cae2c1644226901453c6a24c2b6626c34daedd95f7beac6a94e11744
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:8e36d54f8b21c87a378ab749f940aa6330f7c76925973dd45e1b661ca52f73c2
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:8d57f7b5720f9832cd134c4fb4a6d1faf8b6a51f4e277df4204c29b7f8a557d1
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:6d7ee75503c168821c3fb9a95655a0f99d80dec128bb1317c3e270a3c59cd711
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:cf56f54e3dc7133374a79607646944bffd11a75480dce5233ed1964a67877bba
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:d4c1df74974cfee738ca29ce541d6bafc421e3ca062d7e61c9901b8c7643d3cd
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:bb84ead437042603254efcb703442be8500a9450b10bbcaaee81b48a6ed869ea
registry.redhat.io/rhel8/postgresql-15@sha256:ffdee937e9726f3214bd3ba2070487291b0e43d53301ca16900b8af905c680d5
registry.redhat.io/rhel8/redis-6@sha256:3ee676ec769c5f5ece69ad14f66b96a99db603982628510eb878bb4b5ca61371
registry.redhat.io/ubi8/ubi-minimal@sha256:fceb1f445ccd61a60d91d404fd76dbebaf3403e6cc2219cf6d6af4fd4bf7df6a
```

</details>
