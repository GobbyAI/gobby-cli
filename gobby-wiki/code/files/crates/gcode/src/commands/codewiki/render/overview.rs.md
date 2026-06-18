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

`crates/gcode/src/commands/codewiki/render/overview.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_architecture_doc` | function | Builds a markdown architecture document string by adding frontmatter and relevant source-file references, then conditionally rendering an overview section, a subsystem dependency diagram, and a subsystems table with module links, responsibilities, and child modules. [crates/gcode/src/commands/codewiki/render/overview.rs:5-48] |
| `render_onboarding_doc` | function | Builds a markdown onboarding document by prepending frontmatter and relevant source-file references, then adding a '# Start Here' heading, an optional 'Entry Points' list, and, if present, a numbered 'Recommended Reading Order' ranked by module centrality score. [crates/gcode/src/commands/codewiki/render/overview.rs:50-87] |
| `render_hotspots_doc` | function | Builds a markdown hotspots document with frontmatter and relevant source-file references, emits an “analytics unavailable” notice and returns early if graph analytics are missing, otherwise renders Hotspots/God Nodes/Bridges sections with cross-references to hotspot IDs and adds a no-results message when all sections are empty. [crates/gcode/src/commands/codewiki/render/overview.rs:89-133] |
| `write_hotspot_section` | function | Delegates hotspot section rendering to 'write_hotspot_section_with_cross_refs', passing the document buffer, title, findings slice, and 'None' for cross references. [crates/gcode/src/commands/codewiki/render/overview.rs:135-137] |
| `write_hotspot_section_with_cross_refs` | function | Writes a markdown “hotspot” section into 'doc' with a heading, emits “None identified.” for an empty finding list, and otherwise formats each 'HotspotFinding' as a bullet with inline metadata, collapsing entries already covered by an optional cross-reference section into a short pointer instead of duplicating details. [crates/gcode/src/commands/codewiki/render/overview.rs:139-198] |

