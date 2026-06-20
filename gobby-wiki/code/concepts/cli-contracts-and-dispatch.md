---
title: CLI Contracts and Dispatch
type: code_concept
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/audit.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/status.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/config/context.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/config/tests.rs
- file: crates/gcode/src/contract.rs
- file: crates/gcode/src/db/queries.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/index/languages.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcode/src/projection/sync.rs
- file: crates/gcode/src/search/fts/tests.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/visibility.rs
provenance_truncated: 189
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: Error-code metadata is not shown in the supplied contract excerpt.
- id: 3
  reason: Dispatch behavior is not shown in the supplied evidence.
- id: 6
  reason: The excluded command areas and the grep/search file references are not supported by the supplied excerpts.
- id: 10
  reason: Cross-component consumption of the contract is not shown in the supplied evidence.
- id: 11
  reason: The command-tree model and line ranges are not shown in the supplied excerpt.
- id: 12
  reason: No dispatch test evidence is supplied here, so the claimed responsibilities are unsupported.
- id: 18
  reason: The cited dispatch tests are not included in the supplied excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/contract/gcode.contract.json](crates/gcode/contract/gcode.contract.json)
- [crates/gcode/src/commands/codewiki/architecture_diagrams.rs](crates/gcode/src/commands/codewiki/architecture_diagrams.rs)
- [crates/gcode/src/commands/codewiki/build_parts/audit.rs](crates/gcode/src/commands/codewiki/build_parts/audit.rs)
- [crates/gcode/src/commands/codewiki/io.rs](crates/gcode/src/commands/codewiki/io.rs)
- [crates/gcode/src/commands/codewiki/prompts.rs](crates/gcode/src/commands/codewiki/prompts.rs)
- [crates/gcode/src/commands/codewiki/system_model.rs](crates/gcode/src/commands/codewiki/system_model.rs)
- [crates/gcode/src/commands/codewiki/text/sanitize.rs](crates/gcode/src/commands/codewiki/text/sanitize.rs)
- [crates/gcode/src/commands/codewiki/types.rs](crates/gcode/src/commands/codewiki/types.rs)
- [crates/gcode/src/commands/graph/lifecycle.rs](crates/gcode/src/commands/graph/lifecycle.rs)
- [crates/gcode/src/commands/graph/reads.rs](crates/gcode/src/commands/graph/reads.rs)
- [crates/gcode/src/commands/grep.rs](crates/gcode/src/commands/grep.rs)
- [crates/gcode/src/commands/search.rs](crates/gcode/src/commands/search.rs)

_207 more source files omitted._

</details>

# CLI Contracts and Dispatch

## Purpose

CLI Contracts and Dispatch is the boundary that makes `gcode` usable both as a human CLI and as a versioned tool surface for Gobby. The contract identifies the tool as `gcode`, sets `contract_version` to `2`, and describes it as a “Fast code index CLI for Gobby” . That static contract captures the invocation shape: global flags, scope behavior, commands, JSON output keys, and error-code metadata .

The CLI side parses the actual command line with Clap. `Cli` owns global options for project selection, output format, warning/log verbosity, freshness checks, and a required subcommand [crates/gcode/src/cli.rs:23-46]. Dispatch then sits after parsing: it turns parsed commands into early execution decisions, service-configuration requirements, and stderr logging behavior [crates/gcode/src/dispatch/tests.rs:5-9].

## Covers / Does not cover

This page covers the public command contract, the Clap CLI entry surface, the relationship between documented command metadata and actual command leaves, and the early dispatch role that decides how parsed commands proceed.

It does not cover the full implementation of search, grep, PostgreSQL index access, graph/vector projection lifecycle, setup, freshness, or visibility commands, except where those systems are reached through the shared CLI contract and command surface , .

| Surface | Covered here | Evidence |
| --- | --- | --- |
| Contract version and metadata | Yes |  |
| Global flags and scope rules | Yes |  |
| Clap top-level parser | Yes | [crates/gcode/src/cli.rs:23-46] |
| Command metadata parity tests | Yes | [crates/gcode/src/cli/tests.rs:12-30] |
| Full command implementations | No | ,  |

## Architecture

The architecture is split between a static contract and a runtime parser/dispatcher.

