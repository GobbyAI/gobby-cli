---
title: crates/gwiki/src/explainer.rs
type: code_file
provenance:
- file: crates/gwiki/src/explainer.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/explainer.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/explainer.rs` exposes 28 indexed API symbols.

## How it fits

`crates/gwiki/src/explainer.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `estimate_tokens` | function | Indexed function `estimate_tokens` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:24-26] |
| `ExplainerPrompt` | class | Indexed class `ExplainerPrompt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:39-45] |
| `ExplainerResponse` | class | Indexed class `ExplainerResponse` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:49-53] |
| `ExplainerGenerator` | type | Indexed type `ExplainerGenerator` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:57-58] |
| `ExplainerGeneration` | type | Indexed type `ExplainerGeneration` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:64-74] |
| `ExplainerReport` | class | Indexed class `ExplainerReport` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:78-86] |
| `ExplainerReport::skipped` | method | Indexed method `ExplainerReport::skipped` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:89-99] |
| `CitationTarget` | class | Indexed class `CitationTarget` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:106-110] |
| `GroundedExplainer` | class | Indexed class `GroundedExplainer` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:114-119] |
| `build_explainer_prompt` | function | Indexed function `build_explainer_prompt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:123-168] |
| `generate_explainer` | function | Indexed function `generate_explainer` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:172-200] |
| `ground_explainer` | function | Indexed function `ground_explainer` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:206-246] |
| `citation_key_matches` | function | Indexed function `citation_key_matches` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:248-253] |
| `apply_section_fallbacks` | function | Indexed function `apply_section_fallbacks` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:257-293] |
| `best_fallback_target` | function | Indexed function `best_fallback_target` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:297-312] |
| `significant_tokens` | function | Indexed function `significant_tokens` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:314-319] |
| `bounded_excerpt` | function | Indexed function `bounded_excerpt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:322-330] |
| `input_with_sources` | function | Indexed function `input_with_sources` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:339-350] |
| `source` | function | Indexed function `source` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:352-358] |
| `explainer_prompt_lists_sections_and_cited_source_paths` | function | Indexed function `explainer_prompt_lists_sections_and_cited_source_paths` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:361-380] |
| `explainer_prompt_without_outline_requests_an_overview_section` | function | Indexed function `explainer_prompt_without_outline_requests_an_overview_section` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:383-390] |
| `explainer_prompt_never_exceeds_token_budget` | function | Indexed function `explainer_prompt_never_exceeds_token_budget` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:393-408] |
| `explainer_prompt_bounds_each_source_excerpt` | function | Indexed function `explainer_prompt_bounds_each_source_excerpt` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:411-428] |
| `grounding_rewrites_valid_markers_and_strips_invented_ones` | function | Indexed function `grounding_rewrites_valid_markers_and_strips_invented_ones` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:431-452] |
| `grounding_appends_fallback_citation_to_uncited_sections` | function | Indexed function `grounding_appends_fallback_citation_to_uncited_sections` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:455-478] |
| `generation_without_sources_or_generator_is_skipped_not_degraded` | function | Indexed function `generation_without_sources_or_generator_is_skipped_not_degraded` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:481-496] |
| `generation_failure_and_empty_output_mark_failed` | function | Indexed function `generation_failure_and_empty_output_mark_failed` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:499-522] |
| `generation_success_trims_and_carries_route_and_model` | function | Indexed function `generation_success_trims_and_carries_route_and_model` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:525-545] |

