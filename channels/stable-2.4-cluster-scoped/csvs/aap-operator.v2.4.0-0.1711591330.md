# `aap-operator.v2.4.0-0.1711591330`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1711591330` |
| **Build date** | 2024-03-28 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1708975279`](./aap-operator.v2.4.0-0.1708975279.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:f73dd744466f574605d0e6375e1e76dd4030b8669881dcdc117aa0b612d3cb1c` |
| **Seen in OCP operator indexes** | 4.12–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.5 | 5 | 2024-03-28 | `sha256:8fb4cba713e7` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 125 | 2024-03-28 | `sha256:fd74a7a5679e` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 8 | 2024-03-28 | `sha256:e624c233d494` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 131 | 2024-03-28 | `sha256:d17b0661b100` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 8 | 2024-03-28 | `sha256:9fe37efb8fba` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 588 | 2024-03-28 | `sha256:144bae8b257a` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 607 | 2024-03-28 | `sha256:ea7817faed9d` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 607 | 2024-03-28 | `sha256:ea7817faed9d` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 607 | 2024-03-28 | `sha256:ea7817faed9d` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 8 | 2024-03-28 | `sha256:a37bc160c3f9` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 119 | 2024-03-28 | `sha256:6ff95d95c5f8` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 7 | 2024-03-28 | `sha256:689f688eb236` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 112 | 2024-03-28 | `sha256:8efcf95ba1e3` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 138 | 2024-03-28 | `sha256:f6b2076bbb5c` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1324 | 2024-03-28 | `sha256:f73dd744466f` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403060808.p0.gb17014f.assembly.stream.el8 | 2024-03-06 | `sha256:07844eb40d60` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169.1708918658 | 2024-02-26 | `sha256:d8e7066ddd94` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169.1708918658 | 2024-02-26 | `sha256:d8e7066ddd94` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169.1708918658 | 2024-02-26 | `sha256:d8e7066ddd94` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.5 | 5 | 2024-03-28 | `sha256:8fb4cba713e7` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 125 | 2024-03-28 | `sha256:fd74a7a5679e` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.5 | 8 | 2024-03-28 | `sha256:e624c233d494` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 131 | 2024-03-28 | `sha256:d17b0661b100` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.5 | 8 | 2024-03-28 | `sha256:9fe37efb8fba` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 588 | 2024-03-28 | `sha256:144bae8b257a` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 607 | 2024-03-28 | `sha256:ea7817faed9d` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 607 | 2024-03-28 | `sha256:ea7817faed9d` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 607 | 2024-03-28 | `sha256:ea7817faed9d` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.1 | 8 | 2024-03-28 | `sha256:a37bc160c3f9` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 119 | 2024-03-28 | `sha256:6ff95d95c5f8` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.1 | 7 | 2024-03-28 | `sha256:689f688eb236` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 112 | 2024-03-28 | `sha256:8efcf95ba1e3` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 138 | 2024-03-28 | `sha256:f6b2076bbb5c` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403060808.p0.gb17014f.assembly.stream.el8 | 2024-03-06 | `sha256:07844eb40d60` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403060808.p0.gb17014f.assembly.stream.el8 | 2024-03-06 | `sha256:07844eb40d60` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403060808.p0.gb17014f.assembly.stream.el8 | 2024-03-06 | `sha256:07844eb40d60` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.12.0 | 202403060808.p0.gb17014f.assembly.stream.el8 | 2024-03-06 | `sha256:07844eb40d60` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169.1708918658 | 2024-02-26 | `sha256:d8e7066ddd94` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169.1708918658 | 2024-02-26 | `sha256:d8e7066ddd94` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 169.1708918658 | 2024-02-26 | `sha256:d8e7066ddd94` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 170 | 2024-02-13 | `sha256:29eba91f2fee` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1137 | 2024-02-13 | `sha256:8bedbe742f14` |

## Image pull specs

<details><summary>All 17 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:fd74a7a5679ebb0ba9e0cc50b7d79bf1273e01c558a53a1e7a40e50ae064e9a4
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:8fb4cba713e79b93d5a3b689c4919648bbcabd70337568a647fd228131de61df
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:d17b0661b100bd37493c14cb8c0cf946f0361044fac7207392d6075eeef7b30c
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:e624c233d494dfd527bf7dcb620dedf0dcb68272f41f2549860e97fbdde00a8c
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:9fe37efb8fba894b5d2fcdffb0d47ca68c2ff5343034c36d3342b06c53c20ad5
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:144bae8b257ac728ee5624f810d2bedf4ffef1bf03d7da2f8c5d5a330c077b93
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:ea7817faed9db62ad1ce2adfb20d27e8ed9003f35f3a5fa92a9b8273d2f6a3c2
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:6ff95d95c5f82333bba91be71bc70970548e3f488893552592dc128de0a398f3
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:a37bc160c3f9de0aacefe900c2dd55f182b5d9d1897333c3fc37451377a5fc73
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:689f688eb23672b2c2179daff4ae98f51ad4293bc96e3088a487fc77c88e8633
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:8efcf95ba1e32487efa921a07a9d702c8f10c367988ad8b03dfbd9276c44c0cd
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:f6b2076bbb5c40cddeb814c5a20b53add88273f6991e03cde42999aadb2defe1
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:f73dd744466f574605d0e6375e1e76dd4030b8669881dcdc117aa0b612d3cb1c
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:07844eb40d6091406e0788e41f64727ccacbe9d1c70088a6fb739d879c11dc13
registry.redhat.io/rhel8/postgresql-13@sha256:d8e7066ddd94c201af756edf99cefccab83ac0d104a824c5de5aadb8fa64270d
registry.redhat.io/rhel8/redis-6@sha256:29eba91f2feeb5d5efe146806c83894f53814c06c74d0d6c2806c928aef40d8a
registry.redhat.io/ubi8/ubi-minimal@sha256:8bedbe742f140108897fb3532068e8316900d9814f399d676ac78b46e740e34e
```

</details>
