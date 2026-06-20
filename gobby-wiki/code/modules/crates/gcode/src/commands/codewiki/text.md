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

The `codewiki/text` module owns the prose pipeline for generated wiki pages: deterministic structural summaries, AI-assisted generation, citation grounding, Markdown sanitization, YAML frontmatter, and optional verifier notes. `sanitize_model_markdown_links` first strips unsafe link targets, then rewrites relative citation targets from `path:line[-end]` to resolvable `path#Lline[-Lend]` anchors so downstream linting can validate them (crates/gcode/src/commands/codewiki/text/sanitize.rs:1-100).

Citation handling collaborates with sanitization and provenance spans. `citations.rs` imports `sanitize_model_markdown_links` and `SourceSpan`, caps uncited fallback citations at five, ranks fallback spans by lexical overlap with generated text, and deprioritizes asset/data files unless they are the only provenance available (crates/gcode/src/commands/codewiki/text/citations.rs:1-100). Frontmatter generation serializes title, page type, provenance, degradation state, and verifier notes; it caps listed provenance files at 30 and records truncation separately (crates/gcode/src/commands/codewiki/text/frontmatter.rs:1-100).

Generation and verification form the AI-facing flow. Generation resolves text generators/verifiers, retries bounded failures, detects prompt echoes, and cleans generated output. Verification is a second, optional grounded pass: it splits prose into numbered blocks, calls the configured verifier with source excerpts, symbols, and relationship facts, then preserves the original text while recording unsupported-block findings only as frontmatter notes (crates/gcode/src/commands/codewiki/text/verify.rs:1-100). Externally, this module imports shared `codewiki` types such as `SourceSpan`, `VerifyNote`, `TextVerifier`, `RelationshipFacts`, and prompt structs, and calls out to `prompts::verify_prompt` plus the supplied verifier closure (crates/gcode/src/commands/codewiki/text/frontmatter.rs:1-100; crates/gcode/src/commands/codewiki/text/verify.rs:1-100).

| Area | Public symbols |
| --- | --- |
| Citations | `ground_text`, `fallback_spans`, `citation_list`, `citation_markers`, `citation_references`, `replace_citations_with_markers`, `write_references`, `strip_invalid_citations`, `reanchor_citations`, `CitationResolver`, `ReanchorResult` |
| Frontmatter | `frontmatter`, `frontmatter_with_degradation`, `frontmatter_with_degradation_without_ranges`, `frontmatter_with_degradation_and_verify_notes_without_ranges`, `frontmatter_with_options`, `frontmatter_source_files` |
| Generation | `resolve_text_generator`, `resolve_text_verifier`, `generate_with_bounded_retry`, `resolve_ai_context`, `maybe_generate`, `clean_generated`, `Generation` |
| Sanitization | `sanitize_model_markdown_links`, `neutralize_symbol_purpose_links`, `markdown_link_replacements`, `wikilink_replacements`, `unsafe_link_replacements`, `is_unsafe_link_target` |
| Structural text | `structural_symbol_purpose`, `structural_file_summary`, `display_child_summary`, `structural_module_summary`, `structural_repo_summary` |
| Verification | `VerifyOutcome`, `verify_with_notes`, `split_blocks`, `parse_verify_notes` |
[crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
[crates/gcode/src/commands/codewiki/text/frontmatter.rs:7-23]
[crates/gcode/src/commands/codewiki/text/generation.rs:23-79]
[crates/gcode/src/commands/codewiki/text/sanitize.rs:7-10]
[crates/gcode/src/commands/codewiki/text/structural.rs:7-22]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/text/citations.rs\|crates/gcode/src/commands/codewiki/text/citations.rs]] | `crates/gcode/src/commands/codewiki/text/citations.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/frontmatter.rs\|crates/gcode/src/commands/codewiki/text/frontmatter.rs]] | `crates/gcode/src/commands/codewiki/text/frontmatter.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/generation.rs\|crates/gcode/src/commands/codewiki/text/generation.rs]] | `crates/gcode/src/commands/codewiki/text/generation.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/sanitize.rs\|crates/gcode/src/commands/codewiki/text/sanitize.rs]] | `crates/gcode/src/commands/codewiki/text/sanitize.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/structural.rs\|crates/gcode/src/commands/codewiki/text/structural.rs]] | `crates/gcode/src/commands/codewiki/text/structural.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/text/verify.rs\|crates/gcode/src/commands/codewiki/text/verify.rs]] | `crates/gcode/src/commands/codewiki/text/verify.rs` exposes 18 indexed API symbols. |

