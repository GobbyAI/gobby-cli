---
title: crates/gcode/src/commands/codewiki/text/generation.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/generation.rs
  ranges:
  - 20-68
  - 73-87
  - 89-97
  - 99-112
  - 119-123
  - 125-142
  - 144-158
  - 167-177
  - 179-182
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Provides the Codewiki text-generation pipeline for AI-backed docs: it resolves an `AiContext` and active route, skips generation when AI is disabled or auto-routed off, then builds a closure that picks daemon or direct text generation, applies the configured aggregate profile for aggregate prompts, retries transient failures with bounded backoff, and trims successful output before returning it. The rest of the file defines the retry and error-classification helpers, plus the `Generation` result wrapper and utility functions that distinguish generated, failed, and skipped outcomes, detect prompt echoes, and normalize empty/whitespace-only text so callers can fall back cleanly and mark degraded output only when generation truly failed.
[crates/gcode/src/commands/codewiki/text/generation.rs:20-68]
[crates/gcode/src/commands/codewiki/text/generation.rs:73-87]
[crates/gcode/src/commands/codewiki/text/generation.rs:89-97]
[crates/gcode/src/commands/codewiki/text/generation.rs:99-112]
[crates/gcode/src/commands/codewiki/text/generation.rs:119-123]

## API Symbols

- `resolve_text_generator` (function) component `resolve_text_generator [function]` (`a95a6d74-34aa-5df0-926d-eb4a49ccaead`) lines 20-68 [crates/gcode/src/commands/codewiki/text/generation.rs:20-68]
  - Signature: `pub(crate) fn resolve_text_generator(`
  - Purpose: Resolves an AI text-generation closure by deriving the active AI context and route, returning 'None' for disabled/auto routing, and otherwise producing a boxed generator that selects daemon or direct generation based on route, applies tier-specific aggregate profiling, retries boundedly, cleans successful output, and logs a single non-quiet failure warning before falling back to 'None'. [crates/gcode/src/commands/codewiki/text/generation.rs:20-68]
- `generate_with_bounded_retry` (function) component `generate_with_bounded_retry [function]` (`7283cd8c-8a0b-58bd-afa2-d484e6011f15`) lines 73-87 [crates/gcode/src/commands/codewiki/text/generation.rs:73-87]
  - Signature: `pub(crate) fn generate_with_bounded_retry<T>(`
  - Purpose: Executes a fallible generator callback, retrying on 'retryable_generation_error' up to the bounded delays in 'GENERATION_RETRY_BACKOFF' with 'std::thread::sleep' between attempts, and returns the final 'Result<T, AiError>'. [crates/gcode/src/commands/codewiki/text/generation.rs:73-87]
- `retryable_generation_error` (function) component `retryable_generation_error [function]` (`891be826-d36f-552e-bcac-2405f3e3d5bd`) lines 89-97 [crates/gcode/src/commands/codewiki/text/generation.rs:89-97]
  - Signature: `fn retryable_generation_error(error: &AiError) -> bool {`
  - Purpose: Returns 'true' for transient AI generation failures that should be retried, specifically transport failures, rate limiting, and HTTP status codes 500 or higher, and 'false' for capability, configuration, and parse errors. [crates/gcode/src/commands/codewiki/text/generation.rs:89-97]
- `resolve_ai_context` (function) component `resolve_ai_context [function]` (`870f6403-ab78-5e3f-9e56-c2694de1b5a7`) lines 99-112 [crates/gcode/src/commands/codewiki/text/generation.rs:99-112]
  - Signature: `fn resolve_ai_context(ctx: &Context, ai: Option<AiRouting>) -> anyhow::Result<AiContext> {`
  - Purpose: Connects to the database in read-only mode, builds an AI config source from Postgres plus optional standalone config, and resolves an 'AiContext' for the current project with optional forced routing and 'no_ai' disabled. [crates/gcode/src/commands/codewiki/text/generation.rs:99-112]
- `Generation` (type) component `Generation [type]` (`caf23a4d-82c8-5286-94da-826e50c96869`) lines 119-123 [crates/gcode/src/commands/codewiki/text/generation.rs:119-123]
  - Signature: `pub(crate) enum Generation {`
  - Purpose: Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:119-123]
- `Generation` (class) component `Generation [class]` (`84d8b4a7-7204-55b0-a070-03c67ba64f48`) lines 125-142 [crates/gcode/src/commands/codewiki/text/generation.rs:125-142]
  - Signature: `impl Generation {`
  - Purpose: 'Generation' provides helpers to detect a failed generation and to consume the value as text, returning a fallback string while marking a mutable 'degraded' flag only when the state is 'Failed' (not 'Skipped'). [crates/gcode/src/commands/codewiki/text/generation.rs:125-142]
- `Generation.failed` (method) component `Generation.failed [method]` (`ee94bbce-49a4-5d50-9713-9576829c4ad6`) lines 126-128 [crates/gcode/src/commands/codewiki/text/generation.rs:126-128]
  - Signature: `pub(crate) fn failed(&self) -> bool {`
  - Purpose: Returns 'true' when 'self' is 'Generation::Failed', and 'false' for all other 'Generation' variants. [crates/gcode/src/commands/codewiki/text/generation.rs:126-128]
- `Generation.unwrap_or_record` (method) component `Generation.unwrap_or_record [method]` (`64c617e6-f233-56d6-87b4-2ff280cca315`) lines 132-141 [crates/gcode/src/commands/codewiki/text/generation.rs:132-141]
  - Signature: `pub(crate) fn unwrap_or_record(self, fallback: String, degraded: &mut bool) -> String {`
  - Purpose: Returns the generated text when 'self' is 'Generation::Generated', otherwise returns 'fallback', setting '*degraded = true' only for 'Generation::Failed' and leaving it unchanged for 'Generation::Skipped'. [crates/gcode/src/commands/codewiki/text/generation.rs:132-141]
- `maybe_generate` (function) component `maybe_generate [function]` (`8a4c98bc-11c2-548f-904b-798e6d45daaa`) lines 144-158 [crates/gcode/src/commands/codewiki/text/generation.rs:144-158]
  - Signature: `pub(crate) fn maybe_generate(`
  - Purpose: Returns 'Generation::Skipped' when no generator is available, otherwise invokes the generator and maps prompt-echoed or missing output to 'Generation::Failed', successful non-echoed text to 'Generation::Generated(text)'. [crates/gcode/src/commands/codewiki/text/generation.rs:144-158]
- `is_prompt_echo` (function) component `is_prompt_echo [function]` (`7752da58-8d5a-5b90-824d-92773829b337`) lines 167-177 [crates/gcode/src/commands/codewiki/text/generation.rs:167-177]
  - Signature: `pub(super) fn is_prompt_echo(text: &str, prompt: &str) -> bool {`
  - Purpose: Returns 'true' when 'text', after trimming leading whitespace, starts with the first 'PROMPT_ECHO_PREFIX_CHARS' characters of 'prompt' after trimming its leading whitespace, and 'false' if the prompt prefix is shorter than that length. [crates/gcode/src/commands/codewiki/text/generation.rs:167-177]
- `clean_generated` (function) component `clean_generated [function]` (`03cbe5bf-ebc7-5e5a-8775-8738d3d5ff4f`) lines 179-182 [crates/gcode/src/commands/codewiki/text/generation.rs:179-182]
  - Signature: `fn clean_generated(text: String) -> Option<String> {`
  - Purpose: Trims leading and trailing whitespace from 'text' and returns 'Some' with the trimmed string if it is non-empty, otherwise returns 'None'. [crates/gcode/src/commands/codewiki/text/generation.rs:179-182]

