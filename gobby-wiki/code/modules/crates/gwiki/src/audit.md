---
title: crates/gwiki/src/audit
type: code_module
provenance:
- file: crates/gwiki/src/audit/claims.rs
- file: crates/gwiki/src/audit/render.rs
- file: crates/gwiki/src/audit/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## Module: `crates/gwiki/src/audit`

The `audit` module is responsible for scanning wiki pages for factual claims that lack source provenance or inline citations, collecting those violations into a structured report, and rendering that report as human-readable text. It operates on the parsed wiki content produced by `crate::lint` and cross-references it against provenance data held in `crate::provenance::ProvenanceGraph` to determine which claim lines are supported. The module exposes a public `run` entry-point (exercised throughout `tests.rs`) that accepts a filesystem root and a `ScopeIdentity` and returns an `AuditReport` containing zero or more `UnsupportedClaim` records.

The central flow lives in `claims.rs`. `unsupported_claims` (claims.rs:14-42) calls `claim_lines` to enumerate every claim-bearing line in a `WikiPage`, then calls `supported_claim_lines` to intersect those against the `ProvenanceGraph`. Three exemption paths exist before a claim is emitted: the page has CodeWiki frontmatter source spans (`has_codewiki_frontmatter_source_spans`, claims.rs:63), the line is covered by provenance, or the line carries an inline citation (`has_inline_source_support`). Generated CodeWiki pages — those under `code/` with `trust: generated` in their frontmatter — are detected by `is_generated_codewiki_page` (claims.rs:56-60) and receive an empty `source_context` slice so that raw sources registered in the wider system are not incorrectly attributed to machine-generated content; this behaviour is verified by the `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context` test (tests.rs:54).

Rendering is handled by `render_text` in `render.rs`, the sole public symbol in that file. It formats an `AuditReport` as a plain-text summary, listing each unsupported claim with its file path, line number, claim text, and a bracketed list of contributing source IDs drawn from `AuditSourceContext` records (render.rs:1-31). Source context is threaded into `UnsupportedClaim` at claim-collection time and is populated from `SourceManifest`-registered sources, as demonstrated by the `reports_unsupported_claims` test which registers a URL source with a citation and asserts it appears on the resulting claim (tests.rs:14-46).

### Public API

| Symbol | Location | Description |
|---|---|---|
| `render_text` | render.rs:3 | Converts an `AuditReport` to a plain-text string |
| `unsupported_claims` (pub(super)) | claims.rs:14 | Enumerates claim lines without source provenance |
| `has_codewiki_frontmatter_source_spans` (pub(super)) | claims.rs:63 | Returns true when a `code/` page declares provenance spans in frontmatter |
| `has_inline_source_support` (pub(super)) | claims.rs (tested at tests.rs:5) | Returns true when claim text contains an inline citation marker |
| `claim_lines` (pub(super)) | claims.rs (tested at tests.rs:4) | Extracts all claim-bearing lines from a `WikiPage` |

### Cross-module dependencies

| Import | Used for |
|---|---|
| `crate::lint::{WikiPage, line_number}` | Parsed page representation and line lookup |
| `crate::markdown::{MarkdownFence, markdown_fence_*,  parse_atx_heading}` | Detecting fenced code blocks and headings when classifying claim lines |
| `crate::provenance::ProvenanceGraph` | Determining which lines have source coverage |
| `crate::synthesis::slugify` | Normalising identifiers during claim classification |
| `crate::sources::{SourceDraft, SourceManifest}` | Registering sources in tests and populating `source_context` |
| `gobby_core::codewiki_contract::TRUST_GENERATED` | Sentinel value for identifying machine-generated pages (claims.rs:57) |
[crates/gwiki/src/audit/claims.rs:15-44]
[crates/gwiki/src/audit/render.rs:3-32]
[crates/gwiki/src/audit/tests.rs:14-48]
[crates/gwiki/src/audit/claims.rs:46-55]
[crates/gwiki/src/audit/claims.rs:57-62]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/audit/claims.rs\|crates/gwiki/src/audit/claims.rs]] | `crates/gwiki/src/audit/claims.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/audit/render.rs\|crates/gwiki/src/audit/render.rs]] | `crates/gwiki/src/audit/render.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/audit/tests.rs\|crates/gwiki/src/audit/tests.rs]] | `crates/gwiki/src/audit/tests.rs` exposes 14 indexed API symbols. |

