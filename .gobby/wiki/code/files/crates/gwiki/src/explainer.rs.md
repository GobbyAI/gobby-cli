---
title: crates/gwiki/src/explainer.rs
type: code_file
provenance:
- file: crates/gwiki/src/explainer.rs
  ranges:
  - 24-26
  - 39-45
  - 49-53
  - 57-58
  - 64-74
  - 78-86
  - 88-100
  - 106-110
  - 114-119
  - 123-168
  - 172-200
  - 206-246
  - 248-253
  - 257-293
  - 297-312
  - 314-319
  - 322-330
  - 339-350
  - 352-358
  - 361-380
  - 383-390
  - 393-408
  - 411-428
  - 431-452
  - 455-478
  - 481-496
  - 499-522
  - 525-545
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/explainer.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements bounded LLM explainer synthesis for compiled wiki articles. It defines the prompt and response data types, a token-budgeted prompt builder that formats the topic, outline sections, and accepted source excerpts, and a generation seam that either skips synthesis, returns a trimmed model response, or marks failure. After generation, it grounds the prose by validating and rewriting `[source: ...]` markers against accepted sources, stripping invented citations, and adding section-level fallback source notes when needed. Supporting helpers handle token estimation, excerpt truncation, citation matching, fallback target selection, and source-token heuristics.
[crates/gwiki/src/explainer.rs:24-26]
[crates/gwiki/src/explainer.rs:39-45]
[crates/gwiki/src/explainer.rs:49-53]
[crates/gwiki/src/explainer.rs:57-58]
[crates/gwiki/src/explainer.rs:64-74]

## API Symbols

- `estimate_tokens` (function) component `estimate_tokens [function]` (`c55bd3df-496c-585c-ae5c-d576e1617791`) lines 24-26 [crates/gwiki/src/explainer.rs:24-26]
  - Signature: `pub fn estimate_tokens(chars: usize) -> usize {`
  - Purpose: Returns the token estimate for a character count by rounding up 'chars / 4' using integer ceiling division. [crates/gwiki/src/explainer.rs:24-26]
- `ExplainerPrompt` (class) component `ExplainerPrompt [class]` (`8951482d-dfa2-5543-b7f0-9f0cabe155a3`) lines 39-45 [crates/gwiki/src/explainer.rs:39-45]
  - Signature: `pub struct ExplainerPrompt {`
  - Purpose: 'ExplainerPrompt' is a Rust data holder for an explainer prompt, storing a static system prompt, a dynamic user prompt, an estimated token count, and a count of accepted sources omitted due to token-budget truncation. [crates/gwiki/src/explainer.rs:39-45]
- `ExplainerResponse` (class) component `ExplainerResponse [class]` (`8ee5b6c3-c2ba-5b78-a098-253c5c7591dd`) lines 49-53 [crates/gwiki/src/explainer.rs:49-53]
  - Signature: `pub struct ExplainerResponse {`
  - Purpose: 'ExplainerResponse' is a response struct that carries generated explanation text, an optional model identifier, and a static route string. [crates/gwiki/src/explainer.rs:49-53]
- `ExplainerGenerator` (type) component `ExplainerGenerator [type]` (`2970a559-dc19-544d-81f0-cecfad60ab61`) lines 57-58 [crates/gwiki/src/explainer.rs:57-58]
  - Signature: `pub type ExplainerGenerator<'a> =`
  - Purpose: Indexed type `ExplainerGenerator` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:57-58]
- `ExplainerGeneration` (type) component `ExplainerGeneration [type]` (`efd7a352-609d-5c4f-b6bc-d9a884309c10`) lines 64-74 [crates/gwiki/src/explainer.rs:64-74]
  - Signature: `pub enum ExplainerGeneration {`
  - Purpose: Indexed type `ExplainerGeneration` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:64-74]
- `ExplainerReport` (class) component `ExplainerReport [class]` (`1875f161-a9ed-5e8e-86ba-44ef1192e24e`) lines 78-86 [crates/gwiki/src/explainer.rs:78-86]
  - Signature: `pub struct ExplainerReport {`
  - Purpose: 'ExplainerReport' is a summary record of an explanation run, capturing the outcome status, optional route/model/error metadata, and counts for kept vs. stripped citations plus fallback sections. [crates/gwiki/src/explainer.rs:78-86]
