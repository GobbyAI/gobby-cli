---
title: crates/gcode/src/graph/report/types.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/report/types.rs
  ranges:
  - 10-17
  - 19-50
  - 53-68
  - 71-73
  - 75-81
  - 83-89
  - 92-97
  - 100-105
  - 108-118
  - 121-125
  - 128-136
  - 139-142
  - 145-148
  - 151-155
  - 158-162
  - 164-179
  - '181'
  - 184-192
  - 195-200
  - 202-222
  - 225-229
  - 231-244
  - 247-251
  - 253-262
  - 264-268
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/report/types.rs

Module: [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]

## Purpose

This file defines type structures and implementations for dependency graph analysis and reporting. It provides several layers of abstractions: core elements like BridgeEdgeHypothesis (directed edges with relation semantics and metadata) and graph topology nodes/edges (ReportNode, ReportCodeEdge); analysis results including GraphReportHotspots (high-degree files, symbols, modules), TargetFrequency (occurrence metrics), and ConfidenceRange (numeric bounds); configuration options (ProjectGraphReportOptions) for controlling report scope; and error handling (ProjectGraphReportError) for graph query failures. The main ProjectGraphReport struct aggregates all these components into a serializable report capturing hotspots, unresolved targets, bridge edge hypotheses across multiple source systems, degradation details, and investigation recommendations. BridgeEdgeInput provides factory methods to construct available or unavailable bridge edge variants, while ReportGraphSnapshot encapsulates the complete analyzed graph structure. Together, these types form the complete schema for representing code dependency graph analysis results.
[crates/gcode/src/graph/report/types.rs:10-17]
[crates/gcode/src/graph/report/types.rs:19-50]
[crates/gcode/src/graph/report/types.rs:20-34]
[crates/gcode/src/graph/report/types.rs:36-49]
[crates/gcode/src/graph/report/types.rs:53-68]

## API Symbols

- `BridgeEdgeHypothesis` (class) component `BridgeEdgeHypothesis [class]` (`d918517e-c334-52ce-900a-9e965389ae4a`) lines 10-17 [crates/gcode/src/graph/report/types.rs:10-17]
  - Signature: `pub struct BridgeEdgeHypothesis {`
  - Purpose: `BridgeEdgeHypothesis` is a struct representing a hypothesis for a directed edge connecting a source entity to a target symbol with associated relation semantics and projection metadata. [crates/gcode/src/graph/report/types.rs:10-17]
- `BridgeEdgeHypothesis` (class) component `BridgeEdgeHypothesis [class]` (`781d1611-6a96-55ec-b47f-21f956a2cc83`) lines 19-50 [crates/gcode/src/graph/report/types.rs:19-50]
  - Signature: `impl BridgeEdgeHypothesis {`
  - Purpose: BridgeEdgeHypothesis implements factory methods to instantiate immutable relational hypotheses between source and target symbols with configurable or inference-derived projection metadata. [crates/gcode/src/graph/report/types.rs:19-50]
- `BridgeEdgeHypothesis.new` (method) component `BridgeEdgeHypothesis.new [method]` (`ba33ce95-5ef9-5073-bef7-41d158deca59`) lines 20-34 [crates/gcode/src/graph/report/types.rs:20-34]
  - Signature: `pub fn new(`
  - Purpose: Constructs a read-only projection labeled as an "inferred hypothesis" that relates a source symbol to a target symbol with provided metadata. [crates/gcode/src/graph/report/types.rs:20-34]
- `BridgeEdgeHypothesis.inferred` (method) component `BridgeEdgeHypothesis.inferred [method]` (`7b00de4f-4e37-5d8e-9207-47497357abe1`) lines 36-49 [crates/gcode/src/graph/report/types.rs:36-49]
  - Signature: `pub fn inferred(`
  - Purpose: Creates a new instance with inferred ProjectionMetadata parameterized by the given source system and optional confidence value. [crates/gcode/src/graph/report/types.rs:36-49]
