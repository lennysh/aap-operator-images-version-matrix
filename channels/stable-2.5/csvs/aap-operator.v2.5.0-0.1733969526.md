# `aap-operator.v2.5.0-0.1733969526`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1733969526` |
| **Build date** | 2024-12-12 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1733193164`](./aap-operator.v2.5.0-0.1733193164.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:fd6e49e702910c6c7679fe8a8268239b67a96ab42d1060f9ba7fcb48be5ccbc6` |
| **Seen in OCP operator indexes** | 4.12–4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.3 | 22 | 2024-12-11 | `sha256:03f678b662e1` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 142 | 2024-12-11 | `sha256:313f0646b0c7` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.3 | 9 | 2024-12-11 | `sha256:98542db2f8cb` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 141 | 2024-12-11 | `sha256:f890a5e3d0ab` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.3 | 2 | 2024-12-12 | `sha256:a8b44b15ed2d` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 791 | 2024-12-12 | `sha256:f617059349de` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 862 | 2024-12-12 | `sha256:8cf2954de314` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 862 | 2024-12-12 | `sha256:8cf2954de314` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 862 | 2024-12-12 | `sha256:8cf2954de314` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 35 | 2024-12-11 | `sha256:262e552fa4cc` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20241218 | 3 | 2024-12-11 | `sha256:b1a7ea2fa394` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 172 | 2024-12-11 | `sha256:f5424a9cf1cd` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 17 | 2024-12-11 | `sha256:a26a8e59c898` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 144 | 2024-12-11 | `sha256:dc7a5f859795` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 14 | 2024-12-12 | `sha256:b89bce24d05f` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.241210 | 2 | 2024-12-11 | `sha256:950486d307e0` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 102 | 2024-12-11 | `sha256:b85e783544c6` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 96 | 2024-12-11 | `sha256:d92986febcf7` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 126 | 2024-12-12 | `sha256:5e282317eb81` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 990 | 2024-12-12 | `sha256:fd6e49e70291` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202412041605.p0.g9308e7f.assembly.stream.el8 | 2024-12-04 | `sha256:4a2324acaea7` |
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
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:313f0646b0c769dd1a5837aa93a341ca4a3abc9e73c9d95070d058430da856ba
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:03f678b662e11817b690721dc311754d8034157681da3e6d168b8f627d277cb9
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:f890a5e3d0abbb8772be1fe97796e3eee95519a45d6b165c548baf0f27a625d6
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:98542db2f8cbd77ed801c301b1df4e0ef3d7214f2db8adc0fea98999690ef3b5
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:a8b44b15ed2d0c8aae123d600d31a75c7930cf741646f72bca47e42583242772
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:f617059349de0bff8c0894f5f6c4b9d17145c0cec3e0b2c8d88ab182a13da24e
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:8cf2954de314a8deadef601bda3de1c77f7dd12699103af3120364d5391f0c86
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:262e552fa4ccd339d3fb0e33bc057de85efd9c93f26f90ca4ca701e774482845
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:f5424a9cf1cd01d62538ee1c03f45b18ca55f61ce7a486b7a55f8bdbcfa58f27
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:b1a7ea2fa394c49bc0c7982bd854549c101b48c9c13c74878a2014e4b3ed0078
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:dc7a5f85979509c12595340a3c16ed34d926a39733be76f9af9092604acff793
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:a26a8e59c89840d41f8d67a43ab13ceb16e7bcf7a295af98d9dcb392d2d9dbcd
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:b89bce24d05ff2e6f299b39f1c8ce57eb9066624a1ecdc81251ce1178d7a669e
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:b85e783544c65e04c7041d06cb43c5e5e2c2555537ca1fa4a2f7602710ad3c8e
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:950486d307e0b24deacc04272f73e5009a81776bbfac0d0457e62bbc71c2868e
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:d92986febcf715e7e425029c96364eef2208faa37aed8cef0305b3e18e85de86
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:5e282317eb810ed7d9f6f5bc5d74c636d27d87b94cf6c82614029a86d02be231
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:fd6e49e702910c6c7679fe8a8268239b67a96ab42d1060f9ba7fcb48be5ccbc6
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:4a2324acaea757bae3b01b1aec59f49f4dd79bd1868e69d3418d57c210a6dfd9
registry.redhat.io/rhel8/postgresql-15@sha256:9cf99b00411991ec14e99df0e37c37b54472e9b323aa542c6acd9b112121be95
registry.redhat.io/rhel8/redis-6@sha256:bb24ede28ec4cd2e416f6e299ee16531d8bc0a7496d3e44ac7619d9b09366737
registry.redhat.io/ubi8/ubi-minimal@sha256:c12e67af6a7e15113d76bc72f10bef2045c026c71ec8b7124c8a075458188a83
```

</details>
