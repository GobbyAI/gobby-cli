---
title: Architecture
type: code_narrative
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai_context.rs
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
- file: crates/gwiki/contract/gwiki.contract.json
- file: crates/gwiki/src/ai/chunk.rs
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/collect.rs
- file: crates/gwiki/src/commands/citation_quality.rs
- file: crates/gwiki/src/commands/sources.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/session.rs
- file: crates/gwiki/src/links.rs
- file: crates/gwiki/src/main.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/vector.rs
provenance_truncated: 442
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 3
  reason: The error-code metadata claim is not shown in the provided excerpt.
- id: 4
  reason: Indexing and import-resolution behavior are not evidenced in the supplied excerpts.
- id: 11
  reason: The config resolution order and DB boundary details are not shown in the provided excerpts.
- id: 19
  reason: The indexer and walker behavior is not evidenced in the supplied excerpts.
- id: 21
  reason: The lookup-state claim is not shown in the provided excerpt.
- id: 23
  reason: The call-input and semantic-input claim is not evidenced; only syntax classification/fallback is shown.
- id: 25
  reason: The `Command` row is not supported by the provided excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/contract/gcode.contract.json](crates/gcode/contract/gcode.contract.json)
- [crates/gcode/src/commands/codewiki/prompts.rs](crates/gcode/src/commands/codewiki/prompts.rs)
- [crates/gcode/src/commands/codewiki/types.rs](crates/gcode/src/commands/codewiki/types.rs)
- [crates/gcode/src/commands/graph/reads.rs](crates/gcode/src/commands/graph/reads.rs)
- [crates/gcode/src/commands/grep.rs](crates/gcode/src/commands/grep.rs)
- [crates/gcode/src/commands/search.rs](crates/gcode/src/commands/search.rs)
- [crates/gcode/src/commands/symbol_at.rs](crates/gcode/src/commands/symbol_at.rs)
- [crates/gcode/src/config/services.rs](crates/gcode/src/config/services.rs)
- [crates/gcode/src/db/resolution.rs](crates/gcode/src/db/resolution.rs)
- [crates/gcode/src/index/semantic.rs](crates/gcode/src/index/semantic.rs)
- [crates/gcode/src/models.rs](crates/gcode/src/models.rs)
- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)

_460 more source files omitted._

</details>

# Architecture

## Why this matters

This architecture is built around a clear split: `gcode` is the fast code-index CLI, while `gcore` supplies shared services and deployment assets. The CLI contract makes that boundary explicit: the tool is named `gcode`, uses contract version 2, and describes itself as a “Fast code index CLI for Gobby” .

The main design decision is contract-first orchestration. The CLI surface, global flags, scope rules, commands, JSON output keys, and error-code metadata are centralized in the static contract , while the Rust CLI mirrors those globals through `Cli`: project root, output format, quiet/verbose logging, freshness checks, and a required subcommand [crates/gcode/src/cli.rs:23-46]. That lets daemon-facing code and human-facing commands share one documented interface.

Around that contract, the system separates responsibilities: setup creates the PostgreSQL code-index schema, indexing discovers and persists code facts, import resolution enriches cross-file knowledge, and `gcore` provides local service assets such as FalkorDB, Qdrant, and PostgreSQL .

## How it works

1. The user enters through the `gcode` CLI.

   `Cli` is Clap-parsed and defines the top-level global options: `--project`, `--format`, `--quiet`, `--verbose`, and `--no-freshness`, plus a required `Command` subcommand [crates/gcode/src/cli.rs:23-46]. The contract records the same global flags, including allowed `--format` values of `json` and `text` [crates/gcode/contract/gcode.contract.json:5-43].

2. Project scope is resolved before command work begins.

   The contract says `--project` can override the root, otherwise the default is to “detect project from current working directory,” with identity carried by `project_id` and `project_root` . This keeps every command tied to an explicit codebase identity.

3. Service configuration and storage sit behind boundaries.

   The configuration layer documents a resolution order of `bootstrap.yaml -> PostgreSQL hub -> config_store -> service configs`, including `$secret:NAME` and `${VAR}` expansion [crates/gcode/src/config/context.rs:26-31]. The database boundary resolves the hub PostgreSQL DSN, opens connections, validates schema, and re-exports query/resolution APIs [crates/gcode/src/db/mod.rs:16-20].

