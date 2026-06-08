---
title: crates/gcode/src/commands/codewiki/mod.rs
type: code_file
source_files:
- file: crates/gcode/src/commands/codewiki/mod.rs
  ranges:
  - 68-73
  - 76-80
  - 82-104
  - 83-92
  - 94-103
  - 107-110
  - 113-116
  - 118-139
  - 119-124
  - 126-131
  - 133-138
  - 142-146
  - 149-156
  - 159-165
  - 168-178
  - 181-185
  - 188-192
  - 195-199
  - 202-214
  - 217-220
  - 223-225
  - '227'
  - 229-249
  - 230-236
  - 238-244
  - 246-248
  - 251-326
  - 328-333
  - 335-340
  - 342-405
---

# crates/gcode/src/commands/codewiki/mod.rs

Module: [[modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/mod.rs` exposes 30 indexed API symbols. [crates/gcode/src/commands/codewiki/mod.rs:68-73] [crates/gcode/src/commands/codewiki/mod.rs:76-80] [crates/gcode/src/commands/codewiki/mod.rs:82-104] [crates/gcode/src/commands/codewiki/mod.rs:83-92] [crates/gcode/src/commands/codewiki/mod.rs:94-103] [crates/gcode/src/commands/codewiki/mod.rs:107-110] [crates/gcode/src/commands/codewiki/mod.rs:113-116] [crates/gcode/src/commands/codewiki/mod.rs:118-139] [crates/gcode/src/commands/codewiki/mod.rs:119-124] [crates/gcode/src/commands/codewiki/mod.rs:126-131] [crates/gcode/src/commands/codewiki/mod.rs:133-138] [crates/gcode/src/commands/codewiki/mod.rs:142-146] [crates/gcode/src/commands/codewiki/mod.rs:149-156] [crates/gcode/src/commands/codewiki/mod.rs:159-165] [crates/gcode/src/commands/codewiki/mod.rs:168-178] [crates/gcode/src/commands/codewiki/mod.rs:181-185] [crates/gcode/src/commands/codewiki/mod.rs:188-192] [crates/gcode/src/commands/codewiki/mod.rs:195-199] [crates/gcode/src/commands/codewiki/mod.rs:202-214] [crates/gcode/src/commands/codewiki/mod.rs:217-220] [crates/gcode/src/commands/codewiki/mod.rs:223-225] [crates/gcode/src/commands/codewiki/mod.rs:227] [crates/gcode/src/commands/codewiki/mod.rs:229-249] [crates/gcode/src/commands/codewiki/mod.rs:230-236] [crates/gcode/src/commands/codewiki/mod.rs:238-244] [crates/gcode/src/commands/codewiki/mod.rs:246-248] [crates/gcode/src/commands/codewiki/mod.rs:251-326] [crates/gcode/src/commands/codewiki/mod.rs:328-333] [crates/gcode/src/commands/codewiki/mod.rs:335-340] [crates/gcode/src/commands/codewiki/mod.rs:342-405]

## API Symbols

- `CodewikiInput` (class) component `CodewikiInput [class]` (`d9ec81fe-c548-52af-9f98-31569a197ebe`) lines 68-73 [crates/gcode/src/commands/codewiki/mod.rs:68-73]
  - Signature: `pub struct CodewikiInput {`
  - Purpose: `CodewikiInput` is a struct that aggregates source files, code dependency graph edges, graph availability metadata, and extracted symbols for code wiki analysis and linking. [crates/gcode/src/commands/codewiki/mod.rs:68-73]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`8b76191f-df2c-5844-a712-ef2060e4d9fe`) lines 76-80 [crates/gcode/src/commands/codewiki/mod.rs:76-80]
  - Signature: `pub struct CodewikiGraphEdge {`
  - Purpose: `CodewikiGraphEdge` is a struct representing a directed edge in a component graph that connects a source component to a target component and classifies the relationship between them. [crates/gcode/src/commands/codewiki/mod.rs:76-80]
- `CodewikiGraphEdge` (class) component `CodewikiGraphEdge [class]` (`42319b9f-6f4f-5ae7-acf8-2cf147c417e3`) lines 82-104 [crates/gcode/src/commands/codewiki/mod.rs:82-104]
  - Signature: `impl CodewikiGraphEdge {`
  - Purpose: `CodewikiGraphEdge` provides factory methods to construct directed edges in a component dependency graph, parameterized by semantic relationship kind (Call or Import). [crates/gcode/src/commands/codewiki/mod.rs:82-104]
- `CodewikiGraphEdge.call` (method) component `CodewikiGraphEdge.call [method]` (`97d003b6-289f-5507-bf60-668e65bd9257`) lines 83-92 [crates/gcode/src/commands/codewiki/mod.rs:83-92]
  - Signature: `pub fn call(`
  - Purpose: Constructs a `CodewikiGraphEdge` representing a call relationship between two components by converting the provided component identifiers into `String` and setting the edge kind to `Call`. [crates/gcode/src/commands/codewiki/mod.rs:83-92]
- `CodewikiGraphEdge.import` (method) component `CodewikiGraphEdge.import [method]` (`7f998307-84b2-59b3-a3bb-5b3982abbe2d`) lines 94-103 [crates/gcode/src/commands/codewiki/mod.rs:94-103]
  - Signature: `pub fn import(`
  - Purpose: Constructs an import-kind graph edge instance between two components by converting their generic identifiers to owned Strings via the `Into` trait. [crates/gcode/src/commands/codewiki/mod.rs:94-103]
- `CodewikiGraphEdgeKind` (type) component `CodewikiGraphEdgeKind [type]` (`b5b4614f-5c5b-5219-9c49-c45fe0c495c5`) lines 107-110 [crates/gcode/src/commands/codewiki/mod.rs:107-110]
  - Signature: `pub enum CodewikiGraphEdgeKind {`
  - Purpose: Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:107-110]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`e816a8dc-a330-5953-b9bd-5ed3cbd9ce2e`) lines 113-116 [crates/gcode/src/commands/codewiki/mod.rs:113-116]
  - Signature: `pub(crate) struct CodewikiGraph {`
  - Purpose: # Summary

`CodewikiGraph` is a crate-private struct that encapsulates a graph representation comprising a vector of edges and an associated availability state. [crates/gcode/src/commands/codewiki/mod.rs:113-116]
- `CodewikiGraph` (class) component `CodewikiGraph [class]` (`d2119301-352e-56cf-88c2-fe0cc1cb513c`) lines 118-139 [crates/gcode/src/commands/codewiki/mod.rs:118-139]
  - Signature: `impl CodewikiGraph {`
  - Purpose: `CodewikiGraph` provides three factory methods that construct instances with different availability states—`Available` and `Truncated` (with edges) or `Unavailable` (empty)—for representing graph data at varying levels of completeness. [crates/gcode/src/commands/codewiki/mod.rs:118-139]
- `CodewikiGraph.available` (method) component `CodewikiGraph.available [method]` (`203c956f-df24-5bc7-a6a3-ea5706da0789`) lines 119-124 [crates/gcode/src/commands/codewiki/mod.rs:119-124]
  - Signature: `fn available(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: Constructs a new instance of `Self` with the provided edges and sets the availability status to `CodewikiGraphAvailability::Available`. [crates/gcode/src/commands/codewiki/mod.rs:119-124]
- `CodewikiGraph.truncated` (method) component `CodewikiGraph.truncated [method]` (`61199642-4458-5941-8bee-4c8b05f95006`) lines 126-131 [crates/gcode/src/commands/codewiki/mod.rs:126-131]
  - Signature: `fn truncated(edges: Vec<CodewikiGraphEdge>) -> Self {`
  - Purpose: A constructor that creates an instance with the provided edges vector and sets its availability status to `CodewikiGraphAvailability::Truncated`. [crates/gcode/src/commands/codewiki/mod.rs:126-131]
- `CodewikiGraph.unavailable` (method) component `CodewikiGraph.unavailable [method]` (`35fced91-d1e3-5c40-bd4c-3b0169500367`) lines 133-138 [crates/gcode/src/commands/codewiki/mod.rs:133-138]
  - Signature: `fn unavailable() -> Self {`
  - Purpose: This method constructs and returns a new instance with an empty edges vector and `CodewikiGraphAvailability::Unavailable` status. [crates/gcode/src/commands/codewiki/mod.rs:133-138]
- `CodewikiGraphAvailability` (type) component `CodewikiGraphAvailability [type]` (`6efab90a-01e1-599f-a0bd-e39aba8d579a`) lines 142-146 [crates/gcode/src/commands/codewiki/mod.rs:142-146]
  - Signature: `pub enum CodewikiGraphAvailability {`
  - Purpose: Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:142-146]
- `FileDoc` (class) component `FileDoc [class]` (`22973f10-0e6d-5440-80a0-67368aa59c9c`) lines 149-156 [crates/gcode/src/commands/codewiki/mod.rs:149-156]
  - Signature: `pub(crate) struct FileDoc {`
  - Purpose: FileDoc is a crate-scoped struct that aggregates documentation metadata for a source file, including its path, module name, summary, source code spans, documented symbols, and associated component identifiers. [crates/gcode/src/commands/codewiki/mod.rs:149-156]
- `SymbolDoc` (class) component `SymbolDoc [class]` (`bffaf481-7c7f-5f79-a7d8-ef6c6e609ce7`) lines 159-165 [crates/gcode/src/commands/codewiki/mod.rs:159-165]
  - Signature: `pub(crate) struct SymbolDoc {`
  - Purpose: `SymbolDoc` is a crate-internal struct that encapsulates documentation metadata for a symbol, including its purpose, component identifiers, and source code span. [crates/gcode/src/commands/codewiki/mod.rs:159-165]
- `ModuleDoc` (class) component `ModuleDoc [class]` (`87c240ee-0083-53db-b9a9-8fd1d2a769e0`) lines 168-178 [crates/gcode/src/commands/codewiki/mod.rs:168-178]
  - Signature: `pub(crate) struct ModuleDoc {`
  - Purpose: `ModuleDoc` is a crate-private struct that aggregates module documentation metadata including source spans, file references, child module links, component identifiers, and optional dependency and call diagrams with their availability status. [crates/gcode/src/commands/codewiki/mod.rs:168-178]
- `FileLink` (class) component `FileLink [class]` (`f08b1658-cd6c-57ed-ae73-c42eb70ce7b1`) lines 181-185 [crates/gcode/src/commands/codewiki/mod.rs:181-185]
  - Signature: `pub(crate) struct FileLink {`
  - Purpose: `FileLink` is a crate-internal struct that encapsulates a file path, summary description, and collection of `SourceSpan` locations within that file. [crates/gcode/src/commands/codewiki/mod.rs:181-185]
- `ModuleLink` (class) component `ModuleLink [class]` (`0143d6e3-8c6f-5f21-b0fc-f62687ee343c`) lines 188-192 [crates/gcode/src/commands/codewiki/mod.rs:188-192]
  - Signature: `pub(crate) struct ModuleLink {`
  - Purpose: ModuleLink is a crate-scoped struct that associates a module name with a summary description and its corresponding source code spans. [crates/gcode/src/commands/codewiki/mod.rs:188-192]
- `SourceSpan` (class) component `SourceSpan [class]` (`62d80f23-3c1d-5237-8a1c-7857c6fdbda1`) lines 195-199 [crates/gcode/src/commands/codewiki/mod.rs:195-199]
  - Signature: `pub(crate) struct SourceSpan {`
  - Purpose: SourceSpan is a crate-private struct that represents a contiguous range of source code lines within a named file, tracking both the starting and ending line numbers. [crates/gcode/src/commands/codewiki/mod.rs:195-199]
- `CodewikiRunSummary` (class) component `CodewikiRunSummary [class]` (`31d944e0-eb80-51fa-b358-fb76203fc433`) lines 202-214 [crates/gcode/src/commands/codewiki/mod.rs:202-214]
  - Signature: `pub struct CodewikiRunSummary {`
  - Purpose: `CodewikiRunSummary` is a statistics struct that captures project metadata, output configuration, and aggregate counts of processed files, modules, symbols, and generated documentation pages from a code documentation generation run. [crates/gcode/src/commands/codewiki/mod.rs:202-214]
- `CodewikiMeta` (class) component `CodewikiMeta [class]` (`afa88b86-5479-5690-8bac-a7d87cd0e85a`) lines 217-220 [crates/gcode/src/commands/codewiki/mod.rs:217-220]
  - Signature: `pub(crate) struct CodewikiMeta {`
  - Purpose: `CodewikiMeta` is a crate-private struct that maintains a sorted map of documentation metadata entries and tracks a list of generated documentation identifiers. [crates/gcode/src/commands/codewiki/mod.rs:217-220]
- `CodewikiDocMeta` (class) component `CodewikiDocMeta [class]` (`bf2d1cd5-6b2a-5d6d-9bf8-80eff995286f`) lines 223-225 [crates/gcode/src/commands/codewiki/mod.rs:223-225]
  - Signature: `pub(crate) struct CodewikiDocMeta {`
  - Purpose: `CodewikiDocMeta` is a crate-scoped struct that encapsulates a BTreeMap associating string source identifiers with their corresponding hash values for documentation metadata tracking. [crates/gcode/src/commands/codewiki/mod.rs:223-225]
- `TextGenerator` (type) component `TextGenerator [type]` (`fea6446f-0db1-5789-965b-59af4598d03e`) lines 227-227 [crates/gcode/src/commands/codewiki/mod.rs:227]
  - Signature: `pub type TextGenerator<'a> = dyn FnMut(&str, &str) -> Option<String> + 'a;`
  - Purpose: Indexed type `TextGenerator` in `crates/gcode/src/commands/codewiki/mod.rs`. [crates/gcode/src/commands/codewiki/mod.rs:227]
- `SourceSpan` (class) component `SourceSpan [class]` (`d220490b-047b-54b8-a977-01cc8ce0383b`) lines 229-249 [crates/gcode/src/commands/codewiki/mod.rs:229-249]
  - Signature: `impl SourceSpan {`
  - Purpose: SourceSpan encapsulates a source file location range with methods to construct from symbols, format citations, and test containment relationships. [crates/gcode/src/commands/codewiki/mod.rs:229-249]
- `SourceSpan.from_symbol` (method) component `SourceSpan.from_symbol [method]` (`b654483d-9347-577a-a74b-114fcafeb5a9`) lines 230-236 [crates/gcode/src/commands/codewiki/mod.rs:230-236]
  - Signature: `fn from_symbol(symbol: &Symbol) -> Self {`
  - Purpose: Constructs an instance of `Self` from a `Symbol` reference by extracting its file path (cloned), line start, and line end fields. [crates/gcode/src/commands/codewiki/mod.rs:230-236]
- `SourceSpan.citation` (method) component `SourceSpan.citation [method]` (`bd9158b6-87ac-5e8a-81cf-46a47b473b9f`) lines 238-244 [crates/gcode/src/commands/codewiki/mod.rs:238-244]
  - Signature: `fn citation(&self) -> String {`
  - Purpose: Returns a formatted citation string containing the filename and either a single line number or a line range, depending on whether `line_start` equals `line_end`. [crates/gcode/src/commands/codewiki/mod.rs:238-244]
- `SourceSpan.contains` (method) component `SourceSpan.contains [method]` (`07fde728-d9be-50b8-b70c-984c519fc336`) lines 246-248 [crates/gcode/src/commands/codewiki/mod.rs:246-248]
  - Signature: `fn contains(&self, file: &str, line_start: usize, line_end: usize) -> bool {`
  - Purpose: Returns `true` if the specified file and line range `[line_start, line_end]` are fully contained within this object's file and line range. [crates/gcode/src/commands/codewiki/mod.rs:246-248]
- `run` (function) component `run [function]` (`1ca16b29-b339-5ccd-a6ba-46152db62538`) lines 251-326 [crates/gcode/src/commands/codewiki/mod.rs:251-326]
  - Signature: `pub fn run(`
  - Purpose: Generates hierarchical documentation for scoped source files and symbols by querying a read-only database, fetching code graph edges, optionally applying AI-assisted content generation, and writing incremental output to disk. [crates/gcode/src/commands/codewiki/mod.rs:251-326]
- `validate_edge_limit` (function) component `validate_edge_limit [function]` (`1b8b9271-89ec-5be2-bcae-92ec729cbe26`) lines 328-333 [crates/gcode/src/commands/codewiki/mod.rs:328-333]
  - Signature: `fn validate_edge_limit(edge_limit: usize) -> anyhow::Result<()> {`
  - Purpose: Validates that the `edge_limit` parameter falls within the inclusive range [1, MAX_EDGE_LIMIT], returning `Ok(())` if valid or an `anyhow::Error` with a descriptive message if out of bounds. [crates/gcode/src/commands/codewiki/mod.rs:328-333]
- `generate_hierarchical_docs` (function) component `generate_hierarchical_docs [function]` (`085ae06e-ac09-53a3-928a-c176a32c6022`) lines 335-340 [crates/gcode/src/commands/codewiki/mod.rs:335-340]
  - Signature: `pub fn generate_hierarchical_docs(`
  - Purpose: Generates hierarchical documentation as a vector of string tuples from CodewikiInput with optional TextGenerator support. [crates/gcode/src/commands/codewiki/mod.rs:335-340]
- `generate_hierarchical_docs_with_graph_availability` (function) component `generate_hierarchical_docs_with_graph_availability [function]` (`5ef76abe-66dd-59c3-ab1e-2d99e76502a8`) lines 342-405 [crates/gcode/src/commands/codewiki/mod.rs:342-405]
  - Signature: `fn generate_hierarchical_docs_with_graph_availability(`
  - Purpose: Generates a three-level documentation hierarchy (repository, modules, and files) by clustering core code files using dependency graph edges and building documentation artifacts with availability metadata. [crates/gcode/src/commands/codewiki/mod.rs:342-405]

