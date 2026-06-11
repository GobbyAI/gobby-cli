---
title: crates/gcore/src/config/resolve.rs
type: code_file
provenance:
- file: crates/gcore/src/config/resolve.rs
  ranges:
  - 11-21
  - 24-75
  - 78-84
  - 87-90
  - 93-95
  - 103-112
  - 114-126
  - '130'
  - 132-143
  - 133-135
  - 137-142
  - 146-165
  - 168-174
  - 177-179
  - 182-189
  - 192-202
  - 205-240
  - 242-244
  - 247-254
  - 257-265
  - 268-279
  - 281-317
  - 319-341
  - 343-345
  - 347-350
  - 352-361
  - 363-369
  - 376-385
  - 387-389
  - 391-397
  - 399-416
  - 418-431
  - 433-441
  - 443-447
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/resolve.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

`crates/gcore/src/config/resolve.rs` exposes 34 indexed API symbols.
[crates/gcore/src/config/resolve.rs:11-21]
[crates/gcore/src/config/resolve.rs:24-75]
[crates/gcore/src/config/resolve.rs:78-84]
[crates/gcore/src/config/resolve.rs:87-90]
[crates/gcore/src/config/resolve.rs:93-95]

## API Symbols

- `decode_config_value` (function) component `decode_config_value [function]` (`ffda9bee-e2b2-5a85-b8a5-d5264597bd68`) lines 11-21 [crates/gcore/src/config/resolve.rs:11-21]
  - Signature: `pub fn decode_config_value(raw: &str) -> Option<String> {`
  - Purpose: Parses a raw string as JSON and returns the stringified value, or the original string if parsing fails, except JSON null which returns None. [crates/gcore/src/config/resolve.rs:11-21]
- `resolve_env_pattern` (function) component `resolve_env_pattern [function]` (`2eda9199-61a3-5764-9294-9e869157122f`) lines 24-75 [crates/gcore/src/config/resolve.rs:24-75]
  - Signature: `pub fn resolve_env_pattern(value: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Resolves shell-style environment variable substitutions (`${VAR}` and `${VAR:-default}`) within a string, returning the fully interpolated result or `None` if any referenced variables are unresolved. [crates/gcore/src/config/resolve.rs:24-75]
- `ConfigSource` (type) component `ConfigSource [type]` (`e7391422-76ef-5e5a-b8d7-8f4df7c06fc3`) lines 78-84 [crates/gcore/src/config/resolve.rs:78-84]
  - Signature: `pub trait ConfigSource {`
  - Purpose: Indexed type `ConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:78-84]
- `LayeredConfigSource` (class) component `LayeredConfigSource [class]` (`f22fd710-7880-5444-9a95-6558552726d1`) lines 87-90 [crates/gcore/src/config/resolve.rs:87-90]
  - Signature: `pub struct LayeredConfigSource<P, F> {`
  - Purpose: `LayeredConfigSource` is a generic struct that implements a two-tier configuration cascade by composing optional primary and fallback sources, allowing configuration resolution to fall through from the primary source to the fallback. [crates/gcore/src/config/resolve.rs:87-90]
- `new` (function) component `new [function]` (`37e2770b-91b5-5149-8ae1-24ee33aae643`) lines 93-95 [crates/gcore/src/config/resolve.rs:93-95]
  - Signature: `pub fn new(primary: Option<P>, fallback: Option<F>) -> Self {`
  - Purpose: Constructs a new instance that wraps optional primary and fallback values of generic types P and F respectively. [crates/gcore/src/config/resolve.rs:93-95]
- `config_value` (function) component `config_value [function]` (`316b2ec9-f98f-577b-8d0c-0cb02419883e`) lines 103-112 [crates/gcore/src/config/resolve.rs:103-112]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Performs a cascading lookup of a configuration value by key, attempting the primary source first and falling back to the secondary source if the primary returns `None`. [crates/gcore/src/config/resolve.rs:103-112]
- `resolve_value` (function) component `resolve_value [function]` (`221e2b27-32cb-5904-9c9e-0e6dc8a55f48`) lines 114-126 [crates/gcore/src/config/resolve.rs:114-126]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves a string value by attempting delegation to a primary resolver, then a fallback resolver, then environment pattern expansion, or returns an error if unresolved. [crates/gcore/src/config/resolve.rs:114-126]
- `EnvOnlySource` (class) component `EnvOnlySource [class]` (`65f10da6-91d2-5593-aea8-550ca546d25b`) lines 130-130 [crates/gcore/src/config/resolve.rs:130]
  - Signature: `pub struct EnvOnlySource;`
  - Purpose: `EnvOnlySource` is a zero-sized unit struct serving as a marker type for environment variable sourcing. [crates/gcore/src/config/resolve.rs:130]
