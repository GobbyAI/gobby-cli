---
title: crates/gcode/src/commands/setup.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/setup.rs
  ranges:
  - 23-95
  - 97-100
  - 102-118
  - 120-166
  - 168-187
  - 189-202
  - 204-220
  - 222-288
  - 290-301
  - 303-306
  - 308-356
  - 358-377
  - 379-395
  - 403-481
  - 484-532
  - 535-550
  - 553-562
  - 573-610
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/setup.rs:23-95](crates/gcode/src/commands/setup.rs#L23-L95), [crates/gcode/src/commands/setup.rs:97-100](crates/gcode/src/commands/setup.rs#L97-L100), [crates/gcode/src/commands/setup.rs:102-118](crates/gcode/src/commands/setup.rs#L102-L118), [crates/gcode/src/commands/setup.rs:120-166](crates/gcode/src/commands/setup.rs#L120-L166), [crates/gcode/src/commands/setup.rs:168-187](crates/gcode/src/commands/setup.rs#L168-L187), [crates/gcode/src/commands/setup.rs:189-202](crates/gcode/src/commands/setup.rs#L189-L202), [crates/gcode/src/commands/setup.rs:204-220](crates/gcode/src/commands/setup.rs#L204-L220), [crates/gcode/src/commands/setup.rs:222-288](crates/gcode/src/commands/setup.rs#L222-L288), [crates/gcode/src/commands/setup.rs:290-301](crates/gcode/src/commands/setup.rs#L290-L301), [crates/gcode/src/commands/setup.rs:303-306](crates/gcode/src/commands/setup.rs#L303-L306), [crates/gcode/src/commands/setup.rs:308-356](crates/gcode/src/commands/setup.rs#L308-L356), [crates/gcode/src/commands/setup.rs:358-377](crates/gcode/src/commands/setup.rs#L358-L377), [crates/gcode/src/commands/setup.rs:379-395](crates/gcode/src/commands/setup.rs#L379-L395), [crates/gcode/src/commands/setup.rs:403-481](crates/gcode/src/commands/setup.rs#L403-L481), [crates/gcode/src/commands/setup.rs:484-532](crates/gcode/src/commands/setup.rs#L484-L532), [crates/gcode/src/commands/setup.rs:535-550](crates/gcode/src/commands/setup.rs#L535-L550), [crates/gcode/src/commands/setup.rs:553-562](crates/gcode/src/commands/setup.rs#L553-L562), [crates/gcode/src/commands/setup.rs:573-610](crates/gcode/src/commands/setup.rs#L573-L610)

</details>

# crates/gcode/src/commands/setup.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Implements the standalone `gcode` setup flow: it validates a setup request, applies service overrides, resolves embedding bootstrap and database provisioning, connects to Postgres, optionally clears existing overwrite projections, runs the underlying standalone setup, and then writes the generated `gcore` config and status output. The helper functions split that work into database resolution/retry, config generation and redaction of embedding keys, embedding bootstrap selection/cleanup, and endpoint reachability checks, while the `OverwriteProjectionConfigs` helper drives projection rewrites. The test functions cover embedding-provider alias handling, canonical provider acceptance, config emission for AI embeddings, and installation of the public code index subset in standalone mode.
[crates/gcode/src/commands/setup.rs:23-95]
[crates/gcode/src/commands/setup.rs:97-100]
[crates/gcode/src/commands/setup.rs:102-118]
[crates/gcode/src/commands/setup.rs:120-166]
[crates/gcode/src/commands/setup.rs:168-187]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run` | function | `pub fn run(request: StandaloneSetupRequest, format: Format, quiet: bool) -> anyhow::Result<()> {` | `run [function]` | `349bea47-d213-5230-9583-d7e4e9d98c65` | 23-95 [crates/gcode/src/commands/setup.rs:23-95] | Indexed function `run` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:23-95] |
| `OverwriteProjectionConfigs` | class | `struct OverwriteProjectionConfigs {` | `OverwriteProjectionConfigs [class]` | `d155f612-fa21-5e36-b686-be8363e98d2d` | 97-100 [crates/gcode/src/commands/setup.rs:97-100] | Indexed class `OverwriteProjectionConfigs` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:97-100] |
| `clear_overwrite_projections` | function | `fn clear_overwrite_projections(` | `clear_overwrite_projections [function]` | `f0f02929-5395-5eb5-940d-fd6aa02401a9` | 102-118 [crates/gcode/src/commands/setup.rs:102-118] | Indexed function `clear_overwrite_projections` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:102-118] |
| `overwrite_projection_configs` | function | `fn overwrite_projection_configs(` | `overwrite_projection_configs [function]` | `41d2e5b9-410e-527d-934d-7499fb299d64` | 120-166 [crates/gcode/src/commands/setup.rs:120-166] | Indexed function `overwrite_projection_configs` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:120-166] |
| `resolve_or_provision_database` | function | `fn resolve_or_provision_database(` | `resolve_or_provision_database [function]` | `e4079dd7-91e6-5bd9-9741-5bca385b3ce3` | 168-187 [crates/gcode/src/commands/setup.rs:168-187] | Indexed function `resolve_or_provision_database` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:168-187] |
| `apply_service_overrides` | function | `fn apply_service_overrides(` | `apply_service_overrides [function]` | `a7d8cbea-beb2-5dcc-8662-74b508acf56d` | 189-202 [crates/gcode/src/commands/setup.rs:189-202] | Indexed function `apply_service_overrides` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:189-202] |
| `connect_postgres_with_retry` | function | `fn connect_postgres_with_retry(database_url: &str, retry: bool) -> anyhow::Result<Client> {` | `connect_postgres_with_retry [function]` | `353329d9-2ae8-5604-86e1-fd9ee1c6d79f` | 204-220 [crates/gcode/src/commands/setup.rs:204-220] | Indexed function `connect_postgres_with_retry` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:204-220] |
| `write_gcore_config` | function | `fn write_gcore_config(` | `write_gcore_config [function]` | `a7579a9d-36e0-5fc5-a5d4-5bab01956c56` | 222-288 [crates/gcode/src/commands/setup.rs:222-288] | Indexed function `write_gcore_config` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:222-288] |
| `remove_embedding_keys` | function | `fn remove_embedding_keys(config: &mut StandaloneConfig) {` | `remove_embedding_keys [function]` | `4a07eeec-bf5a-5167-8efa-479b3d4e2ece` | 290-301 [crates/gcode/src/commands/setup.rs:290-301] | Indexed function `remove_embedding_keys` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:290-301] |
| `service_configured_compose_file` | function | `fn service_configured_compose_file(home: &std::path::Path) -> Option<String> {` | `service_configured_compose_file [function]` | `360203b3-5bb1-5fe7-9db9-1b9196d3948f` | 303-306 [crates/gcode/src/commands/setup.rs:303-306] | Indexed function `service_configured_compose_file` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:303-306] |
| `resolve_embedding_bootstrap` | function | `fn resolve_embedding_bootstrap(` | `resolve_embedding_bootstrap [function]` | `25756eae-fc65-58d4-82da-cf66fa17dd18` | 308-356 [crates/gcode/src/commands/setup.rs:308-356] | Indexed function `resolve_embedding_bootstrap` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:308-356] |
| `explicit_embedding_bootstrap` | function | `fn explicit_embedding_bootstrap(` | `explicit_embedding_bootstrap [function]` | `3c641824-0510-5ef2-a7c1-10ba448b82c7` | 358-377 [crates/gcode/src/commands/setup.rs:358-377] | Indexed function `explicit_embedding_bootstrap` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:358-377] |
| `endpoint_reachable` | function | `fn endpoint_reachable(api_base: &str) -> bool {` | `endpoint_reachable [function]` | `31179f2a-1ed0-5056-8b20-d8596d87cb24` | 379-395 [crates/gcode/src/commands/setup.rs:379-395] | Indexed function `endpoint_reachable` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:379-395] |
| `write_gcore_config_writes_ai_embeddings_and_redacts_api_key` | function | `fn write_gcore_config_writes_ai_embeddings_and_redacts_api_key() {` | `write_gcore_config_writes_ai_embeddings_and_redacts_api_key [function]` | `4d541fc0-5646-5008-9bbb-022661ddd341` | 403-481 [crates/gcode/src/commands/setup.rs:403-481] | Indexed function `write_gcore_config_writes_ai_embeddings_and_redacts_api_key` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:403-481] |
| `write_gcore_config_clears_embedding_keys_when_disabled` | function | `fn write_gcore_config_clears_embedding_keys_when_disabled() {` | `write_gcore_config_clears_embedding_keys_when_disabled [function]` | `ecd64a06-dd6f-5f6f-af19-3d852a6e05f1` | 484-532 [crates/gcode/src/commands/setup.rs:484-532] | Indexed function `write_gcore_config_clears_embedding_keys_when_disabled` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:484-532] |
| `setup_rejects_removed_embedding_provider_aliases` | function | `fn setup_rejects_removed_embedding_provider_aliases() {` | `setup_rejects_removed_embedding_provider_aliases [function]` | `e748aa27-42e5-5a74-8145-d4fbd688a9ad` | 535-550 [crates/gcode/src/commands/setup.rs:535-550] | Indexed function `setup_rejects_removed_embedding_provider_aliases` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:535-550] |
| `setup_accepts_canonical_lmstudio_embedding_provider` | function | `fn setup_accepts_canonical_lmstudio_embedding_provider() {` | `setup_accepts_canonical_lmstudio_embedding_provider [function]` | `d4bc16e1-fbb8-590c-86a3-9b1a72bc216c` | 553-562 [crates/gcode/src/commands/setup.rs:553-562] | Indexed function `setup_accepts_canonical_lmstudio_embedding_provider` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:553-562] |
| `standalone_command_installs_public_code_index_subset` | function | `fn standalone_command_installs_public_code_index_subset() {` | `standalone_command_installs_public_code_index_subset [function]` | `f8ed9755-4697-5a0b-af4f-50f3bed3206c` | 573-610 [crates/gcode/src/commands/setup.rs:573-610] | Indexed function `standalone_command_installs_public_code_index_subset` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:573-610] |
