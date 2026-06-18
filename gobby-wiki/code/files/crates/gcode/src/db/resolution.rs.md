---
title: crates/gcode/src/db/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/db/resolution.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db/resolution.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Overview

`crates/gcode/src/db/resolution.rs` exposes 55 indexed API symbols.

## How it fits

`crates/gcode/src/db/resolution.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `BrokerDatabaseUrlResponse` | class | Indexed class `BrokerDatabaseUrlResponse` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:16-18] |
| `BootstrapDatabase` | class | Indexed class `BootstrapDatabase` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:21-24] |
| `gobby_home` | function | Indexed function `gobby_home` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:27-29] |
| `bootstrap_path` | function | Indexed function `bootstrap_path` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:31-33] |
| `resolve_database_url` | function | Indexed function `resolve_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:39-48] |
| `resolve_database_url_from_sources` | function | Indexed function `resolve_database_url_from_sources` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:51-64] |
| `resolve_database_url_from_sources_with_identity` | function | Indexed function `resolve_database_url_from_sources_with_identity` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:67-81] |
| `resolve_database_url_from_sources_with_identity_and_reachability` | function | Indexed function `resolve_database_url_from_sources_with_identity_and_reachability` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:83-138] |
| `resolve_recorded_hub_database_url` | function | Indexed function `resolve_recorded_hub_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:140-156] |
| `resolve_database_url_from_bootstrap_file` | function | Indexed function `resolve_database_url_from_bootstrap_file` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:158-166] |
| `resolve_database_url_from_gcore_config` | function | Indexed function `resolve_database_url_from_gcore_config` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:168-175] |
| `resolve_database_url_from_env` | function | Indexed function `resolve_database_url_from_env` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:177-186] |
| `parse_bootstrap_database` | function | Indexed function `parse_bootstrap_database` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:188-211] |
| `resolve_database_url_from_bootstrap` | function | Indexed function `resolve_database_url_from_bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:213-226] |
| `non_empty_trimmed` | function | Indexed function `non_empty_trimmed` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:228-235] |
| `resolve_brokered_database_url_at` | function | Indexed function `resolve_brokered_database_url_at` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:237-244] |
| `read_local_cli_token_at` | function | Indexed function `read_local_cli_token_at` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:246-255] |
| `request_broker_database_url` | function | Indexed function `request_broker_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:257-280] |
| `broker_timeout` | function | Indexed function `broker_timeout` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:282-284] |
| `broker_timeout_from_env` | function | Indexed function `broker_timeout_from_env` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:286-300] |
| `validate_loopback_daemon_url` | function | Indexed function `validate_loopback_daemon_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:302-323] |
| `validate_broker_database_url` | function | Indexed function `validate_broker_database_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:325-353] |
| `bootstrap` | function | Indexed function `bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:362-367] |
| `database_url_env_prefers_gcode_specific_var` | function | Indexed function `database_url_env_prefers_gcode_specific_var` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:370-378] |
| `database_url_env_falls_back_to_gobby_postgres_dsn` | function | Indexed function `database_url_env_falls_back_to_gobby_postgres_dsn` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:381-388] |
| `database_url_env_ignores_empty_values` | function | Indexed function `database_url_env_ignores_empty_values` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:391-399] |
| `database_url_sources_prefer_env_over_daemon_broker` | function | Indexed function `database_url_sources_prefer_env_over_daemon_broker` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:402-417] |
| `database_url_sources_use_daemon_broker_after_env` | function | Indexed function `database_url_sources_use_daemon_broker_after_env` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:420-432] |
| `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable` | function | Indexed function `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:435-452] |
| `database_url_sources_use_gcore_after_daemon_and_bootstrap` | function | Indexed function `database_url_sources_use_gcore_after_daemon_and_bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:455-472] |
| `adopted_hub_resolves_without_conflict` | function | Indexed function `adopted_hub_resolves_without_conflict` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:475-500] |
| `postgres_bootstrap_accepts_inline_url` | function | Indexed function `postgres_bootstrap_accepts_inline_url` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:503-511] |
| `non_postgres_bootstrap_fails_clearly` | function | Indexed function `non_postgres_bootstrap_fails_clearly` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:514-521] |
| `missing_hub_backend_fails_clearly` | function | Indexed function `missing_hub_backend_fails_clearly` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:524-529] |
| `missing_postgres_dsn_fails_clearly` | function | Indexed function `missing_postgres_dsn_fails_clearly` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:532-537] |
| `parse_bootstrap_database_reads_postgres_fields` | function | Indexed function `parse_bootstrap_database_reads_postgres_fields` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:540-552] |
| `broker_request_returns_database_url_and_sends_local_token` | function | Indexed function `broker_request_returns_database_url_and_sends_local_token` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:555-572] |
| `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token` | function | Indexed function `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:575-583] |
| `broker_request_allows_cold_daemon_latency` | function | Indexed function `broker_request_allows_cold_daemon_latency` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:586-597] |
| `broker_timeout_defaults_to_seven_seconds` | function | Indexed function `broker_timeout_defaults_to_seven_seconds` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:600-604] |
| `broker_timeout_reads_positive_env_value` | function | Indexed function `broker_timeout_reads_positive_env_value` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:607-613] |
| `broker_timeout_ignores_invalid_env_value` | function | Indexed function `broker_timeout_ignores_invalid_env_value` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:616-622] |
| `broker_missing_token_fails` | function | Indexed function `broker_missing_token_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:625-633] |
| `broker_daemon_down_fails` | function | Indexed function `broker_daemon_down_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:636-648] |
| `broker_auth_failure_fails` | function | Indexed function `broker_auth_failure_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:651-665] |
| `broker_non_success_status_fails` | function | Indexed function `broker_non_success_status_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:668-682] |
| `broker_invalid_json_fails` | function | Indexed function `broker_invalid_json_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:685-696] |
| `broker_empty_database_url_fails` | function | Indexed function `broker_empty_database_url_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:699-711] |
| `broker_invalid_database_url_scheme_fails` | function | Indexed function `broker_invalid_database_url_scheme_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:714-722] |
| `broker_missing_database_url_host_fails` | function | Indexed function `broker_missing_database_url_host_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:725-733] |
| `broker_missing_database_url_path_fails` | function | Indexed function `broker_missing_database_url_path_fails` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:736-744] |
| `write_bootstrap` | function | Indexed function `write_bootstrap` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:746-754] |
| `http_response` | function | Indexed function `http_response` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:756-761] |
| `spawn_http_response` | function | Indexed function `spawn_http_response` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:763-765] |
| `spawn_http_response_after` | function | Indexed function `spawn_http_response_after` in `crates/gcode/src/db/resolution.rs`. [crates/gcode/src/db/resolution.rs:767-794] |

