---
title: crates/gcore/src/config/resolve.rs
type: code_file
provenance:
- file: crates/gcore/src/config/resolve.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/resolve.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Overview

`crates/gcore/src/config/resolve.rs` exposes 34 indexed API symbols.

## How it fits

`crates/gcore/src/config/resolve.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `decode_config_value` | function | Parses 'raw' as JSON and returns 'None' for 'null', the inner string for JSON strings, a canonical JSON serialization for arrays/objects, 'to_string()' for other JSON scalars, and the original input on parse failure. [crates/gcore/src/config/resolve.rs:11-21] |
| `resolve_env_pattern` | function | Resolves '${VAR}' and '${VAR:-default}' placeholders in a string by substituting environment values or defaults, returning 'Ok(Some(resolved))' when all variables are satisfied, 'Ok(None)' when at least one placeholder is unresolved without a default, and an error for malformed patterns or non-unicode environment values. [crates/gcore/src/config/resolve.rs:24-75] |
| `ConfigSource` | type | Indexed type `ConfigSource` in `crates/gcore/src/config/resolve.rs`. [crates/gcore/src/config/resolve.rs:78-84] |
| `LayeredConfigSource` | class | 'LayeredConfigSource<P, F>' is a generic configuration source wrapper that holds an optional primary source and an optional fallback source, enabling layered resolution of configuration data. [crates/gcore/src/config/resolve.rs:87-90] |
| `new` | function | Constructs a new instance by storing the provided 'primary' and 'fallback' optional values into the struct fields and returning 'Self'. [crates/gcore/src/config/resolve.rs:93-95] |
| `config_value` | function | Returns the first 'config_value(key)' from 'self.primary' if present, otherwise falls back to 'self.fallback', yielding 'None' if neither source produces a value. [crates/gcore/src/config/resolve.rs:103-112] |
| `resolve_value` | function | Resolves 'value' by delegating to 'primary' if present, otherwise to 'fallback' if present, and if neither exists attempts environment-pattern expansion via 'resolve_env_pattern', returning an error when the pattern remains unresolved. [crates/gcore/src/config/resolve.rs:114-126] |
| `EnvOnlySource` | class | 'EnvOnlySource' is a zero-sized public struct type that serves as an environment-only source marker or implementation handle. [crates/gcore/src/config/resolve.rs:130] |
| `EnvOnlySource::config_value` | method | 'config_value' is a placeholder accessor that ignores the provided key and always returns 'None', indicating no configuration value is available. [crates/gcore/src/config/resolve.rs:133-135] |
| `EnvOnlySource::resolve_value` | method | Returns the input string after resolving any environment-variable patterns via 'resolve_env_pattern', but rejects values containing '"$secret:"' with an error and errors if no pattern is resolved. [crates/gcore/src/config/resolve.rs:137-142] |
| `resolve_falkordb_config` | function | Resolves FalkorDB connection settings from environment or config keys, requiring 'host', defaulting 'port' via 'FALKORDB_DEFAULT_PORT', and optionally including 'password', then returns a 'FalkorConfig' if the host is present. [crates/gcore/src/config/resolve.rs:146-165] |
| `resolve_qdrant_config` | function | Returns 'None' unless a Qdrant URL is resolved from 'GOBBY_QDRANT_URL' or 'databases.qdrant.url', otherwise constructs 'Some(QdrantConfig)' with that URL and an optionally resolved API key from 'GOBBY_QDRANT_API_KEY' or 'databases.qdrant.api_key'. [crates/gcore/src/config/resolve.rs:168-174] |
| `resolve_embedding_config` | function | Returns the resolved embedding configuration from the given 'ConfigSource' by delegating to 'resolve_embedding_config_resolution' and extracting its 'config' field, or 'None' if no resolution is available. [crates/gcore/src/config/resolve.rs:177-179] |
| `resolve_indexing_config` | function | Resolves 'IndexingConfig' by determining 'respect_gitignore' from the 'INDEXING_RESPECT_GITIGNORE_ENV' environment variable if set, otherwise from the 'INDEXING_RESPECT_GITIGNORE_KEY' config value with a default of 'true', and returns the resulting config. [crates/gcore/src/config/resolve.rs:182-189] |
| `resolve_embedding_config_resolution` | function | Resolves the 'AiCapability::Embed' capability binding from the given config source, derives an embedding config from that binding, and returns it wrapped in 'EmbeddingConfigResolution' with 'embedding_keys::AI_NAMESPACE', or 'None' if resolution fails. [crates/gcore/src/config/resolve.rs:192-202] |
| `resolve_embedding_config_from_binding` | function | Constructs an 'EmbeddingConfig' from a 'CapabilityBinding' by requiring a non-empty trimmed 'api_base', using a trimmed 'model' or the default embedding model, optionally capturing a trimmed 'api_key', resolving 'query_prefix' and 'timeout_seconds' from the 'ConfigSource' with a default timeout fallback, and returning 'None' if 'api_base' is missing or blank. [crates/gcore/src/config/resolve.rs:205-240] |
| `resolve_embedding_setting` | function | Returns the optional embedding setting by delegating lookup of 'config_key' to 'resolve_ai_config_value' on the provided 'ConfigSource'. [crates/gcore/src/config/resolve.rs:242-244] |
| `resolve_capability_routing` | function | Returns the 'AiRouting' for a given capability by looking up its capability-specific routing key in 'source', falling back to the global 'ai_keys::ROUTING' value, and finally defaulting if neither is set. [crates/gcore/src/config/resolve.rs:247-254] |
| `resolve_capability_binding` | function | Dispatches capability binding resolution by calling a dedicated audio-translate resolver for 'AiCapability::AudioTranslate' and otherwise delegating to the generic base capability binding resolver with the provided mutable 'ConfigSource'. [crates/gcore/src/config/resolve.rs:257-265] |
| `resolve_ai_tuning` | function | Resolves AI tuning by parsing 'max_concurrency' as a positive 'u8' from config and falling back to 'AI_DEFAULT_MAX_CONCURRENCY' on missing or invalid input, while passing through the configured 'keep_alive' value into an 'AiTuning' struct. [crates/gcore/src/config/resolve.rs:268-279] |
| `resolve_base_capability_binding` | function | The 'resolve_base_capability_binding' function resolves and constructs a 'CapabilityBinding' from a mutable configuration source for a given 'AiCapability' by populating shared routing, transport, and credential values along with capability-specific fields determined via pattern matching on the capability variant. [crates/gcore/src/config/resolve.rs:281-347] |
| `resolve_audio_translate_binding` | function | The 'resolve_audio_translate_binding' function resolves and constructs a 'CapabilityBinding' for audio translation by retrieving specific configuration values from a 'ConfigSource' and falling back to base configuration values inherited from 'AiCapability::AudioTranscribe' where unspecified. [crates/gcore/src/config/resolve.rs:349-376] |
| `resolve_ai_routing_value` | function | This function retrieves a configuration value for a given key from a mutable 'ConfigSource' via 'resolve_ai_config_value' and parses it, returning 'Some(AiRouting)' upon successful parsing or 'None' otherwise. [crates/gcore/src/config/resolve.rs:378-380] |
| `resolve_ai_config_value` | function | This function retrieves a configuration value associated with a specified key from a mutable 'ConfigSource' implementation and, if present, resolves and returns it as an optional string via 'resolve_ai_non_empty'. [crates/gcore/src/config/resolve.rs:382-385] |

_10 more symbol(s) not shown — run `gcode outline crates/gcore/src/config/resolve.rs` for the full list._

