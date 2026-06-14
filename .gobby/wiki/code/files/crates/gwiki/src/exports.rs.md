---
title: crates/gwiki/src/exports.rs
type: code_file
provenance:
- file: crates/gwiki/src/exports.rs
  ranges:
  - 9-13
  - 16-20
  - 23-27
  - 30-38
  - 41-45
  - 47-55
  - 58-62
  - 82-84
  - 86-96
  - 98-110
  - 112-131
  - 133-168
  - 170-175
  - 177-190
  - 192-214
  - 216-238
  - 240-245
  - 247-260
  - 276-330
  - 333-448
  - 451-467
  - 470-486
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/exports.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the export model and execution path for gwiki. It introduces `ExportKind`, `ExportRequest`, `ExportArtifact`, `ExportCommand`, and `ExportOutput` to describe what is being exported, what gets written, and how results are reported. `WorkflowAsset` plus `bundled_workflow_assets()` provide the built-in workflow templates, while `run()` dispatches export commands to the specific exporters.

The exporters handle writing workflow assets, copying report files, and producing graph exports and markdown reports. Helper functions such as `write_export()`, `export_relative_path()`, `invalid_export_filename()`, and `workflow_assets_bundle()` enforce safe output paths and bundle layout, and the graph-specific helpers convert graph facts/options into report artifacts or structured errors. The tests verify exports do not mutate wiki state, graph exports include expected degradation and Mermaid output, failed report writes clean up partial JSON output, and graph export errors map to invalid input.
[crates/gwiki/src/exports.rs:9-13]
[crates/gwiki/src/exports.rs:16-20]
[crates/gwiki/src/exports.rs:23-27]
[crates/gwiki/src/exports.rs:30-38]
[crates/gwiki/src/exports.rs:41-45]

## API Symbols

- `ExportKind` (type) component `ExportKind [type]` (`e4c70df6-3935-5003-8a3d-c52a0d2fe3a2`) lines 9-13 [crates/gwiki/src/exports.rs:9-13]
  - Signature: `pub enum ExportKind {`
  - Purpose: Indexed type `ExportKind` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:9-13]
- `ExportRequest` (class) component `ExportRequest [class]` (`26c5c12a-1855-5d00-abf5-8df23166c2d3`) lines 16-20 [crates/gwiki/src/exports.rs:16-20]
  - Signature: `pub struct ExportRequest {`
  - Purpose: Indexed class `ExportRequest` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:16-20]
- `ExportArtifact` (class) component `ExportArtifact [class]` (`aea3b630-b223-5027-a77e-3b57981ace26`) lines 23-27 [crates/gwiki/src/exports.rs:23-27]
  - Signature: `pub struct ExportArtifact {`
  - Purpose: Indexed class `ExportArtifact` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:23-27]
- `ExportCommand` (type) component `ExportCommand [type]` (`fe3555b8-f97c-5daa-8a6c-f88f12baf878`) lines 30-38 [crates/gwiki/src/exports.rs:30-38]
  - Signature: `pub enum ExportCommand {`
  - Purpose: Indexed type `ExportCommand` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:30-38]
- `ExportOutput` (class) component `ExportOutput [class]` (`c97b1fd9-5d15-5e7a-bc93-76c25f4797a3`) lines 41-45 [crates/gwiki/src/exports.rs:41-45]
  - Signature: `pub struct ExportOutput {`
  - Purpose: Indexed class `ExportOutput` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:41-45]
- `ExportOutput` (class) component `ExportOutput [class]` (`b5234f9a-c131-5494-899b-206f6cc20870`) lines 47-55 [crates/gwiki/src/exports.rs:47-55]
  - Signature: `impl ExportOutput {`
  - Purpose: Indexed class `ExportOutput` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:47-55]
- `ExportOutput.new` (method) component `ExportOutput.new [method]` (`871bba1c-a52a-5692-9d43-c68d220ffb38`) lines 48-54 [crates/gwiki/src/exports.rs:48-54]
  - Signature: `pub fn new(scope: ScopeIdentity, artifacts: Vec<ExportArtifact>) -> Self {`
  - Purpose: Indexed method `ExportOutput.new` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:48-54]
- `WorkflowAsset` (class) component `WorkflowAsset [class]` (`37a44dc7-471f-58bc-b5f8-ea66ad6e85b5`) lines 58-62 [crates/gwiki/src/exports.rs:58-62]
  - Signature: `pub struct WorkflowAsset {`
  - Purpose: Indexed class `WorkflowAsset` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:58-62]
- `bundled_workflow_assets` (function) component `bundled_workflow_assets [function]` (`08df431a-d024-595d-9a8f-7c0aef0903e4`) lines 82-84 [crates/gwiki/src/exports.rs:82-84]
  - Signature: `pub fn bundled_workflow_assets() -> &'static [WorkflowAsset] {`
  - Purpose: Indexed function `bundled_workflow_assets` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:82-84]
- `run` (function) component `run [function]` (`bf287703-ea62-596e-9f2f-72a3e66dd307`) lines 86-96 [crates/gwiki/src/exports.rs:86-96]
  - Signature: `pub fn run(root: &Path, command: ExportCommand) -> Result<Vec<ExportArtifact>, WikiError> {`
  - Purpose: Indexed function `run` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:86-96]
