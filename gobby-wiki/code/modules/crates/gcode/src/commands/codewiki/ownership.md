---
title: crates/gcode/src/commands/codewiki/ownership
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
- file: crates/gcode/src/commands/codewiki/ownership/codeowners.rs
- file: crates/gcode/src/commands/codewiki/ownership/render.rs
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/ownership

Parent: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

## Module: `crates/gcode/src/commands/codewiki/ownership`

This module implements the code-ownership pipeline for the `codewiki` command. It is responsible for collecting, merging, and rendering two independent ownership signals — CODEOWNERS declarations and git-blame–derived contributor statistics — into a single structured wiki document. The three production files (`codeowners.rs`, `analysis.rs`, `render.rs`) cover respectively: parsing the CODEOWNERS file, running git blame to rank contributors, and serialising the combined result as YAML-fronted Markdown.

`codeowners.rs` locates and parses the project's CODEOWNERS file from up to three canonical paths (`CODEOWNERS`, `.github/CODEOWNERS`, `docs/CODEOWNERS`) and performs glob-aware, last-match-wins pattern matching against each input file path (codeowners.rs:14–26, codeowners.rs:48–64). `analysis.rs` discovers the git repository via `gix::discover`, computes a SHA-256 content hash for each file, and consults an `OwnershipMeta` cache before invoking `git blame` via a child process; results are written back to the cache so subsequent runs skip files whose content is unchanged (analysis.rs:22–75). A global blame timeout and a per-run `blame_file_cap` bound how many uncached files are processed in a single invocation; exceeding either limit marks the result as `partial` (analysis.rs:38–65). `render.rs` merges the two owner sets, computes YAML frontmatter including degradation flags, and emits wikilink-formatted Markdown referencing sibling module pages (render.rs:1–9, render.rs:36–60).

The public entry point consumed by the parent `codewiki` command is `build_ownership_doc`, which orchestrates all three sub-steps. The `OwnershipMeta` cache struct is serialised/deserialised by the caller; its `files` map stores `CachedBlameSummary` records keyed by file path, and contributor identities are stored only as opaque `contributor_id` hashes — raw email addresses are never persisted (tests.rs:56–62). The render layer calls into `gobby_core::codewiki_contract` for shared provenance constants (`GENERATED_BY_CODEWIKI`, `TRUST_GENERATED`, `FRESHNESS_INDEXED`) and uses sibling helpers `file_wikilink` / `module_wikilink` from the parent `codewiki` module (render.rs:6–7).

### Degradation Sources

The `degraded_sources` vector, emitted in frontmatter, is built from `OwnershipStatus` flags (render.rs:10–34):

| Degraded-source token | Condition |
|---|---|
| `codeowners_unavailable` | No CODEOWNERS file found in any search path |
| `git_blame_unavailable` | Repo not found or HEAD not resolvable |
| `git_blame_errors` | One or more blame sub-processes exited with an error |
| `git_blame_partial` | Timeout or `blame_file_cap` exhausted before all files processed |
| `ownership_unknown` | Every file has empty `declared` and `derived` owner lists |

### Runtime Options (`OwnershipOptions`)

| Field | Purpose |
|---|---|
| `blame_file_cap` | Maximum number of cache-miss files that will be blamed in a single run |
| `blame_timeout` | Wall-clock deadline shared across all blame sub-processes in one run |

### Key Public API Symbols

| Symbol | File | Role |
|---|---|---|
| `build_ownership_doc` | (parent mod) | Top-level entry point; calls `codeowners`, `analysis`, `render` |
| `derived_owners_for_files` | `analysis.rs:22` | Runs git blame, updates `OwnershipMeta` cache |
| `declared_owners_for_files` | `codeowners.rs:48` | Maps files → CODEOWNERS owners |
| `read_codeowners` | `codeowners.rs:14` | Discovers and parses CODEOWNERS |
| `degraded_sources` | `render.rs:10` | Computes degradation-flag list for frontmatter |
| `ownership_frontmatter` | `render.rs:37` | Serialises YAML frontmatter block |
| `OwnershipMeta` | (parent mod) | Persistent blame cache; must deserialise with `contributor_id` (tests.rs:64–76) |
| `OwnershipStatus` | (parent mod) | Accumulates per-run health flags fed to renderer |
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7]
[crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/analysis.rs\|crates/gcode/src/commands/codewiki/ownership/analysis.rs]] | `crates/gcode/src/commands/codewiki/ownership/analysis.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/codeowners.rs\|crates/gcode/src/commands/codewiki/ownership/codeowners.rs]] | `crates/gcode/src/commands/codewiki/ownership/codeowners.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/render.rs\|crates/gcode/src/commands/codewiki/ownership/render.rs]] | `crates/gcode/src/commands/codewiki/ownership/render.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/codewiki/ownership/tests.rs\|crates/gcode/src/commands/codewiki/ownership/tests.rs]] | `crates/gcode/src/commands/codewiki/ownership/tests.rs` exposes 13 indexed API symbols. |