- `ExplainerReport` (class) component `ExplainerReport [class]` (`479d7eee-ea10-5083-ba7f-ef2c9248392e`) lines 88-100 [crates/gwiki/src/explainer.rs:88-100]
  - Signature: `impl ExplainerReport {`
  - Purpose: 'ExplainerReport' is a report constructor that initializes a “skipped” state with no route, model, or error and zeroed citation/fallback counters. [crates/gwiki/src/explainer.rs:88-100]
- `ExplainerReport.skipped` (method) component `ExplainerReport.skipped [method]` (`cdc72d7f-deea-599b-b951-f9df24cc7bec`) lines 89-99 [crates/gwiki/src/explainer.rs:89-99]
  - Signature: `pub fn skipped() -> Self {`
  - Purpose: Constructs and returns a new 'Self' instance representing a skipped result, with 'status' set to '"skipped"' and all optional fields unset and counters initialized to zero. [crates/gwiki/src/explainer.rs:89-99]
- `CitationTarget` (class) component `CitationTarget [class]` (`f4837245-ec0d-5467-b1f0-0f3dc7730901`) lines 106-110 [crates/gwiki/src/explainer.rs:106-110]
  - Signature: `pub struct CitationTarget {`
  - Purpose: 'CitationTarget' is a Rust struct that identifies a citation target by storing a 'key', 'link', and 'corpus' as owned 'String' fields. [crates/gwiki/src/explainer.rs:106-110]
- `GroundedExplainer` (class) component `GroundedExplainer [class]` (`cc6b4b34-ba5e-50cc-b62f-e71a9e612b91`) lines 114-119 [crates/gwiki/src/explainer.rs:114-119]
  - Signature: `pub struct GroundedExplainer {`
  - Purpose: 'GroundedExplainer' is a struct that captures an explainer body plus metrics for how many citations were retained, stripped, and how many fallback sections were used during grounding processing. [crates/gwiki/src/explainer.rs:114-119]
- `build_explainer_prompt` (function) component `build_explainer_prompt [function]` (`a6335756-1ba7-53d7-aa9b-32d774dc4d8c`) lines 123-168 [crates/gwiki/src/explainer.rs:123-168]
  - Signature: `pub fn build_explainer_prompt(vault_root: &Path, input: &SynthesisInput) -> ExplainerPrompt {`
  - Purpose: Constructs an 'ExplainerPrompt' by assembling a user prompt from the topic, required section headings derived from the outline or a default 'Overview', and numbered source excerpts keyed by vault-relative paths, stopping before a token budget would be exceeded and returning the system prompt, estimated token count, and number of truncated sources. [crates/gwiki/src/explainer.rs:123-168]
- `generate_explainer` (function) component `generate_explainer [function]` (`cf7b04ad-01b8-5d2c-b34c-40ace2e4d4a7`) lines 172-200 [crates/gwiki/src/explainer.rs:172-200]
  - Signature: `pub fn generate_explainer(`
  - Purpose: Returns 'Skipped' when no explainer generator is provided or 'input.accepted_sources' is empty, otherwise invokes the generator and returns 'Generated' with the trimmed non-empty response text and metadata, or 'Failed' if the call errors or yields an empty body. [crates/gwiki/src/explainer.rs:172-200]
- `ground_explainer` (function) component `ground_explainer [function]` (`54a07ce9-8038-53ee-b212-feb34092d8b9`) lines 206-246 [crates/gwiki/src/explainer.rs:206-246]
  - Signature: `pub fn ground_explainer(body: &str, targets: &[CitationTarget]) -> GroundedExplainer {`
  - Purpose: Parses 'body' for '[source:...]' citation markers, replaces matched markers with the corresponding target links while stripping unmatched markers and tracking kept/stripped counts, then applies section fallbacks and returns a 'GroundedExplainer' containing the transformed body and fallback metadata. [crates/gwiki/src/explainer.rs:206-246]
- `citation_key_matches` (function) component `citation_key_matches [function]` (`02983ae7-9b7f-5577-92a1-2fbf6a96bb4e`) lines 248-253 [crates/gwiki/src/explainer.rs:248-253]
  - Signature: `fn citation_key_matches(target_key: &str, cited: &str) -> bool {`
  - Purpose: Returns 'true' when 'target_key' exactly equals 'cited', or when 'target_key' ends with '.md' and its suffix-stripped form equals 'cited'. [crates/gwiki/src/explainer.rs:248-253]
