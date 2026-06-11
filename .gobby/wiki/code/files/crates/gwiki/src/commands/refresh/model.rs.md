---
title: crates/gwiki/src/commands/refresh/model.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/refresh/model.rs
  ranges:
  - 5-9
  - 12-17
  - 19-24
  - 27-38
  - 41-43
  - 45-52
  - 46-51
  - 54-69
  - 55-68
  - 72-85
  - 88-98
  - 101-107
  - 110-116
  - 119-125
  - 127-137
  - 128-136
  - 140-144
  - 146-170
  - 147-153
  - 155-161
  - 163-169
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/refresh/model.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

`crates/gwiki/src/commands/refresh/model.rs` exposes 21 indexed API symbols.
[crates/gwiki/src/commands/refresh/model.rs:5-9]
[crates/gwiki/src/commands/refresh/model.rs:12-17]
[crates/gwiki/src/commands/refresh/model.rs:19-24]
[crates/gwiki/src/commands/refresh/model.rs:27-38]
[crates/gwiki/src/commands/refresh/model.rs:41-43]

## API Symbols

- `Selection` (class) component `Selection [class]` (`43669b6c-7faf-5bd2-afb3-d105e22ba108`) lines 5-9 [crates/gwiki/src/commands/refresh/model.rs:5-9]
  - Signature: `pub(crate) struct Selection {`
  - Purpose: `Selection` is a crate-private struct that partitions refresh operations into three categorized vectors: planned executions, skipped operations, and failed attempts. [crates/gwiki/src/commands/refresh/model.rs:5-9]
- `ChangedRefresh` (class) component `ChangedRefresh [class]` (`bf1bc86b-1ac9-53d4-8741-51cad3b7925b`) lines 12-17 [crates/gwiki/src/commands/refresh/model.rs:12-17]
  - Signature: `pub(crate) struct ChangedRefresh {`
  - Purpose: `ChangedRefresh` is a crate-private struct that encapsulates the result and metadata of an ingest refresh operation, including the prior raw path, removed paths, and degradation records. [crates/gwiki/src/commands/refresh/model.rs:12-17]
- `RefreshSinks` (class) component `RefreshSinks [class]` (`8117eae6-c791-5b5e-adf4-a3b6ac0d78da`) lines 19-24 [crates/gwiki/src/commands/refresh/model.rs:19-24]
  - Signature: `pub(crate) struct RefreshSinks<'a> {`
  - Purpose: `RefreshSinks` is a lifetime-parameterized container holding mutable references to four vectors that segregate refresh operation outcomes into refreshed sources, unchanged results, failures, and degradations. [crates/gwiki/src/commands/refresh/model.rs:19-24]
- `RefreshRender` (class) component `RefreshRender [class]` (`1fa98b8d-014e-5085-bf84-934fbc50f9d5`) lines 27-38 [crates/gwiki/src/commands/refresh/model.rs:27-38]
  - Signature: `pub(crate) struct RefreshRender {`
  - Purpose: RefreshRender is a result container that tracks the complete state of a scoped refresh operation, including planned, refreshed, unchanged, failed, and skipped sources along with index status and degradation metrics. [crates/gwiki/src/commands/refresh/model.rs:27-38]
- `RefreshPlan` (class) component `RefreshPlan [class]` (`457c7789-2c3b-5dc5-bcb5-0e2c2d9c2db2`) lines 41-43 [crates/gwiki/src/commands/refresh/model.rs:41-43]
  - Signature: `pub(crate) struct RefreshPlan {`
  - Purpose: `RefreshPlan` is a crate-private struct that encapsulates a `SourceRecord` for refresh operations. [crates/gwiki/src/commands/refresh/model.rs:41-43]
- `RefreshPlan` (class) component `RefreshPlan [class]` (`b3da7bc7-485c-5d14-90de-0ac1b86f6dfe`) lines 45-52 [crates/gwiki/src/commands/refresh/model.rs:45-52]
  - Signature: `impl RefreshPlan {`
  - Purpose: `RefreshPlan::from_record` is a fallible constructor that validates a `SourceRecord`'s path via `raw_source_path()` before wrapping a cloned copy of the record in a new `RefreshPlan` instance. [crates/gwiki/src/commands/refresh/model.rs:45-52]
