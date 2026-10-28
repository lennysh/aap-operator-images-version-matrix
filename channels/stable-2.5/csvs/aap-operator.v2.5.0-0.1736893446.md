# `aap-operator.v2.5.0-0.1736893446`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1736893446` |
| **Build date** | 2025-01-14 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1733969526`](./aap-operator.v2.5.0-0.1733969526.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:3e083f1324e09514f902af7797178ee67ce48e6407513558c0794db10f822a79` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.6 | 1 | 2025-01-09 | `sha256:b74a7efd1eaf` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 146 | 2025-01-09 | `sha256:655d37bfd9fc` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.3 | 12 | 2025-01-09 | `sha256:249fcebc6027` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 145 | 2025-01-09 | `sha256:6bdd170a8f90` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.3 | 3 | 2025-01-09 | `sha256:9f640bebb052` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 799 | 2025-01-09 | `sha256:3f0dedf3a335` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 874 | 2025-01-09 | `sha256:4d2169d22141` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 874 | 2025-01-09 | `sha256:4d2169d22141` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 874 | 2025-01-09 | `sha256:4d2169d22141` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 37 | 2025-01-09 | `sha256:6d51c75c110c` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250115 | 1 | 2025-01-09 | `sha256:22cb9a71a4e4` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 187 | 2025-01-14 | `sha256:310d4df80a96` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 19 | 2025-01-09 | `sha256:6cd20acb7d96` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 147 | 2025-01-09 | `sha256:12670fe33ec9` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 16 | 2025-01-09 | `sha256:c3e2d63811df` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250107 | 1 | 2025-01-09 | `sha256:e33e8f69695e` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 106 | 2025-01-09 | `sha256:69e52b8b347e` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 99 | 2025-01-09 | `sha256:3801ce40fe29` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 130 | 2025-01-09 | `sha256:9086ab014620` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1050 | 2025-01-14 | `sha256:3e083f1324e0` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202412170135.p0.g9308e7f.assembly.stream.el8 | 2024-12-17 | `sha256:55cf59b4df17` |
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
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:655d37bfd9fc387c6636a57c02b9765088173e87ca775f8c5d8f89cede5f932b
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:b74a7efd1eaf150b3a47524085a87b0ada21fb6713720f0192f61fe4722add62
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:6bdd170a8f905f1675e859482b89b26f5b29f890a18faf5b5631b6b511fc17e5
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:249fcebc602751e569bf27da8f59065c886fd2c62eb568a85011e0611d83b274
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:9f640bebb052e04e0ad8d06896fb2cad9d79b2005dd1b8265c2ca3d0a80c9688
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:3f0dedf3a33583d7ed5c74e509a9f8e05c579144df5d1665ea960d9764fb3d2a
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:4d2169d221419da141c9adde1fef6ee717d338e0af83ebda7cf64ef1e237de32
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:6d51c75c110c89695565ead0811c1c0e112b01bb16f7946591b0bd2a7bf5b28f
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:310d4df80a96395bccf6140a7df0214d0df881c9dc1c804487f37d2caabf080f
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:22cb9a71a4e4dfb0e9047cd0209acf7ea200b6b45328265079dee7732ddd166f
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:12670fe33ec92386a09ed2136a9798ea67e3592bbf3c97bf34d69321311b7584
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:6cd20acb7d96f593416e125e928408197c382cc3cb957ecd5ebc1e0bc54db057
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:c3e2d63811dfd87d601e7474f795825f26ae28ea4f478ad816b0e46781167378
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:69e52b8b347efea9f292cc1d18563ebaaba9f1bf7cf309f81e2b63b5b1acc3f5
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:e33e8f69695e9818fe97778c76fedc8686400d282b885d4c10f25183937aed41
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:3801ce40fe29d463d193f8c8d8a44764731776da2dfe194c2e026b12fb657a5b
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:9086ab0146202275d4edefee7ba116f990b2354008582e2d457e2d0aeea439ab
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:3e083f1324e09514f902af7797178ee67ce48e6407513558c0794db10f822a79
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:55cf59b4df17a3cd70188af8332bd1c995e503e8f7291c15a5067748a4219e30
registry.redhat.io/rhel8/postgresql-15@sha256:985f4b09370b339740c6ee461a5e2989dd51a27aabb14e307590865cd885aaad
registry.redhat.io/rhel8/redis-6@sha256:27413346612521f4d74783136fd7723b05a3b31fc8b07fe16d33acde0720516e
registry.redhat.io/ubi8/ubi-minimal@sha256:cf095e5668919ba1b4ace3888107684ad9d587b1830d3eb56973e6a54f456e67
```

</details>
