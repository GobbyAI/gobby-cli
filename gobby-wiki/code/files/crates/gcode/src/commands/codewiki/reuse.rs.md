---
title: crates/gcode/src/commands/codewiki/reuse.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/reuse.rs
  ranges:
  - 11-19
  - 22-31
  - 36-46
  - 49-57
  - 59-88
  - 90-126
  - 128-135
  - 140-142
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/reuse.rs:11-19](crates/gcode/src/commands/codewiki/reuse.rs#L11-L19), [crates/gcode/src/commands/codewiki/reuse.rs:22-31](crates/gcode/src/commands/codewiki/reuse.rs#L22-L31), [crates/gcode/src/commands/codewiki/reuse.rs:36-46](crates/gcode/src/commands/codewiki/reuse.rs#L36-L46), [crates/gcode/src/commands/codewiki/reuse.rs:49-57](crates/gcode/src/commands/codewiki/reuse.rs#L49-L57), [crates/gcode/src/commands/codewiki/reuse.rs:59-88](crates/gcode/src/commands/codewiki/reuse.rs#L59-L88), [crates/gcode/src/commands/codewiki/reuse.rs:90-126](crates/gcode/src/commands/codewiki/reuse.rs#L90-L126), [crates/gcode/src/commands/codewiki/reuse.rs:128-135](crates/gcode/src/commands/codewiki/reuse.rs#L128-L135), [crates/gcode/src/commands/codewiki/reuse.rs:140-142](crates/gcode/src/commands/codewiki/reuse.rs#L140-L142)

</details>

# crates/gcode/src/commands/codewiki/reuse.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file builds a `ReusePlan` that decides when previously generated codewiki docs can be reused without another LLM call. `ReusePlan::load` reads the saved codewiki metadata from the output directory and initializes lazy current-source hash tracking; the `reusable_page` and `reusable_page_with_summary` methods return the on-disk page, and optionally its stored summary, only if the doc still qualifies as reusable. `reusable_pages_with_prefixes` and `reusable` apply that reuse check across matching docs by comparing AI mode, doc health, recorded sources, current source hashes, and whether the generated page still exists on disk, while `current_hash` caches source hashes so missing or unhashable inputs are handled once. `span_files` is a small helper used to turn source spans into file sets for reuse validation.
[crates/gcode/src/commands/codewiki/reuse.rs:11-19]
[crates/gcode/src/commands/codewiki/reuse.rs:22-31]
[crates/gcode/src/commands/codewiki/reuse.rs:36-46]
[crates/gcode/src/commands/codewiki/reuse.rs:49-57]
[crates/gcode/src/commands/codewiki/reuse.rs:59-88]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ReusePlan` | class | `pub(crate) struct ReusePlan {` | `ReusePlan [class]` | `5bda1d67-27ee-567f-a570-6ca7942496a4` | 11-19 [crates/gcode/src/commands/codewiki/reuse.rs:11-19] | Indexed class `ReusePlan` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:11-19] |
| `ReusePlan::load` | method | `pub(crate) fn load(project_root: &Path, out_dir: &Path, ai_mode: &str) -> anyhow::Result<Self> {` | `ReusePlan::load [method]` | `fd379cda-cd64-58fc-b47a-1ad99a09d4ad` | 22-31 [crates/gcode/src/commands/codewiki/reuse.rs:22-31] | Indexed method `ReusePlan::load` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:22-31] |
| `ReusePlan::reusable_page` | method | `pub(crate) fn reusable_page(` | `ReusePlan::reusable_page [method]` | `5ff9ea69-185f-5904-9b4a-79f848b7040d` | 36-46 [crates/gcode/src/commands/codewiki/reuse.rs:36-46] | Indexed method `ReusePlan::reusable_page` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:36-46] |
| `ReusePlan::reusable_page_with_summary` | method | `pub(crate) fn reusable_page_with_summary(` | `ReusePlan::reusable_page_with_summary [method]` | `3c13013a-df0e-597d-b7d7-f27ca3f2f13a` | 49-57 [crates/gcode/src/commands/codewiki/reuse.rs:49-57] | Indexed method `ReusePlan::reusable_page_with_summary` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:49-57] |
| `ReusePlan::reusable_pages_with_prefixes` | method | `pub(crate) fn reusable_pages_with_prefixes(` | `ReusePlan::reusable_pages_with_prefixes [method]` | `34c3b3d4-12a7-5a63-b4fc-7091fdf9f307` | 59-88 [crates/gcode/src/commands/codewiki/reuse.rs:59-88] | Indexed method `ReusePlan::reusable_pages_with_prefixes` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:59-88] |
| `ReusePlan::reusable` | method | `fn reusable(&mut self, doc_path: &str, sources: &BTreeSet<String>) -> bool {` | `ReusePlan::reusable [method]` | `abe1f2df-374f-5334-8974-be39ddb0595c` | 90-126 [crates/gcode/src/commands/codewiki/reuse.rs:90-126] | Indexed method `ReusePlan::reusable` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:90-126] |
| `ReusePlan::current_hash` | method | `fn current_hash(&mut self, file: &str) -> Option<String> {` | `ReusePlan::current_hash [method]` | `c602ef4b-5543-59c1-8768-c633fa5f2f7e` | 128-135 [crates/gcode/src/commands/codewiki/reuse.rs:128-135] | Indexed method `ReusePlan::current_hash` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:128-135] |
| `span_files` | function | `pub(crate) fn span_files(spans: &[SourceSpan]) -> BTreeSet<String> {` | `span_files [function]` | `c65faa98-176a-5618-a15b-adc5dc0d9f74` | 140-142 [crates/gcode/src/commands/codewiki/reuse.rs:140-142] | Indexed function `span_files` in `crates/gcode/src/commands/codewiki/reuse.rs`. [crates/gcode/src/commands/codewiki/reuse.rs:140-142] |
