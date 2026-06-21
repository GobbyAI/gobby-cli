---
title: 'Introduction: The Gobby Code Intelligence Workspace'
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

# Introduction: The Gobby Code Intelligence Workspace

# Introduction: The Gobby Code Intelligence Workspace

## Why this matters

Before you can read any single file with confidence, you need a map of the territory. Gobby is organized as a Cargo workspace whose top-level `crates` module partitions the system into focused, separately-buildable units. The design decision here is separation by responsibility: code intelligence, shared primitives, hook dispatch, and the wiki engine each live in their own crate, with `gcore` serving as the common foundation that the others build on top of. That layering keeps the heavy machinery — indexing, language imports, services — from leaking into the primitives everyone shares.

You can already see the consequences of that split in the assets each crate carries. The intelligence crate, `gcode`, ships language-aware data such as `elixir_dependency_roots.json` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2], because resolving imports across ecosystems is its job. The foundation crate, `gcore`, ships infrastructure concerns instead — for example a `docker-compose.services.yml` describing the backing services the rest of the workspace depends on [crates/gcore/assets/docker-compose.services.yml:5-117]. Reading the directory layout, then, is the fastest way to predict where a given concern lives.

## How it works

Here is the real flow of how the workspace orients itself and prepares to build:

1. **Start at the workspace root.** The `crates` module is the entry point that groups the member crates [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]. Think of it the way the `import_roots` assets work for `gcode`: a small set of declared roots tells the rest of the system where to begin resolving everything else.

2. **Identify the foundation, `gcore`.** Everything else layers on top of it, and it owns the shared infrastructure — including the service definitions in `docker-compose.services.yml` [crates/gcore/assets/docker-compose.services.yml:5-117] that stand up the dependencies the workspace needs at runtime.

3. **Move outward to `gcode`, the code-intelligence crate.** This is where language-specific knowledge lives, such as the Elixir dependency roots used during import resolution [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2].

4. **Let the build script wire in optional capabilities.** When Cargo builds `gcode`, its `build.rs` runs first. The `main` function emits three directives: it asks Cargo to rerun the script whenever `GCODE_POSTGRES_TEST_DATABASE_URL` changes, registers the `gcode_postgres_tests` cfg so `cargo`'s check-cfg lint accepts it, and conditionally enables that cfg [crates/gcode/build.rs:1-8].

5. **Fall back gracefully when Postgres is absent.** The enabling step is gated on the environment: only `if std::env::var_os("GCODE_POSTGRES_TEST_DATABASE_URL").is_some()` does the script emit `cargo:rustc-cfg=gcode_postgres_tests` [crates/gcode/build.rs:4-6]. If the variable is unset, the cfg simply stays off and the Postgres-backed tests compile out — so a contributor without a database can still build the crate.

## Key components

| Symbol / File | Kind | Role |
| --- | --- | --- |
| `crates` | module | Workspace root that partitions the system into member crates [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] |
| `crates/gcore` | module | Shared foundation carrying infrastructure assets like the service compose file [crates/gcore/assets/docker-compose.services.yml:5-117] |
| `crates/gcode` | module | Code-intelligence crate holding language import data [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] |
| `main` | function | Build script that registers and conditionally enables the `gcode_postgres_tests` cfg [crates/gcode/build.rs:1-8] |

## What to read next

Continue with the chapter on **`gcore`, the common foundation**, since it underpins every other crate and explains the shared primitives and services (such as the `docker-compose.services.yml` you saw above [crates/gcore/assets/docker-compose.services.yml:5-117]) before you dive into the higher-level code-intelligence, hook-dispatch, and wiki crates.

## Concepts

- [[code/concepts/crates|Workspace Topology]]
- [[code/concepts/crates-gcore|Shared Platform Primitives]]

## Explore

- [[code/modules/crates|crates]]
- [[code/modules/crates/gcode|crates/gcode]]
- [[code/modules/crates/gcore|crates/gcore]]

## Continue the tour

- Next →: [[code/narrative/02-architecture|Architecture]]

