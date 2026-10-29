# `aap-operator.v2.5.0-0.1746138413`

[← Back to `stable-2.5-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.5-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.5.0+0.1746138413` |
| **Build date** | 2025-05-01 |
| **Previous CSV** | [`aap-operator.v2.5.0-0.1743660958`](./aap-operator.v2.5.0-0.1743660958.md) |
| **Skip range** | `>=2.4.0-0.1727259094 <2.5.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:58c114102d68be408fddc46411dd5f63b53484f2b49461f9a173d8d77b954319` |
| **Seen in OCP operator indexes** | 4.12–4.21 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8` | 4.6.12 | 13 | 2025-05-01 | `sha256:7a8214083781` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator` | 2.5 | 176 | 2025-05-01 | `sha256:3ffc8abbf39c` |
| eda | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8` | 1.1.8 | 5 | 2025-05-01 | `sha256:23e059f090eb` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator` | 2.5 | 178 | 2025-05-01 | `sha256:df139bfa83b8` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8` | 1.1.8 | 1 | 2025-05-01 | `sha256:91f88f167965` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8` | 1.0.0 | 902 | 2025-05-01 | `sha256:0e902fe90276` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1000 | 2025-05-01 | `sha256:658ca6e4c568` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1000 | 2025-05-01 | `sha256:658ca6e4c568` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8` | 1.0.0 | 1000 | 2025-05-01 | `sha256:658ca6e4c568` |
| gateway_proxy | `registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8` | 2.5.10 | 13 | 2025-05-01 | `sha256:19f8eef28d84` |
| gateway | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8` | 2.5.20250507 | 1 | 2025-05-01 | `sha256:f9ebf8435a8f` |
| manager | `registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator` | 2.5 | 229 | 2025-05-01 | `sha256:e0dbba9fb503` |
| hub | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8` | 4.10.4 | 2 | 2025-05-01 | `sha256:b10b7faec5b7` |
| automation-hub-operator | `registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator` | 2.5 | 178 | 2025-05-01 | `sha256:612bfca23b8e` |
| hub_web | `registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8` | 4.10.4 | 1 | 2025-05-01 | `sha256:27970564fe89` |
| ansible_ai_connect_chatbot | `registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8` | 2.5.250429 | 1 | 2025-05-01 | `sha256:91613027e70c` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8` | 2.5.250429 | 1 | 2025-05-01 | `sha256:1bae12e13375` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator` | 2.5 | 138 | 2025-05-01 | `sha256:6cbf70cb8e0d` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator` | 2.5 | 131 | 2025-05-01 | `sha256:1cbf52731ef3` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8` | 2.5 | 170 | 2025-05-01 | `sha256:fab0843b2197` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.5 | 1315 | 2025-05-01 | `sha256:58c114102d68` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202503310336.p0.g9308e7f.assembly.stream.el8 | 2025-03-31 | `sha256:ee2b26f32680` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| gateway_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 92 | 2025-04-16 | `sha256:0576206b44a5` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| gateway_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 214 | 2025-04-16 | `sha256:3d8c1326faad` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1255 | 2025-04-16 | `sha256:b2a1bec3dfbc` |

## Image pull specs

<details><summary>All 23 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-25/controller-rhel8-operator@sha256:3ffc8abbf39ca983b04adc85f7f89b21eef36eea421e23c54114e02dbc2712bb
registry.redhat.io/ansible-automation-platform-25/controller-rhel8@sha256:7a8214083781ef563c5bb26e86237501e05c170faee9528a947998f41deb188a
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8-operator@sha256:df139bfa83b82c9cfd24554946ef533360e7f535cdbdd845f6ecba7a70b2f213
registry.redhat.io/ansible-automation-platform-25/eda-controller-rhel8@sha256:23e059f090eb0425e4fd2c3ff4705b72945cb8ca01f691571e0b32a4f6ae7d0c
registry.redhat.io/ansible-automation-platform-25/eda-controller-ui-rhel8@sha256:91f88f1679657f85107646df959265af923c280c6e1375b270595309120d9cba
registry.redhat.io/ansible-automation-platform-25/ee-minimal-rhel8@sha256:0e902fe90276a2ae7ae96de7dab65e2656b2a7f54634a0d966721974a26ac9a7
registry.redhat.io/ansible-automation-platform-25/ee-supported-rhel8@sha256:658ca6e4c5688b262a159a962b706fca9ffc7b187c31040ed31ac6e80ec65172
registry.redhat.io/ansible-automation-platform-25/gateway-proxy-rhel8@sha256:19f8eef28d84821811c47221318af78238937d820ffb543fc204a91485df0978
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8-operator@sha256:e0dbba9fb50338ce588e82b25ded260218e5bf00ce42b7d982af3822ccecc178
registry.redhat.io/ansible-automation-platform-25/gateway-rhel8@sha256:f9ebf8435a8f2aeecd824cc18162cf348099d2d535858845746012e783551015
registry.redhat.io/ansible-automation-platform-25/hub-rhel8-operator@sha256:612bfca23b8e3bcbe389eacb8f6edcc4e135d5ca960e4a9ccd625f3e2344e0ff
registry.redhat.io/ansible-automation-platform-25/hub-rhel8@sha256:b10b7faec5b75bc183ba794b2071060c366c3ea15c23f7a74a0b79b0048286d6
registry.redhat.io/ansible-automation-platform-25/hub-web-rhel8@sha256:27970564fe896b59702cc49c9d4c0a44c5ae66f3d7f66ee4906351878bc48d95
registry.redhat.io/ansible-automation-platform-25/lightspeed-chatbot-rhel8@sha256:91613027e70c37ac1a519c12694a541c3bed9ff077bc5b1215e25215d2d9fcba
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8-operator@sha256:6cbf70cb8e0d14cf0fe3670eafc33bac8ff587242de0513922c77e230864b970
registry.redhat.io/ansible-automation-platform-25/lightspeed-rhel8@sha256:1bae12e1337572e3bc1e72ef071d6476301441a4c5d4eda2e0c3fec24d86dc72
registry.redhat.io/ansible-automation-platform-25/platform-resource-rhel8-operator@sha256:1cbf52731ef3510d1f749c6d26b1dc97a4944c8d4601a2b77410697974d56328
registry.redhat.io/ansible-automation-platform-25/platform-resource-runner-rhel8@sha256:fab0843b219785a9dd699a1b0af02416c86bcb996f46388e765b83f563ed3655
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:58c114102d68be408fddc46411dd5f63b53484f2b49461f9a173d8d77b954319
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:ee2b26f326808f90a89e2e91ca0efbf3387916ae59a765c075d7c35e9fbe8e79
registry.redhat.io/rhel8/postgresql-15@sha256:0576206b44a5cb073b6364f7af104a4a17994f9bb8c7a948da9588d6b4bbf1e8
registry.redhat.io/rhel8/redis-6@sha256:3d8c1326faadcb66b79facb311844cbdb3a462a4af47f8e68944382824d1ba8b
registry.redhat.io/ubi8/ubi-minimal@sha256:b2a1bec3dfbc7a14a1d84d98934dfe8fdde6eb822a211286601cf109cbccb075
```

</details>
