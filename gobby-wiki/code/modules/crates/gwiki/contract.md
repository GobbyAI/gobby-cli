---
title: crates/gwiki/contract
type: code_module
provenance:
- file: crates/gwiki/contract/gwiki.contract.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/contract

Parent: [[code/modules/crates/gwiki|crates/gwiki]]

## Overview

## crates/gwiki/contract

This module contains the single machine-readable source of truth for the `gwiki` CLI's public API surface: `gwiki.contract.json`. The file is a versioned (currently `contract_version: 5`) JSON document that declares every command the tool exposes, together with its positional arguments, flags, allowed values, structured output keys, dependency requirements, and error codes. The top-level `summary` field — "Local-first wiki CLI for capture, search, upkeep, and synthesis." — serves as the human-readable elevator pitch for the tool. With 429 indexed symbols spread across the file, the contract is the definitive reference consulted by the daemon, shell completions, documentation generators, and any other consumers that need to understand what `gwiki` can do without executing it.

The schema is organised into three top-level concerns. `global_flags` applies to every invocation (`--format json|text`, `--quiet`). The `scope` object holds the two workspace-narrowing flags (`--project ROOT`, `--topic NAME`) and records how scope is resolved when neither flag is supplied ("detect project from current working directory; bare `--project` uses current directory"); it also names the `identity_keys` used to deduplicate results (`kind`, `id`). The `commands` array is the largest section; each entry carries a `name`, human-readable `summary`, a `daemon_consumed` boolean that tells callers whether a running background service will handle the request, optional `positionals` and per-command `flags` arrays, and a `json_output_keys` list that documents the exact keys present in JSON-mode output. A subset of commands additionally declare `hard_dependencies`, `optional_dependencies`, `multimodal`, `degradation`, `output_shape`, and `metadata_keys` fields, signalling richer structured results and graceful-degradation behaviour for capabilities such as image or audio processing. The `error_codes` top-level key enumerates the well-known error identifiers the daemon can return.

The `contract` command itself (`daemon_consumed: true`) re-emits the full document at runtime, bridging the static file and the live binary. Its `json_output_keys` — `tool`, `contract_version`, `summary`, `global_flags`, `scope`, `commands`, `error_codes` — mirror the top-level structure of this file exactly (gwiki.contract.json:1–83). Other commands visible in the excerpt include `index` (indexes markdown and source notes, outputs `command`, `scope`, `status`, `indexed_pages`, `indexed_sources`) and `search` (queries wiki documents in the selected scope), with the remainder of the command roster spanning capture, upkeep, and synthesis workflows implied by the 429 total symbols.

### Global Flags

| Flag | Takes Value | Allowed Values | Required | Repeatable |
|---|---|---|---|---|
| `--format` | yes | `json`, `text` | no | no |
| `--quiet` | no | — | no | no |

### Scope Flags

| Flag | Value Name | Required | Default Behaviour |
|---|---|---|---|
| `--project` | `ROOT` | no | Detect from Cwd; bare flag uses Cwd |
| `--topic` | `NAME` | no | — |

| Scope Property | Value |
|---|---|
| `identity_keys` | `kind`, `id` |

### Known Commands (from excerpt)

| Command | Summary | daemon_consumed | Notable json_output_keys |
|---|---|---|---|
| `contract` | Emit this CLI contract | yes | `tool`, `contract_version`, `summary`, `global_flags`, `scope`, `commands`, `error_codes` |
| `index` | Index markdown and source notes in the selected scope | yes | `command`, `scope`, `status`, `indexed_pages`, `indexed_sources` |
| `search` | Search wiki documents in the selected scope | yes | (defined in full contract) |

### Optional Command-Level Schema Fields

| Field | Purpose |
|---|---|
| `hard_dependencies` | External capabilities required for the command to function |
| `optional_dependencies` | Capabilities that enhance but are not required |
| `multimodal` | Whether the command handles non-text media |
| `degradation` | Describes behaviour when optional dependencies are absent |
| `output_shape` | Structural shape of the primary result payload |
| `metadata_keys` | Additional envelope keys alongside the primary output |
| `error_codes` | Well-known error identifiers the daemon may return |
[crates/gwiki/contract/gwiki.contract.json:2]
[crates/gwiki/contract/gwiki.contract.json:3]
[crates/gwiki/contract/gwiki.contract.json:4]
[crates/gwiki/contract/gwiki.contract.json:5-25]
[crates/gwiki/contract/gwiki.contract.json:7]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/contract/gwiki.contract.json\|crates/gwiki/contract/gwiki.contract.json]] | `crates/gwiki/contract/gwiki.contract.json` exposes 429 indexed API symbols. |

