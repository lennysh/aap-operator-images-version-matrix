# `aap-operator.v2.5.0-0.1731456196`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1731456196` |
| **Build date** | 2024-11-13 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1729741547`](./aap-operator.v2.5.0-0.1729741547.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:1317ee317d58633b2247c704291f8a05b8d91acbbdec4f16ac8bae812c79382b` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.2 | 15 | 2024-11-12 | `sha256:7559f73f2378` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 132 | 2024-11-12 | `sha256:88d80cbef662` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.2 | 4 | 2024-11-12 | `sha256:3db1d1f32ff2` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 132 | 2024-11-12 | `sha256:17707a07d687` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.2 | 2 | 2024-11-12 | `sha256:a8f29758f0fd` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 767 | 2024-11-12 | `sha256:788fff710529` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 835 | 2024-11-12 | `sha256:b7f645f202bf` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 835 | 2024-11-12 | `sha256:b7f645f202bf` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 835 | 2024-11-12 | `sha256:b7f645f202bf` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 26 | 2024-11-12 | `sha256:61ab290045f2` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.3 | 2 | 2024-11-12 | `sha256:6df890d13d8d` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 159 | 2024-11-12 | `sha256:d2882b70eae7` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 4 | 2024-11-12 | `sha256:874d216ea2ae` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 134 | 2024-11-12 | `sha256:c9d9eb24fdb1` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 4 | 2024-11-12 | `sha256:c36b81e8012d` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.241009 | 5 | 2024-11-12 | `sha256:a4b117988e60` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 93 | 2024-11-12 | `sha256:f0d80ef78450` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 88 | 2024-11-12 | `sha256:1632a4d38f91` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 121 | 2024-11-12 | `sha256:3a8e460fdd00` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 925 | 2024-11-13 | `sha256:1317ee317d58` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202410230304.p0.g9308e7f.assembly.stream.el8 | 2024-10-23 | `sha256:76a47d100de1` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87 | 2024-10-31 | `sha256:4066e378a1a8` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87 | 2024-10-31 | `sha256:4066e378a1a8` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87 | 2024-10-31 | `sha256:4066e378a1a8` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87 | 2024-10-31 | `sha256:4066e378a1a8` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87 | 2024-10-31 | `sha256:4066e378a1a8` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209 | 2024-10-31 | `sha256:5250d644e80a` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209 | 2024-10-31 | `sha256:5250d644e80a` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209 | 2024-10-31 | `sha256:5250d644e80a` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209 | 2024-10-31 | `sha256:5250d644e80a` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:88d80cbef662bbb51bffe81d8fab560843e27588ab0889e357d334ce55d6656f
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:7559f73f237898c4fae6cafc60b9fa32a7c9af1664dfc67e64d79f8445f6fefd
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:17707a07d68779624c037604a0da2709414d4235ad0740c919eee4b27be94fa9
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:3db1d1f32ff2b50489e46f6470220e15f2de292359cd0563a08d3cb513218870
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:a8f29758f0fdd88de235b6649dbbd2941d4a72fe5b3331acafbc83f96d81891e
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:788fff710529f5f9eea0ec6ecbd58fb2a11645cd601fdc184074a8db8e13d4df
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:b7f645f202bfaed9564746f05185760f02636f766aaa72b12c884b85eed84548
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:61ab290045f21dad55d7b9dd28ebc46d457ce45132fdf7bd965718d3480a6f66
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:d2882b70eae70a6e3f5d8f47e40b7c8376a68a123d3db3d791d5fc6de665e51b
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:6df890d13d8dd4ef2a0c9d150dea54a26b91b0a6f4cfd71692b066c06341823d
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:c9d9eb24fdb14ce801932ed6b7b4aa04791a6c438e4999bc97a8ff798add40b5
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:874d216ea2aee10f67c733d0aac44fdb0e71b7cd5044d8fc74fce8de64890d51
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:c36b81e8012db576090b064ad704ff216ab021fa0cd808cacc6e7b5ffa231344
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:f0d80ef78450da2c49ae72051427b03691c1c94d5a0442dca1e09fcdfb2edb7b
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:a4b117988e60eaacfc973e9f0bbbe61e4bc1414da63a4b23cd3e21b6061f54ba
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:1632a4d38f91825a04e957dd9e019c8e47a670ea5025e3a165893909fe89dcf3
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:3a8e460fdd008295bb5ef174b8ae3d532d9e0f41a62e53cbc48148883933ffad
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:1317ee317d58633b2247c704291f8a05b8d91acbbdec4f16ac8bae812c79382b
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:76a47d100de1f2afa23803bec503d9440605db03c7179b231f963e5663a3d12a
registry.redhat.io/rhel8/postgresql-15@sha256:4066e378a1a8bc14ed19dbdc016a669d3476021a640ec225c022d9044d7e9241
registry.redhat.io/rhel8/redis-6@sha256:5250d644e80aea794b0f732e9285883a4348dace83557f177f64d78fe4dcabd0
registry.redhat.io/ubi8/ubi-minimal@sha256:c12e67af6a7e15113d76bc72f10bef2045c026c71ec8b7124c8a075458188a83
```

</details>
