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
  - 424-436
  - 438-451
  - 453-473
  - 475-507
  - 509-548
  - 550-552
  - 554-564
  - 566-609
  - 611-618
  - 634-676
  - 679-730
  - 733-835
  - 838-856
  - 859-873
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/ask.rs` exposes 41 indexed API symbols.
[crates/gwiki/src/commands/ask.rs:25-46]
[crates/gwiki/src/commands/ask.rs:48-88]
[crates/gwiki/src/commands/ask.rs:90-99]
[crates/gwiki/src/commands/ask.rs:101-119]
[crates/gwiki/src/commands/ask.rs:121-174]

## API Symbols

- `execute` (function) component `execute [function]` (`4353e2b8-d8b1-5293-a498-b7a2531873d7`) lines 25-46 [crates/gwiki/src/commands/ask.rs:25-46]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Retrieves search results for a scoped query, enriches them with unified graph context, optionally synthesizes the output via LLM based on configuration flags, and renders the final command outcome. [crates/gwiki/src/commands/ask.rs:25-46]
- `ask_output_from_search` (function) component `ask_output_from_search [function]` (`14a85748-a5cf-54cf-b83c-3a68ad9b9bc1`) lines 48-88 [crates/gwiki/src/commands/ask.rs:48-88]
  - Signature: `fn ask_output_from_search(search: SearchOutput) -> AskOutput {`
  - Purpose: Transforms a `SearchOutput` into an `AskOutput` by extracting related pages, unique sources, code citations, and degradation information while determining retrieval status based on result availability. [crates/gwiki/src/commands/ask.rs:48-88]
- `unique_sources` (function) component `unique_sources [function]` (`b1024d5e-48d6-5ade-b322-dbc73619edd5`) lines 90-99 [crates/gwiki/src/commands/ask.rs:90-99]
  - Signature: `fn unique_sources(search: &SearchOutput) -> Vec<String> {`
  - Purpose: Extracts and deduplicates all source paths and source references from search results, returning them as a sorted vector of unique strings. [crates/gwiki/src/commands/ask.rs:90-99]
- `code_citations_from_results` (function) component `code_citations_from_results [function]` (`f2ea9f92-7d88-5f5a-b351-41427e848347`) lines 101-119 [crates/gwiki/src/commands/ask.rs:101-119]
  - Signature: `fn code_citations_from_results(results: &[SearchResultOutput]) -> Vec<AskCodeCitationOutput> {`
  - Purpose: Deduplicates code search results by (file, symbol) pairs and produces citation objects for each unique combination. [crates/gwiki/src/commands/ask.rs:101-119]
- `enrich_with_attached_unified_graph_context` (function) component `enrich_with_attached_unified_graph_context [function]` (`0dd091dc-5f5d-58c8-8964-215b56eb2d33`) lines 121-174 [crates/gwiki/src/commands/ask.rs:121-174]
  - Signature: `fn enrich_with_attached_unified_graph_context(`
  - Purpose: Enriches an AskOutput with code graph context by loading wiki facts and shared code edges from PostgreSQL and falkor, marking degraded sources for unavailable or truncated data. [crates/gwiki/src/commands/ask.rs:121-174]
- `optional_falkor_config` (function) component `optional_falkor_config [function]` (`55167441-f46a-5e00-af7f-93ba393155e1`) lines 176-189 [crates/gwiki/src/commands/ask.rs:176-189]
  - Signature: `fn optional_falkor_config(conn: &mut postgres::Client) -> Result<Option<FalkorConfig>, WikiError> {`
  - Purpose: Resolves optional FalkorDB configuration from a composite source combining PostgreSQL and file-based configuration from the Gobby home directory. [crates/gwiki/src/commands/ask.rs:176-189]
- `enrich_with_unified_graph_context` (function) component `enrich_with_unified_graph_context [function]` (`9fbb6318-bd03-56da-a82f-09207c863935`) lines 191-241 [crates/gwiki/src/commands/ask.rs:191-241]
  - Signature: `fn enrich_with_unified_graph_context(`
  - Purpose: Populates an AskOutput with deduplicated graph context (related pages, sources, code edges, and citations) from a WikiGraphFacts context pack while tracking degradation and truncation states. [crates/gwiki/src/commands/ask.rs:191-241]
- `mark_degraded_source` (function) component `mark_degraded_source [function]` (`402ecd2a-7a1f-5e0c-bccd-2c8e631658ed`) lines 243-246 [crates/gwiki/src/commands/ask.rs:243-246]
  - Signature: `fn mark_degraded_source(output: &mut AskOutput, dedup: &mut AskOutputDedup, source: &str) {`
  - Purpose: This function marks an AskOutput as degraded by setting its degraded flag to true and registers it in a deduplication structure with the specified source identifier. [crates/gwiki/src/commands/ask.rs:243-246]
- `code_citations_from_context_edges` (function) component `code_citations_from_context_edges [function]` (`5491d85a-49d1-5bb5-b46c-a6367d090fa7`) lines 248-261 [crates/gwiki/src/commands/ask.rs:248-261]
  - Signature: `fn code_citations_from_context_edges<'a>(`
  - Purpose: Generates code citations by extracting source and target endpoint information from each graph context code edge, aggregating successful citations into a vector. [crates/gwiki/src/commands/ask.rs:248-261]
- `code_edge_from_context` (function) component `code_edge_from_context [function]` (`090e5fa2-0c71-5957-a82e-662778a8115e`) lines 263-272 [crates/gwiki/src/commands/ask.rs:263-272]
  - Signature: `fn code_edge_from_context(edge: &GraphContextCodeEdge) -> AskCodeEdgeOutput {`
  - Purpose: Converts a `GraphContextCodeEdge` reference into an `AskCodeEdgeOutput` struct by cloning all fields. [crates/gwiki/src/commands/ask.rs:263-272]
- `code_citation_from_endpoint` (function) component `code_citation_from_endpoint [function]` (`e891fcac-1f8f-59d2-af71-9a0a649c4049`) lines 274-293 [crates/gwiki/src/commands/ask.rs:274-293]
  - Signature: `fn code_citation_from_endpoint(`
  - Purpose: Parses an endpoint string to extract file path and optional symbol components (delimited by '#' or ':'), returning a structured `AskCodeCitationOutput` or `None` if the endpoint is malformed or empty. [crates/gwiki/src/commands/ask.rs:274-293]
- `AskOutputDedup` (class) component `AskOutputDedup [class]` (`4e2a433e-883a-56a7-aadf-0fe37de67bd0`) lines 295-302 [crates/gwiki/src/commands/ask.rs:295-302]
  - Signature: `struct AskOutputDedup {`
  - Purpose: `AskOutputDedup` is a deduplication container that maintains distinct HashSets of sources, degraded sources, truncated components, warnings, code edges, and code citations to eliminate duplicates from Ask operation outputs. [crates/gwiki/src/commands/ask.rs:295-302]
- `CodeEdgeKey` (type) component `CodeEdgeKey [type]` (`5333f87a-ac51-5a0a-b58b-e0352dee42e6`) lines 304-304 [crates/gwiki/src/commands/ask.rs:304]
  - Signature: `type CodeEdgeKey = (String, String, String, String, Option<usize>, String);`
  - Purpose: Indexed type `CodeEdgeKey` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:304]
- `CodeCitationKey` (type) component `CodeCitationKey [type]` (`8f9f056a-d8ed-53b6-8446-6d43fef80764`) lines 305-305 [crates/gwiki/src/commands/ask.rs:305]
  - Signature: `type CodeCitationKey = (String, Option<usize>, Option<String>);`
  - Purpose: Indexed type `CodeCitationKey` in `crates/gwiki/src/commands/ask.rs`. [crates/gwiki/src/commands/ask.rs:305]
- `AskOutputDedup` (class) component `AskOutputDedup [class]` (`1ffb4c35-47e1-5188-8f79-a1a7eef53f57`) lines 307-360 [crates/gwiki/src/commands/ask.rs:307-360]
  - Signature: `impl AskOutputDedup {`
  - Purpose: `AskOutputDedup` is a deduplication utility that conditionally appends items to an `AskOutput` structure only if they haven't been previously added, using HashSet-backed tracking for sources, warnings, code edges, and citations. [crates/gwiki/src/commands/ask.rs:307-360]
- `AskOutputDedup.from_output` (method) component `AskOutputDedup.from_output [method]` (`211c103b-a757-5a99-8ec2-6bf7c70da35e`) lines 308-321 [crates/gwiki/src/commands/ask.rs:308-321]
  - Signature: `fn from_output(output: &AskOutput) -> Self {`
  - Purpose: Constructs a new instance of Self from an AskOutput by cloning collections for sources, degraded sources, truncated components, and warnings, while mapping code edges and citations through key-generating functions. [crates/gwiki/src/commands/ask.rs:308-321]
- `AskOutputDedup.push_source` (method) component `AskOutputDedup.push_source [method]` (`9e40fd2e-e0cd-5721-b523-6d0c3babdea9`) lines 323-327 [crates/gwiki/src/commands/ask.rs:323-327]
  - Signature: `fn push_source(&mut self, output: &mut AskOutput, source: String) {`
  - Purpose: Appends a source to the output collection if and only if the source is newly inserted into the internal deduplication set. [crates/gwiki/src/commands/ask.rs:323-327]
- `AskOutputDedup.push_degraded_source` (method) component `AskOutputDedup.push_degraded_source [method]` (`02aaa023-9823-59d2-a2de-ce768058bbe1`) lines 329-334 [crates/gwiki/src/commands/ask.rs:329-334]
  - Signature: `fn push_degraded_source(&mut self, output: &mut AskOutput, source: String) {`
  - Purpose: Inserts a source into a deduplicating internal set, conditionally appends it to the output's degraded_sources list if newly inserted, and unconditionally pushes a warning. [crates/gwiki/src/commands/ask.rs:329-334]
- `AskOutputDedup.push_truncated_component` (method) component `AskOutputDedup.push_truncated_component [method]` (`f658335a-e518-5bbc-95c0-04a758d24252`) lines 336-340 [crates/gwiki/src/commands/ask.rs:336-340]
  - Signature: `fn push_truncated_component(&mut self, output: &mut AskOutput, component: String) {`
  - Purpose: Inserts a component into an internal deduplicating set and appends it to the output's truncated components list only if the component is newly inserted. [crates/gwiki/src/commands/ask.rs:336-340]
- `AskOutputDedup.push_warning` (method) component `AskOutputDedup.push_warning [method]` (`5a0dbaf2-0496-5b78-9356-7118cb325d49`) lines 342-346 [crates/gwiki/src/commands/ask.rs:342-346]
  - Signature: `fn push_warning(&mut self, output: &mut AskOutput, warning: String) {`
  - Purpose: This method deduplicates warnings by inserting them into an internal set and only appending to the output if the warning is newly added (not previously stored). [crates/gwiki/src/commands/ask.rs:342-346]
- `AskOutputDedup.push_code_edge` (method) component `AskOutputDedup.push_code_edge [method]` (`a9e13b90-66cb-5b77-a441-48f2a104b5c5`) lines 348-352 [crates/gwiki/src/commands/ask.rs:348-352]
  - Signature: `fn push_code_edge(&mut self, output: &mut AskOutput, edge: AskCodeEdgeOutput) {`
  - Purpose: Deduplicates code edges by appending to the output only if the edge's key is not already present in the internal set. [crates/gwiki/src/commands/ask.rs:348-352]
- `AskOutputDedup.push_code_citation` (method) component `AskOutputDedup.push_code_citation [method]` (`e05cc882-12da-59d2-b2b0-35b2fff16959`) lines 354-359 [crates/gwiki/src/commands/ask.rs:354-359]
  - Signature: `fn push_code_citation(&mut self, output: &mut AskOutput, citation: AskCodeCitationOutput) {`
  - Purpose: Inserts a code citation into the output and pushes its source file, but only if the citation key is newly inserted (deduplicating based on citation identity). [crates/gwiki/src/commands/ask.rs:354-359]
- `ordered_unique_strings` (function) component `ordered_unique_strings [function]` (`6d18b8e4-7105-5ab3-8caa-d683cdd5f6b2`) lines 362-368 [crates/gwiki/src/commands/ask.rs:362-368]
  - Signature: `fn ordered_unique_strings(values: Vec<String>) -> Vec<String> {`
  - Purpose: Filters and returns a deduplicated vector containing only the first occurrence of each unique string while preserving insertion order. [crates/gwiki/src/commands/ask.rs:362-368]
- `code_edge_key` (function) component `code_edge_key [function]` (`879b8ad8-a1c1-5fc6-8a9b-0c106dc06901`) lines 370-379 [crates/gwiki/src/commands/ask.rs:370-379]
  - Signature: `fn code_edge_key(edge: &AskCodeEdgeOutput) -> CodeEdgeKey {`
  - Purpose: Constructs a `CodeEdgeKey` tuple by extracting and cloning the source, target, kind, direction, line, and provenance fields from an `AskCodeEdgeOutput`. [crates/gwiki/src/commands/ask.rs:370-379]
- `code_citation_key` (function) component `code_citation_key [function]` (`6ad85944-9afa-5653-870f-e9b5d5e1ec1f`) lines 381-387 [crates/gwiki/src/commands/ask.rs:381-387]
  - Signature: `fn code_citation_key(citation: &AskCodeCitationOutput) -> CodeCitationKey {`
  - Purpose: Constructs a `CodeCitationKey` tuple by extracting the file path, line number, and symbol name from an `AskCodeCitationOutput` reference. [crates/gwiki/src/commands/ask.rs:381-387]
- `is_code_result` (function) component `is_code_result [function]` (`b2631415-1303-5ddd-acab-4cea51a2b91f`) lines 389-391 [crates/gwiki/src/commands/ask.rs:389-391]
  - Signature: `fn is_code_result(hit: &SearchResultOutput) -> bool {`
  - Purpose: This function returns a boolean indicating whether the given `SearchResultOutput` represents a code search result by calling the `is_code()` method on its `result_type` field. [crates/gwiki/src/commands/ask.rs:389-391]
- `synthesize` (function) component `synthesize [function]` (`a93d90b9-e54d-535b-965a-8cbd911a6c95`) lines 393-422 [crates/gwiki/src/commands/ask.rs:393-422]
  - Signature: `fn synthesize(`
  - Purpose: Resolves an AI context with the requested routing mode, determines the effective text generation route, and dispatches to the corresponding handler (direct generation, daemon, or unavailability marking). [crates/gwiki/src/commands/ask.rs:393-422]
- `generate_direct` (function) component `generate_direct [function]` (`71607693-b19f-5daf-a4bb-0adb83857735`) lines 424-436 [crates/gwiki/src/commands/ask.rs:424-436]
  - Signature: `fn generate_direct(`
  - Purpose: Generates AI-synthesized text from a synthesis prompt within the given context, records the result on success, or marks AI unavailable on error based on the `require_ai` constraint. [crates/gwiki/src/commands/ask.rs:424-436]
- `generate_daemon` (function) component `generate_daemon [function]` (`c5726362-dd79-5f95-a88d-bfda26e1804c`) lines 438-451 [crates/gwiki/src/commands/ask.rs:438-451]
  - Signature: `fn generate_daemon(`
  - Purpose: Calls the daemon-based synthesis generator with the provided context and synthesis prompt, recording the text and model information on success, or marking AI unavailable on failure based on the `require_ai` flag. [crates/gwiki/src/commands/ask.rs:438-451]
- `record_synthesis` (function) component `record_synthesis [function]` (`b1504580-3e65-54de-a976-aeef3224bee5`) lines 453-473 [crates/gwiki/src/commands/ask.rs:453-473]
  - Signature: `fn record_synthesis(`
  - Purpose: Records an AI synthesis result by marking an `AskOutput` as "answered" and populating its AI and synthesis metadata with the provided route, model, and answer. [crates/gwiki/src/commands/ask.rs:453-473]
- `mark_ai_unavailable` (function) component `mark_ai_unavailable [function]` (`c723890d-4338-5db8-89c9-1afcc5368371`) lines 475-507 [crates/gwiki/src/commands/ask.rs:475-507]
  - Signature: `fn mark_ai_unavailable(`
  - Purpose: Fails with a `WikiError::Config` if AI synthesis is required, otherwise marks the output as degraded, sets its status to "partial", and records "model_provider_unavailable" in degraded sources. [crates/gwiki/src/commands/ask.rs:475-507]
- `synthesis_prompt` (function) component `synthesis_prompt [function]` (`7495ed1e-7c43-5061-a611-12726bd63bba`) lines 509-548 [crates/gwiki/src/commands/ask.rs:509-548]
  - Signature: `fn synthesis_prompt(output: &AskOutput) -> String {`
  - Purpose: Synthesizes an `AskOutput` query, wiki search results, related pages, and code citations into a formatted prompt string for downstream processing. [crates/gwiki/src/commands/ask.rs:509-548]
- `synthesis_system` (function) component `synthesis_system [function]` (`a981b604-1625-536d-9267-f230d0ee2841`) lines 550-552 [crates/gwiki/src/commands/ask.rs:550-552]
  - Signature: `fn synthesis_system() -> &'static str {`
  - Purpose: `synthesis_system` returns a static string reference containing a system prompt that instructs answers to be grounded exclusively in provided wiki hits, unified graph context, and code citations while acknowledging insufficient evidence. [crates/gwiki/src/commands/ask.rs:550-552]
- `render` (function) component `render [function]` (`45949a04-86ac-5ec6-a3a9-ea65018a366f`) lines 554-564 [crates/gwiki/src/commands/ask.rs:554-564]
  - Signature: `fn render(output: AskOutput) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Transforms an `AskOutput` into a `CommandOutcome` by rendering its query text against the scope and serializing the output as JSON. [crates/gwiki/src/commands/ask.rs:554-564]
- `render_text` (function) component `render_text [function]` (`02220be1-52c1-5a2d-8add-4441dc5e37a6`) lines 566-609 [crates/gwiki/src/commands/ask.rs:566-609]
  - Signature: `fn render_text(query: &str, scope: &ScopeIdentity, output: &AskOutput) -> String {`
  - Purpose: Formats an `AskOutput` into a human-readable text string, returning either a synthesized answer or a formatted list of wiki hits and code citations with scope and degraded source metadata. [crates/gwiki/src/commands/ask.rs:566-609]
- `routing_label` (function) component `routing_label [function]` (`fef977e1-5462-5c7e-b458-2c646b483ad2`) lines 611-618 [crates/gwiki/src/commands/ask.rs:611-618]
  - Signature: `fn routing_label(route: AiRouting) -> &'static str {`
  - Purpose: Maps an `AiRouting` enum variant to its corresponding static string representation. [crates/gwiki/src/commands/ask.rs:611-618]
- `ask_output_keeps_full_retrieval_shape` (function) component `ask_output_keeps_full_retrieval_shape [function]` (`667a24a4-1620-56a4-94cf-10fcd4994c62`) lines 634-676 [crates/gwiki/src/commands/ask.rs:634-676]
  - Signature: `fn ask_output_keeps_full_retrieval_shape() {`
  - Purpose: # Summary

This test verifies that `ask_output_from_search()` preserves the complete retrieval structure—including search results, source metadata, and semantic degradation warnings—when transforming a `SearchOutput` into an `AskOutput`. [crates/gwiki/src/commands/ask.rs:634-676]
- `ask_unified_graph_output_carries_code_citations_and_degradation` (function) component `ask_unified_graph_output_carries_code_citations_and_degradation [function]` (`0310bf76-3847-5c02-aaa3-b12186eede5c`) lines 679-730 [crates/gwiki/src/commands/ask.rs:679-730]
  - Signature: `fn ask_unified_graph_output_carries_code_citations_and_degradation() {`
  - Purpose: This test verifies that a unified graph search output correctly extracts code file citations from search results and properly propagates degradation status when the shared code graph source is unavailable. [crates/gwiki/src/commands/ask.rs:679-730]
- `ask_unified_graph_enrichment_uses_context_pack_code_edges_and_degrades` (function) component `ask_unified_graph_enrichment_uses_context_pack_code_edges_and_degrades [function]` (`5aadfa7d-9f29-5286-9987-99f2582c3546`) lines 733-835 [crates/gwiki/src/commands/ask.rs:733-835]
  - Signature: `fn ask_unified_graph_enrichment_uses_context_pack_code_edges_and_degrades() {`
  - Purpose: Constructs a SearchOutput enriched with WikiGraphFacts to establish graph-based semantic links between wiki documentation and code files, enabling unified graph enrichment of search results with code-to-documentation cross-references. [crates/gwiki/src/commands/ask.rs:733-835]
- `ask_unified_graph_model_unavailable_marks_degraded` (function) component `ask_unified_graph_model_unavailable_marks_degraded [function]` (`2502c0aa-8f2b-5460-a270-50d27a695900`) lines 838-856 [crates/gwiki/src/commands/ask.rs:838-856]
  - Signature: `fn ask_unified_graph_model_unavailable_marks_degraded() {`
  - Purpose: This function validates that `mark_ai_unavailable()` gracefully degrades a SearchOutput by setting its degraded flag to true, adding 'model_provider_unavailable' to degraded_sources, and 'ai_unavailable' to warnings. [crates/gwiki/src/commands/ask.rs:838-856]
- `llm_ai_off_is_invalid_input` (function) component `llm_ai_off_is_invalid_input [function]` (`0f732658-6a41-59c8-bf1b-b568f8141736`) lines 859-873 [crates/gwiki/src/commands/ask.rs:859-873]
  - Signature: `fn llm_ai_off_is_invalid_input() {`
  - Purpose: This test function verifies that executing an "ask" query with `AiRouting::Off` produces a `WikiError::InvalidInput` for the "ask" field before retrieval is attempted. [crates/gwiki/src/commands/ask.rs:859-873]

