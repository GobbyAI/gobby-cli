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
  - 89-99
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/explainer.rs:24-26](crates/gwiki/src/explainer.rs#L24-L26), [crates/gwiki/src/explainer.rs:39-45](crates/gwiki/src/explainer.rs#L39-L45), [crates/gwiki/src/explainer.rs:49-53](crates/gwiki/src/explainer.rs#L49-L53), [crates/gwiki/src/explainer.rs:57-58](crates/gwiki/src/explainer.rs#L57-L58), [crates/gwiki/src/explainer.rs:64-74](crates/gwiki/src/explainer.rs#L64-L74), [crates/gwiki/src/explainer.rs:78-86](crates/gwiki/src/explainer.rs#L78-L86), [crates/gwiki/src/explainer.rs:89-99](crates/gwiki/src/explainer.rs#L89-L99), [crates/gwiki/src/explainer.rs:106-110](crates/gwiki/src/explainer.rs#L106-L110), [crates/gwiki/src/explainer.rs:114-119](crates/gwiki/src/explainer.rs#L114-L119), [crates/gwiki/src/explainer.rs:123-168](crates/gwiki/src/explainer.rs#L123-L168), [crates/gwiki/src/explainer.rs:172-200](crates/gwiki/src/explainer.rs#L172-L200), [crates/gwiki/src/explainer.rs:206-246](crates/gwiki/src/explainer.rs#L206-L246), [crates/gwiki/src/explainer.rs:248-253](crates/gwiki/src/explainer.rs#L248-L253), [crates/gwiki/src/explainer.rs:257-293](crates/gwiki/src/explainer.rs#L257-L293), [crates/gwiki/src/explainer.rs:297-312](crates/gwiki/src/explainer.rs#L297-L312), [crates/gwiki/src/explainer.rs:314-319](crates/gwiki/src/explainer.rs#L314-L319), [crates/gwiki/src/explainer.rs:322-330](crates/gwiki/src/explainer.rs#L322-L330), [crates/gwiki/src/explainer.rs:339-350](crates/gwiki/src/explainer.rs#L339-L350), [crates/gwiki/src/explainer.rs:352-358](crates/gwiki/src/explainer.rs#L352-L358), [crates/gwiki/src/explainer.rs:361-380](crates/gwiki/src/explainer.rs#L361-L380), [crates/gwiki/src/explainer.rs:383-390](crates/gwiki/src/explainer.rs#L383-L390), [crates/gwiki/src/explainer.rs:393-408](crates/gwiki/src/explainer.rs#L393-L408), [crates/gwiki/src/explainer.rs:411-428](crates/gwiki/src/explainer.rs#L411-L428), [crates/gwiki/src/explainer.rs:431-452](crates/gwiki/src/explainer.rs#L431-L452), [crates/gwiki/src/explainer.rs:455-478](crates/gwiki/src/explainer.rs#L455-L478), [crates/gwiki/src/explainer.rs:481-496](crates/gwiki/src/explainer.rs#L481-L496), [crates/gwiki/src/explainer.rs:499-522](crates/gwiki/src/explainer.rs#L499-L522), [crates/gwiki/src/explainer.rs:525-545](crates/gwiki/src/explainer.rs#L525-L545)

</details>

# crates/gwiki/src/explainer.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements bounded LLM-based explainer synthesis for compiled wiki articles: it builds a single prompt from accepted sources under a fixed token budget, sends it through a transport-agnostic generation interface, then grounds the result by validating citation markers against the source set before prose is accepted. The helpers handle token estimation, prompt assembly, source excerpt truncation and fallback selection, citation matching, and excerpt formatting, while the report and response types track generation outcomes. Tests cover prompt content, token limits, grounding behavior, fallback citations, and success/failure/skip paths so the explainer degrades cleanly to the deterministic skeleton when generation is unavailable or invalid.
[crates/gwiki/src/explainer.rs:24-26]
[crates/gwiki/src/explainer.rs:39-45]
[crates/gwiki/src/explainer.rs:49-53]
[crates/gwiki/src/explainer.rs:57-58]
[crates/gwiki/src/explainer.rs:64-74]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `estimate_tokens` | function | `pub fn estimate_tokens(chars: usize) -> usize {` | `estimate_tokens [function]` | `c55bd3df-496c-585c-ae5c-d576e1617791` | 24-26 [crates/gwiki/src/explainer.rs:24-26] | Indexed function `estimate_tokens` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:24-26] |
| `ExplainerPrompt` | class | `pub struct ExplainerPrompt {` | `ExplainerPrompt [class]` | `8951482d-dfa2-5543-b7f0-9f0cabe155a3` | 39-45 [crates/gwiki/src/explainer.rs:39-45] | Indexed class `ExplainerPrompt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:39-45] |
| `ExplainerResponse` | class | `pub struct ExplainerResponse {` | `ExplainerResponse [class]` | `8ee5b6c3-c2ba-5b78-a098-253c5c7591dd` | 49-53 [crates/gwiki/src/explainer.rs:49-53] | Indexed class `ExplainerResponse` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:49-53] |
| `ExplainerGenerator` | type | `pub type ExplainerGenerator<'a> =` | `ExplainerGenerator [type]` | `2970a559-dc19-544d-81f0-cecfad60ab61` | 57-58 [crates/gwiki/src/explainer.rs:57-58] | Indexed type `ExplainerGenerator` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:57-58] |
| `ExplainerGeneration` | type | `pub enum ExplainerGeneration {` | `ExplainerGeneration [type]` | `efd7a352-609d-5c4f-b6bc-d9a884309c10` | 64-74 [crates/gwiki/src/explainer.rs:64-74] | Indexed type `ExplainerGeneration` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:64-74] |
| `ExplainerReport` | class | `pub struct ExplainerReport {` | `ExplainerReport [class]` | `1875f161-a9ed-5e8e-86ba-44ef1192e24e` | 78-86 [crates/gwiki/src/explainer.rs:78-86] | Indexed class `ExplainerReport` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:78-86] |
| `ExplainerReport::skipped` | method | `pub fn skipped() -> Self {` | `ExplainerReport::skipped [method]` | `cdc72d7f-deea-599b-b951-f9df24cc7bec` | 89-99 [crates/gwiki/src/explainer.rs:89-99] | Indexed method `ExplainerReport::skipped` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:89-99] |
| `CitationTarget` | class | `pub struct CitationTarget {` | `CitationTarget [class]` | `f4837245-ec0d-5467-b1f0-0f3dc7730901` | 106-110 [crates/gwiki/src/explainer.rs:106-110] | Indexed class `CitationTarget` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:106-110] |
| `GroundedExplainer` | class | `pub struct GroundedExplainer {` | `GroundedExplainer [class]` | `cc6b4b34-ba5e-50cc-b62f-e71a9e612b91` | 114-119 [crates/gwiki/src/explainer.rs:114-119] | Indexed class `GroundedExplainer` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:114-119] |
| `build_explainer_prompt` | function | `pub fn build_explainer_prompt(vault_root: &Path, input: &SynthesisInput) -> ExplainerPrompt {` | `build_explainer_prompt [function]` | `a6335756-1ba7-53d7-aa9b-32d774dc4d8c` | 123-168 [crates/gwiki/src/explainer.rs:123-168] | Indexed function `build_explainer_prompt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:123-168] |
| `generate_explainer` | function | `pub fn generate_explainer(` | `generate_explainer [function]` | `cf7b04ad-01b8-5d2c-b34c-40ace2e4d4a7` | 172-200 [crates/gwiki/src/explainer.rs:172-200] | Indexed function `generate_explainer` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:172-200] |
| `ground_explainer` | function | `pub fn ground_explainer(body: &str, targets: &[CitationTarget]) -> GroundedExplainer {` | `ground_explainer [function]` | `54a07ce9-8038-53ee-b212-feb34092d8b9` | 206-246 [crates/gwiki/src/explainer.rs:206-246] | Indexed function `ground_explainer` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:206-246] |
| `citation_key_matches` | function | `fn citation_key_matches(target_key: &str, cited: &str) -> bool {` | `citation_key_matches [function]` | `02983ae7-9b7f-5577-92a1-2fbf6a96bb4e` | 248-253 [crates/gwiki/src/explainer.rs:248-253] | Indexed function `citation_key_matches` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:248-253] |
| `apply_section_fallbacks` | function | `fn apply_section_fallbacks(body: &str, targets: &[CitationTarget]) -> (String, usize) {` | `apply_section_fallbacks [function]` | `e7449041-3911-55b9-9b75-aa1cb33517a8` | 257-293 [crates/gwiki/src/explainer.rs:257-293] | Indexed function `apply_section_fallbacks` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:257-293] |
| `best_fallback_target` | function | `fn best_fallback_target<'a>(` | `best_fallback_target [function]` | `386b319a-db86-5fd4-b381-2cd0f7623619` | 297-312 [crates/gwiki/src/explainer.rs:297-312] | Indexed function `best_fallback_target` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:297-312] |
| `significant_tokens` | function | `fn significant_tokens(text: &str) -> std::collections::BTreeSet<String> {` | `significant_tokens [function]` | `441e485c-1811-5d7b-b69a-6f1ef0e7f544` | 314-319 [crates/gwiki/src/explainer.rs:314-319] | Indexed function `significant_tokens` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:314-319] |
| `bounded_excerpt` | function | `fn bounded_excerpt(text: &str, max_chars: usize) -> String {` | `bounded_excerpt [function]` | `0e967952-bb98-5fa2-a5fe-3626d5726542` | 322-330 [crates/gwiki/src/explainer.rs:322-330] | Indexed function `bounded_excerpt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:322-330] |
| `input_with_sources` | function | `fn input_with_sources(sources: Vec<SynthesisSource>) -> SynthesisInput {` | `input_with_sources [function]` | `0c3d694c-c456-5110-98d0-71e5cf71ad96` | 339-350 [crates/gwiki/src/explainer.rs:339-350] | Indexed function `input_with_sources` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:339-350] |
| `source` | function | `fn source(title: &str, path: &str, chunk: &str) -> SynthesisSource {` | `source [function]` | `ea310cf2-a7d4-5ad3-a99f-33c583e7f2d3` | 352-358 [crates/gwiki/src/explainer.rs:352-358] | Indexed function `source` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:352-358] |
| `explainer_prompt_lists_sections_and_cited_source_paths` | function | `fn explainer_prompt_lists_sections_and_cited_source_paths() {` | `explainer_prompt_lists_sections_and_cited_source_paths [function]` | `09599bba-0e42-5331-ae19-82e8c1bc5a55` | 361-380 [crates/gwiki/src/explainer.rs:361-380] | Indexed function `explainer_prompt_lists_sections_and_cited_source_paths` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:361-380] |
| `explainer_prompt_without_outline_requests_an_overview_section` | function | `fn explainer_prompt_without_outline_requests_an_overview_section() {` | `explainer_prompt_without_outline_requests_an_overview_section [function]` | `dfa3d4eb-c087-57dc-9ea2-76f1c189d3ec` | 383-390 [crates/gwiki/src/explainer.rs:383-390] | Indexed function `explainer_prompt_without_outline_requests_an_overview_section` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:383-390] |
| `explainer_prompt_never_exceeds_token_budget` | function | `fn explainer_prompt_never_exceeds_token_budget() {` | `explainer_prompt_never_exceeds_token_budget [function]` | `30368c09-f93d-5ba4-8af2-593f6c74c68a` | 393-408 [crates/gwiki/src/explainer.rs:393-408] | Indexed function `explainer_prompt_never_exceeds_token_budget` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:393-408] |
| `explainer_prompt_bounds_each_source_excerpt` | function | `fn explainer_prompt_bounds_each_source_excerpt() {` | `explainer_prompt_bounds_each_source_excerpt [function]` | `2371e3d0-3944-5ed3-92a4-2076f603bf11` | 411-428 [crates/gwiki/src/explainer.rs:411-428] | Indexed function `explainer_prompt_bounds_each_source_excerpt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:411-428] |
| `grounding_rewrites_valid_markers_and_strips_invented_ones` | function | `fn grounding_rewrites_valid_markers_and_strips_invented_ones() {` | `grounding_rewrites_valid_markers_and_strips_invented_ones [function]` | `b75b3055-24a7-56b5-b6de-0882226db2b4` | 431-452 [crates/gwiki/src/explainer.rs:431-452] | Indexed function `grounding_rewrites_valid_markers_and_strips_invented_ones` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:431-452] |
| `grounding_appends_fallback_citation_to_uncited_sections` | function | `fn grounding_appends_fallback_citation_to_uncited_sections() {` | `grounding_appends_fallback_citation_to_uncited_sections [function]` | `ba5e34bf-4cfd-58c4-a96b-1a63492968a8` | 455-478 [crates/gwiki/src/explainer.rs:455-478] | Indexed function `grounding_appends_fallback_citation_to_uncited_sections` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:455-478] |
| `generation_without_sources_or_generator_is_skipped_not_degraded` | function | `fn generation_without_sources_or_generator_is_skipped_not_degraded() {` | `generation_without_sources_or_generator_is_skipped_not_degraded [function]` | `12d899ef-be0b-56a1-8025-4574ce6c5008` | 481-496 [crates/gwiki/src/explainer.rs:481-496] | Indexed function `generation_without_sources_or_generator_is_skipped_not_degraded` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:481-496] |
| `generation_failure_and_empty_output_mark_failed` | function | `fn generation_failure_and_empty_output_mark_failed() {` | `generation_failure_and_empty_output_mark_failed [function]` | `c9f1a2a9-3721-5904-9393-0ac206b852be` | 499-522 [crates/gwiki/src/explainer.rs:499-522] | Indexed function `generation_failure_and_empty_output_mark_failed` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:499-522] |
| `generation_success_trims_and_carries_route_and_model` | function | `fn generation_success_trims_and_carries_route_and_model() {` | `generation_success_trims_and_carries_route_and_model [function]` | `dd6e2c36-cf6a-5235-8559-455b21081a09` | 525-545 [crates/gwiki/src/explainer.rs:525-545] | Indexed function `generation_success_trims_and_carries_route_and_model` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:525-545] |
