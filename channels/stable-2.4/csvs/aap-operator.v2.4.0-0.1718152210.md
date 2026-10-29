# `aap-operator.v2.4.0-0.1718152210`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1718152210` |
| **Build date** | 2024-06-12 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1717558474`](./aap-operator.v2.4.0-0.1717558474.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:45ce8d93765ef977cfc9ec8bc712854638d5bb03b11d878e2c5301eb880fea0e` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.7 | 11 | 2024-06-11 | `sha256:09344081c568` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 139 | 2024-06-11 | `sha256:30c77ed9afac` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 9 | 2024-06-11 | `sha256:771a90d3be60` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 142 | 2024-06-11 | `sha256:0c5e024332f8` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 7 | 2024-06-11 | `sha256:399b9cb371d3` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 659 | 2024-06-11 | `sha256:ca6f46c6d986` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 690 | 2024-06-11 | `sha256:f52f2d73e083` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 690 | 2024-06-11 | `sha256:f52f2d73e083` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 690 | 2024-06-11 | `sha256:f52f2d73e083` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 12 | 2024-06-11 | `sha256:2757caf89e5e` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 136 | 2024-06-11 | `sha256:304ba06b0f0a` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 11 | 2024-06-11 | `sha256:94214f3477af` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.0 | 1 | 2024-06-11 | `sha256:4d85da1adb29` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 3 | 2024-06-11 | `sha256:c28dfe5dfb05` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 127 | 2024-06-11 | `sha256:439cd19a3838` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 159 | 2024-06-12 | `sha256:40fa197a352a` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1635 | 2024-06-12 | `sha256:45ce8d93765e` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1717586544 | 2024-06-05 | `sha256:c4a98010f7dd` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1717586544 | 2024-06-05 | `sha256:c4a98010f7dd` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1717586544 | 2024-06-05 | `sha256:c4a98010f7dd` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1717584414 | 2024-06-05 | `sha256:5f1cd3422d5d` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1717584414 | 2024-06-05 | `sha256:5f1cd3422d5d` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1717584414 | 2024-06-05 | `sha256:5f1cd3422d5d` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.7 | 11 | 2024-06-11 | `sha256:09344081c568` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 139 | 2024-06-11 | `sha256:30c77ed9afac` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 9 | 2024-06-11 | `sha256:771a90d3be60` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 142 | 2024-06-11 | `sha256:0c5e024332f8` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 7 | 2024-06-11 | `sha256:399b9cb371d3` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 659 | 2024-06-11 | `sha256:ca6f46c6d986` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 690 | 2024-06-11 | `sha256:f52f2d73e083` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 690 | 2024-06-11 | `sha256:f52f2d73e083` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 690 | 2024-06-11 | `sha256:f52f2d73e083` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 12 | 2024-06-11 | `sha256:2757caf89e5e` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 136 | 2024-06-11 | `sha256:304ba06b0f0a` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 11 | 2024-06-11 | `sha256:94214f3477af` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.0 | 1 | 2024-06-11 | `sha256:4d85da1adb29` |
| ansible-lightspeed-operator-controller-manager/ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 3 | 2024-06-11 | `sha256:c28dfe5dfb05` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 127 | 2024-06-11 | `sha256:439cd19a3838` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 159 | 2024-06-12 | `sha256:40fa197a352a` |
| ansible-lightspeed-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202405141537.p0.gb17014f.assembly.stream.el8 | 2024-05-14 | `sha256:e31a70c7e169` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 185.1717586543 | 2024-06-05 | `sha256:ddcb2721ea55` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1717586544 | 2024-06-05 | `sha256:c4a98010f7dd` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1717586544 | 2024-06-05 | `sha256:c4a98010f7dd` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 186.1717586544 | 2024-06-05 | `sha256:c4a98010f7dd` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1717584414 | 2024-06-05 | `sha256:5f1cd3422d5d` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1717584414 | 2024-06-05 | `sha256:5f1cd3422d5d` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 896.1717584414 | 2024-06-05 | `sha256:5f1cd3422d5d` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:30c77ed9afacade4243c463271983a2feacf077664f42cc484b06774c816f3d2
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:09344081c5683ba9fc644df620af72e71f3fc23c566f79b6ad98b5a759b822ee
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:0c5e024332f82a84f2911ff738bb5fd6cc87448e49f511c051849b5a70cb8d5b
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:771a90d3be6053522c56313a5616dd4b54054e2940b6a13b3268fba6d676515a
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:399b9cb371d307a3959bcdb3c5923fb4149e1cdeefb2f2f5c2724bbe0a9a6a39
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:ca6f46c6d9860d925e95f61c5edbf348a359b9ca5655f19e7e994d9816fda0a9
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:f52f2d73e0838532b88e35aac3b3653192d398a46b7c2f04224a6bc0860298d2
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:304ba06b0f0a773485fbd691dac21191d04635fe56b6bce72aa412dd1b7edba0
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:2757caf89e5e0235ece21317af30611ec09354d1c8b707a48615315e7cc518fc
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:94214f3477af7fc4c169569dacb5e7c348f5dd231c7e7aeac5c041e4cd56623c
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:c28dfe5dfb057fe631a4de04dccd1b62403943ac73a093625d7985998d1757b0
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:4d85da1adb291a004b38fd6475818424206ec7b057ed51e83d4bc838fc283063
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:439cd19a38388e84a730f380437435999f1877bf9b5e6a64c848af5041d943f8
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:40fa197a352a799255213faa2879b7126b03fba8401212b4827b7e6e801a9c48
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:45ce8d93765ef977cfc9ec8bc712854638d5bb03b11d878e2c5301eb880fea0e
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:e31a70c7e16952634f87a124c5a15e0e8507856b6b298d0cd030003cd92b1517
registry.redhat.io/rhel8/postgresql-13@sha256:ddcb2721ea5530f5390e1b0361e1d403d5d4c6048863079ff9e8e9ec92e2f210
registry.redhat.io/rhel8/redis-6@sha256:c4a98010f7dd5faec2047bb9803061704233a8efc930be2a02386ac16d062d86
registry.redhat.io/ubi8/ubi-minimal@sha256:5f1cd3422d5d46aea35dac80825dbcbd58213eef49c317f42a394345fb4e8ff1
```

</details>
