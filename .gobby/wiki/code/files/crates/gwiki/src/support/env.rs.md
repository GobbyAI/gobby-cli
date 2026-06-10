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

# crates/gwiki/src/support/env.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

`crates/gwiki/src/support/env.rs` exposes 22 indexed API symbols.
[crates/gwiki/src/support/env.rs:21-24]
[crates/gwiki/src/support/env.rs:27-30]
[crates/gwiki/src/support/env.rs:32-49]
[crates/gwiki/src/support/env.rs:51-55]
[crates/gwiki/src/support/env.rs:57-66]
[crates/gwiki/src/support/env.rs:68-75]
[crates/gwiki/src/support/env.rs:77-89]
[crates/gwiki/src/support/env.rs:91-98]
[crates/gwiki/src/support/env.rs:100-109]
[crates/gwiki/src/support/env.rs:111-142]
[crates/gwiki/src/support/env.rs:144-154]
[crates/gwiki/src/support/env.rs:156-180]
[crates/gwiki/src/support/env.rs:182-188]
[crates/gwiki/src/support/env.rs:190-200]
[crates/gwiki/src/support/env.rs:202-218]
[crates/gwiki/src/support/env.rs:220-224]
[crates/gwiki/src/support/env.rs:226-234]
[crates/gwiki/src/support/env.rs:236-238]
[crates/gwiki/src/support/env.rs:251-257]
[crates/gwiki/src/support/env.rs:261-285]
[crates/gwiki/src/support/env.rs:288-297]
[crates/gwiki/src/support/env.rs:299-322]

## API Symbols

- `HubBootstrap` (class) component `HubBootstrap [class]` (`6eef951c-c8de-5b3b-9eeb-431794396c90`) lines 21-24 [crates/gwiki/src/support/env.rs:21-24]
  - Signature: `struct HubBootstrap {`
  - Purpose: Indexed class `HubBootstrap` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:21-24]
- `ValidatedDaemonUrl` (class) component `ValidatedDaemonUrl [class]` (`8786c9c3-4b38-5f85-8f9a-a2fa7b4b178a`) lines 27-30 [crates/gwiki/src/support/env.rs:27-30]
  - Signature: `struct ValidatedDaemonUrl {`
  - Purpose: Indexed class `ValidatedDaemonUrl` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:27-30]
