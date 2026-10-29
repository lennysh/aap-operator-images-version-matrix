# `aap-operator.v2.4.0-0.1707506910`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1707506910` |
| **Build date** | 2024-02-09 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1702352195`](./aap-operator.v2.4.0-0.1702352195.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:7bb2530e42d28474abce8a549f76c17cccace023b79e40f602477ca220520a4b` |
| **Seen in OCP operator indexes** | 4.11–4.16 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.1 | 9 | 2024-02-09 | `sha256:8ff3fd6876d2` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 114 | 2024-02-09 | `sha256:4293abc76ece` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.3 | 37 | 2024-02-09 | `sha256:df0e727d3341` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 123 | 2024-02-09 | `sha256:bd491d49db01` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.3 | 38 | 2024-02-09 | `sha256:56c8c301e1c4` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 528 | 2024-02-09 | `sha256:4f9066d475b0` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 543 | 2024-02-09 | `sha256:dd834d88ea96` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 543 | 2024-02-09 | `sha256:dd834d88ea96` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 543 | 2024-02-09 | `sha256:dd834d88ea96` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.7.3 | 42 | 2024-02-09 | `sha256:913f3895f0b9` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 108 | 2024-02-09 | `sha256:3270d26662c9` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.7.3 | 42 | 2024-02-09 | `sha256:1c8bc23dcca7` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 103 | 2024-02-09 | `sha256:d7acfaed3151` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 125 | 2024-02-09 | `sha256:61c4519c3751` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 1122 | 2024-02-09 | `sha256:7bb2530e42d2` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202401291254.p0.gc04896c.assembly.stream | 2024-01-29 | `sha256:75adbc384463` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 163 | 2024-01-03 | `sha256:3903d562425d` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 163 | 2024-01-03 | `sha256:3903d562425d` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 163 | 2024-01-03 | `sha256:3903d562425d` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 162 | 2024-01-03 | `sha256:444200241cb9` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 162 | 2024-01-03 | `sha256:444200241cb9` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 162 | 2024-01-03 | `sha256:444200241cb9` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1108.1706795067 | 2024-02-01 | `sha256:6825946f10e8` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1108.1706795067 | 2024-02-01 | `sha256:6825946f10e8` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1108.1706795067 | 2024-02-01 | `sha256:6825946f10e8` |
| RELATED_IMAGE_CONTROLLER | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.1 | 9 | 2024-02-09 | `sha256:8ff3fd6876d2` |
| automation-controller-operator-controller-manager/automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 114 | 2024-02-09 | `sha256:4293abc76ece` |
| RELATED_IMAGE_EDA | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.3 | 37 | 2024-02-09 | `sha256:df0e727d3341` |
| eda-server-operator-controller-manager/eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 123 | 2024-02-09 | `sha256:bd491d49db01` |
| RELATED_IMAGE_EDA_UI | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.3 | 38 | 2024-02-09 | `sha256:56c8c301e1c4` |
| RELATED_IMAGE_EE_MINIMAL | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 528 | 2024-02-09 | `sha256:4f9066d475b0` |
| RELATED_IMAGE_CONTROLLER_INIT_CONTAINER | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 543 | 2024-02-09 | `sha256:dd834d88ea96` |
| RELATED_IMAGE_CONTROL_PLANE_EE | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 543 | 2024-02-09 | `sha256:dd834d88ea96` |
| RELATED_IMAGE_EE_SUPPORTED | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 543 | 2024-02-09 | `sha256:dd834d88ea96` |
| RELATED_IMAGE_HUB | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.7.3 | 42 | 2024-02-09 | `sha256:913f3895f0b9` |
| automation-hub-operator-controller-manager/automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 108 | 2024-02-09 | `sha256:3270d26662c9` |
| RELATED_IMAGE_HUB_WEB | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.7.3 | 42 | 2024-02-09 | `sha256:1c8bc23dcca7` |
| resource-operator-controller-manager/platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 103 | 2024-02-09 | `sha256:d7acfaed3151` |
| RELATED_IMAGE_ANSIBLE_JOB_RUNNER_IMAGE | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 125 | 2024-02-09 | `sha256:61c4519c3751` |
| automation-controller-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202401291254.p0.gc04896c.assembly.stream | 2024-01-29 | `sha256:75adbc384463` |
| automation-hub-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202401291254.p0.gc04896c.assembly.stream | 2024-01-29 | `sha256:75adbc384463` |
| eda-server-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202401291254.p0.gc04896c.assembly.stream | 2024-01-29 | `sha256:75adbc384463` |
| resource-operator-controller-manager/kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.11.0 | 202401291254.p0.gc04896c.assembly.stream | 2024-01-29 | `sha256:75adbc384463` |
| RELATED_IMAGE_CONTROLLER_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 163 | 2024-01-03 | `sha256:3903d562425d` |
| RELATED_IMAGE_EDA_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 163 | 2024-01-03 | `sha256:3903d562425d` |
| RELATED_IMAGE_HUB_POSTGRES | `registry.redhat.io/rhel8/postgresql-13` | 1 | 163 | 2024-01-03 | `sha256:3903d562425d` |
| RELATED_IMAGE_CONTROLLER_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 162 | 2024-01-03 | `sha256:444200241cb9` |
| RELATED_IMAGE_EDA_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 162 | 2024-01-03 | `sha256:444200241cb9` |
| RELATED_IMAGE_HUB_REDIS | `registry.redhat.io/rhel8/redis-6` | 1 | 162 | 2024-01-03 | `sha256:444200241cb9` |
| RELATED_IMAGE_CONTROLLER_INIT_PROJECTS_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1108.1706795067 | 2024-02-01 | `sha256:6825946f10e8` |
| RELATED_IMAGE_EDA_INIT_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1108.1706795067 | 2024-02-01 | `sha256:6825946f10e8` |
| RELATED_IMAGE_HUB_INIT_GPG_CONTAINER | `registry.redhat.io/ubi8/ubi-minimal` | 8.9 | 1108.1706795067 | 2024-02-01 | `sha256:6825946f10e8` |

