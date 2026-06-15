---
title: crates/gwiki/src/commands/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/setup.rs
  ranges:
  - '18'
  - 20-92
  - 94-111
  - 113-123
  - 125-127
  - 129-180
  - 182-198
  - 200-233
  - 235-242
  - 244-248
  - 250-276
  - 278-292
  - 302-310
  - 313-355
  - 358-386
  - 389-412
  - 415-434
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/setup.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `gwiki setup` command: it resolves the requested scope, gathers Postgres object metadata, and either runs a normal Postgres setup or, in standalone mode, validates embedding settings, provisions or reuses services, merges database and service credentials into gCore config, and reports the result as a `CommandOutcome` or `WikiError`. The helper functions break that flow into pieces for service overrides, home-path lookup, config writing, service diagnostics, embedding validation, error conversion, status classification, and final rendering, with tests covering config merging and status behavior.
[crates/gwiki/src/commands/setup.rs:18]
[crates/gwiki/src/commands/setup.rs:20-92]
[crates/gwiki/src/commands/setup.rs:94-111]
[crates/gwiki/src/commands/setup.rs:113-123]
[crates/gwiki/src/commands/setup.rs:125-127]

## API Symbols

- `PostgresSetupResult` (type) component `PostgresSetupResult [type]` (`58c58e25-9dd3-5e0a-abcb-cc1752f3aea7`) lines 18-18 [crates/gwiki/src/commands/setup.rs:18]
  - Signature: `type PostgresSetupResult = (Vec<String>, Vec<String>, Vec<(String, String)>);`
  - Purpose: Indexed type `PostgresSetupResult` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:18]
- `execute` (function) component `execute [function]` (`23fa4ad1-0818-57b6-9aad-f22e75ebe5c7`) lines 20-92 [crates/gwiki/src/commands/setup.rs:20-92]
  - Signature: `pub(crate) fn execute(`
  - Purpose: 'execute' resolves the requested scope, prepares Postgres object metadata, conditionally validates standalone embedding settings, selects or provisions a database URL/service environment, runs the GWiki Postgres setup, and returns the resulting 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/setup.rs:20-92]
- `run_gwiki_postgres_setup` (function) component `run_gwiki_postgres_setup [function]` (`6c9c3ed4-350d-50e4-9cc1-f37a77bee11a`) lines 94-111 [crates/gwiki/src/commands/setup.rs:94-111]
  - Signature: `fn run_gwiki_postgres_setup(`
  - Purpose: Connects to the PostgreSQL database in read-write mode, builds a non-interactive 'SetupContext' with that client, runs 'StandaloneSetup::create', and returns the created/skipped/failed counts as 'PostgresSetupResult', mapping connection or setup errors into 'WikiError'. [crates/gwiki/src/commands/setup.rs:94-111]
- `apply_service_overrides` (function) component `apply_service_overrides [function]` (`d27fca9a-b375-5fc4-97cf-e208bbfd7b6e`) lines 113-123 [crates/gwiki/src/commands/setup.rs:113-123]
  - Signature: `fn apply_service_overrides(options: &SetupOptions, service_options: &mut DockerServiceOptions) {`
  - Purpose: 'apply_service_overrides' copies any present 'falkordb_host', 'falkordb_port', and 'falkordb_password' values from 'SetupOptions' into the mutable 'DockerServiceOptions', overwriting the corresponding service fields only when each option is set. [crates/gwiki/src/commands/setup.rs:113-123]
- `gobby_home` (function) component `gobby_home [function]` (`552f3deb-def6-55fd-b7dc-8200d700b354`) lines 125-127 [crates/gwiki/src/commands/setup.rs:125-127]
  - Signature: `fn gobby_home() -> anyhow::Result<PathBuf> {`
  - Purpose: Returns the gobby home directory path as a `PathBuf` or an error by delegating to `gobby_core::gobby_home()`. [crates/gwiki/src/commands/setup.rs:125-127]
- `write_gwiki_gcore_config` (function) component `write_gwiki_gcore_config [function]` (`c1999cf9-629a-5bf9-9af1-c045a8fe9f11`) lines 129-180 [crates/gwiki/src/commands/setup.rs:129-180]
  - Signature: `fn write_gwiki_gcore_config(`
  - Purpose: Generates a gCore configuration file by merging PostgreSQL and database service credentials from Docker provisioning results or explicit setup options, validates it, and persists to disk. [crates/gwiki/src/commands/setup.rs:129-180]
- `diagnose_required_service_config` (function) component `diagnose_required_service_config [function]` (`4434861f-627d-5966-9e9c-5e58f2596f3f`) lines 182-198 [crates/gwiki/src/commands/setup.rs:182-198]
  - Signature: `fn diagnose_required_service_config(config: &mut StandaloneConfig) {`
  - Purpose: Logs warnings when a 'StandaloneConfig' lacks a resolvable FalkorDB configuration or a non-empty Qdrant URL, indicating graph and semantic functionality are unavailable until those services are configured. [crates/gwiki/src/commands/setup.rs:182-198]
- `apply_embedding_options` (function) component `apply_embedding_options [function]` (`9dfee5d3-21df-5e6e-b378-2446560efaad`) lines 200-233 [crates/gwiki/src/commands/setup.rs:200-233]
  - Signature: `fn apply_embedding_options(`
  - Purpose: 'apply_embedding_options' validates the requested embedding vector dimension, no-ops if no embedding-related CLI options are set, and otherwise copies each provided embedding setting from 'SetupOptions' into the 'StandaloneConfig' under the corresponding AI config keys. [crates/gwiki/src/commands/setup.rs:200-233]
