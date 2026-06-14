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
  - 552-589
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/setup.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Implements the standalone `gcode setup` flow: it validates the request, applies any explicit FalkorDB service overrides, resolves or provisions the database and supporting services, connects to Postgres with retry, optionally clears existing code-index projections, runs the standalone setup, and then writes the resulting `gcore` config and status output. The helper functions split that work into projection cleanup, service/database resolution, embedding bootstrap selection and endpoint probing, config writing, and embedding-key removal, while the tests verify config persistence, provider validation, and isolated setup behavior.
[crates/gcode/src/commands/setup.rs:22-94]
[crates/gcode/src/commands/setup.rs:96-99]
[crates/gcode/src/commands/setup.rs:101-117]
[crates/gcode/src/commands/setup.rs:119-165]
[crates/gcode/src/commands/setup.rs:167-186]

## API Symbols

- `run` (function) component `run [function]` (`9dc50e8d-0c99-53b3-a7ae-4d010ee7bfd6`) lines 22-94 [crates/gcode/src/commands/setup.rs:22-94]
  - Signature: `pub fn run(request: StandaloneSetupRequest, format: Format, quiet: bool) -> anyhow::Result<()> {`
  - Purpose: Validates a standalone setup request, provisions or connects to the required database and services, optionally clears code-index projections, runs the setup, reports any failures in the requested format, and on success writes the gcore config and records the resulting service, embedding, and config-file status. [crates/gcode/src/commands/setup.rs:22-94]
- `OverwriteProjectionConfigs` (class) component `OverwriteProjectionConfigs [class]` (`1059a619-b0f5-53ff-b42c-12e3ad77c4f5`) lines 96-99 [crates/gcode/src/commands/setup.rs:96-99]
  - Signature: `struct OverwriteProjectionConfigs {`
  - Purpose: 'OverwriteProjectionConfigs' is a configuration overlay struct that optionally provides replacement settings for FalkorDB and Qdrant projection backends via 'falkordb: Option<config::FalkorConfig>' and 'qdrant: Option<QdrantConfig>'. [crates/gcode/src/commands/setup.rs:96-99]
- `clear_overwrite_projections` (function) component `clear_overwrite_projections [function]` (`b75a2915-26c4-5465-93ad-03f319e7ddd8`) lines 101-117 [crates/gcode/src/commands/setup.rs:101-117]
  - Signature: `fn clear_overwrite_projections(`
  - Purpose: Clears any existing overwrite projections by resolving the configured FalkorDB and Qdrant targets and, if present, wiping the FalkorDB code index and deleting Qdrant code-symbol collections, returning an error if either cleanup step fails. [crates/gcode/src/commands/setup.rs:101-117]
- `overwrite_projection_configs` (function) component `overwrite_projection_configs [function]` (`a3e3ae09-6903-5d40-8127-08436c0b2173`) lines 119-165 [crates/gcode/src/commands/setup.rs:119-165]
  - Signature: `fn overwrite_projection_configs(`
  - Purpose: Loads the standalone config from 'home', applies Docker-derived defaults when a provisioning report is present, overrides them with any explicit request values, then resolves and returns the projected FalkorDB and Qdrant configs in an 'OverwriteProjectionConfigs' result. [crates/gcode/src/commands/setup.rs:119-165]
- `resolve_or_provision_database` (function) component `resolve_or_provision_database [function]` (`bbcfa564-c3ab-5959-b8d3-59ba484d1857`) lines 167-186 [crates/gcode/src/commands/setup.rs:167-186]
  - Signature: `fn resolve_or_provision_database(`
  - Purpose: Returns an explicit 'request.database_url' if provided, otherwise resolves the existing database URL when 'request.no_services' is set, and otherwise provisions/ensures the hub using cloned service options plus any resolvable candidate database URL, returning the resulting database URL and optional 'DockerProvisioningReport'. [crates/gcode/src/commands/setup.rs:167-186]
