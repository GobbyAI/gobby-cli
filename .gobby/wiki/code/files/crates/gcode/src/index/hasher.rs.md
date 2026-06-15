---
title: crates/gcode/src/index/hasher.rs
type: code_file
provenance:
- file: crates/gcode/src/index/hasher.rs
  ranges:
  - 7-9
  - 12-14
  - 17-27
  - 35-49
  - 52-59
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/hasher.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Provides content-hashing helpers for incremental indexing by delegating SHA-256 hashing to `gobby_core::indexing`. It exposes wrappers for hashing an entire file, hashing an in-memory byte slice, and hashing a validated subrange of a byte slice for symbol content, returning an error when the requested range is out of bounds. The tests verify these wrappers match `gobby_core`’s behavior and that the file-level helper does not reimplement buffering locally.
[crates/gcode/src/index/hasher.rs:7-9]
[crates/gcode/src/index/hasher.rs:12-14]
[crates/gcode/src/index/hasher.rs:17-27]
[crates/gcode/src/index/hasher.rs:35-49]
[crates/gcode/src/index/hasher.rs:52-59]

## API Symbols

- `file_content_hash` (function) component `file_content_hash [function]` (`c600b0c6-f66e-52ae-b3e1-f362d21b5616`) lines 7-9 [crates/gcode/src/index/hasher.rs:7-9]
  - Signature: `pub fn file_content_hash(path: &Path) -> anyhow::Result<String> {`
  - Purpose: This function computes and returns a hash digest of the file contents at the given path as a String, wrapped in an anyhow Result for error handling. [crates/gcode/src/index/hasher.rs:7-9]
- `content_hash` (function) component `content_hash [function]` (`f7bcf6cd-26cb-5578-98c7-61253811ba0e`) lines 12-14 [crates/gcode/src/index/hasher.rs:12-14]
  - Signature: `pub fn content_hash(source: &[u8]) -> String {`
  - Purpose: This function computes and returns a String representation of the content hash for a given byte slice by delegating to the gobby_core indexing module. [crates/gcode/src/index/hasher.rs:12-14]
- `symbol_content_hash` (function) component `symbol_content_hash [function]` (`913a763d-ce18-5b88-8b21-a4dd80fae937`) lines 17-27 [crates/gcode/src/index/hasher.rs:17-27]
  - Signature: `pub fn symbol_content_hash(source: &[u8], start: usize, end: usize) -> anyhow::Result<String> {`
  - Purpose: Returns the content hash of a byte slice extracted from `source[start..end]`, or an error if the range is out of bounds. [crates/gcode/src/index/hasher.rs:17-27]
- `file_content_hash_delegates_to_gobby_core` (function) component `file_content_hash_delegates_to_gobby_core [function]` (`6957af87-88db-5c60-9cd2-ace100fa662d`) lines 35-49 [crates/gcode/src/index/hasher.rs:35-49]
  - Signature: `fn file_content_hash_delegates_to_gobby_core() {`
  - Purpose: This test verifies that the `file_content_hash` wrapper function correctly delegates to `gobby_core::indexing::file_content_hash` by asserting identical hash outputs and confirming the source code contains the delegation call without a local buffer implementation. [crates/gcode/src/index/hasher.rs:35-49]
- `content_hash_delegates_to_gobby_core` (function) component `content_hash_delegates_to_gobby_core [function]` (`1106bcfa-cd46-5069-ac5e-43764f61253a`) lines 52-59 [crates/gcode/src/index/hasher.rs:52-59]
  - Signature: `fn content_hash_delegates_to_gobby_core() {`
  - Purpose: This test asserts that the `content_hash` function produces identical output to `gobby_core::indexing::content_hash` when hashing the same byte input. [crates/gcode/src/index/hasher.rs:52-59]

