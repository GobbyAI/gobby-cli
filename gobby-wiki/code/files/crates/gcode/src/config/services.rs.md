---
title: crates/gcode/src/config/services.rs
type: code_file
provenance:
- file: crates/gcode/src/config/services.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/config/services.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

This file manages the resolution and retrieval of service-specific configuration settings for the Gcode application. It acts as a specialized adapter layer that abstracts different backend configuration stores behind unified interfaces.

At the core of this configuration layer is the ServiceConfigSource trait [crates/gcode/src/config/services.rs:24-27], which defines standard methods to retrieve raw values and resolve encrypted secrets. The file implements multiple concrete sources to handle different environments and operational modes. These include PostgresConfigSource [crates/gcode/src/config/services.rs:20-22] for reading configuration values from a PostgreSQL database, and FallbackConfigSource [crates/gcode/src/config/services.rs:64-67] which layers database lookups over a file-based standalone configuration.

## How it fits

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PostgresConfigSource` | class | 'PostgresConfigSource<'a>' is a lifetime-parametrized Rust struct that owns a mutable borrow of a 'Client', indicating it serves as a PostgreSQL-backed configuration source through an existing database connection. [crates/gcode/src/config/services.rs:20-22] |
| `ServiceConfigSource` | type | Indexed type `ServiceConfigSource` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:24-27] |
| `service_env_value` | function | Maps a small set of known service configuration keys to specific environment variable names and returns the corresponding environment value if present, otherwise 'None'. [crates/gcode/src/config/services.rs:29-39] |
| `config_store_missing` | function | Returns 'true' if any error in the chain is a 'postgres::Error' whose database error code is 'SqlState::UNDEFINED_TABLE' (indicating a missing table/config store), otherwise 'false'. [crates/gcode/src/config/services.rs:41-48] |
| `config_value` | function | Returns the decoded configuration value for 'key' from the PostgreSQL-backed config store, yielding 'Ok(None)' if the store is missing or the key is absent/un-decodable, and propagating any other read error. [crates/gcode/src/config/services.rs:51-57] |
| `resolve_value` | function | Delegates resolution of the input config value to 'secrets::resolve_config_value' using 'self.conn' and returns the resulting 'String' or an 'anyhow::Error'. [crates/gcode/src/config/services.rs:59-61] |
| `FallbackConfigSource` | class | 'FallbackConfigSource<'a>' is a configuration source that always includes a 'PostgresConfigSource<'a>' and optionally carries a 'StandaloneConfig' to use as a fallback when standalone settings are available. [crates/gcode/src/config/services.rs:64-67] |
| `config_value` | function | Returns the first available configuration value for 'key', preferring an environment-derived service value, then the Postgres config source, and finally an optional standalone config lookup, while propagating any errors from the Postgres lookup. [crates/gcode/src/config/services.rs:70-81] |
| `resolve_value` | function | Delegates resolution of 'value' to 'ServiceConfigSource::resolve_value' using 'self.postgres' as the mutable config source and returns the resulting 'anyhow::Result<String>'. [crates/gcode/src/config/services.rs:83-85] |
| `EmbeddingConfigDetails` | class | 'EmbeddingConfigDetails' is a crate-visible struct that packages an 'EmbeddingConfig' together with two ''static' string metadata fields, 'namespace' and 'source'. [crates/gcode/src/config/services.rs:89-93] |
| `TracingFallbackConfigSource` | class | 'TracingFallbackConfigSource<'a>' encapsulates a PostgreSQL-backed configuration source, an optional standalone fallback configuration, and a 'HashMap' that records string-keyed hit metadata as '&'static str' values. [crates/gcode/src/config/services.rs:95-99] |
| `hit_source` | function | Returns the ''static' string value associated with 'key' in 'self.hits', or 'None' if the key is absent. [crates/gcode/src/config/services.rs:102-104] |
| `config_value` | function | Resolves a configuration key by checking, in order, environment variables, the PostgreSQL-backed config store, and then the standalone config, recording the source of any hit in 'self.hits' before returning 'Ok(Some(value))' or 'Ok(None)'. [crates/gcode/src/config/services.rs:108-125] |
| `resolve_value` | function | Delegates resolution of 'value' to 'ServiceConfigSource::resolve_value' on 'self.postgres', returning the resolved string as 'anyhow::Result<String>'. [crates/gcode/src/config/services.rs:127-129] |
| `ErrorCapturingConfigSource` | class | 'ErrorCapturingConfigSource<'a, S>' is a wrapper around a mutable configuration source that stores the first 'anyhow::Error' encountered while reading from it in 'first_error' for later inspection. [crates/gcode/src/config/services.rs:132-135] |
| `finish` | function | Consumes 'self' and returns 'Err(self.first_error)' if an error was recorded, otherwise returns 'Ok(value)' unchanged. [crates/gcode/src/config/services.rs:138-143] |
| `config_value` | function | Returns the configuration value for 'key' from 'self.source', but if 'self.first_error' is already set or the lookup fails, it records the first error with key context and returns 'None'. [crates/gcode/src/config/services.rs:150-162] |
| `resolve_value` | function | Delegates resolution of the input string to 'self.source.resolve_value(value)' and returns the resulting 'String' or propagated 'anyhow::Error'. [crates/gcode/src/config/services.rs:164-166] |
| `read_standalone_config_optional` | function | Attempts to read the standalone config, returning 'Some(config)' on success, 'None' if the config is missing, and otherwise logging a warning for the read error before returning 'None'. [crates/gcode/src/config/services.rs:169-178] |
| `StandaloneConfigReadError` | type | Indexed type `StandaloneConfigReadError` in `crates/gcode/src/config/services.rs`. [crates/gcode/src/config/services.rs:181-196] |
| `StandaloneConfigReadError::fmt` | method | Implements 'Display'-style formatting for the error enum by matching each variant and writing a variant-specific diagnostic message, including the relevant path or source error where applicable. [crates/gcode/src/config/services.rs:199-221] |
| `read_standalone_config` | function | Reads the standalone config YAML from '$GOBBY_HOME/GCORE_CONFIG_FILENAME', mapping home resolution, missing-file, I/O read, and parse failures into 'StandaloneConfigReadError' variants. [crates/gcode/src/config/services.rs:226-241] |
| `ClosureConfigSource` | class | 'ClosureConfigSource<R, S>' is a generic configuration source that stores two closures or function objects, 'read_config_value' for retrieving a raw config value and 'resolve_value' for transforming or resolving that value. [crates/gcode/src/config/services.rs:244-247] |
| `config_value` | function | Returns the decoded configuration value for 'key' by invoking 'self.read_config_value(key)' and passing any raw result through 'gobby_core::config::decode_config_value', yielding 'None' if either lookup or decoding fails. [crates/gcode/src/config/services.rs:255-257] |
| `resolve_value` | function | Invokes the stored 'resolve_value' callback on the provided '&str' and returns its 'anyhow::Result<String>' output. [crates/gcode/src/config/services.rs:259-261] |
| `config_value` | function | Returns the first available configuration value for 'key', preferring 'service_env_value(key)' and otherwise reading the raw config via 'self.read_config_value', decoding it with 'gobby_core::config::decode_config_value', and propagating any errors as 'anyhow::Result<Option<String>>'. [crates/gcode/src/config/services.rs:270-276] |
| `resolve_value` | function | Delegates 'value' to the 'self.resolve_value' handler and returns its 'anyhow::Result<String>' output unchanged. [crates/gcode/src/config/services.rs:278-280] |
| `FallibleClosureConfigSource` | class | 'FallibleClosureConfigSource<R, S>' is a generic configuration source wrapper that stores a 'read_config_value' callback and a 'resolve_value' callback for producing config values through potentially fallible closure-based resolution. [crates/gcode/src/config/services.rs:284-287] |
| `config_value` | function | Returns the environment override for 'key' if present, otherwise reads the stored config value, decodes it via 'gobby_core::config::decode_config_value', and returns the resulting 'Option<String>' wrapped in 'anyhow::Result'. [crates/gcode/src/config/services.rs:295-301] |
| `resolve_value` | function | Delegates resolution of the input string to the 'self.resolve_value' callback and returns its 'anyhow::Result<String>' outcome. [crates/gcode/src/config/services.rs:303-305] |
| `resolve_falkordb_config_from_values` | function | Constructs a temporary 'ClosureConfigSource' from the provided value readers and returns the resolved 'FalkorConfig' by delegating to 'resolve_falkordb_config_from_source', panicking if resolution fails. [crates/gcode/src/config/services.rs:309-322] |
| `resolve_qdrant_config_from_values` | function | Builds a 'ClosureConfigSource' from the provided config-read and value-resolution closures, delegates to 'resolve_qdrant_config_from_source', and returns the resulting 'Option<QdrantConfig>' while panicking if resolution fails. [crates/gcode/src/config/services.rs:325-338] |
| `resolve_embedding_config_from_values` | function | Wraps the provided config-reading and value-resolving closures in a 'ClosureConfigSource' and delegates to 'resolve_embedding_config_from_source(None, ...)' to produce an optional 'EmbeddingConfig'. [crates/gcode/src/config/services.rs:341-354] |
| `resolve_embedding_config_from_fallible_values` | function | Wraps the provided fallible config-read and value-resolution closures in a 'FallibleClosureConfigSource' and delegates to 'resolve_embedding_config_from_service_source(None, ...)' to produce an 'anyhow::Result<Option<EmbeddingConfig>>'. [crates/gcode/src/config/services.rs:357-370] |
| `resolve_code_vector_settings_from_values` | function | Creates a 'ClosureConfigSource' that reads raw string config values via the provided 'FnMut(&str) -> Option<String>' and returns 'resolve_code_vector_settings_from_source(&mut source)', yielding either 'CodeVectorSettings' or 'CodeVectorConfigError'. [crates/gcode/src/config/services.rs:373-384] |
| `resolve_falkordb_config` | function | Creates a 'FallbackConfigSource' from the mutable PostgreSQL client and optional standalone config, then delegates to 'resolve_falkordb_config_from_source' to return a resolved 'Option<FalkorConfig>' wrapped in 'anyhow::Result'. [crates/gcode/src/config/services.rs:389-399] |
| `resolve_falkordb_config_from_source` | function | Resolves FalkorDB connection settings from a 'ServiceConfigSource', returning 'None' if the host is unset, otherwise constructing a 'FalkorConfig' with the resolved host, port defaulting to '16379', optional password, and a fixed graph name. [crates/gcode/src/config/services.rs:401-416] |
| `resolve_qdrant_config` | function | Constructs a 'FallbackConfigSource' from a mutable PostgreSQL client and an optional standalone config, then delegates to 'resolve_qdrant_config_from_source' to return an 'anyhow::Result<Option<QdrantConfig>>'. [crates/gcode/src/config/services.rs:421-431] |
| `resolve_qdrant_config_from_source` | function | Resolves 'databases.qdrant.url' and, only if present, 'databases.qdrant.api_key' from the provided service config source and returns 'Ok(Some(QdrantConfig { url, api_key }))', otherwise 'Ok(None)'. [crates/gcode/src/config/services.rs:433-442] |
| `resolve_service_setting` | function | Fetches an optional configuration value for 'key' from 'source' and, if present, delegates to 'resolve_service_non_empty' to validate/resolve it, otherwise returns 'Ok(None)'. [crates/gcode/src/config/services.rs:444-452] |
| `resolve_service_non_empty` | function | Trims the input string, returns 'Ok(None)' if it is empty after trimming, otherwise resolves it through 'source.resolve_value', trims the resolved result, and returns 'Ok(Some(...))' only when the final resolved text is still non-empty. [crates/gcode/src/config/services.rs:454-469] |
| `resolve_service_port` | function | Resolves an optional service port setting from the config source, parses it as 'u16', and falls back to the provided default while emitting a warning if the value is missing, invalid, or '0'. [crates/gcode/src/config/services.rs:471-494] |
| `resolve_embedding_config` | function | Creates a fallback config source from the PostgreSQL client and optional standalone config, then delegates to 'resolve_embedding_config_from_service_source(None, ...)' and returns its 'Result<Option<EmbeddingConfig>>'. [crates/gcode/src/config/services.rs:501-511] |
| `resolve_embedding_config_details` | function | Resolves embedding configuration by querying a tracing fallback source built from a PostgreSQL client plus optional standalone config, and if found returns 'EmbeddingConfigDetails' containing the config, the fixed AI namespace, and the source name of the 'AI_API_BASE' value. [crates/gcode/src/config/services.rs:513-533] |
| `resolve_embedding_config_from_service_source` | function | Wraps a 'ServiceConfigSource' in an error-capturing adapter, resolves an 'Option<EmbeddingConfig>' from it via 'resolve_embedding_config_from_source', and then finalizes the result by propagating any captured source error through 'finish'. [crates/gcode/src/config/services.rs:535-545] |
| `resolve_embedding_config_from_source` | function | Resolves and returns an 'EmbeddingConfig' from the given config source only when the AI embed binding uses the OpenAI HTTP backend and routes directly; otherwise it returns 'None'. [crates/gcode/src/config/services.rs:547-557] |
| `embedding_binding_routes_direct` | function | Returns 'true' only when 'binding.routing' is 'AiRouting::Auto' or 'AiRouting::Direct' and 'binding.api_base' contains a non-empty trimmed string, otherwise 'false' for 'Off' and 'Daemon'. [crates/gcode/src/config/services.rs:559-568] |
| `embedding_binding_uses_openai_http` | function | Returns 'true' when 'binding.transport' is absent, blank after trimming, or exactly '"openai_compatible_http"', and 'false' for any other transport value. [crates/gcode/src/config/services.rs:570-576] |
| `resolve_code_vector_settings` | function | Creates a 'FallbackConfigSource' from the mutable PostgreSQL client and optional standalone config, then delegates to 'resolve_code_vector_settings_from_source' to produce a 'CodeVectorSettings' result or 'CodeVectorConfigError'. [crates/gcode/src/config/services.rs:578-587] |
| `resolve_indexing_settings` | function | Resolves 'IndexingSettings' by building a layered config source from a mutable PostgreSQL client and optional standalone config, delegating to 'gobby_core::config::resolve_indexing_config', then finalizing the result while preserving the first captured configuration error. [crates/gcode/src/config/services.rs:589-603] |
| `resolve_code_vector_settings_from_source` | function | Resolves the code vector configuration by reading the embedding dimension from the given 'ServiceConfigSource' via 'resolve_vector_dim(source, embedding_keys::AI_DIM)' and returning a 'CodeVectorSettings' containing that 'vector_dim', or a 'CodeVectorConfigError' on failure. [crates/gcode/src/config/services.rs:605-611] |
| `resolve_vector_dim` | function | Resolves an optional vector dimension from a 'ServiceConfigSource' by reading the config value for 'key', converting any read failure into 'CodeVectorConfigError::Read', trimming the value, parsing it with 'parse_vector_dim', and transposing the result into 'Result<Option<usize>, CodeVectorConfigError>'. [crates/gcode/src/config/services.rs:613-624] |
| `parse_vector_dim` | function | Parses 'value' as a 'usize' and returns it only if it is greater than zero, otherwise yields 'CodeVectorConfigError::InvalidVectorDim' containing 'source' and the original string. [crates/gcode/src/config/services.rs:626-635] |

