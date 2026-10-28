# `aap-operator.v2.5.0-0.1755835086`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1755835086` |
| **Build date** | 2025-08-22 |
| **Replaces** | [`aap-operator.v2.5.0-0.1753900156`](./aap-operator.v2.5.0-0.1753900156.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:696ce8c524ada1829ac5bee150f839cbcc3c553af79c693d7f033c570b52d6bf` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.19 | 15 | 2025-08-20 | `sha256:ee283fb42ad6` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 189 | 2025-08-20 | `sha256:09f7115ed6c9` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.13 | 6 | 2025-08-20 | `sha256:1a153c39ccec` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 188 | 2025-08-20 | `sha256:0f5bcc615569` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.13 | 1 | 2025-08-21 | `sha256:9c556498b4c5` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 955 | 2025-08-21 | `sha256:d542b8468da9` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1075 | 2025-08-21 | `sha256:701b78f939d6` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1075 | 2025-08-21 | `sha256:701b78f939d6` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1075 | 2025-08-21 | `sha256:701b78f939d6` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 63 | 2025-08-20 | `sha256:ac41da18638f` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250827 | 1 | 2025-08-20 | `sha256:0a7b86695052` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 252 | 2025-08-20 | `sha256:3d9dfb2fafc6` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.7 | 3 | 2025-08-21 | `sha256:5e1d3244f556` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 188 | 2025-08-20 | `sha256:dba31b778430` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.7 | 3 | 2025-08-21 | `sha256:a68693604da6` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250827 | 3 | 2025-08-21 | `sha256:898eb4c35caa` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250827 | 1 | 2025-08-20 | `sha256:197602d34aa9` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 146 | 2025-08-20 | `sha256:d0467739c8fe` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 144 | 2025-08-20 | `sha256:15cddb07c0c2` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 196 | 2025-08-21 | `sha256:41a8aeaae761` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1582 | 2025-08-22 | `sha256:696ce8c524ad` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202507282305.p0.g9308e7f.assembly.stream.el8 | 2025-07-29 | `sha256:56653df97e44` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1755735215 | 2025-08-21 | `sha256:a5f36e7893a5` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1755735183 | 2025-08-21 | `sha256:966a3dafa2dd` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1755735183 | 2025-08-21 | `sha256:966a3dafa2dd` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1755735183 | 2025-08-21 | `sha256:966a3dafa2dd` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1755735183 | 2025-08-21 | `sha256:966a3dafa2dd` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1755695263 | 2025-08-20 | `sha256:89f2c9794a33` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1755695263 | 2025-08-20 | `sha256:89f2c9794a33` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1755695263 | 2025-08-20 | `sha256:89f2c9794a33` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:09f7115ed6c95791cd5a26dab7ae173721b87fe966fb85d8ed082f8c21e2a59a
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:ee283fb42ad68cda89878b1072906d441a269b6c194d39a378b40fb6920a34cf
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:0f5bcc615569136eb5b03a25b952014d394701645949cbc2cb4acfc52d52c2d9
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:1a153c39ccec9ad17afa72b7f9d9ab796147d0b7fe13489903170fcf95bcd30b
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:9c556498b4c53a39e56bb9cdfd1e0c404d567242e99a533888491b18938e8a9b
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:d542b8468da9099446135b0a3883f9098f15accb04c19785687ecb4d94b27088
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:701b78f939d6ba3479b078e6c31391eed0d120c054a02170922512283fe58e02
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:ac41da18638fcc18d5ff925bf0bd21025f85b21244c949f135155e7652bddf81
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:3d9dfb2fafc69fb0e979f8b6994be037ffcb723ab14c256feefda7f8c86408a1
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:0a7b866950527b614fb71e4f70189f1fa1c06572db2fa732adc799212a338cd4
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:dba31b7784300c909b84d4d4b96e6837731e67f23a016f4c260682744bbe4885
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:5e1d3244f556e8f9e0713fc82f44551084f601d599a3294812092bad0ecd9ff8
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:a68693604da61a7e55986e58f94cbdc5222ef04b5200c4ec9f0361cf5e977854
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:898eb4c35caabf9f75c5b6b35766ede49845881754860b1d5beea501acfe1122
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:d0467739c8fe0f19d7c07dd1795ec8609bb0e65f0d7ec60b2b737edd111f17e1
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:197602d34aa92b16f2e11ae41dacf7053397fa1a6fff9dec9d5a41cee0b7d37a
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:15cddb07c0c2d7f15fe22522216730568ab16a97b0e2baf6b70090d7d18e6ab4
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:41a8aeaae761b14919f3800432aa338900f528f56707ae8e6c2a010ca9712e17
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:696ce8c524ada1829ac5bee150f839cbcc3c553af79c693d7f033c570b52d6bf
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:56653df97e4498ecd67b9645d75e44f65c625594e312dbcf0f09937b57d76010
registry.redhat.io/rhel8/postgresql-15@sha256:a5f36e7893a519c12752c6118233c92d4e83618670bc9ea7bd3a8a34a63bd50b
registry.redhat.io/rhel8/redis-6@sha256:966a3dafa2dd31ac1a39e826e08c1b988fe694189fe79449bbe14a48b2631213
registry.redhat.io/ubi8/ubi-minimal@sha256:89f2c9794a3357a8463e3acc4dad45075b1a9a63ae05d4a493dd1451625f2222
```

</details>
