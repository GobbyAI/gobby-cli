---
title: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
  ranges:
  - 5-134
  - 136-160
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/hotspots.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds the codewiki “hotspots” document by combining file docs with graph edges and graph availability state. `build_hotspots_doc` returns an empty, degraded document when analytics are unavailable, otherwise it derives hotspot nodes from all symbols via `hotspot_nodes`, converts the surviving edges into an `AnalyticsGraph`, runs graph analytics, and packages the resulting hotspots, bridges, god nodes, and source spans along with any degraded-source markers.
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134]
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160]

## API Symbols

- `build_hotspots_doc` (function) component `build_hotspots_doc [function]` (`827f6d4e-76a7-54f7-ad22-c97eb3ead5a9`) lines 5-134 [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134]
  - Signature: `pub(crate) fn build_hotspots_doc(`
  - Purpose: 'build_hotspots_doc' builds a 'HotspotsDoc' from file docs and graph edges by deriving hotspot nodes, filtering and translating graph edges into an 'AnalyticsGraph', and propagating graph availability into 'degraded_sources', returning an empty document when analytics are unavailable. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134]
- `hotspot_nodes` (function) component `hotspot_nodes [function]` (`18942d3b-f308-5760-92c4-056e14bbba25`) lines 136-160 [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160]
  - Signature: `fn hotspot_nodes(files: &[FileDoc]) -> BTreeMap<String, HotspotNode> {`
  - Purpose: Builds a 'BTreeMap' keyed by each symbol’s 'component_id' to 'HotspotNode' records derived from all symbols in all files, using the symbol’s qualified name when present otherwise its name, and attaching wikilinks, file wikilinks, kind, and source span metadata. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160]

