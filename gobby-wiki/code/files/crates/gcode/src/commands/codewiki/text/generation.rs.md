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
  - 126-128
  - 132-141
  - 144-158
  - 167-177
  - 179-182
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/text/generation.rs:20-68](crates/gcode/src/commands/codewiki/text/generation.rs#L20-L68), [crates/gcode/src/commands/codewiki/text/generation.rs:73-87](crates/gcode/src/commands/codewiki/text/generation.rs#L73-L87), [crates/gcode/src/commands/codewiki/text/generation.rs:89-97](crates/gcode/src/commands/codewiki/text/generation.rs#L89-L97), [crates/gcode/src/commands/codewiki/text/generation.rs:99-112](crates/gcode/src/commands/codewiki/text/generation.rs#L99-L112), [crates/gcode/src/commands/codewiki/text/generation.rs:119-123](crates/gcode/src/commands/codewiki/text/generation.rs#L119-L123), [crates/gcode/src/commands/codewiki/text/generation.rs:126-128](crates/gcode/src/commands/codewiki/text/generation.rs#L126-L128), [crates/gcode/src/commands/codewiki/text/generation.rs:132-141](crates/gcode/src/commands/codewiki/text/generation.rs#L132-L141), [crates/gcode/src/commands/codewiki/text/generation.rs:144-158](crates/gcode/src/commands/codewiki/text/generation.rs#L144-L158), [crates/gcode/src/commands/codewiki/text/generation.rs:167-177](crates/gcode/src/commands/codewiki/text/generation.rs#L167-L177), [crates/gcode/src/commands/codewiki/text/generation.rs:179-182](crates/gcode/src/commands/codewiki/text/generation.rs#L179-L182)

</details>

# crates/gcode/src/commands/codewiki/text/generation.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

This file wires codewiki text generation end to end: it resolves an AI-backed text generator from the current context and routing settings, wraps model calls in a bounded retry loop for retryable errors, and falls back cleanly when generation is unavailable or fails. The `Generation` type tracks successful or degraded generation results, `maybe_generate` decides whether generation should run, and the cleanup helpers filter out prompt echoes and normalize generated text before it is returned or recorded.
[crates/gcode/src/commands/codewiki/text/generation.rs:20-68]
[crates/gcode/src/commands/codewiki/text/generation.rs:73-87]
[crates/gcode/src/commands/codewiki/text/generation.rs:89-97]
[crates/gcode/src/commands/codewiki/text/generation.rs:99-112]
[crates/gcode/src/commands/codewiki/text/generation.rs:119-123]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `resolve_text_generator` | function | `pub(crate) fn resolve_text_generator(` | `resolve_text_generator [function]` | `a95a6d74-34aa-5df0-926d-eb4a49ccaead` | 20-68 [crates/gcode/src/commands/codewiki/text/generation.rs:20-68] | Indexed function `resolve_text_generator` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:20-68] |
| `generate_with_bounded_retry` | function | `pub(crate) fn generate_with_bounded_retry<T>(` | `generate_with_bounded_retry [function]` | `7283cd8c-8a0b-58bd-afa2-d484e6011f15` | 73-87 [crates/gcode/src/commands/codewiki/text/generation.rs:73-87] | Indexed function `generate_with_bounded_retry` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:73-87] |
| `retryable_generation_error` | function | `fn retryable_generation_error(error: &AiError) -> bool {` | `retryable_generation_error [function]` | `891be826-d36f-552e-bcac-2405f3e3d5bd` | 89-97 [crates/gcode/src/commands/codewiki/text/generation.rs:89-97] | Indexed function `retryable_generation_error` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:89-97] |
| `resolve_ai_context` | function | `fn resolve_ai_context(ctx: &Context, ai: Option<AiRouting>) -> anyhow::Result<AiContext> {` | `resolve_ai_context [function]` | `870f6403-ab78-5e3f-9e56-c2694de1b5a7` | 99-112 [crates/gcode/src/commands/codewiki/text/generation.rs:99-112] | Indexed function `resolve_ai_context` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:99-112] |
| `Generation` | type | `pub(crate) enum Generation {` | `Generation [type]` | `caf23a4d-82c8-5286-94da-826e50c96869` | 119-123 [crates/gcode/src/commands/codewiki/text/generation.rs:119-123] | Indexed type `Generation` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:119-123] |
| `Generation::failed` | method | `pub(crate) fn failed(&self) -> bool {` | `Generation::failed [method]` | `ee94bbce-49a4-5d50-9713-9576829c4ad6` | 126-128 [crates/gcode/src/commands/codewiki/text/generation.rs:126-128] | Indexed method `Generation::failed` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:126-128] |
| `Generation::unwrap_or_record` | method | `pub(crate) fn unwrap_or_record(self, fallback: String, degraded: &mut bool) -> String {` | `Generation::unwrap_or_record [method]` | `64c617e6-f233-56d6-87b4-2ff280cca315` | 132-141 [crates/gcode/src/commands/codewiki/text/generation.rs:132-141] | Indexed method `Generation::unwrap_or_record` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:132-141] |
| `maybe_generate` | function | `pub(crate) fn maybe_generate(` | `maybe_generate [function]` | `8a4c98bc-11c2-548f-904b-798e6d45daaa` | 144-158 [crates/gcode/src/commands/codewiki/text/generation.rs:144-158] | Indexed function `maybe_generate` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:144-158] |
| `is_prompt_echo` | function | `pub(super) fn is_prompt_echo(text: &str, prompt: &str) -> bool {` | `is_prompt_echo [function]` | `7752da58-8d5a-5b90-824d-92773829b337` | 167-177 [crates/gcode/src/commands/codewiki/text/generation.rs:167-177] | Indexed function `is_prompt_echo` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:167-177] |
| `clean_generated` | function | `fn clean_generated(text: String) -> Option<String> {` | `clean_generated [function]` | `03cbe5bf-ebc7-5e5a-8775-8738d3d5ff4f` | 179-182 [crates/gcode/src/commands/codewiki/text/generation.rs:179-182] | Indexed function `clean_generated` in `crates/gcode/src/commands/codewiki/text/generation.rs`. [crates/gcode/src/commands/codewiki/text/generation.rs:179-182] |
