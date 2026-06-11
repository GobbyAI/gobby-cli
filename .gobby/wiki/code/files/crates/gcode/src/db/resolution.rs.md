---
title: crates/gcode/src/db/resolution.rs
type: code_file
provenance:
- file: crates/gcode/src/db/resolution.rs
  ranges:
  - 16-18
  - 21-24
  - 27-29
  - 31-33
  - 39-48
  - 51-64
  - 67-81
  - 83-138
  - 140-156
  - 158-166
  - 168-175
  - 177-186
  - 188-211
  - 213-226
  - 228-235
  - 237-244
  - 246-255
  - 257-280
  - 282-284
  - 286-300
  - 302-323
  - 325-353
  - 362-367
  - 370-378
  - 381-388
  - 391-399
  - 402-417
  - 420-432
  - 435-452
  - 455-472
  - 475-500
  - 503-511
  - 514-521
  - 524-529
  - 532-537
  - 540-552
  - 555-572
  - 575-583
  - 586-597
  - 600-604
  - 607-613
  - 616-622
  - 625-633
  - 636-648
  - 651-665
  - 668-682
  - 685-696
  - 699-711
  - 714-722
  - 725-733
  - 736-744
  - 746-754
  - 756-761
  - 763-765
  - 767-794
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/db/resolution.rs

Module: [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]

## Purpose

`crates/gcode/src/db/resolution.rs` exposes 55 indexed API symbols.
[crates/gcode/src/db/resolution.rs:16-18]
[crates/gcode/src/db/resolution.rs:21-24]
[crates/gcode/src/db/resolution.rs:27-29]
[crates/gcode/src/db/resolution.rs:31-33]
[crates/gcode/src/db/resolution.rs:39-48]

## API Symbols

- `BrokerDatabaseUrlResponse` (class) component `BrokerDatabaseUrlResponse [class]` (`e1a47bd4-8488-57c2-b9f3-fe11f328e9ee`) lines 16-18 [crates/gcode/src/db/resolution.rs:16-18]
  - Signature: `struct BrokerDatabaseUrlResponse {`
  - Purpose: `BrokerDatabaseUrlResponse` is a struct that encapsulates a single `String` field holding a database URL returned by a broker. [crates/gcode/src/db/resolution.rs:16-18]
- `BootstrapDatabase` (class) component `BootstrapDatabase [class]` (`a4a8ec5f-8b7e-56f7-b7b0-98451701ff1b`) lines 21-24 [crates/gcode/src/db/resolution.rs:21-24]
  - Signature: `struct BootstrapDatabase {`
  - Purpose: `BootstrapDatabase` is a configuration struct that holds a required hub backend identifier and an optional database connection URL for initializing database connectivity. [crates/gcode/src/db/resolution.rs:21-24]
- `gobby_home` (function) component `gobby_home [function]` (`abf8feb8-2b7f-59c8-a22b-3b7b171bead7`) lines 27-29 [crates/gcode/src/db/resolution.rs:27-29]
  - Signature: `pub fn gobby_home() -> anyhow::Result<PathBuf> {`
  - Purpose: Delegates to `gobby_core::gobby_home()` to return the gobby home directory path as a `PathBuf` with error handling via `anyhow::Result`. [crates/gcode/src/db/resolution.rs:27-29]
- `bootstrap_path` (function) component `bootstrap_path [function]` (`2d5e07d4-698a-547c-9493-86b1404eb7f7`) lines 31-33 [crates/gcode/src/db/resolution.rs:31-33]
  - Signature: `pub fn bootstrap_path() -> anyhow::Result<PathBuf> {`
  - Purpose: Returns the file path to `bootstrap.yaml` located in the gobby home directory, propagating any errors from home directory resolution. [crates/gcode/src/db/resolution.rs:31-33]
- `resolve_database_url` (function) component `resolve_database_url [function]` (`62e0931c-0f59-5d70-aee0-e3a67f5cd70b`) lines 39-48 [crates/gcode/src/db/resolution.rs:39-48]
  - Signature: `pub fn resolve_database_url() -> anyhow::Result<String> {`
  - Purpose: Resolves a PostgreSQL database URL from multiple sources (environment variables and brokered bootstrap configurations) while validating connectivity and identity via readonly connection testing. [crates/gcode/src/db/resolution.rs:39-48]
