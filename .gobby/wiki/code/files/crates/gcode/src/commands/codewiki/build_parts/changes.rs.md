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

# crates/gcode/src/commands/codewiki/build_parts/changes.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

This file builds the Markdown “Index Changes” page for Codewiki snapshots. `build_codewiki_changes_doc` starts by writing YAML frontmatter and current-snapshot counts, then either marks the page as the baseline when no prior snapshot exists or compares `previous` and `current` to list added, removed, and content-changed files plus added and removed symbols. `changes_frontmatter` serializes metadata about generation, trust/freshness, baseline state, and degraded sources, while `write_bullet_section` formats the comparison results into reusable bullet sections and `symbol_label` renders human-readable symbol entries.
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163]

## API Symbols

- `build_codewiki_changes_doc` (function) component `build_codewiki_changes_doc [function]` (`83dd441f-f8ae-5caf-93ee-7fb58a33acb9`) lines 5-101 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
  - Signature: `pub(crate) fn build_codewiki_changes_doc(`
  - Purpose: Generates a markdown document documenting changes between two CodewikiIndexSnapshot versions by comparing file and symbol additions, removals, and content hash modifications, with special handling for baseline snapshots. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
- `ChangesFrontmatter` (class) component `ChangesFrontmatter [class]` (`66b787f9-a6ca-5499-94e2-9743c2a99efe`) lines 104-113 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113]
  - Signature: `struct ChangesFrontmatter<'a> {`
  - Purpose: `ChangesFrontmatter` is a struct that encapsulates metadata and quality indicators for changes, including generation provenance, trust/freshness metrics, baseline status, and a list of degraded data sources. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113]
- `changes_frontmatter` (function) component `changes_frontmatter [function]` (`4e4335db-4971-58c5-9017-670a914be229`) lines 115-138 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138]
  - Signature: `fn changes_frontmatter(`
  - Purpose: This function constructs and returns a YAML-formatted frontmatter block by serializing a `ChangesFrontmatter` struct containing code change metadata, baseline/degradation status, and degraded sources. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138]
- `write_bullet_section` (function) component `write_bullet_section [function]` (`ceaa24be-e770-5f29-997c-6320949ae401`) lines 140-156 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156]
  - Signature: `fn write_bullet_section(`
  - Purpose: Appends a Markdown section with a level-2 heading and bullet-point list to a string, wrapping each item with optional prefix and suffix strings, or defaulting to "- None" if the items vector is empty. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156]
- `symbol_label` (function) component `symbol_label [function]` (`a7ee3e63-5ba5-5afb-ab5f-7cb30507dd2a`) lines 158-163 [crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163]
  - Signature: `fn symbol_label(symbol: &CodewikiSymbolSnapshot) -> String {`
  - Purpose: Returns a formatted string label concatenating a code symbol's qualified name, kind, and file path. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163]

