# `aap-operator.v2.4.0-0.1741194076`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1741194076` |
| **Build date** | 2025-03-05 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1737661496`](./aap-operator.v2.4.0-0.1737661496.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:832a3c6588295fbdd2e187962cc7e960fba9aee90a9f61a4005313d92cad575f` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.19 | 1 | 2025-03-05 | `sha256:b29a19a546bb` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 168 | 2025-03-05 | `sha256:5504a6a8ea0b` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 32 | 2025-03-05 | `sha256:ace28a71dff6` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 168 | 2025-03-05 | `sha256:ce9c347787bb` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 31 | 2025-03-05 | `sha256:bfed8eb13f3b` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 835 | 2025-03-05 | `sha256:38ef1077469a` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 928 | 2025-03-05 | `sha256:9278ac2e1e55` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 928 | 2025-03-05 | `sha256:9278ac2e1e55` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 928 | 2025-03-05 | `sha256:9278ac2e1e55` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.2 | 36 | 2025-03-05 | `sha256:5e15346e4410` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 167 | 2025-03-05 | `sha256:ee1d807826b1` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.2 | 34 | 2025-03-05 | `sha256:d8e6852cc15d` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 2 | 2025-03-05 | `sha256:8fd64fbc6f7c` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 34 | 2025-03-05 | `sha256:3a31cbf86e8c` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 162 | 2025-03-05 | `sha256:9b0bf9f8a63a` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 203 | 2025-03-05 | `sha256:fd448daca321` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2383 | 2025-03-05 | `sha256:832a3c658829` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202502171304.p0.g9308e7f.assembly.stream.el8 | 2025-02-17 | `sha256:c811cffdb695` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 213.1739758163 | 2025-02-17 | `sha256:286d68707de5` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 213.1739758163 | 2025-02-17 | `sha256:286d68707de5` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 213.1739758163 | 2025-02-17 | `sha256:286d68707de5` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 213.1739758163 | 2025-02-17 | `sha256:286d68707de5` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:5504a6a8ea0bdb548c0dfe4a6e7d6bb64326eca497fec8e4d2aae4f23d31311b
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:b29a19a546bb80952889694aa917d145e2aee052afea4be0843fd0f6e687b2af
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:ce9c347787bb5ffad532e3377626cc119f0b182088e3811555397c6a31573b31
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:ace28a71dff6df8e3b82e9f65e98c1d8f89966e3d0d6943506f37eafbaae6b17
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:bfed8eb13f3bb51417207b2f0022b14d598bcf42b61477c97effca580a9b2d6b
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:38ef1077469a9e1754ca550cf21ea6c7b937253fbeaa6d0c585366d4b8e27e73
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:9278ac2e1e55f0484b815844efa55a6d339f6710b9b118f7b7cc39bea2efd916
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:ee1d807826b1b6e5dffbe4fa2e1fd3c9a380abe1b64be309e46f9fea6c518f35
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:5e15346e44109339385b6a0ca3cd9193b29eddbd841ad246b3b59f74098172ed
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:d8e6852cc15defb33316ade88bb7fb1a9050559511a96e595dbcfacda4eb3eff
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:3a31cbf86e8c7b73867ddefa501f33df70a7b8194c71d973b9bc1eb25542e064
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:8fd64fbc6f7cf59af4647668d06aee2d034d8934af9c51164e45be88e3082b0b
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:9b0bf9f8a63ab39d045f7bd966aab2cc5a7e7ae44474d8e367df3f4436f96893
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:fd448daca321e4b4eafeaac309b7d419efe5530a47e53069b83706848191d099
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:832a3c6588295fbdd2e187962cc7e960fba9aee90a9f61a4005313d92cad575f
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:c811cffdb695664388fbbece7a6d434ab44ada8bccd02581179ee62859db7e02
registry.redhat.io/rhel8/postgresql-13@sha256:286d68707de5e737ae60c8c1f88de1bf6b47d3eefe9d4e0f611ce1801110e8f0
registry.redhat.io/rhel8/redis-6@sha256:5aae6ed0346240c17e62fa32425f84a8ad45498a9599a61bcc324bd17b2e54ce
registry.redhat.io/ubi8/ubi-minimal@sha256:c38cc770631788157f8ea989df65ff30359c9f8af3246fef244b32caed9d5862
```

</details>
