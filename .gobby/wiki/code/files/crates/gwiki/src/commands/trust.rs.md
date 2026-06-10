---
title: crates/gwiki/src/commands/trust.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/trust.rs
  ranges:
  - 14-46
  - 48-52
  - 54-94
  - 96-105
  - 108-123
  - 125-197
  - 126-196
  - 200-207
  - 209-220
  - 210-219
  - 223-227
  - 230-234
  - 237-240
  - 243-246
  - 249-256
  - 258-295
  - 297-319
  - 321-327
  - 329-335
  - 337-357
  - 364-373
  - 376-404
  - 407-480
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/trust.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/trust.rs` exposes 23 indexed API symbols.
[crates/gwiki/src/commands/trust.rs:14-46]
[crates/gwiki/src/commands/trust.rs:48-52]
[crates/gwiki/src/commands/trust.rs:54-94]
[crates/gwiki/src/commands/trust.rs:96-105]
[crates/gwiki/src/commands/trust.rs:108-123]
[crates/gwiki/src/commands/trust.rs:125-197]
[crates/gwiki/src/commands/trust.rs:126-196]
[crates/gwiki/src/commands/trust.rs:200-207]
[crates/gwiki/src/commands/trust.rs:209-220]
[crates/gwiki/src/commands/trust.rs:210-219]
[crates/gwiki/src/commands/trust.rs:223-227]
[crates/gwiki/src/commands/trust.rs:230-234]
[crates/gwiki/src/commands/trust.rs:237-240]
[crates/gwiki/src/commands/trust.rs:243-246]
[crates/gwiki/src/commands/trust.rs:249-256]
[crates/gwiki/src/commands/trust.rs:258-295]
[crates/gwiki/src/commands/trust.rs:297-319]
[crates/gwiki/src/commands/trust.rs:321-327]
[crates/gwiki/src/commands/trust.rs:329-335]
[crates/gwiki/src/commands/trust.rs:337-357]
[crates/gwiki/src/commands/trust.rs:364-373]
[crates/gwiki/src/commands/trust.rs:376-404]
[crates/gwiki/src/commands/trust.rs:407-480]

## API Symbols

- `execute` (function) component `execute [function]` (`10c09de1-bf0b-56d8-9fc6-770d1316814d`) lines 14-46 [crates/gwiki/src/commands/trust.rs:14-46]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Aggregates runtime status, index counts, health inspection, and audit diagnostics for a scope into a TrustReport, serializes it to JSON, and returns the result as a command outcome. [crates/gwiki/src/commands/trust.rs:14-46]
- `IndexCountsOutcome` (class) component `IndexCountsOutcome [class]` (`ff66e055-4525-5a59-83fe-a203a116b52a`) lines 48-52 [crates/gwiki/src/commands/trust.rs:48-52]
  - Signature: `struct IndexCountsOutcome {`
  - Purpose: `IndexCountsOutcome` is a struct that encapsulates the results of an indexing operation, containing the computed index counts, the backend implementation used, and a vector of any performance degradations encountered. [crates/gwiki/src/commands/trust.rs:48-52]
- `load_index_counts` (function) component `load_index_counts [function]` (`9fa3d9f3-cae0-5baa-a69e-b4a5c3115926`) lines 54-94 [crates/gwiki/src/commands/trust.rs:54-94]
  - Signature: `fn load_index_counts(`
  - Purpose: Retrieves search index counts from PostgreSQL if available and configured, falling back to memory-based computation while recording any connection or query failures as degradations. [crates/gwiki/src/commands/trust.rs:54-94]
- `memory_index_counts` (function) component `memory_index_counts [function]` (`bcc8b184-f0af-5694-bfa4-4d26481f138f`) lines 96-105 [crates/gwiki/src/commands/trust.rs:96-105]
  - Signature: `fn memory_index_counts(`
  - Purpose: Indexes a wiki vault at the specified root path with provided options into a MemoryWikiStore and returns count statistics of the indexed content. [crates/gwiki/src/commands/trust.rs:96-105]
- `TrustReport` (class) component `TrustReport [class]` (`2033039c-784b-5c5f-b6ac-3d22e8347588`) lines 108-123 [crates/gwiki/src/commands/trust.rs:108-123]
  - Signature: `struct TrustReport {`
  - Purpose: TrustReport is a composite diagnostic structure that aggregates trust verification status, audit state, health metrics, and service freshness summaries for a scoped execution context rooted at a specific filesystem path. [crates/gwiki/src/commands/trust.rs:108-123]
- `TrustReport` (class) component `TrustReport [class]` (`c4b2bafd-41b9-5212-b832-0159fafdf7aa`) lines 125-197 [crates/gwiki/src/commands/trust.rs:125-197]
  - Signature: `impl TrustReport {`
  - Purpose: **TrustReport::from_parts** aggregates health diagnostics, audit findings, index metrics, and service configuration into a unified trust assessment containing summaries of data freshness, audit compliance, link integrity, and system degradations. [crates/gwiki/src/commands/trust.rs:125-197]
- `TrustReport.from_parts` (method) component `TrustReport.from_parts [method]` (`a2c1eac3-80e3-5d99-a71d-5410d47bf766`) lines 126-196 [crates/gwiki/src/commands/trust.rs:126-196]
  - Signature: `fn from_parts(`
  - Purpose: Constructs Self by aggregating index counts, health metrics, and audit data into structured summaries (freshness, audit, links, health, and graph metrics) to compute trust status and service degradation state. [crates/gwiki/src/commands/trust.rs:126-196]
- `TrustIndexCounts` (class) component `TrustIndexCounts [class]` (`f0a42b4a-e160-5225-98bd-9aead5b4f8a3`) lines 200-207 [crates/gwiki/src/commands/trust.rs:200-207]
  - Signature: `struct TrustIndexCounts {`
  - Purpose: `TrustIndexCounts` is a struct that stores quantitative metrics—document, chunk, link, source, and ingestion counts—associated with a static backend identifier. [crates/gwiki/src/commands/trust.rs:200-207]
- `TrustIndexCounts` (class) component `TrustIndexCounts [class]` (`695d0e35-d7c1-5f02-920d-e49d35115b51`) lines 209-220 [crates/gwiki/src/commands/trust.rs:209-220]
  - Signature: `impl TrustIndexCounts {`
  - Purpose: The `from_counts` method constructs a `TrustIndexCounts` instance by mapping fields from a source `IndexCounts` reference and associating them with a static backend identifier. [crates/gwiki/src/commands/trust.rs:209-220]
- `TrustIndexCounts.from_counts` (method) component `TrustIndexCounts.from_counts [method]` (`7a6783e8-7455-55b0-bbcc-a7f6879f4a9e`) lines 210-219 [crates/gwiki/src/commands/trust.rs:210-219]
  - Signature: `fn from_counts(backend: &'static str, counts: &counts::IndexCounts) -> Self {`
  - Purpose: Constructs a new instance by extracting document, chunk, link, source, and ingestion count metrics from an `IndexCounts` reference and associating them with a static backend identifier. [crates/gwiki/src/commands/trust.rs:210-219]
- `FreshnessSummary` (class) component `FreshnessSummary [class]` (`d2e8bcfe-38b5-5117-a3bb-124374b49361`) lines 223-227 [crates/gwiki/src/commands/trust.rs:223-227]
  - Signature: `struct FreshnessSummary {`
  - Purpose: FreshnessSummary is a struct that aggregates content freshness metrics, containing counts of stale pages and stale citations (both usize) and a boolean flag indicating overall freshness status. [crates/gwiki/src/commands/trust.rs:223-227]
- `AuditSummary` (class) component `AuditSummary [class]` (`0f00b216-4500-5548-b22d-02725addc862`) lines 230-234 [crates/gwiki/src/commands/trust.rs:230-234]
  - Signature: `struct AuditSummary {`
  - Purpose: AuditSummary aggregates audit state information with counts of unsupported claims and source contexts. [crates/gwiki/src/commands/trust.rs:230-234]
- `LinkSummary` (class) component `LinkSummary [class]` (`17a94480-3a78-5703-bb0a-3c720a55b65e`) lines 237-240 [crates/gwiki/src/commands/trust.rs:237-240]
  - Signature: `struct LinkSummary {`
  - Purpose: LinkSummary is a struct that stores counts of broken links and duplicate concepts. [crates/gwiki/src/commands/trust.rs:237-240]
- `GraphMetrics` (class) component `GraphMetrics [class]` (`baed0555-2bb2-58f5-a229-b86ac5a5501c`) lines 243-246 [crates/gwiki/src/commands/trust.rs:243-246]
  - Signature: `struct GraphMetrics {`
  - Purpose: GraphMetrics is a struct that aggregates metrics for a graph system, tracking the count of wiki links and whether FalkorDB is configured. [crates/gwiki/src/commands/trust.rs:243-246]
- `HealthSummary` (class) component `HealthSummary [class]` (`3f0f7880-d52e-5534-94cf-3f26606170dd`) lines 249-256 [crates/gwiki/src/commands/trust.rs:249-256]
  - Signature: `struct HealthSummary {`
  - Purpose: `HealthSummary` is a struct that aggregates counts of various content quality issues including stale pages/citations, uncited sources, uncompiled code, broken links, and duplicate concepts. [crates/gwiki/src/commands/trust.rs:249-256]
- `degradation_labels` (function) component `degradation_labels [function]` (`d2254af8-b521-526f-b66e-91708879f743`) lines 258-295 [crates/gwiki/src/commands/trust.rs:258-295]
  - Signature: `fn degradation_labels(`
  - Purpose: Constructs a sorted vector of degradation labels by merging input degradations with conditionally-generated labels indicating unconfigured services, empty indices, stale content, unsupported claims, broken links, duplicate concepts, and citation/compilation issues. [crates/gwiki/src/commands/trust.rs:258-295]
- `trust_status` (function) component `trust_status [function]` (`e5b16265-52b7-5974-9e37-29638fdb6a42`) lines 297-319 [crates/gwiki/src/commands/trust.rs:297-319]
  - Signature: `fn trust_status(`
  - Purpose: Classifies trust status into one of four levels ('unindexed', 'attention_required', 'clean', or 'degraded') by hierarchically evaluating document indexing state, audit findings, link validity, source health, data freshness, and system degradations. [crates/gwiki/src/commands/trust.rs:297-319]
- `audit_state` (function) component `audit_state [function]` (`62783b68-3024-5fbb-91d1-769b3379bdb5`) lines 321-327 [crates/gwiki/src/commands/trust.rs:321-327]
  - Signature: `fn audit_state(unsupported_claim_count: usize) -> &'static str {`
  - Purpose: Maps the unsupported claim count to a static audit state string, returning `"clean"` if the count is zero, otherwise `"unsupported_claims"`. [crates/gwiki/src/commands/trust.rs:321-327]
- `service_configured` (function) component `service_configured [function]` (`489d07d4-0175-51f9-97b3-32509204431f`) lines 329-335 [crates/gwiki/src/commands/trust.rs:329-335]
  - Signature: `fn service_configured(services: &Value, service: &str) -> bool {`
  - Purpose: Returns the boolean value of the `"configured"` field for a specified service from a `Value` structure, defaulting to `false` if the service, field, or type conversion is absent. [crates/gwiki/src/commands/trust.rs:329-335]
- `render_text` (function) component `render_text [function]` (`d033754f-6f13-575c-9bef-1be62b55acb6`) lines 337-357 [crates/gwiki/src/commands/trust.rs:337-357]
  - Signature: `fn render_text(report: &TrustReport) -> String {`
  - Purpose: Converts a TrustReport struct into a formatted text string displaying trust status, scope, runtime, index metrics, freshness indicators, audit findings, link quality, and system degradations. [crates/gwiki/src/commands/trust.rs:337-357]
- `indexed_counts` (function) component `indexed_counts [function]` (`6b13bbf3-600c-5791-ab79-b45ea819c0a1`) lines 364-373 [crates/gwiki/src/commands/trust.rs:364-373]
  - Signature: `fn indexed_counts() -> TrustIndexCounts {`
  - Purpose: Returns a hardcoded `TrustIndexCounts` struct indicating 1 document, 2 chunks, 3 links, 1 source, and 1 ingestion stored in the memory backend. [crates/gwiki/src/commands/trust.rs:364-373]
- `trust_status_prioritizes_audit_attention` (function) component `trust_status_prioritizes_audit_attention [function]` (`0b8cde2c-40cf-5d19-80bb-a7aaa5ea605d`) lines 376-404 [crates/gwiki/src/commands/trust.rs:376-404]
  - Signature: `fn trust_status_prioritizes_audit_attention() {`
  - Purpose: This unit test verifies that the `trust_status` function returns `"attention_required"` when audit anomalies (unsupported claims) are detected, prioritizing audit findings over otherwise healthy freshness, link, and health metrics. [crates/gwiki/src/commands/trust.rs:376-404]
- `trust_report_json_includes_contract_fields` (function) component `trust_report_json_includes_contract_fields [function]` (`7830881e-3b97-5a6c-ae82-4fd4fe15d3f8`) lines 407-480 [crates/gwiki/src/commands/trust.rs:407-480]
  - Signature: `fn trust_report_json_includes_contract_fields() {`
  - Purpose: This function constructs a complete `TrustReport` instance with all required contract fields (audit summary, freshness/health metrics, service configurations, and degradation labels) populated to verify JSON serialization includes the full schema. [crates/gwiki/src/commands/trust.rs:407-480]

