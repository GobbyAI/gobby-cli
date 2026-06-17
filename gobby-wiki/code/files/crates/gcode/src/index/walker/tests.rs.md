---
title: crates/gcode/src/index/walker/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/tests.rs
  ranges:
  - 11-17
  - 19-31
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/walker/tests.rs:11-17](crates/gcode/src/index/walker/tests.rs#L11-L17), [crates/gcode/src/index/walker/tests.rs:19-31](crates/gcode/src/index/walker/tests.rs#L19-L31)

</details>

# crates/gcode/src/index/walker/tests.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

Test support utilities for the walker index tests. `write_file` creates parent directories as needed and writes test fixtures under a root path, while `rels` normalizes a list of discovered `PathBuf`s into sorted relative path strings for assertions. The file also pulls in the `classification`, `discovery`, `generated`, and `hidden` test modules that exercise the walker behavior.
[crates/gcode/src/index/walker/tests.rs:11-17]
[crates/gcode/src/index/walker/tests.rs:19-31]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_file` | function | `fn write_file(root: &Path, rel: &str, contents: &[u8]) {` | `write_file [function]` | `8cdbdb21-4dad-50df-8229-7384dd4ce8c3` | 11-17 [crates/gcode/src/index/walker/tests.rs:11-17] | Indexed function `write_file` in `crates/gcode/src/index/walker/tests.rs`. [crates/gcode/src/index/walker/tests.rs:11-17] |
| `rels` | function | `fn rels(root: &Path, paths: Vec<PathBuf>) -> Vec<String> {` | `rels [function]` | `61fa14cb-3e0b-569c-9365-bc120f11dc91` | 19-31 [crates/gcode/src/index/walker/tests.rs:19-31] | Indexed function `rels` in `crates/gcode/src/index/walker/tests.rs`. [crates/gcode/src/index/walker/tests.rs:19-31] |