- `ProjectGraphReport` (class) component `ProjectGraphReport [class]` (`736b2c55-42ec-57f9-b92f-9b76c89a641a`) lines 53-68 [crates/gcode/src/graph/report/types.rs:53-68]
  - Signature: `pub struct ProjectGraphReport {`
  - Purpose: # Summary

ProjectGraphReport is a serializable struct aggregating comprehensive dependency graph analysis metrics including performance hotspots, target resolution frequencies, bridge connectivity data, build degradations, and investigation recommendations. [crates/gcode/src/graph/report/types.rs:53-68]
- `ProjectGraphReportOptions` (class) component `ProjectGraphReportOptions [class]` (`01af899d-41da-5467-a90c-00bb23c09a05`) lines 71-73 [crates/gcode/src/graph/report/types.rs:71-73]
  - Signature: `pub struct ProjectGraphReportOptions {`
  - Purpose: `ProjectGraphReportOptions` is a configuration struct that encapsulates a single `usize` parameter (`top_n`) to specify the number of top results to include in a project graph report. [crates/gcode/src/graph/report/types.rs:71-73]
- `ProjectGraphReportOptions` (class) component `ProjectGraphReportOptions [class]` (`9ef147d0-2cc4-5408-91eb-3439ac024527`) lines 75-81 [crates/gcode/src/graph/report/types.rs:75-81]
  - Signature: `impl Default for ProjectGraphReportOptions {`
  - Purpose: The `Default` trait implementation for `ProjectGraphReportOptions` instantiates the struct with `top_n` field set to `DEFAULT_TOP_LIMIT`. [crates/gcode/src/graph/report/types.rs:75-81]
- `ProjectGraphReportOptions.default` (method) component `ProjectGraphReportOptions.default [method]` (`e40d2796-48c9-58a3-a236-b0b21433ba9c`) lines 76-80 [crates/gcode/src/graph/report/types.rs:76-80]
  - Signature: `fn default() -> Self {`
  - Purpose: Implements the `Default` trait by constructing a new instance with the `top_n` field initialized to `DEFAULT_TOP_LIMIT`. [crates/gcode/src/graph/report/types.rs:76-80]
- `ProjectGraphReportOptions` (class) component `ProjectGraphReportOptions [class]` (`92e4d371-7d9f-5ddd-b209-4c018bb444d1`) lines 83-89 [crates/gcode/src/graph/report/types.rs:83-89]
  - Signature: `impl ProjectGraphReportOptions {`
  - Purpose: `ProjectGraphReportOptions::normalized` ensures the `top_n` field has a minimum value of 1 by returning a normalized instance with `max(1)` applied. [crates/gcode/src/graph/report/types.rs:83-89]
- `ProjectGraphReportOptions.normalized` (method) component `ProjectGraphReportOptions.normalized [method]` (`78d1b3e4-93d3-5791-bf3f-86126114eab1`) lines 84-88 [crates/gcode/src/graph/report/types.rs:84-88]
  - Signature: `pub(super) fn normalized(self) -> Self {`
  - Purpose: This method returns a new `Self` instance with the `top_n` field set to its maximum between the current value and 1, ensuring a minimum threshold of 1. [crates/gcode/src/graph/report/types.rs:84-88]
- `GraphReportSummary` (class) component `GraphReportSummary [class]` (`aab5e21d-fb38-5b57-a1be-b52e369980e4`) lines 92-97 [crates/gcode/src/graph/report/types.rs:92-97]
  - Signature: `pub struct GraphReportSummary {`
  - Purpose: `GraphReportSummary` is a struct that aggregates graph topology statistics comprising total node and edge counts along with type-stratified distributions stored in BTreeMaps. [crates/gcode/src/graph/report/types.rs:92-97]
- `GraphReportHotspots` (class) component `GraphReportHotspots [class]` (`8cf33a5b-e916-5815-b5a5-417f5b145ba3`) lines 100-105 [crates/gcode/src/graph/report/types.rs:100-105]
  - Signature: `pub struct GraphReportHotspots {`
  - Purpose: GraphReportHotspots aggregates four categories of graph hotspots: high-degree files, symbols, and modules, plus incoming call hotspots, each represented as a vector of GraphHotspot items. [crates/gcode/src/graph/report/types.rs:100-105]
