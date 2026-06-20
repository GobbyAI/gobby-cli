---
title: crates/gwiki/src/commands/ask
type: code_module
provenance:
- file: crates/gwiki/src/commands/ask/assembly.rs
- file: crates/gwiki/src/commands/ask/citation.rs
- file: crates/gwiki/src/commands/ask/evidence.rs
- file: crates/gwiki/src/commands/ask/narration.rs
- file: crates/gwiki/src/commands/ask/render.rs
- file: crates/gwiki/src/commands/ask/synthesis.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask

Parent: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

The `ask` module turns search retrieval into a grounded answer. `evidence.rs` builds a bounded `EvidencePlan` from `SearchRetrieval`, centering excerpts around query terms with `query_window`, estimating tokens conservatively, and dropping later hits once the prompt would exceed the 12,000-token budget . `synthesis.rs` then resolves gwiki’s shared AI routing, records requested and effective route metadata on `AskOutput`, and dispatches the single text-generation call through either the direct OpenAI-compatible path or the daemon path .

After generation, the module tightens answer quality in two ways. `narration.rs` strips leading model self-narration by scanning only the opening sentence window, preserving later first-person content once real answer text has begun . `citation.rs` performs post-generation grounding: it extracts sentence-level claims, tokenizes them against titles/snippets/paths/excerpts/code citations, and marks the answer `supported` only when every checkable claim overlaps retrieved evidence above the configured threshold .

Collaboration is intentionally narrow and parent-command scoped: the files expose `pub(super)` helpers and data for the surrounding `ask` command rather than a crate-wide API. The module imports search retrieval primitives from `crate::commands::search`, output DTOs from `crate::output`, wiki errors/config support from the crate, and AI routing/generation facilities from `gobby_core`   . It calls out to shared gcore routing and transport so `ask` follows the same daemon/direct/auto/off behavior as other gwiki AI capabilities .

| Fact | Value | Source |
| --- | --- | --- |
| Prompt token budget | `ASK_PROMPT_TOKEN_BUDGET = 12_000` |  |
| Excerpt window | 800 chars before, 3,200 chars after query match |  |
| Token estimate | `chars.div_ceil(4)` |  |
| AI routes handled | `Direct`, `Daemon`, `Auto`, `Off` | [crates/gwiki/src/commands/ask/synthesis.rs:36-40] |
| Direct config keys | `ai.text_generate.api_base`, `api_key` |  |
| Citation status values | `supported`, `unsupported_claims` |  |
| Claim support threshold | `0.5` |  |
| Minimum claim tokens | `3` |  |
| Narration scan limit | `30` sentences |  |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/commands/ask/assembly.rs\|crates/gwiki/src/commands/ask/assembly.rs]] | `crates/gwiki/src/commands/ask/assembly.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/citation.rs\|crates/gwiki/src/commands/ask/citation.rs]] | `crates/gwiki/src/commands/ask/citation.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/evidence.rs\|crates/gwiki/src/commands/ask/evidence.rs]] | `crates/gwiki/src/commands/ask/evidence.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/narration.rs\|crates/gwiki/src/commands/ask/narration.rs]] | `crates/gwiki/src/commands/ask/narration.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/render.rs\|crates/gwiki/src/commands/ask/render.rs]] | `crates/gwiki/src/commands/ask/render.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/synthesis.rs\|crates/gwiki/src/commands/ask/synthesis.rs]] | `crates/gwiki/src/commands/ask/synthesis.rs` exposes 12 indexed API symbols. |

