# `aap-operator.v2.5.0-0.1753900156`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1753900156` |
| **Build date** | 2025-07-30 |
| **Replaces** | [`aap-operator.v2.5.0-0.1750901111`](./aap-operator.v2.5.0-0.1750901111.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:bf4896234757a8c7ccbf76acb04ad9b8175fdfb4e155c37c15c79d65aeec4f44` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.18 | 1 | 2025-07-24 | `sha256:ab58b8cb5b57` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 186 | 2025-07-24 | `sha256:69196d84ad23` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.11 | 3 | 2025-07-24 | `sha256:65b04d088625` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 185 | 2025-07-24 | `sha256:5bb7d06aef0a` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.11 | 3 | 2025-07-24 | `sha256:54ac342dcfda` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 944 | 2025-07-24 | `sha256:1070bbb38c7d` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1062 | 2025-07-24 | `sha256:9861e113289c` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1062 | 2025-07-24 | `sha256:9861e113289c` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1062 | 2025-07-24 | `sha256:9861e113289c` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 55 | 2025-07-30 | `sha256:bca3007240e0` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250730 | 2 | 2025-07-30 | `sha256:08a07f1cd756` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 246 | 2025-07-24 | `sha256:0fc639e792e0` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.6 | 3 | 2025-07-24 | `sha256:eb3cf3f27d24` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 185 | 2025-07-24 | `sha256:02f8cc6e4bad` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.6 | 3 | 2025-07-24 | `sha256:1c7e21a4a918` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250730 | 2 | 2025-07-24 | `sha256:968345297ed8` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250730 | 3 | 2025-07-24 | `sha256:06554327bd70` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 145 | 2025-07-24 | `sha256:ddab00358745` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 142 | 2025-07-24 | `sha256:1638f38e369e` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 193 | 2025-07-24 | `sha256:2fd30607e38a` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1531 | 2025-07-30 | `sha256:bf4896234757` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202507150036.p0.g9308e7f.assembly.stream.el8 | 2025-07-15 | `sha256:9b7aabfbead9` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1753769402 | 2025-07-29 | `sha256:1435c8fa9ac2` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1753769402 | 2025-07-29 | `sha256:1435c8fa9ac2` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1753769402 | 2025-07-29 | `sha256:1435c8fa9ac2` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1753769402 | 2025-07-29 | `sha256:1435c8fa9ac2` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1753769402 | 2025-07-29 | `sha256:1435c8fa9ac2` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1753770728 | 2025-07-29 | `sha256:e1b804064692` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1753770728 | 2025-07-29 | `sha256:e1b804064692` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1753770728 | 2025-07-29 | `sha256:e1b804064692` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1753770728 | 2025-07-29 | `sha256:e1b804064692` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1753764099 | 2025-07-29 | `sha256:7957d61cf18d` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1753764099 | 2025-07-29 | `sha256:7957d61cf18d` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1753764099 | 2025-07-29 | `sha256:7957d61cf18d` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:69196d84ad2307e0127e48402f9cca880dcd8397a6b3bd094c7c9d31abe18adb
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:ab58b8cb5b57ef89a22a681376dff0686052ac858e6c56bf5e5ef2f64afb638c
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:5bb7d06aef0a6ec41058821a60f757fc316cb89313370b1d7a8c441cf046015a
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:65b04d08862510b2faf0e2a53197369b16d0d323e99d4bec84c2274b87be6691
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:54ac342dcfda5312c48c9db16fb5012bf8c0717e90f7e247490316b5f23563d2
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:1070bbb38c7d0f6fd7f00aeca7ea2aa58c22c9949f4df0a1710b2a2f4e74dfb7
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:9861e113289cb88696fdefad64b00e9f73af1ea2d241ec161027def3a9ee5be8
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:bca3007240e02314d26db8b21cabb63bb91f188e8a5538dc683fd4112de8a858
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:0fc639e792e08e157bef4cd585bd6fded1951f7ca05bf19f87dcec46bf58c107
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:08a07f1cd7560eb37c1fd9ae47aa4b131ba828db451a56f1a66bb25084a4b7ca
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:02f8cc6e4badd45de534762305c83a1b549a81fa51934ae077edec23e4f7c0f7
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:eb3cf3f27d2430a73bd60067e5612b1762d439ba5ea390a6819744aa3d551c33
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:1c7e21a4a9183fc4a6879bc4ed4d8c8bb6a56e2806d07022e393ad5a7cb32de5
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:968345297ed80c9b28d830197fb1517f89f6f77bffa96d16f248625c8fd73333
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:ddab00358745eab63045f89b508bbfaec32a7442412816a6f5857a95ec58a2d0
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:06554327bd70130c55eccb850ed4c0f7deb570ec0c8474a9bf672f92139033f7
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:1638f38e369effc7ef5caeea1396af8df6c9f228114d026e5f88583bda9003a4
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:2fd30607e38ad63465d30c29e5023c5e88fe8c5cd157c8eb7c58570d131bc663
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:bf4896234757a8c7ccbf76acb04ad9b8175fdfb4e155c37c15c79d65aeec4f44
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:9b7aabfbead92df3a4afeb1854e45a92f23da52321d1705fce444510fa856145
registry.redhat.io/rhel8/postgresql-15@sha256:1435c8fa9ac2297ac2912c3377bc1408f2a342c35bb249474ada675f462ae986
registry.redhat.io/rhel8/redis-6@sha256:e1b804064692cf4958ba09364f4fb986f0a462ca7ef84c32c02e088db30d58a6
registry.redhat.io/ubi8/ubi-minimal@sha256:7957d61cf18d023b426249b456fee704106acf7a93e83de2690ae7c29b7f4323
```

</details>
