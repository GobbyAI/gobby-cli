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

# crates/gwiki/src/synthesis/generate.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Purpose

This file orchestrates wiki content synthesis. `synthesize_article` builds the target article path, validates it stays inside the vault, resolves source pages and citation links, grounds the explainer text, and renders the final article markdown with frontmatter, title, sources, and either generated prose or outline-based fallback content. `ground_article_explainer` wraps explainer grounding and reporting, while `synthesize_source_pages` generates corresponding markdown pages for each accepted source with source metadata, excerpts, and a backreference to the synthesized article.
[crates/gwiki/src/synthesis/generate.rs:13-100]
[crates/gwiki/src/synthesis/generate.rs:106-148]
[crates/gwiki/src/synthesis/generate.rs:150-190]

## API Symbols

- `synthesize_article` (function) component `synthesize_article [function]` (`0263f169-28eb-5daf-af73-0e82de1a1e71`) lines 13-100 [crates/gwiki/src/synthesis/generate.rs:13-100]
  - Signature: `pub fn synthesize_article(`
  - Purpose: 'synthesize_article' determines the target article path within the vault, validates it, resolves accepted source pages and links, runs the explainer grounding step, and assembles a markdown page with frontmatter, title, source list, and either the generated body or outline-based placeholder content into a 'SynthesizedPage'. [crates/gwiki/src/synthesis/generate.rs:13-100]
- `ground_article_explainer` (function) component `ground_article_explainer [function]` (`4cc01a9b-4cd0-5f77-a008-49c7410cf3d0`) lines 106-148 [crates/gwiki/src/synthesis/generate.rs:106-148]
  - Signature: `fn ground_article_explainer(`
  - Purpose: 'ground_article_explainer' grounds a generated explainer body against citation targets derived from accepted sources and source links, returning the grounded text plus an 'ExplainerReport', or 'None' with a failed/skipped report when generation did not occur. [crates/gwiki/src/synthesis/generate.rs:106-148]
- `synthesize_source_pages` (function) component `synthesize_source_pages [function]` (`ea8e504d-5eb7-5496-938a-293d095450ad`) lines 150-190 [crates/gwiki/src/synthesis/generate.rs:150-190]
  - Signature: `pub fn synthesize_source_pages(`
  - Purpose: Builds a 'Vec<SynthesizedPage>' for each accepted source by validating the synthesized path is inside the vault, generating source-page markdown with frontmatter, title, source path, extracts, and a backreference to the article, and returning the pages or a 'WikiError' on validation failure. [crates/gwiki/src/synthesis/generate.rs:150-190]

