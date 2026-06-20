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

`crates/gcode/contract` is the static contract surface for the `gcode` CLI, identified as contract version 2 and summarized as a “Fast code index CLI for Gobby” (crates/gcode/contract/gcode.contract.json:1-4). It centralizes the tool’s invocation schema: global flags, scope resolution, commands, JSON output keys, and error-code metadata (crates/gcode/contract/gcode.contract.json:5-94).

Project context is modeled through a scoped `--project ROOT` flag, with the default behavior detecting the project from the current working directory and stable identity keys of `project_id` and `project_root` (crates/gcode/contract/gcode.contract.json:50-65). The visible command flow starts with `contract`, which emits the CLI contract and is marked daemon-consumed, while `init` initializes project context for the current repository and is not daemon-consumed (crates/gcode/contract/gcode.contract.json:67-100).

| Global flag | Value | Allowed values | Required | Repeatable | Source |
| --- | --- | --- | --- | --- | --- |
| `--project` | `ROOT` | none | no | no | crates/gcode/contract/gcode.contract.json:6-13 |
| `--format` | `json\|text` | `json`, `text` | no | no | crates/gcode/contract/gcode.contract.json:14-24 |
| `--quiet` | none | none | no | no | crates/gcode/contract/gcode.contract.json:25-32 |
| `--verbose` | none | none | no | no | crates/gcode/contract/gcode.contract.json:33-40 |
| `--no-freshness` | none | none | no | no | crates/gcode/contract/gcode.contract.json:41-48 |

| Command | Responsibility | Daemon consumed | Notable output/flags | Source |
| --- | --- | --- | --- | --- |
| `contract` | Emit this CLI contract | yes | `--format`; outputs `tool`, `contract_version`, `summary`, `global_flags`, `scope`, `commands`, `error_codes` | crates/gcode/contract/gcode.contract.json:68-94 |
| `init` | Initialize project context for the current repository | no | no positionals shown in excerpt | crates/gcode/contract/gcode.contract.json:96-100 |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/contract/gcode.contract.json\|crates/gcode/contract/gcode.contract.json]] | `crates/gcode/contract/gcode.contract.json` exposes 988 indexed API symbols. |

