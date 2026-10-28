# `aap-operator.v2.5.0-0.1747345055`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1747345055` |
| **Build date** | 2025-05-15 |
| **Replaces** | [`aap-operator.v2.5.0-0.1746138413`](./aap-operator.v2.5.0-0.1746138413.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:4a56a485781bf1378e5db510c4eb1b81c7f3c9cf9a94ae32add30a011f8dbfac` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.13 | 9 | 2025-05-15 | `sha256:3e514086eecb` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 181 | 2025-05-15 | `sha256:1d3f1e2002c3` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.8 | 6 | 2025-05-15 | `sha256:df249c8a8acc` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 180 | 2025-05-15 | `sha256:0185e4ae8ebf` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.8 | 2 | 2025-05-15 | `sha256:53b5e9bdac6b` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 912 | 2025-05-15 | `sha256:5e2d0cd76751` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1016 | 2025-05-15 | `sha256:e1bfda943b1b` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1016 | 2025-05-15 | `sha256:e1bfda943b1b` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1016 | 2025-05-15 | `sha256:e1bfda943b1b` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 26 | 2025-05-15 | `sha256:61312ac42b55` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250528 | 1 | 2025-05-15 | `sha256:c664b5d8cc2e` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 234 | 2025-05-15 | `sha256:45914c9c367a` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.4 | 10 | 2025-05-15 | `sha256:bc6c513c53d4` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 180 | 2025-05-15 | `sha256:5e2b0e2b8f3b` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.4 | 9 | 2025-05-15 | `sha256:409964f452f7` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250528 | 1 | 2025-05-15 | `sha256:16e90d67f726` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250528 | 1 | 2025-05-15 | `sha256:0522234fcd56` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 141 | 2025-05-15 | `sha256:39817f99b52e` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 134 | 2025-05-15 | `sha256:9cb5b0a43f47` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 178 | 2025-05-15 | `sha256:f82bd1b122b7` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1347 | 2025-05-15 | `sha256:4a56a485781b` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202504220035.p0.g9308e7f.assembly.stream.el8 | 2025-04-22 | `sha256:bb84ead43704` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:1d3f1e2002c389155022a183a103b7b687367c11ff6db92d3327b66dd5528f42
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:3e514086eecb17f6100bdb974496b98a198ddd45ae4a322b4a196c6b4b6b359d
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:0185e4ae8ebfca380676393c1872bf811f8ef9d716af2d7d39df3c161a6ae817
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:df249c8a8accabfc549115765a14d4033d6bfcd39fceda1c7a02bae3fb349d8d
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:53b5e9bdac6b8608911e2f3954af01eb388904652ddf976bcb9fbf3f081148c3
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:5e2d0cd76751ecd97b90593c21bd0c8f2f51a0c0a429e5fc192a5dfd4bdc37c4
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:e1bfda943b1b1c1da5b275cc254a4fae982ab52c716dc2a7759081d59db0eaa0
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:61312ac42b5552eeb8816aed2e60c42bdf164f9b968e8ac23ef8ce63a09874d0
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:45914c9c367a4777164a401fe4fc9c057386fa6bbefdd191cdd92d37a369359e
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:c664b5d8cc2e1991b6ea94645b4698685724c0c89e2671ae197b0e1cf6feb75f
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:5e2b0e2b8f3bca518a002ffc2a52e0c9460a4d7dedcd5f4a3756954a9bbf3279
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:bc6c513c53d4197c8f6b157565de68d3a2722d2fb1f9b4b2513538834cfb4870
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:409964f452f78451e9856804f0ad2ceafb45275045f6adf4e1bcadacf0916aad
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:16e90d67f726fa686dd140d8f3cabb85653a9ebcee26b142c6ffb2b53faabde5
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:39817f99b52eee1bbb6398f80a7f8265691c639cceb122920ddf46c9a466cb8e
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:0522234fcd56dd02ef2e45a71a2f1163f499dcd134eb3b0d14b622acc3337102
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:9cb5b0a43f474c2a37ac0a75a2023f62642720a1a6792a4a06bfc651c7c253b8
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:f82bd1b122b76c0092becc0f29dce1d0bd7a67e01d9b2492df1b0ec9ca66ab53
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:4a56a485781bf1378e5db510c4eb1b81c7f3c9cf9a94ae32add30a011f8dbfac
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:bb84ead437042603254efcb703442be8500a9450b10bbcaaee81b48a6ed869ea
registry.redhat.io/rhel8/postgresql-15@sha256:0576206b44a5cb073b6364f7af104a4a17994f9bb8c7a948da9588d6b4bbf1e8
registry.redhat.io/rhel8/redis-6@sha256:3d8c1326faadcb66b79facb311844cbdb3a462a4af47f8e68944382824d1ba8b
registry.redhat.io/ubi8/ubi-minimal@sha256:b2a1bec3dfbc7a14a1d84d98934dfe8fdde6eb822a211286601cf109cbccb075
```

</details>
