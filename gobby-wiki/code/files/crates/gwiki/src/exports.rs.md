---
title: crates/gwiki/src/exports.rs
type: code_file
provenance:
- file: crates/gwiki/src/exports.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/exports.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/exports.rs` exposes 39 indexed API symbols.

## How it fits

`crates/gwiki/src/exports.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ExportKind` | type | Indexed type `ExportKind` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:11-15] |
| `ExportRequest` | class | **ExportRequest is a public struct that encapsulates the parameters required for an export operation: a target filename, an export kind specifier, and the content to be exported.** [crates/gwiki/src/exports.rs:18-22] |
| `ExportArtifact` | class | 'ExportArtifact' is a struct that encapsulates metadata about a completed export operation, containing the destination file path, the export kind classification, and the number of bytes written. [crates/gwiki/src/exports.rs:25-29] |
| `ExportCommand` | type | Indexed type `ExportCommand` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:32-40] |
| `ExportOutput` | class | ExportOutput encapsulates the results of an export operation, comprising a static command identifier, a ScopeIdentity, and a vector of ExportArtifacts. [crates/gwiki/src/exports.rs:43-47] |
| `ExportOutput::new` | method | Constructs and returns a new Self instance with the command field hardcoded to "export" and the provided scope and artifacts parameters assigned to their respective fields. [crates/gwiki/src/exports.rs:50-56] |
| `WorkflowAsset` | class | WorkflowAsset is a struct with three public fields of static string references ('&'static str') representing an asset's name, filename, and contents. [crates/gwiki/src/exports.rs:60-64] |
| `bundled_workflow_assets` | function | Returns a static reference to a constant slice of 'WorkflowAsset' items bundled with the application. [crates/gwiki/src/exports.rs:84-86] |
| `run` | function | This function dispatches an 'ExportCommand' enum to the corresponding export handler (either 'export_workflow_assets' or 'export_report_file') and returns the resulting 'ExportArtifact' wrapped in a vector, or a 'WikiError' on failure. [crates/gwiki/src/exports.rs:88-98] |
| `export_workflow_assets` | function | Exports workflow assets as a bundle file to the specified root path and filename, returning an 'ExportArtifact' on success or a 'WikiError' on failure. [crates/gwiki/src/exports.rs:100-112] |
| `export_report_file` | function | Reads a report file from the specified source path and exports it with the given filename as an ExportArtifact, returning a WikiError on I/O failure. [crates/gwiki/src/exports.rs:114-133] |
| `export_graph_artifacts` | function | Exports a 'WikiGraphFacts' instance by serializing it to JSON and rendering a Markdown report, writing both artifacts to the specified root directory and returning their paths or a 'WikiError'. [crates/gwiki/src/exports.rs:135-170] |
| `graph_export_error` | function | Converts a 'GraphAnalyticsError' into a 'WikiError::InvalidInput' variant with the field "graph" and the error message stringified. [crates/gwiki/src/exports.rs:172-177] |
| `export_agent_artifacts` | function | Exports a WikiGraph by rendering it to JSON-LD and two LLM-compatible text formats (index and full), persisting each as an artifact file, and returning a vector of the resulting ExportArtifacts. [crates/gwiki/src/exports.rs:184-218] |
| `write_agent_artifact` | function | Writes an export artifact to disk and appends it to a tracking vector on success, or rolls back all previously written artifacts by deleting them if the write operation fails. [crates/gwiki/src/exports.rs:222-248] |
| `render_graph_jsonld` | function | # Summary 'render_graph_jsonld' converts a GraphExport into a JSON-LD formatted string by constructing JSON entities from nodes and aggregating citation, audit, and trust relationship edges into entity properties. [crates/gwiki/src/exports.rs:255-329] |
| `id_references` | function | Converts a slice of string identifiers into a 'serde_json::Value' array where each string is wrapped in a JSON object with an '@id' field. [crates/gwiki/src/exports.rs:331-337] |
| `jsonld_type` | function | This function maps content kind identifiers to JSON-LD type strings using pattern matching, returning specialized semantic types ('Article', 'SoftwareSourceCode', 'CreativeWork') for specific kinds with 'DigitalDocument' as the default fallback. [crates/gwiki/src/exports.rs:340-347] |
| `render_llms_index` | function | Generates a markdown-formatted index string containing document and source node link sections with their respective counts extracted from a GraphExport structure. [crates/gwiki/src/exports.rs:352-373] |
| `render_llms_full` | function | # Summary 'render_llms_full' generates a markdown-formatted string aggregating all documents from a 'GraphExport' with their paths and file contents retrieved from the filesystem rooted at the provided path. [crates/gwiki/src/exports.rs:379-403] |
| `document_nodes` | function | Filters a GraphExport's nodes collection and returns references to those nodes whose kind passes the 'is_document_node' predicate. [crates/gwiki/src/exports.rs:407-413] |
| `is_document_node` | function | Returns 'true' if the input string matches one of three document node kinds: "wiki_page", "code", or "document"; otherwise returns 'false'. [crates/gwiki/src/exports.rs:415-417] |
| `push_link_section` | function | Appends a markdown-formatted section with a heading and bulleted list of links (from the provided nodes' labels and paths) to an output string, or a placeholder if the node list is empty. [crates/gwiki/src/exports.rs:419-428] |
| `node_label` | function | This function returns the cloned title of the node, or falls back to returning the cloned path if the title is 'None'. [crates/gwiki/src/exports.rs:430-432] |

_8 more symbol(s) not shown — run `gcode outline crates/gwiki/src/exports.rs` for the full list._

_Verified by 7 in-file unit tests._

