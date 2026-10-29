# `aap-operator.v2.4.0-0.1774577278`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1774577278` |
| **Build date** | 2026-03-27 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1773412457`](./aap-operator.v2.4.0-0.1773412457.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c73197e51b2a92440fa84474558f019c144b0f03684a46a1e8b55689ace53ab0` |
| **Seen in OCP operator indexes** | 4.12, 4.14, 4.16–4.20 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.32 | 1774368033 | 2026-03-25 | `sha256:5564b5bbdcd1` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-22 | `sha256:e0dc8d6c6e22` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1774368033 | 2026-03-25 | `sha256:1891a04ebe22` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-22 | `sha256:6bfe8c10431e` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1774427670 | 2026-03-26 | `sha256:8f24e2d549cf` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1774368033 | 2026-03-25 | `sha256:344d909bc9fa` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1774368033 | 2026-03-25 | `sha256:c16e86fa4ba5` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1774368033 | 2026-03-25 | `sha256:c16e86fa4ba5` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1774368033 | 2026-03-25 | `sha256:c16e86fa4ba5` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.7 | 1774368033 | 2026-03-27 | `sha256:924a6060ca20` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-22 | `sha256:3b59f3f56f73` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 1774427670 | 2026-03-27 | `sha256:78dd50b09e82` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1774368033 | 2026-03-25 | `sha256:995a358995f7` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-22 | `sha256:5fab2892950c` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-22 | `sha256:716fce55d652` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1774368033 | 2026-03-25 | `sha256:950f4baa07dd` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-03-27 | `sha256:c73197e51b2a` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202509151014.p2.g9308e7f.assembly.stream.el8 | 2025-09-16 | `sha256:fa0acefda43e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1774427839 | 2026-03-25 | `sha256:6361cc5d749c` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1774427839 | 2026-03-25 | `sha256:6361cc5d749c` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1774427839 | 2026-03-25 | `sha256:6361cc5d749c` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1774427839 | 2026-03-25 | `sha256:6361cc5d749c` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1774427872 | 2026-03-25 | `sha256:c4af09814d1c` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1774427872 | 2026-03-25 | `sha256:c4af09814d1c` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1774427872 | 2026-03-25 | `sha256:c4af09814d1c` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1774368033 | 2026-03-24 | `sha256:69c5a7ae39a5` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1774368033 | 2026-03-24 | `sha256:69c5a7ae39a5` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1774368033 | 2026-03-24 | `sha256:69c5a7ae39a5` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:e0dc8d6c6e2280f0d7af8bf70faacbc025be16155c8f800209c81fd4cf8a9cc9
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:5564b5bbdcd12685473fa6c6b386c7b1d73b9c5326647bd2dcfab152ea8497d9
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:6bfe8c10431e97c73d9ea9752de6881f321d216d93449cc93958158656a19ca2
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:1891a04ebe22ce37dbdea314fdc14c190897f6922ead0aa2fe3411b92ed458eb
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:8f24e2d549cfd2bcaea9f12cb2a069693d667d9a26959134689af87b2bcde24b
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:344d909bc9fa2405770503a52959ad423f0e56f825111f46ccd48da83301cc68
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:c16e86fa4ba5658e37ea0526dc1dd45920d24aa6b0cd0d1a5516a0157eb318f8
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:3b59f3f56f737b130002b5f01bc0a47108d2fef1c413de6c2c0ebb66d128c1c3
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:924a6060ca2026cd940748cdc92bc7575da85d884068184ae5a0f40e6d16e09b
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:78dd50b09e821596063c0ff349d83ec0c8e0a36a3c958a2ec135438430a5ed94
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:5fab2892950c26d1dc5bde87356373f6f6d8cfa39c007b3e9ea8d59954b6f712
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:995a358995f7eed507d82da9b1cf16d19138342a945a5251b588a4659285db76
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:716fce55d6526df4ee8b6ba1bb1244e54e9bf091413717489f003d6e318d940e
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:950f4baa07dd0f498897f22da0d56e53f2964aadda51a56ad1e5af58c2628147
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:c73197e51b2a92440fa84474558f019c144b0f03684a46a1e8b55689ace53ab0
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:fa0acefda43e309e7f9f31f5247c933d0b868ff1573ece2f38e0549d7e2ec942
registry.redhat.io/rhel8/postgresql-15@sha256:6361cc5d749c2781932d8c188c2742e576547271f5fe60afe1fcd3341e323dcd
registry.redhat.io/rhel8/redis-6@sha256:c4af09814d1ccdd098d7a7eabc751ac72166d25273d14f0ebda2cd4da0938d95
registry.redhat.io/ubi8/ubi-minimal@sha256:69c5a7ae39a5ab42160d4c6dd6014360a65659541766129225dc0402a41b2825
```

</details>
