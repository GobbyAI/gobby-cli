---
title: crates/gwiki/src/support/config.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/config.rs
  ranges:
  - 18-20
  - 22-44
  - 23-29
  - 31-43
  - 46-61
  - 68-71
  - 73-80
  - 74-79
  - 82-86
  - 88-93
  - 96-102
  - 104-111
  - 113-118
  - 120-127
  - 129-136
  - 138-142
  - 144-151
  - 153-168
  - 182-185
  - 187-201
  - 188-200
  - 203-212
  - 204-211
  - 214-220
  - 223-225
  - 227-232
  - 228-231
  - 234-242
  - 235-237
  - 239-241
  - 245-257
  - 260-279
  - 283-301
  - 304-316
  - 320-332
  - 336-363
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/config.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

`crates/gwiki/src/support/config.rs` exposes 36 indexed API symbols.
[crates/gwiki/src/support/config.rs:18-20]
[crates/gwiki/src/support/config.rs:22-44]
[crates/gwiki/src/support/config.rs:23-29]
[crates/gwiki/src/support/config.rs:31-43]
[crates/gwiki/src/support/config.rs:46-61]

## API Symbols

- `HubPrimary` (class) component `HubPrimary [class]` (`bf09877f-8772-5b79-a0ea-177a058fea73`) lines 18-20 [crates/gwiki/src/support/config.rs:18-20]
  - Signature: `pub(crate) struct HubPrimary {`
  - Purpose: HubPrimary is a crate-private struct that wraps an optional Client connection for managing a primary hub database connection. [crates/gwiki/src/support/config.rs:18-20]
- `HubPrimary` (class) component `HubPrimary [class]` (`89604c04-2512-5bfc-a00c-5b62cdbbab09`) lines 22-44 [crates/gwiki/src/support/config.rs:22-44]
  - Signature: `impl ConfigSource for HubPrimary {`
  - Purpose: HubPrimary implements ConfigSource to fetch and decode configuration values from PostgreSQL while resolving `$secret:`-prefixed values through the secrets module, with fallback error handling when the database connection is unavailable. [crates/gwiki/src/support/config.rs:22-44]
- `HubPrimary.config_value` (method) component `HubPrimary.config_value [method]` (`46a3fb54-b9ad-5717-be8e-31b1ea45da5f`) lines 23-29 [crates/gwiki/src/support/config.rs:23-29]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Retrieves and decodes a configuration value from the PostgreSQL database for the specified key, returning `None` if the connection is unavailable or if either the database read or value decoding operation fails. [crates/gwiki/src/support/config.rs:23-29]
- `HubPrimary.resolve_value` (method) component `HubPrimary.resolve_value [method]` (`7e81b3d9-3fd8-5dce-b466-5aa424f98ba2`) lines 31-43 [crates/gwiki/src/support/config.rs:31-43]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves a configuration value string by delegating to a core secrets resolver if a database connection exists, otherwise returns the literal value unchanged unless it contains a `$secret:` prefix, which raises an error. [crates/gwiki/src/support/config.rs:31-43]
- `hub_ai_config_source` (function) component `hub_ai_config_source [function]` (`03673ec0-e042-5ecb-8465-83e2e29b50c4`) lines 46-61 [crates/gwiki/src/support/config.rs:46-61]
  - Signature: `pub(crate) fn hub_ai_config_source(`
  - Purpose: Constructs and returns an `AiConfigSource<HubPrimary>` initialized from Gobby home with an optional read-write PostgreSQL database connection for the specified command. [crates/gwiki/src/support/config.rs:46-61]
- `SharedCodeGraphLimits` (class) component `SharedCodeGraphLimits [class]` (`faa4c6ea-6b38-5a26-b2f0-43a0a74136be`) lines 68-71 [crates/gwiki/src/support/config.rs:68-71]
  - Signature: `pub(crate) struct SharedCodeGraphLimits {`
  - Purpose: `SharedCodeGraphLimits` is a crate-private struct that defines configurable upper bounds for the number of call edges and import edges permitted in a code graph representation. [crates/gwiki/src/support/config.rs:68-71]
- `SharedCodeGraphLimits` (class) component `SharedCodeGraphLimits [class]` (`2d122f90-2cec-5b9b-844c-c2bcf3f3085a`) lines 73-80 [crates/gwiki/src/support/config.rs:73-80]
  - Signature: `impl Default for SharedCodeGraphLimits {`
  - Purpose: `SharedCodeGraphLimits` implements the `Default` trait by initializing both `call_edge_limit` and `import_edge_limit` fields to `DEFAULT_SHARED_CODE_GRAPH_EDGE_LIMIT`. [crates/gwiki/src/support/config.rs:73-80]
