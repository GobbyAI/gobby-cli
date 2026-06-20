---
title: crates/gwiki/src/compile
type: code_module
provenance:
- file: crates/gwiki/src/compile/collect.rs
- file: crates/gwiki/src/compile/index.rs
- file: crates/gwiki/src/compile/mod.rs
- file: crates/gwiki/src/compile/render.rs
- file: crates/gwiki/src/compile/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/compile` prepares research-session handoffs into wiki-ready synthesis inputs. Its core data surface is defined in `mod.rs`: `CompileRequest` captures topic, outline, optional target page, and write intent, while `CompileBundle`, `CompileOutcome`, and `WikiCompileOutcome` carry accepted sources, citations, conflict/gap notes, generated prompts, write results, and optional explainer output (crates/gwiki/src/compile/mod.rs:24-95). The module imports session state, synthesis APIs, citation rendering, and explainer generation, so it sits between accepted research notes and the wiki article-writing pipeline (crates/gwiki/src/compile/mod.rs:5-16).

The collection flow starts from `ResearchSession.accepted_notes`, normalizes each note path against the session scope, rejects missing or out-of-scope notes, reads note text, parses note sections, de-duplicates citations/conflicts/gaps, and records accepted chunks plus offsets (crates/gwiki/src/compile/collect.rs:8-58). Tests exercise this contract by building a `ResearchSession` with an accepted note, calling `prepare_handoff`, and asserting that the resulting bundle includes outline entries, accepted sources, citations, conflicting claims, and missing evidence (crates/gwiki/src/compile/tests.rs:6-100).

The index flow collaborates with synthesis and provenance code. `update_wiki_index` creates a state lock under the vault, locks the index, reads or initializes `_index.md`, computes a wiki link for the synthesized article, inserts it under “Compiled pages” only when absent, and writes the updated index [crates/gwiki/src/compile/index.rs:16-57](crates/gwiki/src/compile/index.rs#L16-L57). That file imports citation source-record helpers, provenance graph/link types, source manifest compile status, and synthesis helpers such as `wiki_link`, `relative_path`, and `slugify`, reflecting its role in wiring compiled pages back into vault metadata and navigation (crates/gwiki/src/compile/index.rs:1-14).

| Public/API symbol | Kind | Role |
| --- | --- | --- |
| `CompileRequest` | struct | User-facing compile request: topic, outline, target page, write intent (crates/gwiki/src/compile/mod.rs:24-30) |
| `CompileOutcome` | struct | Prepared bundle plus updated compile state (crates/gwiki/src/compile/mod.rs:32-36) |
| `WikiCompileOptions` | struct | Controls article kind and daemon synthesis availability (crates/gwiki/src/compile/mod.rs:38-51) |
| `WikiCompileOutcome` | struct | Final wiki compile result with paths, writes, prompt, and explainer report (crates/gwiki/src/compile/mod.rs:53-62) |
| `CompileBundle` | struct | Handoff payload containing sources, citations, conflicts, gaps, and target metadata (crates/gwiki/src/compile/mod.rs:64-76) |
| `AcceptedCompileSource` | struct | Accepted note source with chunks and offsets (crates/gwiki/src/compile/mod.rs:78-84) |
| `collect_accepted_sources` | function | Builds compile sources from accepted session notes (crates/gwiki/src/compile/collect.rs:8-58) |
| `update_wiki_index` | function | Adds compiled article links to `_index.md` under lock [crates/gwiki/src/compile/index.rs:16-57](crates/gwiki/src/compile/index.rs#L16-L57) |

| Environment variable | Default | Purpose |
| --- | --- | --- |
| `GWIKI_INDEX_LOCK_TIMEOUT_MS` | `5000` | Configures wiki index lock timeout (crates/gwiki/src/compile/mod.rs:18-21) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/compile/collect.rs\|crates/gwiki/src/compile/collect.rs]] | `crates/gwiki/src/compile/collect.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/index.rs\|crates/gwiki/src/compile/index.rs]] | `crates/gwiki/src/compile/index.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/mod.rs\|crates/gwiki/src/compile/mod.rs]] | `crates/gwiki/src/compile/mod.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/render.rs\|crates/gwiki/src/compile/render.rs]] | `crates/gwiki/src/compile/render.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/compile/tests.rs\|crates/gwiki/src/compile/tests.rs]] | `crates/gwiki/src/compile/tests.rs` exposes 16 indexed API symbols. |

