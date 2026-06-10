---
title: crates/gcode/src/config/services.rs
type: code_file
provenance:
- file: crates/gcode/src/config/services.rs
  ranges:
  - 22-24
  - 26-29
  - 31-41
  - 43-50
  - 53-59
  - 61-63
  - 67-72
  - 74-76
  - 79-82
  - 85-93
  - 95-97
  - 101-112
  - 114-116
  - 120-124
  - 126-130
  - 133-135
  - 139-156
  - 158-160
  - 163-172
  - 175-190
  - 192-216
  - 193-215
  - '218'
  - 220-235
  - 238-241
  - 249-251
  - 253-255
  - 264-270
  - 272-274
  - 278-291
  - 294-307
  - 310-323
  - 326-337
  - 342-352
  - 354-369
  - 374-384
  - 386-395
  - 397-405
  - 407-422
  - 424-447
  - 454-464
  - 466-484
  - 486-496
  - 498-507
  - 509-515
  - 517-526
  - 528-535
  - 537-543
  - 545-556
  - 558-567
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/services.rs

Module: [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]

## Purpose

`crates/gcode/src/config/services.rs` exposes 50 indexed API symbols.
[crates/gcode/src/config/services.rs:22-24]
[crates/gcode/src/config/services.rs:26-29]
[crates/gcode/src/config/services.rs:31-41]
[crates/gcode/src/config/services.rs:43-50]
[crates/gcode/src/config/services.rs:53-59]
[crates/gcode/src/config/services.rs:61-63]
[crates/gcode/src/config/services.rs:67-72]
[crates/gcode/src/config/services.rs:74-76]
[crates/gcode/src/config/services.rs:79-82]
[crates/gcode/src/config/services.rs:85-93]
[crates/gcode/src/config/services.rs:95-97]
[crates/gcode/src/config/services.rs:101-112]
[crates/gcode/src/config/services.rs:114-116]
[crates/gcode/src/config/services.rs:120-124]
[crates/gcode/src/config/services.rs:126-130]
[crates/gcode/src/config/services.rs:133-135]
[crates/gcode/src/config/services.rs:139-156]
[crates/gcode/src/config/services.rs:158-160]
[crates/gcode/src/config/services.rs:163-172]
[crates/gcode/src/config/services.rs:175-190]
[crates/gcode/src/config/services.rs:192-216]
[crates/gcode/src/config/services.rs:193-215]
[crates/gcode/src/config/services.rs:218]
[crates/gcode/src/config/services.rs:220-235]
[crates/gcode/src/config/services.rs:238-241]
[crates/gcode/src/config/services.rs:249-251]
[crates/gcode/src/config/services.rs:253-255]
[crates/gcode/src/config/services.rs:264-270]
[crates/gcode/src/config/services.rs:272-274]
[crates/gcode/src/config/services.rs:278-291]
[crates/gcode/src/config/services.rs:294-307]
[crates/gcode/src/config/services.rs:310-323]
[crates/gcode/src/config/services.rs:326-337]
[crates/gcode/src/config/services.rs:342-352]
[crates/gcode/src/config/services.rs:354-369]
[crates/gcode/src/config/services.rs:374-384]
[crates/gcode/src/config/services.rs:386-395]
[crates/gcode/src/config/services.rs:397-405]
[crates/gcode/src/config/services.rs:407-422]
[crates/gcode/src/config/services.rs:424-447]
[crates/gcode/src/config/services.rs:454-464]
[crates/gcode/src/config/services.rs:466-484]
[crates/gcode/src/config/services.rs:486-496]
[crates/gcode/src/config/services.rs:498-507]
[crates/gcode/src/config/services.rs:509-515]
[crates/gcode/src/config/services.rs:517-526]
[crates/gcode/src/config/services.rs:528-535]
[crates/gcode/src/config/services.rs:537-543]
[crates/gcode/src/config/services.rs:545-556]
[crates/gcode/src/config/services.rs:558-567]

## API Symbols

