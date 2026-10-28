# `aap-operator.v2.4.0-0.1753232084`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1753232084` |
| **Build date** | 2025-07-23 |
| **Replaces** | [`aap-operator.v2.4.0-0.1750877268`](./aap-operator.v2.4.0-0.1750877268.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:4663962837129477519d02e9c3b42374ad604ce7bdc25e65cccf9197a6af7380` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.24 | 2 | 2025-07-22 | `sha256:22d55931673c` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 178 | 2025-07-22 | `sha256:7926dcbb35d4` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 41 | 2025-07-22 | `sha256:acc503607edf` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 178 | 2025-07-22 | `sha256:41891e884088` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 39 | 2025-07-22 | `sha256:ffeef3719ca8` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 940 | 2025-07-22 | `sha256:82ffe7398b8e` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1057 | 2025-07-22 | `sha256:e2e6e632dca3` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1057 | 2025-07-22 | `sha256:e2e6e632dca3` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1057 | 2025-07-22 | `sha256:e2e6e632dca3` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.4 | 3 | 2025-07-22 | `sha256:f18ac56b050e` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 178 | 2025-07-22 | `sha256:7039656387a7` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.4 | 3 | 2025-07-22 | `sha256:b9b3437d9a99` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 14 | 2025-07-22 | `sha256:c43df4380a2e` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 47 | 2025-07-22 | `sha256:f375fb3cf9a5` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 174 | 2025-07-22 | `sha256:aae60793f301` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 215 | 2025-07-23 | `sha256:3e1d64df22b6` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2679 | 2025-07-23 | `sha256:466396283712` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202507012239.p0.g9308e7f.assembly.stream.el8 | 2025-07-02 | `sha256:71c2421379d1` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1752582967 | 2025-07-15 | `sha256:a67ae298cc00` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1752582967 | 2025-07-15 | `sha256:a67ae298cc00` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1752582967 | 2025-07-15 | `sha256:a67ae298cc00` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1752582967 | 2025-07-15 | `sha256:a67ae298cc00` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1752582033 | 2025-07-15 | `sha256:753206aa7c32` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1752582033 | 2025-07-15 | `sha256:753206aa7c32` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1752582033 | 2025-07-15 | `sha256:753206aa7c32` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1752564239 | 2025-07-15 | `sha256:5b195cf0b8eb` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1752564239 | 2025-07-15 | `sha256:5b195cf0b8eb` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1752564239 | 2025-07-15 | `sha256:5b195cf0b8eb` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:7926dcbb35d44c99cc24e34cb0ada46efaaeaa1fa2431d1d7302ad2b0d649939
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:22d55931673c97f75f3f9b94007264bcc5b89f1a71e68559581460a584289f72
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:41891e884088861f234a256bc75ba0ff8a6b8cf48770755d5b03c81dedd4448c
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:acc503607edf125808fba5e8e7beb8b79b0a5f52de19411233e6e92f885b0b5b
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:ffeef3719ca8801f0e4e3fe814efda01fdc9633f71365e06568af3ce10abe6a0
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:82ffe7398b8ec9da5d6fa22917a8c2aee15839ee2304191bce8ad5d47ae439be
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:e2e6e632dca397ffc4a4715f29bbec455ee56fd87ca7a7bd52c6b3df7f45b93d
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:7039656387a777eece3389956397efe62d7cc31ef9bff665e2d1bf31ce5dcb36
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:f18ac56b050e5be53275924794668ab2fcf6c3b49e5d8a83fee70726f2abd73c
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:b9b3437d9a99b8c24e634c6cc4b900229ef394defcd331495dff9e5730cfae77
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:f375fb3cf9a5a215e7382357db05fb97a0929720082135934a06366ee8b65d23
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:c43df4380a2e805cbf397efdb247974ce82c9305e14309eda2fdcd3edaac8553
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:aae60793f301d2770eaaadfe630c12f50a5f7afe98dfef6a7d31eaa75d2b1d68
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:3e1d64df22b637f20c55e4953d7dea7592dc8e9d40b5be5b6c4fd23769d0a280
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:4663962837129477519d02e9c3b42374ad604ce7bdc25e65cccf9197a6af7380
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:71c2421379d1573fd2b94d5d05809935db272465d6b5f9a4c4deb70ea53f1213
registry.redhat.io/rhel8/postgresql-15@sha256:a67ae298cc0078d23f2d186210fe444ea675b862fc314fd5837304838fc5b62d
registry.redhat.io/rhel8/redis-6@sha256:753206aa7c32415891bb42d08bd5c3b94ca7a30dee1d15a94ecd67b234c4a7d2
registry.redhat.io/ubi8/ubi-minimal@sha256:5b195cf0b8eb2262ce81334ee44066fdb5026022803f55bfe607be7d08d4fe43
```

</details>
