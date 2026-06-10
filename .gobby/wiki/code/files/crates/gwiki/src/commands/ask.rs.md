---
title: crates/gwiki/src/commands/ask.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask.rs
  ranges:
  - 25-46
  - 48-88
  - 90-99
  - 101-119
  - 121-174
  - 176-189
  - 191-241
  - 243-246
  - 248-261
  - 263-272
  - 274-293
  - 295-302
  - '304'
  - '305'
  - 307-360
  - 308-321
  - 323-327
  - 329-334
  - 336-340
  - 342-346
  - 348-352
  - 354-359
  - 362-368
  - 370-379
  - 381-387
  - 389-391
  - 393-422
  - 424-431
  - 433-445
  - 447-460
  - 462-482
  - 484-516
  - 518-557
  - 559-561
  - 563-573
  - 575-618
  - 620-627
  - 643-685
  - 688-739
  - 742-844
  - 847-865
  - 868-882
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/ask.rs` exposes 42 indexed API symbols.
[crates/gwiki/src/commands/ask.rs:25-46]
[crates/gwiki/src/commands/ask.rs:48-88]
[crates/gwiki/src/commands/ask.rs:90-99]
[crates/gwiki/src/commands/ask.rs:101-119]
[crates/gwiki/src/commands/ask.rs:121-174]
[crates/gwiki/src/commands/ask.rs:176-189]
[crates/gwiki/src/commands/ask.rs:191-241]
[crates/gwiki/src/commands/ask.rs:243-246]
[crates/gwiki/src/commands/ask.rs:248-261]
[crates/gwiki/src/commands/ask.rs:263-272]
[crates/gwiki/src/commands/ask.rs:274-293]
[crates/gwiki/src/commands/ask.rs:295-302]
[crates/gwiki/src/commands/ask.rs:304]
[crates/gwiki/src/commands/ask.rs:305]
[crates/gwiki/src/commands/ask.rs:307-360]
[crates/gwiki/src/commands/ask.rs:308-321]
[crates/gwiki/src/commands/ask.rs:323-327]
[crates/gwiki/src/commands/ask.rs:329-334]
[crates/gwiki/src/commands/ask.rs:336-340]
[crates/gwiki/src/commands/ask.rs:342-346]
[crates/gwiki/src/commands/ask.rs:348-352]
[crates/gwiki/src/commands/ask.rs:354-359]
[crates/gwiki/src/commands/ask.rs:362-368]
[crates/gwiki/src/commands/ask.rs:370-379]
[crates/gwiki/src/commands/ask.rs:381-387]
[crates/gwiki/src/commands/ask.rs:389-391]
[crates/gwiki/src/commands/ask.rs:393-422]
[crates/gwiki/src/commands/ask.rs:424-431]
[crates/gwiki/src/commands/ask.rs:433-445]
[crates/gwiki/src/commands/ask.rs:447-460]
[crates/gwiki/src/commands/ask.rs:462-482]
[crates/gwiki/src/commands/ask.rs:484-516]
[crates/gwiki/src/commands/ask.rs:518-557]
[crates/gwiki/src/commands/ask.rs:559-561]
[crates/gwiki/src/commands/ask.rs:563-573]
[crates/gwiki/src/commands/ask.rs:575-618]
[crates/gwiki/src/commands/ask.rs:620-627]
[crates/gwiki/src/commands/ask.rs:643-685]
[crates/gwiki/src/commands/ask.rs:688-739]
[crates/gwiki/src/commands/ask.rs:742-844]
[crates/gwiki/src/commands/ask.rs:847-865]
[crates/gwiki/src/commands/ask.rs:868-882]

## API Symbols

- `execute` (function) component `execute [function]` (`4353e2b8-d8b1-5293-a498-b7a2531873d7`) lines 25-46 [crates/gwiki/src/commands/ask.rs:25-46]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Indexed function `execute` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:25-46]
- `ask_output_from_search` (function) component `ask_output_from_search [function]` (`14a85748-a5cf-54cf-b83c-3a68ad9b9bc1`) lines 48-88 [crates/gwiki/src/commands/ask.rs:48-88]
  - Signature: `fn ask_output_from_search(search: SearchOutput) -> AskOutput {`
  - Purpose: Indexed function `ask_output_from_search` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:48-88]
- `unique_sources` (function) component `unique_sources [function]` (`b1024d5e-48d6-5ade-b322-dbc73619edd5`) lines 90-99 [crates/gwiki/src/commands/ask.rs:90-99]
  - Signature: `fn unique_sources(search: &SearchOutput) -> Vec<String> {`
  - Purpose: Indexed function `unique_sources` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:90-99]
- `code_citations_from_results` (function) component `code_citations_from_results [function]` (`f2ea9f92-7d88-5f5a-b351-41427e848347`) lines 101-119 [crates/gwiki/src/commands/ask.rs:101-119]
  - Signature: `fn code_citations_from_results(results: &[SearchResultOutput]) -> Vec<AskCodeCitationOutput> {`
  - Purpose: Indexed function `code_citations_from_results` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:101-119]
- `enrich_with_attached_unified_graph_context` (function) component `enrich_with_attached_unified_graph_context [function]` (`0dd091dc-5f5d-58c8-8964-215b56eb2d33`) lines 121-174 [crates/gwiki/src/commands/ask.rs:121-174]
  - Signature: `fn enrich_with_attached_unified_graph_context(`
  - Purpose: Indexed function `enrich_with_attached_unified_graph_context` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:121-174]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`55167441-f46a-5e00-af7f-93ba393155e1`) lines 176-189 [crates/gwiki/src/commands/ask.rs:176-189]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Indexed function `optional_falkor_config` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:176-189]
- `enrich_with_unified_graph_context` (function) component `enrich_with_unified_graph_context [function]` (`9fbb6318-bd03-56da-a82f-09207c863935`) lines 191-241 [crates/gwiki/src/commands/ask.rs:191-241]
  - Signature: `fn enrich_with_unified_graph_context(`
  - Purpose: Indexed function `enrich_with_unified_graph_context` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:191-241]
- `mark_degraded_source` (function) component `mark_degraded_source [function]` (`402ecd2a-7a1f-5e0c-bccd-2c8e631658ed`) lines 243-246 [crates/gwiki/src/commands/ask.rs:243-246]
  - Signature: `fn mark_degraded_source(output: &mut AskOutput, dedup: &mut AskOutputDedup, source: &str) {`
  - Purpose: Indexed function `mark_degraded_source` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:243-246]
- `code_citations_from_context_edges` (function) component `code_citations_from_context_edges [function]` (`5491d85a-49d1-5bb5-b46c-a6367d090fa7`) lines 248-261 [crates/gwiki/src/commands/ask.rs:248-261]
  - Signature: `fn code_citations_from_context_edges<'a>(`
  - Purpose: Indexed function `code_citations_from_context_edges` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:248-261]
- `code_edge_from_context` (function) component `code_edge_from_context [function]` (`090e5fa2-0c71-5957-a82e-662778a8115e`) lines 263-272 [crates/gwiki/src/commands/ask.rs:263-272]
  - Signature: `fn code_edge_from_context(edge: &GraphContextCodeEdge) -> AskCodeEdgeOutput {`
  - Purpose: Indexed function `code_edge_from_context` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:263-272]
- `code_citation_from_endpoint` (function) component `code_citation_from_endpoint [function]` (`e891fcac-1f8f-59d2-af71-9a0a649c4049`) lines 274-293 [crates/gwiki/src/commands/ask.rs:274-293]
  - Signature: `fn code_citation_from_endpoint(`
  - Purpose: Indexed function `code_citation_from_endpoint` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:274-293]
- `AskOutputDedup` (class) component `AskOutputDedup [class]` (`4e2a433e-883a-56a7-aadf-0fe37de67bd0`) lines 295-302 [crates/gwiki/src/commands/ask.rs:295-302]
  - Signature: `struct AskOutputDedup {`
  - Purpose: Indexed class `AskOutputDedup` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:295-302]
- `CodeEdgeKey` (type) component `CodeEdgeKey [type]` (`5333f87a-ac51-5a0a-b58b-e0352dee42e6`) lines 304-304 [crates/gwiki/src/commands/ask.rs:304]
  - Signature: `type CodeEdgeKey = (String, String, String, String, Option<usize>, String);`
  - Purpose: Indexed type `CodeEdgeKey` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:304]
- `CodeCitationKey` (type) component `CodeCitationKey [type]` (`8f9f056a-d8ed-53b6-8446-6d43fef80764`) lines 305-305 [crates/gwiki/src/commands/ask.rs:305]
  - Signature: `type CodeCitationKey = (String, Option<usize>, Option<String>);`
  - Purpose: Indexed type `CodeCitationKey` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:305]
