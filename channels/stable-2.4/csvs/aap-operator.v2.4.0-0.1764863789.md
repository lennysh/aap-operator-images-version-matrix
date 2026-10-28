# `aap-operator.v2.4.0-0.1764863789`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1764863789` |
| **Build date** | 2025-12-04 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1763136910`](./aap-operator.v2.4.0-0.1763136910.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:43f77fc68979d735cec7c9754ee152e996df775540f6c591ad23c71dc3701178` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.28 | 1764046129 | 2025-12-03 | `sha256:59be91b48de2` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2025-11-29 | `sha256:5662e37033b9` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 1764046129 | 2025-12-01 | `sha256:f25ee41cd983` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2025-11-29 | `sha256:5ee941e5c68f` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 1764274975 | 2025-11-29 | `sha256:d4e9c305bb8c` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 1764046129 | 2025-12-02 | `sha256:6332f9dc1cb5` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1764046129 | 2025-12-04 | `sha256:b1caab055b36` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1764046129 | 2025-12-04 | `sha256:b1caab055b36` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1764046129 | 2025-12-04 | `sha256:b1caab055b36` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.5 | 1764046129 | 2025-11-29 | `sha256:2d2afa34f4ca` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2025-11-29 | `sha256:129fb767723f` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 1764274975 | 2025-11-29 | `sha256:b466c985af34` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.251202 | 1764046129 | 2025-12-04 | `sha256:9d75ba41f5c4` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2025-11-29 | `sha256:d5ebbaf12f59` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2025-12-02 | `sha256:c2dac27f5afa` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1764046129 | 2025-12-04 | `sha256:81b976ff2a53` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2025-12-04 | `sha256:43f77fc68979` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202509151014.p2.g9308e7f.assembly.stream.el8 | 2025-09-16 | `sha256:fa0acefda43e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1764260985 | 2025-11-27 | `sha256:042f6efe0f16` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1764260985 | 2025-11-27 | `sha256:042f6efe0f16` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1764260985 | 2025-11-27 | `sha256:042f6efe0f16` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1764260985 | 2025-11-27 | `sha256:042f6efe0f16` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1764260860 | 2025-11-27 | `sha256:c521ebfcd5c3` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1764260860 | 2025-11-27 | `sha256:c521ebfcd5c3` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1764260860 | 2025-11-27 | `sha256:c521ebfcd5c3` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1764046129 | 2025-11-25 | `sha256:a670c5b61328` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1764046129 | 2025-11-25 | `sha256:a670c5b61328` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1764046129 | 2025-11-25 | `sha256:a670c5b61328` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:5662e37033b97abcfae12d4589d7a2a2befba67946b01893c47582a3d1230a7a
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:59be91b48de218d7f8326bb1ef4bdcfb5509ebb8df910d9dad20d5644e2dd9fd
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:5ee941e5c68f781c7613d7916dafa83faeb7a73e90aeeaaed5ac8b9dc94792c2
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:f25ee41cd983a0cdc03c1faae2a08d167f84b69344f0ae6989e6f4d1d0bf6962
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:d4e9c305bb8c960a36042a10ee3598a885ddfcee3495a63a230ce2de21baf746
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:6332f9dc1cb52f746d7ae69318d4f8ec7a5c8e04cafda94b1185559408a53424
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:b1caab055b36f279091e80dfc36ae5db477defbb5528ff3b7c4fb31c50ab32e5
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:129fb767723f12c2ae3b970710848be00f359b80aa6184d48c1be020b94297fc
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:2d2afa34f4ca55167ef25facdd54f44488486caea214f2dfd0f6ad15583ee999
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:b466c985af349a5400b2fbc93f4fba15545b19602d527bc6fbda1b37e26c20bd
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:d5ebbaf12f59aac81bd17c579a35fd59e40d00c32c563968a460ccfcfa302f33
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:9d75ba41f5c4db204be2a29dc6b436e69f808ad039de832b6e41fe80627bbd4f
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:c2dac27f5afa6cae8d4a932030b40c9cfaabe5139ad420d37577f676eb44dac6
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:81b976ff2a53ea3a02bb3da7a3ce1838a76e27b495582b9f6b02f1700d94b5ad
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:43f77fc68979d735cec7c9754ee152e996df775540f6c591ad23c71dc3701178
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:fa0acefda43e309e7f9f31f5247c933d0b868ff1573ece2f38e0549d7e2ec942
registry.redhat.io/rhel8/postgresql-15@sha256:042f6efe0f16e94ffb2d0a3bede852bb026b6dce661ac5b339e6f63846467b9d
registry.redhat.io/rhel8/redis-6@sha256:c521ebfcd5c334c46b4bb7d8ddad270f789857de2fcc374c7ca338c078ec4b71
registry.redhat.io/ubi8/ubi-minimal@sha256:a670c5b613280e17a666c858c9263a50aafe1a023a8d5730c7a83cb53771487b
```

</details>