- `PostgresConfigSource` (class) component `PostgresConfigSource [class]` (`14c4212d-a6da-54df-a04d-2d0c25e27714`) lines 22-24 [crates/gcode/src/config/services.rs:22-24]
  - Signature: `struct PostgresConfigSource<'a> {`
  - Purpose: PostgresConfigSource is a wrapper struct that holds a mutable reference to a PostgreSQL Client connection, with an explicit lifetime bound to ensure the reference validity. [crates/gcode/src/config/services.rs:22-24]
- `ServiceConfigSource` (type) component `ServiceConfigSource [type]` (`2a2eb8b3-dca4-5844-8004-a6d2ee165753`) lines 26-29 [crates/gcode/src/config/services.rs:26-29]
  - Signature: `trait ServiceConfigSource {`
  - Purpose: Indexed type `ServiceConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:26-29]
- `service_env_value` (function) component `service_env_value [function]` (`7fd2e53c-7c6f-5155-bc27-a3c429561fc3`) lines 31-41 [crates/gcode/src/config/services.rs:31-41]
  - Signature: `fn service_env_value(key: &str) -> Option<String> {`
  - Purpose: Retrieves environment variable values for service configuration keys by mapping them to their GOBBY_* prefixed counterparts, returning None for unmapped keys. [crates/gcode/src/config/services.rs:31-41]
- `config_store_missing` (function) component `config_store_missing [function]` (`db0efd01-b1fd-56f8-96a0-9f9aa605494a`) lines 43-50 [crates/gcode/src/config/services.rs:43-50]
  - Signature: `fn config_store_missing(error: &anyhow::Error) -> bool {`
  - Purpose: Returns true if any error in the error chain is a PostgreSQL database error with UNDEFINED_TABLE SQL state. [crates/gcode/src/config/services.rs:43-50]
- `config_value` (function) component `config_value [function]` (`81aa888c-ee22-59df-bcfb-9d1856edf208`) lines 53-59 [crates/gcode/src/config/services.rs:53-59]
  - Signature: `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Reads a configuration value from PostgreSQL by key and returns its decoded string value, or `None` if the config store is missing, otherwise propagating errors. [crates/gcode/src/config/services.rs:53-59]
- `resolve_value` (function) component `resolve_value [function]` (`ece694a9-8654-5fe8-921d-7e2ec8a7fc71`) lines 61-63 [crates/gcode/src/config/services.rs:61-63]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves a configuration value string by delegating to `secrets::resolve_config_value` with the provided value and the struct's database connection. [crates/gcode/src/config/services.rs:61-63]
- `config_value` (function) component `config_value [function]` (`95851a28-1ce8-5335-a925-11d6294a992a`) lines 67-72 [crates/gcode/src/config/services.rs:67-72]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Retrieves a configuration value from the ServiceConfigSource trait by key, logs any errors as warnings, and returns a flattened Option<String>. [crates/gcode/src/config/services.rs:67-72]
- `resolve_value` (function) component `resolve_value [function]` (`766144d1-42b2-5eb4-9c04-d0de59ae07ba`) lines 74-76 [crates/gcode/src/config/services.rs:74-76]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Delegates the resolution of a string value to the `ServiceConfigSource` trait implementation, returning the resolved string or an error. [crates/gcode/src/config/services.rs:74-76]
- `FallbackConfigSource` (class) component `FallbackConfigSource [class]` (`1b29490e-8a84-58b4-b2e4-e88b56517a91`) lines 79-82 [crates/gcode/src/config/services.rs:79-82]
  - Signature: `struct FallbackConfigSource<'a> {`
  - Purpose: `FallbackConfigSource` is a generic struct that holds a primary PostgreSQL configuration source with an optional standalone configuration as a fallback option. [crates/gcode/src/config/services.rs:79-82]
- `config_value` (function) component `config_value [function]` (`e0a31368-fe19-5829-a9f7-006712693029`) lines 85-93 [crates/gcode/src/config/services.rs:85-93]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Retrieves a configuration string value by key through sequential fallback sources: environment variables, PostgreSQL configuration, and optional standalone configuration, returning the first match or None. [crates/gcode/src/config/services.rs:85-93]
- `resolve_value` (function) component `resolve_value [function]` (`291295b5-55b7-5bf3-a726-51c76420218f`) lines 95-97 [crates/gcode/src/config/services.rs:95-97]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves a configuration value string by delegating to `ConfigSource::resolve_value` with a mutable reference to the instance's PostgreSQL connection. [crates/gcode/src/config/services.rs:95-97]
- `config_value` (function) component `config_value [function]` (`8f26dbba-a2b9-5ae2-8dab-ea12e8705fd4`) lines 101-112 [crates/gcode/src/config/services.rs:101-112]
  - Signature: `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Retrieves a configuration value for a given key through a hierarchical lookup chain that checks environment variables first, then PostgreSQL-backed config, then standalone config, returning the first available value or None. [crates/gcode/src/config/services.rs:101-112]
- `resolve_value` (function) component `resolve_value [function]` (`71905ef8-695f-58c8-88ac-5d22f59699f0`) lines 114-116 [crates/gcode/src/config/services.rs:114-116]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: This method delegates value resolution to `ServiceConfigSource::resolve_value` by passing a mutable reference to its `postgres` field, returning an `anyhow::Result<String>`. [crates/gcode/src/config/services.rs:114-116]
- `EmbeddingConfigDetails` (class) component `EmbeddingConfigDetails [class]` (`304017c5-dfe2-5555-9875-6a31c9c87662`) lines 120-124 [crates/gcode/src/config/services.rs:120-124]
  - Signature: `pub(crate) struct EmbeddingConfigDetails {`
  - Purpose: `EmbeddingConfigDetails` is a crate-private struct that encapsulates an `EmbeddingConfig` with static namespace and source metadata. [crates/gcode/src/config/services.rs:120-124]
- `TracingFallbackConfigSource` (class) component `TracingFallbackConfigSource [class]` (`18d76442-1497-5a59-b7c0-433ae9a91455`) lines 126-130 [crates/gcode/src/config/services.rs:126-130]
  - Signature: `struct TracingFallbackConfigSource<'a> {`
  - Purpose: A configuration provider struct that resolves values from a PostgreSQL source first with an optional standalone configuration fallback, while tracking which configuration keys have been accessed via a hit counter map. [crates/gcode/src/config/services.rs:126-130]
- `hit_source` (function) component `hit_source [function]` (`a9717877-1099-5736-9ea8-4683a02da418`) lines 133-135 [crates/gcode/src/config/services.rs:133-135]
  - Signature: `fn hit_source(&self, key: &str) -> Option<&'static str> {`
  - Purpose: Retrieves an optional static string reference from the `hits` map associated with the given key. [crates/gcode/src/config/services.rs:133-135]
- `config_value` (function) component `config_value [function]` (`942fe0c8-6639-56ff-880f-f34202374a6a`) lines 139-156 [crates/gcode/src/config/services.rs:139-156]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: # Summary

This function retrieves a configuration value by hierarchically searching environment variables, PostgreSQL, and standalone YAML in priority order, while tracking the source of each successful lookup. [crates/gcode/src/config/services.rs:139-156]
- `resolve_value` (function) component `resolve_value [function]` (`0e03cae1-d6e4-55c9-bdd9-fbe4cfb36c83`) lines 158-160 [crates/gcode/src/config/services.rs:158-160]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: This instance method delegates to `ConfigSource::resolve_value()` to resolve a configuration string value using a mutable reference to the postgres configuration source. [crates/gcode/src/config/services.rs:158-160]
- `read_standalone_config_optional` (function) component `read_standalone_config_optional [function]` (`bab6d8b0-2808-57bc-9374-f31156cfadcd`) lines 163-172 [crates/gcode/src/config/services.rs:163-172]
  - Signature: `pub(crate) fn read_standalone_config_optional() -> Option<StandaloneConfig> {`
  - Purpose: Reads a standalone configuration and returns `Option<StandaloneConfig>`, returning `Some(config)` on success or `None` on any error, with non-NotFound errors logged as warnings. [crates/gcode/src/config/services.rs:163-172]
- `StandaloneConfigReadError` (type) component `StandaloneConfigReadError [type]` (`2025869c-530b-5de2-acfc-9ceac7b6aa5b`) lines 175-190 [crates/gcode/src/config/services.rs:175-190]
  - Signature: `pub(crate) enum StandaloneConfigReadError {`
  - Purpose: Indexed type `StandaloneConfigReadError` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:175-190]
- `StandaloneConfigReadError` (class) component `StandaloneConfigReadError [class]` (`b0087188-b260-582c-ab15-c85f480fb3fc`) lines 192-216 [crates/gcode/src/config/services.rs:192-216]
  - Signature: `impl fmt::Display for StandaloneConfigReadError {`
  - Purpose: Implements the `Display` trait for `StandaloneConfigReadError` to format contextual error messages for four failure modes: Gobby home directory resolution, missing config file, file read operation, and configuration parsing. [crates/gcode/src/config/services.rs:192-216]
- `StandaloneConfigReadError.fmt` (method) component `StandaloneConfigReadError.fmt [method]` (`2bfb9379-f5f4-5b1c-af1a-4c1bebff0804`) lines 193-215 [crates/gcode/src/config/services.rs:193-215]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements the `Display` trait to format human-readable error messages for a gcode configuration error enum, handling four failure variants: home directory resolution, config file not found, read errors, and parse errors. [crates/gcode/src/config/services.rs:193-215]
- `StandaloneConfigReadError` (class) component `StandaloneConfigReadError [class]` (`8e4e4d87-e10e-54f2-8f96-7ff390850c8e`) lines 218-218 [crates/gcode/src/config/services.rs:218]
  - Signature: `impl std::error::Error for StandaloneConfigReadError {}`
  - Purpose: Indexed class `StandaloneConfigReadError` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:218]
- `read_standalone_config` (function) component `read_standalone_config [function]` (`6d278f4b-ad53-5786-94c6-3cd1ddac3032`) lines 220-235 [crates/gcode/src/config/services.rs:220-235]
  - Signature: `pub(crate) fn read_standalone_config() -> Result<StandaloneConfig, StandaloneConfigReadError> {`
  - Purpose: Indexed function `read_standalone_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:220-235]
- `ClosureConfigSource` (class) component `ClosureConfigSource [class]` (`0379ee82-5f77-5559-b9b8-a76e2fda6bf1`) lines 238-241 [crates/gcode/src/config/services.rs:238-241]
  - Signature: `struct ClosureConfigSource<R, S> {`
  - Purpose: Indexed class `ClosureConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:238-241]
- `config_value` (function) component `config_value [function]` (`65852c62-c7a9-5d1d-9fb0-9fc6ad950252`) lines 249-251 [crates/gcode/src/config/services.rs:249-251]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:249-251]
- `resolve_value` (function) component `resolve_value [function]` (`12fc04f2-7460-5ebb-8536-1c38dee51dee`) lines 253-255 [crates/gcode/src/config/services.rs:253-255]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:253-255]
- `config_value` (function) component `config_value [function]` (`743a17c5-9359-51f4-967b-10ee0d1607c7`) lines 264-270 [crates/gcode/src/config/services.rs:264-270]
  - Signature: `fn config_value(&mut self, key: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Indexed function `config_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:264-270]
