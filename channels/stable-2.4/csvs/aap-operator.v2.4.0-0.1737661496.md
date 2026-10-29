# `aap-operator.v2.4.0-0.1737661496`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1737661496` |
| **Build date** | 2025-01-23 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1733943951`](./aap-operator.v2.4.0-0.1733943951.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c62fc7d053bcf9e6cabcf3f385a341f476ae2fe955087845fdb6eb0fe996cad4` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.17 | 2 | 2025-01-23 | `sha256:7b59f459ecde` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 167 | 2025-01-23 | `sha256:176fa7f0e832` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 31 | 2025-01-23 | `sha256:40f86e657009` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 167 | 2025-01-23 | `sha256:ec037d2f8c53` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 30 | 2025-01-23 | `sha256:04202f549fbd` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 809 | 2025-01-23 | `sha256:2ce32d6402d8` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 887 | 2025-01-23 | `sha256:880dadb7f632` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 887 | 2025-01-23 | `sha256:880dadb7f632` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 887 | 2025-01-23 | `sha256:880dadb7f632` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 35 | 2025-01-23 | `sha256:32ae921cb77b` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 166 | 2025-01-23 | `sha256:8fb4120ecdac` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 33 | 2025-01-23 | `sha256:1480156f8b7a` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250121 | 2 | 2025-01-23 | `sha256:fcaeb3add704` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 33 | 2025-01-23 | `sha256:aeddb89da1bd` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 160 | 2025-01-23 | `sha256:901ddae77326` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 200 | 2025-01-23 | `sha256:ce4229427f10` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2300 | 2025-01-23 | `sha256:c62fc7d053bc` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202501021509.p0.g9308e7f.assembly.stream.el8 | 2025-01-02 | `sha256:38ee3484ba60` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 212.1735831616 | 2025-01-02 | `sha256:8f9ed84a0811` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 212.1735831616 | 2025-01-02 | `sha256:8f9ed84a0811` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 212.1735831616 | 2025-01-02 | `sha256:8f9ed84a0811` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 212.1735831616 | 2025-01-02 | `sha256:8f9ed84a0811` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 211.1735831615 | 2025-01-02 | `sha256:274133466125` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 211.1735831615 | 2025-01-02 | `sha256:274133466125` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 211.1735831615 | 2025-01-02 | `sha256:274133466125` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1154 | 2024-12-10 | `sha256:cf095e566891` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1154 | 2024-12-10 | `sha256:cf095e566891` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1154 | 2024-12-10 | `sha256:cf095e566891` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:176fa7f0e832932f5ae0179d80853f51f93ad7168b543b29fb7b7b176a457c5a
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:7b59f459ecde53cf4a0e014fe1f593dbb45fb37086ce80c2ba5d0bb6f6b72d47
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:ec037d2f8c5326664e28385436b548dd89699f9a0ed87f8dc3dc72d5296024b0
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:40f86e657009f85b1e4f2ea71342b6b5674cd81ed76b33e8b3a3c153ad9b2d14
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:04202f549fbd64be1bc78343100b0352467402d529e7164285cc10fbb116a49a
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:2ce32d6402d87799d638bc8dc253f85b108162df0fc9401660f6d32d043353e0
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:880dadb7f632ba574721e94aaa1909993ec7b36101001101395a26d1ae379627
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:8fb4120ecdacdc2105a2fc0dca133424a9116fae66435200e9b64f65ac32bead
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:32ae921cb77bdbd2f939aac019611be2fc7fca711e1122340c394abac9f2b282
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:1480156f8b7af56646a7f09538bf83e3f96745ac21f41ab667f1021f391d072b
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:aeddb89da1bd51e43d2d04a12c43fbb56d56012781ff22a621f31db07490a908
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:fcaeb3add7042c12023de2797750ae83ed96c9c0629ed7fa9a852179bf71ad69
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:901ddae7732698bf956cdbe1157521d6cc1802468d87421e8a1f309858f48fb2
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:ce4229427f106c01c10cf95d58a76d73b5efbac410dc81dd54f1f637bc6e315c
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c62fc7d053bcf9e6cabcf3f385a341f476ae2fe955087845fdb6eb0fe996cad4
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:38ee3484ba60bb474e7231e9d0718157386716cea7ffd6da6f32ddd551a5243d
registry.redhat.io/rhel8/postgresql-13@sha256:8f9ed84a0811a9d2c92b0c4fa7a8bc5ff061ee889fd0c4d9c90a2d9af956f26c
registry.redhat.io/rhel8/redis-6@sha256:27413346612521f4d74783136fd7723b05a3b31fc8b07fe16d33acde0720516e
registry.redhat.io/ubi8/ubi-minimal@sha256:cf095e5668919ba1b4ace3888107684ad9d587b1830d3eb56973e6a54f456e67
```

</details>
