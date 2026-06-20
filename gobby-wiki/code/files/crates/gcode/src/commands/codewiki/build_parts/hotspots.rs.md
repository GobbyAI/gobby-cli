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

`crates/gcode/src/commands/codewiki/build_parts/hotspots.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_hotspots_doc` | function | 'build_hotspots_doc' constructs a 'HotspotsDoc' from 'files' and filtered 'graph_edges', but returns an empty, non-degraded hotspots document when graph analytics are unavailable. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-130] |
| `hotspot_nodes` | function | Builds a 'BTreeMap' from each symbol’s 'component_id' to a 'HotspotNode' populated with its kind, resolved label, file and source-span links, by flattening all symbols across the input files. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:132-156] |