- `resolve_value` (function) component `resolve_value [function]` (`9d45a022-4b3f-508c-9eca-e6af37c96c2a`) lines 272-274 [crates/gcode/src/config/services.rs:272-274]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_value` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:272-274]
- `resolve_falkordb_config_from_values` (function) component `resolve_falkordb_config_from_values [function]` (`523926e7-1690-5cc7-b673-05e87a2b3fbf`) lines 278-291 [crates/gcode/src/config/services.rs:278-291]
  - Signature: `pub(super) fn resolve_falkordb_config_from_values<R, S>(`
  - Purpose: Indexed function `resolve_falkordb_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:278-291]
- `resolve_qdrant_config_from_values` (function) component `resolve_qdrant_config_from_values [function]` (`e00f9a7a-fece-5757-8288-3cbbacb9c2d7`) lines 294-307 [crates/gcode/src/config/services.rs:294-307]
  - Signature: `pub(super) fn resolve_qdrant_config_from_values<R, S>(`
  - Purpose: Indexed function `resolve_qdrant_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:294-307]
- `resolve_embedding_config_from_values` (function) component `resolve_embedding_config_from_values [function]` (`33141d32-6bc8-5e65-8efe-06ac8a6370a9`) lines 310-323 [crates/gcode/src/config/services.rs:310-323]
  - Signature: `pub(super) fn resolve_embedding_config_from_values<R, S>(`
  - Purpose: Indexed function `resolve_embedding_config_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:310-323]
