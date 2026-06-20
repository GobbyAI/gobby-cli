---
title: crates/gcode/src/index/walker
type: code_module
provenance:
- file: crates/gcode/src/index/walker/classification.rs
- file: crates/gcode/src/index/walker/discovery.rs
- file: crates/gcode/src/index/walker/generated.rs
- file: crates/gcode/src/index/walker/hidden.rs
- file: crates/gcode/src/index/walker/tests.rs
- file: crates/gcode/src/index/walker/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker

Parent: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

The `crates/gcode/src/index/walker` module discovers and classifies project files for indexing. Its top-level flow walks a root with `gobby_core::indexing::WalkerSettings`, applying gitignore behavior from `DiscoveryOptions`, bounding file size with `MAX_FILE_SIZE`, and enabling hidden traversal before splitting files into AST candidates and content-only candidates (`discovery.rs:18-45`). It then adds hidden files that are explicitly allowlisted through `HiddenPathAllowlist::load(root).discover(root)`, deduplicating by canonical path before routing each file through `classify_file` (`discovery.rs:47-85`).

Classification is the policy layer. `classify_file` first rejects unsafe text, generated wiki metadata, and generated JavaScript bundles, then marks hidden metadata files as content-only (`classification.rs:14-31`). Language detection decides whether a safe file is AST-indexed or content-only: known languages normally become `FileClassification::Ast`, but oversized JSON/YAML-style data languages are downgraded to content-only to avoid excessive symbol output (`classification.rs:33-49`). Explicit single-file classification reuses the same policy while optionally checking gitignore visibility for just that path (`classification.rs:53-64`).

Hidden-file handling centers on `.gobby/gcode.json` plus a small default allowlist for Gobby plans, wiki markdown, and GitHub workflow YAML files (`hidden.rs:4-11`). The allowlist normalizes patterns, validates them, expands zero-depth globstars, resolves them against the root, and only returns files that are actually hidden relative to the root (`hidden.rs:17-46`). Generated JavaScript detection is deliberately bounded: it only applies to JS-family extensions, reads a prefix of the file, rejects files with generated markers, and treats sufficiently large minified-looking bundles as generated (`generated.rs:11-34`, `generated.rs:36-93`).

| Public API Symbol | Role | Evidence |
| --- | --- | --- |
| `discover_files` | Default discovery entry point returning AST and content-only absolute paths | `discovery.rs:10-16` |
| `discover_files_with_options` | Discovery entry point with `DiscoveryOptions` | `discovery.rs:18-58` |
| `classify_file` | Classifies one file as AST, content-only, or excluded | `classification.rs:14-50` |
| `classify_explicit_file_with_options` | Applies explicit-path visibility then classifies one file | `classification.rs:53-64` |
| `HiddenPathAllowlist::load` | Combines default and project hidden allowlist patterns | `hidden.rs:17-24` |
| `HiddenPathAllowlist::discover` | Expands allowlisted hidden paths under a root | `hidden.rs:33-46` |
| `is_generated_js_bundle` | Filters generated or minified JS-family bundles | `generated.rs:19-34` |

| Configuration / Constant | Meaning | Evidence |
| --- | --- | --- |
| `.gobby/gcode.json` | Project config path read for hidden allowlist patterns | `hidden.rs:4`, `hidden.rs:60-64` |
| `.gobby/plans/**/*.md` | Default hidden allowlist pattern | `hidden.rs:5-11` |
| `gobby-wiki/**/*.md` | Default hidden allowlist pattern | `hidden.rs:5-11` |
| `.github/workflows/**/*.yml` / `.yaml` | Default hidden allowlist patterns | `hidden.rs:5-11` |
| `GENERATED_JS_MARKER_SCAN_BYTES` | Prefix scan limit for generated markers | `generated.rs:4`, `generated.rs:49-55` |
| `GENERATED_JS_ANALYSIS_READ_BYTES` | Prefix read limit for bundle analysis | `generated.rs:5`, `generated.rs:26-28` |
| `MINIFIED_JS_MIN_BYTES` | Minimum size before minified-bundle heuristic applies | `generated.rs:6`, `generated.rs:31-34` |
[crates/gcode/src/index/walker/classification.rs:15-52]
[crates/gcode/src/index/walker/discovery.rs:12-17]
[crates/gcode/src/index/walker/generated.rs:18-38]
[crates/gcode/src/index/walker/hidden.rs:13-15]
[crates/gcode/src/index/walker/tests.rs:11-17]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/walker/classification.rs\|crates/gcode/src/index/walker/classification.rs]] | `crates/gcode/src/index/walker/classification.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/walker/discovery.rs\|crates/gcode/src/index/walker/discovery.rs]] | `crates/gcode/src/index/walker/discovery.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/index/walker/generated.rs\|crates/gcode/src/index/walker/generated.rs]] | `crates/gcode/src/index/walker/generated.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/walker/hidden.rs\|crates/gcode/src/index/walker/hidden.rs]] | `crates/gcode/src/index/walker/hidden.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/index/walker/tests.rs\|crates/gcode/src/index/walker/tests.rs]] | `crates/gcode/src/index/walker/tests.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/index/walker/types.rs\|crates/gcode/src/index/walker/types.rs]] | `crates/gcode/src/index/walker/types.rs` exposes 3 indexed API symbols. |

