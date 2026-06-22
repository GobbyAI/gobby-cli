---
title: crates/gcode/src/commands/codewiki/render/overview.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/overview.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render/overview.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

`crates/gcode/src/commands/codewiki/render/overview.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/render/overview.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_architecture_doc` | function | The 'render_architecture_doc' function serializes an 'ArchitectureDoc' struct into a Markdown-formatted string comprising frontmatter metadata, related source files, a narrative overview, architectural diagrams, a service matrix, and a tabular listing of subsystems and their child modules. [crates/gcode/src/commands/codewiki/render/overview.rs:5-63] |
| `render_onboarding_doc` | function | This function serializes an 'OnboardingDoc' struct into a Markdown-formatted onboarding guide containing metadata frontmatter, referenced source files, listed entry points, and an optional recommended reading order section populated with module centralities, scores, and summaries. [crates/gcode/src/commands/codewiki/render/overview.rs:65-102] |
| `render_hotspots_doc` | function | The 'render_hotspots_doc' function serializes a 'HotspotsDoc' struct into a Markdown string containing frontmatter metadata, relevant source file lists, and structured sections for hotspots, god nodes, and bridges, with cross-references where appropriate and fallback text when no results are found. [crates/gcode/src/commands/codewiki/render/overview.rs:104-139] |
| `write_hotspot_section` | function | The 'write_hotspot_section' function appends a formatted hotspot section to a mutable document string with a specified title and slice of findings by delegating to 'write_hotspot_section_with_cross_refs' without cross-references. [crates/gcode/src/commands/codewiki/render/overview.rs:141-143] |
| `write_hotspot_section_with_cross_refs` | function | This function appends a Markdown-formatted section to a mutable string buffer, iterating over a collection of hotspot findings to write either their detailed attributes—such as kind, component, score, and source span—or a simplified cross-reference line if the finding is already listed under a specified section. [crates/gcode/src/commands/codewiki/render/overview.rs:145-204] |

