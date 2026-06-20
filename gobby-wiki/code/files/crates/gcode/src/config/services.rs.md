---
title: crates/gcode/src/config/services.rs
type: code_file
provenance:
- file: crates/gcode/src/config/services.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/services.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/config/services.rs` exposes 53 indexed API symbols.

## How it fits

`crates/gcode/src/config/services.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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
| `config_value` | function | Returns the decoded configuration value for 'key' by invoking 'self.read_config_value(key)' and passing any raw result through 'gobby_core::config::decode_config_value', yielding 'None' if either lookup or decoding fails. [crates/gcode/src/config/services.rs:255-257] |
| `resolve_value` | function | Invokes the stored 'resolve_value' callback on the provided '&str' and returns its 'anyhow::Result<String>' output. [crates/gcode/src/config/services.rs:259-261] |

_22 more symbol(s) not shown — run `gcode outline crates/gcode/src/config/services.rs` for the full list._

_Verified by 7 in-file unit tests._

