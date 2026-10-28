# `aap-operator.v2.5.0-0.1739248042`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1739248042` |
| **Build date** | 2025-02-11 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1737675968`](./aap-operator.v2.5.0-0.1737675968.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:73c8691b436c5d28ee7dc5bd338d05027809ba7fcf376d99ae94a2f29396d231` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.8 | 9 | 2025-02-11 | `sha256:47d7ba6ece4e` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 154 | 2025-02-11 | `sha256:441d5d59b1bb` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.4 | 10 | 2025-02-11 | `sha256:671bef930411` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 156 | 2025-02-11 | `sha256:4cf21a742f2e` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.4 | 5 | 2025-02-11 | `sha256:2653d66824de` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 823 | 2025-02-11 | `sha256:c8f96573ec2c` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 907 | 2025-02-11 | `sha256:2d301e895487` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 907 | 2025-02-11 | `sha256:2d301e895487` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 907 | 2025-02-11 | `sha256:2d301e895487` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 45 | 2025-02-11 | `sha256:7f4f9267f35c` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250213 | 3 | 2025-02-11 | `sha256:f08fb99ef0d8` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 203 | 2025-02-11 | `sha256:ba00c37b38fc` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 31 | 2025-02-11 | `sha256:15b1c8c7a9fc` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 157 | 2025-02-11 | `sha256:6605dbf004a5` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 29 | 2025-02-11 | `sha256:482d5b681c90` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250204 | 3 | 2025-02-11 | `sha256:6c7b2b31720b` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 115 | 2025-02-11 | `sha256:10a4c62c1870` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 110 | 2025-02-11 | `sha256:206e874c1b0c` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 141 | 2025-02-11 | `sha256:1e2c3d36152d` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1117 | 2025-02-11 | `sha256:73c8691b436c` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202501150635.p0.g9308e7f.assembly.stream.el8 | 2025-01-15 | `sha256:98455d503b79` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90 | 2025-01-21 | `sha256:cf566f25ee67` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90 | 2025-01-21 | `sha256:cf566f25ee67` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90 | 2025-01-21 | `sha256:cf566f25ee67` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90 | 2025-01-21 | `sha256:cf566f25ee67` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90 | 2025-01-21 | `sha256:cf566f25ee67` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212 | 2025-01-21 | `sha256:343b7f7cf8a1` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212 | 2025-01-21 | `sha256:343b7f7cf8a1` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212 | 2025-01-21 | `sha256:343b7f7cf8a1` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212 | 2025-01-21 | `sha256:343b7f7cf8a1` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179 | 2025-01-21 | `sha256:d16d4445b156` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179 | 2025-01-21 | `sha256:d16d4445b156` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179 | 2025-01-21 | `sha256:d16d4445b156` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:441d5d59b1bb8c3db034759c4e42c4c8db2df5549abec843cf33f9f6fdfb8cf9
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:47d7ba6ece4edede45beaef43ab65b7c5f79d57baadc97b20ef507c0eeea70b9
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:4cf21a742f2e5a6fab742452f5502444dbf4d085342405b1b28daec09962f95f
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:671bef930411997d57c8f96b89e563590602218c4df61b817727fa5704d3ff70
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:2653d66824de28a383acf717b4b313549488d2de01e5f0cfe348b4e9a344997d
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:c8f96573ec2c7f73ebdb1d62fc5c8354759f5eb55e85c6ab788bf8c64bcab35d
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:2d301e895487b6afdde2a4fea7d4ebbd38a5a54c1502b161918499b7b7945b61
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:7f4f9267f35c910b9dbce34c33203fb24329fbaabe52f830dab4c91141359474
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:ba00c37b38fc0e509231886f9ed1971bf48b39a4b6e9bbc2bc631ed14dd02769
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:f08fb99ef0d8c39600577f86658f39fc0046e01cf24c16897b975a5241cc83ed
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:6605dbf004a5f7b3a70f706eb6d89ea3df9dbbc50faba2a8f37465eb58da945b
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:15b1c8c7a9fca3c31648f037806b42443d64d23d66ec947f2811bdb97f7f31b0
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:482d5b681c902e6c46f77d0ff8668c24f93025d73c6f9f53e758eb16cfbb580d
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:10a4c62c1870c89aca0ecf619eb7d48a4269b34c23b9d03196e48d19acaa3580
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:6c7b2b31720bde534c720769ec4165886aa83b5890eba38d52decdf90ee7af2e
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:206e874c1b0cd79bf1a29766dfc6b7b79ed532da62925bf6c0a8db56c8d95662
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:1e2c3d36152d8bbe4237461068a61ee4bf54ed73022cc02e4c60d7f1796fa8a2
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:73c8691b436c5d28ee7dc5bd338d05027809ba7fcf376d99ae94a2f29396d231
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:98455d503b797b6b02edcfd37045c8fab0796b95ee5cf4cfe73b221a07e805f0
registry.redhat.io/rhel8/postgresql-15@sha256:cf566f25ee67d2733123cf5a8b62397f4f2191c28b8bf814aa71418d4ee8bf23
registry.redhat.io/rhel8/redis-6@sha256:343b7f7cf8a1e8a8e9f275238a1abae5ad328293291f718f0f0a9de9cf14df27
registry.redhat.io/ubi8/ubi-minimal@sha256:d16d4445b1567f29449fba3b6d2bc37db467dc3067d33e940477e55aecdf6e8e
```

</details>
