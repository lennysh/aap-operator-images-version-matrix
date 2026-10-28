# `aap-operator.v2.5.0-0.1750901111`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1750901111` |
| **Build date** | 2025-06-26 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1749604727`](./aap-operator.v2.5.0-0.1749604727.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:bcd18a86b1ca2f62177bb66a72ec2a4fcd58b49411635e3b725c4b934e59ee2e` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.16 | 9 | 2025-06-25 | `sha256:f5c17f6a3106` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 184 | 2025-06-25 | `sha256:f27af6a96421` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.11 | 1 | 2025-06-25 | `sha256:7b034614cca7` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 184 | 2025-06-25 | `sha256:88f7ac25161c` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.11 | 1 | 2025-06-25 | `sha256:3318fe01f065` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 936 | 2025-06-25 | `sha256:fc67e07764d8` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1048 | 2025-06-25 | `sha256:3bcd54957ba5` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1048 | 2025-06-25 | `sha256:3bcd54957ba5` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1048 | 2025-06-25 | `sha256:3bcd54957ba5` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 47 | 2025-06-25 | `sha256:e9c3a0338858` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250702 | 1 | 2025-06-25 | `sha256:10c79502d33e` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 241 | 2025-06-25 | `sha256:ec8475ab4fff` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.5 | 1 | 2025-06-25 | `sha256:bf061436f642` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 183 | 2025-06-25 | `sha256:9fd403e2c90a` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.5 | 1 | 2025-06-25 | `sha256:f0d0ed6a4190` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250702 | 1 | 2025-06-25 | `sha256:8beac0a0dbb9` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250702 | 1 | 2025-06-25 | `sha256:f3312a9a4e1c` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 143 | 2025-06-25 | `sha256:8ba9448fa328` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 137 | 2025-06-25 | `sha256:d1819d6c8ae3` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 188 | 2025-06-26 | `sha256:cc7fadfaafe4` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1450 | 2025-06-26 | `sha256:bcd18a86b1ca` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202506112235.p0.g9308e7f.assembly.stream.el8 | 2025-06-12 | `sha256:f15d124e4868` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749685130 | 2025-06-11 | `sha256:ffdee937e972` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749685126 | 2025-06-11 | `sha256:3ee676ec769c` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749685126 | 2025-06-11 | `sha256:3ee676ec769c` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749685126 | 2025-06-11 | `sha256:3ee676ec769c` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749685126 | 2025-06-11 | `sha256:3ee676ec769c` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295.1749680713 | 2025-06-11 | `sha256:fceb1f445ccd` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295.1749680713 | 2025-06-11 | `sha256:fceb1f445ccd` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295.1749680713 | 2025-06-11 | `sha256:fceb1f445ccd` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:f27af6a96421e6b836572b93ff2d669eb6c64599bd589e5aea921bac292d7146
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:f5c17f6a3106adba06a4ba5b16d538d5b6fa3f223cacdc0fc274f200dc4af07d
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:88f7ac25161c1c15035438df9348887e253d6d5325fd664a9244416c77a670d1
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:7b034614cca7a0d8730e00591d6b4cdd12490f85b5243024f5ccf1aece015694
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:3318fe01f065b092fe9143e00ecec89fcbf68257ef466abd9df1307097e29a8c
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:fc67e07764d83e592009a6cb0318d5542910f249863a147f8b43a339835137e8
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:3bcd54957ba5fcc3e542a70f8f9c2127cf5cc22f9f7b4145d461e7aee40146ac
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:e9c3a033885860495bd06b2da9fe674f69b2e96571bf7d145d5fc388632f8693
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:ec8475ab4fffea14989539e4a0ef23cb40faad7d6a01a1f91354b137bce3caa2
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:10c79502d33e6061e5038a66abdf45dcec555b3cc75c60f81935be53bb72cc80
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:9fd403e2c90ae77ea6b5eab1173fd8744c7db8e0bbc2859a1913833d3410456d
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:bf061436f642041250fceb947a4298c109235f041eea2fd0694eb991fc1eda93
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:f0d0ed6a4190adeed8a5720a91de9244e11d736a0a2b0fed97e0c67ead135727
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:8beac0a0dbb9ea05919da8bbdbbe4c0fee31adfe2f19369a3a35a0e1f2f8afe1
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:8ba9448fa32867613c13faf1ac59bab0c58dd197b1cc4b1e0df4bdc1040ecf14
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:f3312a9a4e1c05bb9c5255c57c54e3764d9e3e1c9701447c64ab6a0369d34f08
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:d1819d6c8ae389c1c6875c868f76685d48d5fd3d947a9a9032294a72814c02f0
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:cc7fadfaafe466ff139afe0cae9b51c82bdc42eaa0cedf9754663b0b9cdc5237
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:bcd18a86b1ca2f62177bb66a72ec2a4fcd58b49411635e3b725c4b934e59ee2e
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:f15d124e4868a4f3ee30141535abc7f2654a3707f8595fd28bbc9ab0d366c9df
registry.redhat.io/rhel8/postgresql-15@sha256:ffdee937e9726f3214bd3ba2070487291b0e43d53301ca16900b8af905c680d5
registry.redhat.io/rhel8/redis-6@sha256:3ee676ec769c5f5ece69ad14f66b96a99db603982628510eb878bb4b5ca61371
registry.redhat.io/ubi8/ubi-minimal@sha256:fceb1f445ccd61a60d91d404fd76dbebaf3403e6cc2219cf6d6af4fd4bf7df6a
```

</details>
