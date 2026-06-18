---
title: crates/gcode/src/commands/codewiki/build_parts/changes.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build_parts/changes.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

The `crates/gcode/src/commands/codewiki/build_parts/changes.rs` file is responsible for generating structured Markdown change reports that document modifications between codebase index snapshots. It provides developers and automated systems with a clear mechanism to trace files and symbols that have been introduced, modified, or removed across different versions of the codebase index.

At the core of this file is the `build_codewiki_changes_doc` function in `crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101`. This function acts as the generator for the change report, accepting current and optional previous snapshot states to determine changes in files, symbols, and dependency graph neighborhoods. If no previous index snapshot exists, the file gracefully generates a baseline report indicating that this is the initial snapshot.

## How it fits

The main data flow starts with `build_codewiki_changes_doc` in `crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101`, which compares the keys of the file and symbol maps of the previous and current snapshots. It computes sets of added, removed, and modified files by cross-referencing keys and comparing content hashes.
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_codewiki_changes_doc` | function | Generates a markdown change report for a 'CodewikiIndexSnapshot', including frontmatter status, current snapshot counts, and, when a previous snapshot exists, lists of added, removed, and modified files and symbols. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] |
| `ChangesFrontmatter` | class | 'ChangesFrontmatter' is a borrowed frontmatter record that captures change-metadata fields for a document, including title, kind, generator, trust and freshness status, a baseline/degraded flag pair, and a list of degraded sources. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] |
| `changes_frontmatter` | function | Builds a YAML frontmatter block for an “Index Changes” code-changes document from the supplied 'baseline', 'degraded', and 'degraded_sources' flags, serializing a 'ChangesFrontmatter' struct and wrapping it in '---' delimiters with a guaranteed trailing newline. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138] |
| `write_bullet_section` | function | Appends a Markdown '##' section heading to 'doc', emits '- None' when 'items' is empty, otherwise writes each item as a bullet formatted as 'prefix + item + suffix', and terminates the section with a blank line. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156] |
| `symbol_label` | function | Returns a formatted string describing a symbol as ''<qualified_name>' <kind> in '<file_path>''. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163] |