- `SharedCodeGraphLimits.default` (method) component `SharedCodeGraphLimits.default [method]` (`fe650e09-8172-5b62-82ad-66fb771a5059`) lines 74-79 [crates/gwiki/src/support/config.rs:74-79]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a default instance with both `call_edge_limit` and `import_edge_limit` fields initialized to `DEFAULT_SHARED_CODE_GRAPH_EDGE_LIMIT`. [crates/gwiki/src/support/config.rs:74-79]
- `local_index_options` (function) component `local_index_options [function]` (`410c7d5e-0ab7-5e59-965c-ebac3fe2d0a2`) lines 82-86 [crates/gwiki/src/support/config.rs:82-86]
  - Signature: `pub(crate) fn local_index_options() -> Result<IndexOptions, WikiError> {`
  - Purpose: Resolves and returns `IndexOptions` from a layered configuration source that combines environment variables with locally-read standalone configuration. [crates/gwiki/src/support/config.rs:82-86]
- `index_options_from_conn` (function) component `index_options_from_conn [function]` (`f55cd370-a57f-5a75-a653-96990fbd8c19`) lines 88-93 [crates/gwiki/src/support/config.rs:88-93]
  - Signature: `pub(crate) fn index_options_from_conn(conn: &mut Client) -> Result<IndexOptions, WikiError> {`
  - Purpose: Resolves IndexOptions by merging PostgreSQL configuration from the provided client connection with a standalone configuration source. [crates/gwiki/src/support/config.rs:88-93]
- `local_shared_code_graph_limits` (function) component `local_shared_code_graph_limits [function]` (`60853d35-bf82-58e6-ad93-cc1f079f8d0d`) lines 96-102 [crates/gwiki/src/support/config.rs:96-102]
  - Signature: `pub(crate) fn local_shared_code_graph_limits() -> Result<SharedCodeGraphLimits, WikiError> {`
  - Purpose: Retrieves `SharedCodeGraphLimits` from a standalone configuration file via resolution if present, otherwise returns the default configuration. [crates/gwiki/src/support/config.rs:96-102]
- `shared_code_graph_limits_from_conn` (function) component `shared_code_graph_limits_from_conn [function]` (`d61deee2-96f4-5fde-ace0-2f4e6cd04042`) lines 104-111 [crates/gwiki/src/support/config.rs:104-111]
  - Signature: `pub(crate) fn shared_code_graph_limits_from_conn(`
  - Purpose: Resolves `SharedCodeGraphLimits` from a layered configuration source that prioritizes PostgreSQL-backed config over standalone config. [crates/gwiki/src/support/config.rs:104-111]
- `qdrant_config_has_url` (function) component `qdrant_config_has_url [function]` (`d63925a8-cd8e-5d7e-82ab-f08e1213999a`) lines 113-118 [crates/gwiki/src/support/config.rs:113-118]
  - Signature: `pub(crate) fn qdrant_config_has_url(config: &QdrantConfig) -> bool {`
  - Purpose: Returns `true` if the QdrantConfig's URL field is `Some` and contains non-whitespace content after trimming. [crates/gwiki/src/support/config.rs:113-118]
- `read_standalone_config` (function) component `read_standalone_config [function]` (`fbc1bd41-cbfc-577a-aabe-3bcc8801eb76`) lines 120-127 [crates/gwiki/src/support/config.rs:120-127]
  - Signature: `fn read_standalone_config() -> Result<Option<StandaloneConfig>, WikiError> {`
  - Purpose: Reads and returns the `StandaloneConfig` from the gwiki indexing configuration file in the Gobby home directory, converting any resolution or parsing errors to `WikiError`. [crates/gwiki/src/support/config.rs:120-127]
- `resolve_index_options` (function) component `resolve_index_options [function]` (`c35262bf-e907-56e5-a22b-192bcc35ddcf`) lines 129-136 [crates/gwiki/src/support/config.rs:129-136]
  - Signature: `fn resolve_index_options(`
  - Purpose: Resolves indexing configuration from a mutable config source and transforms it into IndexOptions, mapping configuration errors to WikiError. [crates/gwiki/src/support/config.rs:129-136]
- `index_options_from_config` (function) component `index_options_from_config [function]` (`8f6696ea-2c91-51c7-8c27-d72238555df6`) lines 138-142 [crates/gwiki/src/support/config.rs:138-142]
  - Signature: `fn index_options_from_config(config: gobby_core::config::IndexingConfig) -> indexer::IndexOptions {`
  - Purpose: Converts an `IndexingConfig` into an `IndexOptions` struct by extracting and forwarding the `respect_gitignore` configuration field. [crates/gwiki/src/support/config.rs:138-142]
