# `aap-operator.v2.4.0-0.1755833968`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1755833968` |
| **Build date** | 2025-08-22 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1753232791`](./aap-operator.v2.4.0-0.1753232791.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c4f07daae4de4e923d80e9d87e91a8258fda3310e73146eea924d3185a045d95` |
| **Seen in OCP operator indexes** | 4.12–4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.25 | 1 | 2025-08-20 | `sha256:4100ba629b73` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 179 | 2025-08-20 | `sha256:114557a5adce` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 42 | 2025-08-20 | `sha256:15708f8cf5f9` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 179 | 2025-08-20 | `sha256:307930cac031` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 40 | 2025-08-20 | `sha256:75392fcb6a2b` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 954 | 2025-08-20 | `sha256:c3f055933fcd` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1072 | 2025-08-21 | `sha256:b5bc9882d5b7` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1072 | 2025-08-21 | `sha256:b5bc9882d5b7` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1072 | 2025-08-21 | `sha256:b5bc9882d5b7` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | N/A | N/A | N/A | `sha256:dabbf281aad5` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 179 | 2025-08-20 | `sha256:6364113ed0ef` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 1 | 2025-08-20 | `sha256:23237bd0368f` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 15 | 2025-08-20 | `sha256:14f8e85a25b2` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 48 | 2025-08-20 | `sha256:56751601afeb` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 175 | 2025-08-20 | `sha256:33f8a2dce99f` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 216 | 2025-08-21 | `sha256:2b9e5e5748b7` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2745 | 2025-08-22 | `sha256:c4f07daae4de` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202507282305.p0.g9308e7f.assembly.stream.el8 | 2025-07-29 | `sha256:56653df97e44` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1755735183 | 2025-08-21 | `sha256:966a3dafa2dd` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1755735183 | 2025-08-21 | `sha256:966a3dafa2dd` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1755735183 | 2025-08-21 | `sha256:966a3dafa2dd` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1755695263 | 2025-08-20 | `sha256:89f2c9794a33` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1755695263 | 2025-08-20 | `sha256:89f2c9794a33` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1755695263 | 2025-08-20 | `sha256:89f2c9794a33` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:114557a5adce850e239d237dac4c752e05abb21af849c5950ada5801b5ca88a2
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:4100ba629b731b56d0e71dda0ce2989ed04a572aa7198150713996a3dcdbe502
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:307930cac031ca4f3b5059b457fc5b7ae0d5d88601a554f31df5a937497fb351
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:15708f8cf5f9b705b17fab0b84a2e23cf66c5a78a22325373ad75c4a278a5cc6
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:75392fcb6a2be33c99e729fb5cc541fb34e02a33df3a8a9a31fcd8e9b85a0b38
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:c3f055933fcde87dc7918a017f342b1af4cc86f168ab91495f274101c8e06a25
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:b5bc9882d5b7f01ca2cbcdae990d1e9864846eb5cdf79ed95acf9fab28e66c4c
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:6364113ed0ef14463db317e45dba88702c6efd102ba9951fa5762639cc0b3744
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:dabbf281aad509dd41613aba2c4443dc7e06c6d08e0397212790f052f1b82336
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:23237bd0368fd6eaa92fbed0b4623dd1e9a521abbfcc7e03b479846d00ee849e
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:56751601afeb36142c8b0fac44c91a23ee20d6863acecc1b9b287a2294f5eee3
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:14f8e85a25b27994324f7c4e0d09c3343b0ff2ca4129370e68959adea8c6cdfc
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:33f8a2dce99f2eaa7c46dfbdbf1b8d6194a43afa34a9b81a5687de1055842170
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:2b9e5e5748b75fa199022fad851b632c23203eaacfc18194d587b649ee6406b2
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c4f07daae4de4e923d80e9d87e91a8258fda3310e73146eea924d3185a045d95
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:56653df97e4498ecd67b9645d75e44f65c625594e312dbcf0f09937b57d76010
registry.redhat.io/rhel8/postgresql-15@sha256:a5f36e7893a519c12752c6118233c92d4e83618670bc9ea7bd3a8a34a63bd50b
registry.redhat.io/rhel8/redis-6@sha256:966a3dafa2dd31ac1a39e826e08c1b988fe694189fe79449bbe14a48b2631213
registry.redhat.io/ubi8/ubi-minimal@sha256:89f2c9794a3357a8463e3acc4dad45075b1a9a63ae05d4a493dd1451625f2222
```

</details>
