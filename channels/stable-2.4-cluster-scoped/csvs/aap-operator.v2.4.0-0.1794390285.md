# `aap-operator.v2.4.0-0.1794390285`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1794390285` |
| **Build date** | 2026-11-11 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1793887686`](./aap-operator.v2.4.0-0.1793887686.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:80e5e29c1b3c1345c3e17e009a371e4668790d942a022b9c38a97a2f263b1d3e` |
| **Seen in OCP operator indexes** | 4.12, 4.14, 4.16, 4.18–4.20 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.39 | 1794244899 | 2026-11-11 | `sha256:49070f74d987` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator` | 2.4 | 202611030126.p2.gbc7aeec.assembly.stream.el9 | 2026-11-07 | `sha256:87e444927e20` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1794244899 | 2026-11-10 | `sha256:6be3393493e8` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator` | 2.4 | 202611030126.p2.gbc7aeec.assembly.stream.el9 | 2026-11-07 | `sha256:d73bc9ec2fdb` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1794313724 | 2026-11-11 | `sha256:06a85f94e42d` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1794244899 | 2026-11-11 | `sha256:42f51cc1da1f` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1794244899 | 2026-11-10 | `sha256:b5c2d69b9ed9` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1794244899 | 2026-11-10 | `sha256:b5c2d69b9ed9` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1794244899 | 2026-11-10 | `sha256:b5c2d69b9ed9` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1794244899 | 2026-11-10 | `sha256:0f9810a863eb` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator` | 2.4 | 202611030126.p2.gbc7aeec.assembly.stream.el9 | 2026-11-07 | `sha256:5b3f35805932` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1794313724 | 2026-11-11 | `sha256:e0463a03b1e8` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1794244899 | 2026-11-11 | `sha256:af07d80e4b29` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator` | 2.4 | 202611030126.p2.gbc7aeec.assembly.stream.el9 | 2026-11-07 | `sha256:d9ed90020dd2` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator` | 2.4 | 202611030126.p2.gbc7aeec.assembly.stream.el9 | 2026-11-10 | `sha256:ebf96190a092` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1794244899 | 2026-11-10 | `sha256:af2b87187f8e` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-11-11 | `sha256:80e5e29c1b3c` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9` | v4.18.0 | 202610271721.p2.gf72b2ec.assembly.stream.el9 | 2026-10-27 | `sha256:dcf51417d04e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1794315639 | 2026-11-10 | `sha256:4d373d63ba46` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1794315639 | 2026-11-10 | `sha256:4d373d63ba46` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1794315639 | 2026-11-10 | `sha256:4d373d63ba46` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1794315639 | 2026-11-10 | `sha256:4d373d63ba46` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1794314485 | 2026-11-10 | `sha256:671381c8a2a7` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1794314485 | 2026-11-10 | `sha256:671381c8a2a7` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1794314485 | 2026-11-10 | `sha256:671381c8a2a7` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1794244899 | 2026-11-09 | `sha256:95689582e591` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1794244899 | 2026-11-09 | `sha256:95689582e591` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1794244899 | 2026-11-09 | `sha256:95689582e591` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:49070f74d98752cb2a418d8b0720dbdcf11a65a3939e5d26664d146584715a0c
registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator@sha256:87e444927e20479760105951e4a59642916c3b22ba95dca9686f501e4db4858c
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:6be3393493e8cf7f250396ec267eb5893c8f8a9a4e349166adb9e372d4a74873
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator@sha256:d73bc9ec2fdbfc3221cff08260c83814d1df38d66363bf84f4faafafba7fc5d8
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:06a85f94e42da8213f8b1d37ffd824d5f72d6792cb791dd6ac9d021a8106a15f
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:42f51cc1da1f3e5b1413823d6b76a9f0c5297a36ff15ee84bfbf6b41f46307a5
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:b5c2d69b9ed9a8d712867f52bcce47bd6e77de8556d9066cfea9326a39698a06
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:0f9810a863ebdc63d6f7228b67681e6055d3de39c99de61efc6fc6b8c9cc7399
registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator@sha256:5b3f35805932de61c859305d8e36d62d9158ae173e4cd8940b98dc3395f864fd
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:e0463a03b1e8533d567be90a9707e471809441993f713f90935ae5aa7f265b98
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:af07d80e4b2973eb18fecb0aed8d4f287a755c580eedbe2d34592588020d6fb5
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator@sha256:d9ed90020dd227076c68fb8a47206fc9a8ab13f7803d74d153335d956fe5ac79
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator@sha256:ebf96190a092b7ca8979fd6aa00e73bcbccf5e58f4ae8b35d27180b574d5c437
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:af2b87187f8efb011f666a3b5789dfa8e8c927bb47e7c3a93ecb8fb3652bcf43
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:80e5e29c1b3c1345c3e17e009a371e4668790d942a022b9c38a97a2f263b1d3e
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9@sha256:dcf51417d04e0f0f1d0efe25d12f764ddea07f0401bd6fd668a9547dcc92ec9a
registry.redhat.io/rhel8/postgresql-15@sha256:4d373d63ba46d73718834171fafcb5c101ffc53fa999352dfd60da447f085112
registry.redhat.io/rhel8/redis-6@sha256:671381c8a2a70353f787e8c2d8c04d48350a2f5a7ad59981216b33225b6daff0
registry.redhat.io/ubi8/ubi-minimal@sha256:95689582e591ea3490d7d4da6f240e1b5138dacc5883cc87057750b7eaabafc2
```

</details>
