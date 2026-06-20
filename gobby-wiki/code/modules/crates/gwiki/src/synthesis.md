---
title: crates/gwiki/src/synthesis
type: code_module
provenance:
- file: crates/gwiki/src/synthesis/generate.rs
- file: crates/gwiki/src/synthesis/paths.rs
- file: crates/gwiki/src/synthesis/render.rs
- file: crates/gwiki/src/synthesis/tests.rs
- file: crates/gwiki/src/synthesis/types.rs
- file: crates/gwiki/src/synthesis/write.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/synthesis` owns the data and safety envelope for turning accepted knowledge handoffs into vault pages. Its types define article targets, source bundles, generation input, prompt telemetry, synthesized pages, and write outcomes; synthesized concept/topic pages can carry an `ExplainerReport`, while source pages leave it absent (`crates/gwiki/src/synthesis/types.rs:1-67`). `ArticleKind` provides the stable mapping from logical article type to vault directory and source-kind metadata (`crates/gwiki/src/synthesis/types.rs:7-30`).

The write flow is guarded before and during persistence. Callers may preflight with `ensure_page_write_allowed`; `write_synthesized_page` then normalizes Markdown, verifies the destination stays under the vault, validates the parent, creates missing directories, and applies the selected write policy (`crates/gwiki/src/synthesis/write.rs:10-39`). Path validation canonicalizes the vault root and existing path prefixes, rejects paths outside the root or containing parent/root/prefix components, and separately checks existing parents before directory creation (`crates/gwiki/src/synthesis/paths.rs:10-80`). Tests capture the intended behavior: existing pages fail under `RequireMergeIntent`, existing content is preserved, and successful writes classify create versus overwrite outcomes (`crates/gwiki/src/synthesis/tests.rs:14-66`).

Collaboration points are mostly crate-local. The path layer imports `WikiError` and synthesis types (`crates/gwiki/src/synthesis/paths.rs:1-6`), the write layer imports path guards plus page/write types and calls `crate::markdown::normalize` before persistence (`crates/gwiki/src/synthesis/write.rs:5-8`, `crates/gwiki/src/synthesis/write.rs:31-37`), and the data model imports `serde::Serialize` plus `crate::explainer::ExplainerReport` (`crates/gwiki/src/synthesis/types.rs:3-5`). The tests exercise public API across pathing, rendering, generation, and writing, including `source_page_paths`, `yaml_scalar`, `slugify_unique`, `synthesize_article`, and `write_synthesized_page` (`crates/gwiki/src/synthesis/tests.rs:7-12`).

| Public symbol | Kind | Contract / fields |
| --- | --- | --- |
| `ArticleKind` | enum | `Source`, `Concept`, `Topic` (`crates/gwiki/src/synthesis/types.rs:7-13`) |
| `ArticleKind::directory` | method | Maps kinds to `knowledge/sources`, `knowledge/concepts`, `knowledge/topics` (`crates/gwiki/src/synthesis/types.rs:15-22`) |
| `ArticleKind::source_kind` | method | Maps kinds to `source_note`, `concept`, `topic` (`crates/gwiki/src/synthesis/types.rs:24-30`) |
| `SynthesisSource` | struct | `title`, `path`, `chunks` (`crates/gwiki/src/synthesis/types.rs:32-37`) |
| `SynthesisInput` | struct | Handoff/topic/outline, target kind, accepted sources, citations, conflicts, missing evidence (`crates/gwiki/src/synthesis/types.rs:39-49`) |
| `SynthesisPrompt` | struct | Prompt text plus daemon/token/truncation metadata (`crates/gwiki/src/synthesis/types.rs:51-58`) |
| `SynthesizedPage` | struct | `path`, `title`, `markdown`, optional `explainer` (`crates/gwiki/src/synthesis/types.rs:60-67`) |
| `WritePolicy` | enum | `RequireMergeIntent`, `AllowOverwriteAfterMerge` (`crates/gwiki/src/synthesis/types.rs:69-73`) |
| `PageWriteKind` | enum | `Created`, `Overwritten` (`crates/gwiki/src/synthesis/types.rs:75-80`) |
| `PageWriteOutcome` | struct | Written `path` plus write `kind` (`crates/gwiki/src/synthesis/types.rs:82-86`) |

| Write behavior | Evidence |
| --- | --- |
| Existing pages require merge intent under strict policy | `ensure_page_write_allowed` checks `page.path.exists()` with `RequireMergeIntent` (`crates/gwiki/src/synthesis/write.rs:15-28`) |
| Strict writes use exclusive creation | `.create_new(true)` is used for `RequireMergeIntent` writes (`crates/gwiki/src/synthesis/write.rs:47-52`) |
| Vault containment is enforced before writing | `write_synthesized_page` calls `ensure_synthesized_path_inside_vault` (`crates/gwiki/src/synthesis/write.rs:31-37`) |
| Parent directory is validated before creation | parent guard runs before `create_dir_all` (`crates/gwiki/src/synthesis/write.rs:38-44`) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/synthesis/generate.rs\|crates/gwiki/src/synthesis/generate.rs]] | `crates/gwiki/src/synthesis/generate.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/paths.rs\|crates/gwiki/src/synthesis/paths.rs]] | `crates/gwiki/src/synthesis/paths.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/render.rs\|crates/gwiki/src/synthesis/render.rs]] | `crates/gwiki/src/synthesis/render.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/tests.rs\|crates/gwiki/src/synthesis/tests.rs]] | `crates/gwiki/src/synthesis/tests.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/types.rs\|crates/gwiki/src/synthesis/types.rs]] | `crates/gwiki/src/synthesis/types.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gwiki/src/synthesis/write.rs\|crates/gwiki/src/synthesis/write.rs]] | `crates/gwiki/src/synthesis/write.rs` exposes 6 indexed API symbols. |