- `GraphHotspot` (class) component `GraphHotspot [class]` (`fd3fd065-2c4a-5417-a7d2-2a034a958a1a`) lines 108-118 [crates/gcode/src/graph/report/types.rs:108-118]
  - Signature: `pub struct GraphHotspot {`
  - Purpose: GraphHotspot is a serializable struct representing a graph node with topology metrics (degree, incoming/outgoing edge counts) and optional file path metadata. [crates/gcode/src/graph/report/types.rs:108-118]
- `TargetFrequency` (class) component `TargetFrequency [class]` (`73aa6fbb-8662-50bb-9035-ba2c9e89dc22`) lines 121-125 [crates/gcode/src/graph/report/types.rs:121-125]
  - Signature: `pub struct TargetFrequency {`
  - Purpose: `TargetFrequency` is a struct that associates a unique identifier and descriptive name with an occurrence count metric for tracking frequency data. [crates/gcode/src/graph/report/types.rs:121-125]
- `BridgeReportSummary` (class) component `BridgeReportSummary [class]` (`018ad04b-3a6c-5dfe-b4ec-a43b0694c285`) lines 128-136 [crates/gcode/src/graph/report/types.rs:128-136]
  - Signature: `pub struct BridgeReportSummary {`
  - Purpose: BridgeReportSummary aggregates metadata for a bridged relation, comprising edge count, per-source-system cardinality counts, derivation and mutability flags, and optional confidence range bounds. [crates/gcode/src/graph/report/types.rs:128-136]
- `NamedCount` (class) component `NamedCount [class]` (`312eac88-28c0-5584-8e8d-d96efcd071d5`) lines 139-142 [crates/gcode/src/graph/report/types.rs:139-142]
  - Signature: `pub struct NamedCount {`
  - Purpose: NamedCount is a public struct that pairs a `String` name field with a `usize` count field, providing a simple container for named numeric quantities. [crates/gcode/src/graph/report/types.rs:139-142]
- `ConfidenceRange` (class) component `ConfidenceRange [class]` (`8015de67-583e-51b7-b2f7-d757d1da8b08`) lines 145-148 [crates/gcode/src/graph/report/types.rs:145-148]
  - Signature: `pub struct ConfidenceRange {`
  - Purpose: `ConfidenceRange` is a public struct that represents a numeric interval bounded by `f64` minimum and maximum values. [crates/gcode/src/graph/report/types.rs:145-148]
- `ReportDegradation` (class) component `ReportDegradation [class]` (`ea809185-b36b-513b-86a9-59c58b3c46a8`) lines 151-155 [crates/gcode/src/graph/report/types.rs:151-155]
  - Signature: `pub struct ReportDegradation {`
  - Purpose: ReportDegradation is a struct that represents a degradation report containing an input identifier, a boolean requirement flag, and associated detail information. [crates/gcode/src/graph/report/types.rs:151-155]
- `ProjectGraphReportError` (type) component `ProjectGraphReportError [type]` (`2165f448-b64d-5cdb-b9c4-9c5b242c5608`) lines 158-162 [crates/gcode/src/graph/report/types.rs:158-162]
  - Signature: `pub enum ProjectGraphReportError {`
  - Purpose: Indexed type `ProjectGraphReportError` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:158-162]
- `ProjectGraphReportError` (class) component `ProjectGraphReportError [class]` (`c33027c5-1a67-5410-9571-8e1c3586ccb9`) lines 164-179 [crates/gcode/src/graph/report/types.rs:164-179]
  - Signature: `impl fmt::Display for ProjectGraphReportError {`
  - Purpose: This implementation of the `Display` trait for `ProjectGraphReportError` formats three error variants—FalkorDB misconfiguration, unreachability, and query failure—into human-readable error messages. [crates/gcode/src/graph/report/types.rs:164-179]