- `apply_service_overrides` (function) component `apply_service_overrides [function]` (`bb0421c5-16f5-5db4-afd9-fa6a38aae8ae`) lines 188-201 [crates/gcode/src/commands/setup.rs:188-201]
  - Signature: `fn apply_service_overrides(`
  - Purpose: 'apply_service_overrides' copies any explicitly provided FalkorDB host, port, and password from a 'StandaloneSetupRequest' into the mutable 'DockerServiceOptions', overriding the existing service configuration only for fields present in the request. [crates/gcode/src/commands/setup.rs:188-201]
- `connect_postgres_with_retry` (function) component `connect_postgres_with_retry [function]` (`c906be44-d257-515c-a451-591115c32c89`) lines 203-219 [crates/gcode/src/commands/setup.rs:203-219]
  - Signature: `fn connect_postgres_with_retry(database_url: &str, retry: bool) -> anyhow::Result<Client> {`
  - Purpose: Attempts to establish a read-write PostgreSQL connection via 'gobby_core::postgres::connect_readwrite', retrying up to 30 times with 2-second delays when 'retry' is true, and otherwise returning the last error wrapped with context if all attempts fail. [crates/gcode/src/commands/setup.rs:203-219]
- `write_gcore_config` (function) component `write_gcore_config [function]` (`902bec0d-7426-5a01-8728-1e22bd8aaf74`) lines 221-283 [crates/gcode/src/commands/setup.rs:221-283]
  - Signature: `fn write_gcore_config(`
  - Purpose: Writes or updates the standalone gcore config at 'gcore_config_path(home)', populating the PostgreSQL DSN and, depending on whether a provisioning report is present, either provisioned service endpoints or request-specified FalkorDB/Qdrant values, plus optional embedding settings, then returns the config path. [crates/gcode/src/commands/setup.rs:221-283]
- `remove_embedding_keys` (function) component `remove_embedding_keys [function]` (`be627624-6381-5faa-8220-44f4cff9b592`) lines 285-296 [crates/gcode/src/commands/setup.rs:285-296]
  - Signature: `fn remove_embedding_keys(config: &mut StandaloneConfig) {`
  - Purpose: Removes the embedding-related configuration entries ('AI_PROVIDER', 'AI_API_BASE', 'AI_MODEL', 'AI_DIM', 'AI_QUERY_PREFIX', and 'AI_API_KEY') from the given 'StandaloneConfig' by iterating over their keys and calling 'config.remove' on each. [crates/gcode/src/commands/setup.rs:285-296]
- `service_configured_compose_file` (function) component `service_configured_compose_file [function]` (`0f6a5297-78c8-5929-9e16-88fa9130caa2`) lines 298-301 [crates/gcode/src/commands/setup.rs:298-301]
  - Signature: `fn service_configured_compose_file(home: &std::path::Path) -> Option<String> {`
  - Purpose: Returns the configured compose file path as a string if 'compose_file_path(home)' exists on disk, otherwise 'None'. [crates/gcode/src/commands/setup.rs:298-301]
- `resolve_embedding_bootstrap` (function) component `resolve_embedding_bootstrap [function]` (`a2b563fb-1353-5cfd-a555-7cfc7760f498`) lines 303-351 [crates/gcode/src/commands/setup.rs:303-351]
  - Signature: `fn resolve_embedding_bootstrap(`
  - Purpose: Resolves an 'EmbeddingBootstrap' from 'StandaloneSetupRequest' by selecting a provider ('none', 'lmstudio', 'ollama', or explicit 'openai-compatible'), auto-detecting a default when unspecified, then overriding fields from request parameters and rejecting invalid provider names or a zero vector dimension. [crates/gcode/src/commands/setup.rs:303-351]
- `explicit_embedding_bootstrap` (function) component `explicit_embedding_bootstrap [function]` (`68d3e471-bb90-5c9e-8b50-bab88333cd79`) lines 353-372 [crates/gcode/src/commands/setup.rs:353-372]
  - Signature: `fn explicit_embedding_bootstrap(`
  - Purpose: Builds an 'EmbeddingBootstrap' for an OpenAI-compatible embedding backend by requiring 'request.embedding_api_base', defaulting the model and vector dimension when absent, and copying the query prefix and API key from the setup request. [crates/gcode/src/commands/setup.rs:353-372]
