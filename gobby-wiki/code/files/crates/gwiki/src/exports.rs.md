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

`crates/gwiki/src/exports.rs` exposes 22 indexed API symbols.

## How it fits

`crates/gwiki/src/exports.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ExportKind` | type | Indexed type `ExportKind` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:9-13] |
| `ExportRequest` | class | 'ExportRequest' is a data transfer struct that represents an export operation with a target 'filename', an 'ExportKind' discriminator, and the exported 'contents' as a string. [crates/gwiki/src/exports.rs:16-20] |
| `ExportArtifact` | class | 'ExportArtifact' is a struct that records an exported file’s destination 'path', its 'kind' ('ExportKind'), and the number of 'bytes_written' during the export. [crates/gwiki/src/exports.rs:23-27] |
| `ExportCommand` | type | Indexed type `ExportCommand` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:30-38] |
| `ExportOutput` | class | 'ExportOutput' is a Rust struct that represents the result of an export operation, containing the static command name, the associated 'ScopeIdentity', and a list of 'ExportArtifact' values. [crates/gwiki/src/exports.rs:41-45] |
| `ExportOutput::new` | method | Constructs a new instance with 'command' set to '"export"' and initializes it from the provided 'scope' and 'artifacts' vectors. [crates/gwiki/src/exports.rs:48-54] |
| `WorkflowAsset` | class | 'WorkflowAsset' is a 'pub' struct that statically describes an embedded workflow resource by storing its 'name', 'filename', and 'contents' as ''static' string slices. [crates/gwiki/src/exports.rs:58-62] |
| `bundled_workflow_assets` | function | Returns the static 'WORKFLOW_ASSETS' slice as a '&'static [WorkflowAsset]'. [crates/gwiki/src/exports.rs:82-84] |
| `run` | function | Dispatches the given 'ExportCommand' to either 'export_workflow_assets' or 'export_report_file' using 'root', then wraps the single returned 'ExportArtifact' in a one-element 'Vec' and propagates any 'WikiError'. [crates/gwiki/src/exports.rs:86-96] |
| `export_workflow_assets` | function | Creates a bundle export artifact by converting the provided filename into an 'ExportRequest' with 'ExportKind::Bundle' and 'workflow_assets_bundle()' contents, then delegating to 'write_export' and returning its 'Result<ExportArtifact, WikiError>'. [crates/gwiki/src/exports.rs:98-110] |
| `export_report_file` | function | Reads the report text from 'source_path' into a string and then delegates to 'write_export' to create a 'Report' export artifact under 'root' with the given 'filename', mapping any file-read failure into a 'WikiError::Io' annotated as '"read export report"'. [crates/gwiki/src/exports.rs:112-131] |
| `export_graph_artifacts` | function | Exports graph data from 'facts' into a pretty-printed 'graph.json' and a generated 'GRAPH_REPORT.md' under 'root', returning both written artifacts, and if report writing fails it removes the JSON file before propagating the error. [crates/gwiki/src/exports.rs:133-168] |
| `graph_export_error` | function | Converts a 'GraphAnalyticsError' into a 'WikiError::InvalidInput' with 'field' set to '"graph"' and 'message' populated from the error's string representation. [crates/gwiki/src/exports.rs:170-175] |
| `export_markdown_report` | function | Creates a report export artifact by wrapping the given filename and markdown contents in an 'ExportRequest' of kind 'Report' and delegating to 'write_export' for the specified root path. [crates/gwiki/src/exports.rs:177-190] |
| `write_export` | function | Creates the export file under 'root/outputs/<validated relative filename>', ensures its parent directories exist, writes 'request.contents' to disk, and returns an 'ExportArtifact' containing the path, requested kind, and byte count, mapping any I/O failure to 'WikiError::Io'. [crates/gwiki/src/exports.rs:192-214] |
| `export_relative_path` | function | Validates that 'filename' is a non-empty, non-absolute, strictly relative path containing only normal components or '.' segments, rejects any '..', root, or prefix components, and returns the normalized 'PathBuf' or a 'WikiError' for invalid input. [crates/gwiki/src/exports.rs:216-238] |
| `invalid_export_filename` | function | Constructs a 'WikiError::InvalidInput' for the 'filename' field with a message stating that the export filename must remain under 'outputs/', including the provided filename. [crates/gwiki/src/exports.rs:240-245] |
| `workflow_assets_bundle` | function | Builds and returns a single markdown string titled '# GWiki Workflow Assets' by iterating over 'bundled_workflow_assets()' and appending each asset’s name, source filename, and trimmed contents as a section. [crates/gwiki/src/exports.rs:247-260] |

_Verified by 4 in-file unit tests._

