# `aap-operator.v2.4.0-0.1708975279`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1708975279` |
| **Build date** | 2024-02-26 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1707507304`](./aap-operator.v2.4.0-0.1707507304.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:3b6522ecb32befca70fd384913308c8d5e11faa9351356560ce38b827dfe9f98` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.2 | 6 | 2024-02-23 | `sha256:e9d9ab6f44a3` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 117 | 2024-02-23 | `sha256:4a98d6fc5f43` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 3 | 2024-02-23 | `sha256:14ad6736f3f6` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 127 | 2024-02-23 | `sha256:e2eec43f9a7a` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 3 | 2024-02-23 | `sha256:9cf2b23e93d2` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 547 | 2024-02-23 | `sha256:7821e2f0d445` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 572 | 2024-02-26 | `sha256:375d121bed67` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 572 | 2024-02-26 | `sha256:375d121bed67` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 572 | 2024-02-26 | `sha256:375d121bed67` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 4 | 2024-02-23 | `sha256:0d66d63ee2b4` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 112 | 2024-02-23 | `sha256:53637a015ca4` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 4 | 2024-02-23 | `sha256:58a3a01caff8` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 107 | 2024-02-23 | `sha256:fd6e4eff9f8c` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 130 | 2024-02-26 | `sha256:cfc86033877e` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1202 | 2024-02-26 | `sha256:3b6522ecb32b` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202402081808.p0.gb17014f.assembly.stream.el8 | 2024-02-08 | `sha256:263090bea39e` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169 | 2024-02-13 | `sha256:a9a7a7812b19` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169 | 2024-02-13 | `sha256:a9a7a7812b19` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169 | 2024-02-13 | `sha256:a9a7a7812b19` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.2 | 6 | 2024-02-23 | `sha256:e9d9ab6f44a3` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 117 | 2024-02-23 | `sha256:4a98d6fc5f43` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 3 | 2024-02-23 | `sha256:14ad6736f3f6` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 127 | 2024-02-23 | `sha256:e2eec43f9a7a` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 3 | 2024-02-23 | `sha256:9cf2b23e93d2` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 547 | 2024-02-23 | `sha256:7821e2f0d445` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 572 | 2024-02-26 | `sha256:375d121bed67` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 572 | 2024-02-26 | `sha256:375d121bed67` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 572 | 2024-02-26 | `sha256:375d121bed67` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 4 | 2024-02-23 | `sha256:0d66d63ee2b4` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 112 | 2024-02-23 | `sha256:53637a015ca4` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 4 | 2024-02-23 | `sha256:58a3a01caff8` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 107 | 2024-02-23 | `sha256:fd6e4eff9f8c` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 130 | 2024-02-26 | `sha256:cfc86033877e` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202402081808.p0.gb17014f.assembly.stream.el8 | 2024-02-08 | `sha256:263090bea39e` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202402081808.p0.gb17014f.assembly.stream.el8 | 2024-02-08 | `sha256:263090bea39e` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202402081808.p0.gb17014f.assembly.stream.el8 | 2024-02-08 | `sha256:263090bea39e` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202402081808.p0.gb17014f.assembly.stream.el8 | 2024-02-08 | `sha256:263090bea39e` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169 | 2024-02-13 | `sha256:a9a7a7812b19` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169 | 2024-02-13 | `sha256:a9a7a7812b19` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169 | 2024-02-13 | `sha256:a9a7a7812b19` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |

## Image pull specs

<details><summary>All 17 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:4a98d6fc5f43e4418a0681de154a9ce67f6205d69cfb91137da93ad1322aa523
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:e9d9ab6f44a323f781808c4e35b4e0403e86b0413de2319d14116b510eb77fe9
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:e2eec43f9a7ae2cc466640f681cb4d4f62b25505db98a2b6d45b756660cfd993
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:14ad6736f3f68017b8e930ce7e8c0f369fa458c5f94c1faca340c1d7c3b62d53
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:9cf2b23e93d21e749c806397a4c548a87e6f4d8a723645727fe4a1f451e53496
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:7821e2f0d445379078c51b797435ffe4a334b5bb6a9d0e8f996868165a3d9b6a
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:375d121bed676a58210484209b1316c29e3af4a81f56f20ef4b914e0e46e7377
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:53637a015ca453de862ee9a17466e936f650d09f4d7108bcf8e37c0a3060cbe8
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:0d66d63ee2b457127997dbbbbb5afd6c0dd52f66e4f5ee7c1e6ba417b879ef44
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:58a3a01caff8052c886a27524cf14625b01e7cfdcf6ae431040985ee17136a7d
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:fd6e4eff9f8c71d17c58004b2492af2f2071179fd591b9b819379919641ae6cc
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:cfc86033877ed7ee9735cad1ef6b6dd7616bbe1ef68e4e644c3921a4d224d55c
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:3b6522ecb32befca70fd384913308c8d5e11faa9351356560ce38b827dfe9f98
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:263090bea39e7875b40e128a059f6f971916196ffd8308504d92e4fd06d4f83a
registry.redhat.io/rhel8/postgresql-13@sha256:a9a7a7812b19ea85aee2d234d422a13205c6830958b00efa5b2e946beaf6c4f8
registry.redhat.io/rhel8/redis-6@sha256:29eba91f2feeb5d5efe146806c83894f53814c06c74d0d6c2806c928aef40d8a
registry.redhat.io/ubi8/ubi-minimal@sha256:8bedbe742f140108897fb3532068e8316900d9814f399d676ac78b46e740e34e
```

</details>