- `resolve_database_url_from_sources` (function) component `resolve_database_url_from_sources [function]` (`2eb15708-e3e4-5511-80ba-28078ec3c819`) lines 51-64 [crates/gcode/src/db/resolution.rs:51-64]
  - Signature: `fn resolve_database_url_from_sources(`
  - Purpose: Resolves a database URL from multiple sources (home directory, broker resolver, environment variables, and reachability checks) by delegating to an underlying implementation with a default PostgreSQL hub identity prober. [crates/gcode/src/db/resolution.rs:51-64]
- `resolve_database_url_from_sources_with_identity` (function) component `resolve_database_url_from_sources_with_identity [function]` (`14f5c3a0-921c-5ad1-87ac-2cfcec180161`) lines 67-81 [crates/gcode/src/db/resolution.rs:67-81]
  - Signature: `fn resolve_database_url_from_sources_with_identity(`
  - Purpose: Resolves a database URL from multiple sources—broker configuration, environment variables, and home directory—validated through reachability checks and identity probing. [crates/gcode/src/db/resolution.rs:67-81]
- `resolve_database_url_from_sources_with_identity_and_reachability` (function) component `resolve_database_url_from_sources_with_identity_and_reachability [function]` (`195bd3ff-a7ef-5a63-91b1-ab7762b1edf9`) lines 83-138 [crates/gcode/src/db/resolution.rs:83-138]
  - Signature: `fn resolve_database_url_from_sources_with_identity_and_reachability(`
  - Purpose: # Summary

Resolves a PostgreSQL database URL by cascading through multiple sources in priority order (environment variable, gcore config, broker resolver, local bootstrap.yaml) with conditional identity and reachability validation applied to broker and bootstrap sources. [crates/gcode/src/db/resolution.rs:83-138]
- `resolve_recorded_hub_database_url` (function) component `resolve_recorded_hub_database_url [function]` (`5bc0cad3-9212-5aba-a753-cbefe56a1abf`) lines 140-156 [crates/gcode/src/db/resolution.rs:140-156]
  - Signature: `fn resolve_recorded_hub_database_url(`
  - Purpose: Resolves the hub database URL by validating reachability and identity of a recorded or candidate endpoint, returning the confirmed database URL or None. [crates/gcode/src/db/resolution.rs:140-156]
- `resolve_database_url_from_bootstrap_file` (function) component `resolve_database_url_from_bootstrap_file [function]` (`61681180-8d76-5562-94de-2dbce8c9144b`) lines 158-166 [crates/gcode/src/db/resolution.rs:158-166]
  - Signature: `fn resolve_database_url_from_bootstrap_file(path: &Path) -> anyhow::Result<Option<String>> {`
  - Purpose: Reads and parses a bootstrap configuration file at the given path and returns its resolved database URL, or `None` if the file does not exist. [crates/gcode/src/db/resolution.rs:158-166]
- `resolve_database_url_from_gcore_config` (function) component `resolve_database_url_from_gcore_config [function]` (`20fd61b6-3117-5b9a-93b0-14ff0ea8b39a`) lines 168-175 [crates/gcode/src/db/resolution.rs:168-175]
  - Signature: `fn resolve_database_url_from_gcore_config(home: &Path) -> anyhow::Result<Option<String>> {`
  - Purpose: Reads a gcore configuration file from the home directory and returns the trimmed PostgreSQL database source name (DSN) if present and non-empty, or None otherwise. [crates/gcode/src/db/resolution.rs:168-175]
- `resolve_database_url_from_env` (function) component `resolve_database_url_from_env [function]` (`4bd03715-17ec-5950-ae70-0671e91e616a`) lines 177-186 [crates/gcode/src/db/resolution.rs:177-186]
  - Signature: `fn resolve_database_url_from_env(`
  - Purpose: Resolves a database URL by sequentially checking two environment variables (GCODE_DATABASE_URL_ENV and GOBBY_POSTGRES_DSN_ENV), returning the first non-empty trimmed value encountered or None if neither is set. [crates/gcode/src/db/resolution.rs:177-186]
