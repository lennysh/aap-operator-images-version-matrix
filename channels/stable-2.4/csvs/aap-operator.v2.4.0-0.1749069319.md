# `aap-operator.v2.4.0-0.1749069319`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1749069319` |
| **Build date** | 2025-06-04 |
| **Previous CSV** | — |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:178a702dfa2951b5e4c26aa2d3b9dc03aba45d30bf488110e2dc8e28057a5868` |
| **Seen in OCP operator indexes** | 4.12–4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.23 | 2 | 2025-05-30 | `sha256:9aaf5ff60788` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 175 | 2025-05-28 | `sha256:dc165ec26449` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 39 | 2025-05-28 | `sha256:7942468c0147` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 175 | 2025-05-28 | `sha256:63659923e758` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 37 | 2025-05-28 | `sha256:ebb6bfa656c2` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 921 | 2025-05-28 | `sha256:e79bec80fcda` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1030 | 2025-06-04 | `sha256:344396fd2c81` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1030 | 2025-06-04 | `sha256:344396fd2c81` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1030 | 2025-06-04 | `sha256:344396fd2c81` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.4 | 1 | 2025-05-28 | `sha256:6dcc18690f53` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 174 | 2025-05-28 | `sha256:013cf55082b2` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.4 | 1 | 2025-05-28 | `sha256:a3d55db1fb0a` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 12 | 2025-05-28 | `sha256:1d0bb5a320fc` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 44 | 2025-05-28 | `sha256:8ebdf2645f56` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 172 | 2025-05-28 | `sha256:3152f929db0c` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 212 | 2025-06-04 | `sha256:0307fd0e9031` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2582 | 2025-06-04 | `sha256:178a702dfa29` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202504220035.p0.g9308e7f.assembly.stream.el8 | 2025-04-22 | `sha256:bb84ead43704` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 216 | 2025-05-29 | `sha256:f975bcfc5497` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 216 | 2025-05-29 | `sha256:f975bcfc5497` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 216 | 2025-05-29 | `sha256:f975bcfc5497` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 216 | 2025-05-29 | `sha256:f975bcfc5497` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215 | 2025-05-29 | `sha256:b43e9d9c97e7` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215 | 2025-05-29 | `sha256:b43e9d9c97e7` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 215 | 2025-05-29 | `sha256:b43e9d9c97e7` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295 | 2025-05-29 | `sha256:73064ec359dc` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295 | 2025-05-29 | `sha256:73064ec359dc` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1295 | 2025-05-29 | `sha256:73064ec359dc` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:dc165ec26449be9c5dcf8cf0ee7e2f135c435d9a0b8b33437b00499a314b65c3
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:9aaf5ff60788cabc58ada8094dcaee1edb6d425675e75f1683e11d72bb88e8a5
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:63659923e758ceee93fcf3bfbae9392898ba600f065b4ab9db5bb732478809c1
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:7942468c01471e3bbce6bb5592cec8145c73e1566d186acbb7eaf4ebcf2fd04d
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:ebb6bfa656c285960ece5903eca9bc830e8de436ee37d1c7d808c84f8698b384
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:e79bec80fcda5d5a3dfbce4f5324d4ae7119dded179998eaaad361804bbc42a0
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:344396fd2c812be135f3a7c9c869f5bdb123780c4ee8355ea513904663a9b220
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:013cf55082b202d5ee21ed2d18af1bea0bf471c16b47a0adf4b0d677bf7f88fb
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:6dcc18690f5348b84104569aa579fe4ca25a0a9b0079174f4f164eb44ed6eb85
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:a3d55db1fb0a3374d8557dfe582449a525b97dc9efeba64a9e7606901663892f
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:8ebdf2645f564efef2eda63c6848f4bd86f1feeefb7e4951fcbd9eb4da5e4ff6
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:1d0bb5a320fc8ecc13f5cb7a65a90d106c7110ed9d30d33a8421ab4d033e5a0e
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:3152f929db0cea0858db6c7443b9c75c6a986f7c7d6e4a4e7e8fc86eac40a7d5
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:0307fd0e90312c37bd352ea3a43d6322c450dad4e50263c7f721b4efc8bc5ae5
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:178a702dfa2951b5e4c26aa2d3b9dc03aba45d30bf488110e2dc8e28057a5868
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:bb84ead437042603254efcb703442be8500a9450b10bbcaaee81b48a6ed869ea
registry.redhat.io/rhel8/postgresql-13@sha256:f975bcfc549728776d3c27d1f545a33063992ad5721b5d9ee7aad3c89d3f7bde
registry.redhat.io/rhel8/redis-6@sha256:b43e9d9c97e74306a913321a5505768275147dd2b8bd75573bcaae0d73b24639
registry.redhat.io/ubi8/ubi-minimal@sha256:73064ec359dcd71e56677f8173a134809c885484ba89e6a137d33521ad29dd4c
```

</details>
