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
  - 48-54
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
  - 333-452
  - 455-471
  - 474-490
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/exports.rs:9-13](crates/gwiki/src/exports.rs#L9-L13), [crates/gwiki/src/exports.rs:16-20](crates/gwiki/src/exports.rs#L16-L20), [crates/gwiki/src/exports.rs:23-27](crates/gwiki/src/exports.rs#L23-L27), [crates/gwiki/src/exports.rs:30-38](crates/gwiki/src/exports.rs#L30-L38), [crates/gwiki/src/exports.rs:41-45](crates/gwiki/src/exports.rs#L41-L45), [crates/gwiki/src/exports.rs:48-54](crates/gwiki/src/exports.rs#L48-L54), [crates/gwiki/src/exports.rs:58-62](crates/gwiki/src/exports.rs#L58-L62), [crates/gwiki/src/exports.rs:82-84](crates/gwiki/src/exports.rs#L82-L84), [crates/gwiki/src/exports.rs:86-96](crates/gwiki/src/exports.rs#L86-L96), [crates/gwiki/src/exports.rs:98-110](crates/gwiki/src/exports.rs#L98-L110), [crates/gwiki/src/exports.rs:112-131](crates/gwiki/src/exports.rs#L112-L131), [crates/gwiki/src/exports.rs:133-168](crates/gwiki/src/exports.rs#L133-L168), [crates/gwiki/src/exports.rs:170-175](crates/gwiki/src/exports.rs#L170-L175), [crates/gwiki/src/exports.rs:177-190](crates/gwiki/src/exports.rs#L177-L190), [crates/gwiki/src/exports.rs:192-214](crates/gwiki/src/exports.rs#L192-L214), [crates/gwiki/src/exports.rs:216-238](crates/gwiki/src/exports.rs#L216-L238), [crates/gwiki/src/exports.rs:240-245](crates/gwiki/src/exports.rs#L240-L245), [crates/gwiki/src/exports.rs:247-260](crates/gwiki/src/exports.rs#L247-L260), [crates/gwiki/src/exports.rs:276-330](crates/gwiki/src/exports.rs#L276-L330), [crates/gwiki/src/exports.rs:333-452](crates/gwiki/src/exports.rs#L333-L452), [crates/gwiki/src/exports.rs:455-471](crates/gwiki/src/exports.rs#L455-L471), [crates/gwiki/src/exports.rs:474-490](crates/gwiki/src/exports.rs#L474-L490)

</details>

# crates/gwiki/src/exports.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the export model and execution path for writing wiki-related outputs. It introduces `ExportKind`, `ExportRequest`, `ExportArtifact`, `ExportCommand`, and `ExportOutput` to describe what is being exported, what gets written, and the result returned to callers. It also bundles built-in workflow assets (`compile`, `query`, `audit`) and exposes `run` as the dispatcher that routes export commands to helpers for workflow assets, report files, graph artifacts, markdown report generation, and filesystem writes. The supporting helpers handle path validation and normalization, generate graph/report content, and surface errors such as invalid filenames or export failures; the tests verify exports do not mutate wiki state and that graph exports include the expected artifacts and cleanup behavior.
[crates/gwiki/src/exports.rs:9-13]
[crates/gwiki/src/exports.rs:16-20]
[crates/gwiki/src/exports.rs:23-27]
[crates/gwiki/src/exports.rs:30-38]
[crates/gwiki/src/exports.rs:41-45]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ExportKind` | type | `pub enum ExportKind {` | `ExportKind [type]` | `e4c70df6-3935-5003-8a3d-c52a0d2fe3a2` | 9-13 [crates/gwiki/src/exports.rs:9-13] | Indexed type `ExportKind` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:9-13] |
| `ExportRequest` | class | `pub struct ExportRequest {` | `ExportRequest [class]` | `26c5c12a-1855-5d00-abf5-8df23166c2d3` | 16-20 [crates/gwiki/src/exports.rs:16-20] | Indexed class `ExportRequest` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:16-20] |
| `ExportArtifact` | class | `pub struct ExportArtifact {` | `ExportArtifact [class]` | `aea3b630-b223-5027-a77e-3b57981ace26` | 23-27 [crates/gwiki/src/exports.rs:23-27] | Indexed class `ExportArtifact` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:23-27] |
| `ExportCommand` | type | `pub enum ExportCommand {` | `ExportCommand [type]` | `fe3555b8-f97c-5daa-8a6c-f88f12baf878` | 30-38 [crates/gwiki/src/exports.rs:30-38] | Indexed type `ExportCommand` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:30-38] |
| `ExportOutput` | class | `pub struct ExportOutput {` | `ExportOutput [class]` | `c97b1fd9-5d15-5e7a-bc93-76c25f4797a3` | 41-45 [crates/gwiki/src/exports.rs:41-45] | Indexed class `ExportOutput` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:41-45] |
| `ExportOutput::new` | method | `pub fn new(scope: ScopeIdentity, artifacts: Vec<ExportArtifact>) -> Self {` | `ExportOutput::new [method]` | `871bba1c-a52a-5692-9d43-c68d220ffb38` | 48-54 [crates/gwiki/src/exports.rs:48-54] | Indexed method `ExportOutput::new` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:48-54] |
| `WorkflowAsset` | class | `pub struct WorkflowAsset {` | `WorkflowAsset [class]` | `37a44dc7-471f-58bc-b5f8-ea66ad6e85b5` | 58-62 [crates/gwiki/src/exports.rs:58-62] | Indexed class `WorkflowAsset` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:58-62] |
| `bundled_workflow_assets` | function | `pub fn bundled_workflow_assets() -> &'static [WorkflowAsset] {` | `bundled_workflow_assets [function]` | `08df431a-d024-595d-9a8f-7c0aef0903e4` | 82-84 [crates/gwiki/src/exports.rs:82-84] | Indexed function `bundled_workflow_assets` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:82-84] |
| `run` | function | `pub fn run(root: &Path, command: ExportCommand) -> Result<Vec<ExportArtifact>, WikiError> {` | `run [function]` | `bf287703-ea62-596e-9f2f-72a3e66dd307` | 86-96 [crates/gwiki/src/exports.rs:86-96] | Indexed function `run` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:86-96] |
| `export_workflow_assets` | function | `pub fn export_workflow_assets(` | `export_workflow_assets [function]` | `fd40e7f9-7ae9-52bd-b7bc-081123b69ae1` | 98-110 [crates/gwiki/src/exports.rs:98-110] | Indexed function `export_workflow_assets` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:98-110] |
| `export_report_file` | function | `pub fn export_report_file(` | `export_report_file [function]` | `9fe001b9-7614-5808-b65b-a89807879e4b` | 112-131 [crates/gwiki/src/exports.rs:112-131] | Indexed function `export_report_file` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:112-131] |
| `export_graph_artifacts` | function | `pub fn export_graph_artifacts(` | `export_graph_artifacts [function]` | `6b1f587c-fdf0-596d-86db-fbe153e8d77e` | 133-168 [crates/gwiki/src/exports.rs:133-168] | Indexed function `export_graph_artifacts` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:133-168] |
| `graph_export_error` | function | `fn graph_export_error(error: crate::graph::analytics::GraphAnalyticsError) -> WikiError {` | `graph_export_error [function]` | `eb68a6d3-e5b7-5eab-9aee-99279b71bebe` | 170-175 [crates/gwiki/src/exports.rs:170-175] | Indexed function `graph_export_error` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:170-175] |
| `export_markdown_report` | function | `pub fn export_markdown_report(` | `export_markdown_report [function]` | `e8a8e2d2-6ece-5df7-b9a0-3440fc201071` | 177-190 [crates/gwiki/src/exports.rs:177-190] | Indexed function `export_markdown_report` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:177-190] |
| `write_export` | function | `pub fn write_export(root: &Path, request: ExportRequest) -> Result<ExportArtifact, WikiError> {` | `write_export [function]` | `09ee7edb-a4f4-5279-afc3-68ea90ca82f5` | 192-214 [crates/gwiki/src/exports.rs:192-214] | Indexed function `write_export` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:192-214] |
| `export_relative_path` | function | `fn export_relative_path(filename: &str) -> Result<PathBuf, WikiError> {` | `export_relative_path [function]` | `e661c499-7ca7-5441-ae47-21d03701c179` | 216-238 [crates/gwiki/src/exports.rs:216-238] | Indexed function `export_relative_path` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:216-238] |
| `invalid_export_filename` | function | `fn invalid_export_filename(filename: &str) -> WikiError {` | `invalid_export_filename [function]` | `ae1b6a22-fe4d-53f5-8e24-66c93a496034` | 240-245 [crates/gwiki/src/exports.rs:240-245] | Indexed function `invalid_export_filename` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:240-245] |
| `workflow_assets_bundle` | function | `fn workflow_assets_bundle() -> String {` | `workflow_assets_bundle [function]` | `8543f843-5cb4-5fa3-9e9e-4cb36833f6a7` | 247-260 [crates/gwiki/src/exports.rs:247-260] | Indexed function `workflow_assets_bundle` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:247-260] |
| `exports_do_not_mutate_wiki_state` | function | `fn exports_do_not_mutate_wiki_state() {` | `exports_do_not_mutate_wiki_state [function]` | `a52d1077-e788-59d5-a6e4-d2706db2c634` | 276-330 [crates/gwiki/src/exports.rs:276-330] | Indexed function `exports_do_not_mutate_wiki_state` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:276-330] |
| `graph_analytics_export_artifacts_include_degradation_and_mermaid` | function | `fn graph_analytics_export_artifacts_include_degradation_and_mermaid() {` | `graph_analytics_export_artifacts_include_degradation_and_mermaid [function]` | `f13a7e08-a4f0-59aa-87f7-edf0a4d3e3d5` | 333-452 [crates/gwiki/src/exports.rs:333-452] | Indexed function `graph_analytics_export_artifacts_include_degradation_and_mermaid` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:333-452] |
| `graph_export_removes_json_when_report_write_fails` | function | `fn graph_export_removes_json_when_report_write_fails() {` | `graph_export_removes_json_when_report_write_fails [function]` | `14cb20da-f658-598b-bb61-ec65a69f2385` | 455-471 [crates/gwiki/src/exports.rs:455-471] | Indexed function `graph_export_removes_json_when_report_write_fails` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:455-471] |
| `graph_export_errors_are_invalid_input` | function | `fn graph_export_errors_are_invalid_input() {` | `graph_export_errors_are_invalid_input [function]` | `60d3b867-5f9a-5085-afa2-7d8377d41454` | 474-490 [crates/gwiki/src/exports.rs:474-490] | Indexed function `graph_export_errors_are_invalid_input` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:474-490] |
