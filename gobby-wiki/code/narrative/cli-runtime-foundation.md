---
title: CLI Runtime Foundation
type: code_narrative
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
  reason: '`error_codes` metadata is not shown in the supplied contract excerpt.'
- id: 4
  reason: Claims about `context.rs`, `db/mod.rs`, and `setup/contracts.rs` are not supported by the provided excerpts.
- id: 9
  reason: '`dispatch/tests.rs` and the described dispatch behavior are not shown in the supplied evidence.'
- id: 10
  reason: The config resolution order from `context.rs` is not shown in the provided excerpt.
- id: 11
  reason: '`db/mod.rs` and `db/queries.rs` behavior is not shown in the supplied evidence.'
- id: 16
  reason: The `gcode.contract.json` row mentions `error_codes`, and the `Command` row cites lines not included in the excerpt.
- id: 18
  reason: '`commands/grep.rs` and `commands/search.rs` are not provided, so the search/text-lookup claim is unsupported.'
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

# CLI Runtime Foundation

## Why this matters

The CLI runtime foundation is where `gcode` turns “run this command in this workspace” into a stable, versioned operation. The design decision is to treat the CLI as both a Rust command parser and a published contract: `gcode.contract.json` declares `tool: "gcode"`, `contract_version: 2`, and the summary “Fast code index CLI for Gobby” . That contract records global flags, scope behavior, commands, JSON output keys, and error-code metadata .

This matters because the CLI is not only for humans. Some commands are marked as daemon-consumed, output formats are explicit, and project identity is part of the runtime scope . The Rust side reinforces that contract: tests walk the Clap command tree and fail if a leaf command is missing from the generated contract [crates/gcode/src/cli/tests.rs:12-30]. In other words, the command surface is intentionally versioned and checked instead of being an accidental byproduct of parser code.

From there, runtime setup fans out into three foundations: project/config context, PostgreSQL access, and optional standalone provisioning. The config layer documents resolution through `bootstrap.yaml -> PostgreSQL hub -> config_store -> service configs`, with `$secret:NAME` and `${VAR}` expansion [crates/gcode/src/config/context.rs:26-31]. The database boundary resolves the hub PostgreSQL DSN, opens read/write or read-only connections, validates schema, and re-exports query/resolution APIs [crates/gcode/src/db/mod.rs:16-20]. If the code index needs to be created independently, setup owns the standalone PostgreSQL path [crates/gcode/src/setup/contracts.rs:5-8].

## How it works

1. `gcode` starts from a versioned contract surface. The contract names the tool, pins `contract_version` to `2`, and describes the command-line interface as a “Fast code index CLI for Gobby” . It also defines global flags such as `--project`, `--format`, `--quiet`, `--verbose`, and `--no-freshness` [crates/gcode/contract/gcode.contract.json:5-39].

2. Clap parses the concrete invocation into `Cli`. The top-level `Cli` struct carries the project override, output format, warning/logging controls, freshness behavior, and one required `Command` subcommand [crates/gcode/src/cli.rs:23-46]. This is the runtime shape corresponding to the public contract.

3. Project scope is resolved around the project root. The contract says `--project ROOT` can override scope, otherwise the default is to “detect project from current working directory,” and identity is tracked with `project_id` and `project_root` . The config facade exposes project-root detection, project identity resolution, identity warning, and project index scope symbols for the rest of the CLI [crates/gcode/src/config.rs:7-14].

4. Dispatch decides how early execution should proceed. The `dispatch` module turns parsed CLI commands into early execution decisions, service-configuration requirements, and stderr logging behavior; its tests collaborate with CLI parsing and output format resolution through `Cli` and `effective_format` . This is where a parsed command becomes a runtime decision rather than just syntax.

5. Configuration is resolved through the shared gcode config layer. The documented order is `bootstrap.yaml -> PostgreSQL hub -> config_store -> service configs`, including `$secret:NAME` and `${VAR}` expansion [crates/gcode/src/config/context.rs:26-31]. The public facade re-exports service settings and constants such as FalkorDB environment/config keys, Qdrant config, embedding config, code-vector settings, and project identity types [crates/gcode/src/config.rs:7-14].