- `resolve_code_vector_settings_from_values` (function) component `resolve_code_vector_settings_from_values [function]` (`adc777b9-e542-598e-8fab-875b00c2efbf`) lines 326-337 [crates/gcode/src/config/services.rs:326-337]
  - Signature: `pub(super) fn resolve_code_vector_settings_from_values<R>(`
  - Purpose: Indexed function `resolve_code_vector_settings_from_values` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:326-337]
- `resolve_falkordb_config` (function) component `resolve_falkordb_config [function]` (`890b2a87-752d-5d0f-8152-34488090abfd`) lines 342-352 [crates/gcode/src/config/services.rs:342-352]
  - Signature: `pub(super) fn resolve_falkordb_config(`
  - Purpose: Indexed function `resolve_falkordb_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:342-352]
- `resolve_falkordb_config_from_source` (function) component `resolve_falkordb_config_from_source [function]` (`739040b9-4171-55ea-81f9-f84fc990f9dc`) lines 354-369 [crates/gcode/src/config/services.rs:354-369]
  - Signature: `fn resolve_falkordb_config_from_source(`
  - Purpose: Indexed function `resolve_falkordb_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:354-369]
- `resolve_qdrant_config` (function) component `resolve_qdrant_config [function]` (`b14f66d8-fde5-573a-908b-ddf133d35105`) lines 374-384 [crates/gcode/src/config/services.rs:374-384]
  - Signature: `pub(super) fn resolve_qdrant_config(`
  - Purpose: Indexed function `resolve_qdrant_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:374-384]
- `resolve_qdrant_config_from_source` (function) component `resolve_qdrant_config_from_source [function]` (`8bd1e74a-54a0-57c3-b63b-25060269a9f3`) lines 386-395 [crates/gcode/src/config/services.rs:386-395]
  - Signature: `fn resolve_qdrant_config_from_source(`
  - Purpose: Indexed function `resolve_qdrant_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:386-395]
