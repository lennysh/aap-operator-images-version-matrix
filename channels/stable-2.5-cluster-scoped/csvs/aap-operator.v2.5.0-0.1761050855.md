# `aap-operator.v2.5.0-0.1761050855`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1761050855` |
| **Build date** | 2025-10-21 |
| **Replaces** | [`aap-operator.v2.5.0-0.1758147817`](./aap-operator.v2.5.0-0.1758147817.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:fdee8a8f7ef6916f313c982e8f0ae10b1e4a0263e2ea5e8dc8cbc087ac75405b` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.21 | 13 | 2025-10-15 | `sha256:abaaaaa134cc` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 197 | 2025-10-15 | `sha256:cd2d02c8763d` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.13 | 8 | 2025-10-15 | `sha256:e5009c7c1720` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 192 | 2025-10-15 | `sha256:5f855208c4ad` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.13 | 3 | 2025-10-16 | `sha256:b90205883c38` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 982 | 2025-10-16 | `sha256:7df6b485ae4f` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1109 | 2025-10-16 | `sha256:cb92687c7b79` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1109 | 2025-10-16 | `sha256:cb92687c7b79` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1109 | 2025-10-16 | `sha256:cb92687c7b79` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 85 | 2025-10-15 | `sha256:1dd4e03131b2` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20251022 | 1 | 2025-10-15 | `sha256:26020aaca8e8` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 258 | 2025-10-15 | `sha256:915d5ab7bb3d` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.9 | 1 | 2025-10-15 | `sha256:ccfbe7d5bfa7` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 195 | 2025-10-15 | `sha256:30baa4157b9c` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.9 | 1 | 2025-10-16 | `sha256:792cf0c901cb` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250924 | 3 | 2025-10-16 | `sha256:5f5900ef640a` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250924 | 2 | 2025-10-15 | `sha256:851ec1a654f1` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 152 | 2025-10-21 | `sha256:2fade831fd37` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 150 | 2025-10-15 | `sha256:864ea86ee07e` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 208 | 2025-10-16 | `sha256:78b4d1ef67d1` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1716 | 2025-10-21 | `sha256:fdee8a8f7ef6` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202509151014.p2.g9308e7f.assembly.stream.el8 | 2025-09-16 | `sha256:fa0acefda43e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1760371733 | 2025-10-13 | `sha256:705d7e2f23ae` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1760371733 | 2025-10-13 | `sha256:705d7e2f23ae` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1760371733 | 2025-10-13 | `sha256:705d7e2f23ae` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1760371733 | 2025-10-13 | `sha256:705d7e2f23ae` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1761032271 | 2025-10-21 | `sha256:951ee3cabb74` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1761032271 | 2025-10-21 | `sha256:951ee3cabb74` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1761032271 | 2025-10-21 | `sha256:951ee3cabb74` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:cd2d02c8763ddf24a394ebeadfd746e9f7b18b5871ab7aa093d1013f56eda9cb
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:abaaaaa134cc06b1dc8d1aa0b6f78649cdca12fc6ed70a3a1b0f3826fe48b2c7
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:5f855208c4ad89be2dd37f2eef0775581da9453b6f6eb7a8e19a3ed57a4a756b
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:e5009c7c1720558d2d2b3203f95012e9ced0dcd859f8b3de22d204d1a196f172
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:b90205883c38b025a68e39efa0625807cb01b70cf49709db5b6b291f446a8234
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:7df6b485ae4f53c513ca67dcc44109f8b80e812a8d9069c70fca08bada37b531
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:cb92687c7b7926d06e1683b07fbe5dc10fc22f6c052fb1dface041ef84c1f2cd
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:1dd4e03131b27178635226e77cdd3cac0143e3c6d0d592cad8763655f7d8562c
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:915d5ab7bb3db7216992d35cf528d89f7171e13ef7c1f41dcaf8662425d0b398
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:26020aaca8e8ba52e9efc8f7931859bb97db79bfe989dfce0a424c57f6ced2e1
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:30baa4157b9c04e233dadea1235bbafa5cb819916db240e52595b1188c6265ef
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:ccfbe7d5bfa78602a44499339a81fcb17105dfd40b8ff80d57c674beb2b6a9d4
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:792cf0c901cbd3758a0fea3a5fcd45253f0aaab85a1bc6d480b4c387513814bd
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:5f5900ef640a16a5c223636c111096e1d5513e3daae1a4a926f684af11b3cbe2
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:2fade831fd37b2183156820d6defa82de25fbdbf1f746f6e842a48e5cdbe1d9f
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:851ec1a654f1f350f7534fde319caf8eafaae83c0aa5ff7fe5963bad748f3742
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:864ea86ee07ec63cc163f8a1e26ab98fb6623bf56cf8acc21ffac24ee18dc7d2
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:78b4d1ef67d1e6c211d3ced03c3af61ea2df271b2b722251dc96b96c515bccc9
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:fdee8a8f7ef6916f313c982e8f0ae10b1e4a0263e2ea5e8dc8cbc087ac75405b
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:fa0acefda43e309e7f9f31f5247c933d0b868ff1573ece2f38e0549d7e2ec942
registry.redhat.io/rhel8/postgresql-15@sha256:64bca18004dc5b79eb21cce15996c8cb0a606405bc7797f7ddc69c87a6cc149b
registry.redhat.io/rhel8/redis-6@sha256:705d7e2f23ae3dcd8d96d083bf7d98b46250c2bc44c13a68fad752568bff9ad2
registry.redhat.io/ubi8/ubi-minimal@sha256:951ee3cabb74246821ae31c2b808b7789310f5509882c153b7b178aaaeefa2d3
```

</details>
