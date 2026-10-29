# `aap-operator.v2.5.0-0.1727875896`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1727875896` |
| **Build date** | 2024-10-02 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1727241223`](./aap-operator.v2.5.0-0.1727241223.md) |
| **Skip range** | `>=2.4.1 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c7fedd33f9cd59a4ce0e6404ec2c2b586988145574f3301358ddbbb287c91051` |
| **Seen in OCP operator indexes** | 4.12–4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.1 | 3 | 2024-10-02 | `sha256:bed0110ba42a` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 116 | 2024-10-02 | `sha256:6bf8bb1668e6` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.1 | 2 | 2024-10-02 | `sha256:9d26f944eaf0` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 115 | 2024-10-02 | `sha256:b7508500f978` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.1 | 2 | 2024-10-02 | `sha256:4c6e45931cec` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 747 | 2024-10-01 | `sha256:61ca9b663930` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 812 | 2024-10-02 | `sha256:3dd2ef7b2c1d` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 812 | 2024-10-02 | `sha256:3dd2ef7b2c1d` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 812 | 2024-10-02 | `sha256:3dd2ef7b2c1d` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 22 | 2024-10-02 | `sha256:94fdb3cb40a1` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.0 | 58 | 2024-10-02 | `sha256:626c4fd54687` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 129 | 2024-10-02 | `sha256:b13fc09b9118` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.0 | 207 | 2024-10-02 | `sha256:a79293a16923` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 116 | 2024-10-02 | `sha256:1fd26ee7ad6b` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.0 | 196 | 2024-10-02 | `sha256:d2a5c02e4954` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.240919 | 6 | 2024-10-02 | `sha256:d28d36096a51` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 79 | 2024-10-02 | `sha256:3e9f4fdaf775` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 75 | 2024-10-02 | `sha256:6c7a7f759cd3` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 105 | 2024-10-02 | `sha256:d3fe1755dabe` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 799 | 2024-10-02 | `sha256:c7fedd33f9cd` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202409240105.p0.ge8e8c84.assembly.stream.el8 | 2024-09-24 | `sha256:e34f91215898` |
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
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:6bf8bb1668e6b25b8dc4ea36849707f88edaf550d26895dda3688378bd44afa3
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:bed0110ba42a5879f69aafb2aba18b6342721a59b52907a59e034786d84967d4
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:b7508500f9786e283716743f3cc68c40742c099cd887d67043a2857c8ffdefe5
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:9d26f944eaf0b56a5c967430698ec5fef366e809ce0f8a48884f7759d17c8e08
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:4c6e45931cec4c93784f7ed715fdf5c3a45ecca638b27c15f5d3c552b2128369
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:61ca9b6639306921718aba8afc5db077f94eec6df962b81678f466d2a465d55c
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:3dd2ef7b2c1d764437752bda030161322196fe53608b94edc433ad0dfd7851f0
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:94fdb3cb40a1e66b5299c3b575be1df0edb279a3df38e871c18d779627843ae2
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:b13fc09b91187533bb449fca89ddf79f6eb9e6fcf20f7be695522e5f3e6626be
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:626c4fd5468745c900edf5eb6a03f81876c56b7c0b0d7f582022fc14167fde91
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:1fd26ee7ad6be7367a9ced0a578d4c6ced83725da0c8021070df7ef3a8874e9e
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:a79293a16923ad943ab488f7f94fd70cc0604d6c72a77fd967cc4922d893a900
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:d2a5c02e4954fd97f1ebc34aa791c6c653ea7e3ad0d425d92785f47ff09fc209
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:3e9f4fdaf775635f2eb1ee078972bacd58132fff4be0342e38d1b32eb6c8b43d
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:d28d36096a51256f00eb1ed98ecd2c11c28eda928fe1e4c43220a66aeaef6064
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:6c7a7f759cd35c0a135ec0a7eb724a6dec0da94e07a61b3dba547cadcfb6e2a6
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:d3fe1755dabee51d52cbcfa98be8af87a8f24d189c6cd221c14aaedd2ae9a358
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c7fedd33f9cd59a4ce0e6404ec2c2b586988145574f3301358ddbbb287c91051
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:e34f912158985525f6efb3c4b675f20854fc677c867d12fe3cd2e971309428dc
registry.redhat.io/rhel8/postgresql-15@sha256:41340556682aa87a51b26803b0449250a65c846df96867131c5dde7c615e6b75
registry.redhat.io/rhel8/redis-6@sha256:218f7fa2458c274cc34f79190423e0aba03027f55ef6b3334d916951a668b7b7
registry.redhat.io/ubi8/ubi-minimal@sha256:7583ca0ea52001562bd81a961da3f75222209e6192e4e413ee226cff97dbd48c
```

</details>
