---
title: crates/gcode/src/commands/codewiki/render/pages.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/pages.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render/pages.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

`crates/gcode/src/commands/codewiki/render/pages.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/render/pages.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_module_doc` | function | 'render_module_doc' builds a Markdown document for a 'ModuleDoc' by emitting frontmatter, the module heading and parent link, an overview section, dependency/call diagram sections conditioned on graph availability, and a child-modules table when present. [crates/gcode/src/commands/codewiki/render/pages.rs:6-68] |
| `render_file_doc` | function | 'render_file_doc' builds and returns a Markdown document for a 'FileDoc', starting with frontmatter and a file heading/module link plus optional body text, then appending a “Key components” table of indexed symbols with their kinds and neutralized purposes, or a “No indexed symbols” note if none exist. [crates/gcode/src/commands/codewiki/render/pages.rs:70-111] |

