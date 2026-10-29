# `aap-operator.v2.4.0-0.1746133932`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1746133932` |
| **Build date** | 2025-05-01 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1743630487`](./aap-operator.v2.4.0-0.1743630487.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:002a7a9a52b098d38fe220cbcea3e4d3011a122562eb62d5ec665cc5aadf26d1` |
| **Seen in OCP operator indexes** | 4.12–4.17 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.22 | 4 | 2025-05-01 | `sha256:81d479e8b6fe` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 174 | 2025-05-01 | `sha256:672af485e0db` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.7 | 38 | 2025-05-01 | `sha256:784195ddc177` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4 | 174 | 2025-05-01 | `sha256:f6135f55c669` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.7 | 36 | 2025-05-01 | `sha256:3e824193d253` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 899 | 2025-05-01 | `sha256:c65f73ebd2b4` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 999 | 2025-05-01 | `sha256:cdf0052c69a8` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 999 | 2025-05-01 | `sha256:cdf0052c69a8` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 999 | 2025-05-01 | `sha256:cdf0052c69a8` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.3 | 6 | 2025-05-01 | `sha256:e04c43ab601b` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 173 | 2025-05-01 | `sha256:9c84ae223bd8` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.3 | 4 | 2025-05-01 | `sha256:cd2b123b2574` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.250225 | 9 | 2025-05-01 | `sha256:c6aeb90340dc` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 42 | 2025-05-01 | `sha256:9f399e76103a` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 170 | 2025-05-01 | `sha256:08fc64964525` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 209 | 2025-05-01 | `sha256:bb4a7a47bfd4` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2500 | 2025-05-01 | `sha256:002a7a9a52b0` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202503310336.p0.g9308e7f.assembly.stream.el8 | 2025-03-31 | `sha256:ee2b26f32680` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 215 | 2025-04-16 | `sha256:e08d70285e94` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 215 | 2025-04-16 | `sha256:e08d70285e94` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 215 | 2025-04-16 | `sha256:e08d70285e94` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-13` | 1 | 215 | 2025-04-16 | `sha256:e08d70285e94` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:672af485e0db94f762195f70e31561a1d8d035652399de88dc5ac80818a345ee
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:81d479e8b6fe7d0486d33fa5b785af935c8dc96823e9bdd17d1ec1bf5402d78b
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:f6135f55c669a9f3e4fcfafec2083fd98a8379ef2d0ae7662c000da16920090f
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:784195ddc1772924976b73e6046714c00cf18cede62c1864ec72895631c3b405
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:3e824193d2531579a789aed043ce44207d3ba534e502bd26d814277cf4e4f17e
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:c65f73ebd2b4aea15ddeb949a7890c465bddc0cde3850a03e7ff0d9cc63a24fa
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:cdf0052c69a826fc117b8dd97c4f77ac09961438e05797fed55be72264e28d95
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:9c84ae223bd822efb9d2fcb17ae559441440a51f586d727b0d005a4382b22430
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:e04c43ab601b06dcfec45209c86c9e80b3ff737c4b6b41664cc8ad14ee013fb0
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:cd2b123b257435901a20e1d870c0d95f088fcb2285ba24ceddaeba37dd188d2c
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:9f399e76103a472caa606a4c3fbec210b458be014856ffd4682fec426e86cb14
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:c6aeb90340dcb7ddf31af135dbfd5e69d225d72ca4deb86dfc3433411a338935
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:08fc64964525349d0c3c423ae4fa73824d70d2a1fd5326d504711c6b8edc0b7d
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:bb4a7a47bfd4c8c413df1f20ff9372bcdb9301497a67ceffc5b845b7ccf9e4ab
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:002a7a9a52b098d38fe220cbcea3e4d3011a122562eb62d5ec665cc5aadf26d1
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:ee2b26f326808f90a89e2e91ca0efbf3387916ae59a765c075d7c35e9fbe8e79
registry.redhat.io/rhel8/postgresql-13@sha256:e08d70285e94618417354ba7ba099fbb11394465aa7e7edbe1779ed197525813
registry.redhat.io/rhel8/redis-6@sha256:3d8c1326faadcb66b79facb311844cbdb3a462a4af47f8e68944382824d1ba8b
registry.redhat.io/ubi8/ubi-minimal@sha256:b2a1bec3dfbc7a14a1d84d98934dfe8fdde6eb822a211286601cf109cbccb075
```

</details>
