---
title: Data Flow
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

# Data Flow

## Why this matters

The data flow in `gcode` turns a local codebase into a stable, queryable code index. The design starts with a declared CLI contract, then carries project files through discovery, language-aware parsing, import/call resolution, and PostgreSQL persistence. That lets Gobby treat the CLI as a reliable boundary: commands, flags, JSON keys, and scope rules are described in one static contract instead of being inferred from runtime behavior .

The key design decision is separation of responsibilities. The CLI owns user intent and project scope, setup owns the storage contract, the walker/indexer owns file-to-fact conversion, import resolution owns language-specific lookup context, and shared `gcore` assets provide the backing local services [crates/gcode/src/cli.rs:23-46] [crates/gcode/src/setup/ddl.rs:8-10] [crates/gcore/assets/docker-compose.services.yml:5-117].

## How it works

1. A user enters through the `gcode` CLI. The contract identifies the tool as `gcode`, contract version `2`, with the summary “Fast code index CLI for Gobby” . The real Clap entry point is `Cli`, which accepts global options for project root, output format, quiet or verbose logging, freshness checks, and then requires a `Command` subcommand [crates/gcode/src/cli.rs:23-46].

2. Project scope is resolved before data is read or written. The contract says `--project ROOT` can override the scope, otherwise the default is to “detect project from current working directory,” with `project_id` and `project_root` as identity keys . This keeps every indexed fact tied back to a project identity.

3. The local service layer supplies the backing stores. `gcore` packages Docker Compose services for FalkorDB, Qdrant, and PostgreSQL, each under profiles with persistent volumes and health checks [crates/gcore/assets/docker-compose.services.yml:5-46]. PostgreSQL is configured with `pg_search` and audit logging options, including `pgaudit.log=${GOBBY_PGAUDIT_LOG:-ddl}` [crates/gcore/assets/docker-compose.services.yml:53-70].

4. Standalone setup prepares the PostgreSQL code index. `run_standalone_setup` validates the request, creates a `GcodeStandaloneSetup`, opens a transaction, optionally resets an existing code index, otherwise checks compatibility, then calls `setup.create` through a `SetupContext` [crates/gcode/src/setup/postgres.rs:12-43]. It commits only when the setup report has no failures; if failures exist, created and skipped entries are cleared before returning status [crates/gcode/src/setup/postgres.rs:44-57].

5. The schema defines where indexed facts land. `GcodeStandaloneSetup` stores the target schema and builds qualified PostgreSQL object definitions . Its DDL includes `pg_search` plus tables such as `code_indexed_projects`, `code_indexed_files`, `code_symbols`, `code_content_chunks`, `code_imports`, and `code_calls` .

6. File discovery and classification split the project into indexing paths. The walker uses project settings, gitignore behavior, file-size bounds, hidden traversal, and an explicit hidden-path allowlist before routing files through `classify_file` [crates/gcode/src/index/walker/discovery.rs:12-17] [crates/gcode/src/index/walker/classification.rs:15-52]. This is the first fallback point: files that are not good AST candidates can still become content-only candidates.

7. `index_file` performs the single-file indexing flow. It derives the project-relative path, parses with semantic resolution, detects language, hashes content, reads metadata, and writes transactional facts through the PostgreSQL fact sink [crates/gcode/src/index/indexer/file.rs:15-91]. This is where discovered source becomes stored index data.

8. Import resolution enriches raw imports with language knowledge. JavaScript package metadata is loaded from `package.json`; if the file is missing or invalid JSON, the package set falls back to empty [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-34]. Go module lookup similarly returns `None` when `go.mod` cannot be read, and discovered Go files are grouped by package directory to support directory-granular resolution .

9. Static import-root assets handle common external names. For example, Elixir dependency names such as `jason`, `phoenix`, and `ecto` map to API roots like `Jason`, `Phoenix`, and `Ecto` . This acts like a small lookup table: when source text names a package, indexing can attach it to the top-level symbol a reader expects.

10. Call extraction records relationships between symbols. `CallSyntaxKind` classifies call syntax as `Bare`, `Member`, or `Other` [crates/gcode/src/index/parser/calls/resolution.rs:6-10]. Resolution then uses symbol ranges to find the deepest enclosing caller and distinguishes same-file bare calls from member-style calls .

## Key components

| Symbol | Role in the data flow |
| --- | --- |
| `Cli` | Captures global scope, output, logging, freshness, and the required subcommand before any indexing or querying happens [crates/gcode/src/cli.rs:23-46]. |
| `Command` | Represents the concrete CLI operation selected after global options are parsed [crates/gcode/src/cli.rs:121-469]. |
| `GcodeStandaloneSetup` | Carries the target schema and builds PostgreSQL object definitions for the code index [crates/gcode/src/setup/ddl.rs:8-10]. |
| `run_standalone_setup` | Orchestrates validation, reset or compatibility checks, setup execution, commit, and failure reporting [crates/gcode/src/setup/postgres.rs:12-57]. |
| `CallSyntaxKind` | Preserves whether a call was bare, member-style, or unresolved enough to affect callee resolution [crates/gcode/src/index/parser/calls/resolution.rs:6-10]. |

## What to read next

Read the Indexing chapter next, especially the file walker, `index_file`, import-resolution context, and call-resolution references. For command behavior, keep the CLI contract nearby as the reference for supported flags, scope rules, commands, and JSON output keys .

## Concepts

- [[code/concepts/workspace-map|Workspace Map]]
- [[code/concepts/shared-service-substrate|Shared Service Substrate]]
- [[code/concepts/cli-contracts-and-dispatch|CLI Contracts and Dispatch]]
- [[code/concepts/configuration-and-postgresql-setup|Configuration and PostgreSQL Setup]]
- [[code/concepts/file-discovery-and-indexing|File Discovery and Indexing]]
- [[code/concepts/import-and-call-resolution|Import and Call Resolution]]

## Continue the tour

- ← Previous: [[code/narrative/architecture|Architecture]]
- Next →: [[code/narrative/cli-runtime-foundation|CLI Runtime Foundation]]

