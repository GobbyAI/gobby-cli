---
title: Src
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/graph/tests.rs
- file: crates/gcode/src/commands/grep.rs
- file: crates/gcode/src/commands/search.rs
- file: crates/gcode/src/commands/status.rs
- file: crates/gcode/src/commands/symbol_at.rs
- file: crates/gcode/src/commands/symbols.rs
- file: crates/gcode/src/config/context.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/config/tests.rs
- file: crates/gcode/src/contract.rs
- file: crates/gcode/src/db/queries.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/graph/typed_query.rs
- file: crates/gcode/src/index/languages.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcode/src/projection/sync.rs
- file: crates/gcode/src/search/fts/tests.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/visibility.rs
provenance_truncated: 176
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/io.rs](crates/gcode/src/commands/codewiki/io.rs)
- [crates/gcode/src/commands/codewiki/prompts.rs](crates/gcode/src/commands/codewiki/prompts.rs)
- [crates/gcode/src/commands/codewiki/text/sanitize.rs](crates/gcode/src/commands/codewiki/text/sanitize.rs)
- [crates/gcode/src/commands/codewiki/types.rs](crates/gcode/src/commands/codewiki/types.rs)
- [crates/gcode/src/commands/graph/lifecycle.rs](crates/gcode/src/commands/graph/lifecycle.rs)
- [crates/gcode/src/commands/graph/reads.rs](crates/gcode/src/commands/graph/reads.rs)
- [crates/gcode/src/commands/graph/tests.rs](crates/gcode/src/commands/graph/tests.rs)
- [crates/gcode/src/commands/grep.rs](crates/gcode/src/commands/grep.rs)
- [crates/gcode/src/commands/search.rs](crates/gcode/src/commands/search.rs)
- [crates/gcode/src/commands/status.rs](crates/gcode/src/commands/status.rs)
- [crates/gcode/src/commands/symbol_at.rs](crates/gcode/src/commands/symbol_at.rs)
- [crates/gcode/src/commands/symbols.rs](crates/gcode/src/commands/symbols.rs)

_194 more source files omitted._

</details>

# Src

## Purpose

Src groups the related modules and files listed below; read the key components for the grounded detail.

## Key components

| Symbol | Kind | Source | Role |
| --- | --- | --- | --- |
| AiDepthArg | type | [crates/gcode/src/cli.rs:68-73] | Indexed type `AiDepthArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:68-73] |
| AiRouteArg | type | [crates/gcode/src/cli.rs:49-54] | Indexed type `AiRouteArg` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:49-54] |
| Cli | class | [crates/gcode/src/cli.rs:23-46] | 'Cli' is a crate-private Clap-parsed top-level command-line configuration struct that provides global flags for project root, output format, quiet/verbose logging, and freshness checks, plus a required 'Command' subcommand. [crates/gcode/src/cli.rs:23-46] |
| CodeGraphLifecycleBackend | class | [crates/gcode/src/commands/graph/lifecycle.rs:86] | 'CodeGraphLifecycleBackend' is a backend abstraction for managing the lifecycle of a code graph, represented here as an opaque 'struct' with no exposed fields or methods. [crates/gcode/src/commands/graph/lifecycle.rs:86] |
| Command | type | [crates/gcode/src/cli.rs:86-414] | Indexed type `Command` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:86-414] |
| EmbeddingsCommand | type | [crates/gcode/src/cli.rs:503-506] | Indexed type `EmbeddingsCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:503-506] |
| GraphCommand | type | [crates/gcode/src/cli.rs:417-481] | Indexed type `GraphCommand` in `crates/gcode/src/cli.rs`. [crates/gcode/src/cli.rs:417-481] |
| GraphFileSyncOutcome | type | [crates/gcode/src/commands/graph/lifecycle.rs:131-140] | Indexed type `GraphFileSyncOutcome` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:131-140] |
| GraphPathEndpoint | class | [crates/gcode/src/commands/graph/reads.rs:155-159] | 'GraphPathEndpoint' is a serde-serializable struct representing a path endpoint with an optional 'id' field omitted when 'None' and a required 'display_name' string. [crates/gcode/src/commands/graph/reads.rs:155-159] |
| GraphPathResponse | class | [crates/gcode/src/commands/graph/reads.rs:162-172] | 'GraphPathResponse' is a serialized response struct describing whether a path was found between two graph endpoints in a project, along with the search depth, hop count, ordered path steps, and an optional hint. [crates/gcode/src/commands/graph/reads.rs:162-172] |
| GraphResolutionProjectCleanup | class | [crates/gcode/src/commands/graph/reads.rs:663-666] | 'GraphResolutionProjectCleanup' is a struct that holds the 'database_url' and 'project_id' needed to identify and clean up graph resolution state for a specific project in a database-backed system. [crates/gcode/src/commands/graph/reads.rs:663-666] |
| GraphSyncContractError | class | [crates/gcode/src/commands/graph/lifecycle.rs:12-14] | 'GraphSyncContractError' is a Rust struct that encapsulates a 'serde_json::Value' payload representing contract error data. [crates/gcode/src/commands/graph/lifecycle.rs:12-14] |

## Members

- `crates/gcode/src` (module) [crates/gcode/src/cli.rs:23-46]
- `crates/gcode/src/cli.rs` (file) [crates/gcode/src/cli.rs:23-46]
- `crates/gcode/src/commands/graph/lifecycle.rs` (file) [crates/gcode/src/commands/graph/lifecycle.rs:12-14]
- `crates/gcode/src/commands/graph/payload.rs` (file) [crates/gcode/src/commands/graph/payload.rs:6-37]
- `crates/gcode/src/commands/graph/reads.rs` (file) [crates/gcode/src/commands/graph/reads.rs:19-25]
- `crates/gcode/src/commands/graph/tests.rs` (file) [crates/gcode/src/commands/graph/tests.rs:22-36]
- `crates/gcode/src/commands/index.rs` (file) [crates/gcode/src/commands/index.rs:10-60]


## Explore

- [[code/modules/crates/gcode/src|crates/gcode/src]]

