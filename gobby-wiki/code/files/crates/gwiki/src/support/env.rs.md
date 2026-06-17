---
title: crates/gwiki/src/support/env.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/env.rs
  ranges:
  - 21-24
  - 27-30
  - 32-49
  - 51-55
  - 57-66
  - 68-75
  - 77-89
  - 91-98
  - 100-109
  - 111-142
  - 144-154
  - 156-180
  - 182-188
  - 190-200
  - 202-218
  - 220-224
  - 226-234
  - 236-238
  - 251-257
  - 261-285
  - 288-297
  - 299-322
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/env.rs:21-24](crates/gwiki/src/support/env.rs#L21-L24), [crates/gwiki/src/support/env.rs:27-30](crates/gwiki/src/support/env.rs#L27-L30), [crates/gwiki/src/support/env.rs:32-49](crates/gwiki/src/support/env.rs#L32-L49), [crates/gwiki/src/support/env.rs:51-55](crates/gwiki/src/support/env.rs#L51-L55), [crates/gwiki/src/support/env.rs:57-66](crates/gwiki/src/support/env.rs#L57-L66), [crates/gwiki/src/support/env.rs:68-75](crates/gwiki/src/support/env.rs#L68-L75), [crates/gwiki/src/support/env.rs:77-89](crates/gwiki/src/support/env.rs#L77-L89), [crates/gwiki/src/support/env.rs:91-98](crates/gwiki/src/support/env.rs#L91-L98), [crates/gwiki/src/support/env.rs:100-109](crates/gwiki/src/support/env.rs#L100-L109), [crates/gwiki/src/support/env.rs:111-142](crates/gwiki/src/support/env.rs#L111-L142), [crates/gwiki/src/support/env.rs:144-154](crates/gwiki/src/support/env.rs#L144-L154), [crates/gwiki/src/support/env.rs:156-180](crates/gwiki/src/support/env.rs#L156-L180), [crates/gwiki/src/support/env.rs:182-188](crates/gwiki/src/support/env.rs#L182-L188), [crates/gwiki/src/support/env.rs:190-200](crates/gwiki/src/support/env.rs#L190-L200), [crates/gwiki/src/support/env.rs:202-218](crates/gwiki/src/support/env.rs#L202-L218), [crates/gwiki/src/support/env.rs:220-224](crates/gwiki/src/support/env.rs#L220-L224), [crates/gwiki/src/support/env.rs:226-234](crates/gwiki/src/support/env.rs#L226-L234), [crates/gwiki/src/support/env.rs:236-238](crates/gwiki/src/support/env.rs#L236-L238), [crates/gwiki/src/support/env.rs:251-257](crates/gwiki/src/support/env.rs#L251-L257), [crates/gwiki/src/support/env.rs:261-285](crates/gwiki/src/support/env.rs#L261-L285), [crates/gwiki/src/support/env.rs:288-297](crates/gwiki/src/support/env.rs#L288-L297), [crates/gwiki/src/support/env.rs:299-322](crates/gwiki/src/support/env.rs#L299-L322)

</details>

# crates/gwiki/src/support/env.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Resolves and validates gwiki runtime environment settings, centered on how to find the PostgreSQL database URL and related broker/daemon metadata. `database_url` tries direct env vars first, then falls back through a brokered lookup, a bootstrap file, and finally gcore config; `database_url_for` wraps failures in `WikiError` for command-specific reporting. The rest of the helpers support that flow by reading local tokens, building broker requests with timeouts, validating loopback daemon URLs and database URLs, parsing trimmed/positive env values, and spawning the broker when needed.
[crates/gwiki/src/support/env.rs:21-24]
[crates/gwiki/src/support/env.rs:27-30]
[crates/gwiki/src/support/env.rs:32-49]
[crates/gwiki/src/support/env.rs:51-55]
[crates/gwiki/src/support/env.rs:57-66]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `HubBootstrap` | class | `struct HubBootstrap {` | `HubBootstrap [class]` | `6eef951c-c8de-5b3b-9eeb-431794396c90` | 21-24 [crates/gwiki/src/support/env.rs:21-24] | Indexed class `HubBootstrap` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:21-24] |
| `ValidatedDaemonUrl` | class | `struct ValidatedDaemonUrl {` | `ValidatedDaemonUrl [class]` | `8786c9c3-4b38-5f85-8f9a-a2fa7b4b178a` | 27-30 [crates/gwiki/src/support/env.rs:27-30] | Indexed class `ValidatedDaemonUrl` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:27-30] |
| `database_url` | function | `pub(crate) fn database_url() -> anyhow::Result<Option<String>> {` | `database_url [function]` | `7acfa5f4-1a8d-55c2-8c66-45705c0b2ae9` | 32-49 [crates/gwiki/src/support/env.rs:32-49] | Indexed function `database_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:32-49] |
| `database_url_for` | function | `pub(crate) fn database_url_for(command: &str) -> Result<Option<String>, WikiError> {` | `database_url_for [function]` | `58500376-9458-5dd0-aacc-f3d53c8080f0` | 51-55 [crates/gwiki/src/support/env.rs:51-55] | Indexed function `database_url_for` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:51-55] |
| `database_url_from_env` | function | `pub(crate) fn database_url_from_env() -> Option<String> {` | `database_url_from_env [function]` | `1fad4bf4-a690-52bc-8d03-af8b394ae02c` | 57-66 [crates/gwiki/src/support/env.rs:57-66] | Indexed function `database_url_from_env` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:57-66] |
| `resolve_database_url_from_gcore_config` | function | `fn resolve_database_url_from_gcore_config(home: &Path) -> anyhow::Result<Option<String>> {` | `resolve_database_url_from_gcore_config [function]` | `18b25317-47eb-57e2-a149-7bee167bfb4a` | 68-75 [crates/gwiki/src/support/env.rs:68-75] | Indexed function `resolve_database_url_from_gcore_config` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:68-75] |
| `resolve_database_url_from_bootstrap_file` | function | `fn resolve_database_url_from_bootstrap_file(path: &Path) -> anyhow::Result<Option<String>> {` | `resolve_database_url_from_bootstrap_file [function]` | `30377db8-c862-5fb7-a883-ddd62e0e4acb` | 77-89 [crates/gwiki/src/support/env.rs:77-89] | Indexed function `resolve_database_url_from_bootstrap_file` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:77-89] |
| `resolve_brokered_database_url_at` | function | `fn resolve_brokered_database_url_at(` | `resolve_brokered_database_url_at [function]` | `96399e18-c124-5761-8a66-ebd00f10e793` | 91-98 [crates/gwiki/src/support/env.rs:91-98] | Indexed function `resolve_brokered_database_url_at` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:91-98] |
| `read_local_cli_token_at` | function | `fn read_local_cli_token_at(gobby_home: &Path) -> anyhow::Result<String> {` | `read_local_cli_token_at [function]` | `61248448-64b6-5ffa-b408-02fe22e9008a` | 100-109 [crates/gwiki/src/support/env.rs:100-109] | Indexed function `read_local_cli_token_at` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:100-109] |
| `request_broker_database_url` | function | `fn request_broker_database_url(daemon_url: &str, token: &str) -> anyhow::Result<String> {` | `request_broker_database_url [function]` | `ce1e7c82-54fe-51d6-8571-84cfc5fe744e` | 111-142 [crates/gwiki/src/support/env.rs:111-142] | Indexed function `request_broker_database_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:111-142] |
| `broker_timeout` | function | `fn broker_timeout() -> Duration {` | `broker_timeout [function]` | `3e2c75af-1071-5ca2-a35a-c7576e8bb014` | 144-154 [crates/gwiki/src/support/env.rs:144-154] | Indexed function `broker_timeout` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:144-154] |
| `validate_loopback_daemon_url` | function | `fn validate_loopback_daemon_url(daemon_url: &str) -> anyhow::Result<ValidatedDaemonUrl> {` | `validate_loopback_daemon_url [function]` | `920f35da-5b07-5065-b5fa-c5ab57f1ad2c` | 156-180 [crates/gwiki/src/support/env.rs:156-180] | Indexed function `validate_loopback_daemon_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:156-180] |
| `request_base_url` | function | `fn request_base_url(url: &url::Url, target_addr: SocketAddr) -> anyhow::Result<String> {` | `request_base_url [function]` | `65d37a63-038e-5844-85cd-a977b9824c6e` | 182-188 [crates/gwiki/src/support/env.rs:182-188] | Indexed function `request_base_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:182-188] |
| `host_header` | function | `fn host_header(host: &str, port: Option<u16>) -> String {` | `host_header [function]` | `51ab5688-3f0e-5b2e-8541-8fe116e619a9` | 190-200 [crates/gwiki/src/support/env.rs:190-200] | Indexed function `host_header` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:190-200] |
| `validate_database_url` | function | `fn validate_database_url(database_url: &str) -> anyhow::Result<String> {` | `validate_database_url [function]` | `d20510a2-2f42-591d-b7be-4edd7db4fba3` | 202-218 [crates/gwiki/src/support/env.rs:202-218] | Indexed function `validate_database_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:202-218] |
| `non_empty_trimmed` | function | `fn non_empty_trimmed(value: Option<String>) -> Option<String> {` | `non_empty_trimmed [function]` | `bb07c06f-6a16-5a03-b359-d42af8261ce6` | 220-224 [crates/gwiki/src/support/env.rs:220-224] | Indexed function `non_empty_trimmed` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:220-224] |
| `max_inbox_item_bytes_from_env` | function | `pub(crate) fn max_inbox_item_bytes_from_env() -> u64 {` | `max_inbox_item_bytes_from_env [function]` | `227d07d9-395c-5de5-b248-f26b36b2c4fb` | 226-234 [crates/gwiki/src/support/env.rs:226-234] | Indexed function `max_inbox_item_bytes_from_env` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:226-234] |
| `parse_positive_u64` | function | `fn parse_positive_u64(raw: &str) -> Option<u64> {` | `parse_positive_u64 [function]` | `aafef5e8-bf8a-5a7f-a7d7-e7a44e2a4855` | 236-238 [crates/gwiki/src/support/env.rs:236-238] | Indexed function `parse_positive_u64` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:236-238] |
| `positive_u64_env_parser_rejects_invalid_values` | function | `fn positive_u64_env_parser_rejects_invalid_values() {` | `positive_u64_env_parser_rejects_invalid_values [function]` | `4dadd1a6-e5a9-5733-8ff9-727835cf4023` | 251-257 [crates/gwiki/src/support/env.rs:251-257] | Indexed function `positive_u64_env_parser_rejects_invalid_values` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:251-257] |
| `database_url_uses_gobby_broker_when_env_missing` | function | `fn database_url_uses_gobby_broker_when_env_missing() {` | `database_url_uses_gobby_broker_when_env_missing [function]` | `d5b21cc5-c6c1-530d-8aac-f21ed1660bd6` | 261-285 [crates/gwiki/src/support/env.rs:261-285] | Indexed function `database_url_uses_gobby_broker_when_env_missing` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:261-285] |
| `database_url_broker_rejects_non_loopback_daemon_host` | function | `fn database_url_broker_rejects_non_loopback_daemon_host() {` | `database_url_broker_rejects_non_loopback_daemon_host [function]` | `6091d7ec-1fde-5e22-b8d8-76e452eb8ad4` | 288-297 [crates/gwiki/src/support/env.rs:288-297] | Indexed function `database_url_broker_rejects_non_loopback_daemon_host` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:288-297] |
| `spawn_database_url_broker` | function | `fn spawn_database_url_broker(` | `spawn_database_url_broker [function]` | `df1722b7-7ee6-534e-ae75-bd9bd50080e3` | 299-322 [crates/gwiki/src/support/env.rs:299-322] | Indexed function `spawn_database_url_broker` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:299-322] |
