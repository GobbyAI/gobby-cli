---
title: crates/gcode/src/commands/codewiki/render/pages.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/pages.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/render/pages.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

The function `render_module_doc` crates/gcode/src/commands/codewiki/render/pages.rs:6-68 constructs the Markdown representation of a module. It formats frontmatter, establishes parent navigation links, includes overview narratives, and lists nested child modules or files in table formats. It also conditionally embeds dependency and call diagrams based on graph availability crates/gcode/src/commands/codewiki/render/pages.rs:24-44.

## How it fits
[crates/gcode/src/commands/codewiki/render/pages.rs:6-68]
[crates/gcode/src/commands/codewiki/render/pages.rs:70-111]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_module_doc` | function | 'render_module_doc' builds a Markdown document for a 'ModuleDoc' by emitting frontmatter, the module heading and parent link, an overview section, dependency/call diagram sections conditioned on graph availability, and a child-modules table when present. [crates/gcode/src/commands/codewiki/render/pages.rs:6-68] |
| `render_file_doc` | function | 'render_file_doc' builds and returns a Markdown document for a 'FileDoc', starting with frontmatter and a file heading/module link plus optional body text, then appending a “Key components” table of indexed symbols with their kinds and neutralized purposes, or a “No indexed symbols” note if none exist. [crates/gcode/src/commands/codewiki/render/pages.rs:70-111] |

