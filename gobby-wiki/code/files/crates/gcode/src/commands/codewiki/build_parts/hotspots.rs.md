---
title: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/hotspots.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/hotspots.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/hotspots.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_hotspots_doc` | function | Builds a 'HotspotsDoc' by deriving hotspot nodes from 'files', constructing an analytics graph from in-scope 'graph_edges' and node span weights, and returning a degraded or empty document when graph analytics is truncated or unavailable. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134] |
| `hotspot_nodes` | function | Builds a 'BTreeMap' keyed by each symbol’s 'component_id', where each 'HotspotNode' is assembled from file and symbol metadata using the symbol’s qualified name when available, otherwise its name, along with wiki links and source span. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160] |

