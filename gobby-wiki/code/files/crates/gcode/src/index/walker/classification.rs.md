---
title: crates/gcode/src/index/walker/classification.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/classification.rs
  ranges:
  - 15-52
  - 56-66
  - 69-78
  - 81-93
  - 95-111
  - 113-117
  - 119-144
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/walker/classification.rs:15-52](crates/gcode/src/index/walker/classification.rs#L15-L52), [crates/gcode/src/index/walker/classification.rs:56-66](crates/gcode/src/index/walker/classification.rs#L56-L66), [crates/gcode/src/index/walker/classification.rs:69-78](crates/gcode/src/index/walker/classification.rs#L69-L78), [crates/gcode/src/index/walker/classification.rs:81-93](crates/gcode/src/index/walker/classification.rs#L81-L93), [crates/gcode/src/index/walker/classification.rs:95-111](crates/gcode/src/index/walker/classification.rs#L95-L111), [crates/gcode/src/index/walker/classification.rs:113-117](crates/gcode/src/index/walker/classification.rs#L113-L117), [crates/gcode/src/index/walker/classification.rs:119-144](crates/gcode/src/index/walker/classification.rs#L119-L144)

</details>

# crates/gcode/src/index/walker/classification.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

This file classifies candidate files for the indexer, deciding whether each path should be skipped, treated as AST-indexable, or kept content-only. `classify_file` applies safety, hidden/generated-file, and language-based rules; `classify_explicit_file_with_options` adds per-path discovery visibility checks for explicitly requested files; `is_content_indexable` and `is_safe_text_file` expose the lower-level gating logic, while `content_language`, `explicit_path_visible`, and `same_existing_path` support those decisions.
[crates/gcode/src/index/walker/classification.rs:15-52]
[crates/gcode/src/index/walker/classification.rs:56-66]
[crates/gcode/src/index/walker/classification.rs:69-78]
[crates/gcode/src/index/walker/classification.rs:81-93]
[crates/gcode/src/index/walker/classification.rs:95-111]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `classify_file` | function | `pub fn classify_file(` | `classify_file [function]` | `2b6a5919-acd7-599b-8e25-a5668bbd68c2` | 15-52 [crates/gcode/src/index/walker/classification.rs:15-52] | Indexed function `classify_file` in `crates/gcode/src/index/walker/classification.rs`. [crates/gcode/src/index/walker/classification.rs:15-52] |
| `classify_explicit_file_with_options` | function | `pub fn classify_explicit_file_with_options(` | `classify_explicit_file_with_options [function]` | `9e3f2864-703d-518a-944a-7d2a35ff744b` | 56-66 [crates/gcode/src/index/walker/classification.rs:56-66] | Indexed function `classify_explicit_file_with_options` in `crates/gcode/src/index/walker/classification.rs`. [crates/gcode/src/index/walker/classification.rs:56-66] |
| `is_content_indexable` | function | `pub fn is_content_indexable(` | `is_content_indexable [function]` | `01e57cf4-5711-55ab-8ff5-c0e7e800f88a` | 69-78 [crates/gcode/src/index/walker/classification.rs:69-78] | Indexed function `is_content_indexable` in `crates/gcode/src/index/walker/classification.rs`. [crates/gcode/src/index/walker/classification.rs:69-78] |
| `content_language` | function | `pub fn content_language(path: &Path) -> String {` | `content_language [function]` | `44ba0277-d89a-549c-9061-755cf7af4b2a` | 81-93 [crates/gcode/src/index/walker/classification.rs:81-93] | Indexed function `content_language` in `crates/gcode/src/index/walker/classification.rs`. [crates/gcode/src/index/walker/classification.rs:81-93] |
| `explicit_path_visible` | function | `fn explicit_path_visible(root: &Path, path: &Path, options: DiscoveryOptions) -> bool {` | `explicit_path_visible [function]` | `b80b2c1b-627d-5c31-813a-c3b758cf87e9` | 95-111 [crates/gcode/src/index/walker/classification.rs:95-111] | Indexed function `explicit_path_visible` in `crates/gcode/src/index/walker/classification.rs`. [crates/gcode/src/index/walker/classification.rs:95-111] |
| `same_existing_path` | function | `fn same_existing_path(left: &Path, right: &Path) -> bool {` | `same_existing_path [function]` | `ce414d42-18fb-53a0-9266-ab69b2ae3312` | 113-117 [crates/gcode/src/index/walker/classification.rs:113-117] | Indexed function `same_existing_path` in `crates/gcode/src/index/walker/classification.rs`. [crates/gcode/src/index/walker/classification.rs:113-117] |
| `is_safe_text_file` | function | `fn is_safe_text_file(root: &Path, path: &Path, exclude_patterns: &[impl AsRef<str>]) -> bool {` | `is_safe_text_file [function]` | `1d62664b-98f9-531f-a9aa-a81238650db4` | 119-144 [crates/gcode/src/index/walker/classification.rs:119-144] | Indexed function `is_safe_text_file` in `crates/gcode/src/index/walker/classification.rs`. [crates/gcode/src/index/walker/classification.rs:119-144] |