4. Local services come from shared `gcore` assets.

   The Compose asset is installed by `gobby install` and managed through daemon start/stop profiles . It defines services for FalkorDB, Qdrant, and PostgreSQL, with health checks, persistent volumes, restart policy, and configurable ports [crates/gcore/assets/docker-compose.services.yml:5-46]. PostgreSQL is configured with `pg_search` and audit logging, including `GOBBY_PGAUDIT_LOG` [crates/gcore/assets/docker-compose.services.yml:87].

5. Standalone setup prepares the code-index schema transactionally.

   `run_standalone_setup` validates the request, creates a `GcodeStandaloneSetup`, opens a transaction, optionally resets the code index on overwrite, otherwise checks compatibility, then calls `setup.create` [crates/gcode/src/setup/postgres.rs:12-44]. If creation succeeds with no failures, it commits; if failures exist, it clears created/skipped report entries instead of reporting partial success [crates/gcode/src/setup/postgres.rs:45-57].

6. The DDL layer defines the actual PostgreSQL objects.

   `GcodeStandaloneSetup` stores the target schema [crates/gcode/src/setup/ddl.rs:8-10], qualifies relation names, and builds object definitions for `pg_search` plus tables such as `code_indexed_projects`, `code_indexed_files`, `code_symbols`, `code_content_chunks`, `code_imports`, and `code_calls` .

7. Indexing discovers files, classifies them, and writes facts.

   The indexer’s single-file path derives a relative path, parses with semantic resolution, detects language, hashes content, reads metadata, and writes transactional facts through `PostgresCodeFactSink` [crates/gcode/src/index/indexer/file.rs:15-91]. The walker side discovers files with configured walker settings, gitignore behavior, file-size limits, and hidden-file handling before splitting files into AST and content-only candidates [crates/gcode/src/index/walker/classification.rs:15-52].

8. Import resolution adds language-specific context.

   Import resolution keeps lookup state for local modules, external packages, candidate files, and language-specific maps [crates/gcode/src/index/import_resolution/context.rs:41-138]. JavaScript package loading reads `package.json`; if the file is missing or invalid JSON, it falls back to an empty package set [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-18]. Static import-root registries cover ecosystem conventions such as `jason` mapping to `Jason` in Elixir .

9. Call extraction records relationships between symbols.

   Call parsing produces call relationships from source, symbols, import context, and optional semantic inputs [crates/gcode/src/index/parser/calls.rs:26-35]. `CallSyntaxKind` classifies syntax as `Bare`, `Member`, or `Other` [crates/gcode/src/index/parser/calls/resolution.rs:6-10]. When ancestry is missing or does not match the expected call shape, resolution falls back to `Other` .

## Key components

| Symbol | Role | Where |
| --- | --- | --- |
| `Cli` | Top-level parsed CLI options and required subcommand. | [crates/gcode/src/cli.rs:23-46] |
| `Command` | Main command enum behind the CLI contract. | [crates/gcode/src/cli.rs:121-469] |
| `GcodeStandaloneSetup` | Owns standalone PostgreSQL schema setup for the code index. | [crates/gcode/src/setup/ddl.rs:8-10] |
| `CallSyntaxKind` | Classifies call syntax during call-resolution work. | [crates/gcode/src/index/parser/calls/resolution.rs:6-10] |
| `GOBBY_PGAUDIT_LOG` | Compose-level PostgreSQL audit logging setting. | [crates/gcore/assets/docker-compose.services.yml:87] |

## What to read next

Read the CLI contract reference next. It is the best bridge from architecture into concrete behavior because it names the tool, contract version, global flags, scope model, commands, and JSON output keys in one place .

## Concepts

- [[code/concepts/workspace-map|Workspace Map]]
- [[code/concepts/shared-service-substrate|Shared Service Substrate]]
- [[code/concepts/cli-contracts-and-dispatch|CLI Contracts and Dispatch]]
- [[code/concepts/configuration-and-postgresql-setup|Configuration and PostgreSQL Setup]]
- [[code/concepts/file-discovery-and-indexing|File Discovery and Indexing]]
- [[code/concepts/import-and-call-resolution|Import and Call Resolution]]

## Continue the tour

- ← Previous: [[code/narrative/introduction|System Orientation]]
- Next →: [[code/narrative/data-flow|Data Flow]]

