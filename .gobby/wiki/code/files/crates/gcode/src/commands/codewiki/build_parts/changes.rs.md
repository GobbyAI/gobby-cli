---
title: crates/gcode/src/commands/codewiki/build_parts/changes.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
  ranges:
  - 5-101
  - 104-113
  - 115-136
  - 138-154
  - 156-161
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/changes.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

`crates/gcode/src/commands/codewiki/build_parts/changes.rs` exposes 5 indexed API symbols.
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-136]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:138-154] [crates/gcode/src/commands/codewiki/build_parts/changes.rs:156-161]

## API Symbols

- `build_codewiki_changes_doc` (function) component `build_codewiki_changes_doc [function]` (`83dd441f-f8ae-5caf-93ee-7fb58a33acb9`) lines 5-101 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
  - Signature: `pub(crate) fn build_codewiki_changes_doc(`
  - Purpose: Constructs a markdown document comparing current and previous CodewikiIndexSnapshot instances to track file and symbol changes, treating the current snapshot as a baseline when no previous snapshot is available. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
- `ChangesFrontmatter` (class) component `ChangesFrontmatter [class]` (`f7b4c7e6-402b-5579-8998-0be7002599c6`) lines 104-113 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113]
  - Signature: `struct ChangesFrontmatter<'a> {`
  - Purpose: ChangesFrontmatter is a struct containing borrowed metadata about changes, including generation details, quality indicators (trust, freshness), status flags (baseline, degraded), and a vector of degraded source references. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113]
- `changes_frontmatter` (function) component `changes_frontmatter [function]` (`e154758d-f7e9-5e75-85da-07464f161f2a`) lines 115-136 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-136]
  - Signature: `fn changes_frontmatter(baseline: bool, degraded: bool, degraded_sources: &[String]) -> String {`
  - Purpose: Constructs and returns a YAML frontmatter block serializing code change metadata (baseline status, degradation flag, and degraded sources) with proper delimiter formatting. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-136]
- `write_bullet_section` (function) component `write_bullet_section [function]` (`d920d59a-aa9c-5c60-89ff-56ce343a7ec0`) lines 138-154 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:138-154]
  - Signature: `fn write_bullet_section(`
  - Purpose: Appends a markdown section with a level-2 heading and bulleted list items (with optional prefix/suffix wrapping) to a mutable string, or "- None" if the list is empty. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:138-154]
- `symbol_label` (function) component `symbol_label [function]` (`3e7e8fd8-f827-53ae-9b53-5630b832d1a8`) lines 156-161 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:156-161]
  - Signature: `fn symbol_label(symbol: &CodewikiSymbolSnapshot) -> String {`
  - Purpose: This function generates a formatted string label displaying a code symbol's qualified name, kind, and source file path. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:156-161]

