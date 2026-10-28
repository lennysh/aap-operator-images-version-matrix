# `aap-operator.v2.5.0-0.1740773472`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1740773472` |
| **Build date** | 2025-02-28 |
| **Replaces** | [`aap-operator.v2.5.0-0.1740093573`](./aap-operator.v2.5.0-0.1740093573.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:70000ea53693a3514b7372414c88be7041eb753174fffbde460a84c8f097ccf1` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.8 | 17 | 2025-02-28 | `sha256:fa5a00fe0003` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 163 | 2025-02-28 | `sha256:7c42fb8f5369` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.4 | 18 | 2025-02-28 | `sha256:32ee41cb3986` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 165 | 2025-02-28 | `sha256:5c8b5815ee73` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.4 | 10 | 2025-02-28 | `sha256:01236bfbeef6` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 833 | 2025-02-28 | `sha256:be46ba015b7d` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 918 | 2025-02-28 | `sha256:ac8541737645` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 918 | 2025-02-28 | `sha256:ac8541737645` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 918 | 2025-02-28 | `sha256:ac8541737645` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 53 | 2025-02-28 | `sha256:bd769e566155` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250305 | 5 | 2025-02-28 | `sha256:de2db8784787` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 211 | 2025-02-28 | `sha256:52e419ec4cac` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 43 | 2025-02-28 | `sha256:365280a1853b` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 165 | 2025-02-28 | `sha256:5517284bbb98` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 38 | 2025-02-28 | `sha256:2577a42fd848` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250204 | 7 | 2025-02-28 | `sha256:e31ce3f79d8f` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 122 | 2025-02-28 | `sha256:ad130041fe51` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 117 | 2025-02-28 | `sha256:b829ae200701` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 146 | 2025-02-28 | `sha256:68bbc470108b` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1165 | 2025-02-28 | `sha256:70000ea53693` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202502171304.p0.g9308e7f.assembly.stream.el8 | 2025-02-17 | `sha256:c811cffdb695` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740072850 | 2025-02-20 | `sha256:0ffd9b340ad8` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740072850 | 2025-02-20 | `sha256:0ffd9b340ad8` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740072850 | 2025-02-20 | `sha256:0ffd9b340ad8` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740072850 | 2025-02-20 | `sha256:0ffd9b340ad8` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740072850 | 2025-02-20 | `sha256:0ffd9b340ad8` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:7c42fb8f5369bba9ab8187a0eff4e24d2ac2230983024581515989dc134e4b3a
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:fa5a00fe00034f5558118fd0cb80008c7802bf938e34ab13059e83e50e0de03a
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:5c8b5815ee73154a6fb807a37d86cebc805f3d20616ade69856614c697365e36
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:32ee41cb39860da2c110f918ccc0dc0ac7728da76ed898f8dd5f2c6cc8db7038
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:01236bfbeef6ccfab319387bdb7d1eca6da32d8074c3b5d69a158a723be989d8
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:be46ba015b7dbc00d8ab1d603be798ed6f56acab8c5e173543488d7b1cbbc7a9
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:ac8541737645ed47f25ab9dcb4b1ce103edfd8913f238ac1070d8d670d95da2c
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:bd769e566155d61e13592371167d6fb28acb8a56ffec944fdfb5e3afd9b9dcbd
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:52e419ec4cac97685aa8757b394d8cd47af2584153d90e65ac253e206d34fb24
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:de2db8784787cd693ceb9c3635ce132eb95817b9b570fe9bc7dcab90ee101dda
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:5517284bbb9831a53dcd63d035d4b395daf1f685bd32ae71b08931ca4b935177
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:365280a1853b44913234153bd633c20ed2c7ff1ea83701552b16a09de3bd57c7
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:2577a42fd848a6c9afb8fe48b824504e360c49eab093c89bb05b8ecd11f55fb3
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:ad130041fe515a0acd85e03abf1369fc98cf7922b775865254f8273f7bb8807d
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:e31ce3f79d8f9fca3f7b9006d7732a313e35fa342eadbb757fda50a30d21bc70
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:b829ae2007018e3ad05779fa1f01ea48d9a74f6d82370e6671ff7e3ba4dbdf15
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:68bbc470108b9563705dfbc8a888553a24f2028ded26ef51441c55305d2bbee5
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:70000ea53693a3514b7372414c88be7041eb753174fffbde460a84c8f097ccf1
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:c811cffdb695664388fbbece7a6d434ab44ada8bccd02581179ee62859db7e02
registry.redhat.io/rhel8/postgresql-15@sha256:0ffd9b340ad815070f81efb870ea7bcff03ef3cf68e6168fc67de35371d937ca
registry.redhat.io/rhel8/redis-6@sha256:5aae6ed0346240c17e62fa32425f84a8ad45498a9599a61bcc324bd17b2e54ce
registry.redhat.io/ubi8/ubi-minimal@sha256:c38cc770631788157f8ea989df65ff30359c9f8af3246fef244b32caed9d5862
```

</details>