- `resolve_shared_code_graph_limits` (function) component `resolve_shared_code_graph_limits [function]` (`d0057609-80cc-5913-9b05-63a231f0a13e`) lines 144-151 [crates/gwiki/src/support/config.rs:144-151]
  - Signature: `fn resolve_shared_code_graph_limits(`
  - Purpose: Resolves call and import edge limit configuration parameters from a `ConfigSource` into a `SharedCodeGraphLimits` struct. [crates/gwiki/src/support/config.rs:144-151]
- `resolve_limit` (function) component `resolve_limit [function]` (`fef1c01e-4e64-5064-9a84-fedd43d43c67`) lines 153-168 [crates/gwiki/src/support/config.rs:153-168]
  - Signature: `fn resolve_limit(source: &mut impl ConfigSource, key: &'static str) -> Result<usize, WikiError> {`
  - Purpose: Resolves and parses a configuration value to `usize` with a default fallback, returning `WikiError` on resolution or parse failure. [crates/gwiki/src/support/config.rs:153-168]
- `EnvGuard` (class) component `EnvGuard [class]` (`9b254d32-ba5e-511e-933d-54eb161a4d0d`) lines 182-185 [crates/gwiki/src/support/config.rs:182-185]
  - Signature: `struct EnvGuard {`
  - Purpose: EnvGuard is a RAII type that holds a static mutex lock and preserves a previous OsString value to enable thread-safe, scoped environment variable manipulation with automatic restoration on drop. [crates/gwiki/src/support/config.rs:182-185]
- `EnvGuard` (class) component `EnvGuard [class]` (`283bd840-f436-58f3-8b06-2b559813f06b`) lines 187-201 [crates/gwiki/src/support/config.rs:187-201]
  - Signature: `impl EnvGuard {`
  - Purpose: A thread-safe RAII guard that atomically mutates GOBBY_HOME while preserving its previous value under a global mutex lock, enabling transactional restoration on drop. [crates/gwiki/src/support/config.rs:187-201]
- `EnvGuard.set_gobby_home` (method) component `EnvGuard.set_gobby_home [method]` (`7d7aa43d-75b2-5e0a-8631-f66e995e198d`) lines 188-200 [crates/gwiki/src/support/config.rs:188-200]
  - Signature: `fn set_gobby_home(path: &Path) -> Self {`
  - Purpose: Atomically sets the GOBBY_HOME environment variable to the provided path under lock protection, returning a guard containing the lock and previous value to ensure safe restoration on drop for test isolation. [crates/gwiki/src/support/config.rs:188-200]