- `validate_embedding_vector_dim` (function) component `validate_embedding_vector_dim [function]` (`2c60d4a1-a51c-5ac7-acaa-8a5839bbce9d`) lines 235-242 [crates/gwiki/src/commands/setup.rs:235-242]
  - Signature: `fn validate_embedding_vector_dim(options: &SetupOptions) -> anyhow::Result<()> {`
  - Purpose: Validates that if `embedding_vector_dim` is specified in `SetupOptions`, its value falls within the inclusive range [1, 8192], returning an `anyhow::Error` otherwise. [crates/gwiki/src/commands/setup.rs:235-242]
- `standalone_error` (function) component `standalone_error [function]` (`1492fadb-06b1-5554-b791-8c601da623c3`) lines 244-248 [crates/gwiki/src/commands/setup.rs:244-248]
  - Signature: `fn standalone_error(error: anyhow::Error) -> WikiError {`
  - Purpose: This function converts an `anyhow::Error` into a `WikiError::Config` variant with a formatted error message indicating that standalone gwiki initialization failed. [crates/gwiki/src/commands/setup.rs:244-248]
- `render` (function) component `render [function]` (`13a6b729-6d0e-504a-b649-1571e4d545c9`) lines 250-276 [crates/gwiki/src/commands/setup.rs:250-276]
  - Signature: `fn render(`
  - Purpose: Returns a `CommandOutcome` by packaging setup operation metadata (scope, status, objects, results, ownership) into JSON and formatted text representations via a scoped outcome handler. [crates/gwiki/src/commands/setup.rs:250-276]
- `setup_status` (function) component `setup_status [function]` (`05cad23c-54b4-54fa-91b3-526bd8c1fdfb`) lines 278-292 [crates/gwiki/src/commands/setup.rs:278-292]
  - Signature: `fn setup_status(`
  - Purpose: `setup_status` returns a static status string based on priority-ordered evaluation of operation results, returning "failed" if any failures occurred, otherwise "created", "already_present", or "ready" depending on which operation type has non-empty results. [crates/gwiki/src/commands/setup.rs:278-292]
- `setup_status_reports_specific_outcome` (function) component `setup_status_reports_specific_outcome [function]` (`b5cb35d8-a1d4-57e3-8763-5a390ddaa261`) lines 302-310 [crates/gwiki/src/commands/setup.rs:302-310]
  - Signature: `fn setup_status_reports_specific_outcome() {`
  - Purpose: Asserts that 'setup_status' maps the given input cases to the expected outcomes: 'failed' for a bad specific-outcome entry, 'created' when a created item is present, 'already_present' when an existing item is present, and 'ready' when all inputs are empty. [crates/gwiki/src/commands/setup.rs:302-310]
- `standalone_provisions_and_merges_config` (function) component `standalone_provisions_and_merges_config [function]` (`3e2348b2-edf7-5cca-878f-b9bb05fadeb2`) lines 313-355 [crates/gwiki/src/commands/setup.rs:313-355]
  - Signature: `fn standalone_provisions_and_merges_config() {`
  - Purpose: Tests that `write_gwiki_gcore_config` properly merges PostgreSQL, FalkorDB, and Qdrant configurations into an existing `StandaloneConfig` while preserving pre-existing configuration values. [crates/gwiki/src/commands/setup.rs:313-355]
- `reuses_existing_gcode_hub` (function) component `reuses_existing_gcode_hub [function]` (`b20568e3-65c8-58ca-aaab-745cc9d50a43`) lines 358-386 [crates/gwiki/src/commands/setup.rs:358-386]
  - Signature: `fn reuses_existing_gcode_hub() {`
  - Purpose: This test verifies that `write_gwiki_gcore_config` preserves pre-existing database configuration values (PostgreSQL DSN and code index schema) when merging gwiki configuration rather than overwriting them. [crates/gwiki/src/commands/setup.rs:358-386]
- `standalone_config_can_record_postgres_before_required_services` (function) component `standalone_config_can_record_postgres_before_required_services [function]` (`50bca861-ad6d-59b7-ad81-350556f95298`) lines 389-412 [crates/gwiki/src/commands/setup.rs:389-412]
  - Signature: `fn standalone_config_can_record_postgres_before_required_services() {`
  - Purpose: This test verifies that a gcore `StandaloneConfig` can successfully write and read a PostgreSQL datasource connection string while excluding graph (FalkorDB) and vector (Qdrant) database configurations. [crates/gwiki/src/commands/setup.rs:389-412]
- `invalid_embedding_dim_does_not_mutate_config` (function) component `invalid_embedding_dim_does_not_mutate_config [function]` (`75736b33-eab2-5e7c-8cfb-60fe2073aacc`) lines 415-434 [crates/gwiki/src/commands/setup.rs:415-434]
  - Signature: `fn invalid_embedding_dim_does_not_mutate_config() {`
  - Purpose: This test verifies that `apply_embedding_options` rejects embedding vector dimensions outside the valid range [1, 8192] and does not mutate the configuration upon validation failure. [crates/gwiki/src/commands/setup.rs:415-434]

