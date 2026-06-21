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

## Module: crates/gwiki/src/commands/ask

The `ask` module implements gwiki's question-answering pipeline, taking a natural-language query, assembling bounded evidence from the wiki search index, synthesizing an AI-generated answer, and validating that the answer remains grounded in the retrieved content. Responsibility is divided across six cooperating files: evidence budgeting, synthesis routing, narration cleaning, citation checking, result assembly, and output rendering.

The core flow begins in `evidence.rs`, which pulls ranked hits from `SearchRetrieval` and fills a prompt up to the `ASK_PROMPT_TOKEN_BUDGET` token ceiling (evidence.rs:8). Each hit is windowed around query tokens via `query_window` (evidence.rs:37–51), producing an `EvidencePlan` that carries the assembled prompt, per-item excerpts, and a count of budget-dropped hits. `synthesis.rs` then resolves the AI route through `gobby_core`'s `AiContext`/`effective_route` machinery (synthesis.rs:1–44) and dispatches to either a direct OpenAI-compatible endpoint (`generate_direct`) or the gwiki daemon (`generate_daemon`). After generation, `narration.rs` strips any leading model self-narration preamble — scanning up to 30 sentences and applying a density heuristic to avoid removing genuine answer content (narration.rs:1–55). Finally, `citation.rs` tokenizes each sentence-level claim from the answer and verifies that at least 50 % of its significant tokens appear in the retrieved evidence corpus, emitting a `supported` or `unsupported_claims` status (citation.rs:24–46). `assembly.rs` and `render.rs` collect all sub-outputs into the final `AskOutput` structure for display.

Key public API symbols and internal constants are summarized below:

| Symbol | File | Role |
|---|---|---|
| `synthesize` | synthesis.rs:14 | Entry point — resolves AI route and dispatches completion |
| `EvidencePlan` | evidence.rs:23 | Holds prompt, excerpts, items, token estimate, dropped count |
| `plan_evidence` | evidence.rs:32 | Builds budget-bounded prompt from `SearchRetrieval` |
| `estimate_tokens` | evidence.rs:14 | 4 chars/token ceiling estimate (`chars.div_ceil(4)`) |
| `citation_check` | citation.rs:24 | Post-generation grounding verification |
| `answer_claims` | citation.rs:48 | Splits answer into sentence-level claim strings |
| `claim_is_supported` | citation.rs (component) | Checks one claim against evidence token set |
| `evidence_tokens` | citation.rs (component) | Collects token set from output + excerpts |
| `strip_leading_model_narration` | narration.rs:7 | Removes self-referential AI preamble from answers |

| Constant | Value | Purpose |
|---|---|---|
| `ASK_PROMPT_TOKEN_BUDGET` | 12 000 | Hard cap on synthesis prompt tokens (evidence.rs:8) |
| `EVIDENCE_BEFORE_CHARS` | 800 | Characters of context before query match (evidence.rs:11) |
| `EVIDENCE_AFTER_CHARS` | 3 200 | Characters of context after query match (evidence.rs:12) |
| `CLAIM_SUPPORT_THRESHOLD` | 0.5 | Minimum token-overlap fraction for a grounded claim (citation.rs:11) |
| `MIN_CLAIM_TOKENS` | 3 | Minimum significant tokens for a claim to be checked (citation.rs:15) |
| `NARRATION_SCAN_LIMIT` | 30 | Max leading sentences inspected for preamble stripping (narration.rs:4) |
| `CITATION_CHECK_SUPPORTED` | `"supported"` | Grounding status when all claims pass (citation.rs:8) |

The module sits beneath `crates/gwiki/src/commands` and depends heavily on `gobby_core`: it imports `gobby_core::ai::{daemon, effective_route, text}`, `gobby_core::ai_context::{AiContext, AiContextOptions}`, and `gobby_core::config::{AiCapability, AiRouting}` for transport resolution (synthesis.rs:1–3). Evidence assembly calls back into the sibling `commands::search` module for `SearchRetrieval` and `query_window` (evidence.rs:1–2), and output types (`AskOutput`, `AskAiOutput`, `AskEvidenceOutput`, `AskCitationCheckOutput`, `AskSynthesisOutput`) are drawn from `crate::output` (synthesis.rs:8, citation.rs:3). The `synthesis.rs` hub also uses `crate::support::config::hub_ai_config_source` to obtain the hub's AI configuration source before constructing the routing context (synthesis.rs:22).
[crates/gwiki/src/commands/ask/assembly.rs:6-39]
[crates/gwiki/src/commands/ask/citation.rs:25-46]
[crates/gwiki/src/commands/ask/evidence.rs:14-16]
[crates/gwiki/src/commands/ask/narration.rs:7-58]
[crates/gwiki/src/commands/ask/render.rs:6-16]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/commands/ask/assembly.rs\|crates/gwiki/src/commands/ask/assembly.rs]] | `crates/gwiki/src/commands/ask/assembly.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/citation.rs\|crates/gwiki/src/commands/ask/citation.rs]] | `crates/gwiki/src/commands/ask/citation.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/evidence.rs\|crates/gwiki/src/commands/ask/evidence.rs]] | `crates/gwiki/src/commands/ask/evidence.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/narration.rs\|crates/gwiki/src/commands/ask/narration.rs]] | `crates/gwiki/src/commands/ask/narration.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/render.rs\|crates/gwiki/src/commands/ask/render.rs]] | `crates/gwiki/src/commands/ask/render.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/commands/ask/synthesis.rs\|crates/gwiki/src/commands/ask/synthesis.rs]] | `crates/gwiki/src/commands/ask/synthesis.rs` exposes 12 indexed API symbols. |

