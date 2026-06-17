---
title: crates/gcode/src/commands/codewiki/build_parts/changes.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
  ranges:
  - 5-101
  - 104-113
  - 115-138
  - 140-156
  - 158-163
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101](crates/gcode/src/commands/codewiki/build_parts/changes.rs#L5-L101), [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113](crates/gcode/src/commands/codewiki/build_parts/changes.rs#L104-L113), [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138](crates/gcode/src/commands/codewiki/build_parts/changes.rs#L115-L138), [crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156](crates/gcode/src/commands/codewiki/build_parts/changes.rs#L140-L156), [crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163](crates/gcode/src/commands/codewiki/build_parts/changes.rs#L158-L163)

</details>

# crates/gcode/src/commands/codewiki/build_parts/changes.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds a Markdown “index changes” document for Codewiki snapshots, comparing an optional previous `CodewikiIndexSnapshot` against the current one and summarizing file, symbol, and graph-neighborhood changes. `build_codewiki_changes_doc` assembles the page, `changes_frontmatter` emits metadata about baseline/degraded states, `write_bullet_section` formats each change list, and `symbol_label` turns symbol snapshots into human-readable labels for added or removed symbols.
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_codewiki_changes_doc` | function | `pub(crate) fn build_codewiki_changes_doc(` | `build_codewiki_changes_doc [function]` | `83dd441f-f8ae-5caf-93ee-7fb58a33acb9` | 5-101 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] | Indexed function `build_codewiki_changes_doc` in `crates/gcode/src/commands/codewiki/build_parts/changes.rs`. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] |
| `ChangesFrontmatter` | class | `struct ChangesFrontmatter<'a> {` | `ChangesFrontmatter [class]` | `66b787f9-a6ca-5499-94e2-9743c2a99efe` | 104-113 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] | Indexed class `ChangesFrontmatter` in `crates/gcode/src/commands/codewiki/build_parts/changes.rs`. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] |
| `changes_frontmatter` | function | `fn changes_frontmatter(` | `changes_frontmatter [function]` | `4e4335db-4971-58c5-9017-670a914be229` | 115-138 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138] | Indexed function `changes_frontmatter` in `crates/gcode/src/commands/codewiki/build_parts/changes.rs`. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138] |
| `write_bullet_section` | function | `fn write_bullet_section(` | `write_bullet_section [function]` | `ceaa24be-e770-5f29-997c-6320949ae401` | 140-156 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156] | Indexed function `write_bullet_section` in `crates/gcode/src/commands/codewiki/build_parts/changes.rs`. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156] |
| `symbol_label` | function | `fn symbol_label(symbol: &CodewikiSymbolSnapshot) -> String {` | `symbol_label [function]` | `a7ee3e63-5ba5-5afb-ab5f-7cb30507dd2a` | 158-163 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163] | Indexed function `symbol_label` in `crates/gcode/src/commands/codewiki/build_parts/changes.rs`. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163] |
