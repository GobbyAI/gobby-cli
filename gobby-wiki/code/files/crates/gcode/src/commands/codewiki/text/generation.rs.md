---
title: crates/gcode/src/commands/codewiki/text/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/generation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

`crates/gcode/src/commands/codewiki/text/generation.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/generation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `resolve_text_generator` | function | This function resolves the AI context and routing configuration to optionally return a boxed static closure that handles text generation requests by routing them to either a daemon or direct endpoint with bounded retries, token constraints, and error handling. [crates/gcode/src/commands/codewiki/text/generation.rs:23-79] |
| `resolve_text_verifier` | function | The 'resolve_text_verifier' function resolves the AI routing context and configuration options to optionally return a boxed 'TextVerifier' closure that performs bounded-retry text generation through either a local daemon or direct API connection using specified verification profiles, models, and credentials. [crates/gcode/src/commands/codewiki/text/generation.rs:89-154] |
| `generate_with_bounded_retry` | function | This function executes a provided closure returning a 'Result<T, AiError>' and retries it with sleep backoffs defined by 'GENERATION_RETRY_BACKOFF' as long as the returned error satisfies the 'retryable_generation_error' predicate. [crates/gcode/src/commands/codewiki/text/generation.rs:159-173] |
| `retryable_generation_error` | function | The 'retryable_generation_error' function determines if a given 'AiError' is retryable, returning 'true' for transport failures, rate limits, or HTTP status codes of 500 and above, and 'false' for capability unavailability, configuration issues, or parse failures. [crates/gcode/src/commands/codewiki/text/generation.rs:175-183] |
| `resolve_ai_context` | function | This function establishes a read-only database connection to construct an AI configuration source from PostgreSQL and optional standalone configurations, then resolves and returns an 'AiContext' using the specified project ID and routing options. [crates/gcode/src/commands/codewiki/text/generation.rs:185-198] |
| `Generation` | type | Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:205-209] |
| `Generation::failed` | method | This crate-visible method checks whether the 'Generation' enum instance is the 'Failed' variant, returning 'true' if it matches and 'false' otherwise. [crates/gcode/src/commands/codewiki/text/generation.rs:212-214] |
| `Generation::unwrap_or_record` | method | The 'unwrap_or_record' method consumes a 'Generation' instance, returning its inner string on success or a fallback string when failed or skipped, while also mutating a 'degraded' boolean flag to 'true' in the case of failure. [crates/gcode/src/commands/codewiki/text/generation.rs:218-227] |
| `maybe_generate` | function | The 'maybe_generate' function conditionally executes an optional 'TextGenerator' using the provided prompt, system instructions, and prompt tier, returning a 'Generation' enum that indicates whether the generation was skipped, failed (including due to prompt echoing), or successfully completed with the generated text. [crates/gcode/src/commands/codewiki/text/generation.rs:230-244] |
| `is_prompt_echo` | function | The function 'is_prompt_echo' returns whether a trimmed text string starts with a prefix consisting of the first 'PROMPT_ECHO_PREFIX_CHARS' characters of a trimmed prompt, returning 'false' if the trimmed prompt contains fewer than that number of characters. [crates/gcode/src/commands/codewiki/text/generation.rs:253-263] |
| `clean_generated` | function | The function trims leading and trailing whitespace from the input string, returning 'Some' containing the trimmed string if it is not empty, and 'None' otherwise. [crates/gcode/src/commands/codewiki/text/generation.rs:265-268] |

