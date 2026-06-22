---
title: crates/gwiki/src/commands/trust.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/trust.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/trust.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/trust.rs` exposes 21 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/trust.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the selected scope context, gathers runtime status, index counts, health, and audit data, builds a 'TrustReport', serializes it to JSON, and returns a scoped 'CommandOutcome' for the 'trust' command. [crates/gwiki/src/commands/trust.rs:14-46] |
| `IndexCountsOutcome` | class | 'IndexCountsOutcome' is a struct that bundles an 'IndexCounts' value with the backend identifier used to produce it and a list of degradation messages describing any fallback or reduced-fidelity conditions. [crates/gwiki/src/commands/trust.rs:48-52] |
| `load_index_counts` | function | 'load_index_counts' tries to obtain index counts from a read-only PostgreSQL backend configured for “gwiki trust” and, if that fails or is unavailable, logs the degradation cause and falls back to computing memory-based counts from 'root' using local index options, returning an 'IndexCountsOutcome' that records the backend used and any degradations. [crates/gwiki/src/commands/trust.rs:54-94] |
| `memory_index_counts` | function | Creates a default in-memory wiki store, indexes the given directory into it when 'root' is a directory using the provided 'IndexOptions', and returns the resulting index counts. [crates/gwiki/src/commands/trust.rs:96-105] |
| `TrustReport` | class | 'TrustReport' is a data-carrier struct that summarizes a trust evaluation for a scoped root path, including command/runtime metadata, service and index counts, degradation and freshness status, audit and link summaries, graph metrics, and overall health. [crates/gwiki/src/commands/trust.rs:108-123] |
| `TrustReport::from_parts` | method | 'from_parts' constructs a 'Self' value by deriving index trust metrics, freshness, audit, link, health, graph, degradation, and trust-status summaries from the provided scope, paths, runtime, services, index counts, health report, and audit report. [crates/gwiki/src/commands/trust.rs:126-196] |
| `TrustIndexCounts` | class | 'TrustIndexCounts' is a struct that holds a backend identifier and five 'usize' counters for documents, chunks, links, sources, and ingestions. [crates/gwiki/src/commands/trust.rs:200-207] |
| `TrustIndexCounts::from_counts` | method | Constructs a new instance by setting 'backend' and copying the 'documents', 'chunks', 'links', 'sources', and 'ingestions' fields directly from the provided 'counts::IndexCounts'. [crates/gwiki/src/commands/trust.rs:210-219] |
| `FreshnessSummary` | class | 'FreshnessSummary' is a struct that records the number of stale pages and stale citations as 'usize' fields and a 'fresh' boolean indicating whether the overall set is current. [crates/gwiki/src/commands/trust.rs:223-227] |
| `AuditSummary` | class | 'AuditSummary' is a struct that records a static state label plus counts of unsupported claims and source contexts. [crates/gwiki/src/commands/trust.rs:230-234] |
| `LinkSummary` | class | 'LinkSummary' is a struct that records two link-quality metrics: the number of broken links and the number of duplicate concepts, both stored as 'usize' counts. [crates/gwiki/src/commands/trust.rs:237-240] |
| `GraphMetrics` | class | 'GraphMetrics' is a struct that records the number of wiki links as a 'usize' and whether FalkorDB is configured as a 'bool'. [crates/gwiki/src/commands/trust.rs:243-246] |
| `HealthSummary` | class | 'HealthSummary' is a struct that aggregates six 'usize' health metrics for a dataset or knowledge base: stale page count, stale citation count, uncited source count, uncompiled source count, broken link count, and duplicate concept count. [crates/gwiki/src/commands/trust.rs:249-256] |
| `degradation_labels` | function | 'degradation_labels' merges the input 'index_degradations' with additional deduplicated degradation labels derived from service configuration and summary health signals, adding flags for unconfigured core services, empty indexes, stale content, unsupported claims, broken links, duplicate concepts, uncited sources, and uncompiled sources, then returns the labels as a sorted 'Vec<String>'. [crates/gwiki/src/commands/trust.rs:258-295] |
| `trust_status` | function | Returns a static trust-status label by prioritizing 'unindexed' when there are no documents, 'attention_required' when any audit/link/health/freshness check fails, 'clean' when there are no degradations, and otherwise 'degraded'. [crates/gwiki/src/commands/trust.rs:297-319] |
| `audit_state` | function | Returns '"clean"' when 'unsupported_claim_count' is '0', otherwise returns '"unsupported_claims"'. [crates/gwiki/src/commands/trust.rs:321-327] |
| `service_configured` | function | Returns 'true' only if 'services[service]["configured"]' exists and is a boolean 'true', otherwise returns 'false'. [crates/gwiki/src/commands/trust.rs:329-335] |
| `render_text` | function | Formats a 'TrustReport' into a multi-line plain-text status summary listing trust status, scope, runtime, index document/chunk counts and backend, freshness stale-page/citation counts, unsupported-claim count, broken-link count, and a comma-joined degradations list or 'none' if empty. [crates/gwiki/src/commands/trust.rs:337-357] |
| `indexed_counts` | function | Returns a 'TrustIndexCounts' struct with fixed in-memory index counts: 'documents = 1', 'chunks = 2', 'links = 3', 'sources = 1', and 'ingestions = 1'. [crates/gwiki/src/commands/trust.rs:364-373] |

_Verified by 2 in-file unit tests._

