---
title: crates/gcode/src/commands/codewiki/ownership.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/ownership.rs
  ranges:
  - 20-23
  - 25-32
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

# crates/gcode/src/commands/codewiki/ownership.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

Builds a codewiki ownership document for a set of files by combining declared CODEOWNERS data with derived blame-based ownership, then rendering the result into markdown/text. `OwnershipOptions` controls blame limits and timeout, `OwnershipMeta` caches per-file blame summaries by content hash, `OwnershipContributor` and `CachedBlameSummary` carry the ownership data, and `OwnershipStatus` tracks whether CODEOWNERS, blame, or partial data were available. `build_ownership_doc` ties the pieces together: it loads CODEOWNERS, computes declared and derived owners, organizes them per file, and passes the assembled ownership model to the render helpers to produce the final document.
[crates/gcode/src/commands/codewiki/ownership.rs:20-23]
[crates/gcode/src/commands/codewiki/ownership.rs:25-32]
[crates/gcode/src/commands/codewiki/ownership.rs:26-31]
[crates/gcode/src/commands/codewiki/ownership.rs:35-38]
[crates/gcode/src/commands/codewiki/ownership.rs:41-44]

## API Symbols

- `OwnershipOptions` (class) component `OwnershipOptions [class]` (`f41a0ee8-5e30-5962-a6fb-bb079a5b36b8`) lines 20-23 [crates/gcode/src/commands/codewiki/ownership.rs:20-23]
  - Signature: `pub(crate) struct OwnershipOptions {`
  - Purpose: Indexed class `OwnershipOptions` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:20-23]
- `OwnershipOptions` (class) component `OwnershipOptions [class]` (`a3b0bc5e-15fe-5b41-9b29-4435c0965707`) lines 25-32 [crates/gcode/src/commands/codewiki/ownership.rs:25-32]
  - Signature: `impl Default for OwnershipOptions {`
  - Purpose: Indexed class `OwnershipOptions` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:25-32]
- `OwnershipOptions.default` (method) component `OwnershipOptions.default [method]` (`4fe0c950-0a3c-524e-9fb1-ad035344a41c`) lines 26-31 [crates/gcode/src/commands/codewiki/ownership.rs:26-31]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `OwnershipOptions.default` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:26-31]
- `OwnershipMeta` (class) component `OwnershipMeta [class]` (`f9a0d7ef-2830-5d6b-8691-8ac8d9f7476b`) lines 35-38 [crates/gcode/src/commands/codewiki/ownership.rs:35-38]
  - Signature: `pub(crate) struct OwnershipMeta {`
  - Purpose: Indexed class `OwnershipMeta` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:35-38]
- `CachedBlameSummary` (class) component `CachedBlameSummary [class]` (`d3e6d1e4-66e2-588a-9508-207dffc42659`) lines 41-44 [crates/gcode/src/commands/codewiki/ownership.rs:41-44]
  - Signature: `pub(crate) struct CachedBlameSummary {`
  - Purpose: Indexed class `CachedBlameSummary` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:41-44]
- `OwnershipContributor` (class) component `OwnershipContributor [class]` (`7a605b7c-826c-5b65-953b-4f59f3d86866`) lines 47-53 [crates/gcode/src/commands/codewiki/ownership.rs:47-53]
  - Signature: `pub(crate) struct OwnershipContributor {`
  - Purpose: Indexed class `OwnershipContributor` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:47-53]
- `OwnershipStatus` (class) component `OwnershipStatus [class]` (`c4dedc5e-dffe-59cb-b219-51ea84f31d3f`) lines 56-61 [crates/gcode/src/commands/codewiki/ownership.rs:56-61]
  - Signature: `struct OwnershipStatus {`
  - Purpose: Indexed class `OwnershipStatus` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:56-61]
- `FileOwnership` (class) component `FileOwnership [class]` (`64ffa3e8-436f-501f-9115-9509d5832639`) lines 64-67 [crates/gcode/src/commands/codewiki/ownership.rs:64-67]
  - Signature: `struct FileOwnership {`
  - Purpose: Indexed class `FileOwnership` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:64-67]
- `build_ownership_doc` (function) component `build_ownership_doc [function]` (`7932c4da-b0ee-5354-baf2-3b7467af10dc`) lines 69-114 [crates/gcode/src/commands/codewiki/ownership.rs:69-114]
  - Signature: `pub(crate) fn build_ownership_doc(`
  - Purpose: Indexed function `build_ownership_doc` in `crates/gcode/src/commands/codewiki/ownership.rs`. [crates/gcode/src/commands/codewiki/ownership.rs:69-114]

