---
title: crates/gcode/src
type: code_module
provenance:
- file: crates/gcode/src/commands/codewiki/architecture_diagrams.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/system_model.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/types.rs
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/reads.rs
- file: crates/gcode/src/commands/graph/tests.rs
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
- file: crates/gcode/src/graph/typed_query.rs
- file: crates/gcode/src/index/languages.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/models.rs
- file: crates/gcode/src/projection/sync.rs
- file: crates/gcode/src/search/fts/tests.rs
- file: crates/gcode/src/vector/code_symbols/embedding.rs
- file: crates/gcode/src/visibility.rs
provenance_truncated: 192
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src

Parent: [[code/modules/crates/gcode|crates/gcode]]

## Overview

`crates/gcode/src` contains 39 direct files and 11 child modules.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-24]
[crates/gcode/src/cli.rs:23-46]
[crates/gcode/src/cli/tests.rs:12-30]
[crates/gcode/src/commands/codewiki/architecture_diagrams.rs:40-81]
[crates/gcode/src/commands/codewiki/build.rs:1-39]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/cli\|crates/gcode/src/cli]] | `crates/gcode/src/cli` contains 1 direct file and 0 child modules. [crates/gcode/src/cli/tests.rs:12-30] [crates/gcode/src/cli/tests.rs:32-36] [crates/gcode/src/cli/tests.rs:38-55] |
| [[code/modules/crates/gcode/src/commands\|crates/gcode/src/commands]] | `crates/gcode/src/commands` contains 13 direct files and 3 child modules. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-24] [crates/gcode/src/commands/codewiki/architecture_diagrams.rs:40-81] [crates/gcode/src/commands/codewiki/build.rs:1-39] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170] [crates/gcode/src/commands/codewiki/build_parts/audit.rs:28-34] |
| [[code/modules/crates/gcode/src/config\|crates/gcode/src/config]] | `crates/gcode/src/config` contains 3 direct files and 0 child modules. [crates/gcode/src/config/context.rs:26-31] [crates/gcode/src/config/services.rs:20-22] [crates/gcode/src/config/tests.rs:14-22] [crates/gcode/src/config/context.rs:34] [crates/gcode/src/config/context.rs:37] |
| [[code/modules/crates/gcode/src/db\|crates/gcode/src/db]] | `crates/gcode/src/db` contains 3 direct files and 0 child modules. [crates/gcode/src/db/mod.rs:16-20] [crates/gcode/src/db/queries.rs:8-13] [crates/gcode/src/db/resolution.rs:16-18] [crates/gcode/src/db/mod.rs:27-31] [crates/gcode/src/db/mod.rs:33-35] |
| [[code/modules/crates/gcode/src/dispatch\|crates/gcode/src/dispatch]] | `crates/gcode/src/dispatch` contains 1 direct file and 0 child modules. [crates/gcode/src/dispatch/tests.rs:5-9] [crates/gcode/src/dispatch/tests.rs:12-14] [crates/gcode/src/dispatch/tests.rs:17-22] [crates/gcode/src/dispatch/tests.rs:25-27] [crates/gcode/src/dispatch/tests.rs:30-70] |
| [[code/modules/crates/gcode/src/graph\|crates/gcode/src/graph]] | `crates/gcode/src/graph` contains 4 direct files and 2 child modules. [crates/gcode/src/graph/code_graph.rs:1-51] [crates/gcode/src/graph/code_graph/connection.rs:7-12] [crates/gcode/src/graph/code_graph/lifecycle.rs:18-21] [crates/gcode/src/graph/code_graph/payload.rs:10-19] [crates/gcode/src/graph/code_graph/read.rs:1-25] |
| [[code/modules/crates/gcode/src/index\|crates/gcode/src/index]] | `crates/gcode/src/index` contains 18 direct files and 4 child modules. [crates/gcode/src/index/api.rs:16-23] [crates/gcode/src/index/chunker.rs:19-62] [crates/gcode/src/index/hasher.rs:7-9] [crates/gcode/src/index/import_resolution.rs:1-26] [crates/gcode/src/index/import_resolution/context.rs:41-138] |
| [[code/modules/crates/gcode/src/projection\|crates/gcode/src/projection]] | `crates/gcode/src/projection` contains 2 direct files and 0 child modules. [crates/gcode/src/projection/mod.rs:8-11] [crates/gcode/src/projection/sync.rs:12-15] [crates/gcode/src/projection/mod.rs:13-35] [crates/gcode/src/projection/sync.rs:18-22] [crates/gcode/src/projection/sync.rs:25-30] |
| [[code/modules/crates/gcode/src/search\|crates/gcode/src/search]] | `crates/gcode/src/search` contains 4 direct files and 1 child module. [crates/gcode/src/search/fts.rs:1-32] [crates/gcode/src/search/fts/common.rs:16] [crates/gcode/src/search/fts/content.rs:13-21] [crates/gcode/src/search/fts/counts.rs:10-66] [crates/gcode/src/search/fts/graph.rs:16-50] |
| [[code/modules/crates/gcode/src/setup\|crates/gcode/src/setup]] | `crates/gcode/src/setup` contains 6 direct files and 0 child modules. [crates/gcode/src/setup/contracts.rs:5-8] [crates/gcode/src/setup/ddl.rs:8-10] [crates/gcode/src/setup/identifiers.rs:5-15] [crates/gcode/src/setup/postgres.rs:12-57] [crates/gcode/src/setup/tests.rs:12-55] |
| [[code/modules/crates/gcode/src/vector\|crates/gcode/src/vector]] | `crates/gcode/src/vector` contains 2 direct files and 1 child module. [crates/gcode/src/vector/code_symbols.rs:1-29] [crates/gcode/src/vector/code_symbols/embedding.rs:21-23] [crates/gcode/src/vector/code_symbols/lifecycle.rs:29-37] [crates/gcode/src/vector/code_symbols/qdrant.rs:21-27] [crates/gcode/src/vector/code_symbols/repository.rs:6-18] |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/cli.rs\|crates/gcode/src/cli.rs]] | `crates/gcode/src/cli.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/lifecycle.rs\|crates/gcode/src/commands/graph/lifecycle.rs]] | `crates/gcode/src/commands/graph/lifecycle.rs` exposes 25 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/payload.rs\|crates/gcode/src/commands/graph/payload.rs]] | `crates/gcode/src/commands/graph/payload.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/reads.rs\|crates/gcode/src/commands/graph/reads.rs]] | `crates/gcode/src/commands/graph/reads.rs` exposes 42 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/graph/tests.rs\|crates/gcode/src/commands/graph/tests.rs]] | `crates/gcode/src/commands/graph/tests.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/grep.rs\|crates/gcode/src/commands/grep.rs]] | `crates/gcode/src/commands/grep.rs` exposes 44 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/index.rs\|crates/gcode/src/commands/index.rs]] | `crates/gcode/src/commands/index.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/gcode/src/commands/search.rs\|crates/gcode/src/commands/search.rs]] | `crates/gcode/src/commands/search.rs` exposes 39 indexed API symbols. |
| [[code/files/crates/gcode/src/config.rs\|crates/gcode/src/config.rs]] | `crates/gcode/src/config.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/config/context.rs\|crates/gcode/src/config/context.rs]] | `crates/gcode/src/config/context.rs` exposes 38 indexed API symbols. |
| [[code/files/crates/gcode/src/config/services.rs\|crates/gcode/src/config/services.rs]] | `crates/gcode/src/config/services.rs` exposes 53 indexed API symbols. |
| [[code/files/crates/gcode/src/config/tests.rs\|crates/gcode/src/config/tests.rs]] | `crates/gcode/src/config/tests.rs` exposes 27 indexed API symbols. |
| [[code/files/crates/gcode/src/contract.rs\|crates/gcode/src/contract.rs]] | `crates/gcode/src/contract.rs` exposes 28 indexed API symbols. |
| [[code/files/crates/gcode/src/db/mod.rs\|crates/gcode/src/db/mod.rs]] | `crates/gcode/src/db/mod.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/db/queries.rs\|crates/gcode/src/db/queries.rs]] | `crates/gcode/src/db/queries.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gcode/src/dispatch.rs\|crates/gcode/src/dispatch.rs]] | `crates/gcode/src/dispatch.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/src/freshness.rs\|crates/gcode/src/freshness.rs]] | `crates/gcode/src/freshness.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gcode/src/git.rs\|crates/gcode/src/git.rs]] | `crates/gcode/src/git.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/connection.rs\|crates/gcode/src/graph/code_graph/connection.rs]] | `crates/gcode/src/graph/code_graph/connection.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write.rs\|crates/gcode/src/graph/code_graph/write.rs]] | `crates/gcode/src/graph/code_graph/write.rs` exposes 27 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/deletion.rs\|crates/gcode/src/graph/code_graph/write/deletion.rs]] | `crates/gcode/src/graph/code_graph/write/deletion.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/mutation.rs\|crates/gcode/src/graph/code_graph/write/mutation.rs]] | `crates/gcode/src/graph/code_graph/write/mutation.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/support.rs\|crates/gcode/src/graph/code_graph/write/support.rs]] | `crates/gcode/src/graph/code_graph/write/support.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write/sync_plan.rs\|crates/gcode/src/graph/code_graph/write/sync_plan.rs]] | `crates/gcode/src/graph/code_graph/write/sync_plan.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/index_lock.rs\|crates/gcode/src/index_lock.rs]] | `crates/gcode/src/index_lock.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcode/src/lib.rs\|crates/gcode/src/lib.rs]] | `crates/gcode/src/lib.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/main.rs\|crates/gcode/src/main.rs]] | `crates/gcode/src/main.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/models.rs\|crates/gcode/src/models.rs]] | `crates/gcode/src/models.rs` exposes 51 indexed API symbols. |
| [[code/files/crates/gcode/src/output.rs\|crates/gcode/src/output.rs]] | `crates/gcode/src/output.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/progress.rs\|crates/gcode/src/progress.rs]] | `crates/gcode/src/progress.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/project.rs\|crates/gcode/src/project.rs]] | `crates/gcode/src/project.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/src/savings.rs\|crates/gcode/src/savings.rs]] | `crates/gcode/src/savings.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/schema.rs\|crates/gcode/src/schema.rs]] | `crates/gcode/src/schema.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/search/fts/tests.rs\|crates/gcode/src/search/fts/tests.rs]] | `crates/gcode/src/search/fts/tests.rs` exposes 34 indexed API symbols. |
| [[code/files/crates/gcode/src/secrets.rs\|crates/gcode/src/secrets.rs]] | `crates/gcode/src/secrets.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/setup.rs\|crates/gcode/src/setup.rs]] | `crates/gcode/src/setup.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/skill.rs\|crates/gcode/src/skill.rs]] | `crates/gcode/src/skill.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/utils.rs\|crates/gcode/src/utils.rs]] | `crates/gcode/src/utils.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/visibility.rs\|crates/gcode/src/visibility.rs]] | `crates/gcode/src/visibility.rs` exposes 28 indexed API symbols. |

