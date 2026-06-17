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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134](crates/gcode/src/commands/codewiki/build_parts/hotspots.rs#L5-L134), [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160](crates/gcode/src/commands/codewiki/build_parts/hotspots.rs#L136-L160)

</details>

# crates/gcode/src/commands/codewiki/build_parts/hotspots.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds the codewiki “hotspots” document from file docs and graph edges by first checking graph availability, then assembling an analytics graph from the file-derived hotspot nodes and filtered call/import edges. It uses source-span length as node weight, records degraded-source markers when graph data is truncated or unavailable, and returns the computed hotspots, god nodes, bridges, and spans; `hotspot_nodes` supplies the node set used by that assembly.
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134]
[crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_hotspots_doc` | function | `pub(crate) fn build_hotspots_doc(` | `build_hotspots_doc [function]` | `827f6d4e-76a7-54f7-ad22-c97eb3ead5a9` | 5-134 [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134] | Indexed function `build_hotspots_doc` in `crates/gcode/src/commands/codewiki/build_parts/hotspots.rs`. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134] |
| `hotspot_nodes` | function | `fn hotspot_nodes(files: &[FileDoc]) -> BTreeMap<String, HotspotNode> {` | `hotspot_nodes [function]` | `18942d3b-f308-5760-92c4-056e14bbba25` | 136-160 [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160] | Indexed function `hotspot_nodes` in `crates/gcode/src/commands/codewiki/build_parts/hotspots.rs`. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160] |