- `resolve_service_setting` (function) component `resolve_service_setting [function]` (`03755984-285c-57e4-915a-4cea8aeab831`) lines 397-405 [crates/gcode/src/config/services.rs:397-405]
  - Signature: `fn resolve_service_setting(`
  - Purpose: Indexed function `resolve_service_setting` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:397-405]
- `resolve_service_non_empty` (function) component `resolve_service_non_empty [function]` (`55e4f315-a103-56fa-b047-df26a822cd55`) lines 407-422 [crates/gcode/src/config/services.rs:407-422]
  - Signature: `fn resolve_service_non_empty(`
  - Purpose: Indexed function `resolve_service_non_empty` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:407-422]
- `resolve_service_port` (function) component `resolve_service_port [function]` (`17a48f35-a80a-598e-8eb9-aa38301ec306`) lines 424-447 [crates/gcode/src/config/services.rs:424-447]
  - Signature: `fn resolve_service_port(`
  - Purpose: Indexed function `resolve_service_port` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:424-447]
- `resolve_embedding_config` (function) component `resolve_embedding_config [function]` (`87e4e3ff-edb6-5489-a5be-94b63a8002ec`) lines 454-464 [crates/gcode/src/config/services.rs:454-464]
  - Signature: `pub(super) fn resolve_embedding_config(`
  - Purpose: Indexed function `resolve_embedding_config` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:454-464]