- `parse_bootstrap_database` (function) component `parse_bootstrap_database [function]` (`882e9b8a-ebab-5fab-97bf-5e32f701c6d8`) lines 188-211 [crates/gcode/src/db/resolution.rs:188-211]
  - Signature: `fn parse_bootstrap_database(contents: &str) -> anyhow::Result<BootstrapDatabase> {`
  - Purpose: Parses a YAML string into a BootstrapDatabase struct by validating the input is a mapping and extracting the required `hub_backend` and optional `database_url` fields. [crates/gcode/src/db/resolution.rs:188-211]
- `resolve_database_url_from_bootstrap` (function) component `resolve_database_url_from_bootstrap [function]` (`f05288c3-69df-520e-be0c-d278c7d01b7a`) lines 213-226 [crates/gcode/src/db/resolution.rs:213-226]
  - Signature: `fn resolve_database_url_from_bootstrap(bootstrap: &BootstrapDatabase) -> anyhow::Result<String> {`
  - Purpose: Extracts the database URL from bootstrap configuration after validating that PostgreSQL is configured as the hub backend, returning an error if either requirement is unmet. [crates/gcode/src/db/resolution.rs:213-226]
- `non_empty_trimmed` (function) component `non_empty_trimmed [function]` (`731e2901-3f38-57dc-bead-ea5470c45727`) lines 228-235 [crates/gcode/src/db/resolution.rs:228-235]
  - Signature: `fn non_empty_trimmed(value: Option<String>) -> Option<String> {`
  - Purpose: Converts an optional string to `Some(trimmed_string)` if non-empty after whitespace removal, otherwise returns `None`. [crates/gcode/src/db/resolution.rs:228-235]
- `resolve_brokered_database_url_at` (function) component `resolve_brokered_database_url_at [function]` (`b73be4b7-f3af-53af-ada1-32d201a0f27a`) lines 237-244 [crates/gcode/src/db/resolution.rs:237-244]
  - Signature: `fn resolve_brokered_database_url_at(`
  - Purpose: Resolves a brokered database URL by reading a local CLI token and making an authenticated request to the daemon derived from the bootstrap path. [crates/gcode/src/db/resolution.rs:237-244]
- `read_local_cli_token_at` (function) component `read_local_cli_token_at [function]` (`248d9efb-c1f7-5501-aec9-a1ea837a2d7a`) lines 246-255 [crates/gcode/src/db/resolution.rs:246-255]
  - Signature: `fn read_local_cli_token_at(gobby_home: &Path) -> anyhow::Result<String> {`
  - Purpose: Reads a whitespace-trimmed CLI token from a file in the gobby home directory, validating that the token is non-empty and returning an error if the file is missing or the token is empty. [crates/gcode/src/db/resolution.rs:246-255]
- `request_broker_database_url` (function) component `request_broker_database_url [function]` (`60cd637f-925d-5638-95af-884e02f0d7a7`) lines 257-280 [crates/gcode/src/db/resolution.rs:257-280]
  - Signature: `fn request_broker_database_url(daemon_url: &str, token: &str) -> anyhow::Result<String> {`
  - Purpose: Fetches and validates a database URL from a local broker daemon by sending an authenticated HTTP POST request with a security token, returning the URL or an error. [crates/gcode/src/db/resolution.rs:257-280]
- `broker_timeout` (function) component `broker_timeout [function]` (`34b739a1-8fa3-54dd-addd-24326b488f9f`) lines 282-284 [crates/gcode/src/db/resolution.rs:282-284]
  - Signature: `fn broker_timeout() -> Duration {`
  - Purpose: Returns a `Duration` for broker timeout by delegating to `broker_timeout_from_env` with a closure that reads environment variables. [crates/gcode/src/db/resolution.rs:282-284]
