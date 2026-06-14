---
title: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
  ranges:
  - 5-131
  - 133-157
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/hotspots.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

This file builds hotspot documentation by analyzing code structure and dependencies. The `build_hotspots_doc` function orchestrates the process: it checks graph availability and returns an empty degraded document if analytics are unavailable; otherwise it collects hotspot nodes from files via `hotspot_nodes`, constructs a weighted analytics graph where nodes are weighted by line count and edges represent calls/imports, filters edges to include only those with both endpoints present, then runs graph analytics to identify important nodes. The `hotspot_nodes` helper flattens all symbols across input file documents into a keyed map, extracting each symbol's kind, qualified name, file/wiki references, and source span information.
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-131]
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:133-157]

## API Symbols

- `build_hotspots_doc` (function) component `build_hotspots_doc [function]` (`827f6d4e-76a7-54f7-ad22-c97eb3ead5a9`) lines 5-131 [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-131]
  - Signature: `pub(crate) fn build_hotspots_doc(`
  - Purpose: Builds a `HotspotsDoc` from `files` and `graph_edges`, returning an empty degraded document when graph analytics are unavailable and otherwise constructing a weighted analytics graph from hotspot nodes plus edges whose endpoints are both present. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-131]
- `hotspot_nodes` (function) component `hotspot_nodes [function]` (`d5ea9924-4f7a-59fa-af46-01b397a81526`) lines 133-157 [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:133-157]
  - Signature: `fn hotspot_nodes(files: &[FileDoc]) -> BTreeMap<String, HotspotNode> {`
  - Purpose: It flattens all symbols across the input `FileDoc`s into a `BTreeMap` keyed by `component_id`, building each `HotspotNode` from the symbol’s kind, preferred label (`qualified_name` or `name`), file and code wikilinks, and source span. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:133-157]

