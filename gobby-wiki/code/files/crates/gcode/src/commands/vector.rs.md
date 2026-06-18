---
title: crates/gcode/src/commands/vector.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/vector.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/vector.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

`crates/gcode/src/commands/vector.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gcode/src/commands/vector.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `lifecycle_status` | function | 'lifecycle_status' delegates to 'code_symbols::lifecycle_status' using the current context’s cloned 'project_id' and the 'CODE_SYMBOL_COLLECTION_PREFIX', returning the resulting 'CodeSymbolVectorLifecycleStatus' or 'VectorLifecycleError'. [crates/gcode/src/commands/vector.rs:16-22] |
| `lifecycle_from_context` | function | Constructs a 'CodeSymbolVectorLifecycle' from the given 'Context' by deriving the embedding source from that context and delegating to 'lifecycle_from_resolved_embedding_source', returning a 'VectorLifecycleError' on failure. [crates/gcode/src/commands/vector.rs:24-28] |
| `lifecycle_from_resolved_embedding_source` | function | Builds a 'CodeSymbolVectorLifecycle' by requiring 'Context.qdrant' and an 'EmbeddingSource', returning 'MissingQdrantConfig' or 'MissingEmbeddingConfig' if either is absent, and otherwise passing the project ID, Qdrant config, embedding source, and code vector config into 'CodeSymbolVectorLifecycle::new'. [crates/gcode/src/commands/vector.rs:30-45] |
| `sync_file` | function | 'sync_file' verifies that a file is indexed for the current project, fetches its symbols, synchronizes those symbols through the lifecycle, marks the file’s vectors as synced in the database, and prints the resulting lifecycle/report output, optionally skipping missing indexed files when allowed. [crates/gcode/src/commands/vector.rs:47-77] |
| `print_skipped_missing_indexed_file` | function | Attempts to reconcile a deleted indexed file, builds a success payload marking the vector sync as skipped because the indexed file was not found (including any reconciliation failures as a degraded error), and emits either JSON or text plus compact JSON depending on 'format'. [crates/gcode/src/commands/vector.rs:79-131] |
| `clear` | function | Connects to the project database, resets the project’s vector-sync state, clears the project vectors through the lifecycle, and prints the resulting lifecycle output with an empty successful sync report in the requested format. [crates/gcode/src/commands/vector.rs:133-140] |
| `rebuild` | function | Rebuilds a project’s symbol/vector projection by opening a read-write database connection, clearing existing vectors, fetching project symbols, regenerating symbol output via the lifecycle, marking vectors as synced, and printing a sync report in the requested format. [crates/gcode/src/commands/vector.rs:142-152] |
| `cleanup_orphans` | function | Looks up the project’s configured Qdrant client and readonly database, collects the project’s indexed file paths into a 'HashSet', invokes 'code_symbols::cleanup_orphan_file_vectors' to remove orphaned vector records not tied to those paths, and prints the cleanup report in the requested 'format'. [crates/gcode/src/commands/vector.rs:154-166] |
| `print_lifecycle_output` | function | Serializes a lifecycle payload from 'output' and 'report', then prints it as either JSON via 'output::print_json' or as text via 'output::print_text' on a JSON string, returning any serialization or I/O error as 'anyhow::Result<()>'. [crates/gcode/src/commands/vector.rs:168-178] |
| `print_orphan_cleanup` | function | Serializes a 'VectorOrphanCleanup' result into a JSON payload containing project, collection, cleanup counts, and a human-readable summary, then prints it as structured JSON for 'Format::Json' or as a JSON string for 'Format::Text'. [crates/gcode/src/commands/vector.rs:180-199] |
| `VectorLifecycleJsonPayload` | class | 'VectorLifecycleJsonPayload' is a serializable JSON payload struct that captures a project’s vector lifecycle event metadata, including projection/action context, optional file path, sync/projection status, file and symbol synchronization counts, degradation/error state, vector and delete operation counts, and a human-readable summary. [crates/gcode/src/commands/vector.rs:202-220] |
| `lifecycle_json_payload` | function | Constructs and returns a 'VectorLifecycleJsonPayload' by combining fields cloned or moved from 'CodeSymbolVectorLifecycleOutput' with sync outcome data from 'ProjectionSyncReport', while hardcoding 'projection' to '"vector"'. [crates/gcode/src/commands/vector.rs:222-244] |
| `make_ctx` | function | Constructs and returns a 'Context' populated with hardcoded default values, including a placeholder PostgreSQL URL and project path, 'project_id' set to '"project-1"', 'quiet' enabled, all optional service endpoints unset, default indexing settings, and a single-project index scope. [crates/gcode/src/commands/vector.rs:253-267] |
| `qdrant_config` | function | Returns a 'QdrantConfig' with 'url' set to 'Some("http://localhost:6333".to_string())' and 'api_key' set to 'None'. [crates/gcode/src/commands/vector.rs:269-274] |
| `daemon_embedding_source` | function | Creates an 'AiContext' for '"project-1"' with forced 'AiRouting::Daemon' and wraps it in 'EmbeddingSource::Daemon' using a primary-less 'AiConfigSource'. [crates/gcode/src/commands/vector.rs:276-292] |
| `vector_lifecycle_requires_config` | function | Verifies that vector lifecycle construction fails with 'MissingQdrantConfig' when Qdrant config is absent, fails with 'MissingEmbeddingConfig' when embedding config is absent, and succeeds when both Qdrant config and a daemon embedding source are provided. [crates/gcode/src/commands/vector.rs:295-315] |
| `lifecycle_json_contract` | function | Verifies that 'lifecycle_json_payload' serializes a 'CodeSymbolVectorLifecycleOutput' plus a 'ProjectionSyncReport' into the expected JSON contract, including the 'ok' case and a degraded variant. [crates/gcode/src/commands/vector.rs:318-382] |

