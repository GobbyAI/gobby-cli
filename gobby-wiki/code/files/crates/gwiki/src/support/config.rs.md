---
title: crates/gwiki/src/support/config.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/config.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/config.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/config.rs` exposes 30 indexed API symbols.

## How it fits

`crates/gwiki/src/support/config.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HubPrimary` | class | 'HubPrimary' is a crate-visible struct that wraps an optional 'Client' connection in the 'conn' field. [crates/gwiki/src/support/config.rs:18-20] |
| `HubPrimary::config_value` | method | Returns the decoded configuration value for 'key' from the active PostgreSQL connection, yielding 'None' if there is no connection, the lookup fails, or the raw value cannot be decoded. [crates/gwiki/src/support/config.rs:23-29] |
| `HubPrimary::resolve_value` | method | Resolves a configuration string through 'gobby_core::secrets::resolve_config_value' when a PostgreSQL connection is available, otherwise returns the literal string unchanged unless it begins with '$secret:', in which case it errors because secret resolution requires the PostgreSQL hub. [crates/gwiki/src/support/config.rs:31-43] |
| `hub_ai_config_source` | function | Resolves the Gobby home and an optional read-write PostgreSQL connection for the given command, then builds an 'AiConfigSource<HubPrimary>' from that home path, mapping any failure into a 'WikiError::Config' with command-specific context. [crates/gwiki/src/support/config.rs:46-61] |
| `SharedCodeGraphLimits` | class | 'SharedCodeGraphLimits' is a crate-visible struct that stores two 'usize' thresholds, 'call_edge_limit' and 'import_edge_limit', for bounding call and import edges in a shared code graph. [crates/gwiki/src/support/config.rs:68-71] |
| `SharedCodeGraphLimits::default` | method | Returns a 'Self' instance initialized with 'call_edge_limit' and 'import_edge_limit' both set to 'DEFAULT_SHARED_CODE_GRAPH_EDGE_LIMIT'. [crates/gwiki/src/support/config.rs:74-79] |
| `local_index_options` | function | Reads the standalone configuration, layers it with environment-only settings, and resolves that combined source into 'IndexOptions', propagating any 'WikiError' encountered. [crates/gwiki/src/support/config.rs:82-86] |
| `index_options_from_conn` | function | Loads the standalone configuration, layers it over a 'PostgresConfigSource' backed by the provided 'Client', and resolves 'IndexOptions' from the combined config source. [crates/gwiki/src/support/config.rs:88-93] |
| `shared_code_graph_limits_from_conn` | function | Reads the standalone configuration, layers it over a PostgreSQL-backed config source from 'conn', and resolves 'SharedCodeGraphLimits' through 'resolve_shared_code_graph_limits', returning any 'WikiError'. [crates/gwiki/src/support/config.rs:104-111] |
| `qdrant_config_has_url` | function | Returns 'true' if 'config.url' is 'Some' and its string value is not blank after trimming whitespace, otherwise 'false'. [crates/gwiki/src/support/config.rs:113-118] |
| `read_standalone_config` | function | Resolves the Gobby home directory, then reads the standalone configuration from the gcore config path there, mapping any failure into a 'WikiError::Config' with contextual detail. [crates/gwiki/src/support/config.rs:120-127] |
| `resolve_index_options` | function | Resolves the indexing configuration from a mutable 'ConfigSource', maps any resolution failure into a 'WikiError::Config' with context, and converts the resulting config into 'IndexOptions'. [crates/gwiki/src/support/config.rs:129-136] |
| `index_options_from_config` | function | Constructs an 'indexer::IndexOptions' from 'gobby_core::config::IndexingConfig' by copying the 'respect_gitignore' field into the corresponding option. [crates/gwiki/src/support/config.rs:138-142] |
| `resolve_shared_code_graph_limits` | function | Constructs and returns a 'SharedCodeGraphLimits' by resolving the 'call_edge_limit' and 'import_edge_limit' from the provided 'ConfigSource' using their respective keys, propagating any 'WikiError' from limit resolution. [crates/gwiki/src/support/config.rs:144-151] |
| `resolve_limit` | function | Returns the configured limit for 'key' by fetching the raw config value from 'source', resolving any indirections, trimming it, and parsing it as a 'usize', or falling back to 'DEFAULT_SHARED_CODE_GRAPH_EDGE_LIMIT' when the key is unset, with config-specific errors on resolution or parse failure. [crates/gwiki/src/support/config.rs:153-168] |
| `EnvGuard` | class | 'EnvGuard' is an RAII guard that holds a global mutex lock and stores an optional previous environment variable value so the environment can be restored when the guard is dropped. [crates/gwiki/src/support/config.rs:182-185] |
| `EnvGuard::set_gobby_home` | method | Acquires 'ENV_LOCK', saves the current 'GOBBY_HOME' value, sets 'GOBBY_HOME' to the given 'path' for the duration of the returned guard, and stores the lock plus previous value so it can be restored on 'Drop'. [crates/gwiki/src/support/config.rs:188-200] |
| `EnvGuard::drop` | method | On drop, it restores the process 'GOBBY_HOME' environment variable to its previously saved value if present, otherwise removes it, using unsafe 'std::env' mutation under 'ENV_LOCK' serialization. [crates/gwiki/src/support/config.rs:204-211] |
| `write_file` | function | 'write_file' joins 'rel' to 'root', creates any missing parent directories for the target path, and then writes 'contents' to that file, panicking on any filesystem error. [crates/gwiki/src/support/config.rs:214-220] |
| `TestSource` | class | 'TestSource' is a data-only Rust struct that stores a 'BTreeMap<String, String>' named 'values' for key-value string pairs. [crates/gwiki/src/support/config.rs:223-225] |
| `TestSource::with` | method | Consumes 'self', inserts the provided 'key' and 'value' as owned 'String's into 'self.values', and returns the modified instance for chaining. [crates/gwiki/src/support/config.rs:228-231] |
| `TestSource::config_value` | method | Returns a cloned 'String' from 'self.values' for the given 'key', or 'None' if the key is absent. [crates/gwiki/src/support/config.rs:235-237] |
| `TestSource::resolve_value` | method | Returns 'Ok' containing a newly allocated 'String' cloned from the input 'value', performing no transformation or validation. [crates/gwiki/src/support/config.rs:239-241] |

_Verified by 7 in-file unit tests._