## Image pull specs

<details><summary>All 17 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:4293abc76eceedd79802a099ec97daaf7f521a007c91eec620c9e21e57c012a1
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:8ff3fd6876d26f36adc75c3134d55eb5b07bea8d4a1f66e2e4799d231fb4228d
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:bd491d49db010420c62a512ee786847cc1fc89200a1bc595b57c9ba563549d14
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:df0e727d3341667713ec8b4ab3af3a78a9812c221c25a173ab20a3bb66fbf49a
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:56c8c301e1c40f97097da03df89634da248af367c883f2c65ddcab8ea77228be
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:4f9066d475b006dc90ecc77d017f8a8233758016589b5d68bc08966908337732
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:dd834d88ea9634e42d74dce9a08722322e61d211ee557056b4b4f7ded81442ee
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:3270d26662c9744b2e42a46ffc37b0a1beccdf787281d755c0261ea07e0c81eb
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:913f3895f0b9a895350f0f300c097fa225899496f947afe5c7d2b32e5cd82af7
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:1c8bc23dcca78aa087242a9cac0435d955f6bba61ee99a4dd66bdc2604def008
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:d7acfaed3151a1c775c6c38e0f531b30712f2ba77339f6053ef688bddaf56300
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:61c4519c37516c8ab1bc13cba99af9fce99196b4b3b79c9100c659a5a235919d
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:7bb2530e42d28474abce8a549f76c17cccace023b79e40f602477ca220520a4b
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:75adbc384463d1fdde83c867c86bdb86a7275d18f3bdbcdc258577a723c0b46b
registry.redhat.io/rhel8/postgresql-13@sha256:3903d562425dd564986123280dc076548fb3d24c74138dcd857652f53052e0a7
registry.redhat.io/rhel8/redis-6@sha256:444200241cb9186cd97d564d7acf077d83fc997a8ee5ee7fdae41b604895085c
registry.redhat.io/ubi8/ubi-minimal@sha256:6825946f10e8c81586fa7815c4f06016af05cfc231d921ec9699402a6655d201
```

</details>