- `ProjectGraphReportError.fmt` (method) component `ProjectGraphReportError.fmt [method]` (`3c51fdb9-a59d-589d-99a4-45fd856a1115`) lines 165-178 [crates/gcode/src/graph/report/types.rs:165-178]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Implements the `fmt` trait to format error variants of a FalkorDB service error enum into human-readable error messages via pattern matching. [crates/gcode/src/graph/report/types.rs:165-178]
- `ProjectGraphReportError` (class) component `ProjectGraphReportError [class]` (`4ef1b370-953e-5b61-8408-c2f00c3274c1`) lines 181-181 [crates/gcode/src/graph/report/types.rs:181]
  - Signature: `impl std::error::Error for ProjectGraphReportError {}`
  - Purpose: This trait implementation makes `ProjectGraphReportError` conform to Rust's `std::error::Error` trait, enabling it to be used in standard error handling and exception propagation contexts. [crates/gcode/src/graph/report/types.rs:181]
- `ReportGraphSnapshot` (class) component `ReportGraphSnapshot [class]` (`4fd60dcc-aa30-58ce-a308-e9a3ad15df41`) lines 184-192 [crates/gcode/src/graph/report/types.rs:184-192]
  - Signature: `pub(super) struct ReportGraphSnapshot {`
  - Purpose: `ReportGraphSnapshot` is a struct that encapsulates a code report graph consisting of report nodes, code and bridge edges, with optional metadata for summaries, hotspots, and resolved/unresolved/external target frequencies. [crates/gcode/src/graph/report/types.rs:184-192]
- `ReportNode` (class) component `ReportNode [class]` (`c8ca1e44-4439-55e7-a0b1-1ac18baff53a`) lines 195-200 [crates/gcode/src/graph/report/types.rs:195-200]
  - Signature: `pub(super) struct ReportNode {`
  - Purpose: `ReportNode` is a struct representing a typed node in a report system with an identifier, name, type classifier, and optional file path reference. [crates/gcode/src/graph/report/types.rs:195-200]
- `ReportNode` (class) component `ReportNode [class]` (`98518fa6-8901-572b-a995-90690c331cd6`) lines 202-222 [crates/gcode/src/graph/report/types.rs:202-222]
  - Signature: `impl ReportNode {`
  - Purpose: Test-only implementation providing a constructor and builder-pattern method for ReportNode instances, accepting id, name, and node_type via `impl Into<String>` generics with optional file_path initialization. [crates/gcode/src/graph/report/types.rs:202-222]
- `ReportNode.new` (method) component `ReportNode.new [method]` (`26313d90-b424-514e-a96b-db75bb1a36f5`) lines 204-215 [crates/gcode/src/graph/report/types.rs:204-215]
  - Signature: `pub(super) fn new(`
  - Purpose: Constructs a new instance by consuming three generic `Into<String>` parameters for id, name, and node_type, while initializing file_path to None. [crates/gcode/src/graph/report/types.rs:204-215]
- `ReportNode.with_file_path` (method) component `ReportNode.with_file_path [method]` (`365ff31d-340c-5b2a-8403-48f494001740`) lines 218-221 [crates/gcode/src/graph/report/types.rs:218-221]
  - Signature: `pub(super) fn with_file_path(mut self, file_path: impl Into<String>) -> Self {`
  - Purpose: Sets the `file_path` field to `Some(String)` converted from the input parameter and returns `self` to enable builder-pattern method chaining. [crates/gcode/src/graph/report/types.rs:218-221]
- `ReportCodeEdge` (class) component `ReportCodeEdge [class]` (`954751e9-880d-5494-8292-71db5ebe736d`) lines 225-229 [crates/gcode/src/graph/report/types.rs:225-229]
  - Signature: `pub(super) struct ReportCodeEdge {`
  - Purpose: ReportCodeEdge is a struct representing a typed directed edge in a code analysis graph, connecting string-identified source and target nodes with a classification edge type. [crates/gcode/src/graph/report/types.rs:225-229]
