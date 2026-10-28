# `aap-operator.v2.5.0-0.1737675968`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1737675968` |
| **Build date** | 2025-01-23 |
| **Replaces** | [`aap-operator.v2.5.0-0.1737101025`](./aap-operator.v2.5.0-0.1737101025.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:6446c318c217db099973ad311718841e2fd60ffce2d93a38d3df45b1cce9592b` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.7 | 6 | 2025-01-23 | `sha256:3e81f1a3d111` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 151 | 2025-01-23 | `sha256:d440f5ce3b88` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.4 | 7 | 2025-01-23 | `sha256:a0bc05446e1e` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 152 | 2025-01-23 | `sha256:5cff86c7c989` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.4 | 2 | 2025-01-23 | `sha256:d39fcd5d337e` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 812 | 2025-01-23 | `sha256:c97285c6af1e` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 889 | 2025-01-23 | `sha256:f73e82a9fdc5` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 889 | 2025-01-23 | `sha256:f73e82a9fdc5` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 889 | 2025-01-23 | `sha256:f73e82a9fdc5` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 42 | 2025-01-23 | `sha256:54b22df108dd` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250115 | 4 | 2025-01-23 | `sha256:ea543c06a97c` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 198 | 2025-01-23 | `sha256:8db9ed1f6767` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 23 | 2025-01-23 | `sha256:014eafa95236` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 152 | 2025-01-23 | `sha256:a465a6656ef2` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 21 | 2025-01-23 | `sha256:b03b790fe874` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250121 | 2 | 2025-01-23 | `sha256:5913161632b7` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 112 | 2025-01-23 | `sha256:b4ccea42c731` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 104 | 2025-01-23 | `sha256:1c89eb39aaab` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 135 | 2025-01-23 | `sha256:8a09a5b61681` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1077 | 2025-01-23 | `sha256:6446c318c217` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202501021509.p0.g9308e7f.assembly.stream.el8 | 2025-01-02 | `sha256:38ee3484ba60` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 89.1735831620 | 2025-01-02 | `sha256:985f4b09370b` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 89.1735831620 | 2025-01-02 | `sha256:985f4b09370b` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 89.1735831620 | 2025-01-02 | `sha256:985f4b09370b` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 89.1735831620 | 2025-01-02 | `sha256:985f4b09370b` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 89.1735831620 | 2025-01-02 | `sha256:985f4b09370b` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 211.1735831615 | 2025-01-02 | `sha256:274133466125` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 211.1735831615 | 2025-01-02 | `sha256:274133466125` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 211.1735831615 | 2025-01-02 | `sha256:274133466125` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 211.1735831615 | 2025-01-02 | `sha256:274133466125` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1154 | 2024-12-10 | `sha256:cf095e566891` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1154 | 2024-12-10 | `sha256:cf095e566891` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1154 | 2024-12-10 | `sha256:cf095e566891` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:d440f5ce3b88f99acb55555ab176799c2e3e1b2ee3c3ff07550414cbd0d4fd0e
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:3e81f1a3d1119373104b44f078dd20a4826b11e9552418716c9ea70e1b513b63
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:5cff86c7c98980d0fb29b3dd461317fbf6bf3704a59e8f36b60f6d0e0db59715
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:a0bc05446e1e75c62b69e89f2e532326f379b38a060e088c5655f284e5ad483d
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:d39fcd5d337e2c832f476559dad5c411dead7073d3e4ec3bac117b432280ebff
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:c97285c6af1ebbb0e6aac3bcdad95ed5fc003998643d31038df5f0ddb874a96a
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:f73e82a9fdc5f7b3ffe59d3ddc8948543535479c6a25205b1830a8ef5d0f9928
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:54b22df108dd0d37fd1e38725e46b7db5f0116a1b334b9d8468f07aa74348290
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:8db9ed1f6767c04ddadd748fb6dd18e7a1b385c51921fb4599edbb6d42a26bdd
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:ea543c06a97c2d1fe4efd36b6935e010e43288a3ff1f5d8206454cb97197f930
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:a465a6656ef2927b058f29b50a71b2cecb16c459743b24157b4875dc4665c654
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:014eafa952362c2d226a157f0016b28e3eed181b80758be1f112d275d893c260
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:b03b790fe8742a48e106892e7d1622c30c631a5fc96131685aabc96301500710
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:b4ccea42c731edb7de878e0620e0fc7bc06bd0ab672be2aadf549f2697402456
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:5913161632b74ffc852e09cf0b80eb3f912bccadcf1bfefa09a797fc08154f92
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:1c89eb39aaab65edb4967db1a6087205cbbb2e739183b6d652c6bf81134f7f31
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:8a09a5b616813400c74a325c45d33adde9a4cafa678e87ee2ca1ab6ddf19b7a7
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:6446c318c217db099973ad311718841e2fd60ffce2d93a38d3df45b1cce9592b
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:38ee3484ba60bb474e7231e9d0718157386716cea7ffd6da6f32ddd551a5243d
registry.redhat.io/rhel8/postgresql-15@sha256:985f4b09370b339740c6ee461a5e2989dd51a27aabb14e307590865cd885aaad
registry.redhat.io/rhel8/redis-6@sha256:27413346612521f4d74783136fd7723b05a3b31fc8b07fe16d33acde0720516e
registry.redhat.io/ubi8/ubi-minimal@sha256:cf095e5668919ba1b4ace3888107684ad9d587b1830d3eb56973e6a54f456e67
```

</details>
