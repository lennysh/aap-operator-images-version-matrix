# `aap-operator.v2.4.0-0.1715898994`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1715898994` |
| **Build date** | 2024-05-16 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1713466670`](./aap-operator.v2.4.0-0.1713466670.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:13d898e425a237a1e22145ab4a8ffe9621f79e728d1c9d4d1e3ef11a5001120b` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.6 | 10 | 2024-05-16 | `sha256:ae3a207ff5ec` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 135 | 2024-05-16 | `sha256:04803b79fc15` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 15 | 2024-05-16 | `sha256:cea51f6fa59f` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 138 | 2024-05-16 | `sha256:0a4a64efa46f` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 16 | 2024-05-16 | `sha256:2d85638d62f4` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 636 | 2024-05-16 | `sha256:eff48b9f5c96` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 661 | 2024-05-16 | `sha256:61e294676af1` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 661 | 2024-05-16 | `sha256:61e294676af1` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 661 | 2024-05-16 | `sha256:61e294676af1` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 16 | 2024-05-16 | `sha256:eb83b3fe19f8` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 130 | 2024-05-16 | `sha256:18332377d324` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 13 | 2024-05-16 | `sha256:6fba59839ebc` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 121 | 2024-05-16 | `sha256:5231cb8a8f53` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 148 | 2024-05-16 | `sha256:cd898d9f2d99` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1528 | 2024-05-16 | `sha256:13d898e425a2` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405091536.p0.gb17014f.assembly.stream.el8 | 2024-05-09 | `sha256:76d5672691cd` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161.1715068733 | 2024-05-07 | `sha256:2fa47fa9df7b` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161.1715068733 | 2024-05-07 | `sha256:2fa47fa9df7b` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161.1715068733 | 2024-05-07 | `sha256:2fa47fa9df7b` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.6 | 10 | 2024-05-16 | `sha256:ae3a207ff5ec` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 135 | 2024-05-16 | `sha256:04803b79fc15` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 15 | 2024-05-16 | `sha256:cea51f6fa59f` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 138 | 2024-05-16 | `sha256:0a4a64efa46f` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 16 | 2024-05-16 | `sha256:2d85638d62f4` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 636 | 2024-05-16 | `sha256:eff48b9f5c96` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 661 | 2024-05-16 | `sha256:61e294676af1` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 661 | 2024-05-16 | `sha256:61e294676af1` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 661 | 2024-05-16 | `sha256:61e294676af1` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 16 | 2024-05-16 | `sha256:eb83b3fe19f8` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 130 | 2024-05-16 | `sha256:18332377d324` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 13 | 2024-05-16 | `sha256:6fba59839ebc` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 121 | 2024-05-16 | `sha256:5231cb8a8f53` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 148 | 2024-05-16 | `sha256:cd898d9f2d99` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405091536.p0.gb17014f.assembly.stream.el8 | 2024-05-09 | `sha256:76d5672691cd` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405091536.p0.gb17014f.assembly.stream.el8 | 2024-05-09 | `sha256:76d5672691cd` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405091536.p0.gb17014f.assembly.stream.el8 | 2024-05-09 | `sha256:76d5672691cd` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405091536.p0.gb17014f.assembly.stream.el8 | 2024-05-09 | `sha256:76d5672691cd` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 177.1712921781 | 2024-04-12 | `sha256:f490e1e409f8` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 178 | 2024-03-27 | `sha256:07091ba15a3f` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161.1715068733 | 2024-05-07 | `sha256:2fa47fa9df7b` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161.1715068733 | 2024-05-07 | `sha256:2fa47fa9df7b` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1161.1715068733 | 2024-05-07 | `sha256:2fa47fa9df7b` |

## Image pull specs

<details><summary>All 17 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:04803b79fc1595398dfeb64ae54455159e4e3d012e7659c88de4a67d31eed1ff
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:ae3a207ff5ece95ea8377be998113ab7e5a3b48ebf70a2b2fdfe830b4a4a67a3
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:0a4a64efa46f6b18bc9013f7a2c073eaba678f8d06bfa864654e96b4bc3b8dc8
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:cea51f6fa59fe5451cc6bd4acaefa43f8066fa055b4eaa3e650499396a13d301
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:2d85638d62f4710591eeac330ed488e4ad79256a032ce1b12d3fdc165c868b4e
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:eff48b9f5c962c0c0236f16dc3ed2a437345f8ed9268f9a5b023f2f9fe7cf0b1
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:61e294676af1db164ed874930f71b973c2797b942ea443c976219888b7bf5df7
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:18332377d324bbadd4c8f53c129c663bf9f3ff29953c67e4a0b1b8d5c223140c
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:eb83b3fe19f8483ca90695e1f92bddb1804247837ef263e1938f7162e1ec6072
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:6fba59839ebcee69dd32e6e7d6273b7f9e9ad462b29ab698f853403926d130cb
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:5231cb8a8f536b162da2e805d57b81eea07e4b504730b1110e928a7ead5a2e44
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:cd898d9f2d996f053170246a88bd6aac30ddd3fa2dd2aed94c61dc1d25888164
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:13d898e425a237a1e22145ab4a8ffe9621f79e728d1c9d4d1e3ef11a5001120b
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:76d5672691cdae228592a21accdbd68807276ca4102f047e5da54cb4c87e8a40
registry.redhat.io/rhel8/postgresql-13@sha256:f490e1e409f89704d97c7a47b4f0d7610830f8581ae86871ce7aa99dd5cb52b0
registry.redhat.io/rhel8/redis-6@sha256:07091ba15a3f17d7dfd6c5e2dd5b951a338cfd833106f057c24993d57595bd92
registry.redhat.io/ubi8/ubi-minimal@sha256:2fa47fa9df7b98e2776f447855699c01d06c3271b2d7259b8b314084580cf591
```

</details>
