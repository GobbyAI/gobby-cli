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

`crates/gcode/src/commands/codewiki/text/generation.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/generation.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `writer_candidate_chain` | function | This function returns a vector of two hardcoded 'FeatureCandidate' instances: "claude/opus" with "high" reasoning effort and "codex/gpt-5.5" with "xhigh" reasoning effort. [crates/gcode/src/commands/codewiki/text/generation.rs:28-39] |
| `resolve_text_generator` | function | # Summary Returns an optional boxed text generator that routes prompts to configured AI models with tier-based selection (Opus for aggregate, Sonnet for modules) and bounded retry logic based on routing configuration. [crates/gcode/src/commands/codewiki/text/generation.rs:47-124] |
| `resolve_text_verifier` | function | # Summary 'resolve_text_verifier' constructs and returns an optional boxed closure that generates text completions via AI routing (daemon or direct mode) using merged verification configuration (profile, model, API key) from the provided options and context bindings. [crates/gcode/src/commands/codewiki/text/generation.rs:134-199] |
| `generate_with_bounded_retry` | function | Executes a provided closure with bounded-retry semantics using predefined backoff intervals, retrying only on retriable AI generation errors. [crates/gcode/src/commands/codewiki/text/generation.rs:204-218] |
| `retryable_generation_error` | function | This function determines whether an 'AiError' is retryable by returning 'true' for transient failures (transport failures, rate limiting, or HTTP 5xx status codes) and 'false' for permanent errors (unavailable capabilities, misconfiguration, or parse failures). [crates/gcode/src/commands/codewiki/text/generation.rs:220-228] |
| `resolve_ai_context` | function | This function resolves an AI context by combining PostgreSQL and optional standalone configuration sources while applying an optional routing override. [crates/gcode/src/commands/codewiki/text/generation.rs:230-243] |
| `Generation` | type | Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:250-254] |
| `Generation::failed` | method | Returns 'true' if 'self' is the 'Generation::Failed' variant; otherwise returns 'false'. [crates/gcode/src/commands/codewiki/text/generation.rs:257-259] |
| `Generation::unwrap_or_record` | method | Extracts the inner string from a 'Generation' enum, returning the generated text or a fallback string while marking degradation via a mutable boolean flag on failure. [crates/gcode/src/commands/codewiki/text/generation.rs:263-272] |
| `maybe_generate` | function | Attempts to generate text via an optional TextGenerator callback, filtering results for prompt echoes and model refusals, and returning a 'Generation' enum variant indicating success ('Generated'), failure ('Failed'), or absence ('Skipped'). [crates/gcode/src/commands/codewiki/text/generation.rs:275-291] |
| `is_prompt_echo` | function | Returns whether the text (after trimming leading whitespace) begins with the first 'PROMPT_ECHO_PREFIX_CHARS' characters of the prompt (after trimming leading whitespace), provided the prompt contains at least that many characters. [crates/gcode/src/commands/codewiki/text/generation.rs:300-310] |
| `is_model_refusal` | function | Returns whether the input string contains any of eight predefined refusal markers ("i cannot write," "i can't write," etc.) within its first REFUSAL_SCAN_CHARS characters in a case-insensitive comparison. [crates/gcode/src/commands/codewiki/text/generation.rs:324-341] |
| `clean_generated` | function | Trims whitespace from the input string and returns 'Some(String)' if the result is non-empty, otherwise 'None'. [crates/gcode/src/commands/codewiki/text/generation.rs:343-346] |