- `EnvOnlySource` (class) component `EnvOnlySource [class]` (`46035bd8-d162-5096-9c80-2317202dbf62`) lines 132-143 [crates/gcore/src/config/resolve.rs:132-143]
  - Signature: `impl ConfigSource for EnvOnlySource {`
  - Purpose: `EnvOnlySource` is a `ConfigSource` implementation that resolves environment variable patterns in configuration values while rejecting secret resolution and providing no static configuration values. [crates/gcore/src/config/resolve.rs:132-143]
- `EnvOnlySource.config_value` (method) component `EnvOnlySource.config_value [method]` (`4ebcad6c-2c5b-5f22-9bbe-7bb0f8b2e4f7`) lines 133-135 [crates/gcore/src/config/resolve.rs:133-135]
  - Signature: `fn config_value(&mut self, _key: &str) -> Option<String> {`
  - Purpose: `config_value` is a stub method that accepts a configuration key and unconditionally returns `None`, providing no value retrieval functionality. [crates/gcore/src/config/resolve.rs:133-135]
- `EnvOnlySource.resolve_value` (method) component `EnvOnlySource.resolve_value [method]` (`64d4252b-1d29-5401-8681-9e1152c1d2be`) lines 137-142 [crates/gcore/src/config/resolve.rs:137-142]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Resolves environment variable patterns in a string while explicitly rejecting `$secret:` tokens and failing if the pattern cannot be resolved. [crates/gcore/src/config/resolve.rs:137-142]
- `resolve_falkordb_config` (function) component `resolve_falkordb_config [function]` (`bbbae36a-fe46-5a54-9443-eead6e94fcb3`) lines 146-165 [crates/gcore/src/config/resolve.rs:146-165]
  - Signature: `pub fn resolve_falkordb_config(source: &mut impl ConfigSource) -> Option<FalkorConfig> {`
  - Purpose: Resolves a FalkorDB configuration by extracting required host and optional port/password settings from a ConfigSource, returning None if the required host is missing. [crates/gcore/src/config/resolve.rs:146-165]
- `resolve_qdrant_config` (function) component `resolve_qdrant_config [function]` (`6701da20-752e-51c7-a0d9-f8b8018f0974`) lines 168-174 [crates/gcore/src/config/resolve.rs:168-174]
  - Signature: `pub fn resolve_qdrant_config(source: &mut impl ConfigSource) -> Option<QdrantConfig> {`
  - Purpose: Resolves Qdrant database configuration by extracting a required URL and optional API key from environment variables or config sources, returning `Some(QdrantConfig)` only if the URL is present. [crates/gcore/src/config/resolve.rs:168-174]
- `resolve_embedding_config` (function) component `resolve_embedding_config [function]` (`e96c2ca2-f13e-5ad1-b605-b8894857bd55`) lines 177-179 [crates/gcore/src/config/resolve.rs:177-179]
  - Signature: `pub fn resolve_embedding_config(source: &mut impl ConfigSource) -> Option<EmbeddingConfig> {`
  - Purpose: Resolves and returns the `EmbeddingConfig` by delegating to `resolve_embedding_config_resolution` and extracting the config field from its result. [crates/gcore/src/config/resolve.rs:177-179]
- `resolve_indexing_config` (function) component `resolve_indexing_config [function]` (`5206d024-3dbb-5113-b4af-df387497e91d`) lines 182-189 [crates/gcore/src/config/resolve.rs:182-189]
  - Signature: `pub fn resolve_indexing_config(source: &mut impl ConfigSource) -> anyhow::Result<IndexingConfig> {`
  - Purpose: Resolves and returns an IndexingConfig by determining the respect_gitignore setting from an environment variable with highest precedence, falling back to configuration source lookup, and defaulting to true. [crates/gcore/src/config/resolve.rs:182-189]
- `resolve_embedding_config_resolution` (function) component `resolve_embedding_config_resolution [function]` (`bf8edc06-b676-5f07-b47f-e21a3ac320ea`) lines 192-202 [crates/gcore/src/config/resolve.rs:192-202]
  - Signature: `pub fn resolve_embedding_config_resolution(`
  - Purpose: Resolves an embedding configuration with its namespace from a configuration source by first establishing the Embed capability binding. [crates/gcore/src/config/resolve.rs:192-202]
