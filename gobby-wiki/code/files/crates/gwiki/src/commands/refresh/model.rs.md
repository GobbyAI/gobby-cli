---
title: crates/gwiki/src/commands/refresh/model.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/model.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/model.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Overview

`crates/gwiki/src/commands/refresh/model.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/refresh/model.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Selection` | class | 'Selection' is a crate-visible aggregation of refresh outcomes, containing planned 'RefreshPlan' entries, skipped 'SkippedRefresh' entries, and failed 'RefreshFailure' entries. [crates/gwiki/src/commands/refresh/model.rs:5-9] |
| `ChangedRefresh` | class | 'ChangedRefresh' is an internal refresh-result container that bundles an 'IngestResult' with the prior raw path, a list of removed paths, and any degradation messages detected during the refresh. [crates/gwiki/src/commands/refresh/model.rs:12-17] |
| `RefreshSinks` | class | 'RefreshSinks<'a>' is a mutable sink bundle that holds four '&'a mut Vec<_>' accumulators for collecting refreshed sources, unchanged refresh results, refresh failures, and degradation messages during a refresh operation. [crates/gwiki/src/commands/refresh/model.rs:19-24] |
| `RefreshRender` | class | 'RefreshRender' is a render-state aggregate for a refresh operation, tracking the target scope, dry-run mode, planned/processed/unchanged/failed/skipped refresh results, index status, degradation messages, and whether the refresh was explicitly requested. [crates/gwiki/src/commands/refresh/model.rs:27-38] |
| `RefreshPlan` | class | 'RefreshPlan' is a crate-visible struct that encapsulates a single 'SourceRecord' in its 'record' field. [crates/gwiki/src/commands/refresh/model.rs:41-43] |
| `RefreshPlan::from_record` | method | Validates the 'SourceRecord' ID/path via 'raw_source_path(&record.id)?' and, if successful, constructs and returns a 'Self' containing a cloned copy of the record. [crates/gwiki/src/commands/refresh/model.rs:46-51] |
| `RefreshPlan::serialize` | method | Serializes a 'RefreshPlan' as a 6-field struct containing 'id', 'location', 'source_kind', 'replay_kind', 'raw_path', and 'content_hash', deriving 'raw_path' from 'record.id' and converting path lookup errors into Serde serialization errors. [crates/gwiki/src/commands/refresh/model.rs:55-68] |
| `RefreshedSource` | class | 'RefreshedSource' records the outcome of refreshing a source, including its old and new identifiers, location, source/replay metadata, optional final URL, raw and previous raw paths, removed paths, a change flag, and the updated 'SourceRecord'. [crates/gwiki/src/commands/refresh/model.rs:72-85] |
| `RefreshResult` | class | 'RefreshResult' is a crate-private record of a refresh operation containing the item’s identity, location, source and replay kinds, raw file path, content hash, and a 'changed' flag used to preserve output shape for unchanged entries. [crates/gwiki/src/commands/refresh/model.rs:88-98] |
| `RefreshFailure` | class | 'RefreshFailure' is an internal struct that records a refresh error with an identifier, optional location and source kind metadata, and required error code and human-readable message. [crates/gwiki/src/commands/refresh/model.rs:101-107] |
| `SkippedRefresh` | class | 'SkippedRefresh' is an internal record struct that identifies a skipped refresh event by 'id', 'location', 'source_kind', 'code', and 'message'. [crates/gwiki/src/commands/refresh/model.rs:110-116] |
| `IndexedCounts` | class | 'IndexedCounts' is a crate-private aggregate of 'usize' counters tracking the number of documents, chunks, links, sources, and ingestions in an indexed dataset. [crates/gwiki/src/commands/refresh/model.rs:119-125] |
| `IndexedCounts::from` | method | Constructs 'Self' by moving the 'documents', 'chunks', 'links', 'sources', and 'ingestions' fields directly from the provided 'IndexCounts' value. [crates/gwiki/src/commands/refresh/model.rs:128-136] |
| `IndexStatus` | class | 'IndexStatus' is an internal status record that carries a static status label, a flag indicating whether indexing is required, and an optional 'IndexedCounts' payload describing indexed state. [crates/gwiki/src/commands/refresh/model.rs:140-144] |
| `IndexStatus::not_run` | method | Constructs and returns a 'Self' instance initialized with 'status' set to '"not_run"', 'index_required' set to 'false', and 'indexed' set to 'None'. [crates/gwiki/src/commands/refresh/model.rs:147-153] |
| `IndexStatus::indexed` | method | Constructs and returns a 'Self' value representing the '"indexed"' status, with 'index_required' set to 'false' and the provided 'IndexedCounts' stored in 'indexed' as 'Some(indexed)'. [crates/gwiki/src/commands/refresh/model.rs:155-161] |
| `IndexStatus::degraded` | method | Constructs and returns a 'Self' instance with 'status' set to '"degraded"', 'index_required' set to 'false', and 'indexed' left unset ('None'). [crates/gwiki/src/commands/refresh/model.rs:163-169] |

