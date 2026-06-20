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

The ownership module builds CodeWiki ownership documentation by combining declared CODEOWNERS data with derived Git blame contributors. Its tests show the main flow through `build_ownership_doc`, which receives a project root, file list, module map, mutable `OwnershipMeta`, and `OwnershipOptions`, then emits `type: code_ownership`, module wikilinks, declared owners, contributor summaries, and degradation markers when sources are unavailable (`tests.rs:1-100`).

The analysis path discovers a Git repository, resolves HEAD, hashes file content, reuses cached contributor summaries when hashes match, and otherwise runs blame within a file cap and timeout. It records partial status when time or cap limits are reached, and caches successful blame summaries into `OwnershipMeta` (`analysis.rs:1-100`). CODEOWNERS handling searches standard locations, parses non-comment owner entries, and applies the last matching rule per file (`codeowners.rs:1-100`).

Rendering turns ownership status into frontmatter and body-level degradation signals. It imports CodeWiki wikilink helpers from the parent module, deterministic identity retention from analysis, and shared ownership structs; frontmatter uses `gobby_core::codewiki_contract` constants for generated/trust/freshness metadata (`render.rs:1-100`). The module therefore sits between repository/file inspection, ownership-source parsing, cached metadata, and CodeWiki document rendering.

| Symbol | Kind | Role |
| --- | --- | --- |
| `read_codeowners` | function | Finds and parses `CODEOWNERS`, `.github/CODEOWNERS`, or `docs/CODEOWNERS` (`codeowners.rs:1-100`) |
| `declared_owners_for_files` | function | Maps files to declared owners using CODEOWNERS rule precedence (`codeowners.rs:1-100`) |
| `derived_owners_for_files` | function | Computes or reuses Git-blame contributor summaries (`analysis.rs:1-100`) |
| `degraded_sources` | function | Produces degradation labels such as unavailable blame or unknown ownership (`render.rs:1-100`) |
| `ownership_frontmatter` | function | Serializes ownership document YAML frontmatter (`render.rs:1-100`) |

| Option / Status | Purpose |
| --- | --- |
| `blame_file_cap` | Limits uncached blame work; cap hits mark output partial (`analysis.rs:1-100`, `tests.rs:1-100`) |
| `blame_timeout` | Bounds total blame analysis time (`analysis.rs:1-100`, `tests.rs:1-100`) |
| `codeowners_available` | Controls `codeowners_unavailable` degradation (`render.rs:1-100`) |
| `blame_available` | Controls `git_blame_unavailable` degradation (`render.rs:1-100`) |
| `partial` | Marks partial blame output and frontmatter (`render.rs:1-100`) |
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

