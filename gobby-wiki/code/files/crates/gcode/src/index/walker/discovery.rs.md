---
title: crates/gcode/src/index/walker/discovery.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/discovery.rs
  ranges:
  - 12-17
  - 19-64
  - 66-84
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/walker/discovery.rs:12-17](crates/gcode/src/index/walker/discovery.rs#L12-L17), [crates/gcode/src/index/walker/discovery.rs:19-64](crates/gcode/src/index/walker/discovery.rs#L19-L64), [crates/gcode/src/index/walker/discovery.rs:66-84](crates/gcode/src/index/walker/discovery.rs#L66-L84)

</details>

# crates/gcode/src/index/walker/discovery.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

Discovers indexable files under a root path and splits them into AST candidates and content-only candidates. `discover_files` is a convenience wrapper that calls `discover_files_with_options` with default settings. The main discovery function configures a `gobby_core` walker with gitignore and max-size behavior, walks all visible files, then merges in additional files from `HiddenPathAllowlist`; each path is deduplicated with a `BTreeSet` and classified by `classify_file` before being pushed into the appropriate output list. `push_classified_file` centralizes deduplication and classification so both walker sources use the same filtering and routing logic.
[crates/gcode/src/index/walker/discovery.rs:12-17]
[crates/gcode/src/index/walker/discovery.rs:19-64]
[crates/gcode/src/index/walker/discovery.rs:66-84]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `discover_files` | function | `pub fn discover_files<S: AsRef<str>>(` | `discover_files [function]` | `f931f3c8-31a0-557a-838b-3e606577def8` | 12-17 [crates/gcode/src/index/walker/discovery.rs:12-17] | Indexed function `discover_files` in `crates/gcode/src/index/walker/discovery.rs`. [crates/gcode/src/index/walker/discovery.rs:12-17] |
| `discover_files_with_options` | function | `pub fn discover_files_with_options<S: AsRef<str>>(` | `discover_files_with_options [function]` | `9d8a43e3-8601-5f60-884a-8e9bfbfcfd25` | 19-64 [crates/gcode/src/index/walker/discovery.rs:19-64] | Indexed function `discover_files_with_options` in `crates/gcode/src/index/walker/discovery.rs`. [crates/gcode/src/index/walker/discovery.rs:19-64] |
| `push_classified_file` | function | `fn push_classified_file(` | `push_classified_file [function]` | `8d6d0547-e604-5076-858b-fc6889b96385` | 66-84 [crates/gcode/src/index/walker/discovery.rs:66-84] | Indexed function `push_classified_file` in `crates/gcode/src/index/walker/discovery.rs`. [crates/gcode/src/index/walker/discovery.rs:66-84] |
