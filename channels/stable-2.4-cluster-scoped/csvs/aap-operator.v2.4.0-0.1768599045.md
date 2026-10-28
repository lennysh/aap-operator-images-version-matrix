# `aap-operator.v2.4.0-0.1768599045`

[← Back to `stable-2.4-cluster-scoped`](../README.md)

| | |
|---|---|
| **Channel** | `stable-2.4-cluster-scoped` |
| **Operator package** | `ansible-automation-platform-operator` |
| **Operator version** | `2.4.0+0.1768599045` |
| **Build date** | 2026-01-16 |
| **Previous CSV** | [`aap-operator.v2.4.0-0.1767619081`](./aap-operator.v2.4.0-0.1767619081.md) |
| **Skip range** | `>=2.0.1-0.1635283332 <2.4.1` |
| **Bundle image** | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:e6adc5f32e854fbaaa041600819808d9437d74e205109ef3f08a0575d05729a5` |
| **Seen in OCP operator indexes** | 4.18 |

## Container images

| Component | Image | Version | Release | Image Build Date | Digest |
|---|---|---|---|---|---|
| controller | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8` | 4.5.30 | 1768178537 | 2026-01-16 | `sha256:7aa874142520` |
| automation-controller-manager | `registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-01-10 | `sha256:862de9ee1237` |
| eda | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8` | 1.0.8 | 1768178537 | 2026-01-15 | `sha256:a2876f0f756c` |
| eda-manager | `registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator` | 2.4-next | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-01-10 | `sha256:85e3ad8552d3` |
| eda_ui | `registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8` | 1.0.8 | 1766406056 | 2026-01-14 | `sha256:864cc5cdb85b` |
| ee_minimal | `registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8` | 1.0.0 | 1764046129 | 2026-01-10 | `sha256:1b95c0cff557` |
| control_plane_ee | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1764046129 | 2026-01-15 | `sha256:4b5f6837e588` |
| controller_init_container | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1764046129 | 2026-01-15 | `sha256:4b5f6837e588` |
| ee_supported | `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8` | 1.0.0 | 1764046129 | 2026-01-15 | `sha256:4b5f6837e588` |
| hub | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8` | 4.9.5 | 1768178537 | 2026-01-15 | `sha256:0ce63b8082b7` |
| automation-hub-manager | `registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-01-10 | `sha256:12aedd620283` |
| hub_web | `registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8` | 4.9.5 | 1766406056 | 2026-01-15 | `sha256:6059832f6f0a` |
| ansible_ai_connect | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8` | 2.4.20260121 | 1766090732 | 2026-01-13 | `sha256:9306076bb155` |
| ansible-lightspeed-manager | `registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-01-10 | `sha256:c8d28149a0e1` |
| platform-resource-manager | `registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator` | 2.4 | 202411130135.p0.g2a1edf2.assembly.stream.el8 | 2026-01-10 | `sha256:b0543e8edb2d` |
| ansible_job_runner_image | `registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8` | 2.4 | 1764046129 | 2026-01-16 | `sha256:ddc1aa803cf5` |
| (operator bundle) | `registry.redhat.io/ansible-automation-platform/platform-operator-bundle` | 2.4 | 2.4 | 2026-01-16 | `sha256:e6adc5f32e85` |
| kube-rbac-proxy | `registry.redhat.io/openshift4/ose-kube-rbac-proxy` | v4.15.0 | 202509151014.p2.g9308e7f.assembly.stream.el8 | 2025-09-16 | `sha256:fa0acefda43e` |
| ansible_ai_connect_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1768365248 | 2026-01-14 | `sha256:f5ff8f1968b4` |
| controller_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1768365248 | 2026-01-14 | `sha256:f5ff8f1968b4` |
| eda_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1768365248 | 2026-01-14 | `sha256:f5ff8f1968b4` |
| hub_postgres | `registry.redhat.io/rhel8/postgresql-15` | 1 | 1768365248 | 2026-01-14 | `sha256:f5ff8f1968b4` |
| controller_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1766406130 | 2025-12-22 | `sha256:22127c3d0db2` |
| eda_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1766406130 | 2025-12-22 | `sha256:22127c3d0db2` |
| hub_redis | `registry.redhat.io/rhel8/redis-6` | 1 | 1766406130 | 2025-12-22 | `sha256:22127c3d0db2` |
| controller_init_projects_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1768178537 | 2026-01-12 | `sha256:9f5006710578` |
| eda_init_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1768178537 | 2026-01-12 | `sha256:9f5006710578` |
| hub_init_gpg_container | `registry.redhat.io/ubi8/ubi-minimal` | 8.10 | 1768178537 | 2026-01-12 | `sha256:9f5006710578` |