- `EnvGuard` (class) component `EnvGuard [class]` (`56b415b4-f4df-5b29-9ed6-2b9a7db3c254`) lines 203-212 [crates/gwiki/src/support/config.rs:203-212]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: EnvGuard is a RAII guard that conditionally restores or removes the `GOBBY_HOME` environment variable upon drop based on whether a prior value existed. [crates/gwiki/src/support/config.rs:203-212]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`562394c7-f0b4-5683-a08e-78c1833110e3`) lines 204-211 [crates/gwiki/src/support/config.rs:204-211]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Restores the `GOBBY_HOME` environment variable to its previously captured state upon drop, or removes it if no prior value existed. [crates/gwiki/src/support/config.rs:204-211]
- `write_file` (function) component `write_file [function]` (`162348de-8b35-5292-872d-aae9d34f1e6a`) lines 214-220 [crates/gwiki/src/support/config.rs:214-220]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &str) {`
  - Purpose: Writes the provided contents to a file at the path formed by joining `root` and `rel`, creating all necessary parent directories if they don't exist. [crates/gwiki/src/support/config.rs:214-220]
- `TestSource` (class) component `TestSource [class]` (`6ce590b9-9982-5fc5-bba7-38ce4f07de55`) lines 223-225 [crates/gwiki/src/support/config.rs:223-225]
  - Signature: `struct TestSource {`
  - Purpose: TestSource is a struct that wraps a BTreeMap to store ordered string key-value pairs. [crates/gwiki/src/support/config.rs:223-225]
- `TestSource` (class) component `TestSource [class]` (`63949847-1b7f-59b8-91ba-5616e9444d69`) lines 227-232 [crates/gwiki/src/support/config.rs:227-232]
  - Signature: `impl TestSource {`
  - Purpose: A fluent builder method that inserts a string key-value pair into `TestSource`'s internal map and returns `self` to enable method chaining. [crates/gwiki/src/support/config.rs:227-232]
- `TestSource.with` (method) component `TestSource.with [method]` (`bbe05f32-4c07-5393-aa0e-c64985500da8`) lines 228-231 [crates/gwiki/src/support/config.rs:228-231]
  - Signature: `fn with(mut self, key: &str, value: &str) -> Self {`
  - Purpose: This method inserts a key-value pair into an internal `values` map using the builder pattern, returning `self` to enable method chaining. [crates/gwiki/src/support/config.rs:228-231]
- `TestSource` (class) component `TestSource [class]` (`e900ddd4-6107-5fce-8250-6eed86c8b7c5`) lines 234-242 [crates/gwiki/src/support/config.rs:234-242]
  - Signature: `impl gobby_core::config::ConfigSource for TestSource {`
  - Purpose: TestSource is a `ConfigSource` implementation that retrieves configuration values from an in-memory map and performs identity resolution without transformation. [crates/gwiki/src/support/config.rs:234-242]
- `TestSource.config_value` (method) component `TestSource.config_value [method]` (`a3921349-05db-58ca-aaf4-ca8caa1c947f`) lines 235-237 [crates/gwiki/src/support/config.rs:235-237]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: This method retrieves and returns a cloned copy of the configuration value associated with a given key from an internal values map, or `None` if the key does not exist. [crates/gwiki/src/support/config.rs:235-237]
- `TestSource.resolve_value` (method) component `TestSource.resolve_value [method]` (`18816624-9bb0-5bf6-92ae-cca2b4841b3e`) lines 239-241 [crates/gwiki/src/support/config.rs:239-241]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Converts the input string slice to an owned String and wraps it in an Ok result, effectively making the string reference allocation explicit and fallible-operation-compatible. [crates/gwiki/src/support/config.rs:239-241]
- `shared_code_graph_limits_default_to_200` (function) component `shared_code_graph_limits_default_to_200 [function]` (`f1646dc9-8c4c-58f1-9150-c0f8cce540f5`) lines 245-257 [crates/gwiki/src/support/config.rs:245-257]
  - Signature: `fn shared_code_graph_limits_default_to_200() {`
  - Purpose: This test function asserts that `resolve_shared_code_graph_limits` returns `SharedCodeGraphLimits` with both `call_edge_limit` and `import_edge_limit` defaulting to 200. [crates/gwiki/src/support/config.rs:245-257]
- `shared_code_graph_limits_use_config_source_over_standalone` (function) component `shared_code_graph_limits_use_config_source_over_standalone [function]` (`cc49d970-fc85-595f-aae5-63d7e1050965`) lines 260-279 [crates/gwiki/src/support/config.rs:260-279]
  - Signature: `fn shared_code_graph_limits_use_config_source_over_standalone() {`
  - Purpose: Verifies that `resolve_shared_code_graph_limits` prioritizes values from a primary config source over a fallback StandaloneConfig when resolving shared code graph edge limits. [crates/gwiki/src/support/config.rs:260-279]
- `local_shared_code_graph_limits_read_gcore_yaml` (function) component `local_shared_code_graph_limits_read_gcore_yaml [function]` (`78da5e83-3767-5309-8c31-229eca2daee8`) lines 283-301 [crates/gwiki/src/support/config.rs:283-301]
  - Signature: `fn local_shared_code_graph_limits_read_gcore_yaml() {`
  - Purpose: This unit test verifies that `local_shared_code_graph_limits()` correctly deserializes `SharedCodeGraphLimits` (call_edge_limit and import_edge_limit) from a `gcore.yaml` configuration file. [crates/gwiki/src/support/config.rs:283-301]
- `shared_code_graph_limits_reject_invalid_or_negative_values` (function) component `shared_code_graph_limits_reject_invalid_or_negative_values [function]` (`7bd819cf-723b-5c97-a07b-5e6035272491`) lines 304-316 [crates/gwiki/src/support/config.rs:304-316]
  - Signature: `fn shared_code_graph_limits_reject_invalid_or_negative_values() {`
  - Purpose: Verifies that `resolve_shared_code_graph_limits` correctly rejects and reports errors for both non-numeric invalid values and negative limit values. [crates/gwiki/src/support/config.rs:304-316]
- `local_index_options_read_gcore_yaml` (function) component `local_index_options_read_gcore_yaml [function]` (`97fc85e9-83df-5235-9cd4-56db6ab3aba5`) lines 320-332 [crates/gwiki/src/support/config.rs:320-332]
  - Signature: `fn local_index_options_read_gcore_yaml() {`
  - Purpose: This test function verifies that `local_index_options()` correctly reads and parses the `respect_gitignore: false` configuration from a `gcore.yaml` file. [crates/gwiki/src/support/config.rs:320-332]
- `memory_indexing_uses_local_index_options` (function) component `memory_indexing_uses_local_index_options [function]` (`eaf58024-bf53-5d32-bbf3-478b8b17238d`) lines 336-363 [crates/gwiki/src/support/config.rs:336-363]
  - Signature: `fn memory_indexing_uses_local_index_options() {`
  - Purpose: This test verifies that vault indexing with local index options correctly applies the `respect_gitignore: false` configuration setting to include files that would otherwise be excluded by `.gitignore`. [crates/gwiki/src/support/config.rs:336-363]