- `RefreshPlan.from_record` (method) component `RefreshPlan.from_record [method]` (`55975ede-169c-5c20-9780-16926f7f3e50`) lines 46-51 [crates/gwiki/src/commands/refresh/model.rs:46-51]
  - Signature: `pub(crate) fn from_record(record: &SourceRecord) -> Result<Self, WikiError> {`
  - Purpose: Constructs `Self` from a `SourceRecord` reference after validating that the record's ID can resolve to a valid raw source path, or returns a `WikiError` on validation failure. [crates/gwiki/src/commands/refresh/model.rs:46-51]
- `RefreshPlan` (class) component `RefreshPlan [class]` (`f792e1fa-85ac-56a4-8327-f5f12e39d65c`) lines 54-69 [crates/gwiki/src/commands/refresh/model.rs:54-69]
  - Signature: `impl serde::Serialize for RefreshPlan {`
  - Purpose: Implements custom serde serialization for `RefreshPlan` that derives a `raw_path` field from the record's ID and serializes six named fields (id, location, source_kind, replay_kind, raw_path, content_hash). [crates/gwiki/src/commands/refresh/model.rs:54-69]
- `RefreshPlan.serialize` (method) component `RefreshPlan.serialize [method]` (`6f5b1380-21a1-53c6-b3d0-6ee35ae2bde8`) lines 55-68 [crates/gwiki/src/commands/refresh/model.rs:55-68]
  - Signature: `fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>`
  - Purpose: This method serializes a RefreshPlan struct by mapping six fields from an internal record, deriving a raw_path from the record ID and transforming the kind field into replay_kind. [crates/gwiki/src/commands/refresh/model.rs:55-68]
- `RefreshedSource` (class) component `RefreshedSource [class]` (`f8e6d8ea-8cf7-5b0f-9ea2-91fddd659439`) lines 72-85 [crates/gwiki/src/commands/refresh/model.rs:72-85]
  - Signature: `pub(crate) struct RefreshedSource {`
  - Purpose: `RefreshedSource` is a crate-private struct that represents the complete state of a refreshed data source, tracking identity mapping (old/new IDs), file system path mutations (current, previous, removed), change status, and the underlying `SourceRecord`. [crates/gwiki/src/commands/refresh/model.rs:72-85]
- `RefreshResult` (class) component `RefreshResult [class]` (`fb6e0497-0aba-52a0-9d7e-80bd27b2c223`) lines 88-98 [crates/gwiki/src/commands/refresh/model.rs:88-98]
  - Signature: `pub(crate) struct RefreshResult {`
  - Purpose: RefreshResult is a crate-private struct that encapsulates refresh operation metadata for a source item, including its identity, kind classification, file path, content hash, and change status. [crates/gwiki/src/commands/refresh/model.rs:88-98]
- `RefreshFailure` (class) component `RefreshFailure [class]` (`8b94b10e-cbba-5e2a-bc36-4a5a5694f8a5`) lines 101-107 [crates/gwiki/src/commands/refresh/model.rs:101-107]
  - Signature: `pub(crate) struct RefreshFailure {`
  - Purpose: `RefreshFailure` is a crate-private struct that encapsulates error details for a failed refresh operation, containing an identifier, optional location and source kind, an error code, and a human-readable message. [crates/gwiki/src/commands/refresh/model.rs:101-107]
- `SkippedRefresh` (class) component `SkippedRefresh [class]` (`1a9bceb0-a94d-543f-97cd-3b139f30362a`) lines 110-116 [crates/gwiki/src/commands/refresh/model.rs:110-116]
  - Signature: `pub(crate) struct SkippedRefresh {`
  - Purpose: `SkippedRefresh` is a crate-internal struct that encapsulates diagnostic metadata for a skipped refresh operation, containing an identifier, location, source kind, error code, and explanatory message. [crates/gwiki/src/commands/refresh/model.rs:110-116]
