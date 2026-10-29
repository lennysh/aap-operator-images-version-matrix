# `aap-operator.v2.4.0-0.1733185647`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1733185647` |
| **Build date** | 2024-12-03 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1730152858`](./aap-operator.v2.4.0-0.1730152858.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:95a76c94b8b5c68b23cfaee042797d0b21c92fb4bc06c00f794ec5e8dcd64c14` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.13 | 7 | 2024-12-02 | `sha256:307f3f5126fd` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 164 | 2024-12-02 | `sha256:472466abfe56` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 29 | 2024-12-02 | `sha256:40da94742e03` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 164 | 2024-12-02 | `sha256:59038e257e00` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 28 | 2024-12-02 | `sha256:5bd134f356fc` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 782 | 2024-12-02 | `sha256:afb5052f70db` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 849 | 2024-12-02 | `sha256:e542eb431775` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 849 | 2024-12-02 | `sha256:e542eb431775` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 849 | 2024-12-02 | `sha256:e542eb431775` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 33 | 2024-12-02 | `sha256:47324f787d89` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 163 | 2024-12-02 | `sha256:67a4d02f6a35` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 31 | 2024-12-02 | `sha256:52e0e447a6b3` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.241127 | 6 | 2024-12-02 | `sha256:07061180b990` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 30 | 2024-12-02 | `sha256:c4d884bc4d04` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 155 | 2024-12-02 | `sha256:2e2bad757f7a` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 197 | 2024-12-03 | `sha256:407a113e85a0` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2201 | 2024-12-03 | `sha256:95a76c94b8b5` |
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
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:472466abfe56fc47e5201c6f94d8736ff3f2dd85607b9e37648d80e8b508640f
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:307f3f5126fd9b3a83bf174a8087f900ef32938d63f4d56a28978eb965c1eef7
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:59038e257e00fe94d84fe18d86c23aa6145351382703eae89cd76ed5c6dcf35b
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:40da94742e031ea77b139c890204800c7a63db20eb0a78e48b9f6fee091530d3
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:5bd134f356fcd4d1a2fe08d508c9273964bfd8d164c3585b6b711a6bf1f0314e
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:afb5052f70db6a2d9e391f46f242986968c8a0f95cebfde1e7a1d530c75f9825
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:e542eb4317758233c60868f61355ca59766f28d7450567248ee58f8e59771a5c
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:67a4d02f6a3545bfe87fc8daad0d58a39ea115464a5f1ce712205ff31f6e25dd
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:47324f787d89806cf6c62e419b4a68f2d00ff91451e4d548cf674840cbad92a9
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:52e0e447a6b30e5439fe296a369838beb3d3aaf7a16ec8a32ffea35db7555a7a
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:c4d884bc4d04590d78a54b6c4b8cee9e7ec836ce3fd7b400217492b1037cf790
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:07061180b990ba4dec50d6d9472259b7a11adcf394a77e14b0c75b913f817e5d
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:2e2bad757f7a2efc2b16c1563898520dd2b2f759ddd2d02c471ba1045617606c
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:407a113e85a0b7d2114fa44c6bb532a759982a24015133bb05da3be72069eb97
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:95a76c94b8b5c68b23cfaee042797d0b21c92fb4bc06c00f794ec5e8dcd64c14
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:1172e150fff22c5eeab572f26961f3f53fbf896ee76d08c7503cfe2777c55458
registry.redhat.io/rhel8/postgresql-13@sha256:c100244306278d142d9de26c5387e0d030dd4e68d16d4eec1aa428a97b2de04e
registry.redhat.io/rhel8/redis-6@sha256:bb24ede28ec4cd2e416f6e299ee16531d8bc0a7496d3e44ac7619d9b09366737
registry.redhat.io/ubi8/ubi-minimal@sha256:c12e67af6a7e15113d76bc72f10bef2045c026c71ec8b7124c8a075458188a83
```

</details>
