# `aap-operator.v2.4.0-0.1717558474`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1717558474` |
| **Build date** | 2024-06-05 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1715898994`](./aap-operator.v2.4.0-0.1715898994.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:9d6d2a0083c1d127809ccf202c42164f4ac8cd155e7fee68b9feabb9d5eeae70` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.7 | 10 | 2024-06-04 | `sha256:d04c89afbab8` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 138 | 2024-06-04 | `sha256:13752160edb2` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 6 | 2024-06-04 | `sha256:819c65ac4fe7` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 141 | 2024-06-04 | `sha256:e7b32cee0439` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 5 | 2024-06-04 | `sha256:6c58da5aaae0` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 651 | 2024-06-04 | `sha256:761ecc0c732b` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 679 | 2024-06-04 | `sha256:484e6a5f1b6d` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 679 | 2024-06-04 | `sha256:484e6a5f1b6d` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 679 | 2024-06-04 | `sha256:484e6a5f1b6d` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 8 | 2024-06-04 | `sha256:487dc86d7168` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 135 | 2024-06-04 | `sha256:dd6b4f592a29` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 7 | 2024-06-04 | `sha256:76a27bc25b5e` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 126 | 2024-06-04 | `sha256:13d57bed503c` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 155 | 2024-06-04 | `sha256:f6abf083bdbe` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1609 | 2024-06-05 | `sha256:9d6d2a0083c1` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1716485371 | 2024-05-23 | `sha256:8d43bbe3dcba` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1716485371 | 2024-05-23 | `sha256:8d43bbe3dcba` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1716485371 | 2024-05-23 | `sha256:8d43bbe3dcba` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1716485372 | 2024-05-23 | `sha256:c4f52544b8d6` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1716485372 | 2024-05-23 | `sha256:c4f52544b8d6` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1716485372 | 2024-05-23 | `sha256:c4f52544b8d6` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1716497715 | 2024-05-23 | `sha256:9e458f41ff88` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1716497715 | 2024-05-23 | `sha256:9e458f41ff88` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1716497715 | 2024-05-23 | `sha256:9e458f41ff88` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.7 | 10 | 2024-06-04 | `sha256:d04c89afbab8` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 138 | 2024-06-04 | `sha256:13752160edb2` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 6 | 2024-06-04 | `sha256:819c65ac4fe7` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 141 | 2024-06-04 | `sha256:e7b32cee0439` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 5 | 2024-06-04 | `sha256:6c58da5aaae0` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 651 | 2024-06-04 | `sha256:761ecc0c732b` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 679 | 2024-06-04 | `sha256:484e6a5f1b6d` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 679 | 2024-06-04 | `sha256:484e6a5f1b6d` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 679 | 2024-06-04 | `sha256:484e6a5f1b6d` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 8 | 2024-06-04 | `sha256:487dc86d7168` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 135 | 2024-06-04 | `sha256:dd6b4f592a29` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 7 | 2024-06-04 | `sha256:76a27bc25b5e` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 126 | 2024-06-04 | `sha256:13d57bed503c` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 155 | 2024-06-04 | `sha256:f6abf083bdbe` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1716485371 | 2024-05-23 | `sha256:8d43bbe3dcba` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1716485371 | 2024-05-23 | `sha256:8d43bbe3dcba` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1716485371 | 2024-05-23 | `sha256:8d43bbe3dcba` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1716485372 | 2024-05-23 | `sha256:c4f52544b8d6` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1716485372 | 2024-05-23 | `sha256:c4f52544b8d6` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1716485372 | 2024-05-23 | `sha256:c4f52544b8d6` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1716497715 | 2024-05-23 | `sha256:9e458f41ff88` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1716497715 | 2024-05-23 | `sha256:9e458f41ff88` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1716497715 | 2024-05-23 | `sha256:9e458f41ff88` |

## Image pull specs

<details><summary>All 17 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:13752160edb2d05fb8b11ece54707d8296fca75185706492acc76d6c96c6aca1
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:d04c89afbab8b0c45bc3dcda92e8472c00eca052a3da37ffe88a8b6f8313c0d4
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:e7b32cee0439a90ef56636bada022306f39978a96061fbc22982f9212f0c441a
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:819c65ac4fe7ec30479f1ab43bd1c9c78f465b4165b8829c0a822c18d08afb4b
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:6c58da5aaae09dcbd3900024c2e06cb0c42af81968640b348861fe5a313ab4f3
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:761ecc0c732b6cdbd78c81c998768d77839c8f3129e2196b4fcbc30b6d90e185
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:484e6a5f1b6d81e457de5d1041bca0899bb5829495327383c0177b498dca14a4
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:dd6b4f592a292809477a38dbe65105372fc46b03d60d9f88a8913559e30e74f6
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:487dc86d71684ffc6698bf5fa106c82ee440b5192c645be09dd167754054353d
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:76a27bc25b5ef9f49a5b0f2a8508fda367bce5c8070f97c8f6461d0d64c6ef6e
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:13d57bed503ce6993b9d4ff845847b59feda2d6396c5c790b8c8f021544dbb31
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:f6abf083bdbee2218b03eccb69778563b4387db4130e6ccb03c715a5b9eb46e2
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:9d6d2a0083c1d127809ccf202c42164f4ac8cd155e7fee68b9feabb9d5eeae70
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:e31a70c7e16952634f87a124c5a15e0e8507856b6b298d0cd030003cd92b1517
registry.redhat.io/rhel8/postgresql-13@sha256:8d43bbe3dcba74e5d3850acbf89e389eafd71c477ad4fc1e6474fb1faa56a1b9
registry.redhat.io/rhel8/redis-6@sha256:c4f52544b8d60da6cb494f560a88aa18adc2176da4f6a640b621649ec42a7a27
registry.redhat.io/ubi8/ubi-minimal@sha256:9e458f41ff8868ceae00608a6fff35b45fd8bbe967bf8655e5ab08da5964f4d0
```

</details>