- `IndexedCounts` (class) component `IndexedCounts [class]` (`dae32f12-40e1-5ee1-8e41-68514034c103`) lines 119-125 [crates/gwiki/src/commands/refresh/model.rs:119-125]
  - Signature: `pub(crate) struct IndexedCounts {`
  - Purpose: `IndexedCounts` is a crate-private struct that aggregates telemetry counters for five indexed entity types: documents, chunks, links, sources, and ingestions. [crates/gwiki/src/commands/refresh/model.rs:119-125]
- `IndexedCounts` (class) component `IndexedCounts [class]` (`8e873a86-dad2-527e-8ea9-36e1784dc1bd`) lines 127-137 [crates/gwiki/src/commands/refresh/model.rs:127-137]
  - Signature: `impl From<IndexCounts> for IndexedCounts {`
  - Purpose: This `From` trait implementation converts an `IndexCounts` instance into an `IndexedCounts` instance by directly mapping all five count fields (documents, chunks, links, sources, ingestions). [crates/gwiki/src/commands/refresh/model.rs:127-137]
- `IndexedCounts.from` (method) component `IndexedCounts.from [method]` (`de90fac6-1b17-548d-b587-74bbf6b0d1ce`) lines 128-136 [crates/gwiki/src/commands/refresh/model.rs:128-136]
  - Signature: `fn from(counts: IndexCounts) -> Self {`
  - Purpose: This method implements the `From` trait to convert an `IndexCounts` struct into `Self` by extracting and reassigning each of its five count fields (documents, chunks, links, sources, ingestions). [crates/gwiki/src/commands/refresh/model.rs:128-136]
- `IndexStatus` (class) component `IndexStatus [class]` (`da7ff7e7-84ea-59cb-be8d-52e4375f6c40`) lines 140-144 [crates/gwiki/src/commands/refresh/model.rs:140-144]
  - Signature: `pub(crate) struct IndexStatus {`
  - Purpose: `IndexStatus` is a crate-private struct that encapsulates the state of an indexing operation, comprising a static status descriptor, a boolean flag indicating whether indexing is required, and an optional `IndexedCounts` containing the indexed item counts. [crates/gwiki/src/commands/refresh/model.rs:140-144]
- `IndexStatus` (class) component `IndexStatus [class]` (`fe73f4e0-08df-59bd-bf14-6594034fe599`) lines 146-170 [crates/gwiki/src/commands/refresh/model.rs:146-170]
  - Signature: `impl IndexStatus {`
  - Purpose: Provides factory methods that construct `IndexStatus` instances representing three distinct indexing lifecycle states: `not_run`, `indexed` (with optional `IndexedCounts`), and `degraded`. [crates/gwiki/src/commands/refresh/model.rs:146-170]
- `IndexStatus.not_run` (method) component `IndexStatus.not_run [method]` (`641cb946-d3f9-5425-8a41-cf671eb2d9a8`) lines 147-153 [crates/gwiki/src/commands/refresh/model.rs:147-153]
  - Signature: `pub(crate) fn not_run() -> Self {`
  - Purpose: Returns a new Self instance initialized with status="not_run", index_required=false, and indexed=None. [crates/gwiki/src/commands/refresh/model.rs:147-153]
- `IndexStatus.indexed` (method) component `IndexStatus.indexed [method]` (`ae95f6a6-c89f-59d2-af4b-ccd5f7520ed2`) lines 155-161 [crates/gwiki/src/commands/refresh/model.rs:155-161]
  - Signature: `pub(crate) fn indexed(indexed: IndexedCounts) -> Self {`
  - Purpose: Creates an instance initialized with status "indexed", index_required set to false, and the provided IndexedCounts wrapped in Some. [crates/gwiki/src/commands/refresh/model.rs:155-161]
- `IndexStatus.degraded` (method) component `IndexStatus.degraded [method]` (`32596f90-e4f7-59fb-a334-109181d2b8e8`) lines 163-169 [crates/gwiki/src/commands/refresh/model.rs:163-169]
  - Signature: `pub(crate) fn degraded() -> Self {`
  - Purpose: Constructs a new instance with degraded status, no index requirement, and no indexed value. [crates/gwiki/src/commands/refresh/model.rs:163-169]

