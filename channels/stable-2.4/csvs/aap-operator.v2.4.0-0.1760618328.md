# `aap-operator.v2.4.0-0.1760618328`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1760618328` |
| **Build date** | 2025-10-16 |
| **Replaces** | [`aap-operator.v2.4.0-0.1758079821`](./aap-operator.v2.4.0-0.1758079821.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:ea425cd62f21298dc5a7d8df0e01e6c13e4d6eb7b55a320ae5ce70bfa64c754d` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.26 | 3 | 2025-10-15 | `sha256:0067b18d6399` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 184 | 2025-10-16 | `sha256:4378b9c5bf85` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 46 | 2025-10-15 | `sha256:1b22fa91fb29` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 183 | 2025-10-15 | `sha256:829073e2beb0` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 44 | 2025-10-15 | `sha256:e0de04115d0d` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 981 | 2025-10-15 | `sha256:10f8225b9a1d` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1106 | 2025-10-15 | `sha256:ab407167737d` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1106 | 2025-10-15 | `sha256:ab407167737d` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1106 | 2025-10-15 | `sha256:ab407167737d` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.5 | 5 | 2025-10-15 | `sha256:22ddf98c0671` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 183 | 2025-10-15 | `sha256:ef4ff94fff5f` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 4 | 2025-10-15 | `sha256:2747c5091b01` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 20 | 2025-10-15 | `sha256:9be10feac089` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 52 | 2025-10-15 | `sha256:24c8a88da19b` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 179 | 2025-10-15 | `sha256:1fb34d566ed2` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 218 | 2025-10-16 | `sha256:fab54808ac13` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2852 | 2025-10-16 | `sha256:ea425cd62f21` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202509151014.p2.g9308e7f.assembly.stream.el8 | 2025-09-16 | `sha256:fa0acefda43e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1760372156 | 2025-10-13 | `sha256:64bca18004dc` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1760371733 | 2025-10-13 | `sha256:705d7e2f23ae` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1760371733 | 2025-10-13 | `sha256:705d7e2f23ae` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1760371733 | 2025-10-13 | `sha256:705d7e2f23ae` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1759911539 | 2025-10-08 | `sha256:58b1dc5427b6` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1759911539 | 2025-10-08 | `sha256:58b1dc5427b6` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1759911539 | 2025-10-08 | `sha256:58b1dc5427b6` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:4378b9c5bf85b7b06798ebd934bc6ccd5c390b10f43f20a54ced9720b73cc9e1
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:0067b18d6399bd5bc63b50200b4bfa3e073ca632103c572d99d05d934fa0f66f
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:829073e2beb0935004fb4844134ae5806894ac105e7d5a53deb3993ca435e60b
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:1b22fa91fb294bc64354b0799e6d243334664a5b705029814aba07e8e78165f9
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:e0de04115d0d03e99bc147bf2e0a58fcfebdbaaef53f7735a92687bac5287812
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:10f8225b9a1dc6d49ec34ccff6f509daffbef5123525964f2b10d5fc8b0e8690
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:ab407167737d394debc04b136ec176a9ea3050ecfeda6b34dea940ee8bb5f8c6
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:ef4ff94fff5f6de09c2d3eaa499fbd373010643891088d5a1ace3f5856aa95c7
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:22ddf98c06710a01039c5ccd36ea2e51023fef66fdd876ae4c485ae429a295e5
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:2747c5091b0153834cd7850372e8554e86c4a0036abf0c690cdd78e3425876eb
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:24c8a88da19bf3cf173b9c7cad4911f2625f182146e8f0e6113db7ee3817989e
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:9be10feac089cb428961a876b29620f0737f32aace42f8dbdcdbf8f2a723771b
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:1fb34d566ed2e6fe1ac6791300b65f5265eaa746c854a807a9e647b5fb8645ac
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:fab54808ac13d05cafbb8cedf2c393d65fc4ebf5e92012a3d973a856a0b039ce
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:ea425cd62f21298dc5a7d8df0e01e6c13e4d6eb7b55a320ae5ce70bfa64c754d
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:fa0acefda43e309e7f9f31f5247c933d0b868ff1573ece2f38e0549d7e2ec942
registry.redhat.io/rhel8/postgresql-15@sha256:64bca18004dc5b79eb21cce15996c8cb0a606405bc7797f7ddc69c87a6cc149b
registry.redhat.io/rhel8/redis-6@sha256:705d7e2f23ae3dcd8d96d083bf7d98b46250c2bc44c13a68fad752568bff9ad2
registry.redhat.io/ubi8/ubi-minimal@sha256:58b1dc5427b699255a73475f5e96e9f658f49214e5bd56d03c534fa87980efb1
```

</details>
