# `aap-operator.v2.4.0-0.1793164232`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1793164232` |
| **Build date** | 2026-10-28 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1791963300`](./aap-operator.v2.4.0-0.1791963300.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:856dd0e644071bb3bd5f26fcd859ea0774a059be24d7d0a5f4c3fd99c2195578` |
| **Seen in OCP operator indexes** | 4.12, 4.14, 4.16, 4.18–4.20 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.37 | 1793069394 | 2026-10-28 | `sha256:e4ba7ad3a878` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:81ed289742f0` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1793069394 | 2026-10-28 | `sha256:d27f90a45c4f` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:cfe05b9c0cd5` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1793101871 | 2026-10-28 | `sha256:ecc9c3aad00b` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1792742827 | 2026-10-27 | `sha256:120520cb91e4` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1792742827 | 2026-10-28 | `sha256:cfbb18bef3cf` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1792742827 | 2026-10-28 | `sha256:cfbb18bef3cf` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1792742827 | 2026-10-28 | `sha256:cfbb18bef3cf` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1793069394 | 2026-10-28 | `sha256:b31a68db2129` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:c0403f946495` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1793101871 | 2026-10-28 | `sha256:762d61d6088d` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1792742827 | 2026-10-27 | `sha256:2e075d0222e3` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:f81190022910` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:5a31fe6a3944` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1792742827 | 2026-10-28 | `sha256:773df2893379` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-10-28 | `sha256:856dd0e64407` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9` | v4.18.0 | 202610241849.p2.gf72b2ec.assembly.stream.el9 | 2026-10-24 | `sha256:81853fd2cdac` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793110152 | 2026-10-27 | `sha256:2f682aef9ce8` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793110152 | 2026-10-27 | `sha256:2f682aef9ce8` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793110152 | 2026-10-27 | `sha256:2f682aef9ce8` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793110152 | 2026-10-27 | `sha256:2f682aef9ce8` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1793089025 | 2026-10-27 | `sha256:e77651e8ae02` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1793089025 | 2026-10-27 | `sha256:e77651e8ae02` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1793089025 | 2026-10-27 | `sha256:e77651e8ae02` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1793069394 | 2026-10-27 | `sha256:cee9d1e3abf5` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1793069394 | 2026-10-27 | `sha256:cee9d1e3abf5` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1793069394 | 2026-10-27 | `sha256:cee9d1e3abf5` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:e4ba7ad3a87889b1da9739ae6dcc2f5d91910707ce515cae06db195a78bf8e70
registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator@sha256:81ed289742f0af669fd7dde60c2e1567658cdda80faea72da00645bbf3cb801f
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:d27f90a45c4f7315d70cdfc679ee114508c5da5305a018ec97e27a36eb5a5ffb
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator@sha256:cfe05b9c0cd5a0ddb53bcdb279da59340282d7ab5c84f851aa206760b6c39ab7
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:ecc9c3aad00b61a64d853a7edcdcdd56331e1539e0ff57de1370fb872fd00a93
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:120520cb91e4367fbcac0a3413489ab227ab7d1cd23ee576c474540c504eb1b4
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:cfbb18bef3cff016ecf7cea4d3e90f9c387821a1ccb38f9d5bf578ca24e63bd5
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:b31a68db2129ac4650c827cb709113b0076578b2ea3c7ea852023a6c9958c34e
registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator@sha256:c0403f94649582e06859b9374a442de5839981d4284ac30f1f65b57a91b7e030
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:762d61d6088d4933bfca0a370692d2c51bd998f24f756ab2ea992b5e718de619
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:2e075d0222e302e06fe6c7495a97e5416f776b1664d941a6b2624f9e19e35136
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator@sha256:f811900229105ca6d85b52011df02fcd96899bff6b6c899ff92cc0be27d51225
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator@sha256:5a31fe6a3944313a75d5ba0b677d15a90717946e7b6e17c1c207b73c1e46fb28
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:773df2893379983b486aaf3ef0d8029af015e811aa9be9baa3ecb522a92ae1be
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:856dd0e644071bb3bd5f26fcd859ea0774a059be24d7d0a5f4c3fd99c2195578
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9@sha256:81853fd2cdacb13900522e788191b12f67cdb763ec21607a4ec097b15fb8d012
registry.redhat.io/rhel8/postgresql-15@sha256:2f682aef9ce81bf49fd318f0e62fb23a07c1950cc85b60c8fbc0722bb2e1c8de
registry.redhat.io/rhel8/redis-6@sha256:e77651e8ae02eae188f5fa201a8ea2c530c6322c3c34908603f24f9517448af5
registry.redhat.io/ubi8/ubi-minimal@sha256:cee9d1e3abf52281e183c23d6a2fce99ba174cc11be2d17380cd9286dee4e543
```

</details>