- `resolve_embedding_config_details` (function) component `resolve_embedding_config_details [function]` (`8d7d502b-0be0-5138-a1ae-bbd0411df566`) lines 466-484 [crates/gcode/src/config/services.rs:466-484]
  - Signature: `pub(crate) fn resolve_embedding_config_details(`
  - Purpose: Indexed function `resolve_embedding_config_details` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:466-484]
- `resolve_embedding_config_from_source` (function) component `resolve_embedding_config_from_source [function]` (`5f6fdbea-392e-596b-8fef-08ebf9142edc`) lines 486-496 [crates/gcode/src/config/services.rs:486-496]
  - Signature: `pub(crate) fn resolve_embedding_config_from_source(`
  - Purpose: Indexed function `resolve_embedding_config_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:486-496]
- `embedding_binding_routes_direct` (function) component `embedding_binding_routes_direct [function]` (`6a386e76-9564-5c12-ad19-e46fd2812a9d`) lines 498-507 [crates/gcode/src/config/services.rs:498-507]
  - Signature: `fn embedding_binding_routes_direct(binding: &CapabilityBinding) -> bool {`
  - Purpose: Indexed function `embedding_binding_routes_direct` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:498-507]
- `embedding_binding_uses_openai_http` (function) component `embedding_binding_uses_openai_http [function]` (`c9bca84e-f249-55e3-8578-b0f623c66bac`) lines 509-515 [crates/gcode/src/config/services.rs:509-515]
  - Signature: `fn embedding_binding_uses_openai_http(binding: &CapabilityBinding) -> bool {`
  - Purpose: Indexed function `embedding_binding_uses_openai_http` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:509-515]
- `resolve_code_vector_settings` (function) component `resolve_code_vector_settings [function]` (`7797e0f2-91e7-5b47-9f4d-ec529b1b8d9e`) lines 517-526 [crates/gcode/src/config/services.rs:517-526]
  - Signature: `pub(super) fn resolve_code_vector_settings(`
  - Purpose: Indexed function `resolve_code_vector_settings` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:517-526]
- `resolve_indexing_settings` (function) component `resolve_indexing_settings [function]` (`baec2284-bbbc-5479-92d1-642723622df2`) lines 528-535 [crates/gcode/src/config/services.rs:528-535]
  - Signature: `pub(super) fn resolve_indexing_settings(`
  - Purpose: Indexed function `resolve_indexing_settings` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:528-535]
- `resolve_code_vector_settings_from_source` (function) component `resolve_code_vector_settings_from_source [function]` (`d4038920-4a94-51e8-87d6-4b79d4bf4867`) lines 537-543 [crates/gcode/src/config/services.rs:537-543]
  - Signature: `fn resolve_code_vector_settings_from_source(`
  - Purpose: Indexed function `resolve_code_vector_settings_from_source` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:537-543]
- `resolve_vector_dim` (function) component `resolve_vector_dim [function]` (`1f5d09c3-f01f-5ee8-836f-d2822455fa95`) lines 545-556 [crates/gcode/src/config/services.rs:545-556]
  - Signature: `fn resolve_vector_dim(`
  - Purpose: Indexed function `resolve_vector_dim` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:545-556]
- `parse_vector_dim` (function) component `parse_vector_dim [function]` (`40f0a253-56b5-5d18-8ca2-415b3ca63f3a`) lines 558-567 [crates/gcode/src/config/services.rs:558-567]
  - Signature: `fn parse_vector_dim(source: &'static str, value: &str) -> Result<usize, CodeVectorConfigError> {`
  - Purpose: Indexed function `parse_vector_dim` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:558-567]

