# `aap-operator.v2.5.0-0.1741368605`

[← Back to `stable-2.5`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1741368605` |
| **Build date** | 2025-03-07 |
| **Replaces** | [`aap-operator.v2.5.0-0.1740773472`](./aap-operator.v2.5.0-0.1740773472.md) |
| **Skip range** | `>=2.4.0-0.1727257740 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:4e18565e259a0a1f85ead2d6ce0857ca70d9f9b45680bc2897fb5ef5f661ced7` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.9 | 13 | 2025-03-07 | `sha256:b58e1403f97e` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 165 | 2025-03-07 | `sha256:46e523480a0d` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.6 | 5 | 2025-03-07 | `sha256:63a624d00bb6` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 168 | 2025-03-07 | `sha256:299c457acc3b` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.6 | 2 | 2025-03-07 | `sha256:30bd613c73ec` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 842 | 2025-03-07 | `sha256:e65d16b8eebd` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 934 | 2025-03-07 | `sha256:b9f60d9ebbbb` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 934 | 2025-03-07 | `sha256:b9f60d9ebbbb` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 934 | 2025-03-07 | `sha256:b9f60d9ebbbb` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 55 | 2025-03-07 | `sha256:e4cb517fdb62` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250312 | 2 | 2025-03-07 | `sha256:8cd3409a9dcf` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 213 | 2025-03-07 | `sha256:d1fdf29ff856` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.2 | 3 | 2025-03-07 | `sha256:1d30e7c5866e` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 167 | 2025-03-07 | `sha256:c6e24d76f1eb` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.2 | 3 | 2025-03-07 | `sha256:69cebbea3b0c` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250225 | 1 | 2025-03-07 | `sha256:a54a6fbca5cf` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 124 | 2025-03-07 | `sha256:1f390385bf51` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 120 | 2025-03-07 | `sha256:ba56a15360e9` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 150 | 2025-03-07 | `sha256:2d58147db3bd` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1187 | 2025-03-07 | `sha256:4e18565e259a` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202502171304.p0.g9308e7f.assembly.stream.el8 | 2025-02-17 | `sha256:c811cffdb695` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740654092 | 2025-02-27 | `sha256:8e4248b594c7` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740654092 | 2025-02-27 | `sha256:8e4248b594c7` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740654092 | 2025-02-27 | `sha256:8e4248b594c7` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740654092 | 2025-02-27 | `sha256:8e4248b594c7` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 90.1740654092 | 2025-02-27 | `sha256:8e4248b594c7` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 212.1739758165 | 2025-02-17 | `sha256:5aae6ed03462` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1179.1739286367 | 2025-02-11 | `sha256:c38cc7706317` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:46e523480a0d1e65881d200d614b4a2cc828c9bb4c6b6bfe1310c1e0f15dd47e
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:b58e1403f97ea14e58c02fd276c6044cc115306ff49ad745e2491e6293f21fcb
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:299c457acc3bf6a47d080ac16478ccbf7bd3d6e5cbd63a1da65889de76def628
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:63a624d00bb68d50979ced0836e3417ad042628ad005fd24b683ef22f2995ee8
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:30bd613c73ecf5715cf294a3f508069da9ccf36eef12fbbc144b4b55c79060e3
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:e65d16b8eebd532f0e189a726ab4b979b7059f6b5495cc69e1abfe610f8e3ebe
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:b9f60d9ebbbb5fdc394186574b95dea5763b045ceff253815afeb435c626914d
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:e4cb517fdb62cf1169f85456d6d148c3f9de9af2436f9802b170edf5a4417b06
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:d1fdf29ff8566104f1151d7c5e20bdd275a24cc80cafb9643747bc7d0a66423e
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:8cd3409a9dcf79d9add8cfb89a7c1a861787509a260a0bccdfab296e8ac1fe4f
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:c6e24d76f1ebe1f2391343cd085c68f33ade17bbf486e6b28f33833681ff7111
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:1d30e7c5866ec575afedfc65ea0a56bcb391900913d09dcdf8c5dc5e1c649ba2
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:69cebbea3b0c180fb5bdf4b090b50b9e94d1add731c63ef129020c5238812332
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:1f390385bf51a6119e2e1df48470cf790c226a7c2afec13bdbb76ea2e88d3a52
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:a54a6fbca5cf0e7916dc1efb63864ab5a06865d2a2009891314783780b06f34e
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:ba56a15360e981bc33da55efcbce3a63c7cddb2a61704c4204ddf9de844a0390
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:2d58147db3bde21e3d85731badab6f6fefb6ab1b34abdba8a0923c44d872f814
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:4e18565e259a0a1f85ead2d6ce0857ca70d9f9b45680bc2897fb5ef5f661ced7
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:c811cffdb695664388fbbece7a6d434ab44ada8bccd02581179ee62859db7e02
registry.redhat.io/rhel8/postgresql-15@sha256:8e4248b594c765038c824e5f0edc4bc83af00897c71d83dfe5d859c3a2a34798
registry.redhat.io/rhel8/redis-6@sha256:5aae6ed0346240c17e62fa32425f84a8ad45498a9599a61bcc324bd17b2e54ce
registry.redhat.io/ubi8/ubi-minimal@sha256:c38cc770631788157f8ea989df65ff30359c9f8af3246fef244b32caed9d5862
```

</details>
