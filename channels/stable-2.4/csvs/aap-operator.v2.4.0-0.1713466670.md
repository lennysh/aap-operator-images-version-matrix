# `aap-operator.v2.4.0-0.1713466670`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1713466670` |
| **Build date** | 2024-04-18 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1711590540`](./aap-operator.v2.4.0-0.1711590540.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:f13d84e84c99db0e23dd0516eb3d839b9e9b8c92fc1e08890d7d078465a25fc0` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.6 | 8 | 2024-04-18 | `sha256:ed8ecef044b4` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 134 | 2024-04-18 | `sha256:8b8e52153a45` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 14 | 2024-04-18 | `sha256:820f84af4734` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 137 | 2024-04-18 | `sha256:cd42dc863114` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 15 | 2024-04-18 | `sha256:0b8524beffd1` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 610 | 2024-04-18 | `sha256:a80619158faa` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 626 | 2024-04-18 | `sha256:e018689bbc42` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 626 | 2024-04-18 | `sha256:e018689bbc42` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 626 | 2024-04-18 | `sha256:e018689bbc42` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 15 | 2024-04-18 | `sha256:07dc569521e6` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 127 | 2024-04-18 | `sha256:1fd69578b918` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 12 | 2024-04-18 | `sha256:0fabe9bbc69f` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 120 | 2024-04-18 | `sha256:d5c7a09e2e0f` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 142 | 2024-04-18 | `sha256:48564fe9d357` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1416 | 2024-04-18 | `sha256:f13d84e84c99` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403241038.p0.gb17014f.assembly.stream.el8 | 2024-03-24 | `sha256:8bffe5b4588b` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161 | 2024-03-27 | `sha256:f30dbf77b075` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161 | 2024-03-27 | `sha256:f30dbf77b075` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161 | 2024-03-27 | `sha256:f30dbf77b075` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.6 | 8 | 2024-04-18 | `sha256:ed8ecef044b4` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 134 | 2024-04-18 | `sha256:8b8e52153a45` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 14 | 2024-04-18 | `sha256:820f84af4734` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 137 | 2024-04-18 | `sha256:cd42dc863114` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 15 | 2024-04-18 | `sha256:0b8524beffd1` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 610 | 2024-04-18 | `sha256:a80619158faa` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 626 | 2024-04-18 | `sha256:e018689bbc42` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 626 | 2024-04-18 | `sha256:e018689bbc42` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 626 | 2024-04-18 | `sha256:e018689bbc42` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 15 | 2024-04-18 | `sha256:07dc569521e6` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 127 | 2024-04-18 | `sha256:1fd69578b918` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 12 | 2024-04-18 | `sha256:0fabe9bbc69f` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 120 | 2024-04-18 | `sha256:d5c7a09e2e0f` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 142 | 2024-04-18 | `sha256:48564fe9d357` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403241038.p0.gb17014f.assembly.stream.el8 | 2024-03-24 | `sha256:8bffe5b4588b` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403241038.p0.gb17014f.assembly.stream.el8 | 2024-03-24 | `sha256:8bffe5b4588b` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403241038.p0.gb17014f.assembly.stream.el8 | 2024-03-24 | `sha256:8bffe5b4588b` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403241038.p0.gb17014f.assembly.stream.el8 | 2024-03-24 | `sha256:8bffe5b4588b` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161 | 2024-03-27 | `sha256:f30dbf77b075` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161 | 2024-03-27 | `sha256:f30dbf77b075` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161 | 2024-03-27 | `sha256:f30dbf77b075` |

## Image pull specs

<details><summary>All 17 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:8b8e52153a459ccc145fae0e6adc9638d31efe3300106b6b50bee9cdc7ed11d6
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:ed8ecef044b429491f9cdb2a6fd35b708c9c4ceaec7a9723246d03440abae480
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:cd42dc86311477f5b83e8da9ccd14c2b0aa437dfc28b448cd5a25febfcc0e379
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:820f84af4734e1bbdc8cc1966ee6604ee5c9985b32e70f4a1d0c2fbd19f36427
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:0b8524beffd10aef87572a0728b621efa8f286bcd4e4bf2480e5eeca0e09551b
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:a80619158faa6f9c16123e930204681811345765cae7e6dea8021a9ae8988d0d
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:e018689bbc42d69447117a0ca10d963fb4686999e008ac0cc01431e382268267
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:1fd69578b9186dd3e432ab1181cc8c76e48b8ec00084a39a4a5e5fb02d462dd5
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:07dc569521e63cb987b3e605e98a0200ffb0029fea585afbc3c0bc6f271e2389
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:0fabe9bbc69fdd8169ed03bd91b83193c2994d46309f43f252008e41505fd10f
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:d5c7a09e2e0f14b76bd9f6dda444e4abaee8a288f61c1a86f771aadc68dbecf0
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:48564fe9d35745ae8a1f8c1caa6db058251f0fb7a38303ad3cf9322b39cbe346
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:f13d84e84c99db0e23dd0516eb3d839b9e9b8c92fc1e08890d7d078465a25fc0
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:8bffe5b4588ba03e77a0d16e82d6eef1f9c2e9991e5dc849924f43f3c269e4df
registry.redhat.io/rhel8/postgresql-13@sha256:f490e1e409f89704d97c7a47b4f0d7610830f8581ae86871ce7aa99dd5cb52b0
registry.redhat.io/rhel8/redis-6@sha256:07091ba15a3f17d7dfd6c5e2dd5b951a338cfd833106f057c24993d57595bd92
registry.redhat.io/ubi8/ubi-minimal@sha256:f30dbf77b075215f6c827c269c073b5e0973e5cea8dacdf7ecb6a19c868f37f2
```

</details>
