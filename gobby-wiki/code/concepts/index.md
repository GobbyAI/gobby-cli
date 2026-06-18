---
title: Curated Concept Navigation
type: code_concept_tree
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

# Curated Concept Navigation

Reader-first paths into the grounded code reference.

## Start here — guided tour

New to this codebase? Begin with [[code/narrative/introduction|Introduction]].

1. [[code/narrative/introduction|Introduction]]
2. [[code/narrative/architecture|Architecture]]
3. [[code/narrative/data-flow|Data Flow]]

Ask questions across this vault with `gwiki ask "..."`, or find pages with `gwiki search "..."`.

## Concept Tree

### System Tour

A curated path through the primary modules.

- [[code/concepts/crates|Crates]] - `crates` contains 0 direct files and 4 child modules.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/build.rs:1-8]
[crates/gcode/src/cli.rs:23-46]
[crates/gcode/src/cli/tests.rs:12-30]
[crates/gcode/src/commands/codewiki/build.rs:1-30]
- [[code/concepts/crates-gcode|Gcode]] - `crates/gcode` contains 1 direct file and 3 child modules.
[crates/gcode/src/commands/codewiki/build_parts/file.rs:13-16]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/build.rs:1-8]
[crates/gcode/src/cli.rs:23-46]
- [[code/concepts/crates-gcode-assets|Assets]] - `crates/gcode/assets` contains 0 direct files and 1 child module.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]
- [[code/concepts/crates-gcode-assets-import-roots|Import Roots]] - `crates/gcode/assets/import_roots` contains 2 direct files and 0 child modules.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]
- [[code/concepts/crates-gcode-contract|Contract]] - `crates/gcode/contract` contains 1 direct file and 0 child modules.
[crates/gcode/contract/gcode.contract.json:2]
[crates/gcode/contract/gcode.contract.json:3]
[crates/gcode/contract/gcode.contract.json:4]
[crates/gcode/contract/gcode.contract.json:5-49]
[crates/gcode/contract/gcode.contract.json:7]
- [[code/concepts/crates-gcode-src|Src]] - `crates/gcode/src` contains 37 direct files and 11 child modules.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/src/cli.rs:23-46]
[crates/gcode/src/cli/tests.rs:12-30]
[crates/gcode/src/commands/codewiki/build.rs:1-30]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
- [[code/concepts/crates-gcode-src-cli|Cli]] - `crates/gcode/src/cli` contains 1 direct file and 0 child modules.
[crates/gcode/src/cli/tests.rs:12-30]
[crates/gcode/src/cli/tests.rs:32-36]
[crates/gcode/src/cli/tests.rs:38-55]
- [[code/concepts/crates-gcode-src-commands|Commands]] - `crates/gcode/src/commands` contains 13 direct files and 3 child modules.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/src/commands/codewiki/build.rs:1-30]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85]
- [[code/concepts/crates-gcode-src-commands-codewiki|Codewiki]] - `crates/gcode/src/commands/codewiki` contains 20 direct files and 4 child modules.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/src/commands/codewiki/build.rs:1-30]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85]
- [[code/concepts/crates-gcode-src-commands-codewiki-build-parts|Build Parts]] - `crates/gcode/src/commands/codewiki/build_parts` contains 9 direct files and 1 child module.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
[crates/gcode/src/commands/codewiki/build_parts/changes.rs:5-101]
[crates/gcode/src/commands/codewiki/build_parts/concepts.rs:35-85]
[crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:10-24]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:12-138]
- [[code/concepts/crates-gcode-src-commands-codewiki-build-parts-concepts|Concepts]] - `crates/gcode/src/commands/codewiki/build_parts/concepts` contains 5 direct files and 0 child modules.
[crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs:10-24]
[crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs:12-138]
[crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13]
[crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:1-7]
[crates/gcode/src/commands/codewiki/build_parts/concepts/types.rs:4-11]
- [[code/concepts/crates-gcode-src-commands-codewiki-ownership|Ownership]] - `crates/gcode/src/commands/codewiki/ownership` contains 4 direct files and 0 child modules.
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:17-21]
[crates/gcode/src/commands/codewiki/ownership/codeowners.rs:5-7]
[crates/gcode/src/commands/codewiki/ownership/render.rs:10-34]
[crates/gcode/src/commands/codewiki/ownership/tests.rs:8-35]
[crates/gcode/src/commands/codewiki/ownership/analysis.rs:23-87]

