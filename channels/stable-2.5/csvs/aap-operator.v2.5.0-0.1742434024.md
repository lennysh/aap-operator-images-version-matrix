# `aap-operator.v2.5.0-0.1742434024`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1742434024` |
| **Build date** | 2025-03-20 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1741368605`](./aap-operator.v2.5.0-0.1741368605.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:7c2d7085884998a6022195bb451f397bb91db2a667da793d56cebbc09c59a39f` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.10 | 8 | 2025-03-19 | `sha256:00bea25f312f` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 168 | 2025-03-19 | `sha256:a27cbbc56c26` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.6 | 7 | 2025-03-19 | `sha256:ee97c6ee1dd2` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 170 | 2025-03-19 | `sha256:35381df869dc` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.6 | 4 | 2025-03-19 | `sha256:7d38dd0cf8b7` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 850 | 2025-03-19 | `sha256:63f6a674c507` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 945 | 2025-03-19 | `sha256:cf8ca1db5773` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 945 | 2025-03-19 | `sha256:cf8ca1db5773` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 945 | 2025-03-19 | `sha256:cf8ca1db5773` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 57 | 2025-03-19 | `sha256:f03abbb9ad1f` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250326 | 2 | 2025-03-19 | `sha256:d0eb3ec1db8f` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 217 | 2025-03-19 | `sha256:9d86adeb1b11` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.3 | 2 | 2025-03-19 | `sha256:a8a82e9d5536` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 170 | 2025-03-19 | `sha256:a672a7f849e3` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.3 | 2 | 2025-03-19 | `sha256:e690a4955309` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250318 | 2 | 2025-03-19 | `sha256:c1121777609a` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 127 | 2025-03-19 | `sha256:7767bb4bfb8c` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 123 | 2025-03-19 | `sha256:e3ac5d5eea04` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 154 | 2025-03-20 | `sha256:fe0f99501420` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1215 | 2025-03-20 | `sha256:7c2d70858849` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202502191335.p0.g9308e7f.assembly.stream.el8 | 2025-02-19 | `sha256:f831737dc97e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91 | 2025-03-05 | `sha256:96e94b4a11a5` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91 | 2025-03-05 | `sha256:96e94b4a11a5` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91 | 2025-03-05 | `sha256:96e94b4a11a5` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91 | 2025-03-05 | `sha256:96e94b4a11a5` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 91 | 2025-03-05 | `sha256:96e94b4a11a5` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213 | 2025-03-05 | `sha256:109574014c15` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213 | 2025-03-05 | `sha256:109574014c15` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213 | 2025-03-05 | `sha256:109574014c15` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 213 | 2025-03-05 | `sha256:109574014c15` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741795396 | 2025-03-12 | `sha256:e4ca1025efad` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741795396 | 2025-03-12 | `sha256:e4ca1025efad` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1741795396 | 2025-03-12 | `sha256:e4ca1025efad` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:a27cbbc56c263d6a75337af9e26b96c55c47bc42961bcb1b0bdaa3ae9f4d22c1
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:00bea25f312f11e1fdf84d73c41a8fc1f38e20074ae285c5df0d2cf68a6494fb
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:35381df869dc3dab294f0acbf1f62f35d5b4339bb8e9163ca0026d5c14205ed7
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:ee97c6ee1dd2412e31ef6dd734bc7a11aa87826c8e7934305800d16d0b43b655
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:7d38dd0cf8b79cd69f19866e988241467a2b4ca1b24d3eeefb59f74065c68ed5
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:63f6a674c507ce78e78de8fdecc4d950d0987d4cecd796bc61b3ca732d30413f
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:cf8ca1db577399b78778e222439d6d14bbebd5dd0e475a976c1db8dcabacbe94
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:f03abbb9ad1faa22ee4244f163f63dfeb3ea6421432e999377c5a64db1eb6b90
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:9d86adeb1b11f5baaef4cb12efe9552ed53d7acceb919177711c8bb67d7a4a44
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:d0eb3ec1db8fb3406d96e9d7e7327d66abcd85a0284bbcd74c96cdafd30200ed
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:a672a7f849e3cf9504a92889281246da204bd8b42387cffe2c910a1d20380f06
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:a8a82e9d553692576fa27e34a1dcb6b849ec4b54ea85ccb54274c0485076b11c
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:e690a4955309ce5c0ed102b3b2c58646a87bbf87f97e82a19a2003e7c00dbec1
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:7767bb4bfb8c32408500b26244af53be54c32d6be571782b723a94ee7076d707
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:c1121777609a6a42b848a021054198c8f56ad25b053e948ef31617413d574800
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:e3ac5d5eea0440656de2d2fa6461b6a87d384e552083c84a1ae1a8fdd530465d
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:fe0f9950142097a3d84af2486e319be890e958e9c4a049d45255523aa1db8831
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:7c2d7085884998a6022195bb451f397bb91db2a667da793d56cebbc09c59a39f
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:f831737dc97ecc6abd59b32ef06014586580bd8725419fef48dbdd1871e1a2cf
registry.redhat.io/rhel8/postgresql-15@sha256:96e94b4a11a5ffa86c359a870d2492c3b2e28153ce09f00a5b0f7957a0bbd983
registry.redhat.io/rhel8/redis-6@sha256:109574014c1553a00839c6dc727232f34025b0aa918cc0c8f1639a4a04d9f6f0
registry.redhat.io/ubi8/ubi-minimal@sha256:e4ca1025efad7cc944fb991c716067b12e25ecbe05e6e81715a337179e417aa8
```

</details>
