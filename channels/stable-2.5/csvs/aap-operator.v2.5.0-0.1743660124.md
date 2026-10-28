# `aap-operator.v2.5.0-0.1743660124`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1743660124` |
| **Build date** | 2025-04-03 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1742434024`](./aap-operator.v2.5.0-0.1742434024.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:d85e3f17173c55bcbc0c6378d140dc93896cd30b0042e2a272e8f199cd175311` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.11 | 6 | 2025-04-03 | `sha256:6aebe5618cba` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 174 | 2025-04-03 | `sha256:53c5eaa2ea3c` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.7 | 10 | 2025-04-03 | `sha256:6ba0a02d770b` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 176 | 2025-04-03 | `sha256:3b2047f190f3` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.7 | 2 | 2025-04-03 | `sha256:7b572c80e2d3` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 863 | 2025-04-03 | `sha256:d2a8e5567340` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 962 | 2025-04-03 | `sha256:d8400a472e76` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 962 | 2025-04-03 | `sha256:d8400a472e76` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 962 | 2025-04-03 | `sha256:d8400a472e76` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.9 | 4 | 2025-04-03 | `sha256:6f219d7a3b37` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250409 | 4 | 2025-04-03 | `sha256:cb628684a239` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 221 | 2025-04-03 | `sha256:0a3d24f65816` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.3 | 13 | 2025-04-03 | `sha256:ddcfdf0d6675` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 176 | 2025-04-03 | `sha256:faa4cadf557f` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.3 | 12 | 2025-04-03 | `sha256:b272bfb782c3` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250318 | 6 | 2025-04-03 | `sha256:467ba87d0c06` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 132 | 2025-04-03 | `sha256:15351575d3a7` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 129 | 2025-04-03 | `sha256:bb888edc14ba` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 158 | 2025-04-03 | `sha256:ed64bc083fd8` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1251 | 2025-04-03 | `sha256:d85e3f17173c` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202503170806.p0.g9308e7f.assembly.stream.el8 | 2025-03-17 | `sha256:7ce50398cd29` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91.1741813437 | 2025-03-12 | `sha256:2491ac9b904f` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91.1741813437 | 2025-03-12 | `sha256:2491ac9b904f` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91.1741813437 | 2025-03-12 | `sha256:2491ac9b904f` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91.1741813437 | 2025-03-12 | `sha256:2491ac9b904f` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91.1741813437 | 2025-03-12 | `sha256:2491ac9b904f` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213.1741813435 | 2025-03-12 | `sha256:0f81bae9f081` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213.1741813435 | 2025-03-12 | `sha256:0f81bae9f081` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213.1741813435 | 2025-03-12 | `sha256:0f81bae9f081` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213.1741813435 | 2025-03-12 | `sha256:0f81bae9f081` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741863533 | 2025-03-13 | `sha256:33161cf5ec11` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741863533 | 2025-03-13 | `sha256:33161cf5ec11` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741863533 | 2025-03-13 | `sha256:33161cf5ec11` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:53c5eaa2ea3c2d89e310c877f5af6447874721a10ef0c5deb9a41a80d53544a9
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:6aebe5618cba128a57f99332c6c51270af37288e75e58696fe75ad759c54098f
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:3b2047f190f30a3822b1729ad656343d1ec018b2e930ce8076fdfa7d4025a64e
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:6ba0a02d770b8f6120a33f68cbc0d5faf59b54c6be2c021c9c8e083a22af971c
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:7b572c80e2d310cf9f9b2ad4962413b7369680784be4cf891c4f60a4100e45d1
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:d2a8e5567340d7a2426ec62e2980cd9ee6dfc87957bf5b66651ea1c2a065cdb2
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:d8400a472e769d0f3d591dafaad318522009c583b08e881c23b6d57a27cc10ed
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:6f219d7a3b374c5fe76d6158f260f5cefdc2e2286cb065a8774fcb21a51b90af
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:0a3d24f658163e928a1192f8465ff2aa2f113b1708280b7c8f252c89887ebd8e
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:cb628684a239b561fae4a00125f5c99d90742d74af654280a32b8d2def2a8292
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:faa4cadf557f4e3a795b690ef61cd7e2b13539c5fce130532532409752f40b3e
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:ddcfdf0d66756cc888f0b5c3ed3ca17cd2fb402391800ffff121c7565159e2f3
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:b272bfb782c38f45b5e8199e068d1ba86b089b3750d91f760f157ac562ec3bd8
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:15351575d3a7f18735ee650ae051703703a8ba44f89cc681a6562dce328a351e
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:467ba87d0c06581cd8f38e4dfdb2d797e28c014d297b88c6f56f65e2dbdeafbc
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:bb888edc14ba1ff86b229b6c62338c376a64c1bd66e173d69e5df4201d859b9c
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:ed64bc083fd8e8a9ba4ada495b80398a5f89a37826eab6d052102e87debb37ad
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:d85e3f17173c55bcbc0c6378d140dc93896cd30b0042e2a272e8f199cd175311
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:7ce50398cd29df6e07ccd89790a53a711a7e5b484698c48f6581f5d4e9efb05a
registry.redhat.io/rhel8/postgresql-15@sha256:2491ac9b904f6b57218100b49e2fe7ad5e9a93f09eed1a695f2c34846e0a1943
registry.redhat.io/rhel8/redis-6@sha256:0f81bae9f081a2cd1765f8aac8742ae48e4d6ca0b66bd517deb04b41847e7197
registry.redhat.io/ubi8/ubi-minimal@sha256:33161cf5ec11ea13bfe60cad64f56a3aa4d893852e8ec44b2fd2a6b40cc38539
```

</details>
