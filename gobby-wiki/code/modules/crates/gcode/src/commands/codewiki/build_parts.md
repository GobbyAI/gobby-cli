---
title: crates/gcode/src/commands/codewiki/build_parts
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/build_parts/features.rs
- file: crates/gcode/src/commands/codewiki/build_parts/file.rs
- file: crates/gcode/src/commands/codewiki/build_parts/hotspots.rs
- file: crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
- file: crates/gcode/src/commands/codewiki/build_parts/snapshot.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts

Parent: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

The `build_parts` module is the document-generation toolkit behind codewiki pages: architecture, audits, changes, curated concepts, feature catalogs, file/module pages, hotspots, infrastructure, onboarding, and snapshots. Its audit path is deterministic and LLM-free, building deprecation and dead-code pages from indexed symbols, call graph edges, and bounded source scans, while keeping index parsing and hub schemas untouched (`audit.rs:1-8`). Curated concepts use a two-step flow: first they plan concept modules, sections, and narrative pages from file/module summaries, then render grounded page bodies with fallback behavior when generation is unavailable or degraded (`plan.rs:1-43`, `render.rs:9-33`).

The module collaborates outward with the rest of codewiki generation through shared `super::super` types such as `CodewikiInput`, graph edges, audit docs, feature catalog docs, and test/deprecation indexes (`audit.rs:11-18`). `AuditContext` is explicitly built once and threaded from `run.rs` through the generation core, carrying deprecations, test-gated symbols, project root, and feature-catalog entry points (`audit.rs:35-46`). The onboarding builder imports architecture helpers for module dependency analysis and graph analytics for centrality-based reading order; when graph data is unavailable, it keeps entry points and omits ranked reading order without marking the page degraded (`onboarding.rs:1-18`).

Feature catalog generation reads pinned CLI contract JSON for `gcode` and `gwiki`, then resolves each contract command to dispatch wiring so the docs can link commands back to handler files and entry symbols (`features.rs:5-17`, `features.rs:35-64`). Curated content is intentionally decoupled from concept data structures: callers pass primitive member lists and receive a ready-to-render body string, allowing `concepts` to own structure while `curated_content` owns the per-page prose pass and structural fallback (`curated_content.rs:1-14`, `curated_content.rs:45-51`).

| Area | Symbols / Facts | Purpose |
| --- | --- | --- |
| Audit | `AuditContext`, `DEAD_CODE_CANDIDATE_CAP`, `LOOKBACK_LINES` | Carries deterministic audit state; bounds scans and rendered dead-code output (`audit.rs:20-40`) |
| Curated content | `CuratedPageKind::{Concept, Narrative}`, `CuratedBody`, `curated_page_body` | Expands concept and narrative pages into grounded bodies with degradation tracking (`curated_content.rs:20-51`) |
| Feature catalog | `Contract`, `ContractCommand`, `ContractFlag`, `BinaryContract` | Parses pinned CLI contracts and maps commands to handlers (`features.rs:8-33`, `features.rs:53-64`) |
| Binaries | `gcode`, `gwiki` | Enumerated from contract files under workspace crates (`features.rs:35-50`) |
| Onboarding | `build_onboarding_doc` | Produces entry points and optional graph-ranked reading order (`onboarding.rs:6-35`) |
[crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:6-38]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-133]
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:6-13]
[crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts\|crates/gcode/src/commands/codewiki/build_parts/concepts]] | This module builds the curated “concepts” navigation layer for codewiki. It defines the JSON plan shape for concept modules, sections, and narrative pages, then turns file/module summaries into a prompt, parses model output, and provides fallback planning when needed (`plan.rs:1-43`, `types.rs:5-70`). Rendering normalizes the plan, expands each concept/narrative summary into grounded page bodies, and emits built documentation, tracking degraded body generation and verification notes (`render.rs:9-33`, `types.rs:20-31`, `types.rs:56-69`). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/architecture.rs\|crates/gcode/src/commands/codewiki/build_parts/architecture.rs]] | `crates/gcode/src/commands/codewiki/build_parts/architecture.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/audit.rs\|crates/gcode/src/commands/codewiki/build_parts/audit.rs]] | `crates/gcode/src/commands/codewiki/build_parts/audit.rs` exposes 27 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/changes.rs\|crates/gcode/src/commands/codewiki/build_parts/changes.rs]] | `crates/gcode/src/commands/codewiki/build_parts/changes.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/curated_content.rs\|crates/gcode/src/commands/codewiki/build_parts/curated_content.rs]] | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/features.rs\|crates/gcode/src/commands/codewiki/build_parts/features.rs]] | `crates/gcode/src/commands/codewiki/build_parts/features.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/file.rs\|crates/gcode/src/commands/codewiki/build_parts/file.rs]] | `crates/gcode/src/commands/codewiki/build_parts/file.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/hotspots.rs\|crates/gcode/src/commands/codewiki/build_parts/hotspots.rs]] | `crates/gcode/src/commands/codewiki/build_parts/hotspots.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs\|crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs]] | `crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/modules.rs\|crates/gcode/src/commands/codewiki/build_parts/modules.rs]] | `crates/gcode/src/commands/codewiki/build_parts/modules.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/onboarding.rs\|crates/gcode/src/commands/codewiki/build_parts/onboarding.rs]] | `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/snapshot.rs\|crates/gcode/src/commands/codewiki/build_parts/snapshot.rs]] | `crates/gcode/src/commands/codewiki/build_parts/snapshot.rs` exposes 3 indexed API symbols. |

