---
title: crates/gcode/src/graph/report/types.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/types.rs
  ranges:
  - 10-17
  - 20-34
  - 36-49
  - 53-68
  - 71-73
  - 76-80
  - 84-88
  - 92-97
  - 100-105
  - 108-118
  - 121-125
  - 128-136
  - 139-142
  - 145-148
  - 151-155
  - 158-162
  - 165-178
  - 184-192
  - 195-200
  - 204-215
  - 218-221
  - 225-229
  - 233-243
  - 247-251
  - 254-256
  - 259-261
  - 265-267
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/report/types.rs:10-17](crates/gcode/src/graph/report/types.rs#L10-L17), [crates/gcode/src/graph/report/types.rs:20-34](crates/gcode/src/graph/report/types.rs#L20-L34), [crates/gcode/src/graph/report/types.rs:36-49](crates/gcode/src/graph/report/types.rs#L36-L49), [crates/gcode/src/graph/report/types.rs:53-68](crates/gcode/src/graph/report/types.rs#L53-L68), [crates/gcode/src/graph/report/types.rs:71-73](crates/gcode/src/graph/report/types.rs#L71-L73), [crates/gcode/src/graph/report/types.rs:76-80](crates/gcode/src/graph/report/types.rs#L76-L80), [crates/gcode/src/graph/report/types.rs:84-88](crates/gcode/src/graph/report/types.rs#L84-L88), [crates/gcode/src/graph/report/types.rs:92-97](crates/gcode/src/graph/report/types.rs#L92-L97), [crates/gcode/src/graph/report/types.rs:100-105](crates/gcode/src/graph/report/types.rs#L100-L105), [crates/gcode/src/graph/report/types.rs:108-118](crates/gcode/src/graph/report/types.rs#L108-L118), [crates/gcode/src/graph/report/types.rs:121-125](crates/gcode/src/graph/report/types.rs#L121-L125), [crates/gcode/src/graph/report/types.rs:128-136](crates/gcode/src/graph/report/types.rs#L128-L136), [crates/gcode/src/graph/report/types.rs:139-142](crates/gcode/src/graph/report/types.rs#L139-L142), [crates/gcode/src/graph/report/types.rs:145-148](crates/gcode/src/graph/report/types.rs#L145-L148), [crates/gcode/src/graph/report/types.rs:151-155](crates/gcode/src/graph/report/types.rs#L151-L155), [crates/gcode/src/graph/report/types.rs:158-162](crates/gcode/src/graph/report/types.rs#L158-L162), [crates/gcode/src/graph/report/types.rs:165-178](crates/gcode/src/graph/report/types.rs#L165-L178), [crates/gcode/src/graph/report/types.rs:184-192](crates/gcode/src/graph/report/types.rs#L184-L192), [crates/gcode/src/graph/report/types.rs:195-200](crates/gcode/src/graph/report/types.rs#L195-L200), [crates/gcode/src/graph/report/types.rs:204-215](crates/gcode/src/graph/report/types.rs#L204-L215), [crates/gcode/src/graph/report/types.rs:218-221](crates/gcode/src/graph/report/types.rs#L218-L221), [crates/gcode/src/graph/report/types.rs:225-229](crates/gcode/src/graph/report/types.rs#L225-L229), [crates/gcode/src/graph/report/types.rs:233-243](crates/gcode/src/graph/report/types.rs#L233-L243), [crates/gcode/src/graph/report/types.rs:247-251](crates/gcode/src/graph/report/types.rs#L247-L251), [crates/gcode/src/graph/report/types.rs:254-256](crates/gcode/src/graph/report/types.rs#L254-L256), [crates/gcode/src/graph/report/types.rs:259-261](crates/gcode/src/graph/report/types.rs#L259-L261), [crates/gcode/src/graph/report/types.rs:265-267](crates/gcode/src/graph/report/types.rs#L265-L267)

</details>

# crates/gcode/src/graph/report/types.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

Defines the data model for graph reports produced by `gcode`, including project-level report payloads, summary and hotspot aggregates, edge/node records, bridge-edge hypotheses, and report errors. `ProjectGraphReportOptions` carries report sizing defaults and normalization, while `BridgeEdgeHypothesis::new` and `::inferred` construct read-only inferred bridge edges with projection metadata. The remaining structs organize counts, confidence ranges, snapshots, and related helper types so the report can be serialized, summarized, and annotated with degradation and investigation details.
[crates/gcode/src/graph/report/types.rs:10-17]
[crates/gcode/src/graph/report/types.rs:20-34]
[crates/gcode/src/graph/report/types.rs:36-49]
[crates/gcode/src/graph/report/types.rs:53-68]
[crates/gcode/src/graph/report/types.rs:71-73]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `BridgeEdgeHypothesis` | class | `pub struct BridgeEdgeHypothesis {` | `BridgeEdgeHypothesis [class]` | `d918517e-c334-52ce-900a-9e965389ae4a` | 10-17 [crates/gcode/src/graph/report/types.rs:10-17] | Indexed class `BridgeEdgeHypothesis` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:10-17] |
| `BridgeEdgeHypothesis::new` | method | `pub fn new(` | `BridgeEdgeHypothesis::new [method]` | `ba33ce95-5ef9-5073-bef7-41d158deca59` | 20-34 [crates/gcode/src/graph/report/types.rs:20-34] | Indexed method `BridgeEdgeHypothesis::new` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:20-34] |
| `BridgeEdgeHypothesis::inferred` | method | `pub fn inferred(` | `BridgeEdgeHypothesis::inferred [method]` | `7b00de4f-4e37-5d8e-9207-47497357abe1` | 36-49 [crates/gcode/src/graph/report/types.rs:36-49] | Indexed method `BridgeEdgeHypothesis::inferred` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:36-49] |
| `ProjectGraphReport` | class | `pub struct ProjectGraphReport {` | `ProjectGraphReport [class]` | `736b2c55-42ec-57f9-b92f-9b76c89a641a` | 53-68 [crates/gcode/src/graph/report/types.rs:53-68] | Indexed class `ProjectGraphReport` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:53-68] |
| `ProjectGraphReportOptions` | class | `pub struct ProjectGraphReportOptions {` | `ProjectGraphReportOptions [class]` | `01af899d-41da-5467-a90c-00bb23c09a05` | 71-73 [crates/gcode/src/graph/report/types.rs:71-73] | Indexed class `ProjectGraphReportOptions` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:71-73] |
| `ProjectGraphReportOptions::default` | method | `fn default() -> Self {` | `ProjectGraphReportOptions::default [method]` | `e40d2796-48c9-58a3-a236-b0b21433ba9c` | 76-80 [crates/gcode/src/graph/report/types.rs:76-80] | Indexed method `ProjectGraphReportOptions::default` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:76-80] |
| `ProjectGraphReportOptions::normalized` | method | `pub(super) fn normalized(self) -> Self {` | `ProjectGraphReportOptions::normalized [method]` | `78d1b3e4-93d3-5791-bf3f-86126114eab1` | 84-88 [crates/gcode/src/graph/report/types.rs:84-88] | Indexed method `ProjectGraphReportOptions::normalized` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:84-88] |
| `GraphReportSummary` | class | `pub struct GraphReportSummary {` | `GraphReportSummary [class]` | `aab5e21d-fb38-5b57-a1be-b52e369980e4` | 92-97 [crates/gcode/src/graph/report/types.rs:92-97] | Indexed class `GraphReportSummary` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:92-97] |
| `GraphReportHotspots` | class | `pub struct GraphReportHotspots {` | `GraphReportHotspots [class]` | `8cf33a5b-e916-5815-b5a5-417f5b145ba3` | 100-105 [crates/gcode/src/graph/report/types.rs:100-105] | Indexed class `GraphReportHotspots` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:100-105] |
| `GraphHotspot` | class | `pub struct GraphHotspot {` | `GraphHotspot [class]` | `fd3fd065-2c4a-5417-a7d2-2a034a958a1a` | 108-118 [crates/gcode/src/graph/report/types.rs:108-118] | Indexed class `GraphHotspot` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:108-118] |
| `TargetFrequency` | class | `pub struct TargetFrequency {` | `TargetFrequency [class]` | `73aa6fbb-8662-50bb-9035-ba2c9e89dc22` | 121-125 [crates/gcode/src/graph/report/types.rs:121-125] | Indexed class `TargetFrequency` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:121-125] |
| `BridgeReportSummary` | class | `pub struct BridgeReportSummary {` | `BridgeReportSummary [class]` | `018ad04b-3a6c-5dfe-b4ec-a43b0694c285` | 128-136 [crates/gcode/src/graph/report/types.rs:128-136] | Indexed class `BridgeReportSummary` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:128-136] |
| `NamedCount` | class | `pub struct NamedCount {` | `NamedCount [class]` | `312eac88-28c0-5584-8e8d-d96efcd071d5` | 139-142 [crates/gcode/src/graph/report/types.rs:139-142] | Indexed class `NamedCount` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:139-142] |
| `ConfidenceRange` | class | `pub struct ConfidenceRange {` | `ConfidenceRange [class]` | `8015de67-583e-51b7-b2f7-d757d1da8b08` | 145-148 [crates/gcode/src/graph/report/types.rs:145-148] | Indexed class `ConfidenceRange` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:145-148] |
| `ReportDegradation` | class | `pub struct ReportDegradation {` | `ReportDegradation [class]` | `ea809185-b36b-513b-86a9-59c58b3c46a8` | 151-155 [crates/gcode/src/graph/report/types.rs:151-155] | Indexed class `ReportDegradation` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:151-155] |
| `ProjectGraphReportError` | type | `pub enum ProjectGraphReportError {` | `ProjectGraphReportError [type]` | `2165f448-b64d-5cdb-b9c4-9c5b242c5608` | 158-162 [crates/gcode/src/graph/report/types.rs:158-162] | Indexed type `ProjectGraphReportError` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:158-162] |
| `ProjectGraphReportError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `ProjectGraphReportError::fmt [method]` | `3c51fdb9-a59d-589d-99a4-45fd856a1115` | 165-178 [crates/gcode/src/graph/report/types.rs:165-178] | Indexed method `ProjectGraphReportError::fmt` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:165-178] |
| `ReportGraphSnapshot` | class | `pub(super) struct ReportGraphSnapshot {` | `ReportGraphSnapshot [class]` | `4fd60dcc-aa30-58ce-a308-e9a3ad15df41` | 184-192 [crates/gcode/src/graph/report/types.rs:184-192] | Indexed class `ReportGraphSnapshot` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:184-192] |
| `ReportNode` | class | `pub(super) struct ReportNode {` | `ReportNode [class]` | `c8ca1e44-4439-55e7-a0b1-1ac18baff53a` | 195-200 [crates/gcode/src/graph/report/types.rs:195-200] | Indexed class `ReportNode` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:195-200] |
| `ReportNode::new` | method | `pub(super) fn new(` | `ReportNode::new [method]` | `26313d90-b424-514e-a96b-db75bb1a36f5` | 204-215 [crates/gcode/src/graph/report/types.rs:204-215] | Indexed method `ReportNode::new` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:204-215] |
| `ReportNode::with_file_path` | method | `pub(super) fn with_file_path(mut self, file_path: impl Into<String>) -> Self {` | `ReportNode::with_file_path [method]` | `365ff31d-340c-5b2a-8403-48f494001740` | 218-221 [crates/gcode/src/graph/report/types.rs:218-221] | Indexed method `ReportNode::with_file_path` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:218-221] |
| `ReportCodeEdge` | class | `pub(super) struct ReportCodeEdge {` | `ReportCodeEdge [class]` | `954751e9-880d-5494-8292-71db5ebe736d` | 225-229 [crates/gcode/src/graph/report/types.rs:225-229] | Indexed class `ReportCodeEdge` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:225-229] |
| `ReportCodeEdge::new` | method | `pub(super) fn new(` | `ReportCodeEdge::new [method]` | `c9b69d5d-178d-5767-89c0-ff7b2e809152` | 233-243 [crates/gcode/src/graph/report/types.rs:233-243] | Indexed method `ReportCodeEdge::new` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:233-243] |
| `BridgeEdgeInput` | type | `pub(super) enum BridgeEdgeInput {` | `BridgeEdgeInput [type]` | `2cdc924e-0a75-53cf-bf45-d26fda8442b1` | 247-251 [crates/gcode/src/graph/report/types.rs:247-251] | Indexed type `BridgeEdgeInput` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:247-251] |
| `BridgeEdgeInput::available` | method | `pub(super) fn available(edges: Vec<BridgeEdgeHypothesis>) -> Self {` | `BridgeEdgeInput::available [method]` | `01b34a2c-95ec-505d-be24-f39290d33ee1` | 254-256 [crates/gcode/src/graph/report/types.rs:254-256] | Indexed method `BridgeEdgeInput::available` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:254-256] |
| `BridgeEdgeInput::unavailable` | method | `pub(super) fn unavailable(reason: impl Into<String>) -> Self {` | `BridgeEdgeInput::unavailable [method]` | `b05657c3-0f2b-58bf-a139-a8ee8d26e1ba` | 259-261 [crates/gcode/src/graph/report/types.rs:259-261] | Indexed method `BridgeEdgeInput::unavailable` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:259-261] |
| `BridgeEdgeInput::default` | method | `fn default() -> Self {` | `BridgeEdgeInput::default [method]` | `2ca3a8c2-d7a4-5e3d-beda-41b6d4763941` | 265-267 [crates/gcode/src/graph/report/types.rs:265-267] | Indexed method `BridgeEdgeInput::default` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:265-267] |
