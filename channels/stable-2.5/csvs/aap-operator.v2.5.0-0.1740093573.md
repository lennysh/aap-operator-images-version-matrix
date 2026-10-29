# `aap-operator.v2.5.0-0.1740093573`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1740093573` |
| **Build date** | 2025-02-20 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1739248042`](./aap-operator.v2.5.0-0.1739248042.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:5acee7b6440d3580e92e1264f3a357491e369a9ae272c071a3bdeab1e7a5960e` |
| **Seen in OCP operator indexes** | 4.12–4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.8 | 11 | 2025-02-20 | `sha256:28933827775b` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 156 | 2025-02-20 | `sha256:3abd97288091` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.4 | 12 | 2025-02-20 | `sha256:1bd2201a823b` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 158 | 2025-02-20 | `sha256:c471bf888480` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.4 | 7 | 2025-02-20 | `sha256:2692bf82ce97` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 828 | 2025-02-20 | `sha256:3e6fddb3e18e` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 914 | 2025-02-20 | `sha256:5608d23cec5d` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 914 | 2025-02-20 | `sha256:5608d23cec5d` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 914 | 2025-02-20 | `sha256:5608d23cec5d` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 47 | 2025-02-20 | `sha256:dfef4846a902` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250225 | 2 | 2025-02-20 | `sha256:1f9610a1ffb1` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 205 | 2025-02-20 | `sha256:ed47c5af29fe` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 36 | 2025-02-20 | `sha256:f72b38a2caf3` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 159 | 2025-02-20 | `sha256:aeab46cd4662` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 34 | 2025-02-20 | `sha256:a30e63115a89` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250204 | 5 | 2025-02-20 | `sha256:6b6c06bf8ccb` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 117 | 2025-02-20 | `sha256:67dd4f634fe6` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 112 | 2025-02-20 | `sha256:c15fc40d8627` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 144 | 2025-02-20 | `sha256:eed0b72bd46c` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1141 | 2025-02-20 | `sha256:5acee7b6440d` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202501280037.p0.g9308e7f.assembly.stream.el8 | 2025-01-28 | `sha256:7926a0fd3211` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1739758153 | 2025-02-17 | `sha256:fcd53def9185` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1739758153 | 2025-02-17 | `sha256:fcd53def9185` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1739758153 | 2025-02-17 | `sha256:fcd53def9185` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1739758153 | 2025-02-17 | `sha256:fcd53def9185` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1739758153 | 2025-02-17 | `sha256:fcd53def9185` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179 | 2025-01-21 | `sha256:d16d4445b156` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179 | 2025-01-21 | `sha256:d16d4445b156` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179 | 2025-01-21 | `sha256:d16d4445b156` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:3abd97288091ace21bb3011be348ba9b3f9c926626eb4d1bb6bceb96f6c8d01b
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:28933827775b262566386e5b9cb0da636efa454afde974b75092bd5f21365c2f
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:c471bf88848079831480342ae1c5b283fb81bd3254ffcc8534f7330afd90f36a
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:1bd2201a823be415bdefdcf61c371e997a782072bdfd09012421f1912e497493
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:2692bf82ce97f86e51c96c0302c9a756fd8d13d29b2a94d153b9587468d4c18a
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:3e6fddb3e18ef1737e99c38c05ad986a3a7b39109badb05c9878718e06276e59
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:5608d23cec5d30be2c7d9708d04d9d2ba171a3d7b3fcd60deb7c608e1ae0268f
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:dfef4846a902d79b09f90cf11c51c8d68c79e5818e827f9100f2d59ef99123c0
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:ed47c5af29fe14d270d7abbda334d9ab1018b79d836c247b0f4a5086d209b4e3
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:1f9610a1ffb1842c0f948892ed49382828ce7b0db8dd1e3969717cdab87e06a6
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:aeab46cd4662eeca240633120deaaa4284283dfa8097ab33c6504195e0fc94a5
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:f72b38a2caf38f349f2533b5bf99cffba0a694ea375946281972917f88cafc18
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:a30e63115a897cd3c75e680f3ff9259b42642aded92908b85ebbe86d1e37ddcc
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:67dd4f634fe69abfe4bc1cddf6109e8102a4342adba0bc23973c14bf0f3c9197
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:6b6c06bf8ccbbf2922c1238677e052abe5f6c40d56e3b28d97b88007a731e890
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:c15fc40d8627aebb3be24e433f1c69ca32bba0a6549f7b86425627cec0bd7b21
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:eed0b72bd46c33c5db747be054ebd6b3b1db4c30ad7fae339a1a3f879349c6bf
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:5acee7b6440d3580e92e1264f3a357491e369a9ae272c071a3bdeab1e7a5960e
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:7926a0fd3211fdb15cbb4b44e0db226d882f64a453c83a7659305d1b2dcd8321
registry.redhat.io/rhel8/postgresql-15@sha256:fcd53def91856c6d04f84063462b928ac10352048b8e9412f298b30e4dca5f70
registry.redhat.io/rhel8/redis-6@sha256:5aae6ed0346240c17e62fa32425f84a8ad45498a9599a61bcc324bd17b2e54ce
registry.redhat.io/ubi8/ubi-minimal@sha256:d16d4445b1567f29449fba3b6d2bc37db467dc3067d33e940477e55aecdf6e8e
```

</details>
