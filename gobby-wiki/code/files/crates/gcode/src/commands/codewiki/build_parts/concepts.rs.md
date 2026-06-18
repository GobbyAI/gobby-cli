---
title: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build_parts/concepts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

This file serves as the coordinator for building curated conceptual and navigation documentation within the Codewiki build pipeline. It is responsible for orchestrating high-level overview documentation and guided tours, ensuring they remain digestible and structurally bounded.

A primary role of this file is to define structural constraints for curated documentation. It defines constants that cap the number of narrative chapters and limit list lengths, such as the maximum number of key components and source file links. These constraints prevent verbose automated outputs from overwhelming the final user-facing documentation structure.

## How it fits

This file represents a key module entry point, delegating specific processing tasks to its path-declared submodules including plan, render, spans, support, and types. It integrates directly with the broader Codewiki build system by consuming arrays of FileDoc and ModuleDoc structures.

During the documentation generation flow, the build process extracts all input spans to evaluate document freshness. If the reuse planner confirms that source spans are unchanged, previously compiled markdown pages under the concepts and narrative paths are returned directly, saving translation and processing overhead.
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:93-110]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:113-124]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:127-137]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:140-152]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_curated_navigation_docs` | function | Builds curated navigation documentation by reusing previously generated pages when source spans are unchanged, otherwise generating or falling back to a navigation plan and rendering the resulting docs with optional verification and degraded-mode tracking. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85] |
| `module_with_diagram` | function | Constructs and returns a 'ModuleDoc' for the given module name with empty summary/spans/files/children, an optional copied dependency diagram, no call diagram, the provided graph availability, and all other fields initialized to their default non-degraded, unreused state. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:93-110] |
| `curated_diagram_injected_when_graph_available` | function | Verifies that when a module has an available curated Mermaid diagram, 'append_dependency_diagram' adds an '## Architecture diagram' section containing the diagram markup and does not emit a 'graph-truncated' marker. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:113-124] |
| `curated_diagram_marks_truncated_graph` | function | Asserts that 'append_dependency_diagram' renders a Mermaid diagram with the 'degraded: graph-truncated' marker when given a module whose graph availability is 'Truncated', while preserving the original Mermaid block. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:127-137] |
| `curated_diagram_skipped_when_unavailable_or_absent` | function | Verifies that 'append_dependency_diagram' appends nothing when given 'None', an unavailable graph, or a module without a diagram, leaving the output string empty. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:140-152] |
| `largest_member_module_requires_a_diagram` | function | Verifies that 'largest_member_module' returns the member module that has an attached diagram when one exists, and returns 'None' for a member module without a diagram. [crates/gcode/src/commands/codewiki/build_parts/concepts.rs:155-169] |