- `AskOutputDedup` (class) component `AskOutputDedup [class]` (`1ffb4c35-47e1-5188-8f79-a1a7eef53f57`) lines 307-360 [crates/gwiki/src/commands/ask.rs:307-360]
  - Signature: `impl AskOutputDedup {`
  - Purpose: Indexed class `AskOutputDedup` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:307-360]
- `AskOutputDedup.from_output` (method) component `AskOutputDedup.from_output [method]` (`211c103b-a757-5a99-8ec2-6bf7c70da35e`) lines 308-321 [crates/gwiki/src/commands/ask.rs:308-321]
  - Signature: `fn from_output(output: &AskOutput) -> Self {`
  - Purpose: Indexed method `AskOutputDedup.from_output` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:308-321]
- `AskOutputDedup.push_source` (method) component `AskOutputDedup.push_source [method]` (`9e40fd2e-e0cd-5721-b523-6d0c3babdea9`) lines 323-327 [crates/gwiki/src/commands/ask.rs:323-327]
  - Signature: `fn push_source(&mut self, output: &mut AskOutput, source: String) {`
  - Purpose: Indexed method `AskOutputDedup.push_source` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:323-327]
- `AskOutputDedup.push_degraded_source` (method) component `AskOutputDedup.push_degraded_source [method]` (`02aaa023-9823-59d2-a2de-ce768058bbe1`) lines 329-334 [crates/gwiki/src/commands/ask.rs:329-334]
  - Signature: `fn push_degraded_source(&mut self, output: &mut AskOutput, source: String) {`
  - Purpose: Indexed method `AskOutputDedup.push_degraded_source` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:329-334]
