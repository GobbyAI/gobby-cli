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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/hasher.rs:7-9](crates/gcode/src/index/hasher.rs#L7-L9), [crates/gcode/src/index/hasher.rs:12-14](crates/gcode/src/index/hasher.rs#L12-L14), [crates/gcode/src/index/hasher.rs:17-27](crates/gcode/src/index/hasher.rs#L17-L27), [crates/gcode/src/index/hasher.rs:35-49](crates/gcode/src/index/hasher.rs#L35-L49), [crates/gcode/src/index/hasher.rs:52-59](crates/gcode/src/index/hasher.rs#L52-L59)

</details>

# crates/gcode/src/index/hasher.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file provides SHA-256 content hashing helpers for incremental indexing and mostly delegates the real hashing work to `gobby_core::indexing`. `file_content_hash` hashes a file path, `content_hash` hashes an in-memory byte slice, and `symbol_content_hash` hashes a selected byte range from a larger source after checking that the range is valid. The tests confirm that the local wrappers match `gobby_core`’s behavior and that the file wrapper avoids inlining its own buffering logic.
[crates/gcode/src/index/hasher.rs:7-9]
[crates/gcode/src/index/hasher.rs:12-14]
[crates/gcode/src/index/hasher.rs:17-27]
[crates/gcode/src/index/hasher.rs:35-49]
[crates/gcode/src/index/hasher.rs:52-59]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `file_content_hash` | function | `pub fn file_content_hash(path: &Path) -> anyhow::Result<String> {` | `file_content_hash [function]` | `c600b0c6-f66e-52ae-b3e1-f362d21b5616` | 7-9 [crates/gcode/src/index/hasher.rs:7-9] | Indexed function `file_content_hash` in `crates/gcode/src/index/hasher.rs`. [crates/gcode/src/index/hasher.rs:7-9] |
| `content_hash` | function | `pub fn content_hash(source: &[u8]) -> String {` | `content_hash [function]` | `f7bcf6cd-26cb-5578-98c7-61253811ba0e` | 12-14 [crates/gcode/src/index/hasher.rs:12-14] | Indexed function `content_hash` in `crates/gcode/src/index/hasher.rs`. [crates/gcode/src/index/hasher.rs:12-14] |
| `symbol_content_hash` | function | `pub fn symbol_content_hash(source: &[u8], start: usize, end: usize) -> anyhow::Result<String> {` | `symbol_content_hash [function]` | `913a763d-ce18-5b88-8b21-a4dd80fae937` | 17-27 [crates/gcode/src/index/hasher.rs:17-27] | Indexed function `symbol_content_hash` in `crates/gcode/src/index/hasher.rs`. [crates/gcode/src/index/hasher.rs:17-27] |
| `file_content_hash_delegates_to_gobby_core` | function | `fn file_content_hash_delegates_to_gobby_core() {` | `file_content_hash_delegates_to_gobby_core [function]` | `6957af87-88db-5c60-9cd2-ace100fa662d` | 35-49 [crates/gcode/src/index/hasher.rs:35-49] | Indexed function `file_content_hash_delegates_to_gobby_core` in `crates/gcode/src/index/hasher.rs`. [crates/gcode/src/index/hasher.rs:35-49] |
| `content_hash_delegates_to_gobby_core` | function | `fn content_hash_delegates_to_gobby_core() {` | `content_hash_delegates_to_gobby_core [function]` | `1106bcfa-cd46-5069-ac5e-43764f61253a` | 52-59 [crates/gcode/src/index/hasher.rs:52-59] | Indexed function `content_hash_delegates_to_gobby_core` in `crates/gcode/src/index/hasher.rs`. [crates/gcode/src/index/hasher.rs:52-59] |
