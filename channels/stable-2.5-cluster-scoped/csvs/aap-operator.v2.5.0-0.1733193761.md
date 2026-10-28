# `aap-operator.v2.5.0-0.1733193761`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1733193761` |
| **Build date** | 2024-12-03 |
| **Replaces** | [`aap-operator.v2.5.0-0.1731456854`](./aap-operator.v2.5.0-0.1731456854.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:9ed1844bcea93249862024df740bb1ba9adb35289ac76a58173fd385735bfe26` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.3 | 13 | 2024-12-02 | `sha256:430423770062` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 139 | 2024-12-03 | `sha256:2ec620dd8fcf` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.2 | 9 | 2024-12-02 | `sha256:8e9804fecc32` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 138 | 2024-12-02 | `sha256:b0e4fee664a6` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.2 | 6 | 2024-12-03 | `sha256:17415d133b6d` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 784 | 2024-12-03 | `sha256:f87e344b9b64` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 851 | 2024-12-03 | `sha256:42e4e5b0dcf5` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 851 | 2024-12-03 | `sha256:42e4e5b0dcf5` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 851 | 2024-12-03 | `sha256:42e4e5b0dcf5` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 32 | 2024-12-02 | `sha256:aac347d223a0` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.3 | 8 | 2024-12-02 | `sha256:176390f2c67e` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 168 | 2024-12-03 | `sha256:c91adad624b6` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 9 | 2024-12-02 | `sha256:f9c5f6706679` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 139 | 2024-12-03 | `sha256:ce1793df5bf7` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 7 | 2024-12-03 | `sha256:c9d80d4c3749` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.241127 | 3 | 2024-12-02 | `sha256:a44589b823ac` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 99 | 2024-12-02 | `sha256:9575baf8b565` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 93 | 2024-12-02 | `sha256:58c325293065` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 124 | 2024-12-03 | `sha256:4c8c5da8f336` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 973 | 2024-12-03 | `sha256:9ed1844bcea9` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202411130135.p0.g9308e7f.assembly.stream.el8 | 2024-11-13 | `sha256:1172e150fff2` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87.1732637101 | 2024-11-26 | `sha256:9cf99b004119` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87.1732637101 | 2024-11-26 | `sha256:9cf99b004119` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87.1732637101 | 2024-11-26 | `sha256:9cf99b004119` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87.1732637101 | 2024-11-26 | `sha256:9cf99b004119` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 87.1732637101 | 2024-11-26 | `sha256:9cf99b004119` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209.1732637107 | 2024-11-26 | `sha256:bb24ede28ec4` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209.1732637107 | 2024-11-26 | `sha256:bb24ede28ec4` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209.1732637107 | 2024-11-26 | `sha256:bb24ede28ec4` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 209.1732637107 | 2024-11-26 | `sha256:bb24ede28ec4` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1130 | 2024-10-30 | `sha256:c12e67af6a7e` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:2ec620dd8fcf059872e456bcfd1a3e815b785199190fa6e07f633d7e76d6a684
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:430423770062cb58716925d2485e4c99260ccadef37c9c3b89075b7b58dba0f0
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:b0e4fee664a68070c8f95eeb0aefe10d90145c08eea2dea88a1f90a5c89d3acc
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:8e9804fecc323f864a4c601bc077a5aa0e794c0d449777e243b784f077d0abbb
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:17415d133b6d875f2ceefefc0b93abf8004a64d252c3596bcf5403bf392775de
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:f87e344b9b64c35e28102c37c5ccce9c34696796232e3965705a680ad96ac30b
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:42e4e5b0dcf57154e24a2f0444edc5a31125dc3f9607683236a8c0a1ade2fcdf
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:aac347d223a06117b866cfaefeb759069c805699158dec51599b5dc8d8afaa20
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:c91adad624b61e34ad5ce66a19b605ce9be5257e72a17577f66ad4e639c8743f
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:176390f2c67e28567f1e64ffaecb58014fd984e0fa6797db38827ce4578305d3
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:ce1793df5bf757c5cfe61b3a3a33e29573f1cfc1311b4e162bf74c05e6ecfc1a
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:f9c5f6706679cd4e7f9088688f3d236ebb6149a208a40e001ac8a2618f6b299e
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:c9d80d4c37492b9d177699b2c0291c02d42f3a08e1aefcd1d33b768842b9b2ba
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:9575baf8b5650f646abf15a5ae8ccdcb9b46645810f19561c3de80593b612e17
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:a44589b823ace7efe1d68385fec5224f890abcc253c48c47c07d2753ab5997c4
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:58c325293065588b35e74df8817370a55533a1746d811e058a6977ecadfa47e6
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:4c8c5da8f33674d428c1a56842546c0bc1f48a8c6b34e1ef5f9f695b05bd30f7
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:9ed1844bcea93249862024df740bb1ba9adb35289ac76a58173fd385735bfe26
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:1172e150fff22c5eeab572f26961f3f53fbf896ee76d08c7503cfe2777c55458
registry.redhat.io/rhel8/postgresql-15@sha256:9cf99b00411991ec14e99df0e37c37b54472e9b323aa542c6acd9b112121be95
registry.redhat.io/rhel8/redis-6@sha256:bb24ede28ec4cd2e416f6e299ee16531d8bc0a7496d3e44ac7619d9b09366737
registry.redhat.io/ubi8/ubi-minimal@sha256:c12e67af6a7e15113d76bc72f10bef2045c026c71ec8b7124c8a075458188a83
```

</details>
