---
title: crates/gcode/src/commands/codewiki/text/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/generation.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/text/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

The `crates/gcode/src/commands/codewiki/text/generation.rs` file manages text-generation and verification tasks for the codewiki documentation engine. It acts as an adapter that resolves configuration settings and abstracts the details of calling AI generation endpoints, ensuring robust and clean text outputs.

## How it fits
[crates/gcode/src/commands/codewiki/text/generation.rs:21-69]
[crates/gcode/src/commands/codewiki/text/generation.rs:79-144]
[crates/gcode/src/commands/codewiki/text/generation.rs:149-163]
[crates/gcode/src/commands/codewiki/text/generation.rs:165-173]
[crates/gcode/src/commands/codewiki/text/generation.rs:175-188]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `resolve_text_generator` | function | Resolves and returns an optional boxed text-generation closure that configures AI context and routing, short-circuits when text generation is disabled, invokes either daemon or direct generation with bounded retries and tier-dependent profile selection, cleans successful output, and emits a one-time warning while returning 'None' on failure. [crates/gcode/src/commands/codewiki/text/generation.rs:21-69] |
| `resolve_text_verifier` | function | Resolves the AI context and verification model/API-key settings, returns 'None' for 'Off'/'Auto' routing, and otherwise builds a boxed 'TextVerifier' closure that generates verification text via the selected route with bounded retries, cleans the output, and emits at most one warning on failure. [crates/gcode/src/commands/codewiki/text/generation.rs:79-144] |
| `generate_with_bounded_retry` | function | Calls a generator closure once and, only for retryable 'AiError's, retries it after each delay in 'GENERATION_RETRY_BACKOFF' until success or the retry budget is exhausted, then returns the final 'Result<T, AiError>'. [crates/gcode/src/commands/codewiki/text/generation.rs:149-163] |
| `retryable_generation_error` | function | Returns 'true' for transient AI generation failures that should be retried ('TransportFailure', 'RateLimited', and HTTP 5xx statuses) and 'false' for non-retryable errors ('CapabilityUnavailable', 'NotConfigured', 'ParseFailure'). [crates/gcode/src/commands/codewiki/text/generation.rs:165-173] |
| `resolve_ai_context` | function | Creates a read-only database connection, builds an AI configuration source from primary Postgres and optional standalone config, and resolves an 'AiContext' for the current project with optional forced routing and AI enabled. [crates/gcode/src/commands/codewiki/text/generation.rs:175-188] |
| `Generation` | type | Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:195-199] |
| `Generation::failed` | method | Returns 'true' if 'self' is 'Generation::Failed', and 'false' otherwise. [crates/gcode/src/commands/codewiki/text/generation.rs:202-204] |
| `Generation::unwrap_or_record` | method | Returns the generated 'text' when 'self' is 'Generation::Generated', otherwise returns 'fallback' and sets '*degraded = true' only for 'Generation::Failed' (not for 'Generation::Skipped'). [crates/gcode/src/commands/codewiki/text/generation.rs:208-217] |
| `maybe_generate` | function | Returns 'Generation::Skipped' when no generator is available, otherwise invokes it and maps a prompt-echoing or 'None' result to 'Generation::Failed' and any other 'Some(text)' result to 'Generation::Generated(text)'. [crates/gcode/src/commands/codewiki/text/generation.rs:220-234] |
| `is_prompt_echo` | function | Returns 'true' only when the left-trimmed 'text' begins with the first 'PROMPT_ECHO_PREFIX_CHARS' Unicode scalar values of the left-trimmed 'prompt', and returns 'false' if the prompt prefix is shorter than that threshold. [crates/gcode/src/commands/codewiki/text/generation.rs:243-253] |
| `clean_generated` | function | Returns 'Some(trimmed_text)' when the input string is non-empty after whitespace trimming, otherwise returns 'None'. [crates/gcode/src/commands/codewiki/text/generation.rs:255-258] |