- `AskOutputDedup.push_truncated_component` (method) component `AskOutputDedup.push_truncated_component [method]` (`f658335a-e518-5bbc-95c0-04a758d24252`) lines 336-340 [crates/gwiki/src/commands/ask.rs:336-340]
  - Signature: `fn push_truncated_component(&mut self, output: &mut AskOutput, component: String) {`
  - Purpose: Indexed method `AskOutputDedup.push_truncated_component` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:336-340]
- `AskOutputDedup.push_warning` (method) component `AskOutputDedup.push_warning [method]` (`5a0dbaf2-0496-5b78-9356-7118cb325d49`) lines 342-346 [crates/gwiki/src/commands/ask.rs:342-346]
  - Signature: `fn push_warning(&mut self, output: &mut AskOutput, warning: String) {`
  - Purpose: Indexed method `AskOutputDedup.push_warning` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:342-346]
- `AskOutputDedup.push_code_edge` (method) component `AskOutputDedup.push_code_edge [method]` (`a9e13b90-66cb-5b77-a441-48f2a104b5c5`) lines 348-352 [crates/gwiki/src/commands/ask.rs:348-352]
  - Signature: `fn push_code_edge(&mut self, output: &mut AskOutput, edge: AskCodeEdgeOutput) {`
  - Purpose: Indexed method `AskOutputDedup.push_code_edge` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:348-352]
