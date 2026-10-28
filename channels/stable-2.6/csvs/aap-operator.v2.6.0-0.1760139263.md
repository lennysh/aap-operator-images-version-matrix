# `aap-operator.v2.6.0-0.1760139263`

[← Back to `stable-2.6`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.6` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.6.0+0.1760139263` |
| **Build date** | 2025-10-10 |
| **Replaces** | [`aap-operator.v2.6.0-0.1759764484`](./aap-operator.v2.6.0-0.1759764484.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.6.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:55b5f9f2e8f2670a093374646e0a81668975398c09abc69c127331d065e0f491` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9` | 4.7.2 | 9 | 2025-10-10 | `sha256:310b8599791a` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator` | 2.6 | 44 | 2025-10-10 | `sha256:d1527adcbf8c` |
| eda | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9` | 1.2.0 | 148 | 2025-10-10 | `sha256:645af99ddbdc` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator` | 2.6 | 34 | 2025-10-10 | `sha256:68b8a6a73490` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9` | 1.2.0 | 142 | 2025-10-10 | `sha256:ebf2f051c1c1` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9` | 1.0.0 | 978 | 2025-10-10 | `sha256:a17ebe09a69f` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 1.0.0 | 1103 | 2025-10-10 | `sha256:8b51f6026000` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 1.0.0 | 1103 | 2025-10-10 | `sha256:8b51f6026000` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 1.0.0 | 1103 | 2025-10-10 | `sha256:8b51f6026000` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9` | 2.6.6 | 12 | 2025-10-10 | `sha256:214253c927d3` |
| gateway | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9` | 2.6.20251016 | 1 | 2025-10-10 | `sha256:348b8e4001a7` |
| manager | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator` | 2.6 | 86 | 2025-10-10 | `sha256:178ef639beef` |
| hub | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9` | 4.11.1 | 1 | 2025-10-10 | `sha256:37f802ae98db` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator` | 2.6 | 41 | 2025-10-10 | `sha256:46d09992e304` |
| hub_web | `registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9` | 4.11.1 | 1 | 2025-10-10 | `sha256:6679af41bdee` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9` | 2.6 | 82 | 2025-10-10 | `sha256:90c45286053e` |
| ansible_ai_connect_chatbot_rag_db | `registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9` | 2.6 | 82 | 2025-10-10 | `sha256:90c45286053e` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9` | 2.6.250924 | 4 | 2025-10-10 | `sha256:dc13b942eb2e` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator` | 2.6 | 112 | 2025-10-10 | `sha256:fa080d0b8d2d` |
| ansible_ai_connect_chatbot_mcp_controller | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 4 | 2025-10-10 | `sha256:88f04dfe7d92` |
| ansible_ai_connect_chatbot_mcp_gateway | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 4 | 2025-10-10 | `sha256:88f04dfe7d92` |
| ansible_ai_connect_chatbot_mcp_lightspeed | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 4 | 2025-10-10 | `sha256:88f04dfe7d92` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator` | 2.6 | 24 | 2025-10-10 | `sha256:ec53f1320898` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9` | 2.6 | 72 | 2025-10-10 | `sha256:15125ef10a8a` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.6 | 694 | 2025-10-10 | `sha256:55b5f9f2e8f2` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9` | v4.18.0 | 202509240837.p2.g5a14ea9.assembly.stream.el9 | 2025-09-24 | `sha256:784c4667a867` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel9/postgresql-15` | 1 | 1758514462 | 2025-09-22 | `sha256:5e225c164625` |
| controller_postgres | `registry.redhat.io/rhel9/postgresql-15` | 1 | 1758514462 | 2025-09-22 | `sha256:5e225c164625` |
| eda_postgres | `registry.redhat.io/rhel9/postgresql-15` | 1 | 1758514462 | 2025-09-22 | `sha256:5e225c164625` |
| gateway_postgres | `registry.redhat.io/rhel9/postgresql-15` | 1 | 1758514462 | 2025-09-22 | `sha256:5e225c164625` |
| hub_postgres | `registry.redhat.io/rhel9/postgresql-15` | 1 | 1758514462 | 2025-09-22 | `sha256:5e225c164625` |
| controller_redis | `registry.redhat.io/rhel9/redis-6` | 1 | 1758530358 | 2025-09-22 | `sha256:0962d18bb529` |
| eda_redis | `registry.redhat.io/rhel9/redis-6` | 1 | 1758530358 | 2025-09-22 | `sha256:0962d18bb529` |
| gateway_redis | `registry.redhat.io/rhel9/redis-6` | 1 | 1758530358 | 2025-09-22 | `sha256:0962d18bb529` |
| hub_redis | `registry.redhat.io/rhel9/redis-6` | 1 | 1758530358 | 2025-09-22 | `sha256:0962d18bb529` |
| controller_init_projects_container | `registry.redhat.io/ubi9/ubi-minimal` | 9.6 | 1758184547 | 2025-09-18 | `sha256:7c5495d5fad5` |
| eda_init_container | `registry.redhat.io/ubi9/ubi-minimal` | 9.6 | 1758184547 | 2025-09-18 | `sha256:7c5495d5fad5` |
| hub_init_gpg_container | `registry.redhat.io/ubi9/ubi-minimal` | 9.6 | 1758184547 | 2025-09-18 | `sha256:7c5495d5fad5` |

## Image pull specs

<details><summary>All 24 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator@sha256:d1527adcbf8c00eda9d690c928ce7df2fa1c1798d7ce5620689b141b5bc769f4
registry.redhat.io/ansible-automation-platform-26/controller-rhel9@sha256:310b8599791a0642898b06ac2e2638edb55dffbad364c135fb56b2eea9614c46
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator@sha256:68b8a6a7349050844d96d8ffbe0cac083c3d3017f85fe6746a40c381a2de66b0
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9@sha256:645af99ddbdcd2ce7d5fdaf041950eaf3ea7b16f954c91e65a7e2bd5e890cf61
registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9@sha256:ebf2f051c1c1e178b1fd83c89dcabe22876760c7aead5d427311d7b6015c7569
registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9@sha256:a17ebe09a69f28a183068c3597467311ba9ed77f1c3a42864404d5e343f7c2de
registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9@sha256:8b51f6026000a9f63e8d548e5d4c7b630425bc4504819ceeef97eea691653cd2
registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9@sha256:214253c927d3379c2a72ce7045c87f3943b874d6c94584b10a0e07ab77b66cae
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator@sha256:178ef639beef764bd7a4688be3021f7c17fad5f73efbcbaafbdaf2d17124e38e
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9@sha256:348b8e4001a7712f36bc3bca049deeaf29afa61b88f1f19c8a2daaeef9793457
registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator@sha256:46d09992e304fda678de50e2bd31c31a3f6c4217d6e5149ac6b9e5205efff7fb
registry.redhat.io/ansible-automation-platform-26/hub-rhel9@sha256:37f802ae98dba3d78df5f9d3001294de49fdfd6432997472cb4ef1bd93ecb92b
registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9@sha256:6679af41bdee94b11cfdb011274c43125ebb3475687e146e6add48a96f924839
registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9@sha256:90c45286053e36bf52fb3ddf25d9eba9d146ce42e3bb8e56bb2d3513b5d43bc4
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator@sha256:fa080d0b8d2dceb2edb5b7d5639725fd6598ac2c885b7f6281af458d88b0970e
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9@sha256:dc13b942eb2ee391116f377704aab693d55608d4082a47872a0c2e3390ecfd11
registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9@sha256:88f04dfe7d928a74dfa930f4a3859ddd98996238d56aac433a3c25b29af5f4a4
registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator@sha256:ec53f1320898d4714db6cb0637609ad018939061461cd5de308142227f833747
registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9@sha256:15125ef10a8a27eeb30101021a668d0ed8b8f28b4bbb19d7a4bb1b2016bed0ba
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:55b5f9f2e8f2670a093374646e0a81668975398c09abc69c127331d065e0f491
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9@sha256:784c4667a867abdbec6d31a4bbde52676a0f37f8e448eaae37568a46fcdeace7
registry.redhat.io/rhel9/postgresql-15@sha256:5e225c1646251d2509b3a6e45fad23abfb11dd5c45d3224b59178f90deb38a70
registry.redhat.io/rhel9/redis-6@sha256:0962d18bb5292c0e524354f319b63287c2298a4a2fd34556c68fa285df381427
registry.redhat.io/ubi9/ubi-minimal@sha256:7c5495d5fad59aaee12abc3cbbd2b283818ee1e814b00dbc7f25bf2d14fa4f0c
```

</details>
