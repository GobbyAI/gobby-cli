---
title: crates/gwiki/src/commands/graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/graph.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/graph.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/graph.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the requested scope, obtains a read-only PostgreSQL connection from the gwiki graph index config, loads wiki graph facts, selects available or degraded export options based on degraded sources, exports graph artifacts under the scope root, and returns a scoped 'CommandOutcome' containing the artifact metadata and a success summary. [crates/gwiki/src/commands/graph.rs:13-52] |
| `degraded_optional_sources` | function | Resolves the Gobby home directory, builds an AI config source backed by the provided Postgres client and that home path, maps any configuration-resolution failures into 'WikiError::Config', and returns the degraded optional source list produced from that config source. [crates/gwiki/src/commands/graph.rs:54-67] |
| `degraded_optional_sources_from_config` | function | Returns a list of degradation flags indicating missing optional backends: it adds '"falkordb_unavailable"' when FalkorDB config cannot be resolved, and adds '"semantic_relations_unavailable"' when either embedding capability is unavailable or Qdrant config with a URL is absent. [crates/gwiki/src/commands/graph.rs:69-90] |
| `has_embedding_capability` | function | Returns whether embedding support is available for the given 'AiRouting': 'Off' is always false, 'Daemon' and 'Auto' are true when the 'ai' feature is enabled, 'Direct' is true only if 'resolve_embedding_config(source)' succeeds, and 'Auto' falls back to that config check when 'ai' is disabled. [crates/gwiki/src/commands/graph.rs:93-118] |
| `TestConfigSource` | class | 'TestConfigSource' is a test-only configuration source struct that stores key-value pairs in a 'BTreeMap<&'static str, &'static str>'. [crates/gwiki/src/commands/graph.rs:129-131] |
| `TestConfigSource::with` | method | Consumes 'self', inserts the given static key-value pair into 'self.values', and returns the updated 'Self'. [crates/gwiki/src/commands/graph.rs:134-137] |
| `TestConfigSource::config_value` | method | Returns an owned 'String' cloned from the entry associated with 'key' in 'self.values', or 'None' if the key is absent. [crates/gwiki/src/commands/graph.rs:141-143] |
| `TestConfigSource::resolve_value` | method | 'resolve_value' returns an 'Ok' result containing an owned 'String' cloned from the input '&str', performing no transformation or validation. [crates/gwiki/src/commands/graph.rs:145-147] |
| `degraded_markers` | function | Temporarily unsets the FalkorDB and Qdrant-related environment variables via 'EnvGuard' and then returns the degraded optional source markers produced by 'degraded_optional_sources_from_config(&mut source)'. [crates/gwiki/src/commands/graph.rs:150-158] |
| `falkor_config` | function | Returns a default 'TestConfigSource' with 'databases.falkordb.host' overridden to '127.0.0.1'. [crates/gwiki/src/commands/graph.rs:160-162] |
| `with_embedding_and_qdrant` | function | Returns a 'TestConfigSource' with overrides setting 'ai.embeddings.api_base' to 'http://embeddings.local/v1' and 'databases.qdrant.url' to 'http://qdrant.local'. [crates/gwiki/src/commands/graph.rs:164-168] |

_Verified by 5 in-file unit tests._

