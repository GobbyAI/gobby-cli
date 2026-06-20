---
title: crates/gwiki/src/synthesis/generate.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/generate.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis/generate.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/synthesis/generate.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/synthesis/generate.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `synthesize_article` | function | 'synthesize_article' chooses or constructs a vault-local markdown path for the target article, validates it stays inside the vault, resolves accepted source pages and links, generates a grounded explainer/report, and assembles the synthesized page’s markdown with frontmatter, title, sources, and either the explainer body or an outline-based fallback. [crates/gwiki/src/synthesis/generate.rs:13-100] |
| `ground_article_explainer` | function | 'ground_article_explainer' converts a generated explainer into citation-grounded text using accepted source metadata and links, returning the grounded body plus an 'ExplainerReport', or returns 'None' with a failed/skipped report when generation did not succeed. [crates/gwiki/src/synthesis/generate.rs:106-148] |
| `synthesize_source_pages` | function | Creates one synthesized source page per accepted source by validating each target path, rendering source frontmatter plus title, source-path, extracts, and “Used by” sections, and returning the assembled 'SynthesizedPage' vector. [crates/gwiki/src/synthesis/generate.rs:150-190] |