- `AskOutputDedup.push_code_citation` (method) component `AskOutputDedup.push_code_citation [method]` (`e05cc882-12da-59d2-b2b0-35b2fff16959`) lines 354-359 [crates/gwiki/src/commands/ask.rs:354-359]
  - Signature: `fn push_code_citation(&mut self, output: &mut AskOutput, citation: AskCodeCitationOutput) {`
  - Purpose: Indexed method `AskOutputDedup.push_code_citation` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:354-359]
- `ordered_unique_strings` (function) component `ordered_unique_strings [function]` (`6d18b8e4-7105-5ab3-8caa-d683cdd5f6b2`) lines 362-368 [crates/gwiki/src/commands/ask.rs:362-368]
  - Signature: `fn ordered_unique_strings(values: Vec<String>) -> Vec<String> {`
  - Purpose: Indexed function `ordered_unique_strings` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:362-368]
- `code_edge_key` (function) component `code_edge_key [function]` (`879b8ad8-a1c1-5fc6-8a9b-0c106dc06901`) lines 370-379 [crates/gwiki/src/commands/ask.rs:370-379]
  - Signature: `fn code_edge_key(edge: &AskCodeEdgeOutput) -> CodeEdgeKey {`
  - Purpose: Indexed function `code_edge_key` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:370-379]
- `code_citation_key` (function) component `code_citation_key [function]` (`6ad85944-9afa-5653-870f-e9b5d5e1ec1f`) lines 381-387 [crates/gwiki/src/commands/ask.rs:381-387]
  - Signature: `fn code_citation_key(citation: &AskCodeCitationOutput) -> CodeCitationKey {`
  - Purpose: Indexed function `code_citation_key` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:381-387]
- `is_code_result` (function) component `is_code_result [function]` (`b2631415-1303-5ddd-acab-4cea51a2b91f`) lines 389-391 [crates/gwiki/src/commands/ask.rs:389-391]
  - Signature: `fn is_code_result(hit: &SearchResultOutput) -> bool {`
  - Purpose: Indexed function `is_code_result` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:389-391]
- `synthesize` (function) component `synthesize [function]` (`a93d90b9-e54d-535b-965a-8cbd911a6c95`) lines 393-422 [crates/gwiki/src/commands/ask.rs:393-422]
  - Signature: `fn synthesize(`
  - Purpose: Indexed function `synthesize` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:393-422]
- `ai_config_source` (function) component `ai_config_source [function]` (`af4f21e4-a26e-51bc-9b54-aae1ffdcb677`) lines 424-431 [crates/gwiki/src/commands/ask.rs:424-431]
  - Signature: `fn ai_config_source() -> Result<AiConfigSource, WikiError> {`
  - Purpose: Indexed function `ai_config_source` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:424-431]
- `generate_direct` (function) component `generate_direct [function]` (`895b1dd7-6a57-5825-b966-4354ecde7795`) lines 433-445 [crates/gwiki/src/commands/ask.rs:433-445]
  - Signature: `fn generate_direct(`
  - Purpose: Indexed function `generate_direct` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:433-445]
- `generate_daemon` (function) component `generate_daemon [function]` (`91418d21-b876-5063-bb64-e3a76ab27a5f`) lines 447-460 [crates/gwiki/src/commands/ask.rs:447-460]
  - Signature: `fn generate_daemon(`
  - Purpose: Indexed function `generate_daemon` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:447-460]
- `record_synthesis` (function) component `record_synthesis [function]` (`881e8a89-2906-5647-be46-6d491ee0f0aa`) lines 462-482 [crates/gwiki/src/commands/ask.rs:462-482]
  - Signature: `fn record_synthesis(`
  - Purpose: Indexed function `record_synthesis` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:462-482]
- `mark_ai_unavailable` (function) component `mark_ai_unavailable [function]` (`58edb50a-5435-5b3c-a090-e1976fe735a0`) lines 484-516 [crates/gwiki/src/commands/ask.rs:484-516]
  - Signature: `fn mark_ai_unavailable(`
  - Purpose: Indexed function `mark_ai_unavailable` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:484-516]