- `export_workflow_assets` (function) component `export_workflow_assets [function]` (`fd40e7f9-7ae9-52bd-b7bc-081123b69ae1`) lines 98-110 [crates/gwiki/src/exports.rs:98-110]
  - Signature: `pub fn export_workflow_assets(`
  - Purpose: Indexed function `export_workflow_assets` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:98-110]
- `export_report_file` (function) component `export_report_file [function]` (`9fe001b9-7614-5808-b65b-a89807879e4b`) lines 112-131 [crates/gwiki/src/exports.rs:112-131]
  - Signature: `pub fn export_report_file(`
  - Purpose: Indexed function `export_report_file` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:112-131]
- `export_graph_artifacts` (function) component `export_graph_artifacts [function]` (`6b1f587c-fdf0-596d-86db-fbe153e8d77e`) lines 133-168 [crates/gwiki/src/exports.rs:133-168]
  - Signature: `pub fn export_graph_artifacts(`
  - Purpose: Indexed function `export_graph_artifacts` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:133-168]
- `graph_export_error` (function) component `graph_export_error [function]` (`eb68a6d3-e5b7-5eab-9aee-99279b71bebe`) lines 170-175 [crates/gwiki/src/exports.rs:170-175]
  - Signature: `fn graph_export_error(error: crate::graph::analytics::GraphAnalyticsError) -> WikiError {`
  - Purpose: Indexed function `graph_export_error` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:170-175]
- `export_markdown_report` (function) component `export_markdown_report [function]` (`e8a8e2d2-6ece-5df7-b9a0-3440fc201071`) lines 177-190 [crates/gwiki/src/exports.rs:177-190]
  - Signature: `pub fn export_markdown_report(`
  - Purpose: Indexed function `export_markdown_report` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:177-190]
- `write_export` (function) component `write_export [function]` (`09ee7edb-a4f4-5279-afc3-68ea90ca82f5`) lines 192-214 [crates/gwiki/src/exports.rs:192-214]
  - Signature: `pub fn write_export(root: &Path, request: ExportRequest) -> Result<ExportArtifact, WikiError> {`
  - Purpose: Indexed function `write_export` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:192-214]
- `export_relative_path` (function) component `export_relative_path [function]` (`e661c499-7ca7-5441-ae47-21d03701c179`) lines 216-238 [crates/gwiki/src/exports.rs:216-238]
  - Signature: `fn export_relative_path(filename: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `export_relative_path` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:216-238]
- `invalid_export_filename` (function) component `invalid_export_filename [function]` (`ae1b6a22-fe4d-53f5-8e24-66c93a496034`) lines 240-245 [crates/gwiki/src/exports.rs:240-245]
  - Signature: `fn invalid_export_filename(filename: &str) -> WikiError {`
  - Purpose: Indexed function `invalid_export_filename` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:240-245]
- `workflow_assets_bundle` (function) component `workflow_assets_bundle [function]` (`8543f843-5cb4-5fa3-9e9e-4cb36833f6a7`) lines 247-260 [crates/gwiki/src/exports.rs:247-260]
  - Signature: `fn workflow_assets_bundle() -> String {`
  - Purpose: Indexed function `workflow_assets_bundle` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:247-260]
- `exports_do_not_mutate_wiki_state` (function) component `exports_do_not_mutate_wiki_state [function]` (`a52d1077-e788-59d5-a6e4-d2706db2c634`) lines 276-330 [crates/gwiki/src/exports.rs:276-330]
  - Signature: `fn exports_do_not_mutate_wiki_state() {`
  - Purpose: Indexed function `exports_do_not_mutate_wiki_state` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:276-330]
- `graph_analytics_export_artifacts_include_degradation_and_mermaid` (function) component `graph_analytics_export_artifacts_include_degradation_and_mermaid [function]` (`f13a7e08-a4f0-59aa-87f7-edf0a4d3e3d5`) lines 333-448 [crates/gwiki/src/exports.rs:333-448]
  - Signature: `fn graph_analytics_export_artifacts_include_degradation_and_mermaid() {`
  - Purpose: Indexed function `graph_analytics_export_artifacts_include_degradation_and_mermaid` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:333-448]
- `graph_export_removes_json_when_report_write_fails` (function) component `graph_export_removes_json_when_report_write_fails [function]` (`a006216b-379c-5722-ad6e-3ba38479b67d`) lines 451-467 [crates/gwiki/src/exports.rs:451-467]
  - Signature: `fn graph_export_removes_json_when_report_write_fails() {`
  - Purpose: Indexed function `graph_export_removes_json_when_report_write_fails` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:451-467]
- `graph_export_errors_are_invalid_input` (function) component `graph_export_errors_are_invalid_input [function]` (`bf83b70c-53e2-5115-894f-5a474b383830`) lines 470-486 [crates/gwiki/src/exports.rs:470-486]
  - Signature: `fn graph_export_errors_are_invalid_input() {`
  - Purpose: Indexed function `graph_export_errors_are_invalid_input` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:470-486]

