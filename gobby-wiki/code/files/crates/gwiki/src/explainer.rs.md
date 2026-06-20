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

`crates/gwiki/src/explainer.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `estimate_tokens` | function | The 'estimate_tokens' function estimates the token count of a given text by performing ceiling division on the input character count by four. [crates/gwiki/src/explainer.rs:24-26] |
| `ExplainerPrompt` | class | 'ExplainerPrompt' is a Rust struct that encapsulates system and user prompt strings, an estimated token count, and a count of source documents omitted due to token budget limitations. [crates/gwiki/src/explainer.rs:39-45] |
| `ExplainerResponse` | class | The 'ExplainerResponse' struct is a public Rust data structure that encapsulates a response's generated 'text' string, an optional 'model' identifier, and a static string slice representing the route. [crates/gwiki/src/explainer.rs:49-53] |
| `ExplainerGenerator` | type | Indexed type `ExplainerGenerator` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:57-58] |
| `ExplainerGeneration` | type | Indexed type `ExplainerGeneration` in `crates/gwiki/src/explainer.rs`. [crates/gwiki/src/explainer.rs:64-74] |
| `ExplainerReport` | class | The 'ExplainerReport' struct is a Rust data structure designed to aggregate execution metadata, model routing details, error logs, and quantitative citation processing metrics for an explanation-generation process. [crates/gwiki/src/explainer.rs:78-86] |
| `ExplainerReport::skipped` | method | Constructs and returns an instance of the struct with its 'status' field initialized to '"skipped"', optional fields set to 'None', and citation and fallback counters set to zero. [crates/gwiki/src/explainer.rs:89-99] |
| `CitationTarget` | class | The 'CitationTarget' struct is a public Rust data structure that represents a citation reference, containing public string fields for its identifier key, destination hyperlink, and source corpus. [crates/gwiki/src/explainer.rs:106-110] |
| `GroundedExplainer` | class | 'GroundedExplainer' is a data structure representing an explanation's body text along with metrics tracking the number of citations kept, citations stripped, and fallback sections utilized. [crates/gwiki/src/explainer.rs:114-119] |
| `build_explainer_prompt` | function | The 'build_explainer_prompt' function constructs an 'ExplainerPrompt' by formatting a user prompt with the specified topic, outline sections, and a token-budget-bounded list of relative source excerpts, while tracking the number of sources omitted due to the budget constraint. [crates/gwiki/src/explainer.rs:123-168] |
| `generate_explainer` | function | The 'generate_explainer' function executes an optional generator with a given prompt to return an 'ExplainerGeneration' outcome, skipping the process if the generator is absent or there are no accepted sources, and otherwise handling the resulting success, failure, or empty-text validation states. [crates/gwiki/src/explainer.rs:172-200] |
| `ground_explainer` | function | The 'ground_explainer' function parses citation markup formatted as '[source:<key>]' within a text body, replacing matched keys with links from a list of citation targets or stripping them if unmatched, before applying fallback sections and returning a 'GroundedExplainer' structure containing the resolved text and processing statistics. [crates/gwiki/src/explainer.rs:206-246] |
| `citation_key_matches` | function | The function 'citation_key_matches' returns 'true' if the 'target_key' string is equal to the 'cited' string, either exactly or after stripping a '.md' suffix from 'target_key'. [crates/gwiki/src/explainer.rs:248-253] |
| `apply_section_fallbacks` | function | This function parses a markdown string into header-defined sections and appends a formatted fallback source citation link to any non-empty section that lacks an existing citation, returning the modified body and the count of sections where a fallback was applied. [crates/gwiki/src/explainer.rs:257-293] |
| `best_fallback_target` | function | The function returns the 'CitationTarget' from a slice that has the greatest overlap of significant tokens with the input prose, breaking ties by preferring the earliest occurring target in the slice. [crates/gwiki/src/explainer.rs:297-312] |
| `significant_tokens` | function | This function splits the input string on non-alphanumeric characters, filters out tokens with fewer than three characters, converts the remaining tokens to lowercase, and returns them as a sorted, unique set of strings. [crates/gwiki/src/explainer.rs:314-319] |
| `bounded_excerpt` | function | The 'bounded_excerpt' function trims leading and trailing whitespace from an input string slice and returns it, truncating the result to a specified maximum number of characters and appending an ellipsis ('…') if the trimmed string exceeds that length. [crates/gwiki/src/explainer.rs:322-330] |
| `input_with_sources` | function | The 'input_with_sources' function instantiates and returns a 'SynthesisInput' struct initialized with predefined values for its metadata, topic, outline, and validation fields, while populating its 'accepted_sources' field with the provided vector of 'SynthesisSource' structures. [crates/gwiki/src/explainer.rs:339-350] |
| `source` | function | The 'source' function constructs and returns a 'SynthesisSource' instance by converting the provided string slices into a 'String' for the title, a 'PathBuf' for the path, and a single-element 'Vec<String>' containing the chunk. [crates/gwiki/src/explainer.rs:352-358] |

_Verified by 9 in-file unit tests._

