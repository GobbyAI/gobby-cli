---
title: crates/gcode/src/commands/codewiki/build_parts/changes.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/changes.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/changes.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/changes.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_codewiki_changes_doc` | function | Generates a markdown change report for a 'CodewikiIndexSnapshot', including frontmatter status, current snapshot counts, and, when a previous snapshot exists, lists of added, removed, and modified files and symbols. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101] |
| `ChangesFrontmatter` | class | 'ChangesFrontmatter' is a borrowed frontmatter record that captures change-metadata fields for a document, including title, kind, generator, trust and freshness status, a baseline/degraded flag pair, and a list of degraded sources. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:104-113] |
| `changes_frontmatter` | function | Builds a YAML frontmatter block for an “Index Changes” code-changes document from the supplied 'baseline', 'degraded', and 'degraded_sources' flags, serializing a 'ChangesFrontmatter' struct and wrapping it in '---' delimiters with a guaranteed trailing newline. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:115-138] |
| `write_bullet_section` | function | Appends a Markdown '##' section heading to 'doc', emits '- None' when 'items' is empty, otherwise writes each item as a bullet formatted as 'prefix + item + suffix', and terminates the section with a blank line. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:140-156] |
| `symbol_label` | function | Returns a formatted string describing a symbol as ''<qualified_name>' <kind> in '<file_path>''. [crates/gcode/src/commands/codewiki/build_parts/changes.rs:158-163] |