- `apply_section_fallbacks` (function) component `apply_section_fallbacks [function]` (`e7449041-3911-55b9-9b75-aa1cb33517a8`) lines 257-293 [crates/gwiki/src/explainer.rs:257-293]
  - Signature: `fn apply_section_fallbacks(body: &str, targets: &[CitationTarget]) -> (String, usize) {`
  - Purpose: 'apply_section_fallbacks' splits the body into '## '-headed sections, and for each section lacking any target citation link but containing nonempty prose, appends an italicized '_Source: ..._' fallback citation chosen by 'best_fallback_target', returning the rewritten body and the number of sections augmented. [crates/gwiki/src/explainer.rs:257-293]
- `best_fallback_target` (function) component `best_fallback_target [function]` (`386b319a-db86-5fd4-b381-2cd0f7623619`) lines 297-312 [crates/gwiki/src/explainer.rs:297-312]
  - Signature: `fn best_fallback_target<'a>(`
  - Purpose: Selects and returns the 'CitationTarget' whose corpus shares the most significant-token overlap with the given prose, breaking ties in favor of the later target in the slice, or 'None' if the slice is empty. [crates/gwiki/src/explainer.rs:297-312]
- `significant_tokens` (function) component `significant_tokens [function]` (`441e485c-1811-5d7b-b69a-6f1ef0e7f544`) lines 314-319 [crates/gwiki/src/explainer.rs:314-319]
  - Signature: `fn significant_tokens(text: &str) -> std::collections::BTreeSet<String> {`
  - Purpose: Returns a 'BTreeSet<String>' of all distinct alphanumeric substrings in 'text' with length at least 3, normalized to lowercase and split on any non-alphanumeric character. [crates/gwiki/src/explainer.rs:314-319]
- `bounded_excerpt` (function) component `bounded_excerpt [function]` (`0e967952-bb98-5fa2-a5fe-3626d5726542`) lines 322-330 [crates/gwiki/src/explainer.rs:322-330]
  - Signature: `fn bounded_excerpt(text: &str, max_chars: usize) -> String {`
  - Purpose: Returns the trimmed input string unchanged when its character count is at most 'max_chars', otherwise returns the first 'max_chars' characters followed by an ellipsis character ('…'). [crates/gwiki/src/explainer.rs:322-330]
- `input_with_sources` (function) component `input_with_sources [function]` (`0c3d694c-c456-5110-98d0-71e5cf71ad96`) lines 339-350 [crates/gwiki/src/explainer.rs:339-350]
  - Signature: `fn input_with_sources(sources: Vec<SynthesisSource>) -> SynthesisInput {`
  - Purpose: Constructs and returns a 'SynthesisInput' for the “Compile Behavior” topic with hardcoded 'handoff_id', 'target_kind', outline, and empty citation/conflict/evidence lists, while passing through the provided 'sources' as 'accepted_sources'. [crates/gwiki/src/explainer.rs:339-350]
- `source` (function) component `source [function]` (`ea310cf2-a7d4-5ad3-a99f-33c583e7f2d3`) lines 352-358 [crates/gwiki/src/explainer.rs:352-358]
  - Signature: `fn source(title: &str, path: &str, chunk: &str) -> SynthesisSource {`
  - Purpose: Constructs a 'SynthesisSource' by cloning 'title' into a 'String', converting 'path' into a 'PathBuf', and storing 'chunk' as the sole element of the 'chunks' vector. [crates/gwiki/src/explainer.rs:352-358]
- `explainer_prompt_lists_sections_and_cited_source_paths` (function) component `explainer_prompt_lists_sections_and_cited_source_paths [function]` (`09599bba-0e42-5331-ae19-82e8c1bc5a55`) lines 361-380 [crates/gwiki/src/explainer.rs:361-380]
  - Signature: `fn explainer_prompt_lists_sections_and_cited_source_paths() {`
  - Purpose: Builds an explainer prompt from a sourced input and verifies that it preserves the system prompt, includes the topic, section list, cited source path, source text, a positive token estimate, and no truncated sources. [crates/gwiki/src/explainer.rs:361-380]
- `explainer_prompt_without_outline_requests_an_overview_section` (function) component `explainer_prompt_without_outline_requests_an_overview_section [function]` (`dfa3d4eb-c087-57dc-9ea2-76f1c189d3ec`) lines 383-390 [crates/gwiki/src/explainer.rs:383-390]
  - Signature: `fn explainer_prompt_without_outline_requests_an_overview_section() {`
  - Purpose: Verifies that when the input outline is cleared, 'build_explainer_prompt' still includes an '- Overview' section in the user prompt and notes '- No accepted sources.' [crates/gwiki/src/explainer.rs:383-390]