- `database_url` (function) component `database_url [function]` (`7acfa5f4-1a8d-55c2-8c66-45705c0b2ae9`) lines 32-49 [crates/gwiki/src/support/env.rs:32-49]
  - Signature: `pub(crate) fn database_url() -> anyhow::Result<Option<String>> {`
  - Purpose: Indexed function `database_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:32-49]
- `database_url_for` (function) component `database_url_for [function]` (`58500376-9458-5dd0-aacc-f3d53c8080f0`) lines 51-55 [crates/gwiki/src/support/env.rs:51-55]
  - Signature: `pub(crate) fn database_url_for(command: &str) -> Result<Option<String>, WikiError> {`
  - Purpose: Indexed function `database_url_for` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:51-55]
- `database_url_from_env` (function) component `database_url_from_env [function]` (`1fad4bf4-a690-52bc-8d03-af8b394ae02c`) lines 57-66 [crates/gwiki/src/support/env.rs:57-66]
  - Signature: `pub(crate) fn database_url_from_env() -> Option<String> {`
  - Purpose: Indexed function `database_url_from_env` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:57-66]
- `resolve_database_url_from_gcore_config` (function) component `resolve_database_url_from_gcore_config [function]` (`18b25317-47eb-57e2-a149-7bee167bfb4a`) lines 68-75 [crates/gwiki/src/support/env.rs:68-75]
  - Signature: `fn resolve_database_url_from_gcore_config(home: &Path) -> anyhow::Result<Option<String>> {`
  - Purpose: Indexed function `resolve_database_url_from_gcore_config` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:68-75]
- `resolve_database_url_from_bootstrap_file` (function) component `resolve_database_url_from_bootstrap_file [function]` (`30377db8-c862-5fb7-a883-ddd62e0e4acb`) lines 77-89 [crates/gwiki/src/support/env.rs:77-89]
  - Signature: `fn resolve_database_url_from_bootstrap_file(path: &Path) -> anyhow::Result<Option<String>> {`
  - Purpose: Indexed function `resolve_database_url_from_bootstrap_file` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:77-89]
- `resolve_brokered_database_url_at` (function) component `resolve_brokered_database_url_at [function]` (`96399e18-c124-5761-8a66-ebd00f10e793`) lines 91-98 [crates/gwiki/src/support/env.rs:91-98]
  - Signature: `fn resolve_brokered_database_url_at(`
  - Purpose: Indexed function `resolve_brokered_database_url_at` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:91-98]
- `read_local_cli_token_at` (function) component `read_local_cli_token_at [function]` (`61248448-64b6-5ffa-b408-02fe22e9008a`) lines 100-109 [crates/gwiki/src/support/env.rs:100-109]
  - Signature: `fn read_local_cli_token_at(gobby_home: &Path) -> anyhow::Result<String> {`
  - Purpose: Indexed function `read_local_cli_token_at` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:100-109]
- `request_broker_database_url` (function) component `request_broker_database_url [function]` (`ce1e7c82-54fe-51d6-8571-84cfc5fe744e`) lines 111-142 [crates/gwiki/src/support/env.rs:111-142]
  - Signature: `fn request_broker_database_url(daemon_url: &str, token: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `request_broker_database_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:111-142]
- `broker_timeout` (function) component `broker_timeout [function]` (`3e2c75af-1071-5ca2-a35a-c7576e8bb014`) lines 144-154 [crates/gwiki/src/support/env.rs:144-154]
  - Signature: `fn broker_timeout() -> Duration {`
  - Purpose: Indexed function `broker_timeout` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:144-154]
- `validate_loopback_daemon_url` (function) component `validate_loopback_daemon_url [function]` (`920f35da-5b07-5065-b5fa-c5ab57f1ad2c`) lines 156-180 [crates/gwiki/src/support/env.rs:156-180]
  - Signature: `fn validate_loopback_daemon_url(daemon_url: &str) -> anyhow::Result<ValidatedDaemonUrl> {`
  - Purpose: Indexed function `validate_loopback_daemon_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:156-180]
- `request_base_url` (function) component `request_base_url [function]` (`65d37a63-038e-5844-85cd-a977b9824c6e`) lines 182-188 [crates/gwiki/src/support/env.rs:182-188]
  - Signature: `fn request_base_url(url: &url::Url, target_addr: SocketAddr) -> anyhow::Result<String> {`
  - Purpose: Indexed function `request_base_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:182-188]
- `host_header` (function) component `host_header [function]` (`51ab5688-3f0e-5b2e-8541-8fe116e619a9`) lines 190-200 [crates/gwiki/src/support/env.rs:190-200]
  - Signature: `fn host_header(host: &str, port: Option<u16>) -> String {`
  - Purpose: Indexed function `host_header` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:190-200]
- `validate_database_url` (function) component `validate_database_url [function]` (`d20510a2-2f42-591d-b7be-4edd7db4fba3`) lines 202-218 [crates/gwiki/src/support/env.rs:202-218]
  - Signature: `fn validate_database_url(database_url: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `validate_database_url` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:202-218]
- `non_empty_trimmed` (function) component `non_empty_trimmed [function]` (`bb07c06f-6a16-5a03-b359-d42af8261ce6`) lines 220-224 [crates/gwiki/src/support/env.rs:220-224]
  - Signature: `fn non_empty_trimmed(value: Option<String>) -> Option<String> {`
  - Purpose: Indexed function `non_empty_trimmed` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:220-224]
- `max_inbox_item_bytes_from_env` (function) component `max_inbox_item_bytes_from_env [function]` (`227d07d9-395c-5de5-b248-f26b36b2c4fb`) lines 226-234 [crates/gwiki/src/support/env.rs:226-234]
  - Signature: `pub(crate) fn max_inbox_item_bytes_from_env() -> u64 {`
  - Purpose: Indexed function `max_inbox_item_bytes_from_env` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:226-234]
- `parse_positive_u64` (function) component `parse_positive_u64 [function]` (`aafef5e8-bf8a-5a7f-a7d7-e7a44e2a4855`) lines 236-238 [crates/gwiki/src/support/env.rs:236-238]
  - Signature: `fn parse_positive_u64(raw: &str) -> Option<u64> {`
  - Purpose: Indexed function `parse_positive_u64` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:236-238]
- `positive_u64_env_parser_rejects_invalid_values` (function) component `positive_u64_env_parser_rejects_invalid_values [function]` (`4dadd1a6-e5a9-5733-8ff9-727835cf4023`) lines 251-257 [crates/gwiki/src/support/env.rs:251-257]
  - Signature: `fn positive_u64_env_parser_rejects_invalid_values() {`
  - Purpose: Indexed function `positive_u64_env_parser_rejects_invalid_values` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:251-257]
- `database_url_uses_gobby_broker_when_env_missing` (function) component `database_url_uses_gobby_broker_when_env_missing [function]` (`d5b21cc5-c6c1-530d-8aac-f21ed1660bd6`) lines 261-285 [crates/gwiki/src/support/env.rs:261-285]
  - Signature: `fn database_url_uses_gobby_broker_when_env_missing() {`
  - Purpose: Indexed function `database_url_uses_gobby_broker_when_env_missing` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:261-285]
- `database_url_broker_rejects_non_loopback_daemon_host` (function) component `database_url_broker_rejects_non_loopback_daemon_host [function]` (`6091d7ec-1fde-5e22-b8d8-76e452eb8ad4`) lines 288-297 [crates/gwiki/src/support/env.rs:288-297]
  - Signature: `fn database_url_broker_rejects_non_loopback_daemon_host() {`
  - Purpose: Indexed function `database_url_broker_rejects_non_loopback_daemon_host` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:288-297]
- `spawn_database_url_broker` (function) component `spawn_database_url_broker [function]` (`df1722b7-7ee6-534e-ae75-bd9bd50080e3`) lines 299-322 [crates/gwiki/src/support/env.rs:299-322]
  - Signature: `fn spawn_database_url_broker(`
  - Purpose: Indexed function `spawn_database_url_broker` in `crates/gwiki/src/support/env.rs`. [crates/gwiki/src/support/env.rs:299-322]

