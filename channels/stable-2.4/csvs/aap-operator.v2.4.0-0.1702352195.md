# `aap-operator.v2.4.0-0.1702352195`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1702352195` |
| **Build date** | 2023-12-12 |
| **Previous CSV** | — |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:a8f1df1a41c5af6441cb01f2d584f9b86c0a3153e722033c8da7f51837d450c3` |
| **Seen in OCP operator indexes** | 4.11–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.0 | 51 | 2023-12-11 | `sha256:9f4908f8f9eb` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 100 | 2023-12-11 | `sha256:e6e057edaa8b` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.3 | 20 | 2023-12-11 | `sha256:0df134576d35` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 106 | 2023-12-11 | `sha256:da1a29c28512` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.3 | 21 | 2023-12-11 | `sha256:f02dc7abfa75` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 499 | 2023-12-11 | `sha256:0851fb85bf5a` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 505 | 2023-12-11 | `sha256:b6aed81bd8bf` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 505 | 2023-12-11 | `sha256:b6aed81bd8bf` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 505 | 2023-12-11 | `sha256:b6aed81bd8bf` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.7.3 | 34 | 2023-12-11 | `sha256:996bd1deec25` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 90 | 2023-12-11 | `sha256:9bc95e664649` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.7.3 | 34 | 2023-12-11 | `sha256:28ffac70395e` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 91 | 2023-12-11 | `sha256:7f904f47473f` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 116 | 2023-12-12 | `sha256:7e9de0a50e9a` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 890 | 2023-12-12 | `sha256:a8f1df1a41c5` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202311211130.p0.gc04896c.assembly.stream | 2023-11-21 | `sha256:3b0eb7d2d3ac` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 158.1701272579 | 2023-11-29 | `sha256:6ecee6d67013` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 158.1701272579 | 2023-11-29 | `sha256:6ecee6d67013` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 158.1701272579 | 2023-11-29 | `sha256:6ecee6d67013` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 156 | 2023-11-02 | `sha256:26573f1230a3` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 156 | 2023-11-02 | `sha256:26573f1230a3` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 156 | 2023-11-02 | `sha256:26573f1230a3` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1029 | 2023-11-01 | `sha256:87bcbfedfd70` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1029 | 2023-11-01 | `sha256:87bcbfedfd70` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1029 | 2023-11-01 | `sha256:87bcbfedfd70` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.0 | 51 | 2023-12-11 | `sha256:9f4908f8f9eb` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 100 | 2023-12-11 | `sha256:e6e057edaa8b` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.3 | 20 | 2023-12-11 | `sha256:0df134576d35` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 106 | 2023-12-11 | `sha256:da1a29c28512` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.3 | 21 | 2023-12-11 | `sha256:f02dc7abfa75` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 499 | 2023-12-11 | `sha256:0851fb85bf5a` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 505 | 2023-12-11 | `sha256:b6aed81bd8bf` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 505 | 2023-12-11 | `sha256:b6aed81bd8bf` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 505 | 2023-12-11 | `sha256:b6aed81bd8bf` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.7.3 | 34 | 2023-12-11 | `sha256:996bd1deec25` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 90 | 2023-12-11 | `sha256:9bc95e664649` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.7.3 | 34 | 2023-12-11 | `sha256:28ffac70395e` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 91 | 2023-12-11 | `sha256:7f904f47473f` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 116 | 2023-12-12 | `sha256:7e9de0a50e9a` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202311211130.p0.gc04896c.assembly.stream | 2023-11-21 | `sha256:3b0eb7d2d3ac` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202311211130.p0.gc04896c.assembly.stream | 2023-11-21 | `sha256:3b0eb7d2d3ac` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202311211130.p0.gc04896c.assembly.stream | 2023-11-21 | `sha256:3b0eb7d2d3ac` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202311211130.p0.gc04896c.assembly.stream | 2023-11-21 | `sha256:3b0eb7d2d3ac` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 158.1701272579 | 2023-11-29 | `sha256:6ecee6d67013` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 158.1701272579 | 2023-11-29 | `sha256:6ecee6d67013` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 158.1701272579 | 2023-11-29 | `sha256:6ecee6d67013` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 156 | 2023-11-02 | `sha256:26573f1230a3` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 156 | 2023-11-02 | `sha256:26573f1230a3` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 156 | 2023-11-02 | `sha256:26573f1230a3` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1029 | 2023-11-01 | `sha256:87bcbfedfd70` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1029 | 2023-11-01 | `sha256:87bcbfedfd70` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1029 | 2023-11-01 | `sha256:87bcbfedfd70` |

## Image pull specs

<details><summary>All 17 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:e6e057edaa8b74e888e20f2f654987f15ec69a5a0c25d13562df6ad6eb1fa683
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:9f4908f8f9eb6bc803c0c09fb9206699073fad991b58d373c5602a664ec3bce3
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:da1a29c285125c11b5d9c5c15c36c73ed5713c18830fffd043a7891125f8a621
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:0df134576d35910efe875ab450273c1b6960981346c0c7fd0dc19c7691b1fcfe
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:f02dc7abfa755897567720f501717fca244f74da0b788e91f0cb3449bdc49a32
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:0851fb85bf5a75831277b54c636da1854d50a5ac2a5fa2ddc1c6b768cb02ae77
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:b6aed81bd8bf840db5e98a37a0d6fc6a2ce679c3ce5ddbf5a2f2c5c241c6c059
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:9bc95e664649bea0d8fe6d328b631db3a624ef59f1e57c15f27651087296c0b4
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:996bd1deec251efcbd0d902c35d1dc523c1028c26158705bf05c9d714abf3ffa
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:28ffac70395e8fc4c12e0609eb03c34e538004c9494b5e67b8a75f527ca82192
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:7f904f47473f71bfc230a4e075877dfdc4d935961110fcea91734bbb75e41727
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:7e9de0a50e9a1e95ce4dfc5783f705242946dc31cb83e28c29a4dc2d21caba95
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:a8f1df1a41c5af6441cb01f2d584f9b86c0a3153e722033c8da7f51837d450c3
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:3b0eb7d2d3ac3ab0ed847c521f2c5a629e579a8778829a71d5841e762eea5fb9
registry.redhat.io/rhel8/postgresql-13@sha256:6ecee6d67013493b2735d7c300b0809e4c261a0f682d8f981d5cc4058e990c4c
registry.redhat.io/rhel8/redis-6@sha256:26573f1230a3c7df5475d5968bf6595719950906f8e7594b5394ad6fcab9b0e4
registry.redhat.io/ubi8/ubi-minimal@sha256:87bcbfedfd70e67aab3875fff103bade460aeff510033ebb36b7efa009ab6639
```

</details>
