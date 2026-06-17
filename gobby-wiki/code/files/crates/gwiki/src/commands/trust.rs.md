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
  - 126-196
  - 200-207
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/trust.rs:14-46](crates/gwiki/src/commands/trust.rs#L14-L46), [crates/gwiki/src/commands/trust.rs:48-52](crates/gwiki/src/commands/trust.rs#L48-L52), [crates/gwiki/src/commands/trust.rs:54-94](crates/gwiki/src/commands/trust.rs#L54-L94), [crates/gwiki/src/commands/trust.rs:96-105](crates/gwiki/src/commands/trust.rs#L96-L105), [crates/gwiki/src/commands/trust.rs:108-123](crates/gwiki/src/commands/trust.rs#L108-L123), [crates/gwiki/src/commands/trust.rs:126-196](crates/gwiki/src/commands/trust.rs#L126-L196), [crates/gwiki/src/commands/trust.rs:200-207](crates/gwiki/src/commands/trust.rs#L200-L207), [crates/gwiki/src/commands/trust.rs:210-219](crates/gwiki/src/commands/trust.rs#L210-L219), [crates/gwiki/src/commands/trust.rs:223-227](crates/gwiki/src/commands/trust.rs#L223-L227), [crates/gwiki/src/commands/trust.rs:230-234](crates/gwiki/src/commands/trust.rs#L230-L234), [crates/gwiki/src/commands/trust.rs:237-240](crates/gwiki/src/commands/trust.rs#L237-L240), [crates/gwiki/src/commands/trust.rs:243-246](crates/gwiki/src/commands/trust.rs#L243-L246), [crates/gwiki/src/commands/trust.rs:249-256](crates/gwiki/src/commands/trust.rs#L249-L256), [crates/gwiki/src/commands/trust.rs:258-295](crates/gwiki/src/commands/trust.rs#L258-L295), [crates/gwiki/src/commands/trust.rs:297-319](crates/gwiki/src/commands/trust.rs#L297-L319), [crates/gwiki/src/commands/trust.rs:321-327](crates/gwiki/src/commands/trust.rs#L321-L327), [crates/gwiki/src/commands/trust.rs:329-335](crates/gwiki/src/commands/trust.rs#L329-L335), [crates/gwiki/src/commands/trust.rs:337-357](crates/gwiki/src/commands/trust.rs#L337-L357), [crates/gwiki/src/commands/trust.rs:364-373](crates/gwiki/src/commands/trust.rs#L364-L373), [crates/gwiki/src/commands/trust.rs:376-404](crates/gwiki/src/commands/trust.rs#L376-L404), [crates/gwiki/src/commands/trust.rs:407-480](crates/gwiki/src/commands/trust.rs#L407-L480)

</details>

# crates/gwiki/src/commands/trust.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `gwiki trust` command, which assembles a trust report for the resolved scope by combining runtime status, index counts, health inspection, and audit results, then returns both JSON and rendered text output.

The helper functions and data types organize that flow: `load_index_counts` chooses the index backend and records degradations, `memory_index_counts` provides the in-memory fallback, and `TrustReport` plus its nested summary structs package the final contract fields. The status helpers derive overall trust, audit, freshness, link, graph, and health summaries, while the test functions verify the prioritization and JSON shape of the report.
[crates/gwiki/src/commands/trust.rs:14-46]
[crates/gwiki/src/commands/trust.rs:48-52]
[crates/gwiki/src/commands/trust.rs:54-94]
[crates/gwiki/src/commands/trust.rs:96-105]
[crates/gwiki/src/commands/trust.rs:108-123]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `10c09de1-bf0b-56d8-9fc6-770d1316814d` | 14-46 [crates/gwiki/src/commands/trust.rs:14-46] | Indexed function `execute` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:14-46] |
| `IndexCountsOutcome` | class | `struct IndexCountsOutcome {` | `IndexCountsOutcome [class]` | `ff66e055-4525-5a59-83fe-a203a116b52a` | 48-52 [crates/gwiki/src/commands/trust.rs:48-52] | Indexed class `IndexCountsOutcome` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:48-52] |
| `load_index_counts` | function | `fn load_index_counts(` | `load_index_counts [function]` | `9fa3d9f3-cae0-5baa-a69e-b4a5c3115926` | 54-94 [crates/gwiki/src/commands/trust.rs:54-94] | Indexed function `load_index_counts` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:54-94] |
| `memory_index_counts` | function | `fn memory_index_counts(` | `memory_index_counts [function]` | `bcc8b184-f0af-5694-bfa4-4d26481f138f` | 96-105 [crates/gwiki/src/commands/trust.rs:96-105] | Indexed function `memory_index_counts` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:96-105] |
| `TrustReport` | class | `struct TrustReport {` | `TrustReport [class]` | `2033039c-784b-5c5f-b6ac-3d22e8347588` | 108-123 [crates/gwiki/src/commands/trust.rs:108-123] | Indexed class `TrustReport` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:108-123] |
| `TrustReport::from_parts` | method | `fn from_parts(` | `TrustReport::from_parts [method]` | `a2c1eac3-80e3-5d99-a71d-5410d47bf766` | 126-196 [crates/gwiki/src/commands/trust.rs:126-196] | Indexed method `TrustReport::from_parts` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:126-196] |
| `TrustIndexCounts` | class | `struct TrustIndexCounts {` | `TrustIndexCounts [class]` | `f0a42b4a-e160-5225-98bd-9aead5b4f8a3` | 200-207 [crates/gwiki/src/commands/trust.rs:200-207] | Indexed class `TrustIndexCounts` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:200-207] |
| `TrustIndexCounts::from_counts` | method | `fn from_counts(backend: &'static str, counts: &counts::IndexCounts) -> Self {` | `TrustIndexCounts::from_counts [method]` | `7a6783e8-7455-55b0-bbcc-a7f6879f4a9e` | 210-219 [crates/gwiki/src/commands/trust.rs:210-219] | Indexed method `TrustIndexCounts::from_counts` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:210-219] |
| `FreshnessSummary` | class | `struct FreshnessSummary {` | `FreshnessSummary [class]` | `d2e8bcfe-38b5-5117-a3bb-124374b49361` | 223-227 [crates/gwiki/src/commands/trust.rs:223-227] | Indexed class `FreshnessSummary` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:223-227] |
| `AuditSummary` | class | `struct AuditSummary {` | `AuditSummary [class]` | `0f00b216-4500-5548-b22d-02725addc862` | 230-234 [crates/gwiki/src/commands/trust.rs:230-234] | Indexed class `AuditSummary` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:230-234] |
| `LinkSummary` | class | `struct LinkSummary {` | `LinkSummary [class]` | `17a94480-3a78-5703-bb0a-3c720a55b65e` | 237-240 [crates/gwiki/src/commands/trust.rs:237-240] | Indexed class `LinkSummary` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:237-240] |
| `GraphMetrics` | class | `struct GraphMetrics {` | `GraphMetrics [class]` | `baed0555-2bb2-58f5-a229-b86ac5a5501c` | 243-246 [crates/gwiki/src/commands/trust.rs:243-246] | Indexed class `GraphMetrics` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:243-246] |
| `HealthSummary` | class | `struct HealthSummary {` | `HealthSummary [class]` | `3f0f7880-d52e-5534-94cf-3f26606170dd` | 249-256 [crates/gwiki/src/commands/trust.rs:249-256] | Indexed class `HealthSummary` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:249-256] |
| `degradation_labels` | function | `fn degradation_labels(` | `degradation_labels [function]` | `d2254af8-b521-526f-b66e-91708879f743` | 258-295 [crates/gwiki/src/commands/trust.rs:258-295] | Indexed function `degradation_labels` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:258-295] |
| `trust_status` | function | `fn trust_status(` | `trust_status [function]` | `e5b16265-52b7-5974-9e37-29638fdb6a42` | 297-319 [crates/gwiki/src/commands/trust.rs:297-319] | Indexed function `trust_status` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:297-319] |
| `audit_state` | function | `fn audit_state(unsupported_claim_count: usize) -> &'static str {` | `audit_state [function]` | `62783b68-3024-5fbb-91d1-769b3379bdb5` | 321-327 [crates/gwiki/src/commands/trust.rs:321-327] | Indexed function `audit_state` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:321-327] |
| `service_configured` | function | `fn service_configured(services: &Value, service: &str) -> bool {` | `service_configured [function]` | `489d07d4-0175-51f9-97b3-32509204431f` | 329-335 [crates/gwiki/src/commands/trust.rs:329-335] | Indexed function `service_configured` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:329-335] |
| `render_text` | function | `fn render_text(report: &TrustReport) -> String {` | `render_text [function]` | `d033754f-6f13-575c-9bef-1be62b55acb6` | 337-357 [crates/gwiki/src/commands/trust.rs:337-357] | Indexed function `render_text` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:337-357] |
| `indexed_counts` | function | `fn indexed_counts() -> TrustIndexCounts {` | `indexed_counts [function]` | `6b13bbf3-600c-5791-ab79-b45ea819c0a1` | 364-373 [crates/gwiki/src/commands/trust.rs:364-373] | Indexed function `indexed_counts` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:364-373] |
| `trust_status_prioritizes_audit_attention` | function | `fn trust_status_prioritizes_audit_attention() {` | `trust_status_prioritizes_audit_attention [function]` | `0b8cde2c-40cf-5d19-80bb-a7aaa5ea605d` | 376-404 [crates/gwiki/src/commands/trust.rs:376-404] | Indexed function `trust_status_prioritizes_audit_attention` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:376-404] |
| `trust_report_json_includes_contract_fields` | function | `fn trust_report_json_includes_contract_fields() {` | `trust_report_json_includes_contract_fields [function]` | `7830881e-3b97-5a6c-ae82-4fd4fe15d3f8` | 407-480 [crates/gwiki/src/commands/trust.rs:407-480] | Indexed function `trust_report_json_includes_contract_fields` in `crates/gwiki/src/commands/trust.rs`. [crates/gwiki/src/commands/trust.rs:407-480] |
