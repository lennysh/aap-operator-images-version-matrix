# Red Hat Ansible Automation Platform - Operator Images Version Matrix

[![GitHub last commit](https://img.shields.io/github/last-commit/lennysh/aap-operator-images-version-matrix.svg)](https://github.com/lennysh/aap-operator-images-version-matrix/commits/main) [![GitHub license](https://img.shields.io/github/license/lennysh/aap-operator-images-version-matrix.svg)](https://github.com/lennysh/aap-operator-images-version-matrix/blob/main/LICENSE) [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](https://github.com/lennysh/aap-operator-images-version-matrix/pulls) ![GitHub contributors](https://img.shields.io/github/contributors/lennysh/aap-operator-images-version-matrix) ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/lennysh/aap-operator-images-version-matrix/update-matrix.yml) ![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/lennysh/aap-operator-images-version-matrix)

This repository is a community-driven reference for the container images shipped by every Red Hat Ansible Automation Platform (AAP) operator release on OpenShift. For each operator ClusterServiceVersion (CSV) in each OLM channel, it lists every image the operator deploys, along with its component version, build date, and digest. You can use it to:

* see which Controller, EDA, Hub, Gateway, and other component versions an operator CSV ships,
* compare image digests between operator releases, and
* get the full list of image pull specs for mirroring to disconnected clusters.

## 📋 Operator Channels

The tables below are generated automatically. Click a channel to see every CSV in it.

[comment]: <> (BEGIN Ansible Managed)

| Channel (click for details) | CSVs | Latest CSV | Latest Build Date |
| :-------------------------- | ---: | :--------- | :---------------- |
| [stable-2.4](./channels/stable-2.4/README.md) | 41 | [aap-operator.v2.4.0-0.1793880845](./channels/stable-2.4/csvs/aap-operator.v2.4.0-0.1793880845.md) | 2026-11-05 |
| [stable-2.4-cluster-scoped](./channels/stable-2.4-cluster-scoped/README.md) | 41 | [aap-operator.v2.4.0-0.1793887686](./channels/stable-2.4-cluster-scoped/csvs/aap-operator.v2.4.0-0.1793887686.md) | 2026-11-05 |
| [stable-2.5](./channels/stable-2.5/README.md) | 41 | [aap-operator.v2.5.0-0.1793872036](./channels/stable-2.5/csvs/aap-operator.v2.5.0-0.1793872036.md) | 2026-11-05 |
| [stable-2.5-cluster-scoped](./channels/stable-2.5-cluster-scoped/README.md) | 41 | [aap-operator.v2.5.0-0.1793872138](./channels/stable-2.5-cluster-scoped/csvs/aap-operator.v2.5.0-0.1793872138.md) | 2026-11-05 |
| [stable-2.6](./channels/stable-2.6/README.md) | 25 | [aap-operator.v2.6.0-0.1793870311](./channels/stable-2.6/csvs/aap-operator.v2.6.0-0.1793870311.md) | 2026-11-05 |
| [stable-2.6-cluster-scoped](./channels/stable-2.6-cluster-scoped/README.md) | 25 | [aap-operator.v2.6.0-0.1793870349](./channels/stable-2.6-cluster-scoped/csvs/aap-operator.v2.6.0-0.1793870349.md) | 2026-11-05 |
| [stable-2.7](./channels/stable-2.7/README.md) | 16 | [aap-operator.v2.7.0-0.1794269743](./channels/stable-2.7/csvs/aap-operator.v2.7.0-0.1794269743.md) | 2026-11-10 |
| [stable-2.7-cluster-scoped](./channels/stable-2.7-cluster-scoped/README.md) | 16 | [aap-operator.v2.7.0-0.1794269668](./channels/stable-2.7-cluster-scoped/csvs/aap-operator.v2.7.0-0.1794269668.md) | 2026-11-10 |

[comment]: <> (END Ansible Managed)

## ⚙️ How It Works

1. **Scrape** (`operator_images.yml --tags scrape`): discovers every Red Hat operator index tag (`registry.redhat.io/redhat/redhat-operator-index:v<ocp>`) from OpenShift 4.11 upward, including new major versions, then reads the file-based catalog for the `ansible-automation-platform-operator` package in each one. Every `stable-*` channel for AAP 2.4 and later is tracked automatically, so new AAP releases and new OpenShift versions show up without any config change. For every CSV, it writes `channels/<channel>/vars/<csv>.yml` with the bundle's `relatedImages`. CSVs are merged across all scanned indexes and are never deleted, so the history is kept after Red Hat prunes old CSVs from an index. An index whose digest hasn't changed since its last scrape is not pulled again.
2. **Labels** (`operator_images.yml --tags labels`): runs `skopeo inspect` (without pulling) on each image digest that hasn't been seen before and caches the `version`, `release`, and `build-date` labels in `data/image_labels.yml`. Digests never change, so each one is inspected only once.
3. **Markdown** (`md_generator.yml`): renders `channels/<channel>/README.md`, `channels/<channel>/csvs/<csv>.md`, and the channel table above.

Do **not** edit the generated Markdown files. Run the playbooks instead.

## 🛠 Updating the Matrix

### GitHub Actions (recommended)

The **Update operator images matrix** workflow runs on a schedule and can also be started manually. It opens a pull request when something changed.

1. Add these repository secrets (Settings → Secrets and variables → Actions):
   * `REGISTRY_REDHAT_IO_USERNAME`: Red Hat registry service-account username
   * `REGISTRY_REDHAT_IO_PASSWORD`: Red Hat registry service-account token
2. Allow Actions to open PRs (Settings → Actions → General → Workflow permissions):
   * Read and write permissions
   * **Allow GitHub Actions to create and approve pull requests**

To create a service account, go to [Red Hat Hybrid Cloud Console → Service Accounts](https://console.redhat.com/iam/service-accounts).

### Prerequisites (local)

* Python 3.13+ and the pinned dependencies: `pip install -r requirements.txt`
* `podman` and `skopeo` on your PATH
* Access to `registry.redhat.io` (`podman login registry.redhat.io`, or set `REGISTRY_USERNAME` / `REGISTRY_PASSWORD`)

### Local workflow

Run these from the repository root:

```bash
# 1. Scrape channels and resolve image version labels
ansible-playbook operator_images.yml

# 2. Regenerate the Markdown
ansible-playbook md_generator.yml
```

### Choosing channels and indexes

By default, nothing needs to be configured: operator index versions and channels are discovered on every run. To narrow the discovery, edit [`config.yml`](config.yml):

```yaml
aap_operator_images_ocp_min_version: "4.11"     # oldest operator index to scan
aap_operator_images_ocp_exclude: []             # discovered indexes to skip
aap_operator_images_channel_pattern: '^stable-' # channels to track (regex)
aap_operator_images_channel_min_version: "2.4"  # oldest AAP version to track
aap_operator_images_channel_exclude: []         # matching channels to skip
```

Setting `aap_operator_images_ocp_versions` or `aap_operator_images_channels` to an explicit list turns off discovery for that setting. This is handy for a single run:

```bash
ansible-playbook operator_images.yml \
  -e '{"aap_operator_images_channels": ["stable-2.6"], "aap_operator_images_ocp_versions": ["4.20"]}'
```

Other useful options:

```bash
# Reuse an operator index extract from .cache/ instead of pulling the index again
ansible-playbook operator_images.yml -e aap_operator_images_refresh_index=false

# Re-read every index even if its digest hasn't changed since the last scrape
ansible-playbook operator_images.yml -e aap_operator_images_skip_unchanged_index=false

# Only scrape CSV data; skip the skopeo label lookups
ansible-playbook operator_images.yml --tags scrape
```

## 📁 Repository Layout

| Path | Contents |
| :--- | :------- |
| `config.yml` | Discovery settings, channel filters, and paths |
| `requirements.txt` | Pinned Python dependencies (kept current by Dependabot) |
| `channels/<channel>/vars/<csv>.yml` | Raw image data per CSV (source of truth) |
| `channels/<channel>/README.md` | Generated channel overview |
| `channels/<channel>/csvs/<csv>.md` | Generated per-CSV image report |
| `data/image_labels.yml` | Cached image labels keyed by digest |
| `roles/operator_images_scrape` | Operator index discovery and scraper (`aap_operator_index_discover`, `aap_operator_channel_scrape` modules) |
| `roles/operator_images_labels` | Image label resolver (`aap_image_labels` module) |
| `roles/md_generator` | Markdown templates |

## 🤝 Contributing

Contributions are highly encouraged! New AAP channels and OpenShift versions are picked up automatically, so no config change is needed for a new release. Please don't submit hand edits to files under `channels/`, because they are regenerated (CI fails if the generated Markdown is out of date).

## ✍️ Authors

* [LennySh](https://github.com/lennysh)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
