# `aap-operator.v2.4.0-0.1743629049`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1743629049` |
| **Build date** | 2025-04-02 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1742444794`](./aap-operator.v2.4.0-0.1742444794.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c4fe1decab5e1355cc61882777697174af0ad37f12c23c90f10491e59a772e9a` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.21 | 2 | 2025-04-02 | `sha256:532193c3519a` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 171 | 2025-04-02 | `sha256:63036433399c` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 35 | 2025-04-02 | `sha256:075e6bc38577` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 171 | 2025-04-02 | `sha256:50db1109f84e` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 34 | 2025-04-02 | `sha256:8f8ac13ddcc1` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 861 | 2025-04-02 | `sha256:91a18c7ed4d0` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 960 | 2025-04-02 | `sha256:13c29f388445` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 960 | 2025-04-02 | `sha256:13c29f388445` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 960 | 2025-04-02 | `sha256:13c29f388445` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.3 | 3 | 2025-04-02 | `sha256:6f0b844208d8` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 170 | 2025-04-02 | `sha256:11b397b67e99` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.3 | 2 | 2025-04-02 | `sha256:268ff11c1dd4` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 6 | 2025-04-02 | `sha256:bea7dcbdda6f` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 37 | 2025-04-02 | `sha256:21e433b9b25b` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 166 | 2025-04-02 | `sha256:776288cad590` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 206 | 2025-04-02 | `sha256:c823d5516a31` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2442 | 2025-04-02 | `sha256:c4fe1decab5e` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202503170806.p0.g9308e7f.assembly.stream.el8 | 2025-03-17 | `sha256:7ce50398cd29` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214.1741813439 | 2025-03-12 | `sha256:9e7b35740d53` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214.1741813439 | 2025-03-12 | `sha256:9e7b35740d53` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214.1741813439 | 2025-03-12 | `sha256:9e7b35740d53` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214.1741813439 | 2025-03-12 | `sha256:9e7b35740d53` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213.1741813435 | 2025-03-12 | `sha256:0f81bae9f081` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213.1741813435 | 2025-03-12 | `sha256:0f81bae9f081` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213.1741813435 | 2025-03-12 | `sha256:0f81bae9f081` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741863533 | 2025-03-13 | `sha256:33161cf5ec11` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741863533 | 2025-03-13 | `sha256:33161cf5ec11` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741863533 | 2025-03-13 | `sha256:33161cf5ec11` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:63036433399c824fd34192b230f829b0e6aeaa3d3ad26506b0ae661bf1d02d5b
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:532193c3519a0a84c95445b935a7efd44b8ce6950509c72a9a4b5374f5c47e2e
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:50db1109f84e150d2f2996fa8e01dfeeac6dff915e893915d788f543f1f13eec
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:075e6bc38577d431fb1c02a3db35bc8b94a53d92b7ce1810cc6cab4dbfaaa7b8
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:8f8ac13ddcc1bd07b0adbc854171b9e6b2ac93860097dbe992d0c7cc56284675
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:91a18c7ed4d0783016f2d6eb5cbd07009d2474d092abcb143daa587670983f6c
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:13c29f3884454235b2d60eebdd44f0b0f25b9060048f4553eb0b153f6b3fbbdc
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:11b397b67e99e9ae1846716795d87f6843cbcbf37601992cb73b0956ba64d3f1
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:6f0b844208d82df7b2378792ae7ca0edb347cc9684a91c307b8f417e75ad3986
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:268ff11c1dd4d9faece34a536b6679c937a1c11b5b3e3217a6ee3166c6574594
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:21e433b9b25bea513708c020b40a9aa72d626a2b5025103f94dac4505085bb06
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:bea7dcbdda6f02752e26189a09a7a266e85605beb0ed7360b5bc3bb2118824b0
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:776288cad5900fb5bf84e930746cd5137a3ca5e2ed13f5c4e32911d84d94b411
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:c823d5516a31aef7d0f6a2a3ea261101911c5e74de25da9d895880298b5ba1ba
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c4fe1decab5e1355cc61882777697174af0ad37f12c23c90f10491e59a772e9a
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:7ce50398cd29df6e07ccd89790a53a711a7e5b484698c48f6581f5d4e9efb05a
registry.redhat.io/rhel8/postgresql-13@sha256:9e7b35740d53a1a781351fd49007d505921324c073b0a0375022e42d04b4cfb2
registry.redhat.io/rhel8/redis-6@sha256:0f81bae9f081a2cd1765f8aac8742ae48e4d6ca0b66bd517deb04b41847e7197
registry.redhat.io/ubi8/ubi-minimal@sha256:33161cf5ec11ea13bfe60cad64f56a3aa4d893852e8ec44b2fd2a6b40cc38539
```

</details>
