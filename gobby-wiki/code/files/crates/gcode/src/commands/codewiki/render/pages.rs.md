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

`crates/gcode/src/commands/codewiki/render/pages.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/render/pages.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_module_doc` | function | The 'render_module_doc' function generates a Markdown documentation string for a 'ModuleDoc' by compiling range-free frontmatter, parent module navigation links, an overview section, and structured Markdown tables listing its child modules and direct files. [crates/gcode/src/commands/codewiki/render/pages.rs:5-51] |
| `render_file_doc` | function | The 'render_file_doc' function generates a Markdown document representing a file by assembling metadata-based frontmatter, module reference links, a narrative body, and a structured, capped reference section detailing the non-test API symbols and test summaries. [crates/gcode/src/commands/codewiki/render/pages.rs:53-138] |
| `push_test_summary_line` | function | Appends a formatted Markdown line to a mutable string buffer indicating the number of verifying in-file unit tests, correctly handling pluralization based on the provided count. [crates/gcode/src/commands/codewiki/render/pages.rs:149-152] |

