# `aap-operator.v2.5.0-0.1729742145`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1729742145` |
| **Build date** | 2024-10-24 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1728520687`](./aap-operator.v2.5.0-0.1728520687.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:77091778407714bd8fed8ececb8e634d127fae747db0576d3cb992ef2fefc3cc` |
| **Seen in OCP operator indexes** | 4.18, 4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.2 | 14 | 2024-10-24 | `sha256:7ccbe3358a10` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 129 | 2024-10-24 | `sha256:f939c9ec57c0` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.2 | 2 | 2024-10-24 | `sha256:aed5fd3167d5` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 128 | 2024-10-24 | `sha256:210d01b36ffa` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.2 | 1 | 2024-10-24 | `sha256:c50bb291cb6a` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 754 | 2024-10-24 | `sha256:256b1b675262` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 822 | 2024-10-24 | `sha256:43071a77822b` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 822 | 2024-10-24 | `sha256:43071a77822b` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 822 | 2024-10-24 | `sha256:43071a77822b` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.0 | 25 | 2024-10-24 | `sha256:7b9616b98a13` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.3 | 1 | 2024-10-24 | `sha256:eeac83f10148` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 151 | 2024-10-24 | `sha256:c03ec39d361f` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.1 | 2 | 2024-10-24 | `sha256:523713b08909` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 131 | 2024-10-24 | `sha256:3eafc8a0bf9d` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.1 | 2 | 2024-10-24 | `sha256:bf38acea2512` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.241009 | 4 | 2024-10-24 | `sha256:44c2923b34c4` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 90 | 2024-10-24 | `sha256:b1819400e595` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 87 | 2024-10-24 | `sha256:5d56905794ae` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 117 | 2024-10-24 | `sha256:99e8dfb1ac8e` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 883 | 2024-10-24 | `sha256:770917784077` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202409240105.p0.ge8e8c84.assembly.stream.el8 | 2024-09-24 | `sha256:e34f91215898` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 82 | 2024-10-04 | `sha256:d8a0f58b4b85` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 204 | 2024-10-04 | `sha256:e76f07cdcbba` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1086 | 2024-09-17 | `sha256:7583ca0ea520` |

## Image pull specs

<details><summary>All 22 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:f939c9ec57c0730654d326bf00aa71fd95ca03b2d4b2c53fad0e705bd742fd24
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:7ccbe3358a10e34e9a86ccbb83e587f2813f2ffeee7b64bcb4e5fafd4c469df1
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:210d01b36ffaaf0a3776a9ca3f62e911f6f44bec9bd07b447744d51eed5a6e7f
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:aed5fd3167d51fca4a22ba42a2e29bc0e0ea67b899b8d5365ea927c8905ad14b
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:c50bb291cb6a813b84166a36b6ba657f291757381c477fb338221f88e78111ca
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:256b1b675262b4608a5f03e68287a90030d331e7f395da4e48cf89615f358920
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:43071a77822b13dac040ce7c0787f286234d62e5356d02620be47a4278800678
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:7b9616b98a13d562257d5c0358d4061f809b92867f2c09a92ee782e5533e2e30
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:c03ec39d361f2094886209fad4e5a02ba64e9b03ed6aa08491885c83946c73a4
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:eeac83f10148014bb1fca54a9a8903469cd57608f3c9f6819f533f3568b04507
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:3eafc8a0bf9d0f90c249d5bf783a885caf1c152cac3ed3d911f0cf0464ca75e6
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:523713b0890978feafc716511315452a4fde3f4911488d2e7d779d68e2cf5341
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:bf38acea2512b60db803fd5601c8593e0669e65be8fa66bfdad1daa07e40bca9
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:b1819400e5951787a4c22b7adb9009bb3cb6f42f28d883da7c26c69e571a5ff9
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:44c2923b34c43dd9168c68aecc73bf061d4ad15ec8b45efa7b98d61f1e418cc5
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:5d56905794aeb25ebe60b96e57f533509d8f66404a9c51fb616d9752b555b4d7
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:99e8dfb1ac8e7e7232f21a7f35dfaf45e66506817bc851cf7fc9757ef9ccbc57
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:77091778407714bd8fed8ececb8e634d127fae747db0576d3cb992ef2fefc3cc
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:e34f912158985525f6efb3c4b675f20854fc677c867d12fe3cd2e971309428dc
registry.redhat.io/rhel8/postgresql-15@sha256:d8a0f58b4b85524a55414532913533b60b63e1809b1d76a35680ad1fdce64c0e
registry.redhat.io/rhel8/redis-6@sha256:e76f07cdcbba8faa2ad7e5637045f28197037a68edfb82be23dc331f06beeeca
registry.redhat.io/ubi8/ubi-minimal@sha256:7583ca0ea52001562bd81a961da3f75222209e6192e4e413ee226cff97dbd48c
```

</details>
