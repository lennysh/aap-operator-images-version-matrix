# `aap-operator.v2.4.0-0.1787241496`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1787241496` |
| **Build date** | 2026-08-20 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1785432057`](./aap-operator.v2.4.0-0.1785432057.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:6d9332219f8b928ab5ed0b9d6a412b6cb5ab7da9c993eee0272b5ff892d15bd9` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.35 | 1787081751 | 2026-08-19 | `sha256:46377081b923` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-08-16 | `sha256:9786bd295908` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1787081751 | 2026-08-19 | `sha256:69c83a3dbcc5` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-08-16 | `sha256:2dfab57b5bd9` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1787171612 | 2026-08-20 | `sha256:6b7bc18358a2` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1787081751 | 2026-08-20 | `sha256:00dc5d463362` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1787081751 | 2026-08-20 | `sha256:9ce192e34b96` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1787081751 | 2026-08-20 | `sha256:9ce192e34b96` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1787081751 | 2026-08-20 | `sha256:9ce192e34b96` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1787081751 | 2026-08-19 | `sha256:3b2480e77dde` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-08-16 | `sha256:1189f5ef16c0` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1787171612 | 2026-08-20 | `sha256:fdb96fa1d74d` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1787081751 | 2026-08-20 | `sha256:dec7610616d4` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-08-16 | `sha256:17ee24678b59` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-08-16 | `sha256:f33b013a2b45` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1787081751 | 2026-08-20 | `sha256:4353915bef79` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-08-20 | `sha256:6d9332219f8b` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202607201846.p2.g9308e7f.assembly.stream.el8 | 2026-07-20 | `sha256:c39d4f123860` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1787172163 | 2026-08-19 | `sha256:9d9717f947c6` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1787172163 | 2026-08-19 | `sha256:9d9717f947c6` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1787172163 | 2026-08-19 | `sha256:9d9717f947c6` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1787172163 | 2026-08-19 | `sha256:9d9717f947c6` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1787171331 | 2026-08-19 | `sha256:0c7785376777` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1787171331 | 2026-08-19 | `sha256:0c7785376777` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1787171331 | 2026-08-19 | `sha256:0c7785376777` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1787081751 | 2026-08-18 | `sha256:8eb4bce22077` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1787081751 | 2026-08-18 | `sha256:8eb4bce22077` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1787081751 | 2026-08-18 | `sha256:8eb4bce22077` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:9786bd2959086ec931135bff6b4c1a2fa840ad6d9bd21ae9b5ff793f9fc873c0
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:46377081b9230116058ec0d00cae010a4c40774d5c06f1669d46700b21d9b7b0
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:2dfab57b5bd9c31009e914071f924a35f1c6e09a6ff66558bb4b2c691f531dbe
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:69c83a3dbcc586c2933fb1d95578cd67bfaf6a324e157028f92efcb02366a04d
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:6b7bc18358a2543ea5480537208908b00dbfa284866647fd78a020f40a8c899c
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:00dc5d4633628c3b2dd0092718ac6caf13b96626777914f78b1f010ed6772e8e
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:9ce192e34b969b5763c31f3f4e59529e7ae8a219699489a955f6851b605fe513
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:1189f5ef16c0fde8074bcd4af92db84cd068ff43fa9d6f6bf2251b89eb41cd8c
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:3b2480e77dded4841977db35cf7e40de90a1632d4d8b9f14f673d6ae879e47d3
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:fdb96fa1d74d18cb6cc8cced11596d661dee96b1ffeb81dedd5eb0bdc0ca3581
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:17ee24678b59f4c45f1bffa14d74ad9a27d311340ae4d0baa05b59d9909aec36
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:dec7610616d4a6351cc0df74874cdefcec38a17f3399042ea9c469c0c0e2b6f8
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:f33b013a2b453b47c651a4882e54a4a00ba9c7737997bcaed2898e8b9b7bcd25
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:4353915bef79a84a41f5d8c7e1b3f9fb67b2232ed286ae2f152e483ffc3f263a
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:6d9332219f8b928ab5ed0b9d6a412b6cb5ab7da9c993eee0272b5ff892d15bd9
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:c39d4f12386050f78c335b70129b966039576acd22f7cb117538902ede35fb77
registry.redhat.io/rhel8/postgresql-15@sha256:9d9717f947c60a4d976cc06398bd3129bab7868a5071852aba716df1e97632fc
registry.redhat.io/rhel8/redis-6@sha256:0c77853767770ba5529efea6eed1fd7d9873e286059e807b322289ea17b7e01a
registry.redhat.io/ubi8/ubi-minimal@sha256:8eb4bce220776c3ce885d9ee48430094c9bce2943de30fcdc1e080acde6948f9
```

</details>
