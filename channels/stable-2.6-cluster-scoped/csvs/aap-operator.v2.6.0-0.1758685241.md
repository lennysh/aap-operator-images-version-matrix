# `aap-operator.v2.6.0-0.1758685241`

[← Back to `stable-2.6-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.6-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.6.0+0.1758685241` |
| **Build date** | 2025-09-24 |
| **Replaces** | — |
| **Skip range** | `>=2.4.0-0.1727259094 <2.6.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c1e70f7f62d0f4b8ad5a5b35be267c4252ead44822267a0e983bc16d9a94de9e` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9` | 4.7.1 | 4 | 2025-09-23 | `sha256:64f5e77a7842` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator` | 2.6 | 42 | 2025-09-23 | `sha256:863e77e52ab0` |
| eda | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9` | 1.2.0 | 147 | 2025-09-23 | `sha256:01e56bee772d` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator` | 2.6 | 32 | 2025-09-23 | `sha256:bfd55bffd823` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9` | 1.2.0 | 141 | 2025-09-24 | `sha256:5b5f38a5f767` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9` | 1.0.0 | 973 | 2025-09-24 | `sha256:261c324cac08` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 1.0.0 | 1096 | 2025-09-24 | `sha256:2534d07f1ae4` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 1.0.0 | 1096 | 2025-09-24 | `sha256:2534d07f1ae4` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 1.0.0 | 1096 | 2025-09-24 | `sha256:2534d07f1ae4` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9` | 2.6.6 | 5 | 2025-09-23 | `sha256:13284d20c6fb` |
| gateway | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9` | 2.6.20251001 | 1 | 2025-09-23 | `sha256:c85dbbf6beaa` |
| manager | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator` | 2.6 | 79 | 2025-09-23 | `sha256:fa1b102a0690` |
| hub | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9` | 4.11.0 | 159 | 2025-09-23 | `sha256:8041b141cd89` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator` | 2.6 | 39 | 2025-09-23 | `sha256:18114aab6db0` |
| hub_web | `registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9` | 4.11.0 | 150 | 2025-09-24 | `sha256:aa4041672542` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9` | 2.6 | 76 | 2025-09-23 | `sha256:8901fba14b21` |
| ansible_ai_connect_chatbot_rag_db | `registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9` | 2.6 | 76 | 2025-09-23 | `sha256:8901fba14b21` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9` | 2.6.250924 | 3 | 2025-09-24 | `sha256:c5d4e2e76944` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator` | 2.6 | 108 | 2025-09-23 | `sha256:cfbb98e17297` |
| ansible_ai_connect_chatbot_mcp_controller | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 3 | 2025-09-23 | `sha256:0c1f6f6958f2` |
| ansible_ai_connect_chatbot_mcp_gateway | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 3 | 2025-09-23 | `sha256:0c1f6f6958f2` |
| ansible_ai_connect_chatbot_mcp_lightspeed | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 3 | 2025-09-23 | `sha256:0c1f6f6958f2` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator` | 2.6 | 20 | 2025-09-23 | `sha256:969bbd033fbb` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9` | 2.6 | 67 | 2025-09-24 | `sha256:9983043386df` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.6 | 641 | 2025-09-24 | `sha256:c1e70f7f62d0` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9` | v4.18.0 | 202509100344.p2.g5a14ea9.assembly.stream.el9 | 2025-09-10 | `sha256:467557f453bd` |
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
registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator@sha256:863e77e52ab01cec2a71672a224080a59d963d4fc08b9ed6f3cc7950729b1746
registry.redhat.io/ansible-automation-platform-26/controller-rhel9@sha256:64f5e77a7842965e9c6f7bc7990354b71bb19ffb06ab8ef7793dde956cb6c0f0
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator@sha256:bfd55bffd8239e224d4ebba500d8517e8e66915078d6b59244f5e910fc5e10c8
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9@sha256:01e56bee772d15b120d6e4b02a59024b21eb8b266127b1a9b7f2c535ecdb2855
registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9@sha256:5b5f38a5f76781a042eec9cbf70b8be026878e4fa61c7fb90d1b0ad64bd21592
registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9@sha256:261c324cac081e47d559c5fccbd48e7ec8f5bf64e3f27287fbe4fb8aff6b7d99
registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9@sha256:2534d07f1ae41af32adb681e283cbaea465cbe0f9d234ed5478a7bfad7676e7f
registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9@sha256:13284d20c6fb4f2de24ec1715e7abdb5c4b0e4298c5034a7795f494b93634a02
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator@sha256:fa1b102a0690767a1e08935a0e164c1eabb2d4cf9afccd310262ee9185544de7
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9@sha256:c85dbbf6beaa264afec480dc1f06576aada531cdfd15f247f4db37dc9702be33
registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator@sha256:18114aab6db0d00780fdeaf9efa74ee44cab94824c2fd35f4b9998b6378ad8b3
registry.redhat.io/ansible-automation-platform-26/hub-rhel9@sha256:8041b141cd8921aaaa20cce15eab4c6189da9f449d99057189284891c071ac3b
registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9@sha256:aa4041672542a7f828d8a51c79e9c4dcea2a185388e4f20f828104db37e03a9b
registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9@sha256:8901fba14b21569b02108d2ab9050d558dee29f8177fae9d1bfcd5de3f4ce7c1
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator@sha256:cfbb98e17297134c187673f355342ac5ad60a56d73f4b0c918be2ff244286cc0
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9@sha256:c5d4e2e76944e0991729e5c3b99f43b7f29ea08ad112e5e6513feb8fb1d899a1
registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9@sha256:0c1f6f6958f2570c8cd073287555d28c70ef9dded702ec014d3ead8ce572463e
registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator@sha256:969bbd033fbba33624329ee9347b3b89fb5a1f64e71892f5c6c7d74ed14a6d39
registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9@sha256:9983043386df38a17ff6fffef64dc187691e0b1fefec01eef3af39aa08e532ef
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c1e70f7f62d0f4b8ad5a5b35be267c4252ead44822267a0e983bc16d9a94de9e
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9@sha256:467557f453bde3feaa0129f38c52fba00c3b98acddbf8978bf21ef13a9890fab
registry.redhat.io/rhel9/postgresql-15@sha256:5e225c1646251d2509b3a6e45fad23abfb11dd5c45d3224b59178f90deb38a70
registry.redhat.io/rhel9/redis-6@sha256:0962d18bb5292c0e524354f319b63287c2298a4a2fd34556c68fa285df381427
registry.redhat.io/ubi9/ubi-minimal@sha256:7c5495d5fad59aaee12abc3cbbd2b283818ee1e814b00dbc7f25bf2d14fa4f0c
```

</details>
