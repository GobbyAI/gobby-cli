---
title: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build_parts/hotspots.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

The main entry point is the build_hotspots_doc function [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134]. This function processes incoming source files and graph edges to construct an analytical representation of the codebase. If graph analytics are truncated or completely unavailable, it gracefully handles these states by returning a degraded or empty document [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:10-25].

## How it fits

This file fits into the larger codewiki command pipeline under crates/gcode/src/commands/codewiki/build_parts/hotspots.rs. It bridges raw file and symbol metadata with graph-theoretic algorithms defined in gobby_core::graph_analytics .

Once the lookup map is prepared, build_hotspots_doc builds an AnalyticsGraph [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:28]. It uses the node lookup map to resolve edge endpoints, ensuring only edges connecting valid hotspot nodes are included [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:45-49]. Edge weights are assigned based on their type, such as function calls or module imports [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:50-64]. This completed graph is then used to perform graph calculations, outputting a structured HotspotsDoc containing key metrics like god nodes and bridges.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_hotspots_doc` | function | Builds a 'HotspotsDoc' by deriving hotspot nodes from 'files', constructing an analytics graph from in-scope 'graph_edges' and node span weights, and returning a degraded or empty document when graph analytics is truncated or unavailable. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:5-134] |
| `hotspot_nodes` | function | Builds a 'BTreeMap' keyed by each symbol’s 'component_id', where each 'HotspotNode' is assembled from file and symbol metadata using the symbol’s qualified name when available, otherwise its name, along with wiki links and source span. [crates/gcode/src/commands/codewiki/build_parts/hotspots.rs:136-160] |