- `synthesis_prompt` (function) component `synthesis_prompt [function]` (`27590bad-a4ac-583e-8e0f-4af1a6fd6af6`) lines 518-557 [crates/gwiki/src/commands/ask.rs:518-557]
  - Signature: `fn synthesis_prompt(output: &AskOutput) -> String {`
  - Purpose: Indexed function `synthesis_prompt` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:518-557]
- `synthesis_system` (function) component `synthesis_system [function]` (`89ebd68a-5b81-54d6-96dc-456b2d292a14`) lines 559-561 [crates/gwiki/src/commands/ask.rs:559-561]
  - Signature: `fn synthesis_system() -> &'static str {`
  - Purpose: Indexed function `synthesis_system` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:559-561]
- `render` (function) component `render [function]` (`6d2f8a80-d119-5c10-b3e8-eabf72f90a2c`) lines 563-573 [crates/gwiki/src/commands/ask.rs:563-573]
  - Signature: `fn render(output: AskOutput) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Indexed function `render` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:563-573]
- `render_text` (function) component `render_text [function]` (`b2d07726-da4c-505f-9226-549828d24a14`) lines 575-618 [crates/gwiki/src/commands/ask.rs:575-618]
  - Signature: `fn render_text(query: &str, scope: &ScopeIdentity, output: &AskOutput) -> String {`
  - Purpose: Indexed function `render_text` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:575-618]
- `routing_label` (function) component `routing_label [function]` (`cd78904b-4bd2-55db-b3f2-5e65a2ac4f6c`) lines 620-627 [crates/gwiki/src/commands/ask.rs:620-627]
  - Signature: `fn routing_label(route: AiRouting) -> &'static str {`
  - Purpose: Indexed function `routing_label` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:620-627]
- `ask_output_keeps_full_retrieval_shape` (function) component `ask_output_keeps_full_retrieval_shape [function]` (`7e25140c-cf39-5491-99dd-833aea35ec4f`) lines 643-685 [crates/gwiki/src/commands/ask.rs:643-685]
  - Signature: `fn ask_output_keeps_full_retrieval_shape() {`
  - Purpose: Indexed function `ask_output_keeps_full_retrieval_shape` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:643-685]
- `ask_unified_graph_output_carries_code_citations_and_degradation` (function) component `ask_unified_graph_output_carries_code_citations_and_degradation [function]` (`d6c941d3-ca2c-5a9b-8e6e-5a55eb63664f`) lines 688-739 [crates/gwiki/src/commands/ask.rs:688-739]
  - Signature: `fn ask_unified_graph_output_carries_code_citations_and_degradation() {`
  - Purpose: Indexed function `ask_unified_graph_output_carries_code_citations_and_degradation` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:688-739]
- `ask_unified_graph_enrichment_uses_context_pack_code_edges_and_degrades` (function) component `ask_unified_graph_enrichment_uses_context_pack_code_edges_and_degrades [function]` (`a4430198-951e-5003-9e5e-2986c59626c4`) lines 742-844 [crates/gwiki/src/commands/ask.rs:742-844]
  - Signature: `fn ask_unified_graph_enrichment_uses_context_pack_code_edges_and_degrades() {`
  - Purpose: Indexed function `ask_unified_graph_enrichment_uses_context_pack_code_edges_and_degrades` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:742-844]
- `ask_unified_graph_model_unavailable_marks_degraded` (function) component `ask_unified_graph_model_unavailable_marks_degraded [function]` (`f12bf83f-54ad-5c19-9667-62ffe75de27a`) lines 847-865 [crates/gwiki/src/commands/ask.rs:847-865]
  - Signature: `fn ask_unified_graph_model_unavailable_marks_degraded() {`
  - Purpose: Indexed function `ask_unified_graph_model_unavailable_marks_degraded` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:847-865]
- `llm_ai_off_is_invalid_input` (function) component `llm_ai_off_is_invalid_input [function]` (`403ff745-c666-5b9e-912a-428dd94395da`) lines 868-882 [crates/gwiki/src/commands/ask.rs:868-882]
  - Signature: `fn llm_ai_off_is_invalid_input() {`
  - Purpose: Indexed function `llm_ai_off_is_invalid_input` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:868-882]

