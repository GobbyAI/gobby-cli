---
title: Workspace Topology
type: code_concept
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

# Workspace Topology

## Purpose

Workspace Topology describes how this project is organized as a single Rust workspace partitioned into separate crates, each owning a distinct responsibility: code intelligence, shared primitives, hook dispatch, and the wiki engine. The problem it solves is keeping a large system coherent: by drawing explicit crate boundaries, the workspace makes dependency direction visible and enforceable, prevents the lower-level shared layer from accidentally depending on higher-level features, and lets each domain (indexing, primitives, hooks, wiki) evolve and be built/tested in relative isolation.

The two crates anchored in the supplied evidence are `crates/gcode` — the code-intelligence side, which also carries indexing assets such as import-root definitions ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]) — and `crates/gcore` — the shared-primitives side, which ships service-level infrastructure assets such as a Docker Compose service definition ([crates/gcore/assets/docker-compose.services.yml:5-117]).

## Covers / Does not cover

This page covers how the workspace is split into crates, what each crate is responsible for, and how build-time configuration (such as conditional test compilation) is wired per crate. It uses `crates/gcode` and `crates/gcore` as the concrete, evidenced examples of that partitioning.

It does not cover the internal implementation details of the indexing engine, the hook dispatch runtime, or the wiki engine beyond their place in the topology. The hook-dispatch and wiki-engine crates named in the working summary are not represented by file:line evidence in the supplied input, so their internal APIs are out of scope here. It also does not document the Compose services themselves or the Elixir import-root format beyond noting which crate owns each asset.

## Architecture

The workspace is arranged as a flat set of sibling crates under `crates/` ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]), rather than a single monolithic crate. This arrangement exists so that each domain has its own crate manifest, its own build script, and its own assets, while the workspace root ties them together for unified builds and dependency resolution.

The layering is intentional. `crates/gcore` holds shared primitives and infrastructure — the kind of low-level building blocks (and supporting assets like the Compose service file at [crates/gcore/assets/docker-compose.services.yml:5-117]) that other crates can rely on. `crates/gcode` sits above that as code-intelligence: it owns language-aware assets such as `elixir_dependency_roots.json` ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]) used to resolve import roots. The conceptual rule is that dependencies point toward the shared layer, never away from it, which is why primitives live in their own crate and feature crates depend on them.

Each crate can carry its own `build.rs` to drive compile-time decisions. In `crates/gcode`, the build script is the mechanism that translates an environment signal into a Cargo cfg, keeping integration-test compilation opt-in and local to that crate rather than leaking into the rest of the workspace ([crates/gcode/build.rs:1-8]).

## Data flow

Tracing what happens when the `gcode` crate is built:

1. Cargo invokes the crate's build script, `main` in `crates/gcode/build.rs` ([crates/gcode/build.rs:1-8]).
2. The script emits `cargo:rerun-if-env-changed=GCODE_POSTGRES_TEST_DATABASE_URL`, telling Cargo to re-run the build script whenever that environment variable changes ([crates/gcode/build.rs:2]).
3. The script registers the custom cfg with `cargo:rustc-check-cfg=cfg(gcode_postgres_tests)`, so the compiler recognizes the cfg name as valid and does not warn about it ([crates/gcode/build.rs:3]).
4. The script checks whether `GCODE_POSTGRES_TEST_DATABASE_URL` is set in the environment ([crates/gcode/build.rs:5]).
5. If the variable is present, it emits `cargo:rustc-cfg=gcode_postgres_tests`, enabling that cfg so Postgres-backed tests compile ([crates/gcode/build.rs:6]).
6. If the dependency is unavailable — that is, the variable is not set — step 5 is skipped, the `gcode_postgres_tests` cfg stays off, and the Postgres-dependent test code is excluded from compilation ([crates/gcode/build.rs:5-6]). This is the topology's way of letting one crate gate optional, infrastructure-dependent tests without affecting sibling crates.

## Key components

The most important symbol in the supplied evidence is the `gcode` build script entry point, which demonstrates the per-crate, opt-in build configuration that the topology relies on.

| Symbol / File | Kind | Role |
| --- | --- | --- |
| `main` ([crates/gcode/build.rs:1-8]) | function | Build-script entry for `crates/gcode`; gates Postgres test compilation on an env var via Cargo cfg directives. |
| `crates/gcode` ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]) | module | Code-intelligence crate; owns indexing assets such as import-root definitions. |
| `crates/gcore` ([crates/gcore/assets/docker-compose.services.yml:5-117]) | module | Shared-primitives crate; owns service/infrastructure assets. |
| `crates` ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]) | module | The workspace root grouping all sibling crates. |

## Where to start

Start with `crates/gcode/build.rs` and its `main` function ([crates/gcode/build.rs:1-8]). It is short, fully evidenced, and shows in one place how an individual crate participates in the workspace: it owns its own build-time configuration and gates optional behavior locally. From there, compare the asset ownership of `crates/gcode` ([crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]) against `crates/gcore` ([crates/gcore/assets/docker-compose.services.yml:5-117]) to see the boundary between code-intelligence and shared primitives before exploring the remaining crates.

## Explore

- [[code/modules/crates|crates]]
- [[code/modules/crates/gcode|crates/gcode]]
- [[code/modules/crates/gcore|crates/gcore]]

