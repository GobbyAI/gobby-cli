---
title: crates/gcode/src/commands/setup.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/setup.rs
  ranges:
  - 22-94
  - 96-99
  - 101-117
  - 119-165
  - 167-186
  - 188-201
  - 203-219
  - 221-283
  - 285-296
  - 298-301
  - 303-351
  - 353-372
  - 374-390
  - 398-460
  - 463-511
  - 514-529
  - 532-541
  - 548-586
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/setup.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/setup.rs` exposes 18 indexed API symbols.
[crates/gcode/src/commands/setup.rs:22-94]
[crates/gcode/src/commands/setup.rs:96-99]
[crates/gcode/src/commands/setup.rs:101-117]
[crates/gcode/src/commands/setup.rs:119-165]
[crates/gcode/src/commands/setup.rs:167-186]
[crates/gcode/src/commands/setup.rs:188-201]
[crates/gcode/src/commands/setup.rs:203-219]
[crates/gcode/src/commands/setup.rs:221-283]
[crates/gcode/src/commands/setup.rs:285-296]
[crates/gcode/src/commands/setup.rs:298-301]
[crates/gcode/src/commands/setup.rs:303-351]
[crates/gcode/src/commands/setup.rs:353-372]
[crates/gcode/src/commands/setup.rs:374-390]
[crates/gcode/src/commands/setup.rs:398-460]
[crates/gcode/src/commands/setup.rs:463-511]
[crates/gcode/src/commands/setup.rs:514-529]
[crates/gcode/src/commands/setup.rs:532-541]
[crates/gcode/src/commands/setup.rs:548-586]

## API Symbols

- `run` (function) component `run [function]` (`9dc50e8d-0c99-53b3-a7ae-4d010ee7bfd6`) lines 22-94 [crates/gcode/src/commands/setup.rs:22-94]
  - Signature: `pub fn run(request: StandaloneSetupRequest, format: Format, quiet: bool) -> anyhow::Result<()> {`
  - Purpose: Indexed function `run` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:22-94]
- `OverwriteProjectionConfigs` (class) component `OverwriteProjectionConfigs [class]` (`1059a619-b0f5-53ff-b42c-12e3ad77c4f5`) lines 96-99 [crates/gcode/src/commands/setup.rs:96-99]
  - Signature: `struct OverwriteProjectionConfigs {`
  - Purpose: Indexed class `OverwriteProjectionConfigs` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:96-99]
- `clear_overwrite_projections` (function) component `clear_overwrite_projections [function]` (`b75a2915-26c4-5465-93ad-03f319e7ddd8`) lines 101-117 [crates/gcode/src/commands/setup.rs:101-117]
  - Signature: `fn clear_overwrite_projections(`
  - Purpose: Indexed function `clear_overwrite_projections` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:101-117]
- `overwrite_projection_configs` (function) component `overwrite_projection_configs [function]` (`a3e3ae09-6903-5d40-8127-08436c0b2173`) lines 119-165 [crates/gcode/src/commands/setup.rs:119-165]
  - Signature: `fn overwrite_projection_configs(`
  - Purpose: Indexed function `overwrite_projection_configs` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:119-165]
- `resolve_or_provision_database` (function) component `resolve_or_provision_database [function]` (`bbcfa564-c3ab-5959-b8d3-59ba484d1857`) lines 167-186 [crates/gcode/src/commands/setup.rs:167-186]
  - Signature: `fn resolve_or_provision_database(`
  - Purpose: Indexed function `resolve_or_provision_database` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:167-186]
- `apply_service_overrides` (function) component `apply_service_overrides [function]` (`bb0421c5-16f5-5db4-afd9-fa6a38aae8ae`) lines 188-201 [crates/gcode/src/commands/setup.rs:188-201]
  - Signature: `fn apply_service_overrides(`
  - Purpose: Indexed function `apply_service_overrides` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:188-201]
- `connect_postgres_with_retry` (function) component `connect_postgres_with_retry [function]` (`c906be44-d257-515c-a451-591115c32c89`) lines 203-219 [crates/gcode/src/commands/setup.rs:203-219]
  - Signature: `fn connect_postgres_with_retry(database_url: &str, retry: bool) -> anyhow::Result<Client> {`
  - Purpose: Indexed function `connect_postgres_with_retry` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:203-219]
- `write_gcore_config` (function) component `write_gcore_config [function]` (`902bec0d-7426-5a01-8728-1e22bd8aaf74`) lines 221-283 [crates/gcode/src/commands/setup.rs:221-283]
  - Signature: `fn write_gcore_config(`
  - Purpose: Indexed function `write_gcore_config` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:221-283]
- `remove_embedding_keys` (function) component `remove_embedding_keys [function]` (`be627624-6381-5faa-8220-44f4cff9b592`) lines 285-296 [crates/gcode/src/commands/setup.rs:285-296]
  - Signature: `fn remove_embedding_keys(config: &mut StandaloneConfig) {`
  - Purpose: Indexed function `remove_embedding_keys` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:285-296]
- `service_configured_compose_file` (function) component `service_configured_compose_file [function]` (`0f6a5297-78c8-5929-9e16-88fa9130caa2`) lines 298-301 [crates/gcode/src/commands/setup.rs:298-301]
  - Signature: `fn service_configured_compose_file(home: &std::path::Path) -> Option<String> {`
  - Purpose: Indexed function `service_configured_compose_file` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:298-301]
- `resolve_embedding_bootstrap` (function) component `resolve_embedding_bootstrap [function]` (`a2b563fb-1353-5cfd-a555-7cfc7760f498`) lines 303-351 [crates/gcode/src/commands/setup.rs:303-351]
  - Signature: `fn resolve_embedding_bootstrap(`
  - Purpose: Indexed function `resolve_embedding_bootstrap` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:303-351]
- `explicit_embedding_bootstrap` (function) component `explicit_embedding_bootstrap [function]` (`68d3e471-bb90-5c9e-8b50-bab88333cd79`) lines 353-372 [crates/gcode/src/commands/setup.rs:353-372]
  - Signature: `fn explicit_embedding_bootstrap(`
  - Purpose: Indexed function `explicit_embedding_bootstrap` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:353-372]
- `endpoint_reachable` (function) component `endpoint_reachable [function]` (`2933a9f0-52c1-5a35-8bee-31fada2cbe16`) lines 374-390 [crates/gcode/src/commands/setup.rs:374-390]
  - Signature: `fn endpoint_reachable(api_base: &str) -> bool {`
  - Purpose: Indexed function `endpoint_reachable` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:374-390]
- `write_gcore_config_writes_ai_embeddings_and_redacts_api_key` (function) component `write_gcore_config_writes_ai_embeddings_and_redacts_api_key [function]` (`4d1b94d5-3619-577b-a813-717625cce318`) lines 398-460 [crates/gcode/src/commands/setup.rs:398-460]
  - Signature: `fn write_gcore_config_writes_ai_embeddings_and_redacts_api_key() {`
  - Purpose: Indexed function `write_gcore_config_writes_ai_embeddings_and_redacts_api_key` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:398-460]
- `write_gcore_config_clears_embedding_keys_when_disabled` (function) component `write_gcore_config_clears_embedding_keys_when_disabled [function]` (`49e02074-3acf-5878-a323-7e8bfa745289`) lines 463-511 [crates/gcode/src/commands/setup.rs:463-511]
  - Signature: `fn write_gcore_config_clears_embedding_keys_when_disabled() {`
  - Purpose: Indexed function `write_gcore_config_clears_embedding_keys_when_disabled` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:463-511]
- `setup_rejects_removed_embedding_provider_aliases` (function) component `setup_rejects_removed_embedding_provider_aliases [function]` (`81c55b98-d81d-58d0-910a-91cb16f08e63`) lines 514-529 [crates/gcode/src/commands/setup.rs:514-529]
  - Signature: `fn setup_rejects_removed_embedding_provider_aliases() {`
  - Purpose: Indexed function `setup_rejects_removed_embedding_provider_aliases` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:514-529]
- `setup_accepts_canonical_lmstudio_embedding_provider` (function) component `setup_accepts_canonical_lmstudio_embedding_provider [function]` (`7718a632-c78d-5e34-b22b-3f2a2f888dd4`) lines 532-541 [crates/gcode/src/commands/setup.rs:532-541]
  - Signature: `fn setup_accepts_canonical_lmstudio_embedding_provider() {`
  - Purpose: Indexed function `setup_accepts_canonical_lmstudio_embedding_provider` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:532-541]
- `standalone_command_installs_public_code_index_subset` (function) component `standalone_command_installs_public_code_index_subset [function]` (`83461f9c-ad94-50d1-ad3a-20e14c62b73d`) lines 548-586 [crates/gcode/src/commands/setup.rs:548-586]
  - Signature: `fn standalone_command_installs_public_code_index_subset() {`
  - Purpose: Indexed function `standalone_command_installs_public_code_index_subset` in `crates/gcode/src/commands/setup.rs`. [crates/gcode/src/commands/setup.rs:548-586]

