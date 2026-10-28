# `aap-operator.v2.4.0-0.1789667225`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1789667225` |
| **Build date** | 2026-09-17 |
| **Replaces** | [`aap-operator.v2.4.0-0.1787241496`](./aap-operator.v2.4.0-0.1787241496.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:efd8a1fac150783f8133054261491006d386865b38dabc3c43ddc5149380f19e` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.36 | 1789521592 | 2026-09-17 | `sha256:e58bad21a135` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-09-13 | `sha256:46195cac1a73` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1789521592 | 2026-09-17 | `sha256:ba2be60b079e` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-09-13 | `sha256:c716082483b1` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1789528466 | 2026-09-17 | `sha256:5109e614dee6` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1789521592 | 2026-09-17 | `sha256:1b92af79b5f0` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1789521592 | 2026-09-17 | `sha256:633e52a24435` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1789521592 | 2026-09-17 | `sha256:633e52a24435` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1789521592 | 2026-09-17 | `sha256:633e52a24435` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1789521592 | 2026-09-16 | `sha256:af888be5f654` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-09-13 | `sha256:821f1c4f3674` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1789528466 | 2026-09-17 | `sha256:b666042f2f43` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1789521592 | 2026-09-17 | `sha256:281563110a94` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-09-13 | `sha256:dee5756dde77` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-09-16 | `sha256:ca22a8555c9a` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1789521592 | 2026-09-17 | `sha256:03d241dc09de` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-09-17 | `sha256:efd8a1fac150` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202608180326.p2.g9308e7f.assembly.stream.el8 | 2026-08-18 | `sha256:26b79b3526f4` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1789609073 | 2026-09-17 | `sha256:9772f340faf8` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1789609073 | 2026-09-17 | `sha256:9772f340faf8` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1789609073 | 2026-09-17 | `sha256:9772f340faf8` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1789609073 | 2026-09-17 | `sha256:9772f340faf8` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1789605192 | 2026-09-17 | `sha256:e4b3e6b5dfbb` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1789605192 | 2026-09-17 | `sha256:e4b3e6b5dfbb` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1789605192 | 2026-09-17 | `sha256:e4b3e6b5dfbb` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1789521592 | 2026-09-16 | `sha256:128021168edb` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1789521592 | 2026-09-16 | `sha256:128021168edb` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1789521592 | 2026-09-16 | `sha256:128021168edb` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:46195cac1a73a315e5ce437cc597a5b2c45861c6bec4b829e8933632033708eb
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:e58bad21a1352d11053b7181dce3825d3fbb508f9eb08797fb5990550a841f8c
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:c716082483b15d0c3fb9db5632371e3b31a6625791b5b89ee6b8bdedf1b996f0
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:ba2be60b079e9966fe4ca928d1833bee60902657c5009d3a1692938b491ed487
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:5109e614dee6d39f53c4da7f3ec72ed11e4b4f2ebbaadc35a6c529c05c2ec822
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:1b92af79b5f07d8c22ed2f178863b6e37f5100eeafe1183b720a7abfe9a089e1
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:633e52a24435646a6014f6d66552ed6b5fb3e4d4c5cac278ec1ed0c419fb433a
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:821f1c4f3674020c6cc7267ff5ec992a7b60b3f658fb447f564f69e2d1f53301
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:af888be5f654eb5cae492e9d2a60e8a6acf5e46020b461099e29e7858b7cdd87
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:b666042f2f4308b480b3a44580ea6df88d9cc04beff8844ae0f19eed06809a10
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:dee5756dde77cd1ef8feebb032b5465e44dec0a8490d2cc38754d71066ee89c4
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:281563110a947b1da70b46803dbeebfea159d0b30516fa4ca6529bf52ec8410c
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:ca22a8555c9a4542d5993734c24f4fb7794965b13db6439bd21eb3354028d057
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:03d241dc09dedd7b27de18286c2b7797540a58bb5710b4e3df88621a6413ce87
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:efd8a1fac150783f8133054261491006d386865b38dabc3c43ddc5149380f19e
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:26b79b3526f4daf4ecfc42b1dc72ed005bf72fd7bafa386bd37ed136222620a6
registry.redhat.io/rhel8/postgresql-15@sha256:9772f340faf89f9872346408a00b0532978779450b486ae834dc7a12c2ff02f4
registry.redhat.io/rhel8/redis-6@sha256:e4b3e6b5dfbb886568e5447fef190e01228945d86c91fdf9c84d0c571ab8b8a2
registry.redhat.io/ubi8/ubi-minimal@sha256:128021168edb5b3013258601a2dffe93fddfed91cf996c08c76a24dfdcd6de13
```

</details>
