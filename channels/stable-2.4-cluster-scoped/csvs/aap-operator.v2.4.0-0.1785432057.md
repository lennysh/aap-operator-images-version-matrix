# `aap-operator.v2.4.0-0.1785432057`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1785432057` |
| **Build date** | 2026-07-30 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1784076997`](./aap-operator.v2.4.0-0.1784076997.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:912f3beb5de0d6e7560927dba5bf280230b17eb4b1be1d15ea2c403a029fc37f` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.35 | 1785302592 | 2026-07-30 | `sha256:7d5376524ca9` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-26 | `sha256:00be85d50184` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1785302592 | 2026-07-30 | `sha256:b5f9d15a185e` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-26 | `sha256:8028b9e37864` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1785112314 | 2026-07-27 | `sha256:095acb687447` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1785302592 | 2026-07-30 | `sha256:cefb154baa3b` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1785302592 | 2026-07-30 | `sha256:9658ae0c0a3d` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1785302592 | 2026-07-30 | `sha256:9658ae0c0a3d` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1785302592 | 2026-07-30 | `sha256:9658ae0c0a3d` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1785302592 | 2026-07-30 | `sha256:b44c0eb7393a` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-26 | `sha256:6e7b7abe4b2a` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1785112314 | 2026-07-30 | `sha256:f87303ee81ff` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1785302592 | 2026-07-30 | `sha256:fd87d853852d` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-26 | `sha256:3e12a58b6533` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-07-28 | `sha256:f3fb187e0a8f` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1785302592 | 2026-07-30 | `sha256:f0cbd11aecfc` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-07-30 | `sha256:912f3beb5de0` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202607201846.p2.g9308e7f.assembly.stream.el8 | 2026-07-20 | `sha256:c39d4f123860` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1785389009 | 2026-07-30 | `sha256:e8c30c0741b2` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1785389009 | 2026-07-30 | `sha256:e8c30c0741b2` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1785389009 | 2026-07-30 | `sha256:e8c30c0741b2` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1785389009 | 2026-07-30 | `sha256:e8c30c0741b2` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1785388756 | 2026-07-30 | `sha256:9bfd67da99d2` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1785388756 | 2026-07-30 | `sha256:9bfd67da99d2` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1785388756 | 2026-07-30 | `sha256:9bfd67da99d2` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1785302592 | 2026-07-29 | `sha256:b915e698d01c` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1785302592 | 2026-07-29 | `sha256:b915e698d01c` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1785302592 | 2026-07-29 | `sha256:b915e698d01c` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:00be85d501848b7f0b1a461de205d1979cabebff847a88d144709207c49acb54
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:7d5376524ca97ef2274ec9a222ba8913527c507ef0efe8856d3b5ec1ca74b269
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:8028b9e3786417ffddf26d42692c89ada1b866680734510da038259413bad9d7
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:b5f9d15a185ef16593b5e1780576e0b89d30f63232f4bf00d5a671f7924cf9d4
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:095acb68744743bc42aaa12e0d924d2e5b01b0eaf3bd07979a6287e20c506e23
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:cefb154baa3ba9a9756db1109ec4eea136eb5f55e503249a7fd366b9655f722a
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:9658ae0c0a3dd3d75db6b3d5708e2fdcd2af2770bd5310e8841b26fbdf94a260
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:6e7b7abe4b2a8b34198b0941cd232c1d0f9fb79af3ce4517cb1b1a398aa6cb52
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:b44c0eb7393a9bae7be2fc3dd57d7c043a085084569962088ad76a4143061c6f
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:f87303ee81ff81d9076f89ada546f5b59ff647ccf0dbf2de3d4a279ea7fd9866
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:3e12a58b653337b6ecebfbddadceb88de7d0448ab077e82eee6b8a53a08c3bd0
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:fd87d853852db772145acaf3a8e4736f7027e60dec16de7b37d0c49268a5eaac
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:f3fb187e0a8f4ceed45b949911436f7cb0f9ebd91656cc58214ba3893f242367
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:f0cbd11aecfc836caa2dd08cae088bb4e05cb370b3ee5af3a9f5a3efe7dc5b38
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:912f3beb5de0d6e7560927dba5bf280230b17eb4b1be1d15ea2c403a029fc37f
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:c39d4f12386050f78c335b70129b966039576acd22f7cb117538902ede35fb77
registry.redhat.io/rhel8/postgresql-15@sha256:e8c30c0741b2ca52c2f1286e8fba9c4ef054b90a9ce4558f0c4dd82fbdbea393
registry.redhat.io/rhel8/redis-6@sha256:9bfd67da99d2660a85ac0e46405b0ad55b91ca3ab204183966e007c04482ae00
registry.redhat.io/ubi8/ubi-minimal@sha256:b915e698d01cf0750b82c6ab54adc794870381271670fd7211b082f19f8564f7
```

</details>