- `resolve_embedding_config_from_binding` (function) component `resolve_embedding_config_from_binding [function]` (`06b30412-0b2e-5b9f-8660-a0444aa2310f`) lines 205-240 [crates/gcore/src/config/resolve.rs:205-240]
  - Signature: `pub fn resolve_embedding_config_from_binding(`
  - Purpose: Constructs an `EmbeddingConfig` by extracting and validating fields from a `CapabilityBinding` while resolving additional settings from a `ConfigSource`, returning `None` if the required `api_base` is absent. [crates/gcore/src/config/resolve.rs:205-240]
- `resolve_embedding_setting` (function) component `resolve_embedding_setting [function]` (`f572b7cb-acd5-5a5d-8d3d-f503dfa2609f`) lines 242-244 [crates/gcore/src/config/resolve.rs:242-244]
  - Signature: `fn resolve_embedding_setting(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {`
  - Purpose: Resolves an embedding configuration value by delegating to the generic AI config resolver with the provided mutable config source and key. [crates/gcore/src/config/resolve.rs:242-244]
- `resolve_capability_routing` (function) component `resolve_capability_routing [function]` (`63246edd-b9f1-5f9e-9678-b546fb24f84b`) lines 247-254 [crates/gcore/src/config/resolve.rs:247-254]
  - Signature: `pub fn resolve_capability_routing(`
  - Purpose: Resolves AI routing configuration for a given capability by attempting a capability-specific lookup first, then falling back to a default routing key, returning the default value if neither is found. [crates/gcore/src/config/resolve.rs:247-254]
- `resolve_capability_binding` (function) component `resolve_capability_binding [function]` (`e0d2b5dd-c7ad-55a9-b05d-bdd549988304`) lines 257-265 [crates/gcore/src/config/resolve.rs:257-265]
  - Signature: `pub fn resolve_capability_binding(`
  - Purpose: Resolves an `AiCapability` to a `CapabilityBinding` by dispatching through a specialized handler for `AudioTranslate` capabilities or a generic base handler for all others. [crates/gcore/src/config/resolve.rs:257-265]
- `resolve_ai_tuning` (function) component `resolve_ai_tuning [function]` (`c6a274d4-e7d3-5445-a13a-9e70ee4bf709`) lines 268-279 [crates/gcore/src/config/resolve.rs:268-279]
  - Signature: `pub fn resolve_ai_tuning(source: &mut impl ConfigSource) -> AiTuning {`
  - Purpose: Resolves AI tuning configuration by parsing and validating `max_concurrency` as a positive u8 from a `ConfigSource` with a default fallback, and retrieving the `keep_alive` value. [crates/gcore/src/config/resolve.rs:268-279]
- `resolve_base_capability_binding` (function) component `resolve_base_capability_binding [function]` (`3b0cfcc9-418e-5055-ae12-653fa5aa1cff`) lines 281-317 [crates/gcore/src/config/resolve.rs:281-317]
  - Signature: `fn resolve_base_capability_binding(`
  - Purpose: Constructs a `CapabilityBinding` by resolving routing, transport, credentials, model, and provider configuration values from a `ConfigSource`, along with capability-specific optional parameters based on the `AiCapability` type. [crates/gcore/src/config/resolve.rs:281-317]
- `resolve_audio_translate_binding` (function) component `resolve_audio_translate_binding [function]` (`634225c5-2f22-5f3e-8c8c-b08f33900b9a`) lines 319-341 [crates/gcore/src/config/resolve.rs:319-341]
  - Signature: `fn resolve_audio_translate_binding(source: &mut impl ConfigSource) -> CapabilityBinding {`
  - Purpose: Resolves audio translation configuration parameters from a ConfigSource and constructs a CapabilityBinding with inheritance fallback to the AudioTranscribe capability binding. [crates/gcore/src/config/resolve.rs:319-341]
- `resolve_ai_routing_value` (function) component `resolve_ai_routing_value [function]` (`44993501-8a4a-50c0-8eb8-ca4f80f9278d`) lines 343-345 [crates/gcore/src/config/resolve.rs:343-345]
  - Signature: `fn resolve_ai_routing_value(source: &mut impl ConfigSource, config_key: &str) -> Option<AiRouting> {`
  - Purpose: Retrieves a configuration value from the provided source and attempts to parse it into an `AiRouting` type, returning `Some` if successful or `None` if retrieval or parsing fails. [crates/gcore/src/config/resolve.rs:343-345]
- `resolve_ai_config_value` (function) component `resolve_ai_config_value [function]` (`339c4ec7-135a-5dba-9255-25d0ecd92654`) lines 347-350 [crates/gcore/src/config/resolve.rs:347-350]
  - Signature: `fn resolve_ai_config_value(source: &mut impl ConfigSource, config_key: &str) -> Option<String> {`
  - Purpose: Fetches a configuration value by key from the provided source and resolves it through non-empty validation, returning an `Option<String>`. [crates/gcore/src/config/resolve.rs:347-350]
