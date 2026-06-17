---
title: crates/gcode/src/commands/codewiki/ownership.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership.rs
  ranges:
  - 20-23
  - 26-31
  - 35-38
  - 41-44
  - 47-53
  - 56-61
  - 64-67
  - 69-114
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/ownership.rs:20-23](crates/gcode/src/commands/codewiki/ownership.rs#L20-L23), [crates/gcode/src/commands/codewiki/ownership.rs:26-31](crates/gcode/src/commands/codewiki/ownership.rs#L26-L31), [crates/gcode/src/commands/codewiki/ownership.rs:35-38](crates/gcode/src/commands/codewiki/ownership.rs#L35-L38), [crates/gcode/src/commands/codewiki/ownership.rs:41-44](crates/gcode/src/commands/codewiki/ownership.rs#L41-L44), [crates/gcode/src/commands/codewiki/ownership.rs:47-53](crates/gcode/src/commands/codewiki/ownership.rs#L47-L53), [crates/gcode/src/commands/codewiki/ownership.rs:56-61](crates/gcode/src/commands/codewiki/ownership.rs#L56-L61), [crates/gcode/src/commands/codewiki/ownership.rs:64-67](crates/gcode/src/commands/codewiki/ownership.rs#L64-L67), [crates/gcode/src/commands/codewiki/ownership.rs:69-114](crates/gcode/src/commands/codewiki/ownership.rs#L69-L114)

</details>

# crates/gcode/src/commands/codewiki/ownership.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Builds a codewiki ownership document for a set of files by combining declared owners from `CODEOWNERS` with derived blame-based ownership, caching blame summaries in `OwnershipMeta` to avoid recomputation. `OwnershipOptions` controls blame limits and timeout, the small data structs carry cached summaries, contributor details, and status flags, and `build_ownership_doc` ties the analysis and render modules together to assemble per-file ownership data and emit the final document.
[crates/gcode/src/commands/codewiki/ownership.rs:20-23]
[crates/gcode/src/commands/codewiki/ownership.rs:26-31]
[crates/gcode/src/commands/codewiki/ownership.rs:35-38]
[crates/gcode/src/commands/codewiki/ownership.rs:41-44]
[crates/gcode/src/commands/codewiki/ownership.rs:47-53]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `OwnershipOptions` | class | `pub(crate) struct OwnershipOptions {` | `OwnershipOptions [class]` | `f41a0ee8-5e30-5962-a6fb-bb079a5b36b8` | 20-23 [crates/gcode/src/commands/codewiki/ownership.rs:20-23] | Indexed class `OwnershipOptions` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:20-23] |
| `OwnershipOptions::default` | method | `fn default() -> Self {` | `OwnershipOptions::default [method]` | `4fe0c950-0a3c-524e-9fb1-ad035344a41c` | 26-31 [crates/gcode/src/commands/codewiki/ownership.rs:26-31] | Indexed method `OwnershipOptions::default` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:26-31] |
| `OwnershipMeta` | class | `pub(crate) struct OwnershipMeta {` | `OwnershipMeta [class]` | `f9a0d7ef-2830-5d6b-8691-8ac8d9f7476b` | 35-38 [crates/gcode/src/commands/codewiki/ownership.rs:35-38] | Indexed class `OwnershipMeta` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:35-38] |
| `CachedBlameSummary` | class | `pub(crate) struct CachedBlameSummary {` | `CachedBlameSummary [class]` | `d3e6d1e4-66e2-588a-9508-207dffc42659` | 41-44 [crates/gcode/src/commands/codewiki/ownership.rs:41-44] | Indexed class `CachedBlameSummary` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:41-44] |
| `OwnershipContributor` | class | `pub(crate) struct OwnershipContributor {` | `OwnershipContributor [class]` | `7a605b7c-826c-5b65-953b-4f59f3d86866` | 47-53 [crates/gcode/src/commands/codewiki/ownership.rs:47-53] | Indexed class `OwnershipContributor` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:47-53] |
| `OwnershipStatus` | class | `struct OwnershipStatus {` | `OwnershipStatus [class]` | `c4dedc5e-dffe-59cb-b219-51ea84f31d3f` | 56-61 [crates/gcode/src/commands/codewiki/ownership.rs:56-61] | Indexed class `OwnershipStatus` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:56-61] |
| `FileOwnership` | class | `struct FileOwnership {` | `FileOwnership [class]` | `64ffa3e8-436f-501f-9115-9509d5832639` | 64-67 [crates/gcode/src/commands/codewiki/ownership.rs:64-67] | Indexed class `FileOwnership` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:64-67] |
| `build_ownership_doc` | function | `pub(crate) fn build_ownership_doc(` | `build_ownership_doc [function]` | `7932c4da-b0ee-5354-baf2-3b7467af10dc` | 69-114 [crates/gcode/src/commands/codewiki/ownership.rs:69-114] | Indexed function `build_ownership_doc` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:69-114] |
