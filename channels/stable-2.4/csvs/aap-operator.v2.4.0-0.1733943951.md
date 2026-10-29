# `aap-operator.v2.4.0-0.1733943951`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1733943951` |
| **Build date** | 2024-12-11 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1733185647`](./aap-operator.v2.4.0-0.1733185647.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:674cdb2a5d0801441dd73a0b8484195e834c3cfba8d1160e8b24b6f456a0ecd5` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.15 | 2 | 2024-12-11 | `sha256:3f6fb1f31d98` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 165 | 2024-12-11 | `sha256:9d4bce268f5d` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 30 | 2024-12-11 | `sha256:dc5df1949cb1` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 165 | 2024-12-11 | `sha256:be9435b5199a` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 29 | 2024-12-11 | `sha256:c5e5118c82ca` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 789 | 2024-12-11 | `sha256:92829bc65fc8` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 859 | 2024-12-11 | `sha256:367c49fc8e65` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 859 | 2024-12-11 | `sha256:367c49fc8e65` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 859 | 2024-12-11 | `sha256:367c49fc8e65` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 34 | 2024-12-11 | `sha256:57c99d626965` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 164 | 2024-12-11 | `sha256:57aca39d9a83` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 32 | 2024-12-11 | `sha256:4235bd7fd7ce` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.241210 | 1 | 2024-12-11 | `sha256:375e257c2f69` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 31 | 2024-12-11 | `sha256:872f3bfa0a82` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 157 | 2024-12-11 | `sha256:8604b77de887` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 198 | 2024-12-11 | `sha256:0faa828b7825` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2215 | 2024-12-11 | `sha256:674cdb2a5d08` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202411130135.p0.g9308e7f.assembly.stream.el8 | 2024-11-13 | `sha256:1172e150fff2` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 210.1732637108 | 2024-11-26 | `sha256:c10024430627` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 210.1732637108 | 2024-11-26 | `sha256:c10024430627` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 210.1732637108 | 2024-11-26 | `sha256:c10024430627` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 210.1732637108 | 2024-11-26 | `sha256:c10024430627` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209.1732637107 | 2024-11-26 | `sha256:bb24ede28ec4` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209.1732637107 | 2024-11-26 | `sha256:bb24ede28ec4` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209.1732637107 | 2024-11-26 | `sha256:bb24ede28ec4` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:9d4bce268f5d5de23701af6eafd87a8f64695a4d86aa2ee59c2e44c8766016fc
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:3f6fb1f31d98af18ed0763d6f0d098be016cc828b211b612d9339e7f2734e788
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:be9435b5199a342255680b793fb0a92522be0220b7503e1d5aa6c907020a4bbc
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:dc5df1949cb1fc09c6d84860e141eaecfd5b3016939547c17fb51b084d09f9de
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:c5e5118c82caa59b1a43dfb9f3d786529cbbbd224a86abac156c5b4070e10933
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:92829bc65fc8c545237749b9322892203ad2122f670f6b3f766ea948e6a197d8
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:367c49fc8e65aac6c40a985c687a06ddfc95bcda654e7c2318dabfe3812e64c5
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:57aca39d9a832fb620e69a28e5c066d58ef0a7ad54bb9a39a2e1f0c37fcac44b
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:57c99d62696573b90efa86c04e0f9948f6437a7d0e1c9a146627e47eed2111ad
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:4235bd7fd7cee2bd5f794eb9cf7be2373577180c950fc27ef9bc743ddc96031a
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:872f3bfa0a823f08e50f42dd2b18f8e9695bed0ce18fdbcc957376482f735147
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:375e257c2f69134e2173600cb41af87da9a250dc973382de0b7fbc5baf0ee8fd
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:8604b77de8878e9c4cdc4c84e93b550621d315f3e3038bc247cb47d83f5077dc
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:0faa828b78257d92191f2771a3da9a407ad0dabc9e3f52a5c513efe9ae0e65e3
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:674cdb2a5d0801441dd73a0b8484195e834c3cfba8d1160e8b24b6f456a0ecd5
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:1172e150fff22c5eeab572f26961f3f53fbf896ee76d08c7503cfe2777c55458
registry.redhat.io/rhel8/postgresql-13@sha256:c100244306278d142d9de26c5387e0d030dd4e68d16d4eec1aa428a97b2de04e
registry.redhat.io/rhel8/redis-6@sha256:bb24ede28ec4cd2e416f6e299ee16531d8bc0a7496d3e44ac7619d9b09366737
registry.redhat.io/ubi8/ubi-minimal@sha256:c12e67af6a7e15113d76bc72f10bef2045c026c71ec8b7124c8a075458188a83
```

</details>
