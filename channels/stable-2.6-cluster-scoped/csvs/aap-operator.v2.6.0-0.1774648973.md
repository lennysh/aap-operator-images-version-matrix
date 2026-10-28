# `aap-operator.v2.6.0-0.1774648973`

[← Back to `stable-2.6-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.6-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.6.0+0.1774648973` |
| **Build date** | 2026-03-27 |
| **Previous CSV** | [`aap-operator.v2.6.0-0.1772556740`](./aap-operator.v2.6.0-0.1772556740.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.6.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:f27581c3a84be7fc387d230aad9e3922caac3f5c59aff779a60aa149877f48e1` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| automation-controller-container | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9` | 4.7.10 | 1773939694 | 2026-03-24 | `sha256:468cee27c715` |
| automation-controller-operator-container | `registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator` | 2.6 | 202603051646.p2.gb276665.assembly.stream.el9 | 2026-03-26 | `sha256:dc387b356283` |
| automation-eda-controller-container | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9` | 1.2.7 | 1773939694 | 2026-03-23 | `sha256:a2c7526be6fa` |
| automation-eda-controller-operator-container | `registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator` | 2.6 | 202603051646.p2.gb276665.assembly.stream.el9 | 2026-03-26 | `sha256:68d310f9efc4` |
| automation-eda-ui-container | `registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9` | 1.2.7 | 1774456665 | 2026-03-26 | `sha256:0a314871b108` |
| ee-minimal-rhel9-container | `registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9` | 2.0.0 | 1773939694 | 2026-03-24 | `sha256:105ad5c7c5f7` |
| ee-supported-rhel9-container | `registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9` | 2.0.0 | 1773939694 | 2026-03-24 | `sha256:fe0982d48906` |
| automation-gateway-proxy-container | `registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9` | 2.6.6 | 1773939694 | 2026-03-22 | `sha256:cde14afd41ee` |
| automation-gateway-container | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9` | 2.6.20260325 | 1773939694 | 2026-03-23 | `sha256:c981e64c5ce6` |
| automation-gateway-operator-container | `registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator` | 2.6 | 202603051646.p2.gb276665.assembly.stream.el9 | 2026-03-26 | `sha256:f35a3ca39d22` |
| automation-hub-container | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9` | 4.11.7 | 1773939694 | 2026-03-27 | `sha256:5401ed3e89a5` |
| automation-hub-operator-container | `registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator` | 2.6 | 202603051646.p2.gb276665.assembly.stream.el9 | 2026-03-26 | `sha256:d67b274db014` |
| automation-hub-web-container | `registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9` | 4.11.7 | 1774456665 | 2026-03-27 | `sha256:344743c3fb71` |
| ansible-lightspeed-chatbot-container | `registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9` | 2.6 | 1773939694 | 2026-03-25 | `sha256:deb21ec1c104` |
| ansible-lightspeed-container | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9` | 2.6.260325 | 1773939694 | 2026-03-24 | `sha256:8405d372ba1e` |
| ansible-lightspeed-operator-container | `registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator` | 2.6 | 202603051646.p2.gb276665.assembly.stream.el9 | 2026-03-26 | `sha256:1a8a5ff4d5bb` |
| ansible-mcp-tools-container | `registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9` | 2.6.250924 | 1773939694 | 2026-03-23 | `sha256:00855d9cc1c7` |
| platform-resource-operator-container | `registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator` | 2.6 | 202603051646.p2.gb276665.assembly.stream.el9 | 2026-03-26 | `sha256:c05eaadf14bd` |
| platform-resource-runner-container | `registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9` | 2.6 | 1773939694 | 2026-03-26 | `sha256:a8a4ed4af40d` |
| aap-mcp-server-container | `registry.redhat.io/ansible-automation-platform-tech-preview/mcp-server-rhel9` | 2.6.20260325 | 1774226014 | 2026-03-23 | `sha256:399412eea3b2` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.6 | 2.6 | 2026-03-27 | `sha256:f27581c3a84b` |
| kube-rbac-proxy-container | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9:v4.18` | v4.18.0 | 202509240837.p2.g5a14ea9.assembly.stream.el9 | 2025-09-24 | `sha256:784c4667a867` |
| postgresql-15-container | `registry.redhat.io/rhel9/postgresql-15:1` | 1 | 1758514462 | 2025-09-22 | `sha256:5e225c164625` |
| redis-6-container | `registry.redhat.io/rhel9/redis-6:1` | 1 | 1758530358 | 2025-09-22 | `sha256:0962d18bb529` |
| ubi9-minimal-container | `registry.redhat.io/ubi9-minimal:latest` | 9.6 | 1758184547 | 2025-09-18 | `sha256:7c5495d5fad5` |

## Image pull specs

<details><summary>All 25 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-26/controller-rhel9-operator@sha256:dc387b356283133272f15aca7e5bf3f3e15c380cad178d2cc7696200ba5aafaa
registry.redhat.io/ansible-automation-platform-26/controller-rhel9@sha256:468cee27c715a7b4180b114bc57900b943ff35974ab2480ef0c74b5d7606efa5
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9-operator@sha256:68d310f9efc469129eed6fc96f459c2d0810c2195b184c5b547835b603023e9f
registry.redhat.io/ansible-automation-platform-26/eda-controller-rhel9@sha256:a2c7526be6fa52074ce147eae8e59ada6f67c93688272600c850bc407b555030
registry.redhat.io/ansible-automation-platform-26/eda-controller-ui-rhel9@sha256:0a314871b108d91beb1755a89868aa18b6f8a07918940548161cadddc13e893a
registry.redhat.io/ansible-automation-platform-26/ee-minimal-rhel9@sha256:105ad5c7c5f7b5c4c5ac5478fcdf5de4b5b66d91bb15fa0bc926a4b7da329847
registry.redhat.io/ansible-automation-platform-26/ee-supported-rhel9@sha256:fe0982d489065a2a287fe076873cf1faa5410c0879def91bbc756280e924118d
registry.redhat.io/ansible-automation-platform-26/gateway-proxy-rhel9@sha256:cde14afd41ee6d4c2c46c9caef9982b26d2b26fb590ba6e12e2c1c845c8642a2
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9-operator@sha256:f35a3ca39d22d96457aba00b588029720b258e16b210b45688336a18dd3a1599
registry.redhat.io/ansible-automation-platform-26/gateway-rhel9@sha256:c981e64c5ce6346fafdee2268498c22bef66bf56cd00a6b9395a5ba77f742b57
registry.redhat.io/ansible-automation-platform-26/hub-rhel9-operator@sha256:d67b274db01420011765c38e3841be0f210a6b708f44521e88e346fd23083e78
registry.redhat.io/ansible-automation-platform-26/hub-rhel9@sha256:5401ed3e89a564e242476e9287fe05e07b605097a765e33fb9a4fe626a7a6371
registry.redhat.io/ansible-automation-platform-26/hub-web-rhel9@sha256:344743c3fb717b50fb2c897e77141c052afdbbe0dbd6c2e05500b0c92b40195e
registry.redhat.io/ansible-automation-platform-26/lightspeed-chatbot-rhel9@sha256:deb21ec1c1046890461b38f5a8b67c85f195a3bc2b965c7766dc4542948d918a
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9-operator@sha256:1a8a5ff4d5bbb35d65d87a2df3779045c716b8ca2ed93e39b1c878162401f436
registry.redhat.io/ansible-automation-platform-26/lightspeed-rhel9@sha256:8405d372ba1e747c2aff9c377c8a406b93c96dbcf11616d27acbaf2c93b00c14
registry.redhat.io/ansible-automation-platform-26/mcp-tools-rhel9@sha256:00855d9cc1c7ad28cff51bbd64dc0d6c3507b0c05b599921624b3d7181c14048
registry.redhat.io/ansible-automation-platform-26/platform-resource-rhel9-operator@sha256:c05eaadf14bdaeaa1f5450e79351995ece9f2deff79813b765f01210b034772d
registry.redhat.io/ansible-automation-platform-26/platform-resource-runner-rhel9@sha256:a8a4ed4af40d35389e3cab1e8e1bf9ac3220100ca18144d7a666a2cd55220588
registry.redhat.io/ansible-automation-platform-tech-preview/mcp-server-rhel9@sha256:399412eea3b2365687c5bd51fe7943668d1a80abcec636baa2dc801b25f47741
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:f27581c3a84be7fc387d230aad9e3922caac3f5c59aff779a60aa149877f48e1
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9:v4.18@sha256:784c4667a867abdbec6d31a4bbde52676a0f37f8e448eaae37568a46fcdeace7
registry.redhat.io/rhel9/postgresql-15:1@sha256:5e225c1646251d2509b3a6e45fad23abfb11dd5c45d3224b59178f90deb38a70
registry.redhat.io/rhel9/redis-6:1@sha256:0962d18bb5292c0e524354f319b63287c2298a4a2fd34556c68fa285df381427
registry.redhat.io/ubi9-minimal:latest@sha256:7c5495d5fad59aaee12abc3cbbd2b283818ee1e814b00dbc7f25bf2d14fa4f0c
```

</details>
