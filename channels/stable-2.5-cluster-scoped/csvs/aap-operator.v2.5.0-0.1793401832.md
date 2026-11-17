# `aap-operator.v2.5.0-0.1793401832`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1793401832` |
| **Build date** | 2026-10-30 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1793205548`](./aap-operator.v2.5.0-0.1793205548.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:5360b62df46552990006674e1db82f3711efef8a9426cf6e0209f57df49dc229` |
| **Seen in OCP operator indexes** | 4.12, 4.14, 4.16, 4.18–4.20 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| automation-controller-container | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.34 | 1793307920 | 2026-10-30 | `sha256:0783143fb2b7` |
| automation-controller-operator-container | `registry.redhat.io/ansible-automation-platform-25/controller-rhel9-operator` | 2.5 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:e99c6d93ac70` |
| automation-eda-controller-container | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.23 | 1793307920 | 2026-10-30 | `sha256:47d5a07004ba` |
| automation-eda-controller-operator-container | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel9-operator` | 2.5 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:a281756c6c52` |
| automation-eda-ui-container | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.23 | 1793232806 | 2026-10-30 | `sha256:5356c293866c` |
| ee-minimal-rhel8-container | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 2.0.0 | 1793205688 | 2026-10-29 | `sha256:ad5e04d47364` |
| ee-supported-rhel8-container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 2.0.0 | 1793205688 | 2026-10-30 | `sha256:b39d775d3071` |
| automation-gateway-proxy-container | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 1793307920 | 2026-10-30 | `sha256:979a52c9c52b` |
| automation-gateway-container | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20260923 | 1793307920 | 2026-10-30 | `sha256:b6e0076752e0` |
| automation-gateway-operator-container | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel9-operator` | 2.5 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:1ea1082e8997` |
| automation-hub-container | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.19 | 1793205688 | 2026-10-30 | `sha256:b88272114a96` |
| automation-hub-operator-container | `registry.redhat.io/ansible-automation-platform-25/hub-rhel9-operator` | 2.5 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:b67d9cbd2918` |
| automation-hub-web-container | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.19 | 1793232806 | 2026-10-30 | `sha256:51dcae3b296e` |
| ansible-lightspeed-chatbot-container | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.260325 | 1774368033 | 2026-03-25 | `sha256:a79a6ac47a03` |
| ansible-lightspeed-container | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.20261009 | 1793307920 | 2026-10-30 | `sha256:f4842f883705` |
| ansible-lightspeed-operator-container | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel9-operator` | 2.5 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:d43a29244f0e` |
| platform-resource-operator-container | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel9-operator` | 2.5 | 202610241849.p2.gbc7aeec.assembly.stream.el9 | 2026-10-27 | `sha256:aaacff7889b7` |
| platform-resource-runner-container | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 1793205688 | 2026-10-30 | `sha256:fa5e692e3907` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 2.5 | 2026-10-30 | `sha256:5360b62df465` |
| kube-rbac-proxy-container | `registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9:v4.18` | v4.18.0 | 202610241849.p2.gf72b2ec.assembly.stream.el9 | 2026-10-24 | `sha256:81853fd2cdac` |
| postgresql-15-container | `registry.redhat.io/rhel8/postgresql-15:1` | 1 | 1793232954 | 2026-10-29 | `sha256:9f16073d8fc3` |
| redis-6-container | `registry.redhat.io/rhel8/redis-6:1` | 1 | 1793257610 | 2026-10-29 | `sha256:6812edca8236` |
| ubi8-minimal-container | `registry.redhat.io/ubi8-minimal:latest` | 8.10 | 1793307920 | 2026-10-29 | `sha256:62d3baa1ca1c` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:0783143fb2b70c5ec8b40893b0b7988f097f53442cdea1f9d45ba00c7438e831
registry.redhat.io/ansible-automation-platform-25/controller-rhel9-operator@sha256:e99c6d93ac7071c9d82b151a9f794c343c834e743f02bfd4d790baf5c917a7c3
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:47d5a07004ba7ce0ba2d88910086ae47bb8bd25f08b5b0f8f1ecfd180190f65f
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel9-operator@sha256:a281756c6c52fa19681f1029a6680a7b53b1eeb30fd89fd2fcc17b07114b93fb
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:5356c293866c9d852b77fa2d2b746bd62dda43922ca885c301e63fbf090911d2
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:ad5e04d47364e5d123a8afe33fa3169db90695532ee120e4a6972eb66a389c59
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:b39d775d30714408d06d0d1485290d2ae8099c02901d2d7976ac48538611fafd
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:979a52c9c52b727866633a7ecf599eef996bbe7bb586e9eb250286dd818b8860
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:b6e0076752e08dca5f3c247f0becfd286dba3ae24318282f99c6b2858be7bb3c
registry.redhat.io/ansible-automation-platform-25/gateway-rhel9-operator@sha256:1ea1082e89977a991aa3e1fa9a49d32f4a10bb6a9c1a59b361a6449ba5c44962
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:b88272114a9626c86976f4d87b37c0e57f3b57d9059ba2bdad4e4c27f668abbd
registry.redhat.io/ansible-automation-platform-25/hub-rhel9-operator@sha256:b67d9cbd2918e6c60c1e95733f0c0c4db6ddfc4a07b232d8cdbdff6a4c175e58
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:51dcae3b296e7b9a0b2338c7656a6c96161717b6e474624719133f0d35bf83b8
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:a79a6ac47a035d8ef64d78f49f9c7c423c02ef6b5474608d0490ea49b076c941
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:f4842f883705ab2a4e4fee114c2c30cc9470aa8c06f896b028b1b477508a9d43
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel9-operator@sha256:d43a29244f0e079c7818912a3380adb1cf33cbccfdb279f1ef8ca8c4d20152eb
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel9-operator@sha256:aaacff7889b737bde0c22d730bf95c887a72dfac549a48c7dfe2265559543267
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:fa5e692e3907a5c64c0333007da0550a0646259bad7d2dcf86b641d51a4ca4e6
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:5360b62df46552990006674e1db82f3711efef8a9426cf6e0209f57df49dc229
registry.redhat.io/openshift4/ose-kube-rbac-proxy-rhel9:v4.18@sha256:81853fd2cdacb13900522e788191b12f67cdb763ec21607a4ec097b15fb8d012
registry.redhat.io/rhel8/postgresql-15:1@sha256:9f16073d8fc3ed4beceff4b52f150f29b319fcbe7384afdda5aeb45f0f88d7c9
registry.redhat.io/rhel8/redis-6:1@sha256:6812edca823607aead2752b20061696a296915c1a35951b55f622156729abd19
registry.redhat.io/ubi8-minimal:latest@sha256:62d3baa1ca1cdc4613ad79521b21bdef5baa81ea9167441c731acef18b8253cf
```

</details>
