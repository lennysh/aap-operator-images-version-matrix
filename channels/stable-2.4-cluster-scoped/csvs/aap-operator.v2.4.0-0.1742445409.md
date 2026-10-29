# `aap-operator.v2.4.0-0.1742445409`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1742445409` |
| **Build date** | 2025-03-20 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1741194557`](./aap-operator.v2.4.0-0.1741194557.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:a23ded2cf308dba865fad4fc48e8568fdd9c2215b401b0dc9899f050ceda8180` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.20 | 2 | 2025-03-20 | `sha256:f7718c1e5ff0` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 170 | 2025-03-20 | `sha256:adbd7a13b4bf` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 34 | 2025-03-20 | `sha256:1441881680eb` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 170 | 2025-03-20 | `sha256:ee23659ebbc4` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 33 | 2025-03-20 | `sha256:f2ef935e39c9` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 853 | 2025-03-20 | `sha256:4d47fb8b7ca8` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 947 | 2025-03-20 | `sha256:e220f813b0c8` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 947 | 2025-03-20 | `sha256:e220f813b0c8` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 947 | 2025-03-20 | `sha256:e220f813b0c8` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.3 | 2 | 2025-03-20 | `sha256:f42e3f859338` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 169 | 2025-03-20 | `sha256:18bcafefd501` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.3 | 1 | 2025-03-20 | `sha256:b521220c5cbe` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 5 | 2025-03-20 | `sha256:5c95a3951655` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 36 | 2025-03-20 | `sha256:dfa7809ad3f0` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 164 | 2025-03-20 | `sha256:4656fd4a846f` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 204 | 2025-03-20 | `sha256:0f9ea8bf5c43` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2413 | 2025-03-20 | `sha256:a23ded2cf308` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202502191335.p0.g9308e7f.assembly.stream.el8 | 2025-02-19 | `sha256:f831737dc97e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214 | 2025-03-05 | `sha256:bb0646dcee32` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214 | 2025-03-05 | `sha256:bb0646dcee32` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214 | 2025-03-05 | `sha256:bb0646dcee32` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 214 | 2025-03-05 | `sha256:bb0646dcee32` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213 | 2025-03-05 | `sha256:109574014c15` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213 | 2025-03-05 | `sha256:109574014c15` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213 | 2025-03-05 | `sha256:109574014c15` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741795396 | 2025-03-12 | `sha256:e4ca1025efad` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741795396 | 2025-03-12 | `sha256:e4ca1025efad` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741795396 | 2025-03-12 | `sha256:e4ca1025efad` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:adbd7a13b4bf1349395aef28dd0038f6a0ff009f83683537322918f68ab62a22
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:f7718c1e5ff06ba9d7ddefb433c02b18b5a0a312f616b5e4bd4587f96e1d0b0c
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:ee23659ebbc498c3adf0ec1ea76b9eab325478c0a3785f94eb69094e3aaa02f1
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:1441881680eb208d99183d9730486d9e59c2298d687fbd4e44340a63bac4fa88
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:f2ef935e39c90af1bbc1076aa59ebd7bed397098b2f0ade1aa63cd718a614739
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:4d47fb8b7ca8155982c3d8e3e3f1d30b09fa52005477b4e398e2fb14cfa91d93
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:e220f813b0c8b2f5b501f31dd19aa26f20347b30269ea8488461b51bbe5a56e9
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:18bcafefd5018031309d7a762ac92cbd1553aefed727b17ced8bb2a5a6793dc2
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:f42e3f8593388bcf025e3e2dc0199838d70859dc761ccc0ee46368cd28fbe9e5
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:b521220c5cbe31c9f22ebea8c589c14f37d7618e48c84888f0e570f9bc16115a
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:dfa7809ad3f0eb08a1af05c6e9b610444ee51d5e6bbe28eac8194ba64132f25c
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:5c95a395165575711fb190760b544ad653eda736834a3eea7d6fa14a735a6dd1
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:4656fd4a846f3ecd954d05c1e2ca2dc4e5d229e70aaf89df2363bb04308c9b0d
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:0f9ea8bf5c4358847dff0f3352f186f91a330e944479883dd250cc0249b26cb6
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:a23ded2cf308dba865fad4fc48e8568fdd9c2215b401b0dc9899f050ceda8180
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:f831737dc97ecc6abd59b32ef06014586580bd8725419fef48dbdd1871e1a2cf
registry.redhat.io/rhel8/postgresql-13@sha256:bb0646dcee3237de3bc3e348f0f4d82c19ccffb1aab60bd197ec2fa126a92624
registry.redhat.io/rhel8/redis-6@sha256:109574014c1553a00839c6dc727232f34025b0aa918cc0c8f1639a4a04d9f6f0
registry.redhat.io/ubi8/ubi-minimal@sha256:e4ca1025efad7cc944fb991c716067b12e25ecbe05e6e81715a337179e417aa8
```

</details>
