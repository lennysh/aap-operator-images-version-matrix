# `aap-operator.v2.5.0-0.1737101025`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1737101025` |
| **Build date** | 2025-01-17 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1736893446`](./aap-operator.v2.5.0-0.1736893446.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:1e99d9c9d72dfbb426b63f1025c2d3a33f6eb1df725a743ee599766b78c217b2` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.6 | 2 | 2025-01-17 | `sha256:c48d8f5375ae` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 149 | 2025-01-17 | `sha256:9d768dff8aad` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.3 | 13 | 2025-01-17 | `sha256:52360fdd1751` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 149 | 2025-01-17 | `sha256:7fa8cff9e4e2` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.3 | 4 | 2025-01-17 | `sha256:4591baef4166` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 803 | 2025-01-17 | `sha256:4ff8f6e1e355` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 878 | 2025-01-17 | `sha256:bf889251c13a` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 878 | 2025-01-17 | `sha256:bf889251c13a` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 878 | 2025-01-17 | `sha256:bf889251c13a` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 40 | 2025-01-17 | `sha256:a1c40f810dd1` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250115 | 2 | 2025-01-17 | `sha256:630b876bfa78` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 193 | 2025-01-17 | `sha256:572f6cc4fc26` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 21 | 2025-01-17 | `sha256:f5cccbf3aed4` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 150 | 2025-01-17 | `sha256:d59b84ede568` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 19 | 2025-01-17 | `sha256:e88b353d1beb` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250107 | 2 | 2025-01-17 | `sha256:cc5f5d786af3` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 110 | 2025-01-17 | `sha256:d41a8ca1c4b7` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 102 | 2025-01-17 | `sha256:a236ce5e7e00` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 132 | 2025-01-17 | `sha256:5f5ed4da25db` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1063 | 2025-01-17 | `sha256:1e99d9c9d72d` |
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
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:9d768dff8aada6ff056a6056e6b7f1cf79cd962bf30d9e1a16666d7b738ed16b
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:c48d8f5375aea94496c010ea10744750b47f4b03a021a7debf18e0cfb464c24c
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:7fa8cff9e4e2f89c897cadb0a41871c4b7b21ff181304be92f4fd3d1b5955384
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:52360fdd1751ffa1752c807dd6472736f9fae2730d5c38525ab3981172acabb3
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:4591baef41664ef6e877269a2e10176e2055d6487be4238e1af445b535f0323d
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:4ff8f6e1e355e00e606f5c3b113592f58bb11d16eaee0fa300d53ed3a3e045b4
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:bf889251c13aa45cc7471d019a0ba73a02914bf542b6b8ca759ddd4b30b02204
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:a1c40f810dd1f0fae82def1ce8dc9caca4d7c1b08eed85ed440b91d3f104b7e5
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:572f6cc4fc26cf1a5adf1c63bca6715828bacd8b167173d5e023f4b7fb7a85d0
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:630b876bfa78664f99a3add74821aa3560ef2ba95ba78579edbdb73e90413bb3
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:d59b84ede568c48b1eb00b1b743cbcfbfa96d71be33bf920d70cb5523e9c464a
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:f5cccbf3aed49e9eb3fd3a58e34bc5afaa0d634c8a70d68d0415005049cecf64
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:e88b353d1beba17c9905dfc624f49e26aea54e5a6f2fe41e58f74194beac1d16
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:d41a8ca1c4b76fe758d1b588301cde74fa61c21f371b681c30601e26d84dac5d
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:cc5f5d786af37cdb467543ea6809d325a0580047cd90dcb91bb683e31c180a1e
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:a236ce5e7e0015aa9b40873611bf8f63c695369e17296f88fc64c34fc8568be2
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:5f5ed4da25db2da12662fdaeba193b17c5aecce376ecbcc24258308e63bc1c11
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:1e99d9c9d72dfbb426b63f1025c2d3a33f6eb1df725a743ee599766b78c217b2
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:38ee3484ba60bb474e7231e9d0718157386716cea7ffd6da6f32ddd551a5243d
registry.redhat.io/rhel8/postgresql-15@sha256:985f4b09370b339740c6ee461a5e2989dd51a27aabb14e307590865cd885aaad
registry.redhat.io/rhel8/redis-6@sha256:27413346612521f4d74783136fd7723b05a3b31fc8b07fe16d33acde0720516e
registry.redhat.io/ubi8/ubi-minimal@sha256:cf095e5668919ba1b4ace3888107684ad9d587b1830d3eb56973e6a54f456e67
```

</details>