The static contract lives under `crates/gcode/contract` and is the documented interface that other Gobby components can consume. It defines the tool name, contract version, global flags, scope defaults, command metadata, JSON output keys, and error-code metadata . This gives the CLI a stable, inspectable surface separate from the Rust parser implementation.

The runtime CLI is defined in `crates/gcode/src/cli.rs`. `Cli` is the top-level Clap parser and contains global flags plus the required `Command` subcommand [crates/gcode/src/cli.rs:23-46], while `Command` and nested command enums model the command tree [crates/gcode/src/cli.rs:121-469]. Specialized enums such as `AiRouteArg`, `AiDepthArg`, and related value enums adapt CLI values into internal configuration types [crates/gcode/src/cli.rs:49-54], [crates/gcode/src/cli.rs:68-73].

The dispatch layer depends on parsed CLI state. Its tests show that dispatch collaborates with `Cli`, `effective_format`, and Clap parsing, then decides early execution behavior, service-configuration needs, and stderr logging , [crates/gcode/src/dispatch/tests.rs:5-9].

A test binds the static and runtime sides together: it walks every leaf command exposed by `Cli::command()` and verifies each one has a matching entry in `gobby_code::contract::contract().commands` [crates/gcode/src/cli/tests.rs:12-30]. That keeps the documented contract aligned with the actual command tree.

## Data flow

1. A user invokes `gcode` with global flags and a subcommand. Clap parses the invocation into `Cli`, including optional `--project`, `--format`, `--quiet`, `--verbose`, `--no-freshness`, and a required `Command` [crates/gcode/src/cli.rs:23-46].

2. The contract describes the same top-level surface for consumers. The global flags include `--project`, `--format`, `--quiet`, `--verbose`, and `--no-freshness`; `--format` allows `json` or `text` , [crates/gcode/contract/gcode.contract.json:18-21].

3. Scope resolution uses `--project` when supplied. If that dependency is unavailable because no project root was provided, the documented default is to detect the project from the current working directory .

4. Dispatch receives the parsed CLI command and resolves early behavior. The dispatch tests show it works with `Cli`, `effective_format`, and Clap `Parser`, and that its responsibility includes early execution decisions, service-configuration requirements, and stderr logging behavior , [crates/gcode/src/dispatch/tests.rs:5-9].

5. Some commands can be consumed early by the daemon-facing contract path. For example, the `contract` command is documented as emitting the CLI contract and has JSON output keys for the contract fields themselves .

6. Tests validate contract completeness by collecting every Clap command leaf and comparing those paths with `gobby_code::contract::contract().commands`. If any parsed leaf command is missing from the contract, the test fails with the missing command names [crates/gcode/src/cli/tests.rs:12-30].

## Key components

The main pieces are the static contract, the Clap parser, the command tree, and the parity test that prevents drift.

| Symbol / file | Role |
| --- | --- |
| `gcode.contract.json` | Versioned static contract for tool metadata, flags, scope, commands, JSON output keys, and errors  |
| `Cli` | Top-level Clap parser for global flags and required subcommand [crates/gcode/src/cli.rs:23-46] |
| `Command` | Main subcommand enum for the CLI command tree [crates/gcode/src/cli.rs:121-469] |
| `AiRouteArg` | CLI value enum converted into internal AI routing configuration [crates/gcode/src/cli.rs:49-54] |
| `clap_command_leaves_are_documented_in_contract` | Test ensuring every Clap leaf command is documented in the contract [crates/gcode/src/cli/tests.rs:12-30] |

## Where to start

Start with `Cli` to understand what a real invocation parses into, especially the global flags and required subcommand [crates/gcode/src/cli.rs:23-46]. Then read `gcode.contract.json` to see the versioned contract that external consumers rely on . Finally, read `clap_command_leaves_are_documented_in_contract` to understand how the implementation prevents the Clap command tree from drifting away from the documented contract [crates/gcode/src/cli/tests.rs:12-30].

## Explore

- [[code/modules/crates/gcode|crates/gcode]]
- [[code/modules/crates/gcode/contract|crates/gcode/contract]]
- [[code/modules/crates/gcode/src/cli|crates/gcode/src/cli]]
- [[code/modules/crates/gcode/src/dispatch|crates/gcode/src/dispatch]]

