# `aap-operator.v2.4.0-0.1720482179`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1720482179` |
| **Build date** | 2024-07-08 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1718152210`](./aap-operator.v2.4.0-0.1718152210.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:3579691684ab09996364494a4619494d28a5bcf51718f12b39f2579c874a6651` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.8 | 12 | 2024-07-08 | `sha256:721b1b59b07e` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 144 | 2024-07-08 | `sha256:804d5403f580` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 12 | 2024-07-08 | `sha256:6e10dbd52c5a` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 145 | 2024-07-08 | `sha256:944a7adb24e5` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 10 | 2024-07-08 | `sha256:c81e778c6aa4` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 683 | 2024-07-08 | `sha256:59db2e8f095f` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 721 | 2024-07-08 | `sha256:da419ec83f1e` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 721 | 2024-07-08 | `sha256:da419ec83f1e` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 721 | 2024-07-08 | `sha256:da419ec83f1e` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 15 | 2024-07-08 | `sha256:39d33714040d` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 139 | 2024-07-08 | `sha256:d5639859108d` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 14 | 2024-07-08 | `sha256:888f8fb6ebc9` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.1 | 3 | 2024-07-08 | `sha256:aa1122508420` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 9 | 2024-07-08 | `sha256:e5a267c1df76` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 132 | 2024-07-08 | `sha256:f5174d2e02b0` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 166 | 2024-07-08 | `sha256:8161216923f4` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1739 | 2024-07-08 | `sha256:3579691684ab` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202406190905.p0.gb17014f.assembly.stream.el8 | 2024-06-19 | `sha256:55a49d79b9d2` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 190 | 2024-06-27 | `sha256:726bc80093a7` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 190 | 2024-06-27 | `sha256:726bc80093a7` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 190 | 2024-06-27 | `sha256:726bc80093a7` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1018 | 2024-06-27 | `sha256:de2a0a20c1c3` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1018 | 2024-06-27 | `sha256:de2a0a20c1c3` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1018 | 2024-06-27 | `sha256:de2a0a20c1c3` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.8 | 12 | 2024-07-08 | `sha256:721b1b59b07e` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 144 | 2024-07-08 | `sha256:804d5403f580` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 12 | 2024-07-08 | `sha256:6e10dbd52c5a` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 145 | 2024-07-08 | `sha256:944a7adb24e5` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 10 | 2024-07-08 | `sha256:c81e778c6aa4` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 683 | 2024-07-08 | `sha256:59db2e8f095f` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 721 | 2024-07-08 | `sha256:da419ec83f1e` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 721 | 2024-07-08 | `sha256:da419ec83f1e` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 721 | 2024-07-08 | `sha256:da419ec83f1e` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 15 | 2024-07-08 | `sha256:39d33714040d` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 139 | 2024-07-08 | `sha256:d5639859108d` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 14 | 2024-07-08 | `sha256:888f8fb6ebc9` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 1.0.1 | 3 | 2024-07-08 | `sha256:aa1122508420` |
| ansible-lightspeed-operator-controller-manager/ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 9 | 2024-07-08 | `sha256:e5a267c1df76` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 132 | 2024-07-08 | `sha256:f5174d2e02b0` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 166 | 2024-07-08 | `sha256:8161216923f4` |
| ansible-lightspeed-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202406190905.p0.gb17014f.assembly.stream.el8 | 2024-06-19 | `sha256:55a49d79b9d2` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202406190905.p0.gb17014f.assembly.stream.el8 | 2024-06-19 | `sha256:55a49d79b9d2` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202406190905.p0.gb17014f.assembly.stream.el8 | 2024-06-19 | `sha256:55a49d79b9d2` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202406190905.p0.gb17014f.assembly.stream.el8 | 2024-06-19 | `sha256:55a49d79b9d2` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202406190905.p0.gb17014f.assembly.stream.el8 | 2024-06-19 | `sha256:55a49d79b9d2` |
| RELATED_IMAGE_ANSIBLE_AI_CONNECT_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 189 | 2024-06-27 | `sha256:42eed05d0f68` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 190 | 2024-06-27 | `sha256:726bc80093a7` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 190 | 2024-06-27 | `sha256:726bc80093a7` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 190 | 2024-06-27 | `sha256:726bc80093a7` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1018 | 2024-06-27 | `sha256:de2a0a20c1c3` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1018 | 2024-06-27 | `sha256:de2a0a20c1c3` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1018 | 2024-06-27 | `sha256:de2a0a20c1c3` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:804d5403f58059ea858f255ede455b2f95e0b31144cdce512abb47d1db2e5aa5
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:721b1b59b07ec084ae4ff35f628f7875ed2e4d06e5c8ec492df95fdd0aff8bdc
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:944a7adb24e564009fa96d6e78b5892d2dad551e2ce65320fe07fa636e46aca6
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:6e10dbd52c5acce0f3f8eb6a44bae7725b9b4d1011704c1f6cfa7d412b9e105c
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:c81e778c6aa42509cb94d4f89b8ef31ac2f95c54666c38b120fc0a02ee6ea585
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:59db2e8f095f7fd7bacf0c365c402877cd2ba5b78dd24ec2b6e194ec1c282a8c
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:da419ec83f1eb834735ca9ceebc189a96067414b05ab5a86b067ab76f7adc249
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:d5639859108da69f337990146c02931387deece6ec2c752aa56e2f49822ece49
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:39d33714040d3469dc6cd8c1c62adde8cf4fe8539aec72f8fdd3a25663e2d06d
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:888f8fb6ebc99bebb060cb2993a744e77c3108b3ebfdb07b9fdbad74a9628811
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:e5a267c1df76a26f6602efc101bcb6d67922dfc5dd6b0a4d4bfaa9aadfcbcdec
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:aa11225084203f0d0184b2052a3993420dce91c9e1e374869623ca94ca8727cd
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:f5174d2e02b0fde8c77b935f7557ad031f1726a629be5b3d1820f302504c81af
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:8161216923f483493dbb42cce08ff8b490111c965c8c2c5e0e3f6b915f9f46ad
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:3579691684ab09996364494a4619494d28a5bcf51718f12b39f2579c874a6651
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:55a49d79b9d29757328762e8a4755013fba1ead5a2416cc737e8b06dd2a77eef
registry.redhat.io/rhel8/postgresql-13@sha256:42eed05d0f681deb8d9198bf483bbeda02016c23515f061b828aec71f0ae142f
registry.redhat.io/rhel8/redis-6@sha256:726bc80093a756d382024ac3e214b5dc3ed3dc2ee638f96e0fdead6b8fe2f612
registry.redhat.io/ubi8/ubi-minimal@sha256:de2a0a20c1c3b39c3de829196de9694d09f97cd18fda1004de855ed2b4c841ba
```

</details>
