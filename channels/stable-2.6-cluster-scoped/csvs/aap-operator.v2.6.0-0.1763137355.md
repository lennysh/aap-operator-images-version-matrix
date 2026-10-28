# `aap-operator.v2.6.0-0.1763137355`

[← Back to `stable-2.6-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.6-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.6.0+0.1763137355` |
| **Build date** | 2025-11-14 |
| **Replaces** | [`aap-operator.v2.6.0-0.1762261209`](./aap-operator.v2.6.0-0.1762261209.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.6.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:831a1ecb85d1bd6cb7ae144712152d2c0b59b3efc4c3d53eddf0e7db4fe199eb` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| automation-controller-container | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9` | 4.7.5 | 1762180032 | 2025-11-13 | `sha256:941312dae93c` |
| automation-controller-operator-container | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator` | 2.6 | 202510210939.p2.gb276665.assembly.stream.el9 | 2025-11-08 | `sha256:c45e15460aab` |
| automation-eda-controller-container | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9` | 1.2.2 | 1762956380 | 2025-11-14 | `sha256:50019150d22c` |
| automation-eda-controller-operator-container | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator` | 2.6 | 202510210939.p2.gb276665.assembly.stream.el9 | 2025-11-08 | `sha256:a75bb42b960b` |
| automation-eda-ui-container | `registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9` | 1.2.2 | 1763026876 | 2025-11-14 | `sha256:c2f94f3ca2a4` |
| ee-minimal-rhel9-container | `registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9` | 1.0.0 | 1762956380 | 2025-11-14 | `sha256:9bcf51837f75` |
| ee-supported-rhel9-container | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 1.0.0 | 1762956380 | 2025-11-14 | `sha256:258451a5358e` |
| automation-gateway-proxy-container | `registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9` | 2.6.6 | 1762956380 | 2025-11-13 | `sha256:3497a2a08c57` |
| automation-gateway-container | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9` | 2.6.20251119 | 1762956380 | 2025-11-14 | `sha256:6fc53565a5c9` |
| automation-gateway-operator-container | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator` | 2.6 | 202510210939.p2.gb276665.assembly.stream.el9 | 2025-11-08 | `sha256:237ecc036a71` |
| automation-hub-container | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9` | 4.11.3 | 1762956380 | 2025-11-14 | `sha256:705edf7a20a3` |
| automation-hub-operator-container | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator` | 2.6 | 202510210939.p2.gb276665.assembly.stream.el9 | 2025-11-08 | `sha256:607fea0b38f6` |
| automation-hub-web-container | `registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9` | 4.11.3 | 1763026876 | 2025-11-14 | `sha256:618296a5337d` |
| ansible-lightspeed-chatbot-container | `registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9` | 2.6 | 1760515502 | 2025-11-12 | `sha256:d2700c2f976a` |
| ansible-lightspeed-container | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9` | 2.6.251031 | 1762956380 | 2025-11-14 | `sha256:7fb810b82555` |
| ansible-lightspeed-operator-container | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator` | 2.6 | 202510210939.p2.gb276665.assembly.stream.el9 | 2025-11-14 | `sha256:8750cccb33e7` |
| ansible-mcp-tools-container | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 1758184547 | 2025-11-08 | `sha256:361f5e454a54` |
| platform-resource-operator-container | `registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator` | 2.6 | 202510210939.p2.gb276665.assembly.stream.el9 | 2025-11-13 | `sha256:c40c7ed64ebc` |
| platform-resource-runner-container | `registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9` | 2.6 | 1762956380 | 2025-11-14 | `sha256:7d67a1bcc36f` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.6 | 2.6 | 2025-11-14 | `sha256:831a1ecb85d1` |
| kube-rbac-proxy-container | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9:v4.18` | v4.18.0 | 202509240837.p2.g5a14ea9.assembly.stream.el9 | 2025-09-24 | `sha256:784c4667a867` |
| postgresql-15-container | `registry.redhat.io/rhel9/postgresql-15:1` | 1 | 1758514462 | 2025-09-22 | `sha256:5e225c164625` |
| redis-6-container | `registry.redhat.io/rhel9/redis-6:1` | 1 | 1758530358 | 2025-09-22 | `sha256:0962d18bb529` |
| ubi9-minimal-container | `registry.redhat.io/ubi9-minimal:latest` | 9.6 | 1758184547 | 2025-09-18 | `sha256:7c5495d5fad5` |

## Image pull specs

<details><summary>All 24 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator@sha256:c45e15460aaba2b4b00acec712d3433005e41cd84acdb57e9c5416cfe7d7dd38
registry.redhat.io/ansible-automation-platform-26/controller-rhel9@sha256:941312dae93c4694c2c3c74539ea02b84525e6c46a2858fe53f832ab3e2bf304
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator@sha256:a75bb42b960b944d0cfcb25671b476235d418e27e43d710cc58cf5225026074e
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9@sha256:50019150d22c2ddf9bdc983928ec3c36d7e25db077485a68c06260bacbc2f56f
registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9@sha256:c2f94f3ca2a43f8064a1d3c7d1141dc2772d73cd643bd5bef2e85d516d836525
registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9@sha256:9bcf51837f759f03cea0b4639d336a5595820be14edd088b7cd5688508620026
registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9@sha256:258451a5358e6c3aabde0a0e3fa53695a371e4c5fc910291f029c9c43dda6ce2
registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9@sha256:3497a2a08c57acd00bb651b98cf2e008e69b3082394600f9003174fb3f508d79
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator@sha256:237ecc036a7197391bd863de841dca1ec93b9aec78f834cf3221c6a53d21cf2a
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9@sha256:6fc53565a5c95941baa192f9d52ec20efd9f3976f4c30c6c831872f62a60db56
registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator@sha256:607fea0b38f684c864a6dccadd7146e199f70eb1ef64ebede5660d667c19aa4a
registry.redhat.io/ansible-automation-platform-26/hub-rhel9@sha256:705edf7a20a3d263f7ea006f277699d84cebc7af3403388f3289061eb09e5ea8
registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9@sha256:618296a5337dfcd11f4bc2da3556f653c85273ad0dcee7ccd789e14199a5d540
registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9@sha256:d2700c2f976a0f75045735b04ce5289c6d3254b5d438dc8195549cc8b3f3c852
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator@sha256:8750cccb33e7db3de7fc08fc668a0bf0384e28a2a72e208b0a9d598a678ed2ef
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9@sha256:7fb810b825557d58d5d6bc6806374876c2fc8bd8386ca4cd1c633895486a84dd
registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9@sha256:361f5e454a549dd93b2c8835c144b2ed4b0242880f97e96f85637a66361224ab
registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator@sha256:c40c7ed64ebc5820fb75b7a97c6ea3fd7fb15cc33edd5aa95ceb77ac73b1e26c
registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9@sha256:7d67a1bcc36fde7fc66bf6504af2f5ee075cc839099442d435df251421a2c1f2
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:831a1ecb85d1bd6cb7ae144712152d2c0b59b3efc4c3d53eddf0e7db4fe199eb
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9:v4.18@sha256:784c4667a867abdbec6d31a4bbde52676a0f37f8e448eaae37568a46fcdeace7
registry.redhat.io/rhel9/postgresql-15:1@sha256:5e225c1646251d2509b3a6e45fad23abfb11dd5c45d3224b59178f90deb38a70
registry.redhat.io/rhel9/redis-6:1@sha256:0962d18bb5292c0e524354f319b63287c2298a4a2fd34556c68fa285df381427
registry.redhat.io/ubi9-minimal:latest@sha256:7c5495d5fad59aaee12abc3cbbd2b283818ee1e814b00dbc7f25bf2d14fa4f0c
```

</details>