- `explainer_prompt_never_exceeds_token_budget` (function) component `explainer_prompt_never_exceeds_token_budget [function]` (`30368c09-f93d-5ba4-8af2-593f6c74c68a`) lines 393-408 [crates/gwiki/src/explainer.rs:393-408]
  - Signature: `fn explainer_prompt_never_exceeds_token_budget() {`
  - Purpose: Verifies that 'build_explainer_prompt' respects 'EXPLAINER_PROMPT_TOKEN_BUDGET' by constructing an oversized source set and asserting the resulting prompt is token-limited and reports truncated sources. [crates/gwiki/src/explainer.rs:393-408]
- `explainer_prompt_bounds_each_source_excerpt` (function) component `explainer_prompt_bounds_each_source_excerpt [function]` (`2371e3d0-3944-5ed3-92a4-2076f603bf11`) lines 411-428 [crates/gwiki/src/explainer.rs:411-428]
  - Signature: `fn explainer_prompt_bounds_each_source_excerpt() {`
  - Purpose: Verifies that 'build_explainer_prompt' truncates each oversized source excerpt to 'EXPLAINER_SOURCE_EXCERPT_MAX_CHARS' characters plus a trailing ellipsis in the generated user prompt. [crates/gwiki/src/explainer.rs:411-428]
- `grounding_rewrites_valid_markers_and_strips_invented_ones` (function) component `grounding_rewrites_valid_markers_and_strips_invented_ones [function]` (`b75b3055-24a7-56b5-b6de-0882226db2b4`) lines 431-452 [crates/gwiki/src/explainer.rs:431-452]
  - Signature: `fn grounding_rewrites_valid_markers_and_strips_invented_ones() {`
  - Purpose: Verifies that 'ground_explainer' rewrites a valid source marker to the target citation link while stripping an invented source marker, leaving one citation kept, one stripped, and no fallback sections. [crates/gwiki/src/explainer.rs:431-452]
- `grounding_appends_fallback_citation_to_uncited_sections` (function) component `grounding_appends_fallback_citation_to_uncited_sections [function]` (`ba5e34bf-4cfd-58c4-a96b-1a63492968a8`) lines 455-478 [crates/gwiki/src/explainer.rs:455-478]
  - Signature: `fn grounding_appends_fallback_citation_to_uncited_sections() {`
  - Purpose: Verifies that 'ground_explainer' adds a fallback source citation to an uncited section by using the last matching target and increments 'fallback_sections' to '1'. [crates/gwiki/src/explainer.rs:455-478]
- `generation_without_sources_or_generator_is_skipped_not_degraded` (function) component `generation_without_sources_or_generator_is_skipped_not_degraded [function]` (`12d899ef-be0b-56a1-8025-4574ce6c5008`) lines 481-496 [crates/gwiki/src/explainer.rs:481-496]
  - Signature: `fn generation_without_sources_or_generator_is_skipped_not_degraded() {`
  - Purpose: Verifies that 'generate_explainer' returns 'ExplainerGeneration::Skipped' when there are no accepted sources, both when a generator is provided and when 'None' is passed, and that it does not invoke the generator in that case. [crates/gwiki/src/explainer.rs:481-496]
- `generation_failure_and_empty_output_mark_failed` (function) component `generation_failure_and_empty_output_mark_failed [function]` (`c9f1a2a9-3721-5904-9393-0ac206b852be`) lines 499-522 [crates/gwiki/src/explainer.rs:499-522]
  - Signature: `fn generation_failure_and_empty_output_mark_failed() {`
  - Purpose: Verifies that 'generate_explainer' returns 'ExplainerGeneration::Failed' both when the generation callback errors and when it succeeds with only whitespace output. [crates/gwiki/src/explainer.rs:499-522]
- `generation_success_trims_and_carries_route_and_model` (function) component `generation_success_trims_and_carries_route_and_model [function]` (`dd6e2c36-cf6a-5235-8559-455b21081a09`) lines 525-545 [crates/gwiki/src/explainer.rs:525-545]
  - Signature: `fn generation_success_trims_and_carries_route_and_model() {`
  - Purpose: Verifies that 'generate_explainer' trims leading whitespace from generated text while preserving the returned 'model' and 'route' values in the 'ExplainerGeneration::Generated' result. [crates/gwiki/src/explainer.rs:525-545]