- `resolve_config_bool` (function) component `resolve_config_bool [function]` (`c3b16c9c-a11e-5794-9d69-b252278e7153`) lines 352-361 [crates/gcore/src/config/resolve.rs:352-361]
  - Signature: `fn resolve_config_bool(`
  - Purpose: Retrieves, resolves, and parses a configuration value as a boolean, returning `Ok(Some(bool))` if the key exists or `Ok(None)` otherwise. [crates/gcore/src/config/resolve.rs:352-361]
- `parse_config_bool` (function) component `parse_config_bool [function]` (`912e0010-1a2d-53bd-8d5e-b9ac1ee4fd89`) lines 363-369 [crates/gcore/src/config/resolve.rs:363-369]
  - Signature: `fn parse_config_bool(config_key: &'static str, value: &str) -> anyhow::Result<bool> {`
  - Purpose: Parses a string configuration value into a boolean by matching case-insensitive common boolean representations ("true"/"yes"/"on"/"1" or "false"/"no"/"off"/"0"), returning an error for unrecognized values. [crates/gcore/src/config/resolve.rs:363-369]
- `resolve_ai_non_empty` (function) component `resolve_ai_non_empty [function]` (`48fa415c-3b76-5426-8445-f01934f17b86`) lines 376-385 [crates/gcore/src/config/resolve.rs:376-385]
  - Signature: `fn resolve_ai_non_empty(source: &mut impl ConfigSource, value: &str) -> Option<String> {`
  - Purpose: Resolves a configuration value through a provided source and returns the trimmed result only if non-empty and containing no unresolved environment patterns, else `None`. [crates/gcore/src/config/resolve.rs:376-385]
- `contains_unresolved_env_pattern` (function) component `contains_unresolved_env_pattern [function]` (`eff70cd3-08b2-599f-b96d-619aa430f10d`) lines 387-389 [crates/gcore/src/config/resolve.rs:387-389]
  - Signature: `fn contains_unresolved_env_pattern(value: &str) -> bool {`
  - Purpose: Determines whether a string contains an unresolved environment variable pattern by checking for the presence of the `"${"` delimiter. [crates/gcore/src/config/resolve.rs:387-389]
- `resolve_setting` (function) component `resolve_setting [function]` (`b279e2f3-e510-5653-a005-ca8577aa259d`) lines 391-397 [crates/gcore/src/config/resolve.rs:391-397]
  - Signature: `fn resolve_setting(`
  - Purpose: Resolves and returns an optional string configuration value from a config source by delegating to `resolve_setting_from_keys` with a single config key. [crates/gcore/src/config/resolve.rs:391-397]
- `resolve_setting_from_keys` (function) component `resolve_setting_from_keys [function]` (`97e5d1b0-bade-530f-a15f-80a2d2fbdf98`) lines 399-416 [crates/gcore/src/config/resolve.rs:399-416]
  - Signature: `fn resolve_setting_from_keys(`
  - Purpose: Resolves a configuration setting by checking an environment variable first, then sequentially checking configuration keys in order, returning the first non-empty resolved value or `None`. [crates/gcore/src/config/resolve.rs:399-416]
- `resolve_port` (function) component `resolve_port [function]` (`68387b83-61df-5b11-876c-54ae3f646279`) lines 418-431 [crates/gcore/src/config/resolve.rs:418-431]
  - Signature: `fn resolve_port(`
  - Purpose: Resolves a u16 port number by attempting to retrieve and parse a value from an environment variable or configuration source, with cascading fallback to a default value on missing or invalid input. [crates/gcore/src/config/resolve.rs:418-431]
- `resolve_non_empty` (function) component `resolve_non_empty [function]` (`56309949-ff75-5e67-aecb-4cccd97d8208`) lines 433-441 [crates/gcore/src/config/resolve.rs:433-441]
  - Signature: `fn resolve_non_empty(source: &mut impl ConfigSource, value: &str) -> Option<String> {`
  - Purpose: Resolves a configuration value through a ConfigSource, returning the resolved string only if both the input value and resolved result are non-empty after trimming whitespace. [crates/gcore/src/config/resolve.rs:433-441]
- `env_value` (function) component `env_value [function]` (`378a6648-e1de-5793-a853-b8e8983288ba`) lines 443-447 [crates/gcore/src/config/resolve.rs:443-447]
  - Signature: `fn env_value(key: &str) -> Option<String> {`
  - Purpose: Retrieves an environment variable by key and returns `Some(value)` only if the variable exists and contains non-whitespace content after trimming, otherwise `None`. [crates/gcore/src/config/resolve.rs:443-447]

