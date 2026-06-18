---
title: crates/gcode/src/commands/codewiki/render/diagrams.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/diagrams.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/render/diagrams.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

To keep the rendered diagrams clear and readable, the file implements strict edge bounding and hop-limiting strategies. By applying traversal limits, the engine ensures diagrams do not become cluttered, providing notes or comments when elements are omitted due to these constraints.

## How it fits

This file plays a key rendering role within the larger codewiki module, converting raw file and import data into visual documentation assets. It sits at the output phase of dependency extraction, consuming lists of files and graph edge records to construct Markdown-compatible Mermaid code blocks.
[crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166]
[crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_module_dependency_mermaid` | function | Builds and returns an optional Mermaid left-to-right module dependency diagram by aggregating import edges relative to the current page, filtering self-loops, bounding the edge set to 'MAX_MERMAID_HOPS'/'MAX_MERMAID_EDGES' with a fallback to intra-page child edges when no direct page edges exist, and returning 'None' when no renderable bounded edges remain. [crates/gcode/src/commands/codewiki/render/diagrams.rs:5-67] |
| `aggregate_module_for_page` | function | Returns the page path itself when 'module' matches or is a direct descendant of 'page', otherwise truncates 'module' to the first 'max(module_depth(page), 1)' non-empty path segments and joins them with '/'. [crates/gcode/src/commands/codewiki/render/diagrams.rs:72-92] |
| `render_subsystem_dependency_mermaid` | function | Builds and returns a Mermaid left-to-right dependency graph string for subsystem edges derived from the given roots, files, and graph edges, truncating to 'MAX_MERMAID_EDGES' and returning 'None' when no edges exist. [crates/gcode/src/commands/codewiki/render/diagrams.rs:97-127] |
| `render_architecture_structure_mermaid` | function | Builds and returns an optional Mermaid top-down graph string for the given subsystems, rendering each subsystem as a node with edges from the subsystem to its child modules, omitting excess edges beyond 'MAX_MERMAID_EDGES' and returning 'None' when the input is empty. [crates/gcode/src/commands/codewiki/render/diagrams.rs:131-166] |
| `collect_subsystem_dependency_edges` | function | Builds a deduplicated set of directed import dependency edges between distinct subsystem roots by mapping file component IDs to their subsystem root and retaining only 'Import' graph edges whose source and target components belong to different roots. [crates/gcode/src/commands/codewiki/render/diagrams.rs:170-197] |
| `collect_import_module_edges` | function | Builds a 'BTreeSet' of unique '(source_module, target_module)' import edges by mapping component IDs from 'files' to modules, filtering 'graph_edges' to 'Import' edges whose source and target resolve to different modules, and discarding unresolved or intra-module edges. [crates/gcode/src/commands/codewiki/render/diagrams.rs:199-222] |
| `write_partial_import_graph_comment` | function | Appends a Mermaid-style comment line to 'diagram' stating how many import-graph edges were omitted by bounds, but only when 'omitted_edges' is greater than zero. [crates/gcode/src/commands/codewiki/render/diagrams.rs:224-231] |
| `render_module_call_mermaid` | function | Builds a Mermaid call graph for 'module' by mapping file symbols and component IDs to modules, filtering 'Call' edges that involve the target module or its descendants, bounding the graph by hop/edge limits from seed components in the page, and returning 'None' if no relevant bounded edges remain. [crates/gcode/src/commands/codewiki/render/diagrams.rs:233-330] |
| `simplified_diagram_note` | function | Returns a markdown italicized note indicating that only the top 'shown_edges' of 'total_edges' edges of type 'edge_kind' are displayed, with a different message if the source graph was truncated, and otherwise returns an empty string. [crates/gcode/src/commands/codewiki/render/diagrams.rs:332-349] |
| `bounded_module_dependency_edges` | function | Performs a bounded breadth-first traversal from 'module' over the directed dependency graph implied by 'edges' up to 'max_hops', then returns only those edges whose source and target are both reachable within that hop limit. [crates/gcode/src/commands/codewiki/render/diagrams.rs:351-380] |
| `bounded_component_edges` | function | Computes a hop-limited breadth-first reachability set from 'seed_components', then returns up to 'max_edges' edges whose endpoints are both reachable, ordered by the maximum endpoint distance from the seeds. [crates/gcode/src/commands/codewiki/render/diagrams.rs:382-432] |
| `dependency_neighbors` | function | Returns a vector containing the opposite endpoint(s) of a dependency edge when 'module' matches 'source' and/or 'target', yielding 'target' if 'source == module', 'source' if 'target == module', or both if 'source == target == module'. [crates/gcode/src/commands/codewiki/render/diagrams.rs:434-447] |
| `mermaid_node_id` | function | Returns a Mermaid node identifier by prefixing 'm_' to 'module' and replacing every non-ASCII-alphanumeric character with '_'. [crates/gcode/src/commands/codewiki/render/diagrams.rs:449-459] |
| `mermaid_label` | function | Returns '"repo"' for an empty module name, otherwise escapes backslashes, double quotes, and Mermaid-sensitive bracket, parenthesis, brace, and pipe characters in the module string for safe label rendering. [crates/gcode/src/commands/codewiki/render/diagrams.rs:461-476] |

