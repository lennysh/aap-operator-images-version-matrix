# `aap-operator.v2.5.0-0.1727240614`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1727240614` |
| **Build date** | 2024-09-25 |
| **Replaces** | — |
| **Skip range** | — |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:5726e35665d1f6710e4d25c34e357d29221b09dd9f1901580eadb1eba075d7c5` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.0 | 227 | 2024-09-25 | `sha256:e1891113357c` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 114 | 2024-09-25 | `sha256:f401361f43cb` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.0 | 231 | 2024-09-25 | `sha256:fab8d45c328a` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 113 | 2024-09-25 | `sha256:beee5f03410f` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.0 | 278 | 2024-09-25 | `sha256:60ada611f25f` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 745 | 2024-09-25 | `sha256:a3800be7b548` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 806 | 2024-09-25 | `sha256:1cf3a9821cb6` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 806 | 2024-09-25 | `sha256:1cf3a9821cb6` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 806 | 2024-09-25 | `sha256:1cf3a9821cb6` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 20 | 2024-09-25 | `sha256:201b9a2d61d1` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.0 | 51 | 2024-09-25 | `sha256:f959e09efae9` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 126 | 2024-09-25 | `sha256:2191f8271143` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.0 | 200 | 2024-09-25 | `sha256:683b3eaa2566` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 114 | 2024-09-25 | `sha256:f54de13ca767` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.0 | 189 | 2024-09-25 | `sha256:2ac6d17ba4f0` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.240919 | 4 | 2024-09-25 | `sha256:15195d70fa68` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 77 | 2024-09-25 | `sha256:b6224431a713` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 73 | 2024-09-25 | `sha256:69db28da87ad` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 103 | 2024-09-25 | `sha256:6c2dd4787a37` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 765 | 2024-09-25 | `sha256:5726e35665d1` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202408260908.p0.ge8e8c84.assembly.stream.el8 | 2024-08-27 | `sha256:f6c37678f1eb` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 81 | 2024-09-17 | `sha256:41340556682a` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 81 | 2024-09-17 | `sha256:41340556682a` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 81 | 2024-09-17 | `sha256:41340556682a` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 81 | 2024-09-17 | `sha256:41340556682a` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 81 | 2024-09-17 | `sha256:41340556682a` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 203 | 2024-09-17 | `sha256:218f7fa2458c` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 203 | 2024-09-17 | `sha256:218f7fa2458c` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 203 | 2024-09-17 | `sha256:218f7fa2458c` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 203 | 2024-09-17 | `sha256:218f7fa2458c` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:f401361f43cbc9c7b551449cb303c789629b17c3cc480381d285944f92f763de
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:e1891113357c8abc897763c06ca949a009fbb14bb4aad117c2333b9c9bc2fb2e
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:beee5f03410fa3b7173a7bde103ee333e4dc96cafd94ca607af94da543c13662
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:fab8d45c328a119f28a494a16fc0fba78024df0da6c9fd1c5e9aaa76aff5d44f
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:60ada611f25ff33e3a29b0458c2cf14fb53df96a3335373d0910bb1aff76492c
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:a3800be7b548aa4c05aebfac071fd6f77d4e2740f808d2a727fac5bbc44653e6
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:1cf3a9821cb6c4937ab3b0c465b04f83348c4cab390f3993da111c9747ffcd6a
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:201b9a2d61d11b9c78013ffd7f4c941ee48d0785f5ee06cd8baa905ae261c6bb
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:2191f8271143984079ad02fdd643c6725e5820dab499db4bb5e6cf48e71705f7
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:f959e09efae969b8bedc88c6df1f10e95a6e976138130acfd36bff9cebb5689e
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:f54de13ca767bd788ce3f0c5faed8412385f45d36c6e4240b857b0271dbb051e
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:683b3eaa25661cbea6d9b4713545f7892baa76c0a0341ecb7905776760563036
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:2ac6d17ba4f0e5589abe3386b4f29b4538f25e82a09d23e5bf3faafe2c0dca7b
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:b6224431a7130ea0e5aca92bd9ebc6d2c9a57c06d9c016c0b162d26df31eff49
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:15195d70fa6829e356e04da06b4b7255baa33f163b9086517860e7e4227cdbef
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:69db28da87adf23b4ceb7c15f67214880ba72d5831ed3b3aff8b9e53812dfe8b
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:6c2dd4787a3789373579f8852e009401aea8b99666904bc97f7b6ec3514a7ea7
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:5726e35665d1f6710e4d25c34e357d29221b09dd9f1901580eadb1eba075d7c5
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:f6c37678f1eb3279e603f63d2a821b72394c52d25c2ed5058dc29d4caa15d504
registry.redhat.io/rhel8/postgresql-15@sha256:41340556682aa87a51b26803b0449250a65c846df96867131c5dde7c615e6b75
registry.redhat.io/rhel8/redis-6@sha256:218f7fa2458c274cc34f79190423e0aba03027f55ef6b3334d916951a668b7b7
registry.redhat.io/ubi8/ubi-minimal@sha256:7583ca0ea52001562bd81a961da3f75222209e6192e4e413ee226cff97dbd48c
```

</details>
