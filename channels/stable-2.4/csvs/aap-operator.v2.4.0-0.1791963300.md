# `aap-operator.v2.4.0-0.1791963300`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1791963300` |
| **Build date** | 2026-10-14 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1789660429`](./aap-operator.v2.4.0-0.1789660429.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:68a4826a6609117f0e0dc208ffe2403e1f893770c43cc3dc059f653df6cec1a1` |
| **Seen in OCP operator indexes** | 4.12, 4.14, 4.16, 4.18–4.20 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.37 | 1791896186 | 2026-10-14 | `sha256:ecaf9258d14b` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator` | 2.4 | 202609220956.p2.gbc7aeec.assembly.stream.el9 | 2026-10-02 | `sha256:e7aa447b0141` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1791896186 | 2026-10-14 | `sha256:5d626cc97c0e` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator` | 2.4 | 202609220956.p2.gbc7aeec.assembly.stream.el9 | 2026-10-02 | `sha256:46736bbd6378` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1791836066 | 2026-10-13 | `sha256:4beb8e4fb286` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1791765785 | 2026-10-13 | `sha256:4ee32ee58e5c` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1791442285 | 2026-10-14 | `sha256:1bff3e6c9385` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1791442285 | 2026-10-14 | `sha256:1bff3e6c9385` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1791442285 | 2026-10-14 | `sha256:1bff3e6c9385` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1791896186 | 2026-10-14 | `sha256:dd7824d3db08` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator` | 2.4 | 202609220956.p2.gbc7aeec.assembly.stream.el9 | 2026-10-02 | `sha256:e1e13054cce7` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1791766134 | 2026-10-14 | `sha256:1651c1329348` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1791765785 | 2026-10-13 | `sha256:1ad3f8e18940` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator` | 2.4 | 202609220956.p2.gbc7aeec.assembly.stream.el9 | 2026-10-02 | `sha256:7e605f5493ac` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator` | 2.4 | 202609220956.p2.gbc7aeec.assembly.stream.el9 | 2026-10-13 | `sha256:b9cc047b0395` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1791442285 | 2026-10-14 | `sha256:e94c3e13cada` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-10-14 | `sha256:68a4826a6609` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9` | v4.18.0 | 202609201015.p2.gf72b2ec.assembly.stream.el9 | 2026-09-20 | `sha256:6e55f07cf51a` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1791939163 | 2026-10-14 | `sha256:11d9152512a7` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1791939163 | 2026-10-14 | `sha256:11d9152512a7` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1791939163 | 2026-10-14 | `sha256:11d9152512a7` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1791939163 | 2026-10-14 | `sha256:11d9152512a7` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1791943921 | 2026-10-14 | `sha256:230bcd6b4338` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1791943921 | 2026-10-14 | `sha256:230bcd6b4338` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1791943921 | 2026-10-14 | `sha256:230bcd6b4338` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1791896186 | 2026-10-13 | `sha256:8de6d48ae7b4` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1791896186 | 2026-10-13 | `sha256:8de6d48ae7b4` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1791896186 | 2026-10-13 | `sha256:8de6d48ae7b4` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:ecaf9258d14bf899dd778e9153ca4da8a79d8db199d4d0392e31dd725af2c1b3
registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator@sha256:e7aa447b0141bbfe09f7204084e904c06b4514061dd562b47a925d0aa599474e
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:5d626cc97c0e8b271149f88bc9f803b466b8be9005d36332ae29678b23cab00a
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator@sha256:46736bbd637846ac14d60fe7fbe61a31250509abdaa54ea2d4daaa4347cd77ab
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:4beb8e4fb286782ccd22103039cfe982c44262968bc119fee1ab373ed92f9ee3
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:4ee32ee58e5cd1f0f7cf6c6eeceddf025e5dc5d2eb23f13868e1bd94a6baa92f
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:1bff3e6c93851365a948da16a8b3ab85036b74dbd235adbd8203fdde543d38d0
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:dd7824d3db0841fc93e8f9289e782b63e906852af58e732c36382815a23fb7ac
registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator@sha256:e1e13054cce72ae6f1421b700e4799b32f9f4b790060f82641e7727cc5699edd
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:1651c1329348d9b4bdd617b9c191ead73175a0718a9433488ba10ce8132cbc08
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:1ad3f8e18940086d4612b0424fbdb32af82107786612b310abb7838d4eb14a28
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator@sha256:7e605f5493aceb5db5adc3af5bc279cf7120968e665b1fd5efebc4a3b0eda1ad
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator@sha256:b9cc047b039506eacd69e03fc67b78d87cd485a2b92d2006f9b7cea1c2158130
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:e94c3e13cadaadf64049326aa34e3c38db0805815b39547a7973cbc821818966
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:68a4826a6609117f0e0dc208ffe2403e1f893770c43cc3dc059f653df6cec1a1
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9@sha256:6e55f07cf51a50a23f7826f24ede651d158b8c446bd6f798c0f6b9a1146c14f3
registry.redhat.io/rhel8/postgresql-15@sha256:11d9152512a7a4a20f7b21f07e397ff3de5521b30c8a6db3cae3b61e8d84e139
registry.redhat.io/rhel8/redis-6@sha256:230bcd6b433864d4aad348a8b527aae711d12dea196695ce425f73f47abc7355
registry.redhat.io/ubi8/ubi-minimal@sha256:8de6d48ae7b421bca02fc402543eb69b2acb3dcadf18c0287d509eeea08f6fb2
```

</details>
