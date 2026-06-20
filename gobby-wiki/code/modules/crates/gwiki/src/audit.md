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

The `crates/gwiki/src/audit` module audits wiki pages for unsupported claims and renders the resulting report. Its claim pass takes a `WikiPage`, `ProvenanceGraph`, shared `AuditSourceContext`, and `AuditOptions`, derives candidate claim lines, computes provenance-supported lines, checks CodeWiki frontmatter support, and filters out claims that already have provenance or inline citations before emitting `UnsupportedClaim` records with path, line, heading, reason, and source context .

The module collaborates with linting, markdown parsing, provenance, synthesis, and CodeWiki contract code. `claims.rs` imports `WikiPage` and line utilities from `crate::lint`, markdown fence and heading helpers from `crate::markdown`, `ProvenanceGraph` from `crate::provenance`, `slugify` from `crate::synthesis`, and audit-local types from `super` . Generated CodeWiki pages are treated specially: pages under `code/` with `trust: generated` do not inherit raw source context, avoiding misleading audit source suggestions .

Rendering is intentionally compact. `render_text` accepts an `AuditReport`, prints the report scope, then lists unsupported claims as `path:line claim`, appending source IDs when contextual sources are available; empty reports render `- none` [crates/gwiki/src/audit/render.rs:3-32]. Tests exercise the end-to-end audit path via `run(root, ScopeIdentity::topic("ops"))`, source registration through `SourceManifest::register`, and generated-CodeWiki source-context behavior  .

| Symbol | Kind | Responsibility | Evidence |
| --- | --- | --- | --- |
| `unsupported_claims` | `pub(super)` function | Produces `UnsupportedClaim` entries for claims lacking provenance or inline citation |  |
| `has_codewiki_frontmatter_source_spans` | `pub(super)` function | Detects CodeWiki frontmatter provenance support |  |
| `render_text` | `pub` function | Converts an `AuditReport` into plain text output | [crates/gwiki/src/audit/render.rs:3-32] |

| Collaborator | Direction | Role | Evidence |
| --- | --- | --- | --- |
| `crate::lint::WikiPage` | imported | Supplies parsed page content and relative paths for auditing |  |
| `crate::markdown` helpers | imported | Support claim extraction around headings and fenced blocks |  |
| `crate::provenance::ProvenanceGraph` | imported | Determines which claim lines have source support |  |
| `super::AuditReport` | imported | Input to text rendering |  |
| `SourceManifest` / `SourceDraft` | test dependency | Provides source fixtures and citations for audit behavior |  |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/audit/claims.rs\|crates/gwiki/src/audit/claims.rs]] | `crates/gwiki/src/audit/claims.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gwiki/src/audit/render.rs\|crates/gwiki/src/audit/render.rs]] | `crates/gwiki/src/audit/render.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gwiki/src/audit/tests.rs\|crates/gwiki/src/audit/tests.rs]] | `crates/gwiki/src/audit/tests.rs` exposes 14 indexed API symbols. |

