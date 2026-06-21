---
title: crates/gcode/contract
type: code_module
provenance:
- file: crates/gcode/contract/gcode.contract.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/contract

Parent: [[code/modules/crates/gcode|crates/gcode]]

## Overview

## crates/gcode/contract

The `contract` module contains a single authoritative JSON artifact — `gcode.contract.json` — that serves as the machine-readable specification for the entire `gcode` CLI surface (gcode.contract.json:1-5). It declares the tool identity (`"tool": "gcode"`), the schema revision (`"contract_version": 2`), a human-readable summary (`"Fast code index CLI for Gobby."`), and three top-level sections: `global_flags`, `scope`, and `commands`. The file indexes 988 named API symbols, making it the single source of truth for every flag, positional argument, allowed value set, and JSON output key shape exposed by the tool.

The `scope` block (gcode.contract.json:54-65) governs how `gcode` resolves its project context. It re-exposes the `--project ROOT` flag, provides a human-readable default (`"detect project from current working directory"`), and enumerates the canonical identity keys (`project_id`, `project_root`) that uniquely identify a project session. The `commands` array (gcode.contract.json:67-100+) enumerates every sub-command, each carrying a `name`, `summary`, a `daemon_consumed` boolean indicating whether a background daemon services the request, typed `positionals`, per-command `flags`, and a `json_output_keys` list that specifies which fields appear in structured JSON output. The `contract` command itself is flagged `daemon_consumed: true` and emits the full schema as its JSON payload (gcode.contract.json:69-100).

Because no cross-file relationships were supplied, the contract is consumed passively — external tooling, shell-completion generators, documentation pipelines, or runtime CLI parsers read this file to discover the full API without inspecting compiled binaries. The file itself imports nothing and calls nothing; it is a pure data artifact.

### Global Flags

| Flag | Takes Value | Value / Allowed Values | Required | Repeatable |
|---|---|---|---|---|
| `--project` | yes | `ROOT` (free-form) | no | no |
| `--format` | yes | `json`, `text` | no | no |
| `--quiet` | no | — | no | no |
| `--verbose` | no | — | no | no |
| `--no-freshness` | no | — | no | no |

### Scope Configuration

| Property | Value |
|---|---|
| Scoping flag | `--project ROOT` |
| Default resolution | detect project from current working directory |
| Identity keys | `project_id`, `project_root` |

### Selected Commands (from contract excerpt)

| Command | Summary | Daemon Consumed | JSON Output Keys |
|---|---|---|---|
| `contract` | Emit this CLI contract. | yes | `tool`, `contract_version`, `summary`, `global_flags`, `scope`, `commands`, `error_codes` |
| `init` | Initialize project context for the current repository. | no | — (positionals-based) |

Per-command entries follow a uniform schema: each flag descriptor carries `name`, `takes_value`, `value_name`, `allowed_values`, `required`, and `repeatable` fields (gcode.contract.json:72-83), and each positional carries `name`, `required`, and `repeatable`. The full set of ~988 indexed symbols spans all commands across those repeated descriptor shapes.
[crates/gcode/contract/gcode.contract.json:2]
[crates/gcode/contract/gcode.contract.json:3]
[crates/gcode/contract/gcode.contract.json:4]
[crates/gcode/contract/gcode.contract.json:5-49]
[crates/gcode/contract/gcode.contract.json:7]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/contract/gcode.contract.json\|crates/gcode/contract/gcode.contract.json]] | `crates/gcode/contract/gcode.contract.json` exposes 988 indexed API symbols. |

