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

## Module: `crates/gcode/src/commands/codewiki/build_parts`

This module is the generation engine for the codewiki command, housing one builder file per wiki page type. Each builder accepts structured inputs — file docs, module docs, call-graph edges, and a `CodewikiGraphAvailability` signal — and emits a typed doc struct that the parent codewiki coordinator assembles into the final output. The twelve builders divide cleanly into two rendering strategies: fully deterministic builders (audit, changes, hotspots, snapshot) that rely only on index facts and bounded source scans, and LLM-assisted builders (curated content, module docs, file docs) that include a structural fallback so `--ai off` runs and generation failures still produce real content rather than bare summaries.

The audit subsystem (`audit.rs`) is the most self-contained: it introduces `AuditContext` (audit.rs:38–55), built once per run and threaded through generation in the same pattern as `system_model`. Deprecation detection walks up to `LOOKBACK_LINES = 12` source lines above each symbol (audit.rs:24) scanning for `#[deprecated(...)]` attributes and doc-comment markers; dead-code candidates are derived from the call-graph edge set and filtered against a set of known entry points drawn from the feature catalog, capped at `DEAD_CODE_CANDIDATE_CAP = 500` items (audit.rs:29). Both pages are guaranteed to render even when the graph is unavailable. The onboarding builder (`onboarding.rs`) applies the same availability guard: when `CodewikiGraphAvailability::Unavailable` is signalled it omits the centrality-ranked reading order rather than marking the page degraded (onboarding.rs:19–23), and it delegates topology work to sibling helpers `dependency_topology` and `module_dependency_edges` from `architecture.rs` (onboarding.rs:2).

The feature catalog builder (`features.rs`) is the primary integration point with the CLI contract layer. It parses pinned `*.contract.json` files for two registered binaries and resolves each contract command name to a handler file and entry symbol through binary-specific dispatch resolvers; any unmapped command renders without a Docs wikilink so coverage gaps stay visible (features.rs:57–65). The curated-content builder (`curated_content.rs`) runs a second per-page LLM pass that expands concept and narrative pages beyond the one-line summaries produced by the structure pass in the `concepts` child module; it caps evidence rows fed into a single prompt at `MAX_PAGE_SYMBOL_ROWS = 12` (curated_content.rs:23) and records `degraded: true` on fallback so reviewers can distinguish intended structural output from a failed generation (curated_content.rs:39–44). The snapshot builder (`snapshot.rs`) finalises a run by hashing output files and computing graph-neighbourhood fingerprints, providing the change-detection baseline consumed by `changes.rs`.

### Registered CLI Binaries (features.rs)

| Binary | Crate dir | Contract file |
| --- | --- | --- |
| `gcode` | `gcode` | `gcode.contract.json` |
| `gwiki` | `gwiki` | `gwiki.contract.json` |

### Page Builder Public Entry Points

| File | Primary entry point | Output type |
| --- | --- | --- |
| `architecture.rs` | `build_architecture_doc` | architecture doc |
| `audit.rs` | `build_audit_context`, `build_deprecations_doc`, `build_dead_code_doc` | `AuditContext`, `DeprecationsDoc`, `DeadCodeDoc` |
| `changes.rs` | `build_codewiki_changes_doc` | changes doc |
| `curated_content.rs` | `curated_page_body` | `CuratedBody` |
| `features.rs` | `build_feature_catalog_doc` | `FeatureCatalogDoc` |
| `file.rs` | `build_file_doc` | file doc |
| `hotspots.rs` | `build_hotspots_doc` | hotspots doc |
| `infrastructure.rs` | `build_infrastructure_doc` | infrastructure doc |
| `modules.rs` | `build_module_docs`, `build_module_docs_with_filter` | module docs |
| `onboarding.rs` | `build_onboarding_doc` | `OnboardingDoc` |
| `snapshot.rs` | `build_codewiki_index_snapshot` | snapshot |

### Key Constants

| Constant | Value | Location | Purpose |
| --- | --- | --- | --- |
| `LOOKBACK_LINES` | 12 | audit.rs:24 | Source lines scanned above a symbol for deprecation/test gating |
| `DEAD_CODE_CANDIDATE_CAP` | 500 | audit.rs:29 | Maximum dead-code rows rendered per page |
| `REASON_MAX` | 160 | audit.rs:32 | Max chars kept from a `DEPRECATED` doc-comment reason |
| `MAX_PAGE_SYMBOL_ROWS` | 12 | curated_content.rs:23 | Evidence rows fed into one content-pass prompt |
| `MAX_KEY_FLAGS` | 8 | features.rs:8 | Max flag names listed per command row in feature catalog |
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:10-138]
[crates/gcode/src/commands/codewiki/build_parts/curated_content.rs:28-31]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170]
[crates/gcode/src/commands/codewiki/build_parts/audit.rs:38-51]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts\|crates/gcode/src/commands/codewiki/build_parts/concepts]] | ## Module: `crates/gcode/src/commands/codewiki/build_parts/concepts` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/architecture.rs\|crates/gcode/src/commands/codewiki/build_parts/architecture.rs]] | `crates/gcode/src/commands/codewiki/build_parts/architecture.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/audit.rs\|crates/gcode/src/commands/codewiki/build_parts/audit.rs]] | `crates/gcode/src/commands/codewiki/build_parts/audit.rs` exposes 27 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/changes.rs\|crates/gcode/src/commands/codewiki/build_parts/changes.rs]] | `crates/gcode/src/commands/codewiki/build_parts/changes.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/concepts.rs\|crates/gcode/src/commands/codewiki/build_parts/concepts.rs]] | `crates/gcode/src/commands/codewiki/build_parts/concepts.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/curated_content.rs\|crates/gcode/src/commands/codewiki/build_parts/curated_content.rs]] | `crates/gcode/src/commands/codewiki/build_parts/curated_content.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/features.rs\|crates/gcode/src/commands/codewiki/build_parts/features.rs]] | `crates/gcode/src/commands/codewiki/build_parts/features.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/file.rs\|crates/gcode/src/commands/codewiki/build_parts/file.rs]] | `crates/gcode/src/commands/codewiki/build_parts/file.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/hotspots.rs\|crates/gcode/src/commands/codewiki/build_parts/hotspots.rs]] | `crates/gcode/src/commands/codewiki/build_parts/hotspots.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs\|crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs]] | `crates/gcode/src/commands/codewiki/build_parts/infrastructure.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/modules.rs\|crates/gcode/src/commands/codewiki/build_parts/modules.rs]] | `crates/gcode/src/commands/codewiki/build_parts/modules.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/onboarding.rs\|crates/gcode/src/commands/codewiki/build_parts/onboarding.rs]] | `crates/gcode/src/commands/codewiki/build_parts/onboarding.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/build_parts/snapshot.rs\|crates/gcode/src/commands/codewiki/build_parts/snapshot.rs]] | `crates/gcode/src/commands/codewiki/build_parts/snapshot.rs` exposes 3 indexed API symbols. |

