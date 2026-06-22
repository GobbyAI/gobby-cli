---
title: crates/gwiki/src/commands/index.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/index.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/index.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/index.rs` exposes 35 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/index.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `IndexReport` | class | 'IndexReport' is a struct that aggregates index-related metrics by holding an 'IndexCounts' value and a list of 'DegradationKind' entries describing detected degradations. [crates/gwiki/src/commands/index.rs:35-38] |
| `execute` | function | Resolves the selected command scope, verifies it is the scope root, derives its identity, builds an index report for the resolved scope, and returns the rendered 'CommandOutcome'. [crates/gwiki/src/commands/index.rs:40-46] |
| `index_resolved_scope` | function | Returns the 'IndexCounts' for a 'ResolvedScope' by delegating to 'index_resolved_scope_report(scope)' and extracting its '.counts', propagating any 'WikiError' from the report generation. [crates/gwiki/src/commands/index.rs:48-52] |
| `index_resolved_scope_report` | function | Indexes the vault rooted at a 'ResolvedScope' into either a PostgreSQL-backed search store with optional Qdrant/Falkor synchronization and returns an 'IndexReport', or falls back to an in-memory index and report when no database URL is configured. [crates/gwiki/src/commands/index.rs:54-86] |
| `execute_ingest_file` | function | Initializes the resolved vault scope, resolves AI and ingestion settings from Postgres/gobby-home, ingests the given file path into the PostgreSQL-backed search store for that scope, and then synchronizes Qdrant vectors before returning the command outcome. [crates/gwiki/src/commands/index.rs:88-153] |
| `execute_ingest_url` | function | Resolves the command scope, ensures vault paths exist, timestamps the ingest, then ingests the provided URLs into either the PostgreSQL-backed index or an in-memory store, synchronizes vector/graph indexes when any URLs are accepted, and returns a rendered 'CommandOutcome' with the resulting counts. [crates/gwiki/src/commands/index.rs:155-191] |
| `resolve_ingest_ai_context` | function | Resolves an 'AiContext' from an optional 'project_id' and mutable config source, clones and fills in any missing 'IngestFileOptions' video frame interval from configuration, applies the options to the context, and returns both as a 'Result'. [crates/gwiki/src/commands/index.rs:193-205] |
| `resolve_ingest_file_ai_context` | function | Resolves ingest-time AI context and normalized ingest options for a scope by loading AI config from a Postgres-backed primary source when a database URL is available for the command, otherwise from local gobby home config, and wraps any config resolution failures in 'WikiError::Config'. [crates/gwiki/src/commands/index.rs:207-229] |
| `resolve_video_frame_interval_seconds` | function | Resolves 'VIDEO_FRAME_INTERVAL_KEY' from the config source, falling back to 'ingest::video::DEFAULT_FRAME_INTERVAL_SECONDS' when unset, and otherwise parses the resolved trimmed value as a nonzero 'u32' with 'WikiError::Config' on resolution or validation failure. [crates/gwiki/src/commands/index.rs:231-254] |
| `ai_project_id` | function | Returns a cloned project ID string when 'scope.kind' is 'ScopeKind::Project', otherwise 'None'. [crates/gwiki/src/commands/index.rs:256-258] |
| `ai_project_id_for_search` | function | Returns a cloned 'project_id' only when 'scope' is 'SearchScope::Project', and returns 'None' for 'Global' and 'Topic' scopes. [crates/gwiki/src/commands/index.rs:260-266] |
| `gobby_home` | function | Returns 'gobby_core::gobby_home()' on success, and converts any resolution error into 'WikiError::Config' with a formatted message indicating failure to resolve the Gobby home for gwiki AI config. [crates/gwiki/src/commands/index.rs:268-272] |
| `connect_postgres_index` | function | Connects to PostgreSQL using 'gobby_core::postgres::connect_readwrite' with the given 'database_url', mapping any connection failure into 'WikiError::Config' that includes the 'command' name and the underlying error. [crates/gwiki/src/commands/index.rs:274-281] |
| `postgres_store_for_search` | function | Constructs and returns a 'store::PostgresWikiStore' tied to the provided mutable PostgreSQL 'Client', using the scope derived from 'search_scope' via 'store_scope_for_search'. [crates/gwiki/src/commands/index.rs:283-288] |
| `sync_falkor_graph` | function | Resolves FalkorDB configuration from Gobby home and PostgreSQL, then attempts to sync the provided search scope into FalkorDB, returning 'None' on success or a 'DegradationKind' if FalkorDB is unconfigured or graph sync fails. [crates/gwiki/src/commands/index.rs:290-314] |
| `sync_qdrant_vectors` | function | Resolves embedding and Qdrant configuration from Gobby/AI settings, then syncs wiki vector chunks from PostgreSQL into Qdrant for the given search scope, returning a degradation marker instead of failing when config is missing or the Qdrant sync errors. [crates/gwiki/src/commands/index.rs:316-367] |
| `qdrant_sync_degradation` | function | Maps a 'vector::WikiVectorError' to a 'DegradationKind' by delegating to 'unreachable_degradation(QDRANT_SERVICE, error)'. [crates/gwiki/src/commands/index.rs:369-371] |
| `not_configured_degradation` | function | Returns a 'DegradationKind' by delegating to 'service_unavailable_degradation' with the given service name and 'ServiceState::NotConfigured'. [crates/gwiki/src/commands/index.rs:373-375] |
| `unreachable_degradation` | function | Returns a 'DegradationKind' by converting the given 'error' to a string and delegating to 'service_unavailable_degradation' with 'ServiceState::Unreachable { message }' for the specified 'service'. [crates/gwiki/src/commands/index.rs:377-387] |
| `service_unavailable_degradation` | function | Constructs and returns a 'DegradationKind::ServiceUnavailable' value by converting the static service name to an owned 'String' and pairing it with the provided 'ServiceState'. [crates/gwiki/src/commands/index.rs:389-394] |
| `resolve_vector_embedding` | function | 'resolve_vector_embedding' selects and constructs an optional 'SemanticEmbedding' based on the effective AI routing mode, returning 'None' when embeddings are off or unsupported, a daemon-backed embedding when routed to the daemon and the 'ai' feature is enabled, or a direct embedding resolved from 'source' when routed directly or when 'Auto' falls back without 'ai'. [crates/gwiki/src/commands/index.rs:396-431] |
| `effective_embedding_route` | function | Returns the effective embedding routing for an 'AiContext', delegating to 'effective_route(..., AiCapability::Embed)' when 'ai' support is enabled, and otherwise mapping the configured embed route to 'Off'/'Direct' with warnings that 'Daemon' is disabled and 'Auto' falls back to 'Direct'. [crates/gwiki/src/commands/index.rs:433-457] |
| `indexed_counts_for_postgres` | function | Returns PostgreSQL index counts for the given search scope when 'should_count' is true, otherwise returns a default 'IndexCounts' without querying the database. [crates/gwiki/src/commands/index.rs:459-469] |
| `render_index` | function | 'render_index' formats an 'IndexReport' into a scoped 'CommandOutcome' by building a JSON payload with the '"index"' command, '"indexed"' counts, and degradations, then generating a human-readable completion summary that includes the scope, counts, and a comma-separated degradation list or '"none"'. [crates/gwiki/src/commands/index.rs:471-512] |

_7 more symbol(s) not shown — run `gcode outline crates/gwiki/src/commands/index.rs` for the full list._

_Verified by 4 in-file unit tests._

