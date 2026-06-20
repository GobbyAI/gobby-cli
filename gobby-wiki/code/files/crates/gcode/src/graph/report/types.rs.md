---
title: crates/gcode/src/graph/report/types.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/types.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Overview

`crates/gcode/src/graph/report/types.rs` exposes 27 indexed API symbols.

## How it fits

`crates/gcode/src/graph/report/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `BridgeEdgeHypothesis` | class | 'BridgeEdgeHypothesis' is a Rust struct representing a hypothesized bridge edge between a source node and a target symbol, annotated with a relation, display label, read-only flag, and associated 'ProjectionMetadata'. [crates/gcode/src/graph/report/types.rs:10-17] |
| `BridgeEdgeHypothesis::new` | method | Constructs a new read-only projection record by converting the source, target symbol, and relation inputs into owned strings, setting 'label' to '"inferred hypothesis"', and storing the provided 'ProjectionMetadata'. [crates/gcode/src/graph/report/types.rs:20-34] |
| `BridgeEdgeHypothesis::inferred` | method | Creates a new instance by forwarding 'source_id', 'target_symbol_id', and 'relation' to 'Self::new' and supplying inferred 'ProjectionMetadata' built from 'source_system' and optional 'confidence'. [crates/gcode/src/graph/report/types.rs:36-49] |
| `ProjectGraphReport` | class | 'ProjectGraphReport' is a serialized report struct that aggregates a project’s graph analysis metadata, summary and hotspot metrics, unresolved/external target frequencies, optional bridge analysis, degradation details, investigation questions, and a rendered markdown narrative. [crates/gcode/src/graph/report/types.rs:53-68] |
| `ProjectGraphReportOptions` | class | 'ProjectGraphReportOptions' is a Rust configuration struct for project graph reporting that specifies 'top_n', the number of top entries to include. [crates/gcode/src/graph/report/types.rs:71-73] |
| `ProjectGraphReportOptions::default` | method | Returns a new 'Self' instance with 'top_n' initialized to 'DEFAULT_TOP_LIMIT'. [crates/gcode/src/graph/report/types.rs:76-80] |
| `ProjectGraphReportOptions::normalized` | method | Returns a new 'Self' with 'top_n' clamped to a minimum of '1' using 'max(1)'. [crates/gcode/src/graph/report/types.rs:84-88] |
| `GraphReportSummary` | class | 'GraphReportSummary' is a report aggregate that records total node and edge counts plus per-type node counts and per-kind code edge counts in ordered maps. [crates/gcode/src/graph/report/types.rs:92-97] |
| `GraphReportHotspots` | class | 'GraphReportHotspots' is a report container that groups 'GraphHotspot' lists for high-degree files, symbols, modules, and incoming-call hotspots. [crates/gcode/src/graph/report/types.rs:100-105] |
| `GraphHotspot` | class | GraphHotspot is a serde-serializable record that describes a graph node hotspot with an ID, display name, node type, total degree, incoming and outgoing edge counts, and an optional file path. [crates/gcode/src/graph/report/types.rs:108-118] |
| `TargetFrequency` | class | 'TargetFrequency' is a public struct that represents a named frequency entry with an identifier ('id'), display name ('name'), and occurrence count ('count'). [crates/gcode/src/graph/report/types.rs:121-125] |
| `BridgeReportSummary` | class | 'BridgeReportSummary' is a serializable summary record for a bridge relationship, capturing the relation label, edge count, whether it was inferred or read-only, per-source-system counts, and an optional confidence range. [crates/gcode/src/graph/report/types.rs:128-136] |
| `NamedCount` | class | 'NamedCount' is a public struct that pairs a 'String' name with a 'usize' count. [crates/gcode/src/graph/report/types.rs:139-142] |
| `ConfidenceRange` | class | 'ConfidenceRange' is a public Rust struct representing an inclusive numeric confidence interval with 'f64' bounds 'min' and 'max'. [crates/gcode/src/graph/report/types.rs:145-148] |
| `ReportDegradation` | class | 'ReportDegradation' is a data struct that records an input identifier, a boolean indicating whether degradation reporting is mandatory, and a free-form detail string describing the degradation. [crates/gcode/src/graph/report/types.rs:151-155] |
| `ProjectGraphReportError` | type | Indexed type `ProjectGraphReportError` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:158-162] |
| `ProjectGraphReportError::fmt` | method | Implements 'fmt::Display' for the enum by matching each variant and writing a variant-specific human-readable error message, optionally including the embedded 'message' field. [crates/gcode/src/graph/report/types.rs:165-178] |
| `ReportGraphSnapshot` | class | 'ReportGraphSnapshot' is a report-oriented graph snapshot that aggregates nodes, code edges, optional summary and hotspot metadata, optional unresolved and external target frequency lists, and bridge-edge input for downstream analysis or rendering. [crates/gcode/src/graph/report/types.rs:184-192] |
| `ReportNode` | class | 'ReportNode' is a package-visible Rust struct that models a report node with required 'id', 'name', and 'node_type' string fields plus an optional 'file_path' string. [crates/gcode/src/graph/report/types.rs:195-200] |
| `ReportCodeEdge` | class | 'ReportCodeEdge' is a 'pub(super)' data struct that represents a code edge with three owned string fields: 'source', 'target', and 'edge_type'. [crates/gcode/src/graph/report/types.rs:225-229] |
| `BridgeEdgeInput` | type | Indexed type `BridgeEdgeInput` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:247-251] |
| `BridgeEdgeInput::available` | method | Constructs and returns a 'Self::Available' variant containing the provided 'Vec<BridgeEdgeHypothesis>'. [crates/gcode/src/graph/report/types.rs:254-256] |
| `BridgeEdgeInput::default` | method | Returns a 'Self::Available' value containing an empty 'Vec', i.e. the default state is an available instance with no elements. [crates/gcode/src/graph/report/types.rs:265-267] |

_Verified by 4 in-file unit tests._

