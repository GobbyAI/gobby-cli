---
title: crates/gwiki/src/commands/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/setup.rs
  ranges:
  - '19'
  - 21-93
  - 95-112
  - 114-124
  - 126-128
  - 130-181
  - 183-199
  - 201-244
  - 246-253
  - 255-259
  - 261-287
  - 289-303
  - 313-321
  - 324-366
  - 369-397
  - 400-423
  - 426-445
  - 448-478
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/setup.rs:19](crates/gwiki/src/commands/setup.rs#L19), [crates/gwiki/src/commands/setup.rs:21-93](crates/gwiki/src/commands/setup.rs#L21-L93), [crates/gwiki/src/commands/setup.rs:95-112](crates/gwiki/src/commands/setup.rs#L95-L112), [crates/gwiki/src/commands/setup.rs:114-124](crates/gwiki/src/commands/setup.rs#L114-L124), [crates/gwiki/src/commands/setup.rs:126-128](crates/gwiki/src/commands/setup.rs#L126-L128), [crates/gwiki/src/commands/setup.rs:130-181](crates/gwiki/src/commands/setup.rs#L130-L181), [crates/gwiki/src/commands/setup.rs:183-199](crates/gwiki/src/commands/setup.rs#L183-L199), [crates/gwiki/src/commands/setup.rs:201-244](crates/gwiki/src/commands/setup.rs#L201-L244), [crates/gwiki/src/commands/setup.rs:246-253](crates/gwiki/src/commands/setup.rs#L246-L253), [crates/gwiki/src/commands/setup.rs:255-259](crates/gwiki/src/commands/setup.rs#L255-L259), [crates/gwiki/src/commands/setup.rs:261-287](crates/gwiki/src/commands/setup.rs#L261-L287), [crates/gwiki/src/commands/setup.rs:289-303](crates/gwiki/src/commands/setup.rs#L289-L303), [crates/gwiki/src/commands/setup.rs:313-321](crates/gwiki/src/commands/setup.rs#L313-L321), [crates/gwiki/src/commands/setup.rs:324-366](crates/gwiki/src/commands/setup.rs#L324-L366), [crates/gwiki/src/commands/setup.rs:369-397](crates/gwiki/src/commands/setup.rs#L369-L397), [crates/gwiki/src/commands/setup.rs:400-423](crates/gwiki/src/commands/setup.rs#L400-L423), [crates/gwiki/src/commands/setup.rs:426-445](crates/gwiki/src/commands/setup.rs#L426-L445), [crates/gwiki/src/commands/setup.rs:448-478](crates/gwiki/src/commands/setup.rs#L448-L478)

</details>

# crates/gwiki/src/commands/setup.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki setup` command, resolving the requested scope, discovering Postgres-backed objects, and then either provisioning a standalone Docker-based setup or using an attached database URL. The helpers split the work into configuration and validation steps: service overrides and embedding options are applied to the provisioning inputs, `write_gwiki_gcore_config` and `apply_text_generation_bootstrap` persist the merged runtime config, `run_gwiki_postgres_setup` handles Postgres setup, `setup_status` and `render` format the result, and the tests cover status reporting, config merging, reuse of existing hub services, and validation failures.
[crates/gwiki/src/commands/setup.rs:19]
[crates/gwiki/src/commands/setup.rs:21-93]
[crates/gwiki/src/commands/setup.rs:95-112]
[crates/gwiki/src/commands/setup.rs:114-124]
[crates/gwiki/src/commands/setup.rs:126-128]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `PostgresSetupResult` | type | `type PostgresSetupResult = (Vec<String>, Vec<String>, Vec<(String, String)>);` | `PostgresSetupResult [type]` | `7acb0a5b-acb9-5dd2-962d-c4a4c72a63e0` | 19-19 [crates/gwiki/src/commands/setup.rs:19] | Indexed type `PostgresSetupResult` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:19] |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `8ecfc8de-7d76-5c31-99ae-73ac1b3a21db` | 21-93 [crates/gwiki/src/commands/setup.rs:21-93] | Indexed function `execute` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:21-93] |
| `run_gwiki_postgres_setup` | function | `fn run_gwiki_postgres_setup(` | `run_gwiki_postgres_setup [function]` | `d93824ca-3b48-5c15-ace3-a1dbcc3702ac` | 95-112 [crates/gwiki/src/commands/setup.rs:95-112] | Indexed function `run_gwiki_postgres_setup` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:95-112] |
| `apply_service_overrides` | function | `fn apply_service_overrides(options: &SetupOptions, service_options: &mut DockerServiceOptions) {` | `apply_service_overrides [function]` | `54aad1e4-1319-545e-859e-968303b3210f` | 114-124 [crates/gwiki/src/commands/setup.rs:114-124] | Indexed function `apply_service_overrides` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:114-124] |
| `gobby_home` | function | `fn gobby_home() -> anyhow::Result<PathBuf> {` | `gobby_home [function]` | `16bcbc51-ac86-5f95-9b54-c7886096438a` | 126-128 [crates/gwiki/src/commands/setup.rs:126-128] | Indexed function `gobby_home` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:126-128] |
| `write_gwiki_gcore_config` | function | `fn write_gwiki_gcore_config(` | `write_gwiki_gcore_config [function]` | `cf376b5a-2dc8-5b52-a62d-fab3df029b35` | 130-181 [crates/gwiki/src/commands/setup.rs:130-181] | Indexed function `write_gwiki_gcore_config` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:130-181] |
| `diagnose_required_service_config` | function | `fn diagnose_required_service_config(config: &mut StandaloneConfig) {` | `diagnose_required_service_config [function]` | `91c3254b-673c-55b2-9d12-0317e3abe517` | 183-199 [crates/gwiki/src/commands/setup.rs:183-199] | Indexed function `diagnose_required_service_config` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:183-199] |
| `apply_embedding_options` | function | `fn apply_embedding_options(` | `apply_embedding_options [function]` | `31bb393e-1e63-5774-9406-ebdeee5afe8a` | 201-244 [crates/gwiki/src/commands/setup.rs:201-244] | Indexed function `apply_embedding_options` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:201-244] |
| `validate_embedding_vector_dim` | function | `fn validate_embedding_vector_dim(options: &SetupOptions) -> anyhow::Result<()> {` | `validate_embedding_vector_dim [function]` | `f34818b4-0b18-5acc-9251-d049017f3f32` | 246-253 [crates/gwiki/src/commands/setup.rs:246-253] | Indexed function `validate_embedding_vector_dim` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:246-253] |
| `standalone_error` | function | `fn standalone_error(error: anyhow::Error) -> WikiError {` | `standalone_error [function]` | `0ab4d220-afcb-54c0-9480-aa66e75df6f6` | 255-259 [crates/gwiki/src/commands/setup.rs:255-259] | Indexed function `standalone_error` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:255-259] |
| `render` | function | `fn render(` | `render [function]` | `b3236181-6e4b-59b9-a02c-9f0bad4072e5` | 261-287 [crates/gwiki/src/commands/setup.rs:261-287] | Indexed function `render` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:261-287] |
| `setup_status` | function | `fn setup_status(` | `setup_status [function]` | `6c9c0e18-714c-5c79-9395-ceac34213a49` | 289-303 [crates/gwiki/src/commands/setup.rs:289-303] | Indexed function `setup_status` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:289-303] |
| `setup_status_reports_specific_outcome` | function | `fn setup_status_reports_specific_outcome() {` | `setup_status_reports_specific_outcome [function]` | `de1f9078-3e02-5ece-a191-22b19788f4a3` | 313-321 [crates/gwiki/src/commands/setup.rs:313-321] | Indexed function `setup_status_reports_specific_outcome` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:313-321] |
| `standalone_provisions_and_merges_config` | function | `fn standalone_provisions_and_merges_config() {` | `standalone_provisions_and_merges_config [function]` | `591c3c86-e316-5bed-88a7-a71bc4d3c0d9` | 324-366 [crates/gwiki/src/commands/setup.rs:324-366] | Indexed function `standalone_provisions_and_merges_config` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:324-366] |
| `reuses_existing_gcode_hub` | function | `fn reuses_existing_gcode_hub() {` | `reuses_existing_gcode_hub [function]` | `a4e8a7dc-1009-5300-ad81-af6037cbc740` | 369-397 [crates/gwiki/src/commands/setup.rs:369-397] | Indexed function `reuses_existing_gcode_hub` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:369-397] |
| `standalone_config_can_record_postgres_before_required_services` | function | `fn standalone_config_can_record_postgres_before_required_services() {` | `standalone_config_can_record_postgres_before_required_services [function]` | `384bd437-be42-52d2-9704-23efb7a2d413` | 400-423 [crates/gwiki/src/commands/setup.rs:400-423] | Indexed function `standalone_config_can_record_postgres_before_required_services` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:400-423] |
| `invalid_embedding_dim_does_not_mutate_config` | function | `fn invalid_embedding_dim_does_not_mutate_config() {` | `invalid_embedding_dim_does_not_mutate_config [function]` | `03b6b1e5-929a-5730-8704-fa618983d127` | 426-445 [crates/gwiki/src/commands/setup.rs:426-445] | Indexed function `invalid_embedding_dim_does_not_mutate_config` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:426-445] |
| `embedding_options_write_text_generation_bootstrap` | function | `fn embedding_options_write_text_generation_bootstrap() {` | `embedding_options_write_text_generation_bootstrap [function]` | `2f94f005-6ad2-5121-b4e0-ba35a864d7ab` | 448-478 [crates/gwiki/src/commands/setup.rs:448-478] | Indexed function `embedding_options_write_text_generation_bootstrap` in `crates/gwiki/src/commands/setup.rs`. [crates/gwiki/src/commands/setup.rs:448-478] |
