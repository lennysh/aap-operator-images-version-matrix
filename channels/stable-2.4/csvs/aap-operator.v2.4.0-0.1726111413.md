# `aap-operator.v2.4.0-0.1726111413`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1726111413` |
| **Build date** | 2024-09-12 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1725256739`](./aap-operator.v2.4.0-0.1725256739.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:8f97272dc22c199a29978196e5ae9bc58a4b9573c654fa4129e4781a78171654` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.11 | 4 | 2024-09-12 | `sha256:15d60d3281db` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 152 | 2024-09-12 | `sha256:fcc981770088` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 20 | 2024-09-12 | `sha256:22510d7ca724` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 153 | 2024-09-12 | `sha256:a7040242b588` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 18 | 2024-09-12 | `sha256:fc900faa7ac2` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 728 | 2024-09-12 | `sha256:aad0d5447998` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 786 | 2024-09-12 | `sha256:5bddfc51b023` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 786 | 2024-09-12 | `sha256:5bddfc51b023` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 786 | 2024-09-12 | `sha256:5bddfc51b023` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 23 | 2024-09-12 | `sha256:5c9d5ac7dc5f` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 148 | 2024-09-12 | `sha256:a9478c98dc90` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 22 | 2024-09-12 | `sha256:df946ba1224d` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.2 | 13 | 2024-09-12 | `sha256:c21c8b6e13be` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 20 | 2024-09-12 | `sha256:617ae486081a` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 143 | 2024-09-12 | `sha256:e4b709ccd5ca` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 185 | 2024-09-12 | `sha256:ce42c45c861f` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1996 | 2024-09-12 | `sha256:8f97272dc22c` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202408220304.p0.gb17014f.assembly.stream.el8 | 2024-08-23 | `sha256:9674694d47bf` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.11 | 4 | 2024-09-12 | `sha256:15d60d3281db` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 152 | 2024-09-12 | `sha256:fcc981770088` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 20 | 2024-09-12 | `sha256:22510d7ca724` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 153 | 2024-09-12 | `sha256:a7040242b588` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 18 | 2024-09-12 | `sha256:fc900faa7ac2` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 728 | 2024-09-12 | `sha256:aad0d5447998` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 786 | 2024-09-12 | `sha256:5bddfc51b023` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 786 | 2024-09-12 | `sha256:5bddfc51b023` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 786 | 2024-09-12 | `sha256:5bddfc51b023` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 23 | 2024-09-12 | `sha256:5c9d5ac7dc5f` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 148 | 2024-09-12 | `sha256:a9478c98dc90` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 22 | 2024-09-12 | `sha256:df946ba1224d` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.2 | 13 | 2024-09-12 | `sha256:c21c8b6e13be` |
| ansible-lightspeed-operator-controller-manager/ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 20 | 2024-09-12 | `sha256:617ae486081a` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 143 | 2024-09-12 | `sha256:e4b709ccd5ca` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 185 | 2024-09-12 | `sha256:ce42c45c861f` |
| ansible-lightspeed-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202408220304.p0.gb17014f.assembly.stream.el8 | 2024-08-23 | `sha256:9674694d47bf` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202408220304.p0.gb17014f.assembly.stream.el8 | 2024-08-23 | `sha256:9674694d47bf` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202408220304.p0.gb17014f.assembly.stream.el8 | 2024-08-23 | `sha256:9674694d47bf` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202408220304.p0.gb17014f.assembly.stream.el8 | 2024-08-23 | `sha256:9674694d47bf` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202408220304.p0.gb17014f.assembly.stream.el8 | 2024-08-23 | `sha256:9674694d47bf` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 196.1724929117 | 2024-08-29 | `sha256:a308263f5d10` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 198.1724231532 | 2024-08-21 | `sha256:a848cc4edb44` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1052.1724178568 | 2024-08-20 | `sha256:a47c89f02b39` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:fcc9817700883fda430e6338da6f73051bbf4b2927b63fb6936bd21f2a93c757
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:15d60d3281db28a11da46f1d2f62044570252bcf10dc18bfc8ceef687d10d58f
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:a7040242b588d8b5f76501025bdfa6ed66845a9892cfa77faf9d32879e8389f4
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:22510d7ca72492882d0f1097b3957c01888050ebcedceb5d6b6079f567563a0c
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:fc900faa7ac2c4160d2c93079a9f57c370beeed838b52ab0f5c27ab305878c26
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:aad0d5447998fc8a211b908b88f0f04842f74bdb5e5c14c1f9aa0b0f56399cee
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:5bddfc51b02385aa13936ce729ee3ad02070e74566d2d4f95a956b05105e7de0
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:a9478c98dc905b56ee80aa40974c5bfbafac31e42fe50e1c8f6bcb299c65ecd7
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:5c9d5ac7dc5fc229647e32a224b252bef5c6a062b356d2bdfc006105cd538da7
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:df946ba1224db42c17f031b71274f42d1972e15536ccbadd930f8bbd24dd9d23
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:617ae486081a1704398e2ac9d012f3e422a2a19689f4b68bfc2187b28311bc81
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:c21c8b6e13bede9274b3fed7f409aaf8bf6d0beb6d95d956f1051b249bb74ee3
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:e4b709ccd5caceb4f7ab9d1f7fc202f112ba6e8bc6490100db40637e695e6c04
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:ce42c45c861fd4080a6e35a5fe91c8c67195105cfe066100d64aa1cb747ad379
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:8f97272dc22c199a29978196e5ae9bc58a4b9573c654fa4129e4781a78171654
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:9674694d47bf0056d6ff9ab3c9f8d0849399ac66c74c98b63bc8fa68c8aaec58
registry.redhat.io/rhel8/postgresql-13@sha256:a308263f5d1071be8ac5c13fd84b40609988ca30ed56c22a8bc6769e107ce09b
registry.redhat.io/rhel8/redis-6@sha256:a848cc4edb4405846c673187dd68ce66c328dd1ad42f193f5737288c7971399d
registry.redhat.io/ubi8/ubi-minimal@sha256:a47c89f02b39a98290f88204ed3d162845db0a0c464b319c2596cfd1e94b444e
```

</details>
