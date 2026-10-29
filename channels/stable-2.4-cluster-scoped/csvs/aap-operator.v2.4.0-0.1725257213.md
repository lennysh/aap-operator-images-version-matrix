# `aap-operator.v2.4.0-0.1725257213`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1725257213` |
| **Build date** | 2024-09-02 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1720482740`](./aap-operator.v2.4.0-0.1720482740.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:e1354a80ca1ddcf809f2123cae6a2db10118f293f03d7f8ea3b39cf965507be6` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.10 | 9 | 2024-09-02 | `sha256:38c8c72fd1a3` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 148 | 2024-09-02 | `sha256:fecc9c1d0018` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 18 | 2024-09-02 | `sha256:4fa903eb8b47` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 149 | 2024-09-02 | `sha256:eadb85940c41` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 16 | 2024-09-02 | `sha256:945ab231fc9d` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 719 | 2024-09-02 | `sha256:5922f8e54740` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 774 | 2024-09-02 | `sha256:fcf96133a5bf` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 774 | 2024-09-02 | `sha256:fcf96133a5bf` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 774 | 2024-09-02 | `sha256:fcf96133a5bf` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 21 | 2024-09-02 | `sha256:186fe64458dc` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 144 | 2024-09-02 | `sha256:cbaedd3b5bf6` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 20 | 2024-09-02 | `sha256:30059cafc55f` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.2 | 10 | 2024-09-02 | `sha256:aa47d8a33e2a` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 16 | 2024-09-02 | `sha256:2e52a0406056` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 139 | 2024-09-02 | `sha256:981d8f970819` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 181 | 2024-09-02 | `sha256:3e774f8895ac` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1957 | 2024-09-02 | `sha256:e1354a80ca1d` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | N/A | N/A | N/A | `sha256:514e9e03f1d9` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.10 | 9 | 2024-09-02 | `sha256:38c8c72fd1a3` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 148 | 2024-09-02 | `sha256:fecc9c1d0018` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 18 | 2024-09-02 | `sha256:4fa903eb8b47` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 149 | 2024-09-02 | `sha256:eadb85940c41` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 16 | 2024-09-02 | `sha256:945ab231fc9d` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 719 | 2024-09-02 | `sha256:5922f8e54740` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 774 | 2024-09-02 | `sha256:fcf96133a5bf` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 774 | 2024-09-02 | `sha256:fcf96133a5bf` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 774 | 2024-09-02 | `sha256:fcf96133a5bf` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 21 | 2024-09-02 | `sha256:186fe64458dc` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 144 | 2024-09-02 | `sha256:cbaedd3b5bf6` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 20 | 2024-09-02 | `sha256:30059cafc55f` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.2 | 10 | 2024-09-02 | `sha256:aa47d8a33e2a` |
| ansible-lightspeed-operator-controller-manager/ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 16 | 2024-09-02 | `sha256:2e52a0406056` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 139 | 2024-09-02 | `sha256:981d8f970819` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 181 | 2024-09-02 | `sha256:3e774f8895ac` |
| ansible-lightspeed-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | N/A | N/A | N/A | `sha256:514e9e03f1d9` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | N/A | N/A | N/A | `sha256:514e9e03f1d9` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | N/A | N/A | N/A | `sha256:514e9e03f1d9` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | N/A | N/A | N/A | `sha256:514e9e03f1d9` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | N/A | N/A | N/A | `sha256:514e9e03f1d9` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724231537 | 2024-08-21 | `sha256:b6bcfe5e7b6a` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:fecc9c1d0018f72e158e3058b1d4c3deac47cef1abe9ab9b7fff93176b6d45e6
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:38c8c72fd1a3e3db6940682f1893808e14d05aa8f180f8ffad8dd74ab163ab3a
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:eadb85940c41d7e2aaedd2273e11c83458b05901197cdcaaf0cfada5ee21c3ca
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:4fa903eb8b473260ae74fcd9efd7fdb5a8fd8721fb4d748f8ec1d22a5a981377
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:945ab231fc9d79e19a45c618fa5cff4a36d300e21d872f7fb578c55b6b82ee03
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:5922f8e547405284572075acfc563476f108e4c4ac40391a27b4204bb168df32
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:fcf96133a5bfc7377b0b2561b4feb6d07f84e8ecc6a84ef88fe3dce0e11e51fb
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:cbaedd3b5bf6c061b63db06c9c8e3a2e8e2f3a893539829ab34f02ce42574d07
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:186fe64458dc0e079e3b1c5df23d7df5a44e1aa20d2b10d959777353c2b7307d
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:30059cafc55f2893f052b2cd2614b5d55481184e3e65eee086750fe736bdf582
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:2e52a04060560c7e7f8c8b59e833c4fe31b56c9395f3d7d789d2611651166910
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:aa47d8a33e2a1777331bcf15c6d2bffc8fac264d39f3ff9072eff32620bc2d3b
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:981d8f970819510d87c20296500372588d58d114d6c54ae881276191aafc8891
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:3e774f8895aca8a435247531a494296a832c1128d7531b8b4240572ec51565dd
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:e1354a80ca1ddcf809f2123cae6a2db10118f293f03d7f8ea3b39cf965507be6
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:514e9e03f1d96046ff819798e54aa5672621c15805d61fb6137283f83f57a1e3
registry.redhat.io/rhel8/postgresql-13@sha256:b6bcfe5e7b6a9601c2322559d0014e2378d7757b2a4d79c1c01b8a5c9b6e4b7d
registry.redhat.io/rhel8/redis-6@sha256:a848cc4edb4405846c673187dd68ce66c328dd1ad42f193f5737288c7971399d
registry.redhat.io/ubi8/ubi-minimal@sha256:a47c89f02b39a98290f88204ed3d162845db0a0c464b319c2596cfd1e94b444e
```

</details>