## Image pull specs

<details><summary>All 19 image references (for mirroring)</summary>

```text
registry.redhat.io/ansible-automation-platform-24/controller-rhel8-operator@sha256:862de9ee1237281a433e8db126e264cfaf777a136a401cd76fb0dfa49da8b4f1
registry.redhat.io/ansible-automation-platform-24/controller-rhel8@sha256:7aa874142520b20dd28f2e781625c11b4b9b0c895066d6b4e6c1509a14811c28
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8-operator@sha256:85e3ad8552d376152276e02cdf980fe582e81d41c9585856373f3f4b1cf43ce7
registry.redhat.io/ansible-automation-platform-24/eda-controller-rhel8@sha256:a2876f0f756cb9e75095c0591915e47359ae9a7c1ee2b1313470d21b205eee80
registry.redhat.io/ansible-automation-platform-24/eda-controller-ui-rhel8@sha256:864cc5cdb85b34099167195fbfefa9f60d871dc26a5c3630dc2072ea71d011fc
registry.redhat.io/ansible-automation-platform-24/ee-minimal-rhel8@sha256:1b95c0cff55743709daa0ed99e4878b0a75e6791b48f41605615336e7acaa353
registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8@sha256:4b5f6837e5886e58704e14b302bd1656cb00466988c1adda3a62097b97eefcb1
registry.redhat.io/ansible-automation-platform-24/hub-rhel8-operator@sha256:12aedd62028303dfff8827143b886034f3eccb173816a9cbfa122fbffa10171e
registry.redhat.io/ansible-automation-platform-24/hub-rhel8@sha256:0ce63b8082b7040275408f301df77221e7e9cbdd6d23794cad83b30f54825c7b
registry.redhat.io/ansible-automation-platform-24/hub-web-rhel8@sha256:6059832f6f0aaecd4f8615ebf79fb26c13ee78af77e9b1931c33af3c3fe81940
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8-operator@sha256:c8d28149a0e1277848e8d4743f27a9f238c25761f443c70f454199c2bda435f8
registry.redhat.io/ansible-automation-platform-24/lightspeed-rhel8@sha256:9306076bb15533356d4694341713066078c087ae36e7d4fe1f80fa45580cc9b6
registry.redhat.io/ansible-automation-platform-24/platform-resource-rhel8-operator@sha256:b0543e8edb2d61fa4aa2812f0287c5b9ec54833c1bef5c3c769034ed112391b6
registry.redhat.io/ansible-automation-platform-24/platform-resource-runner-rhel8@sha256:ddc1aa803cf58737e1ba3124ae4d426f9eb9ed2d6701d9d24d48979327306027
registry.redhat.io/ansible-automation-platform/platform-operator-bundle@sha256:e6adc5f32e854fbaaa041600819808d9437d74e205109ef3f08a0575d05729a5
registry.redhat.io/openshift4/ose-kube-rbac-proxy@sha256:fa0acefda43e309e7f9f31f5247c933d0b868ff1573ece2f38e0549d7e2ec942
registry.redhat.io/rhel8/postgresql-15@sha256:f5ff8f1968b4c842da981e234efee065c66bc5208d93055c3135b536f421d432
registry.redhat.io/rhel8/redis-6@sha256:22127c3d0db2e5c71c65378e065442c9064282f46a79867e2501350c5d811ba8
registry.redhat.io/ubi8/ubi-minimal@sha256:9f5006710578c36da022efbc740b27821056d504d582e1aeb204a602d2e8e4ce
```

</details>
