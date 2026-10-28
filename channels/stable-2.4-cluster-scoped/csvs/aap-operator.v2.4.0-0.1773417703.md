# `aap-operator.v2.4.0-0.1773417703`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1773417703` |
| **Build date** | 2026-03-13 |
| **Replaces** | [`aap-operator.v2.4.0-0.1768599045`](./aap-operator.v2.4.0-0.1768599045.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:efdf66f48d9ef544b76d16bcdf049369d28ba39b2f7fcc04e9eeee7445a2a908` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.31 | 1772599255 | 2026-03-13 | `sha256:41ae30fd35bc` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-13 | `sha256:62abcf1d90ae` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.9 | 1772599255 | 2026-03-13 | `sha256:57264679eab3` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-13 | `sha256:eee763b66086` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.9 | 1772713772 | 2026-03-13 | `sha256:a3d88dd9c50b` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1772599255 | 2026-03-12 | `sha256:2da862185ac0` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1771947229 | 2026-03-13 | `sha256:e2f74f6e2331` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1771947229 | 2026-03-13 | `sha256:e2f74f6e2331` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1771947229 | 2026-03-13 | `sha256:e2f74f6e2331` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.6 | 1772599255 | 2026-03-13 | `sha256:50d145a3ce3a` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-13 | `sha256:42a2eae2e5ba` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 1772713772 | 2026-03-13 | `sha256:1c7029bc60bd` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260225 | 1772599255 | 2026-03-12 | `sha256:28268337210e` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-13 | `sha256:fa770ad9c4e7` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-03-13 | `sha256:13dacc2f3c11` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1771947229 | 2026-03-13 | `sha256:ed1b3fa1fa02` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-03-13 | `sha256:efdf66f48d9e` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202509151014.p2.g9308e7f.assembly.stream.el8 | 2025-09-16 | `sha256:fa0acefda43e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1773077204 | 2026-03-09 | `sha256:7fdc65364d67` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1773077204 | 2026-03-09 | `sha256:7fdc65364d67` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1773077204 | 2026-03-09 | `sha256:7fdc65364d67` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1773077204 | 2026-03-09 | `sha256:7fdc65364d67` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1772713890 | 2026-03-05 | `sha256:ad6c53f6e97c` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1772713890 | 2026-03-05 | `sha256:ad6c53f6e97c` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1772713890 | 2026-03-05 | `sha256:ad6c53f6e97c` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1772599255 | 2026-03-04 | `sha256:b880e16b888f` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1772599255 | 2026-03-04 | `sha256:b880e16b888f` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1772599255 | 2026-03-04 | `sha256:b880e16b888f` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:62abcf1d90aef580bd4a2335fbc4fb4802f1d7a4ec0e35fa3113f021be769075
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:41ae30fd35bcca310056ced9b77c0571ea7deca36f8ed4e70161144eff2c6600
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:eee763b66086ed18c606cbdbbb1ce22093fa7a8964d78c18b82877990bf4e35f
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:57264679eab3bdbe2fc58a4b80b5ea899818c5760775e6480ac2902b3b50acab
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:a3d88dd9c50bfaa03e4712e175bb8dd3bd4a0908aa4f830df9df920ef2a01889
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:2da862185ac01423906a94ddec8ab8bf6248b7a95d3e8a8c22229fcb9cfcea3f
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:e2f74f6e2331c590238322716e85e7111cefa401955faf8e56922df359dbafd2
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:42a2eae2e5ba899b2b0cacd7a0411d93dfe0f550ce5111ee5c5d2f081a9ae8de
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:50d145a3ce3a0136320596177f2c1aa6de25310a452249424565fdcaa7c50a21
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:1c7029bc60bd9da0954e04293ebe915db36eebb494241ec9e196d9c4ddba22c1
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:fa770ad9c4e7d3d35667c951d75a6f50434a76320970ba90d79ed783a1ee5635
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:28268337210e8a2560f89c9a845c91532acf181927315b9829767a1351646d6b
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:13dacc2f3c11fbc0ea45342aa0d119cced19cd786b2c057c51928c2c18a5d220
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:ed1b3fa1fa0205bae76b49284449263a67ba2811ceeeb1d14f7b28184481d418
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:efdf66f48d9ef544b76d16bcdf049369d28ba39b2f7fcc04e9eeee7445a2a908
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:fa0acefda43e309e7f9f31f5247c933d0b868ff1573ece2f38e0549d7e2ec942
registry.redhat.io/rhel8/postgresql-15@sha256:7fdc65364d67e5d08f91956c368f1b43670383886049c7ce2b7591cc0a715f76
registry.redhat.io/rhel8/redis-6@sha256:ad6c53f6e97c583e7402ae505d8f9f27d5fe7d9227fb248c701595f86a5b1b31
registry.redhat.io/ubi8/ubi-minimal@sha256:b880e16b888f47bc3fae64e67cd9776b24372f2e7ec2051f5a9386de6f5a75ac
```

</details>
