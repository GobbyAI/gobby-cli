---
title: Architecture
type: code_narrative
provenance:
- file: crates/gcode/contract/gcode.contract.json
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/config/services.rs
- file: crates/gcode/src/db/resolution.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcore/assets/docker-compose.services.yml
- file: crates/gcore/src/ai_context.rs
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/gwiki/contract/gwiki.contract.json
- file: crates/gwiki/src/benchmark.rs
- file: crates/gwiki/src/graph/mod.rs
- file: crates/gwiki/src/health.rs
- file: crates/gwiki/src/ingest/audio.rs
- file: crates/gwiki/src/ingest/mod.rs
- file: crates/gwiki/src/ingest/session.rs
- file: crates/gwiki/src/search/semantic.rs
- file: crates/gwiki/src/vector.rs
- file: docs/evidence/wiki-parity-2026-06/wp3-deposit-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-ask-direct.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-ghook-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q2-rrf-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q3-uuid5-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-ask-daemon.json
- file: docs/evidence/wiki-parity-2026-06/wp3-qa-q4-falkor-search.json
- file: docs/evidence/wiki-parity-2026-06/wp3-search-hybrid.json
- file: docs/evidence/wiki-parity-2026-06/wp3-search-sources.json
provenance_truncated: 452
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/contract/gcode.contract.json](crates/gcode/contract/gcode.contract.json)
- [crates/gcode/src/commands/codewiki/types.rs](crates/gcode/src/commands/codewiki/types.rs)
- [crates/gcode/src/config/services.rs](crates/gcode/src/config/services.rs)
- [crates/gcode/src/db/resolution.rs](crates/gcode/src/db/resolution.rs)
- [crates/gcode/src/index/semantic.rs](crates/gcode/src/index/semantic.rs)
- [crates/gcode/src/models.rs](crates/gcode/src/models.rs)
- [crates/gcore/assets/docker-compose.services.yml](crates/gcore/assets/docker-compose.services.yml)
- [crates/gcore/src/ai_context.rs](crates/gcore/src/ai_context.rs)
- [crates/ghook/schemas/diagnose-output.v2.schema.json](crates/ghook/schemas/diagnose-output.v2.schema.json)
- [crates/gwiki/contract/gwiki.contract.json](crates/gwiki/contract/gwiki.contract.json)
- [crates/gwiki/src/benchmark.rs](crates/gwiki/src/benchmark.rs)
- [crates/gwiki/src/graph/mod.rs](crates/gwiki/src/graph/mod.rs)

_470 more source files omitted._

</details>

# Architecture

## Why this matters

Architecture walks through the modules and files listed below; follow the key components in order, then continue to the linked pages.

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

- `crates` (module) [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
- `crates/gcode` (module) [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
- `crates/gcode/assets` (module) [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
- `crates/gcode/assets/import_roots` (module) [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
- `crates/gcode/contract` (module) [crates/gcode/contract/gcode.contract.json:2]
- `crates/gcode/src` (module) [crates/gcode/src/cli.rs:23-46]
- `docs` (module) [docs/evidence/wiki-parity-2026-06/wp3-audit.json:1-100]
- `scripts` (module) [scripts/verify.sh:4-10]
- `crates/gcode/assets/import_roots/elixir_dependency_roots.json` (file) [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
- `crates/gcode/assets/import_roots/ruby_require_roots.json` (file) [crates/gcode/assets/import_roots/ruby_require_roots.json:2]
- `crates/gcode/build.rs` (file) [crates/gcode/build.rs:1-8]
- `crates/gcode/contract/gcode.contract.json` (file) [crates/gcode/contract/gcode.contract.json:2]
- `crates/gcode/src/cli.rs` (file) [crates/gcode/src/cli.rs:23-46]
- `crates/gcode/src/cli/tests.rs` (file) [crates/gcode/src/cli/tests.rs:12-30]
- `crates/gcode/src/commands/graph/lifecycle.rs` (file) [crates/gcode/src/commands/graph/lifecycle.rs:12-14]
- `crates/gcode/src/commands/graph/payload.rs` (file) [crates/gcode/src/commands/graph/payload.rs:6-37]
- `crates/gcode/src/commands/graph/reads.rs` (file) [crates/gcode/src/commands/graph/reads.rs:19-25]
- `crates/gcode/src/commands/graph/tests.rs` (file) [crates/gcode/src/commands/graph/tests.rs:22-36]
- `crates/gcode/src/commands/index.rs` (file) [crates/gcode/src/commands/index.rs:10-60]


## Concepts

- [[code/concepts/crates|Crates]]
- [[code/concepts/crates-gcode|Gcode]]
- [[code/concepts/crates-gcode-assets|Assets]]
- [[code/concepts/crates-gcode-assets-import-roots|Import Roots]]
- [[code/concepts/crates-gcode-contract|Contract]]
- [[code/concepts/crates-gcode-src|Src]]

## Explore

- [[code/modules/crates|crates]]
- [[code/modules/docs|docs]]
- [[code/modules/scripts|scripts]]

## Continue the tour

- ← Previous: [[code/narrative/introduction|Introduction]]
- Next →: [[code/narrative/data-flow|Data Flow]]

