# `aap-operator.v2.4.0-0.1763137360`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1763137360` |
| **Build date** | 2025-11-14 |
| **Replaces** | [`aap-operator.v2.4.0-0.1760618870`](./aap-operator.v2.4.0-0.1760618870.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:8afc8caa56580c9112a5531a7d7cd3f71c5db71696bf11212e86c393f8d6caf8` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.27 | 2 | 2025-11-13 | `sha256:f97ee7bed5a4` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 185 | 2025-11-13 | `sha256:20bd39030ac8` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.8 | 1 | 2025-11-14 | `sha256:b2546e254a37` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 184 | 2025-11-13 | `sha256:17133ea621d0` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.8 | 1 | 2025-11-14 | `sha256:862c9fbded31` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 989 | 2025-11-13 | `sha256:432652840f2a` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1115 | 2025-11-13 | `sha256:55d58227f4cb` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1115 | 2025-11-13 | `sha256:55d58227f4cb` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1115 | 2025-11-13 | `sha256:55d58227f4cb` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.5 | 7 | 2025-11-13 | `sha256:1c5249f43c84` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 184 | 2025-11-13 | `sha256:afcae038bbec` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 7 | 2025-11-13 | `sha256:537a1995df14` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 22 | 2025-11-13 | `sha256:44d3c6353043` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 53 | 2025-11-13 | `sha256:b36520e23408` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 181 | 2025-11-13 | `sha256:4e7b9f37e7b0` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 221 | 2025-11-13 | `sha256:8e8f2f669e84` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2903 | 2025-11-14 | `sha256:8afc8caa5658` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202510221322.p2.g9308e7f.assembly.stream.el8 | 2025-10-22 | `sha256:58698c84109b` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1762403006 | 2025-11-06 | `sha256:68fc74033591` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1762403006 | 2025-11-06 | `sha256:68fc74033591` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1762403006 | 2025-11-06 | `sha256:68fc74033591` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1762403006 | 2025-11-06 | `sha256:68fc74033591` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1761769259 | 2025-10-29 | `sha256:d2eedb33525d` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1761769259 | 2025-10-29 | `sha256:d2eedb33525d` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1761769259 | 2025-10-29 | `sha256:d2eedb33525d` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1761032271 | 2025-10-21 | `sha256:951ee3cabb74` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1761032271 | 2025-10-21 | `sha256:951ee3cabb74` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1761032271 | 2025-10-21 | `sha256:951ee3cabb74` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:20bd39030ac893cad4dd1f8758620ed830586f00d8d68f940e2484b1e06da509
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:f97ee7bed5a4ccd9f023a54e6371184f536bfc7f17ee700d02d43ee66f2d1c2f
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:17133ea621d068b78e0f018f15bb89bddd4a40526e7c3718a319d4b6a2034adc
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:b2546e254a37819927c3ed97c5335afe8c0ad0cf2d217e10aa684d828e3686dc
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:862c9fbded31a75a5a80aa7960d6395bcaf09370ac1c35a9a067441697c5e55b
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:432652840f2ae39442d39fc1119fca309e029aa81e32b5308408d7260ccb5939
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:55d58227f4cb64ed9a8acf39734d35ff020ff89f4e48b5cc1f22ec93eebb501d
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:afcae038bbec18ed72c578410276936cc748dd4fd8c1b9d72c86d701c8010f14
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:1c5249f43c844d89e52c1544c40e3455206a6db03a76f8142c1a0624280b0eb7
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:537a1995df14761ad8ecd2f3543eb3ac304cb654ccb01c5048ad94c8d2f8c7e8
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:b36520e2340831a43f25deb0519e345195b5aca4eebaa9d8add6f63d69b0e0f7
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:44d3c635304340824e876c1db7e0623d598d072b6bf4d00f193d1461bfc44f45
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:4e7b9f37e7b0f026cbcd2e1dd7b0a7fa9a3fddda7985fcd05ce0d55fdb1a7d61
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:8e8f2f669e84a50e2449d1d40de23c4879ae128d01207f537afbe2a504f6d397
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:8afc8caa56580c9112a5531a7d7cd3f71c5db71696bf11212e86c393f8d6caf8
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:58698c84109b0833060ab86ef36c0092418c87aba61ba271bef60a18e6b5a6af
registry.redhat.io/rhel8/postgresql-15@sha256:68fc74033591a7c7608adb438a81ffdf232f199adbc7c92df286097debd815d0
registry.redhat.io/rhel8/redis-6@sha256:d2eedb33525dea497d4296b7fda806c0a4821937219e8cfb250e713667669fdd
registry.redhat.io/ubi8/ubi-minimal@sha256:951ee3cabb74246821ae31c2b808b7789310f5509882c153b7b178aaaeefa2d3
```

</details>
