---
title: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/concepts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_curated_navigation_docs` | function | Builds curated navigation documentation by reusing previously generated pages when source spans are unchanged, otherwise generating or falling back to a navigation plan and rendering the resulting docs with optional verification and degraded-mode tracking. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85] |
| `module_with_diagram` | function | Constructs and returns a 'ModuleDoc' for the given module name with empty summary/spans/files/children, an optional copied dependency diagram, no call diagram, the provided graph availability, and all other fields initialized to their default non-degraded, unreused state. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:93-110] |
| `curated_diagram_injected_when_graph_available` | function | Verifies that when a module has an available curated Mermaid diagram, 'append_dependency_diagram' adds an '## Architecture diagram' section containing the diagram markup and does not emit a 'graph-truncated' marker. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:113-124] |
| `curated_diagram_marks_truncated_graph` | function | Asserts that 'append_dependency_diagram' renders a Mermaid diagram with the 'degraded: graph-truncated' marker when given a module whose graph availability is 'Truncated', while preserving the original Mermaid block. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:127-137] |
| `curated_diagram_skipped_when_unavailable_or_absent` | function | Verifies that 'append_dependency_diagram' appends nothing when given 'None', an unavailable graph, or a module without a diagram, leaving the output string empty. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:140-152] |
| `largest_member_module_requires_a_diagram` | function | Verifies that 'largest_member_module' returns the member module that has an attached diagram when one exists, and returns 'None' for a member module without a diagram. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:155-169] |

