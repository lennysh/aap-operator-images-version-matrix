# `aap-operator.v2.4.0-0.1793314410`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1793314410` |
| **Build date** | 2026-10-29 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1793164232`](./aap-operator.v2.4.0-0.1793164232.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:05c4cfa5bb4eff45c81bdbf297a4c4db7660eb610530f2311dfdb4a7964e6752` |
| **Seen in OCP operator indexes** | 4.12, 4.14, 4.16, 4.18–4.20 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.37 | 1793205688 | 2026-10-29 | `sha256:e1a1d697dd72` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:81ed289742f0` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1793205688 | 2026-10-29 | `sha256:12b8bfb102ff` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:cfe05b9c0cd5` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1793232806 | 2026-10-29 | `sha256:9c1817bf1fe5` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1793205688 | 2026-10-29 | `sha256:169b078c54ce` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1793205688 | 2026-10-29 | `sha256:546a9eca636d` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1793205688 | 2026-10-29 | `sha256:546a9eca636d` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1793205688 | 2026-10-29 | `sha256:546a9eca636d` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1793205688 | 2026-10-29 | `sha256:690c253a071a` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:c0403f946495` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1793232806 | 2026-10-29 | `sha256:67048ab5328b` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1793205688 | 2026-10-29 | `sha256:cd9478923af4` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:f81190022910` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator` | 2.4 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:5a31fe6a3944` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1793205688 | 2026-10-29 | `sha256:2ac96112ee22` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-10-29 | `sha256:05c4cfa5bb4e` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9` | v4.18.0 | 202610241849.p2.gf72b2ec.assembly.stream.el9 | 2026-10-24 | `sha256:81853fd2cdac` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793232954 | 2026-10-29 | `sha256:9f16073d8fc3` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793232954 | 2026-10-29 | `sha256:9f16073d8fc3` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793232954 | 2026-10-29 | `sha256:9f16073d8fc3` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1793232954 | 2026-10-29 | `sha256:9f16073d8fc3` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1793257610 | 2026-10-29 | `sha256:6812edca8236` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1793257610 | 2026-10-29 | `sha256:6812edca8236` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1793257610 | 2026-10-29 | `sha256:6812edca8236` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1793205688 | 2026-10-28 | `sha256:bc7e42f085da` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1793205688 | 2026-10-28 | `sha256:bc7e42f085da` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1793205688 | 2026-10-28 | `sha256:bc7e42f085da` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:e1a1d697dd724c44cd56521b4f748308972be8c985a999122e437c23be47f7d8
registry.redhat.io/ansible-automation-platform-24/controller-rhel9-operator@sha256:81ed289742f0af669fd7dde60c2e1567658cdda80faea72da00645bbf3cb801f
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:12b8bfb102ffb16bfdd44eec5781ed140030c8589a0c13d321abbbf7e7c85de9
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel9-operator@sha256:cfe05b9c0cd5a0ddb53bcdb279da59340282d7ab5c84f851aa206760b6c39ab7
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:9c1817bf1fe50a76668576c7a9f294fe741a1bc4c3bd146e81647b80a632876b
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:169b078c54ce4e582fea033196ffd62ae25a96783c280fe0f77e36c986e8b16c
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:546a9eca636d3b0e6f9dce426949eca6368ce4869ddf5fbcfff17bb5f69cebe5
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:690c253a071ae90830b2294f8adeb0f348cfce78a188f69fab2fb40820c1555a
registry.redhat.io/ansible-automation-platform-24/hub-rhel9-operator@sha256:c0403f94649582e06859b9374a442de5839981d4284ac30f1f65b57a91b7e030
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:67048ab5328ba0a7c6b41a740f365010205472402e5c5316eef319f7fc85d361
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:cd9478923af458760e1e2f60771b04a1b27fc760d2044b8e22737eafb3ce7a4f
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel9-operator@sha256:f811900229105ca6d85b52011df02fcd96899bff6b6c899ff92cc0be27d51225
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel9-operator@sha256:5a31fe6a3944313a75d5ba0b677d15a90717946e7b6e17c1c207b73c1e46fb28
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:2ac96112ee2223c0af2caa2a78b5a73d6df60920d3f70bb82802ec5184d8b412
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:05c4cfa5bb4eff45c81bdbf297a4c4db7660eb610530f2311dfdb4a7964e6752
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9@sha256:81853fd2cdacb13900522e788191b12f67cdb763ec21607a4ec097b15fb8d012
registry.redhat.io/rhel8/postgresql-15@sha256:9f16073d8fc3ed4beceff4b52f150f29b319fcbe7384afdda5aeb45f0f88d7c9
registry.redhat.io/rhel8/redis-6@sha256:6812edca823607aead2752b20061696a296915c1a35951b55f622156729abd19
registry.redhat.io/ubi8/ubi-minimal@sha256:bc7e42f085daa77b4cc51968ae9afffd0a96d802b710cdba6d75630200591e05
```

</details>
