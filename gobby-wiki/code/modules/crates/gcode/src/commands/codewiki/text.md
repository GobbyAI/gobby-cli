---
title: crates/gcode/src/commands/codewiki/text
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/text/citations.rs
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
- file: crates/gcode/src/commands/codewiki/text/generation.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/text/structural.rs
- file: crates/gcode/src/commands/codewiki/text/verify.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text

Parent: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

## Module: `crates/gcode/src/commands/codewiki/text`

This module is the text-processing backbone of the codewiki command system, covering every stage of wiki-page content from AI generation through sanitization, citation grounding, frontmatter serialization, structural templating, and an optional verification pass. Its six files operate as a pipeline: `generation.rs` drives model calls and retries, `sanitize.rs` repairs the raw model output, `citations.rs` grounds prose in provenance spans, `frontmatter.rs` serializes YAML page headers, `structural.rs` emits deterministically formatted sections for non-generative pages, and `verify.rs` runs a read-only audit that records unsupported prose blocks without rewriting them. All six files are `pub(super)` or `pub(crate)` — the API surface is consumed entirely by the parent `codewiki` command layer, never by callers outside the crate.

The generation flow begins in `generation.rs` with `writer_candidate_chain` and `resolve_text_generator`, which select an AI writer and delegate to `generate_with_bounded_retry` citations.rs:1. Guard functions `is_prompt_echo` and `is_model_refusal` detect degenerate outputs; `clean_generated` normalises whitespace before handing text to `sanitize_model_markdown_links` sanitize.rs:7. That sanitizer runs two replacement passes via `apply_replacements`: first `unsafe_link_replacements` strips Windows absolute paths, `file:` URIs, and directory-traversal targets, collapsing them to label text only; then `citation_anchor_replacements` rewrites bare `path:line` link targets into the `path#Lline` anchor form expected by `gwiki lint` sanitize.rs:20–53. The `pulldown_cmark` event stream drives both passes, with `markdown_code_ranges` used to exclude replacements that fall inside fenced or inline code. After sanitization the text re-enters `citations.rs` where `ground_text` validates inline citations, calls `strip_invalid_citations`, and falls back to `fallback_spans` (capped at `MAX_FALLBACK_CITATIONS`) when no valid inline citation exists citations.rs:60–.

Frontmatter is built by `frontmatter_with_options` in `frontmatter.rs`, which serialises a `Frontmatter` struct to YAML and prepends it to the page body frontmatter.rs:1–. The struct carries provenance files (truncated beyond `MAX_FRONTMATTER_PROVENANCE_FILES`), optional `degraded`/`degraded_sources` fields for partial-graph pages, and `verify_notes` populated by the verification pass. Four public façades expose the same builder with different combinations of options:

| Function | Ranges | Verify notes | Degradation |
|---|---|---|---|
| `frontmatter_with_degradation` | ✓ | — | ✓ |
| `frontmatter_with_degradation_without_ranges` | — | — | ✓ |
| `frontmatter_with_degradation_and_verify_notes_without_ranges` | — | ✓ | ✓ |
| `frontmatter` (test-only) | ✓ | — | — |

The verification pass in `verify.rs` is intentionally read-only: `split_blocks` partitions generated prose into numbered paragraph-level chunks, the `TextVerifier` closure (resolved by `resolve_text_verifier` in `generation.rs`) is called with a prompt built by `prompts::verify_prompt`, and `parse_verify_notes` deserialises the JSON array response into `VerifyNote` values. Malformed verdicts, an unavailable verifier, or an empty block list all resolve to `VerifyOutcome::Skipped`; a clean verdict resolves to `VerifyOutcome::Verified { text, notes }` where `notes` may be empty verify.rs:35–60. Prose is never modified — findings only surface as `verify_notes` entries in the frontmatter serialised by `frontmatter.rs`.

### Key constants

| Constant | Value | Location |
|---|---|---|
| `MAX_FALLBACK_CITATIONS` | `5` | citations.rs:12 |
| `FALLBACK_CITATION_LINE_WIDTH` | `240` | citations.rs:7 |
| `MAX_FRONTMATTER_PROVENANCE_FILES` | `30` | frontmatter.rs:38 |

### `VerifyOutcome` variants

| Variant | Meaning |
|---|---|
| `Skipped` | No verifier configured, unavailable, empty body, or malformed verdict; page proceeds undegraded |
| `Verified { text, notes }` | Verifier ran; `notes` lists unsupported blocks as frontmatter-only audit entries |

### Asset/data file extensions ranked behind source files in fallback citations

`csv gif ico jpeg jpg json lock png svg toml tsv xml yaml yml` — citations.rs:22

### Collaboration points

This module imports `SourceSpan`, `VerifyNote`, `RelationshipFacts`, `TextVerifier`, and `inline_code` from the parent `crate::commands::codewiki` namespace sanitize.rs:5, verify.rs:15. It imports `prompts::{verify_prompt, VERIFY_SYSTEM, SourceExcerpt, SymbolSummary}` from the sibling `prompts` module verify.rs:13. The `pulldown_cmark` crate is used directly in `sanitize.rs` for event-driven link detection sanitize.rs:3. The structural module (`structural.rs`) is self-contained — its seven render functions (`structural_symbol_purpose`, `structural_file_summary`, `structural_module_summary`, `structural_repo_summary`, etc.) accept pre-built string inputs and emit Markdown sections without calling AI or reading files, making them straightforwardly unit-testable.
[crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-23]
[crates/gcode/src/commands/codewiki/text/generation.rs:28-39]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10]
[crates/gcode/src/commands/codewiki/text/structural.rs:7-22]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/text/citations.rs\|crates/gcode/src/commands/codewiki/text/citations.rs]] | `crates/gcode/src/commands/codewiki/text/citations.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/frontmatter.rs\|crates/gcode/src/commands/codewiki/text/frontmatter.rs]] | `crates/gcode/src/commands/codewiki/text/frontmatter.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/generation.rs\|crates/gcode/src/commands/codewiki/text/generation.rs]] | `crates/gcode/src/commands/codewiki/text/generation.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/sanitize.rs\|crates/gcode/src/commands/codewiki/text/sanitize.rs]] | `crates/gcode/src/commands/codewiki/text/sanitize.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/structural.rs\|crates/gcode/src/commands/codewiki/text/structural.rs]] | `crates/gcode/src/commands/codewiki/text/structural.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/verify.rs\|crates/gcode/src/commands/codewiki/text/verify.rs]] | `crates/gcode/src/commands/codewiki/text/verify.rs` exposes 18 indexed API symbols. |

