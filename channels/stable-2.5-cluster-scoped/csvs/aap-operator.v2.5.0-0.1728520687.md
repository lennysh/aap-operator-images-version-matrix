# `aap-operator.v2.5.0-0.1728520687`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1728520687` |
| **Build date** | 2024-10-10 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1727875896`](./aap-operator.v2.5.0-0.1727875896.md) |
| **Skip range** | `>=2.4.1 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:176302a46c54dcaec1b9b18012d66aca55d4c16367cd50686195e53c277e7ed8` |
| **Seen in OCP operator indexes** | 4.12–4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.1 | 5 | 2024-10-09 | `sha256:30853b0a8416` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 118 | 2024-10-09 | `sha256:41c4aad8c3e6` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.1 | 10 | 2024-10-09 | `sha256:1ce7240f228a` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 118 | 2024-10-09 | `sha256:0b0fcc4c1a8e` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.1 | 3 | 2024-10-09 | `sha256:3297b0e1c39e` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 749 | 2024-10-09 | `sha256:3e0396470704` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 816 | 2024-10-09 | `sha256:5c94586b4bda` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 816 | 2024-10-09 | `sha256:5c94586b4bda` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 816 | 2024-10-09 | `sha256:5c94586b4bda` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 24 | 2024-10-09 | `sha256:61e4f0f32cb9` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.0 | 60 | 2024-10-09 | `sha256:03c7a401f5f9` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 132 | 2024-10-09 | `sha256:fa7299a7d2ee` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.0 | 213 | 2024-10-09 | `sha256:3ad48aaddacb` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 118 | 2024-10-09 | `sha256:131082d66ab3` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.0 | 200 | 2024-10-09 | `sha256:d3c6b5c2e2cf` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.241009 | 2 | 2024-10-09 | `sha256:1c1cc82bb94b` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 81 | 2024-10-09 | `sha256:7a03c3d2f5af` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 78 | 2024-10-09 | `sha256:6a85f4d5342d` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 108 | 2024-10-10 | `sha256:e16e6fa29a15` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 819 | 2024-10-10 | `sha256:176302a46c54` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202409240105.p0.ge8e8c84.assembly.stream.el8 | 2024-09-24 | `sha256:e34f91215898` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:41c4aad8c3e65a213ccc4ae20bc8b0d05a5d19c27157e2cd326d409df1a955bc
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:30853b0a84160b0143d579922ea46f4cb2b2c696646b1a73f32e20368cd850d6
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:0b0fcc4c1a8e4a842d062ebb5148ed19b8ffd6c6963f4dcd2502a63d20501afb
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:1ce7240f228a261291c254abcc1e085ef32c0bd16ad219f3b33209541decadaf
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:3297b0e1c39e1aba2270986b0d30f3fe62dae9c7602a9a0bc2942c6be5052f3e
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:3e0396470704f3c50d907f0fe1ee4254d09a61ac0e9f72f1db82c7a1d1a7dd0b
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:5c94586b4bda6b5572092f82861d31e948ecbda7a664c2d92864c56b7201dac3
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:61e4f0f32cb97f6a518552cf86cacb9dacbfcb6d6d252cbea9c9e0d5b4c2661c
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:fa7299a7d2ee874eeadc6d684506459e3f626e755b10b4d80321a1937994613e
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:03c7a401f5f91a3a8786311b0275e44b1955b4f2a6a5c0dc1dfcb688d98558a4
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:131082d66ab354f644d5ff86c1b6df07f76d96dff4050515705d53bd097630b5
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:3ad48aaddacb9f24aa1878aba6ab344285894dc6928f49153dff03c5b1a02e74
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:d3c6b5c2e2cf8fc802709ae0d7f16f286df12a60f2d163c0d7a47b5f45dfb939
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:7a03c3d2f5af3739ffb3df20a24228085a6ecee58890da0943ee83b33ff46bb4
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:1c1cc82bb94b11d09fd5f16a4f5916bc3137b4a2488616f227b0b62c7850a4a5
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:6a85f4d5342de4e1ed3d1dab2734d0bdd8e65db291ec9aeebc4bd09e4493a1d4
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:e16e6fa29a15da03a152c3f91ecaf0ed8b96b8e41ebeafb4fac915703994fb0e
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:176302a46c54dcaec1b9b18012d66aca55d4c16367cd50686195e53c277e7ed8
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:e34f912158985525f6efb3c4b675f20854fc677c867d12fe3cd2e971309428dc
registry.redhat.io/rhel8/postgresql-15@sha256:d8a0f58b4b85524a55414532913533b60b63e1809b1d76a35680ad1fdce64c0e
registry.redhat.io/rhel8/redis-6@sha256:e76f07cdcbba8faa2ad7e5637045f28197037a68edfb82be23dc331f06beeeca
registry.redhat.io/ubi8/ubi-minimal@sha256:7583ca0ea52001562bd81a961da3f75222209e6192e4e413ee226cff97dbd48c
```

</details>
