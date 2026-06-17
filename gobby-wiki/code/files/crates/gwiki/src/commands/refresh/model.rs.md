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
  - 46-51
  - 55-68
  - 72-85
  - 88-98
  - 101-107
  - 110-116
  - 119-125
  - 128-136
  - 140-144
  - 147-153
  - 155-161
  - 163-169
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/refresh/model.rs:5-9](crates/gwiki/src/commands/refresh/model.rs#L5-L9), [crates/gwiki/src/commands/refresh/model.rs:12-17](crates/gwiki/src/commands/refresh/model.rs#L12-L17), [crates/gwiki/src/commands/refresh/model.rs:19-24](crates/gwiki/src/commands/refresh/model.rs#L19-L24), [crates/gwiki/src/commands/refresh/model.rs:27-38](crates/gwiki/src/commands/refresh/model.rs#L27-L38), [crates/gwiki/src/commands/refresh/model.rs:41-43](crates/gwiki/src/commands/refresh/model.rs#L41-L43), [crates/gwiki/src/commands/refresh/model.rs:46-51](crates/gwiki/src/commands/refresh/model.rs#L46-L51), [crates/gwiki/src/commands/refresh/model.rs:55-68](crates/gwiki/src/commands/refresh/model.rs#L55-L68), [crates/gwiki/src/commands/refresh/model.rs:72-85](crates/gwiki/src/commands/refresh/model.rs#L72-L85), [crates/gwiki/src/commands/refresh/model.rs:88-98](crates/gwiki/src/commands/refresh/model.rs#L88-L98), [crates/gwiki/src/commands/refresh/model.rs:101-107](crates/gwiki/src/commands/refresh/model.rs#L101-L107), [crates/gwiki/src/commands/refresh/model.rs:110-116](crates/gwiki/src/commands/refresh/model.rs#L110-L116), [crates/gwiki/src/commands/refresh/model.rs:119-125](crates/gwiki/src/commands/refresh/model.rs#L119-L125), [crates/gwiki/src/commands/refresh/model.rs:128-136](crates/gwiki/src/commands/refresh/model.rs#L128-L136), [crates/gwiki/src/commands/refresh/model.rs:140-144](crates/gwiki/src/commands/refresh/model.rs#L140-L144), [crates/gwiki/src/commands/refresh/model.rs:147-153](crates/gwiki/src/commands/refresh/model.rs#L147-L153), [crates/gwiki/src/commands/refresh/model.rs:155-161](crates/gwiki/src/commands/refresh/model.rs#L155-L161), [crates/gwiki/src/commands/refresh/model.rs:163-169](crates/gwiki/src/commands/refresh/model.rs#L163-L169)

</details>

# crates/gwiki/src/commands/refresh/model.rs

Module: [[code/modules/crates/gwiki/src/commands/refresh|crates/gwiki/src/commands/refresh]]

## Purpose

Defines the data models used by the refresh command to plan, collect, and render refresh outcomes. `Selection` groups planned, skipped, and failed items; `ChangedRefresh` and `RefreshSinks` carry intermediate ingest results and the mutable output buckets; `RefreshRender` aggregates the full command result plus scope, dry-run, index status, and degradations for display. `RefreshPlan` wraps a `SourceRecord`, validates that its raw source path exists in `from_record`, and serializes the plan as source metadata plus derived paths and replay kind. The remaining structs model the per-item output categories (`RefreshedSource`, `RefreshResult`, `RefreshFailure`, `SkippedRefresh`), index counts, and `IndexStatus` helpers for representing whether indexing was not run, successful, or degraded.
[crates/gwiki/src/commands/refresh/model.rs:5-9]
[crates/gwiki/src/commands/refresh/model.rs:12-17]
[crates/gwiki/src/commands/refresh/model.rs:19-24]
[crates/gwiki/src/commands/refresh/model.rs:27-38]
[crates/gwiki/src/commands/refresh/model.rs:41-43]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Selection` | class | `pub(crate) struct Selection {` | `Selection [class]` | `43669b6c-7faf-5bd2-afb3-d105e22ba108` | 5-9 [crates/gwiki/src/commands/refresh/model.rs:5-9] | Indexed class `Selection` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:5-9] |
| `ChangedRefresh` | class | `pub(crate) struct ChangedRefresh {` | `ChangedRefresh [class]` | `bf1bc86b-1ac9-53d4-8741-51cad3b7925b` | 12-17 [crates/gwiki/src/commands/refresh/model.rs:12-17] | Indexed class `ChangedRefresh` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:12-17] |
| `RefreshSinks` | class | `pub(crate) struct RefreshSinks<'a> {` | `RefreshSinks [class]` | `8117eae6-c791-5b5e-adf4-a3b6ac0d78da` | 19-24 [crates/gwiki/src/commands/refresh/model.rs:19-24] | Indexed class `RefreshSinks` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:19-24] |
| `RefreshRender` | class | `pub(crate) struct RefreshRender {` | `RefreshRender [class]` | `1fa98b8d-014e-5085-bf84-934fbc50f9d5` | 27-38 [crates/gwiki/src/commands/refresh/model.rs:27-38] | Indexed class `RefreshRender` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:27-38] |
| `RefreshPlan` | class | `pub(crate) struct RefreshPlan {` | `RefreshPlan [class]` | `457c7789-2c3b-5dc5-bcb5-0e2c2d9c2db2` | 41-43 [crates/gwiki/src/commands/refresh/model.rs:41-43] | Indexed class `RefreshPlan` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:41-43] |
| `RefreshPlan::from_record` | method | `pub(crate) fn from_record(record: &SourceRecord) -> Result<Self, WikiError> {` | `RefreshPlan::from_record [method]` | `55975ede-169c-5c20-9780-16926f7f3e50` | 46-51 [crates/gwiki/src/commands/refresh/model.rs:46-51] | Indexed method `RefreshPlan::from_record` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:46-51] |
| `RefreshPlan::serialize` | method | `fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>` | `RefreshPlan::serialize [method]` | `6f5b1380-21a1-53c6-b3d0-6ee35ae2bde8` | 55-68 [crates/gwiki/src/commands/refresh/model.rs:55-68] | Indexed method `RefreshPlan::serialize` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:55-68] |
| `RefreshedSource` | class | `pub(crate) struct RefreshedSource {` | `RefreshedSource [class]` | `f8e6d8ea-8cf7-5b0f-9ea2-91fddd659439` | 72-85 [crates/gwiki/src/commands/refresh/model.rs:72-85] | Indexed class `RefreshedSource` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:72-85] |
| `RefreshResult` | class | `pub(crate) struct RefreshResult {` | `RefreshResult [class]` | `fb6e0497-0aba-52a0-9d7e-80bd27b2c223` | 88-98 [crates/gwiki/src/commands/refresh/model.rs:88-98] | Indexed class `RefreshResult` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:88-98] |
| `RefreshFailure` | class | `pub(crate) struct RefreshFailure {` | `RefreshFailure [class]` | `8b94b10e-cbba-5e2a-bc36-4a5a5694f8a5` | 101-107 [crates/gwiki/src/commands/refresh/model.rs:101-107] | Indexed class `RefreshFailure` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:101-107] |
| `SkippedRefresh` | class | `pub(crate) struct SkippedRefresh {` | `SkippedRefresh [class]` | `1a9bceb0-a94d-543f-97cd-3b139f30362a` | 110-116 [crates/gwiki/src/commands/refresh/model.rs:110-116] | Indexed class `SkippedRefresh` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:110-116] |
| `IndexedCounts` | class | `pub(crate) struct IndexedCounts {` | `IndexedCounts [class]` | `dae32f12-40e1-5ee1-8e41-68514034c103` | 119-125 [crates/gwiki/src/commands/refresh/model.rs:119-125] | Indexed class `IndexedCounts` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:119-125] |
| `IndexedCounts::from` | method | `fn from(counts: IndexCounts) -> Self {` | `IndexedCounts::from [method]` | `de90fac6-1b17-548d-b587-74bbf6b0d1ce` | 128-136 [crates/gwiki/src/commands/refresh/model.rs:128-136] | Indexed method `IndexedCounts::from` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:128-136] |
| `IndexStatus` | class | `pub(crate) struct IndexStatus {` | `IndexStatus [class]` | `da7ff7e7-84ea-59cb-be8d-52e4375f6c40` | 140-144 [crates/gwiki/src/commands/refresh/model.rs:140-144] | Indexed class `IndexStatus` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:140-144] |
| `IndexStatus::not_run` | method | `pub(crate) fn not_run() -> Self {` | `IndexStatus::not_run [method]` | `641cb946-d3f9-5425-8a41-cf671eb2d9a8` | 147-153 [crates/gwiki/src/commands/refresh/model.rs:147-153] | Indexed method `IndexStatus::not_run` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:147-153] |
| `IndexStatus::indexed` | method | `pub(crate) fn indexed(indexed: IndexedCounts) -> Self {` | `IndexStatus::indexed [method]` | `ae95f6a6-c89f-59d2-af4b-ccd5f7520ed2` | 155-161 [crates/gwiki/src/commands/refresh/model.rs:155-161] | Indexed method `IndexStatus::indexed` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:155-161] |
| `IndexStatus::degraded` | method | `pub(crate) fn degraded() -> Self {` | `IndexStatus::degraded [method]` | `32596f90-e4f7-59fb-a334-109181d2b8e8` | 163-169 [crates/gwiki/src/commands/refresh/model.rs:163-169] | Indexed method `IndexStatus::degraded` in `crates/gwiki/src/commands/refresh/model.rs`. [crates/gwiki/src/commands/refresh/model.rs:163-169] |
