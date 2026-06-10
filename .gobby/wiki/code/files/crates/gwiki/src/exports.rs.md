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
  - 48-54
  - 58-62
  - 87-89
  - 91-101
  - 103-115
  - 117-136
  - 138-173
  - 175-180
  - 182-195
  - 197-219
  - 221-243
  - 245-250
  - 252-265
  - 281-335
  - 338-453
  - 456-472
  - 475-491
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/exports.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/exports.rs` exposes 23 indexed API symbols.
[crates/gwiki/src/exports.rs:9-13]
[crates/gwiki/src/exports.rs:16-20]
[crates/gwiki/src/exports.rs:23-27]
[crates/gwiki/src/exports.rs:30-38]
[crates/gwiki/src/exports.rs:41-45]
[crates/gwiki/src/exports.rs:47-55]
[crates/gwiki/src/exports.rs:48-54]
[crates/gwiki/src/exports.rs:58-62]
[crates/gwiki/src/exports.rs:87-89]
[crates/gwiki/src/exports.rs:91-101]
[crates/gwiki/src/exports.rs:103-115]
[crates/gwiki/src/exports.rs:117-136]
[crates/gwiki/src/exports.rs:138-173]
[crates/gwiki/src/exports.rs:175-180]
[crates/gwiki/src/exports.rs:182-195]
[crates/gwiki/src/exports.rs:197-219]
[crates/gwiki/src/exports.rs:221-243]
[crates/gwiki/src/exports.rs:245-250]
[crates/gwiki/src/exports.rs:252-265]
[crates/gwiki/src/exports.rs:281-335]
[crates/gwiki/src/exports.rs:338-453]
[crates/gwiki/src/exports.rs:456-472]
[crates/gwiki/src/exports.rs:475-491]

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
- `bundled_workflow_assets` (function) component `bundled_workflow_assets [function]` (`bc6f562e-ff68-5f46-9b24-27625782a950`) lines 87-89 [crates/gwiki/src/exports.rs:87-89]
  - Signature: `pub fn bundled_workflow_assets() -> &'static [WorkflowAsset] {`
  - Purpose: Indexed function `bundled_workflow_assets` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:87-89]
- `run` (function) component `run [function]` (`50298874-9702-56f6-9761-830430c0df96`) lines 91-101 [crates/gwiki/src/exports.rs:91-101]
  - Signature: `pub fn run(root: &Path, command: ExportCommand) -> Result<Vec<ExportArtifact>, WikiError> {`
  - Purpose: Indexed function `run` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:91-101]
- `export_workflow_assets` (function) component `export_workflow_assets [function]` (`dbe3c215-af07-575c-b39f-8620332ae88c`) lines 103-115 [crates/gwiki/src/exports.rs:103-115]
  - Signature: `pub fn export_workflow_assets(`
  - Purpose: Indexed function `export_workflow_assets` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:103-115]
- `export_report_file` (function) component `export_report_file [function]` (`0f08e95f-230f-5fa3-add8-012f9f193a8d`) lines 117-136 [crates/gwiki/src/exports.rs:117-136]
  - Signature: `pub fn export_report_file(`
  - Purpose: Indexed function `export_report_file` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:117-136]
- `export_graph_artifacts` (function) component `export_graph_artifacts [function]` (`cb6f0e02-f484-5024-8f91-312bb473db81`) lines 138-173 [crates/gwiki/src/exports.rs:138-173]
  - Signature: `pub fn export_graph_artifacts(`
  - Purpose: Indexed function `export_graph_artifacts` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:138-173]
- `graph_export_error` (function) component `graph_export_error [function]` (`f2ce147a-d7a7-59af-b276-66d4cce36341`) lines 175-180 [crates/gwiki/src/exports.rs:175-180]
  - Signature: `fn graph_export_error(error: crate::graph::analytics::GraphAnalyticsError) -> WikiError {`
  - Purpose: Indexed function `graph_export_error` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:175-180]
- `export_markdown_report` (function) component `export_markdown_report [function]` (`2e04c0c9-b8b2-526e-840c-69a6fc29e579`) lines 182-195 [crates/gwiki/src/exports.rs:182-195]
  - Signature: `pub fn export_markdown_report(`
  - Purpose: Indexed function `export_markdown_report` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:182-195]
- `write_export` (function) component `write_export [function]` (`eb5ada6c-a390-549c-9d39-d3714d0f6123`) lines 197-219 [crates/gwiki/src/exports.rs:197-219]
  - Signature: `pub fn write_export(root: &Path, request: ExportRequest) -> Result<ExportArtifact, WikiError> {`
  - Purpose: Indexed function `write_export` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:197-219]
- `export_relative_path` (function) component `export_relative_path [function]` (`f86dba80-ad40-5c9c-8321-8005b9b84b37`) lines 221-243 [crates/gwiki/src/exports.rs:221-243]
  - Signature: `fn export_relative_path(filename: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `export_relative_path` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:221-243]
- `invalid_export_filename` (function) component `invalid_export_filename [function]` (`e5863d60-a334-5b3b-9569-ccd60c705d7a`) lines 245-250 [crates/gwiki/src/exports.rs:245-250]
  - Signature: `fn invalid_export_filename(filename: &str) -> WikiError {`
  - Purpose: Indexed function `invalid_export_filename` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:245-250]
- `workflow_assets_bundle` (function) component `workflow_assets_bundle [function]` (`c409f1cc-31d7-5f10-89ce-2f1f10f611e1`) lines 252-265 [crates/gwiki/src/exports.rs:252-265]
  - Signature: `fn workflow_assets_bundle() -> String {`
  - Purpose: Indexed function `workflow_assets_bundle` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:252-265]
- `exports_do_not_mutate_wiki_state` (function) component `exports_do_not_mutate_wiki_state [function]` (`38c27d48-9641-52b1-8b0c-4bc3fcc27386`) lines 281-335 [crates/gwiki/src/exports.rs:281-335]
  - Signature: `fn exports_do_not_mutate_wiki_state() {`
  - Purpose: Indexed function `exports_do_not_mutate_wiki_state` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:281-335]
- `graph_analytics_export_artifacts_include_degradation_and_mermaid` (function) component `graph_analytics_export_artifacts_include_degradation_and_mermaid [function]` (`1bd6962a-5607-5f54-a1fc-353f23cf9cd5`) lines 338-453 [crates/gwiki/src/exports.rs:338-453]
  - Signature: `fn graph_analytics_export_artifacts_include_degradation_and_mermaid() {`
  - Purpose: Indexed function `graph_analytics_export_artifacts_include_degradation_and_mermaid` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:338-453]
- `graph_export_removes_json_when_report_write_fails` (function) component `graph_export_removes_json_when_report_write_fails [function]` (`1f902714-fe4c-51a0-966b-37f6fdbd1bbe`) lines 456-472 [crates/gwiki/src/exports.rs:456-472]
  - Signature: `fn graph_export_removes_json_when_report_write_fails() {`
  - Purpose: Indexed function `graph_export_removes_json_when_report_write_fails` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:456-472]
- `graph_export_errors_are_invalid_input` (function) component `graph_export_errors_are_invalid_input [function]` (`57e4aa95-7d36-5c21-96be-ae6a9b5d11ce`) lines 475-491 [crates/gwiki/src/exports.rs:475-491]
  - Signature: `fn graph_export_errors_are_invalid_input() {`
  - Purpose: Indexed function `graph_export_errors_are_invalid_input` in `crates/gwiki/src/exports.rs`. [crates/gwiki/src/exports.rs:475-491]

