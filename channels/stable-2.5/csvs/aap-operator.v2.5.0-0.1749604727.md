# `aap-operator.v2.5.0-0.1749604727`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1749604727` |
| **Build date** | 2025-06-11 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1749074128`](./aap-operator.v2.5.0-0.1749074128.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:37452599772d46edd9749f2ffc827dc6c676226facead89e985f0a7b42e270c3` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.15 | 7 | 2025-06-11 | `sha256:919777713928` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 182 | 2025-05-28 | `sha256:0ba81c4d4d55` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.9 | 10 | 2025-05-28 | `sha256:7694eb4c70ad` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 181 | 2025-05-28 | `sha256:748c6fc43415` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.9 | 1 | 2025-05-28 | `sha256:6da16cfa7c3a` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 922 | 2025-05-28 | `sha256:7d2df3be0924` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1032 | 2025-06-04 | `sha256:3dc96de170d9` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1032 | 2025-06-04 | `sha256:3dc96de170d9` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1032 | 2025-06-04 | `sha256:3dc96de170d9` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 31 | 2025-05-28 | `sha256:c30dd12823cb` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250604 | 1 | 2025-05-28 | `sha256:565eda0263dd` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 237 | 2025-05-28 | `sha256:aabe548dadce` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.4 | 15 | 2025-05-28 | `sha256:51044c492650` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 181 | 2025-05-28 | `sha256:58ab076660cf` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.4 | 14 | 2025-05-28 | `sha256:79110818855e` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250604 | 1 | 2025-05-28 | `sha256:f15787e71a8a` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250604 | 1 | 2025-05-28 | `sha256:ae014bc4ebf9` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 142 | 2025-05-28 | `sha256:7c26a392f5a1` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 136 | 2025-05-28 | `sha256:dd5adbc30eb3` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 183 | 2025-06-04 | `sha256:bc9f590360af` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1410 | 2025-06-11 | `sha256:37452599772d` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202504220035.p0.g9308e7f.assembly.stream.el8 | 2025-04-22 | `sha256:bb84ead43704` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749482736 | 2025-06-09 | `sha256:dd4aec2775da` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749482736 | 2025-06-09 | `sha256:dd4aec2775da` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749482736 | 2025-06-09 | `sha256:dd4aec2775da` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749482736 | 2025-06-09 | `sha256:dd4aec2775da` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 93.1749482736 | 2025-06-09 | `sha256:dd4aec2775da` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749482732 | 2025-06-09 | `sha256:7d69c4d214cc` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749482732 | 2025-06-09 | `sha256:7d69c4d214cc` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749482732 | 2025-06-09 | `sha256:7d69c4d214cc` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215.1749482732 | 2025-06-09 | `sha256:7d69c4d214cc` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295 | 2025-05-29 | `sha256:73064ec359dc` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295 | 2025-05-29 | `sha256:73064ec359dc` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295 | 2025-05-29 | `sha256:73064ec359dc` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:0ba81c4d4d556d70d60b95e949d1c72a7fb45d17997865b33ecd3e124c065679
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:919777713928a849dd1ea550a834ddbe5c363c1d203e7e8bf184ca1f36b3c03c
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:748c6fc4341524a9e0b96eb308eb5d3e602a2654d38acacf26190f1e1f797297
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:7694eb4c70ad792ba5a41db154db85c730673b7cdd4bdbc923ca2c715ee72de9
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:6da16cfa7c3ada33ce77bfbdbb6b74ab73112adf4d7b2f76daad94c25ad57f96
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:7d2df3be0924c78258d974dde537b0a1654e1c4abbcc5f86916502eb89cb7949
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:3dc96de170d94be895de8f872015f4761420565a22182dc21cff71245cade94d
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:c30dd12823cbcb3ed2878cc38b5cffc27d2d2ac9cb1816f6be171cfaf738b5a0
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:aabe548dadce020e1100cef42ad64820d152e11f68acaff01ea076a39f85cdd4
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:565eda0263dd2e8820806b920c043c772a7b224960e2481faf794e155b61d556
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:58ab076660cfb5e5ec887181c1978416bb895693cb7518e948f95832ae37cca5
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:51044c49265013cce66b01cc2405b82baa5dceb206a2ee0d6dc4a83444f3a601
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:79110818855eeab74aeddfa5e797acbeb5fcfe28871ddfebe35f37016cd9ef1e
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:f15787e71a8a54f0ad63f84ac957daa48b487ccfa4d60eab5bbbee034de190fe
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:7c26a392f5a135dd0063c21ef1640a83ac6dc07bc86d9528fb281d1e3d2275c6
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:ae014bc4ebf91adcdb8872bde419f6c06f396c6e15a445d25a54665192f364af
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:dd5adbc30eb321891c0bd8cd7075ec79c1e04d4cb094251aa9647158932d5646
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:bc9f590360af50ee4a39c9efe149ca2fb2e58385b023f594adf04b260173abc8
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:37452599772d46edd9749f2ffc827dc6c676226facead89e985f0a7b42e270c3
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:bb84ead437042603254efcb703442be8500a9450b10bbcaaee81b48a6ed869ea
registry.redhat.io/rhel8/postgresql-15@sha256:dd4aec2775da1cf187c0839384cb16d69268e9781d4330874bbc865f98153a7a
registry.redhat.io/rhel8/redis-6@sha256:7d69c4d214cca97b6dddab320ccabcd48cf6ed529d3fcca4aa07c87c7c6bc68a
registry.redhat.io/ubi8/ubi-minimal@sha256:73064ec359dcd71e56677f8173a134809c885484ba89e6a137d33521ad29dd4c
```

</details>
