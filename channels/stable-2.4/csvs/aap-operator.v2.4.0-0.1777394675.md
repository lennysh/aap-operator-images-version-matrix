# `aap-operator.v2.4.0-0.1777394675`

[← Back to `stable-2.4`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1777394675` |
| **Build date** | 2026-04-28 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1774577278`](./aap-operator.v2.4.0-0.1774577278.md) |
| **Skip range** | `>=2.0.1-0.1635279521 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:9c244cb5d0801944223f0097398388a45b14da6d76fa841711d04fec56d2def9` |
| **Seen in OCP operator indexes** | 4.12, 4.14, 4.16, 4.18–4.20 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.33 | 1776921438 | 2026-04-28 | `sha256:5e6df0e99880` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-04-26 | `sha256:93adcfa2bfba` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.11 | 1776921438 | 2026-04-28 | `sha256:b294fced3ee3` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-04-26 | `sha256:d29f680b97d6` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.11 | 1776865104 | 2026-04-26 | `sha256:51588cd724ef` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 2.0.0 | 1776921438 | 2026-04-28 | `sha256:821e81f63e3a` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1776921438 | 2026-04-28 | `sha256:b011c7e0b154` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1776921438 | 2026-04-28 | `sha256:b011c7e0b154` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 2.0.0 | 1776921438 | 2026-04-28 | `sha256:b011c7e0b154` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.8 | 1776921438 | 2026-04-28 | `sha256:1415398470de` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-04-26 | `sha256:2c0d7225292b` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.8 | 1776865104 | 2026-04-28 | `sha256:7f47c22c8d9f` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.260325 | 1776921438 | 2026-04-28 | `sha256:0b8167b518bb` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-04-26 | `sha256:277829a6fea8` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-04-26 | `sha256:38e8ca2e8d1a` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1776921438 | 2026-04-28 | `sha256:b854538cc1d6` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-04-28 | `sha256:9c244cb5d080` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202603040115.p2.g9308e7f.assembly.stream.el8 | 2026-03-04 | `sha256:e6bfbe1e3a33` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1776847972 | 2026-04-22 | `sha256:d16ef3604f65` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1776847972 | 2026-04-22 | `sha256:d16ef3604f65` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1776847972 | 2026-04-22 | `sha256:d16ef3604f65` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1776847972 | 2026-04-22 | `sha256:d16ef3604f65` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1776848142 | 2026-04-22 | `sha256:f28a7c321695` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1776848142 | 2026-04-22 | `sha256:f28a7c321695` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1776848142 | 2026-04-22 | `sha256:f28a7c321695` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1776921438 | 2026-04-23 | `sha256:46f08923b566` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1776921438 | 2026-04-23 | `sha256:46f08923b566` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1776921438 | 2026-04-23 | `sha256:46f08923b566` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:93adcfa2bfbac717787a2cb10a8b3c2bfa403de98c53688c6f2e5272ea773d3f
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:5e6df0e9988011d73782e3ff63e900782171ed4c31735686e3c728813108a7d6
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:d29f680b97d6164b66c359eb9c3a9d9421450b5322702edef86f9a16f1b60ecf
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:b294fced3ee3e0bd3be2cf3ab8cc022fce72813cb1f98a946671ea465ffdfb54
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:51588cd724ef5b2d86897cb97b122ef41c7aff656e9376b0aba81f3e3e8e97f6
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:821e81f63e3a5e3fc543ef5b37b65acc6da38464c61b2d4ee709f4739bd71d43
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:b011c7e0b154ea897e4e511bccf4d40ed30637b845f715804a14bb8c389884df
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:2c0d7225292bdf23e6657cf02725bf769b24912b87002f4a7580eb6bd0d7f509
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:1415398470de98dac84f20a60a0759baabde7463c9a87b9f9ee1b2720d304632
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:7f47c22c8d9f2c95ce0c2c3b82b6789989a01ba9b254a2b03d842adc473f9f4d
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:277829a6fea81b602720f7bed4251eb4a5a7bda2d7b72d9e3800121cd03759b1
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:0b8167b518bbcd3e8c877196259486353fc18de15c402797b8caa5c3e0b61899
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:38e8ca2e8d1a52ef732f0042d69f008b0533b7316932113d52461c3d20fdf777
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:b854538cc1d629e63b74d8f3dd20889906d80867649065145af56889ba9c9f92
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:9c244cb5d0801944223f0097398388a45b14da6d76fa841711d04fec56d2def9
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:e6bfbe1e3a33d6f146ca70c040d0232ab254f98847efd1b2a382685c331e53a2
registry.redhat.io/rhel8/postgresql-15@sha256:d16ef3604f65c46a8cc80a538b6bafe9b7b42987856654eda8976ed29eccef48
registry.redhat.io/rhel8/redis-6@sha256:f28a7c321695934d6880a36ed82331b32968e9bc1fada522bf53d17fde8981d5
registry.redhat.io/ubi8/ubi-minimal@sha256:46f08923b566497395dda7d4d07bad383b4eedd5a382c3e22e715b169f414331
```

</details>