- `endpoint_reachable` (function) component `endpoint_reachable [function]` (`2933a9f0-52c1-5a35-8bee-31fada2cbe16`) lines 374-390 [crates/gcode/src/commands/setup.rs:374-390]
  - Signature: `fn endpoint_reachable(api_base: &str) -> bool {`
  - Purpose: Returns 'true' only if 'api_base' parses as a URL with a host and port, resolves to at least one socket address, and successfully establishes a TCP connection to any resolved address within 150 ms; otherwise returns 'false'. [crates/gcode/src/commands/setup.rs:374-390]
- `write_gcore_config_writes_ai_embeddings_and_redacts_api_key` (function) component `write_gcore_config_writes_ai_embeddings_and_redacts_api_key [function]` (`4d1b94d5-3619-577b-a813-717625cce318`) lines 398-460 [crates/gcode/src/commands/setup.rs:398-460]
  - Signature: `fn write_gcore_config_writes_ai_embeddings_and_redacts_api_key() {`
  - Purpose: Verifies that 'write_gcore_config' persists AI embedding settings into the generated standalone config, including API base, model, vector dimension, query prefix, and API key presence, while redacting the stored key via the embedding status fingerprinting path. [crates/gcode/src/commands/setup.rs:398-460]
- `write_gcore_config_clears_embedding_keys_when_disabled` (function) component `write_gcore_config_clears_embedding_keys_when_disabled [function]` (`49e02074-3acf-5878-a323-7e8bfa745289`) lines 463-511 [crates/gcode/src/commands/setup.rs:463-511]
  - Signature: `fn write_gcore_config_clears_embedding_keys_when_disabled() {`
  - Purpose: Verifies that 'write_gcore_config' removes all embedding-related config keys from an existing standalone config when embeddings are disabled, while preserving the Postgres DSN. [crates/gcode/src/commands/setup.rs:463-511]
- `setup_rejects_removed_embedding_provider_aliases` (function) component `setup_rejects_removed_embedding_provider_aliases [function]` (`81c55b98-d81d-58d0-910a-91cb16f08e63`) lines 514-529 [crates/gcode/src/commands/setup.rs:514-529]
  - Signature: `fn setup_rejects_removed_embedding_provider_aliases() {`
  - Purpose: Verifies that 'resolve_embedding_bootstrap' rejects deprecated embedding provider aliases ('lm-studio', 'openai', 'remote') when an API base is set, and returns an error message requiring 'lmstudio', 'ollama', 'openai-compatible', or 'none'. [crates/gcode/src/commands/setup.rs:514-529]
- `setup_accepts_canonical_lmstudio_embedding_provider` (function) component `setup_accepts_canonical_lmstudio_embedding_provider [function]` (`7718a632-c78d-5e34-b22b-3f2a2f888dd4`) lines 532-541 [crates/gcode/src/commands/setup.rs:532-541]
  - Signature: `fn setup_accepts_canonical_lmstudio_embedding_provider() {`
  - Purpose: Verifies that 'resolve_embedding_bootstrap' accepts the canonical embedding provider name '"lmstudio"' in a 'StandaloneSetupRequest' and preserves it in the resulting embedding configuration. [crates/gcode/src/commands/setup.rs:532-541]
- `standalone_command_installs_public_code_index_subset` (function) component `standalone_command_installs_public_code_index_subset [function]` (`4d3aceb9-4fd6-5dd5-aaec-6e6c3fcce308`) lines 552-589 [crates/gcode/src/commands/setup.rs:552-589]
  - Signature: `fn standalone_command_installs_public_code_index_subset() {`
  - Purpose: Creates an isolated temporary GOBBY_HOME, runs standalone setup with a test Postgres database, asserts that only the public code-index tables are installed (and 'config_store' is not), verifies 'gcore.yaml' is created, then drops the code-index test objects and cleans up the environment variable. [crates/gcode/src/commands/setup.rs:552-589]