6. PostgreSQL access is centralized behind the `db` boundary. That module resolves the hub PostgreSQL DSN, opens read/write or read-only connections, validates the runtime schema, delegates config reads to `gobby_core`, and re-exports query and resolution APIs [crates/gcode/src/db/mod.rs:16-20]. Its query layer reads indexed files, project/file existence, graph facts, and graph sync state from hub tables such as `code_indexed_files` and `code_indexed_projects` .

7. Commands that need code-index storage rely on the standalone setup path when provisioning is required. `run_standalone_setup` validates the request, creates a `GcodeStandaloneSetup`, starts a PostgreSQL transaction, and then either resets existing gcode-owned relations when `overwrite_code_index` is true or checks compatibility when it is false [crates/gcode/src/setup/postgres.rs:12-35].

8. Setup failure behavior is explicit. If overwrite reset fails, the reset failure is recorded and returned as setup status without continuing [crates/gcode/src/setup/postgres.rs:22-28]. If creation succeeds with no failures, the transaction commits; if setup reports failures, created and skipped objects are cleared before status is returned [crates/gcode/src/setup/postgres.rs:39-53].

9. The standalone DDL object owns schema-qualified PostgreSQL definitions. `GcodeStandaloneSetup` stores the schema [crates/gcode/src/setup/ddl.rs:8-10], qualifies relations before emitting SQL [crates/gcode/src/setup/ddl.rs:31-34], and builds definitions for `pg_search` plus code-index tables including `code_indexed_projects`, `code_indexed_files`, `code_symbols`, `code_content_chunks`, `code_imports`, and `code_calls` .

## Key components

| Symbol | Role |
| --- | --- |
| `gcode.contract.json` | Versioned public CLI contract with global flags, scope, commands, JSON keys, and error metadata . |
| `Cli` | Clap-parsed top-level runtime config: project, format, quiet/verbose, freshness, and required subcommand [crates/gcode/src/cli.rs:23-46]. |
| `Command` | Main subcommand enum behind the required `Cli.command` field [crates/gcode/src/cli.rs:121-469]. |
| `clap_command_leaves_are_documented_in_contract` | Test that keeps Clap leaf commands synchronized with the generated contract [crates/gcode/src/cli/tests.rs:12-30]. |
| `Context` and config exports | Project identity, root detection, service settings, and validation facade for runtime configuration [crates/gcode/src/config.rs:7-17]. |
| `GcodeStandaloneSetup` | Schema-owning standalone setup object that emits PostgreSQL code-index definitions [crates/gcode/src/setup/ddl.rs:8-10]. |
| `IndexContract` | Static contract for expected index name, target table, and method [crates/gcode/src/setup/contracts.rs:10-14]. |
| `PostgresObjectDefinition` | Name plus raw SQL for a PostgreSQL object emitted by setup [crates/gcode/src/setup/ddl.rs:13-16]. |

## What to read next

Read the command-specific `search` and `grep` chapters next, because this runtime foundation leads directly into the application layer that performs indexed search and text lookup , .

## Concepts

- [[code/concepts/cli-contracts-and-dispatch|CLI Contracts and Dispatch]]
- [[code/concepts/configuration-and-postgresql-setup|Configuration and PostgreSQL Setup]]

## Explore

- [[code/modules/crates/gcode/contract|crates/gcode/contract]]
- [[code/modules/crates/gcode/src/cli|crates/gcode/src/cli]]
- [[code/modules/crates/gcode/src/dispatch|crates/gcode/src/dispatch]]
- [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]
- [[code/modules/crates/gcode/src/db|crates/gcode/src/db]]
- [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Continue the tour

- ← Previous: [[code/narrative/data-flow|Data Flow]]
- Next →: [[code/narrative/building-the-code-index|Building the Code Index]]

