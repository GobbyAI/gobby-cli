---
title: crates/gwiki/src/synthesis/generate.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/generate.rs
  ranges:
  - 13-100
  - 106-148
  - 150-190
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/synthesis/generate.rs:13-100](crates/gwiki/src/synthesis/generate.rs#L13-L100), [crates/gwiki/src/synthesis/generate.rs:106-148](crates/gwiki/src/synthesis/generate.rs#L106-L148), [crates/gwiki/src/synthesis/generate.rs:150-190](crates/gwiki/src/synthesis/generate.rs#L150-L190)

</details>

# crates/gwiki/src/synthesis/generate.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file builds synthesized wiki markdown for articles and their supporting source pages. `synthesize_article` picks a safe vault-local target path, resolves accepted sources into page paths and links, grounds the generated explainer, and assembles the final article with frontmatter, title, source list, and either the grounded body or an outline-based fallback; `ground_article_explainer` handles the grounding step and emits an `ExplainerReport`; `synthesize_source_pages` mirrors the process for each accepted source by validating paths and rendering per-source pages with metadata, excerpts, and “Used by” references.
[crates/gwiki/src/synthesis/generate.rs:13-100]
[crates/gwiki/src/synthesis/generate.rs:106-148]
[crates/gwiki/src/synthesis/generate.rs:150-190]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `synthesize_article` | function | `pub fn synthesize_article(` | `synthesize_article [function]` | `0263f169-28eb-5daf-af73-0e82de1a1e71` | 13-100 [crates/gwiki/src/synthesis/generate.rs:13-100] | 'synthesize_article' chooses or constructs a vault-local markdown path for the target article, validates it stays inside the vault, resolves accepted source pages and links, generates a grounded explainer/report, and assembles the synthesized page’s markdown with frontmatter, title, sources, and either the explainer body or an outline-based fallback. [crates/gwiki/src/synthesis/generate.rs:13-100] |
| `ground_article_explainer` | function | `fn ground_article_explainer(` | `ground_article_explainer [function]` | `4cc01a9b-4cd0-5f77-a008-49c7410cf3d0` | 106-148 [crates/gwiki/src/synthesis/generate.rs:106-148] | 'ground_article_explainer' converts a generated explainer into citation-grounded text using accepted source metadata and links, returning the grounded body plus an 'ExplainerReport', or returns 'None' with a failed/skipped report when generation did not succeed. [crates/gwiki/src/synthesis/generate.rs:106-148] |
| `synthesize_source_pages` | function | `pub fn synthesize_source_pages(` | `synthesize_source_pages [function]` | `ea8e504d-5eb7-5496-938a-293d095450ad` | 150-190 [crates/gwiki/src/synthesis/generate.rs:150-190] | Creates one synthesized source page per accepted source by validating each target path, rendering source frontmatter plus title, source-path, extracts, and “Used by” sections, and returning the assembled 'SynthesizedPage' vector. [crates/gwiki/src/synthesis/generate.rs:150-190] |
