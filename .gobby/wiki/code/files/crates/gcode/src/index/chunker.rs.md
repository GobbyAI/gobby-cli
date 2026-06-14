---
title: crates/gcode/src/index/chunker.rs
type: code_file
provenance:
- file: crates/gcode/src/index/chunker.rs
  ranges:
  - 19-62
  - 64-72
  - 77-90
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/chunker.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This module implements line-based content chunking for full-text search indexing. chunk_file_content splits UTF-8 file content into overlapping 100-line chunks (with 10-line overlap) and wraps each in a ContentChunk object containing project identifier, file path, line ranges, language, and timestamp. The epoch_secs_str utility provides current Unix timestamps for chunk metadata. A test function verifies the module maintains intentional independence from gobby_core's generic byte-range Chunk primitives, since gcode needs domain-specific line-based records and derives state from PostgreSQL content hashes rather than core IndexEvent snapshots. This separation keeps the indexing abstraction layers cleanly isolated.
[crates/gcode/src/index/chunker.rs:19-62]
[crates/gcode/src/index/chunker.rs:64-72]
[crates/gcode/src/index/chunker.rs:77-90]

## API Symbols

- `chunk_file_content` (function) component `chunk_file_content [function]` (`d21e3ef6-4770-50f4-9d52-d1ba8459f999`) lines 19-62 [crates/gcode/src/index/chunker.rs:19-62]
  - Signature: `pub fn chunk_file_content(`
  - Purpose: Partitions UTF-8 file content into overlapping line-based chunks, generating `ContentChunk` objects with project-aware identifiers, line ranges, and metadata for content indexing. [crates/gcode/src/index/chunker.rs:19-62]
- `epoch_secs_str` (function) component `epoch_secs_str [function]` (`2398bbf7-1243-50b1-aa90-4b17e9cba4bc`) lines 64-72 [crates/gcode/src/index/chunker.rs:64-72]
  - Signature: `fn epoch_secs_str() -> String {`
  - Purpose: This function returns the current Unix timestamp (seconds since the UNIX_EPOCH) as a string. [crates/gcode/src/index/chunker.rs:64-72]
- `chunker_stays_gcode_owned_with_documented_narrowing` (function) component `chunker_stays_gcode_owned_with_documented_narrowing [function]` (`ae1546cd-8c8e-5a2f-906b-8d4c24c77584`) lines 77-90 [crates/gcode/src/index/chunker.rs:77-90]
  - Signature: `fn chunker_stays_gcode_owned_with_documented_narrowing() {`
  - Purpose: This test function verifies that `chunker.rs` maintains documented independence from `gobby_core::indexing` by asserting the absence of four specific type imports while confirming the presence of required documentation about line-based ContentChunk records. [crates/gcode/src/index/chunker.rs:77-90]