- `ReportCodeEdge` (class) component `ReportCodeEdge [class]` (`3edd1623-35dd-501c-b202-87c245a93e65`) lines 231-244 [crates/gcode/src/graph/report/types.rs:231-244]
  - Signature: `impl ReportCodeEdge {`
  - Purpose: A test-scoped constructor for `ReportCodeEdge` that accepts three generic string-convertible parameters and converts them into `String` fields for `source`, `target`, and `edge_type`. [crates/gcode/src/graph/report/types.rs:231-244]
- `ReportCodeEdge.new` (method) component `ReportCodeEdge.new [method]` (`c9b69d5d-178d-5767-89c0-ff7b2e809152`) lines 233-243 [crates/gcode/src/graph/report/types.rs:233-243]
  - Signature: `pub(super) fn new(`
  - Purpose: Constructs a new instance by accepting three generic parameters implementing `Into<String>` and converting them into owned String fields for `source`, `target`, and `edge_type`. [crates/gcode/src/graph/report/types.rs:233-243]
- `BridgeEdgeInput` (type) component `BridgeEdgeInput [type]` (`2cdc924e-0a75-53cf-bf45-d26fda8442b1`) lines 247-251 [crates/gcode/src/graph/report/types.rs:247-251]
  - Signature: `pub(super) enum BridgeEdgeInput {`
  - Purpose: Indexed type `BridgeEdgeInput` in `crates/gcode/src/graph/report/types.rs`. [crates/gcode/src/graph/report/types.rs:247-251]
- `BridgeEdgeInput` (class) component `BridgeEdgeInput [class]` (`9acfe065-45d3-5dac-ac6a-ec471c9a21ce`) lines 253-262 [crates/gcode/src/graph/report/types.rs:253-262]
  - Signature: `impl BridgeEdgeInput {`
  - Purpose: `BridgeEdgeInput` implements factory methods to construct its `Available` variant from a vector of `BridgeEdgeHypothesis` and its `Unavailable` variant from a string reason. [crates/gcode/src/graph/report/types.rs:253-262]
- `BridgeEdgeInput.available` (method) component `BridgeEdgeInput.available [method]` (`01b34a2c-95ec-505d-be24-f39290d33ee1`) lines 254-256 [crates/gcode/src/graph/report/types.rs:254-256]
  - Signature: `pub(super) fn available(edges: Vec<BridgeEdgeHypothesis>) -> Self {`
  - Purpose: This method constructs and returns the `Available` enum variant, wrapping the provided vector of `BridgeEdgeHypothesis` objects. [crates/gcode/src/graph/report/types.rs:254-256]
- `BridgeEdgeInput.unavailable` (method) component `BridgeEdgeInput.unavailable [method]` (`b05657c3-0f2b-58bf-a139-a8ee8d26e1ba`) lines 259-261 [crates/gcode/src/graph/report/types.rs:259-261]
  - Signature: `pub(super) fn unavailable(reason: impl Into<String>) -> Self {`
  - Purpose: Creates a `Self::Unavailable` variant by converting the provided reason parameter into a `String`. [crates/gcode/src/graph/report/types.rs:259-261]
- `BridgeEdgeInput` (class) component `BridgeEdgeInput [class]` (`11a1ba3c-7466-5ded-9d67-b0f0b2b3fe2d`) lines 264-268 [crates/gcode/src/graph/report/types.rs:264-268]
  - Signature: `impl Default for BridgeEdgeInput {`
  - Purpose: BridgeEdgeInput's Default trait implementation returns the Available enum variant initialized with an empty vector. [crates/gcode/src/graph/report/types.rs:264-268]
- `BridgeEdgeInput.default` (method) component `BridgeEdgeInput.default [method]` (`2ca3a8c2-d7a4-5e3d-beda-41b6d4763941`) lines 265-267 [crates/gcode/src/graph/report/types.rs:265-267]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns the `Available` enum variant initialized with an empty vector as the default instance. [crates/gcode/src/graph/report/types.rs:265-267]