- `broker_timeout_from_env` (function) component `broker_timeout_from_env [function]` (`6635c09c-dd4b-5ac5-8026-f8ba7f8043c2`) lines 286-300 [crates/gcode/src/db/resolution.rs:286-300]
  - Signature: `fn broker_timeout_from_env(env: impl Fn(&str) -> Option<String>) -> Duration {`
  - Purpose: Parses a millisecond-valued broker timeout from an environment variable into a `Duration`, returning a default if the variable is absent or invalid. [crates/gcode/src/db/resolution.rs:286-300]
- `validate_loopback_daemon_url` (function) component `validate_loopback_daemon_url [function]` (`d3d7be68-0422-5599-a960-b776ca36e123`) lines 302-323 [crates/gcode/src/db/resolution.rs:302-323]
  - Signature: `fn validate_loopback_daemon_url(daemon_url: &str) -> anyhow::Result<()> {`
  - Purpose: Validates that a broker daemon URL parses correctly and resolves exclusively to loopback addresses. [crates/gcode/src/db/resolution.rs:302-323]
- `validate_broker_database_url` (function) component `validate_broker_database_url [function]` (`8170e4c7-35e6-5066-ba6d-4760164f2f5d`) lines 325-353 [crates/gcode/src/db/resolution.rs:325-353]
  - Signature: `fn validate_broker_database_url(database_url: &str) -> anyhow::Result<String> {`
  - Purpose: Validates that a broker-provided database URL contains a valid PostgreSQL scheme (postgres:// or postgresql://), a non-empty host component, and a non-empty database path. [crates/gcode/src/db/resolution.rs:325-353]
- `bootstrap` (function) component `bootstrap [function]` (`7928ce0e-d6f7-5d2f-aa5b-055adb4f1117`) lines 362-367 [crates/gcode/src/db/resolution.rs:362-367]
  - Signature: `fn bootstrap(hub_backend: &str, database_url: Option<&str>) -> BootstrapDatabase {`
  - Purpose: Instantiates a `BootstrapDatabase` struct by converting borrowed string slices into owned `String` types for the hub backend and optional database URL. [crates/gcode/src/db/resolution.rs:362-367]
- `database_url_env_prefers_gcode_specific_var` (function) component `database_url_env_prefers_gcode_specific_var [function]` (`ceb3e7e0-7825-55aa-8212-9c9f66a8acbc`) lines 370-378 [crates/gcode/src/db/resolution.rs:370-378]
  - Signature: `fn database_url_env_prefers_gcode_specific_var() {`
  - Purpose: This test verifies that `resolve_database_url_from_env` prioritizes the `GCODE_DATABASE_URL_ENV` variable over `GOBBY_POSTGRES_DSN_ENV` when resolving the database connection URL. [crates/gcode/src/db/resolution.rs:370-378]
- `database_url_env_falls_back_to_gobby_postgres_dsn` (function) component `database_url_env_falls_back_to_gobby_postgres_dsn [function]` (`1e9f51d8-920f-5189-a1eb-e676d4b4f0cc`) lines 381-388 [crates/gcode/src/db/resolution.rs:381-388]
  - Signature: `fn database_url_env_falls_back_to_gobby_postgres_dsn() {`
  - Purpose: This test asserts that `resolve_database_url_from_env` correctly returns the PostgreSQL DSN `'postgresql://gobby/db'` when the resolver maps `GOBBY_POSTGRES_DSN_ENV` to that value. [crates/gcode/src/db/resolution.rs:381-388]
- `database_url_env_ignores_empty_values` (function) component `database_url_env_ignores_empty_values [function]` (`d1770dc2-5349-54c4-97d0-ae0cb69585a7`) lines 391-399 [crates/gcode/src/db/resolution.rs:391-399]
  - Signature: `fn database_url_env_ignores_empty_values() {`
  - Purpose: Asserts that `resolve_database_url_from_env` returns `None` when database URL environment variables contain only whitespace characters. [crates/gcode/src/db/resolution.rs:391-399]
- `database_url_sources_prefer_env_over_daemon_broker` (function) component `database_url_sources_prefer_env_over_daemon_broker [function]` (`4c814114-0977-5503-82e1-8db30e783288`) lines 402-417 [crates/gcode/src/db/resolution.rs:402-417]
  - Signature: `fn database_url_sources_prefer_env_over_daemon_broker() {`
  - Purpose: This test verifies that `resolve_database_url_from_sources` prioritizes the GCODE_DATABASE_URL_ENV environment variable over daemon broker sources when resolving the database URL. [crates/gcode/src/db/resolution.rs:402-417]
- `database_url_sources_use_daemon_broker_after_env` (function) component `database_url_sources_use_daemon_broker_after_env [function]` (`8f222e02-ecf8-5cb3-98de-9d70a122e8e9`) lines 420-432 [crates/gcode/src/db/resolution.rs:420-432]
  - Signature: `fn database_url_sources_use_daemon_broker_after_env() {`
  - Purpose: Tests that `resolve_database_url_from_sources` correctly returns a PostgreSQL daemon broker database URL when the primary source resolver provides it. [crates/gcode/src/db/resolution.rs:420-432]
- `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable` (function) component `database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable [function]` (`693476f8-f3ce-5a0a-8ce0-f8dc4850f406`) lines 435-452 [crates/gcode/src/db/resolution.rs:435-452]
  - Signature: `fn database_url_sources_fall_back_to_bootstrap_inline_when_daemon_is_unavailable() {`
  - Purpose: Test verifying that `resolve_database_url_from_sources` falls back to extracting the database URL from a bootstrap.yaml configuration file when daemon resolution fails. [crates/gcode/src/db/resolution.rs:435-452]
- `database_url_sources_use_gcore_after_daemon_and_bootstrap` (function) component `database_url_sources_use_gcore_after_daemon_and_bootstrap [function]` (`05dc0ea7-ef9e-557a-bdbe-16f72a6914da`) lines 455-472 [crates/gcode/src/db/resolution.rs:455-472]
  - Signature: `fn database_url_sources_use_gcore_after_daemon_and_bootstrap() {`
  - Purpose: Unit test asserting that `resolve_database_url_from_sources` retrieves the PostgreSQL DSN from the gcore configuration file when daemon is unavailable and bootstrap resolution fails. [crates/gcode/src/db/resolution.rs:455-472]
- `adopted_hub_resolves_without_conflict` (function) component `adopted_hub_resolves_without_conflict [function]` (`bae371fd-bdce-5ca6-a0f3-ffddf4b8aa90`) lines 475-500 [crates/gcode/src/db/resolution.rs:475-500]
  - Signature: `fn adopted_hub_resolves_without_conflict() {`
  - Purpose: Tests that `resolve_database_url_from_sources_with_identity` correctly returns the configured PostgreSQL DSN when the hub identity is known, without conflicts between multiple resolution sources. [crates/gcode/src/db/resolution.rs:475-500]
- `postgres_bootstrap_accepts_inline_url` (function) component `postgres_bootstrap_accepts_inline_url [function]` (`e5fd214d-eb81-542e-bd5a-73eb0e17267b`) lines 503-511 [crates/gcode/src/db/resolution.rs:503-511]
  - Signature: `fn postgres_bootstrap_accepts_inline_url() {`
  - Purpose: This test verifies that `resolve_database_url_from_bootstrap` correctly accepts and returns an inline PostgreSQL database URL unchanged when passed through the bootstrap function. [crates/gcode/src/db/resolution.rs:503-511]
- `non_postgres_bootstrap_fails_clearly` (function) component `non_postgres_bootstrap_fails_clearly [function]` (`d372b49d-7b5b-5db2-94c7-a63dc6ba6eed`) lines 514-521 [crates/gcode/src/db/resolution.rs:514-521]
  - Signature: `fn non_postgres_bootstrap_fails_clearly() {`
  - Purpose: This test verifies that `resolve_database_url_from_bootstrap()` fails with a clear error message mentioning the required postgres backend and the attempted non-postgres backend ("local-file") when resolving a database URL. [crates/gcode/src/db/resolution.rs:514-521]
- `missing_hub_backend_fails_clearly` (function) component `missing_hub_backend_fails_clearly [function]` (`132008a8-f931-5acc-badf-e5d5d56063ff`) lines 524-529 [crates/gcode/src/db/resolution.rs:524-529]
  - Signature: `fn missing_hub_backend_fails_clearly() {`
  - Purpose: This function is a unit test that verifies `parse_bootstrap_database` fails with a clear error message containing "hub_backend: postgres" when the `hub_backend` field is missing from the bootstrap configuration. [crates/gcode/src/db/resolution.rs:524-529]
- `missing_postgres_dsn_fails_clearly` (function) component `missing_postgres_dsn_fails_clearly [function]` (`11114b11-3e11-59f1-b5b9-c42abd078123`) lines 532-537 [crates/gcode/src/db/resolution.rs:532-537]
  - Signature: `fn missing_postgres_dsn_fails_clearly() {`
  - Purpose: This function verifies that `resolve_database_url_from_bootstrap` fails with an error message containing "database_url" when attempting to resolve a PostgreSQL database configuration without a provided DSN. [crates/gcode/src/db/resolution.rs:532-537]
- `parse_bootstrap_database_reads_postgres_fields` (function) component `parse_bootstrap_database_reads_postgres_fields [function]` (`a8b6e9ea-2e1e-5ef1-9849-edad058c1246`) lines 540-552 [crates/gcode/src/db/resolution.rs:540-552]
  - Signature: `fn parse_bootstrap_database_reads_postgres_fields() {`
  - Purpose: Unit test verifying that `parse_bootstrap_database` correctly parses PostgreSQL backend and database URL fields from a bootstrap configuration string. [crates/gcode/src/db/resolution.rs:540-552]
- `broker_request_returns_database_url_and_sends_local_token` (function) component `broker_request_returns_database_url_and_sends_local_token [function]` (`edab86ee-085d-5f66-84f0-20d49facd6b4`) lines 555-572 [crates/gcode/src/db/resolution.rs:555-572]
  - Signature: `fn broker_request_returns_database_url_and_sends_local_token() {`
  - Purpose: Verifies that `request_broker_database_url` correctly sends a POST request with the `X-Gobby-Local-Token` header to the broker's database-url endpoint and parses the returned PostgreSQL connection string. [crates/gcode/src/db/resolution.rs:555-572]
- `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token` (function) component `broker_request_rejects_non_loopback_daemon_url_before_sending_local_token [function]` (`26510a28-69d3-5381-a2f8-5af92b456d41`) lines 575-583 [crates/gcode/src/db/resolution.rs:575-583]
  - Signature: `fn broker_request_rejects_non_loopback_daemon_url_before_sending_local_token() {`
  - Purpose: This test function verifies that `request_broker_database_url()` rejects non-loopback daemon URLs and returns an error indicating that the URL must resolve exclusively to loopback addresses. [crates/gcode/src/db/resolution.rs:575-583]
- `broker_request_allows_cold_daemon_latency` (function) component `broker_request_allows_cold_daemon_latency [function]` (`0d8e4e28-deab-5aec-95e8-01a57ddaf503`) lines 586-597 [crates/gcode/src/db/resolution.rs:586-597]
  - Signature: `fn broker_request_allows_cold_daemon_latency() {`
  - Purpose: Verifies that `request_broker_database_url` successfully resolves a PostgreSQL database URL despite the broker having a 1.1-second cold-start latency. [crates/gcode/src/db/resolution.rs:586-597]
- `broker_timeout_defaults_to_seven_seconds` (function) component `broker_timeout_defaults_to_seven_seconds [function]` (`f98ef5c5-95d9-5e2e-b4f4-835edf4ddf71`) lines 600-604 [crates/gcode/src/db/resolution.rs:600-604]
  - Signature: `fn broker_timeout_defaults_to_seven_seconds() {`
  - Purpose: This unit test verifies that `broker_timeout_from_env` returns a `Duration` of 7000 milliseconds when the environment variable lookup closure returns `None`. [crates/gcode/src/db/resolution.rs:600-604]
- `broker_timeout_reads_positive_env_value` (function) component `broker_timeout_reads_positive_env_value [function]` (`6c1402bd-165b-55d2-ae65-aaad2d1e713d`) lines 607-613 [crates/gcode/src/db/resolution.rs:607-613]
  - Signature: `fn broker_timeout_reads_positive_env_value() {`
  - Purpose: Tests that `broker_timeout_from_env` correctly parses a positive millisecond duration from the `GCODE_BROKER_TIMEOUT_MS_ENV` environment variable. [crates/gcode/src/db/resolution.rs:607-613]
- `broker_timeout_ignores_invalid_env_value` (function) component `broker_timeout_ignores_invalid_env_value [function]` (`ec03e1fa-d8fa-5dbd-91a9-0d72195a5d3f`) lines 616-622 [crates/gcode/src/db/resolution.rs:616-622]
  - Signature: `fn broker_timeout_ignores_invalid_env_value() {`
  - Purpose: Tests that `broker_timeout_from_env` rejects "0" as an invalid value for `GCODE_BROKER_TIMEOUT_MS_ENV` and falls back to `DEFAULT_BROKER_TIMEOUT`. [crates/gcode/src/db/resolution.rs:616-622]
- `broker_missing_token_fails` (function) component `broker_missing_token_fails [function]` (`b632aba3-0f0f-546e-9b2d-37b2c3b8f66d`) lines 625-633 [crates/gcode/src/db/resolution.rs:625-633]
  - Signature: `fn broker_missing_token_fails() {`
  - Purpose: This unit test verifies that `resolve_brokered_database_url_at` fails with an error message containing "missing local CLI token" when the required local authentication token is absent. [crates/gcode/src/db/resolution.rs:625-633]
- `broker_daemon_down_fails` (function) component `broker_daemon_down_fails [function]` (`f45f6c51-249a-54d8-b797-bef949997bdc`) lines 636-648 [crates/gcode/src/db/resolution.rs:636-648]
  - Signature: `fn broker_daemon_down_fails() {`
  - Purpose: Tests that `resolve_brokered_database_url_at` fails with a "database_url broker request failed" error when the broker daemon is unavailable. [crates/gcode/src/db/resolution.rs:636-648]
- `broker_auth_failure_fails` (function) component `broker_auth_failure_fails [function]` (`e52f4392-fd13-57b8-a8f5-bbbc74615199`) lines 651-665 [crates/gcode/src/db/resolution.rs:651-665]
  - Signature: `fn broker_auth_failure_fails() {`
  - Purpose: Tests that `request_broker_database_url` properly fails with an error message containing "database_url broker request failed" when the broker responds with a 401 Unauthorized status. [crates/gcode/src/db/resolution.rs:651-665]
- `broker_non_success_status_fails` (function) component `broker_non_success_status_fails [function]` (`45b2ab8a-3d84-5151-99ce-3ce3bd420638`) lines 668-682 [crates/gcode/src/db/resolution.rs:668-682]
  - Signature: `fn broker_non_success_status_fails() {`
  - Purpose: This test verifies that `request_broker_database_url` fails with the expected error message when the broker responds with a non-success HTTP status code (503 Service Unavailable). [crates/gcode/src/db/resolution.rs:668-682]
- `broker_invalid_json_fails` (function) component `broker_invalid_json_fails [function]` (`25cdbc95-780b-5f77-bf31-e6287089462c`) lines 685-696 [crates/gcode/src/db/resolution.rs:685-696]
  - Signature: `fn broker_invalid_json_fails() {`
  - Purpose: Tests that `request_broker_database_url` properly fails and reports the expected error when the broker responds with a 200 OK status containing non-JSON data. [crates/gcode/src/db/resolution.rs:685-696]
- `broker_empty_database_url_fails` (function) component `broker_empty_database_url_fails [function]` (`4fc29167-b0a8-53df-b8fc-44c629729d14`) lines 699-711 [crates/gcode/src/db/resolution.rs:699-711]
  - Signature: `fn broker_empty_database_url_fails() {`
  - Purpose: This unit test asserts that `request_broker_database_url` returns an error containing "database_url broker response was empty" when the broker endpoint returns a JSON response with a whitespace-only database_url field. [crates/gcode/src/db/resolution.rs:699-711]
- `broker_invalid_database_url_scheme_fails` (function) component `broker_invalid_database_url_scheme_fails [function]` (`bfa5b0f2-1d34-5f63-a9fe-c1c5ebb469e3`) lines 714-722 [crates/gcode/src/db/resolution.rs:714-722]
  - Signature: `fn broker_invalid_database_url_scheme_fails() {`
  - Purpose: This unit test verifies that `validate_broker_database_url` rejects database URLs with non-PostgreSQL schemes and returns an error message specifying that only `postgres://` or `postgresql://` schemes are valid. [crates/gcode/src/db/resolution.rs:714-722]
- `broker_missing_database_url_host_fails` (function) component `broker_missing_database_url_host_fails [function]` (`66b42ab9-dfe6-5365-b098-6acb7cdbd1f4`) lines 725-733 [crates/gcode/src/db/resolution.rs:725-733]
  - Signature: `fn broker_missing_database_url_host_fails() {`
  - Purpose: This test validates that `validate_broker_database_url` fails when given a PostgreSQL connection string without a host, returning an error message specifying the missing host requirement. [crates/gcode/src/db/resolution.rs:725-733]
- `broker_missing_database_url_path_fails` (function) component `broker_missing_database_url_path_fails [function]` (`f06db841-f4c0-57ef-9705-213dc8e0de68`) lines 736-744 [crates/gcode/src/db/resolution.rs:736-744]
  - Signature: `fn broker_missing_database_url_path_fails() {`
  - Purpose: This test verifies that `validate_broker_database_url` rejects a PostgreSQL broker connection string lacking a database path and returns an error message containing "database_url broker response must include a database path". [crates/gcode/src/db/resolution.rs:736-744]
- `write_bootstrap` (function) component `write_bootstrap [function]` (`cb84ebd0-8819-571a-9d40-0c4a16c14575`) lines 746-754 [crates/gcode/src/db/resolution.rs:746-754]
  - Signature: `fn write_bootstrap(home: &Path, daemon_port: u16) -> PathBuf {`
  - Purpose: Creates and writes a `bootstrap.yaml` configuration file to the home directory with postgres backend settings and the specified daemon port, returning the resulting `PathBuf`. [crates/gcode/src/db/resolution.rs:746-754]
- `http_response` (function) component `http_response [function]` (`003ca858-885e-50ea-9283-6e4808dc4473`) lines 756-761 [crates/gcode/src/db/resolution.rs:756-761]
  - Signature: `fn http_response(status: &str, body: &str) -> String {`
  - Purpose: Constructs an HTTP/1.1 response string with the given status code and body, including JSON content-type, content-length, and connection-close headers. [crates/gcode/src/db/resolution.rs:756-761]
- `spawn_http_response` (function) component `spawn_http_response [function]` (`f1d75b29-ef41-5e51-89d2-c8d5e1aa70fd`) lines 763-765 [crates/gcode/src/db/resolution.rs:763-765]
  - Signature: `fn spawn_http_response(response: String) -> (String, thread::JoinHandle<String>) {`
  - Purpose: Spawns an HTTP response on a new thread with zero delay, returning a tuple containing the response string and its associated `JoinHandle`. [crates/gcode/src/db/resolution.rs:763-765]
- `spawn_http_response_after` (function) component `spawn_http_response_after [function]` (`8d052b0a-d623-5bc9-beda-f07d7d3f786a`) lines 767-794 [crates/gcode/src/db/resolution.rs:767-794]
  - Signature: `fn spawn_http_response_after(`
  - Purpose: Spawns a single-request TCP server on localhost that accepts an HTTP request, delays by a specified duration, sends a fixed response, and returns the server URL and a JoinHandle yielding the received request. [crates/gcode/src/db/resolution.rs:767-794]

