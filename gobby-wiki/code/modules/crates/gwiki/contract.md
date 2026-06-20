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

The `crates/gwiki/contract` module defines the static CLI contract for `gwiki`: tool identity, contract version, global flags, scope selection, commands, JSON output shapes, and error-code surface. The contract identifies `gwiki` as a local-first wiki CLI for capture, search, upkeep, and synthesis (`crates/gwiki/contract/gwiki.contract.json:2-4`), with the supplied file summary indicating 429 indexed API symbols.

The key flow is scope resolution followed by command execution. Scope defaults to project detection from the current working directory, can be narrowed with `--project ROOT` or `--topic NAME`, and uses `kind` plus `id` as identity keys (`crates/gwiki/contract/gwiki.contract.json:26-49`). The visible commands expose self-description through `contract`, indexing through `index`, and scoped document lookup through `search` (`crates/gwiki/contract/gwiki.contract.json:51-100`).

No cross-file relationship data was supplied for callers, imports, or downstream Rust modules. The collaboration point visible here is daemon integration: the shown commands are marked `daemon_consumed: true`, so daemon-facing code can use this contract to discover supported commands and expected JSON keys (`crates/gwiki/contract/gwiki.contract.json:53-78`, `crates/gwiki/contract/gwiki.contract.json:81-92`, `crates/gwiki/contract/gwiki.contract.json:95-100`).

| Contract Fact | Value | Source |
| --- | --- | --- |
| Tool | `gwiki` | `crates/gwiki/contract/gwiki.contract.json:2` |
| Contract version | `5` | `crates/gwiki/contract/gwiki.contract.json:3` |
| Summary | Local-first wiki CLI for capture, search, upkeep, and synthesis | `crates/gwiki/contract/gwiki.contract.json:4` |

| Flag | Scope | Value | Allowed Values | Source |
| --- | --- | --- | --- | --- |
| `--format` | Global / `contract` | `json\|text` | `json`, `text` | `crates/gwiki/contract/gwiki.contract.json:7-16`, `crates/gwiki/contract/gwiki.contract.json:59-68` |
| `--quiet` | Global | none | none | `crates/gwiki/contract/gwiki.contract.json:18-24` |
| `--project` | Scope | `ROOT` | unrestricted | `crates/gwiki/contract/gwiki.contract.json:29-35` |
| `--topic` | Scope | `NAME` | unrestricted | `crates/gwiki/contract/gwiki.contract.json:37-43` |

| Command | Responsibility | Daemon Consumed | Visible JSON Keys / Inputs | Source |
| --- | --- | --- | --- | --- |
| `contract` | Emit this CLI contract | yes | `tool`, `contract_version`, `summary`, `global_flags`, `scope`, `commands`, `error_codes` | `crates/gwiki/contract/gwiki.contract.json:53-78` |
| `index` | Index markdown and source notes in selected scope | yes | `command`, `scope`, `status`, `indexed_pages`, `indexed_sources` | `crates/gwiki/contract/gwiki.contract.json:81-92` |
| `search` | Search wiki documents in selected scope | yes | begins with positional `QUERY` | `crates/gwiki/contract/gwiki.contract.json:95-100` |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/contract/gwiki.contract.json\|crates/gwiki/contract/gwiki.contract.json]] | `crates/gwiki/contract/gwiki.contract.json` exposes 429 indexed API symbols. |

