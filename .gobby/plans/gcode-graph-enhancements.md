# gcode-owned code projections on the Rust foundation

**Plan ID:** gcode-graph-enhancements

## O1: Overview
`kind: framing`

`gcode` owns code-index behavior and the code projections derived from it on top of the shared Rust foundation defined in `.gobby/plans/gcore-rust-foundation.md`. The durable target is not a graph-only API or a generic datastore/search substrate inside `gobby-code`; it is a code-specific projection layer that owns PostgreSQL code facts, the FalkorDB `gobby_code` graph projection, and Qdrant `code_symbols_<project_id>` symbol-vector collections.

This plan moves code fact writes, graph/vector projection sync, lifecycle operations, and project graph reporting into `gobby-code` library boundaries first. Shared context/config resolution, attached versus standalone setup contracts, PostgreSQL/FalkorDB/Qdrant adapters, generic indexing/search primitives, and degradation vocabulary are consumed from `gobby-core`. `gcode` remains the user-facing CLI wrapper for code APIs. Code projections must work without the daemon process, and standalone mode gets an explicit setup path for the minimal gcode-owned app schema it needs.

For code-symbol vectors, `gcode` calls OpenAI-compatible `/v1/embeddings` endpoints directly. In attached Gobby mode, bootstrap resolves the PostgreSQL hub and service settings come from `config_store` plus secret resolution; env vars remain explicit overrides for standalone, tests, and emergency diagnostics. The daemon embedding service is bypassed for code-index projection sync. Python remains a scheduler, API, UI, and MCP bridge during the migration window; it may shell out to stable `gcode` JSON commands until the future Rust daemon links the same library APIs directly. LLM-generated symbol summaries stay daemon-side for now and remain optional enrichment, not a projection-sync prerequisite.

The code/memory boundary stays sharp. Rust code-index modules own deterministic code facts: files, symbols, imports, definitions, calls, unresolved call targets, and code graph reports derived from those facts. Gobby memory services own memories, knowledge graph extraction, and `RELATES_TO_CODE` bridge creation. Rust report code may read bridge edges when present so agents can see hypotheses beside extracted code facts, but it must not create or mutate memory-owned data.

## D1: Dependent Plans
`kind: framing`

This plan depends on the shared Rust foundation defined in `.gobby/plans/gcore-rust-foundation.md`. Shared context/config resolution, attached/standalone setup contracts, PostgreSQL/FalkorDB/Qdrant adapters, generic indexing/search primitives, and degradation vocabulary are consumed from `gobby-core`. `gobby-code` owns code-specific PostgreSQL fact writes, FalkorDB `gobby_code` graph projection, Qdrant `code_symbols_<project_id>` vector projection, lifecycle commands, and project graph reports.

Memory graph behavior, `RELATES_TO_CODE` bridge edges, and LLM-generated symbol summaries remain owned by the Gobby daemon's memory services and are not in scope for this plan.

## A1: Architecture Principles
`kind: framing`

- Foundation dependency: shared context/config, setup contracts, datastore adapters, generic indexing/search primitives, and degradation types come from `gobby-core`.
- Vector projection lifecycle exception: `gobby-core::qdrant` intentionally scopes to client surface (collection naming, `with_qdrant` ServiceState boundary, `search`, and `upsert`); collection lifecycle (ensure collection with vector params, delete-by-filter, clear/drop, rebuild) is consumer-owned. Code-specific Qdrant lifecycle HTTP is allowed inside `crates/gcode/src/vector/code_symbols.rs` only and must still resolve config through `gobby-core::config::resolve_qdrant_config`, enter the ServiceState/degradation boundary through `gobby-core::qdrant::with_qdrant`, derive collection names through `gobby-core::qdrant::collection_name(.., CollectionScope::Custom(..))`, and use `gobby-core::qdrant::search` / `gobby-core::qdrant::upsert` for non-lifecycle operations. No other `gobby-code` file may issue raw Qdrant lifecycle REST.
- Code-specific core: PostgreSQL code facts, graph projection sync, vector projection sync, reports, symbol IDs, language facts, and code API shapes live in `gobby-code`.
- CLI wrapper: `gcode` parses CLI args, resolves context, calls library APIs, and formats output.
- Direct linking is the target daemon integration. The future Rust daemon links the same Rust code directly; no daemon HTTP, MCP, or CLI shell boundary is the target internal architecture.
- Python daemon shell-outs are transitional only. If needed before the Rust daemon lands, Python calls stable `gcode` JSON commands and treats failures as explicit degradation.
- Bootstrap-first attached config: `bootstrap.yaml` or the daemon broker resolves the PostgreSQL hub; FalkorDB, Qdrant, and embedding settings are read from `config_store` with secret resolution.
- Env vars are overrides, not the attached-mode source of truth. They support standalone mode, tests, and emergency diagnostics.
- Direct embedding ownership: code-symbol vectors are generated by `gcode` through OpenAI-compatible embedding endpoints, not through the daemon embedding service.
- Qdrant compatibility: existing `code_symbols_<project_id>` collection names remain the public storage contract; no vector collection migration is required.
- Gobby-attached mode remains non-destructive. It validates the externally managed hub schema and must not create, alter, or drop Gobby-owned tables.
- Standalone mode is explicit. A setup command creates only the minimal gcode-owned app schema in a selected standalone database or schema namespace. Runtime projection commands validate prerequisites and never run implicit migrations.
- Code owns code; memory owns memory. `CALLS`, `IMPORTS`, and `DEFINES` are extracted code facts. `RELATES_TO_CODE` and LLM-created memory relationships are inferred memory facts.
- Degraded behavior is honest. Missing PostgreSQL/FalkorDB/Qdrant/embedding pieces produce typed errors, degraded report sections, or clear non-zero exits depending on command hardness; projection lifecycle commands must not return fake empty success payloads for unavailable services.
- JSON compatibility is preserved. New metadata fields are optional with `#[serde(skip_serializing_if = "Option::is_none")]`.
- Phase 7 contract tests in the Gobby repo remain a compatibility gate until that external source-inspection contract changes.

## N1: Non-Goals
`kind: framing`

- Do not make `gcode` the long-term owner of daemon orchestration, UI, MCP, or memory graph behavior.
- Do not add generic datastore, search, indexing, or degradation primitives to `gobby-code` when they belong in `gobby-core`.
- Do not add daemon-backed projection/report CLI commands as the target architecture.
- Do not rely on inherited Gobby-owned migrations as the standalone story.
- Do not write `.gobby/project.json`, mutate `config_store`, or run `gcode invalidate`.
- Do not add Graphify or any third-party graph product as a runtime dependency.
- Do not move LLM-generated symbol summaries to Rust in this plan.

## P1: Core Boundary And Setup
`kind: framing`

### 1.1 Create the gobby-code projection library boundary [category: code]
`kind: deliverable`
Targets: `crates/gcode/Cargo.toml`, `crates/gcode/src/lib.rs`, `crates/gcode/src/main.rs`, `crates/gcode/src/commands/graph.rs`, `crates/gcode/src/commands/vector.rs`, `crates/gcode/src/falkor.rs`, `crates/gcode/src/search/semantic.rs`

Add a library target for `gobby-code` and move code-specific projection behavior behind modules callable from both the CLI and a future Rust daemon. The CLI keeps the existing binary surface, but implementation entry points should be library functions with input structs and serializable output structs.

Shared context/config, setup contracts, datastore adapters, generic indexing/search primitives, and degradation contracts come from `gobby-core`. `gobby-code` owns code fact models, graph projection APIs, vector projection APIs, lifecycle commands, reports, and code-specific search boosts.

Initial module shape:

- `crates/gcode/src/lib.rs` exports reusable modules.
- `index::api` owns code-fact write APIs for files, symbols, imports, calls, unresolved targets, and content chunks, callable independent of CLI types. Detailed contract lives in §1.4.
- `graph::typed_query` owns safe FalkorDB parameter rendering.
- `graph::code_graph` owns FalkorDB `gobby_code` graph projection writes, reads, and lifecycle operations.
- `vector::code_symbols` owns embedding requests, Qdrant collection ensure/upsert/delete/clear/rebuild, and lifecycle operations for `code_symbols_<project_id>`.
- `projection::sync` coordinates graph/vector sync status after PostgreSQL code fact writes.
- `graph::report` owns project graph report generation.
- `setup` integrates explicit standalone setup through `gobby-core` contracts.
- `schema` keeps gcode-specific attached-mode validation.

`crates/gcode/src/falkor.rs` remains a compatibility facade for the external Phase 7 contract while implementation moves behind the library boundary. Do not collapse it into a pure re-export until the Gobby-side source-inspection test is revised.

**Acceptance:**

- 1.1.1 - `gobby-code` builds as both a library and `gcode` binary. file: `crates/gcode/Cargo.toml`, `crates/gcode/src/lib.rs`.
- 1.1.2 - `main.rs` and `commands/*` call library APIs rather than owning projection business logic. file: `crates/gcode/src/main.rs`, `crates/gcode/src/commands/graph.rs`, `crates/gcode/src/commands/vector.rs`.
- 1.1.3 - Library APIs avoid CLI-only types in public input/output contracts. test: `crates/gcode/src/lib.rs::tests::public_projection_api_is_cli_independent`.
- 1.1.4 - Phase 7 compatibility surface in `falkor.rs` remains available (file exists, is not a pure re-export, and exposes the basic facade symbols `FalkorClient`, `with_falkor` referenced by downstream gcode modules). The deep source-inspection contract that the Gobby-repo Phase 7 test asserts is pinned by §1.5.11 / §1.5.12 / §1.5.13 / §1.5.14 / §1.5.15 / §1.5.16 once §1.5 lands. test: `crates/gcode/src/lib.rs::tests::falkor_facade_is_available`, test: `gobby/tests/code_index/test_gcode_phase7_contract.py`.

### 1.2 Add explicit standalone setup [category: code] (depends: 1.1)
`kind: deliverable`
Targets: `crates/gcode/src/schema.rs`, `crates/gcode/src/setup.rs`, `crates/gcode/src/commands/setup.rs`, `crates/gcode/src/commands/mod.rs`, `crates/gcode/src/main.rs`

Separate attached-mode validation from standalone setup:

- Attached mode validates the Gobby hub schema, `pg_search`, and BM25 indexes without creating or migrating Gobby-owned objects.
- Standalone setup is an explicit user action invoked through `gcode setup --standalone [--database-url <dsn>] [--schema <name>]` that creates only the minimal gcode-owned app schema needed for indexing, graph/vector sync state, and search in a selected database/schema namespace.
- Runtime commands fail with clear setup guidance when prerequisites are missing.

CLI surface:

- `crates/gcode/src/main.rs` defines the `setup` subcommand with `--standalone` (required for write actions in v1), `--database-url`, and `--schema` flags, and routes execution to `commands::setup::run`.
- `crates/gcode/src/commands/setup.rs` parses the resolved arguments, builds a `setup::StandaloneSetupRequest`, calls the library API in `setup.rs`, and formats output through `output::print_json` / `output::print_text`.
- `crates/gcode/src/commands/mod.rs` exposes the new `setup` module to the binary.

**Early-dispatch requirement**:

`gcode setup --standalone` must dispatch from `main.rs` in the early-dispatch block — alongside `Init`, `Projects`, and `Prune` — **before** `Context::resolve()` is called. The current CLI runs context resolution only for commands that require a resolved project root, PostgreSQL DSN, and validated schema; setup is the command that creates those prerequisites for standalone mode, so it cannot depend on them existing. The dispatch site reads `--database-url` and `--schema` directly from the parsed clap struct, constructs a `setup::StandaloneSetupRequest`, and invokes `commands::setup::run(request)` without touching `Context::resolve()`. Running the command in a project lacking normal gcode context (no `.gobby/project.json`, no resolvable bootstrap PostgreSQL DSN) must succeed when the user supplies an explicit `--database-url` and `--schema`.

**Foundation contract requirement**:

`crates/gcode/src/setup.rs` performs standalone schema/DDL work by implementing the foundation-defined `gobby_core::setup::StandaloneSetup` trait. The foundation plan (`.gobby/plans/gcore-rust-foundation.md` §1.4) defines the trait as `namespace(&self) -> &str`, `owned_objects(&self) -> Vec<OwnedObject>`, and `create(&self, ctx: &mut SetupContext<'_>) -> Result<SetupReport, SetupError>`; `gobby-core` deliberately knows nothing about gcode-owned tables, columns, or BM25 index DDL, so gcode-owned DDL strings live inside gcode's creator callbacks rather than inside `gobby-core`.

Concretely, `crates/gcode/src/setup.rs` defines a struct (for example `GcodeStandaloneSetup`) implementing `gobby_core::setup::StandaloneSetup` with:

- `namespace()` returning the gcode-owned namespace string (for example `"gcode"`).
- `owned_objects()` returning a `Vec<gobby_core::setup::OwnedObject>` enumerating every gcode-owned standalone resource (indexed-files table, symbols table, content-chunks table, sync-state tables, BM25 indexes, etc.). Each `OwnedObject` carries its human-readable `name`, `store: StoreKind::Postgres`, and a `creator: Box<dyn FnMut(&mut SetupContext<'_>) -> Result<(), SetupError>>` closure that owns the literal `CREATE TABLE`/`CREATE INDEX`/`CREATE EXTENSION` strings for that resource.
- `create(ctx)` walks the declared `owned_objects()` list and invokes each creator against the supplied `gobby_core::setup::SetupContext` (which exposes `pg: Option<&mut postgres::Client>` for DDL execution), returning a `SetupReport` summarising created/skipped/failed objects.

All gcode-owned DDL strings live in gcode creator closures; `gobby-core` is the contract owner (trait definition, `SetupContext`, `OwnedObject`, `SetupReport`, `SetupError`, `StoreKind`) but does not contain gcode domain DDL. The foundation contract's `SetupContext` is the only handle through which gcode standalone DDL touches the PostgreSQL connection — gcode does not open its own raw connections or issue DDL outside the creator-callback path.

Standalone-only: the implementation MUST refuse to declare or execute any DDL that touches Gobby-owned tables, the `config_store` table, or the `.gobby/project.json` file. The acceptance test enumerates the gcode-owned object names and asserts the namespace plus this exclusion list explicitly.

Standalone setup must not write `.gobby/project.json`, `config_store`, Gobby migrations, or daemon-owned metadata. It may create only gcode-owned objects after explicit opt-in.

**Acceptance:**

- 1.2.1 - Attached-mode schema validation remains read-only. file: `crates/gcode/src/schema.rs`.
- 1.2.2 - Standalone setup is implemented in a separate module from runtime validation. file: `crates/gcode/src/setup.rs`.
- 1.2.3 - Missing standalone prerequisites produce an actionable error instead of implicit creation. test: `crates/gcode/src/schema.rs::tests::missing_schema_requires_setup`.
- 1.2.4 - Standalone setup creates only gcode-owned objects and never touches `config_store` or `.gobby/project.json`. test: `crates/gcode/src/setup.rs::tests::standalone_setup_is_scoped`.
- 1.2.5 - `gcode setup --standalone [--database-url ...] [--schema ...]` parses via clap and dispatches to `commands::setup::run`. test: `crates/gcode/src/main.rs::tests::parse_setup_standalone`.
- 1.2.6 - `gcode setup --standalone` executes the library setup API end-to-end against the selected standalone database/schema namespace without touching `.gobby/project.json`, `config_store`, or daemon-owned metadata. test: `crates/gcode/src/commands/setup.rs::tests::standalone_command_is_scoped`.
- 1.2.7 - `gcode setup --standalone` dispatches in the early-dispatch block before `Context::resolve()` (alongside `Init`, `Projects`, and `Prune`), and the command runs successfully with an explicit `--database-url` plus `--schema` in a directory lacking `.gobby/project.json` or a resolvable bootstrap PostgreSQL DSN. test: `crates/gcode/src/main.rs::tests::setup_runs_before_context_resolve`.
- 1.2.8 - `crates/gcode/src/setup.rs` defines a struct (for example `GcodeStandaloneSetup`) that implements `gobby_core::setup::StandaloneSetup`; its `namespace()` returns a gcode-owned string (for example `"gcode"`), `owned_objects()` enumerates every gcode-owned standalone resource (indexed-files, symbols, content chunks, sync-state, BM25 indexes) as `OwnedObject` entries whose `creator` closures own the literal `CREATE TABLE`/`CREATE INDEX`/`CREATE EXTENSION` strings, and the declared object list refuses to include Gobby-owned tables, `config_store`, or `.gobby/project.json`. The `create` implementation executes the creator closures against the foundation-supplied `gobby_core::setup::SetupContext`; gcode does not bypass `SetupContext` to open raw PostgreSQL connections or issue DDL outside the creator-callback path. test: `crates/gcode/src/setup.rs::tests::standalone_setup_uses_gobby_core_contract`.

### 1.3 Add safe typed FalkorDB query rendering [category: code] (depends: 1.1, 1.5)
`kind: deliverable`
Targets: `crates/gcode/src/graph/typed_query.rs`, `crates/gcode/src/falkor.rs`

`falkordb-rs` accepts string parameters too narrowly for the graph write shapes this plan needs. Add a typed query wrapper that renders Cypher parameters safely and rejects unsafe identifiers or values before query execution.

Rules:

- Parameter names and map keys must match `^[A-Za-z_][A-Za-z0-9_]*$`.
- Strings escape quotes, backslashes, and unicode correctly.
- Control characters and non-finite floats are rejected.
- Lists and maps are rendered recursively.
- Existing Falkor row conversion is shared with `falkor.rs`; do not duplicate an ad hoc parser.

**Acceptance:**

- 1.3.1 - Typed params render safe Cypher for strings, numbers, booleans, lists, and maps. file: `crates/gcode/src/graph/typed_query.rs`.
- 1.3.2 - Invalid identifiers, control characters, and NaN/Inf values return typed errors. test: `crates/gcode/src/graph/typed_query.rs::tests`.
- 1.3.3 - The wrapper reuses the existing Falkor row conversion boundary. file: `crates/gcode/src/falkor.rs`.

### 1.4 Add reusable code-fact indexing library API [category: code] (depends: 1.1, 1.5)
`kind: deliverable`
Targets: `crates/gcode/src/lib.rs`, `crates/gcode/src/index/mod.rs`, `crates/gcode/src/index/indexer.rs`, `crates/gcode/src/commands/index.rs`, `crates/gcode/src/db.rs`

Decompose the existing code-fact write path into a reusable library API so the future Rust daemon can link the same indexing surface that `gcode index` uses today. The library API owns PostgreSQL code-fact writes for files, symbols, imports, calls, unresolved targets, and content chunks. CLI parsing, output formatting, progress reporting, and freshness messaging stay in `commands/index.rs`.

Library shape:

- `index::api::index_files(IndexRequest, &Context) -> Result<IndexOutcome>` is the public entry point. The function lives in `crates/gcode/src/index/indexer.rs` (or a sibling `api.rs` re-exported through `index::mod`) and is exported from `crates/gcode/src/lib.rs`.
- `IndexRequest` carries: project root, optional file/path filter, optional explicit file list, `full` versus incremental flag, `require_cpp_semantics`, `sync_projections` flag (consumed by §2.6), and other behavior toggles. It must not embed clap derive types or formatter handles.
- `IndexOutcome` is serializable via `serde` and exposes counts: `scanned_files`, `indexed_files`, `skipped_files`, `symbols_indexed`, `chunks_indexed`, plus per-step duration metadata where useful and a typed `degraded` field for partially completed runs.
- `commands/index.rs` parses CLI args, builds the request, calls the library API, and dispatches output through `output::print_json` / `output::print_text`. It must not contain inline PostgreSQL code-fact write logic, language parsing, or chunk assembly.
- `db.rs` exposes connection helpers used by both the library API and projection sync; library entry points must not bypass these helpers to access PostgreSQL directly.

The library API owns code-fact writes only. Graph and vector projection sync is delegated to the projection modules defined in §2.4 and §2.5 via `projection::sync` (see §2.6); the indexing library API does not call FalkorDB or Qdrant directly.

**Acceptance:**

- 1.4.1 - A public `index::api::index_files` library function accepts an `IndexRequest` and returns a serializable `IndexOutcome` covering files, symbols, imports, calls, unresolved targets, and chunks. file: `crates/gcode/src/index/indexer.rs`, `crates/gcode/src/lib.rs`.
- 1.4.2 - `commands/index.rs` calls the library API and contains no inline PostgreSQL code-fact write logic, language parsing, or chunk assembly. file: `crates/gcode/src/commands/index.rs`.
- 1.4.3 - Library input/output structs avoid CLI-only types (no clap derive types, no `output::Format`, no formatter handles). test: `crates/gcode/src/index/indexer.rs::tests::library_api_is_cli_independent`.
- 1.4.4 - Files, symbols, imports, calls, unresolved targets, and chunks are all written through the library API and reflected in `IndexOutcome` counts. test: `crates/gcode/src/index/indexer.rs::tests::library_writes_all_code_facts`.

### 1.5 Wire gcode to the gobby-core foundation [category: code] (depends: 1.1)
`kind: deliverable`
Targets: `crates/gcode/Cargo.toml`, `crates/gcode/src/lib.rs`, `crates/gcode/src/config.rs`, `crates/gcode/src/db.rs`, `crates/gcode/src/falkor.rs`, `crates/gcode/src/search/semantic.rs`, `crates/gcode/src/secrets.rs`

Migrate `gobby-code` from its duplicated foundation plumbing to the shared `gobby-core` crate so the architectural commitment in O1/D1/A1/AC1 is enforced by code, not just by prose. The current `crates/gcode/src/config.rs` resolves `FalkorConfig`/`QdrantConfig`/`EmbeddingConfig` inline, `crates/gcode/src/db.rs` owns its own PostgreSQL connection helpers and config-store reads, `crates/gcode/src/falkor.rs` owns its own FalkorDB client and probe, and `crates/gcode/src/search/semantic.rs` issues raw Qdrant search REST. All four of these surfaces have direct counterparts in `gobby-core` (`gobby-core::config::resolve_*_config` + `CoreContext`, `gobby-core::postgres`, `gobby-core::falkor::with_graph` + `GraphClient`, `gobby-core::qdrant::with_qdrant` + `collection_name` + `search` + `upsert`).

Cargo wiring:

- `crates/gcode/Cargo.toml` declares the `gobby-core` dependency with the features this plan needs enabled: `postgres`, `falkor`, `qdrant`, `search`, `indexing` (or `full`). The enablement is unconditional in `[dependencies]` so the consumer migration compiles in both default and `--no-default-features` builds of `gobby-code`.

Module migration:

- `crates/gcode/src/config.rs` keeps `Context` building but resolves FalkorDB/Qdrant/embedding configs via `gobby_core::config::resolve_falkordb_config` / `resolve_qdrant_config` / `resolve_embedding_config` (or by composing `gobby_core::config::CoreContext`). `QdrantConfig` and `EmbeddingConfig` references in `gobby-code` become thin re-exports of the gobby-core types so existing call sites keep compiling. `FalkorConfig` cannot be a pure re-export because `gobby_core::config::FalkorConfig` exposes only connection-level fields (`host`, `port`, `password`) while the external Phase 7 contract test in the Gobby repo source-inspects `crates/gcode/src/config.rs` for a local `FalkorConfig { graph_name: String }`; see "Phase 7 compatibility wrapper" below for the explicit wrapper contract. The duplicated resolver bodies (env precedence over `config_store` over defaults, `decode_config_value`, JSON-null handling) are removed regardless. Code-specific projection settings that are not part of `gobby-core`'s connection/auth surface — for example the optional vector dimension override consumed by §2.5's code-symbol vector lifecycle — are added as sibling consumer-owned config types in `crates/gcode/src/config.rs` (such as `CodeVectorSettings { vector_dim: Option<usize> }`), resolved through the same `ConfigSource` adapter pipeline (env → `config_store` JSON-decoded → defaults), rather than extending the re-exported `gobby-core` types. `gobby-core::config::EmbeddingConfig` remains the connection/auth surface (`api_base`, `model`, `api_key`) and is not extended for code-specific projection metadata.
- `crates/gcode/src/db.rs` delegates `connect_readonly`, `connect_readwrite`, raw `config_store` reads, and any schema-validation plumbing to `gobby_core::postgres` adapters. `gobby-code` keeps only code-specific helpers on top of the shared adapter; duplicated PostgreSQL client/connect logic is removed.
- `crates/gcode/src/falkor.rs` retains its public facade for the external Phase 7 contract but routes connection plumbing and graph queries through `gobby_core::falkor::with_graph` / `gobby_core::falkor::GraphClient::from_config(config, graph_name)`. The `"gobby_code"` graph name remains consumer-supplied at every call site; no graph default leaks into gobby-core. The facade is an explicit compatibility wrapper, not a pure re-export — `falkor.rs` keeps the local `FalkorClient`, `from_config`, and `with_falkor` symbols that the Phase 7 test source-inspects; see "Phase 7 compatibility wrapper" below for the explicit wrapper contract.
- `crates/gcode/src/search/semantic.rs` calls `gobby_core::qdrant::with_qdrant`, `gobby_core::qdrant::collection_name(.., CollectionScope::Custom("code_symbols_<project_id>"))`, and `gobby_core::qdrant::search` for the soft semantic-search path instead of issuing raw Qdrant REST calls. Embedding config absence remains consumer-owned: the search path checks `Option<&EmbeddingConfig>` and reports missing embedding via the shared degradation vocabulary before entering the Qdrant adapter.
- `crates/gcode/src/lib.rs` re-exports the foundation-bridged module surface used by the rest of this plan and hosts the regression test that asserts the consumer-migration invariants.
- `crates/gcode/src/secrets.rs` keeps the Fernet-backed `resolve_config_value` / `resolve_secret` helpers that the consumer adapter calls through. Secret-token decryption stays in `gobby-code` (Fernet crypto is not pulled into `gobby-core`); the adapter simply pipes the gobby-core decoded value through `secrets::resolve_config_value` before returning it.

**Consumer adapter contract** (matches the foundation plan's `ConfigSource` trait):

`crates/gcode/src/config.rs` defines a PostgreSQL-backed `ConfigSource` implementation owned by the consumer. The adapter wraps `&mut postgres::Client` and routes every config-store read through the shared decode pipeline plus the local secret-resolution helper:

```rust,ignore
// Lives in crates/gcode/src/config.rs (or a sibling consumer adapter module).
// Implements gobby_core::config::ConfigSource for the attached-mode resolver.
struct PostgresConfigSource<'a> {
    conn: &'a mut postgres::Client,
}

impl gobby_core::config::ConfigSource for PostgresConfigSource<'_> {
    fn config_value(&mut self, key: &str) -> Option<String> {
        gobby_core::postgres::read_config_value(self.conn, key)
            .ok()
            .flatten()
            .and_then(|raw| gobby_core::config::decode_config_value(&raw))
    }

    fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {
        crate::secrets::resolve_config_value(value, self.conn)
    }
}
```

`gobby-code` then calls `gobby_core::config::resolve_falkordb_config(&mut source)` / `resolve_qdrant_config(&mut source)` / `resolve_embedding_config(&mut source)` with that adapter in attached mode. Standalone / no-database paths pass `gobby_core::config::EnvOnlySource` instead, matching the foundation plan's contract.

The adapter is the single boundary between gobby-code's Fernet-backed secret store and gobby-core's database-agnostic resolver. It preserves the existing four-step pipeline `env → config_store (JSON-decoded) → $secret:/${VAR} interpolation → defaults` exactly:

- **Env precedence**: `resolve_*_config` checks env vars (`GOBBY_FALKORDB_HOST`, `GOBBY_QDRANT_URL`, `GOBBY_EMBEDDING_API_KEY`, etc.) before calling `ConfigSource.config_value`, so env overrides remain authoritative for standalone, tests, and diagnostics.
- **JSON decode**: `ConfigSource.config_value` always pipes raw `read_config_value` output through `decode_config_value`; a JSON-encoded value such as `"\"http://host:7474\""` is unwrapped to `http://host:7474`; JSON null returns `None` so missing values surface cleanly.
- **Secret resolution**: every config-store value still passes through `crate::secrets::resolve_config_value`, so `$secret:falkordb_password`, `$secret:qdrant_api_key`, and `$secret:embedding_api_key` continue to resolve from `gcode`-managed Fernet tokens. `${VAR}` and `${VAR:-default}` interpolation also continues to work for non-secret env templates.

**Phase 7 compatibility wrapper** (matches A1's Phase 7 contract gate and §1.1's compatibility-facade clause):

The Gobby-repo Phase 7 contract test at `gobby/tests/code_index/test_gcode_phase7_contract.py` source-inspects `gobby-code` for a specific set of public symbols and field shapes. Until that external source-inspection contract is revised (see VS1 and DF1), `gobby-code` MUST preserve the following local shapes in `gobby-code` source — they cannot collapse into pure re-exports of `gobby_core` types:

- `crates/gcode/src/config.rs` defines a local `pub struct FalkorConfig { pub host: String, pub port: u16, pub password: Option<String>, pub graph_name: String }`. The `host`/`port`/`password` fields mirror `gobby_core::config::FalkorConfig` so connection-level data is sourced from `gobby_core::config::resolve_falkordb_config`. The `graph_name` field is gcode-owned and defaults to the `"gobby_code"` constant defined in `config.rs`. Config-key and env-var strings the Phase 7 test inspects (`GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD`, and the corresponding `config_store` keys) remain present in `config.rs` even though the resolver bodies are replaced by calls into `gobby_core`.
- `crates/gcode/src/falkor.rs` defines a local `pub struct FalkorClient { graph: SyncGraph }` plus `impl FalkorClient { pub fn from_config(config: &FalkorConfig) -> anyhow::Result<Self> }` and the free function `pub fn with_falkor<T>(ctx: &Context, default: T, f: impl FnOnce(&mut FalkorClient) -> anyhow::Result<T>) -> anyhow::Result<T>`. The `falkordb::{FalkorClientBuilder, FalkorConnectionInfo, SyncGraph}` import chain remains visible in `falkor.rs` so the source-inspection contract resolves. Internally `FalkorClient::from_config` builds a `gobby_core::config::FalkorConfig { host, port, password }` from the local wrapper, calls `gobby_core::falkor::GraphClient::from_config(&core_config, &config.graph_name)`, and stores the resulting graph handle. `with_falkor(ctx, default, f)` delegates to `gobby_core::falkor::with_graph(ctx.falkordb.as_ref().map(into_core_falkor_config).as_ref(), &graph_name, default, |gc| f(&mut FalkorClient::wrapping(gc)))` (or an equivalent translation) so ServiceState transitions enter the gobby-core boundary while the public wrapper signature remains stable.
- The `gobby_code` graph name is sourced from `FalkorConfig.graph_name` at every call site; the literal string `"gobby_code"` lives only in the `FALKORDB_GRAPH_NAME` constant in `config.rs` (gcode-owned default) and any necessary call-site wiring. No graph-name default leaks into `gobby_core`.
- `crates/gcode/src/falkor.rs` preserves the public read API that the external Phase 7 test source-inspects:
  - `pub fn count_callers(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize>`
  - `pub fn count_usages(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize>`
  - `pub fn find_callers(ctx: &Context, symbol_id: &str, limit: usize, offset: usize) -> anyhow::Result<Vec<GraphResult>>`
  - `pub fn find_usages(ctx: &Context, symbol_id: &str, limit: usize, offset: usize) -> anyhow::Result<Vec<GraphResult>>`
  - `pub fn find_callers_batch(ctx: &Context, symbol_ids: &[String], limit: usize) -> anyhow::Result<HashMap<String, Vec<GraphResult>>>`
  - `pub fn find_callees_batch(ctx: &Context, symbol_ids: &[String], limit: usize) -> anyhow::Result<HashMap<String, Vec<GraphResult>>>`
  - `pub fn get_imports(ctx: &Context, file_path: &str) -> anyhow::Result<Vec<GraphResult>>`
  - `pub fn blast_radius(ctx: &Context, target: &BlastRadiusTarget, depth: usize, limit: usize) -> anyhow::Result<Vec<GraphResult>>`
  Each helper retains its sibling Cypher-builder function in the same file (`count_callers_query`, `count_usages_query`, `find_callers_query`, `find_usages_query`, `find_callers_batch_query`, `find_callees_batch_query`, `get_imports_query`, `blast_radius_query`), keeping the existing numeric clamping (for example `depth`/`limit`/`offset` upper bounds) and string-parameter escaping behavior. Internals MAY delegate to `graph::code_graph` once §2.3 lands so query construction has a single canonical owner (see §2.3.4), but the public signatures and the named `*_query` helpers MUST remain visible to compile-time and source-inspection assertions in `falkor.rs`.
- The following source fragments must remain visible in `crates/gcode/src/falkor.rs`, even if their surrounding bodies are restructured to delegate to `gobby_core::falkor::with_graph` / `gobby_core::falkor::GraphClient`:
  - `urlencoding::encode(password)` — used when constructing the Falkor connection URL.
  - The `falkor://:{}@{}:{}` URL shape literal in the connection-string builder.
  - `.with_connection_info(conn_info)` on the `FalkorClientBuilder` chain.
  - `.with_params(&` (for example `.with_params(&params)`) when issuing parameterized graph queries.
  - `result.header` referenced when iterating the result set of a Falkor query.
  - `FalkorValue::None` referenced when normalising row values.
  - `let mut client =` — used to bind a mutable Falkor client handle before issuing query work.
  - `ctx.falkordb` — read on the resolved `Context` to access the gcode-owned FalkorDB config struct.
  These fragments are what the Gobby-repo Phase 7 test searches for as a proxy for "gcode still owns a local Falkor connection/query surface." Wrapper internals MAY add `gobby_core::falkor` delegation alongside them (and §2.3 requires the read helpers to delegate internally), but the named source fragments above MUST NOT be erased from `falkor.rs`.
- `crates/gcode/src/falkor.rs` retains the following query/row-handling surface, which the Phase 7 test also source-inspects:
  - `pub type Row = HashMap<String, Value>` — a public type alias used by the row-handling helpers and the public read API, where `Value` is `serde_json::Value` (imported as `use serde_json::Value;` so the unqualified name `Value` appears at the public alias declaration). The Phase 7 test source-inspects for the exact substring `pub type Row = HashMap<String, Value>`, so the alias name must remain `Row`, the unqualified type `Value` must appear in the declaration (not `serde_json::Value`), and the alias must remain at the file's public surface. `FalkorValue` is the raw row type returned by the `falkordb` crate; it remains visible in `falkor.rs` (per §1.5.14) for the internal conversion helper and source-fragment checks, but the public `Row` alias is `HashMap<String, Value>` with `Value = serde_json::Value`, not `HashMap<String, FalkorValue>`.
  - `pub fn query(&mut self, cypher: &str, params: Option<HashMap<String, String>>) -> anyhow::Result<Vec<Row>>` (or the equivalent signature the existing wrapper uses) on `impl FalkorClient` — the public Cypher entry point that the Phase 7 test asserts. Internals MAY delegate to `gobby_core::falkor::GraphClient::query` but the public method name, the `cypher: &str` parameter, the `Option<HashMap<String, String>>` params shape, and the `Vec<Row>` return type must remain visible at the public API.
  - `fn parse_falkor_result(...)` — a private helper that converts `FalkorResult` rows into the public `Row` type, preserving null/value normalisation. The helper consumes `FalkorValue` rows from `falkordb` and produces `Row = HashMap<String, Value>` entries (where `Value = serde_json::Value`) via the internal `falkor_value_to_json` conversion. The Phase 7 test asserts this helper exists by name in `falkor.rs`.
- `crates/gcode/src/falkor.rs` retains the production-read-query helper and literal-fragment surface that the Phase 7 production-read-query test asserts. These are query-builder utilities and literal Cypher fragments that the existing `*_query` helpers compose; both the helper functions and the literal substrings must remain visible in `falkor.rs`:
  - `fn cypher_string_literal(value: &str) -> String` — escapes and quotes a string for inline Cypher literal substitution.
  - `fn id_list_literal(ids: &[String]) -> String` — renders a comma-separated list of quoted IDs for inline `IN [...]` clauses.
  - `fn clamp_offset(offset: usize) -> usize` (or matching signature) — clamps the pagination offset to the defined upper bound and is consumed by `find_callers_query`, `find_usages_query`, and similar paginated helpers.
  - The literal Cypher fragment `target:CodeSymbol OR target:UnresolvedCallee OR target:ExternalSymbol` — must appear verbatim inside the relevant `*_query` helper bodies (callers/usages production reads) so the union of allowed target labels is testable by source inspection.
  - The literal `SKIP {offset} LIMIT {limit}` fragment — must appear verbatim inside the paginated `*_query` helper bodies (`find_callers_query`, `find_usages_query`) where pagination clamping is applied via `clamp_offset` and a clamped `limit`.
  - The literal `target.id IN [{ids}]` fragment — must appear verbatim inside the batch helpers (`find_callers_batch_query`, `find_callees_batch_query`) where `{ids}` is the inline list rendered via `id_list_literal`.
  - **Unbound-parameter ban**: the generated Cypher strings produced by these helpers MUST NOT contain `$offset`, `$limit`, or `$ids`. Pagination and ID-list values are substituted inline via `clamp_offset`, `cypher_string_literal`, and `id_list_literal`; they are not bound through `.with_params(...)`. The Phase 7 production-read-query test asserts both that the named literal fragments are present and that `$offset` / `$limit` / `$ids` do not appear in the produced query strings.

The wrapper layer is the only place in `gobby-code` allowed to keep the duplicated symbol shapes that mirror `gobby_core::falkor::GraphClient` / `with_graph`. All other code-graph consumers in `gobby-code` (the §2.2/§2.3/§2.4 writers, readers, and CLI commands) call the wrapper or `gobby_core::falkor::with_graph` directly; they do not bypass the wrapper to instantiate `falkordb::FalkorClientBuilder` themselves.

Behavioral guarantees:

- All FalkorDB ServiceState transitions in `gobby-code` enter through `gobby_core::falkor::with_graph`; `gobby-code` does not implement its own four-state Falkor probe.
- All non-lifecycle Qdrant ServiceState transitions enter through `gobby_core::qdrant::with_qdrant`; raw Qdrant REST is allowed only inside the §2.5 lifecycle exception scope (see A1).
- PostgreSQL connection plumbing flows through `gobby_core::postgres`; gobby-code does not duplicate `connect_readonly` / `connect_readwrite` bodies.
- `cargo build -p gobby-code` succeeds with default features and with `--no-default-features`, matching the workspace VS1 verification.
- Attached mode resolves FalkorDB, Qdrant, and embedding service settings from `config_store` plus `$secret:` resolution rather than from env-only paths or duplicated resolver bodies; standalone/tests use `EnvOnlySource` for the same call sites.

**Acceptance:**

- 1.5.1 - `crates/gcode/Cargo.toml` enables the required `gobby-core` features for the consumer migration: `postgres`, `falkor`, `qdrant`, `search`, and `indexing` (or the umbrella `full` feature). file: `crates/gcode/Cargo.toml`.
- 1.5.2 - `gobby-code` compiles with default features and with `--no-default-features` after the foundation wiring lands, with the gobby-core feature gates supplying the adapters used by `config.rs`, `db.rs`, `falkor.rs`, and `search/semantic.rs`. file: `crates/gcode/Cargo.toml`.
- 1.5.3 - `crates/gcode/src/config.rs` resolves FalkorDB, Qdrant, and embedding configs via `gobby_core::config::resolve_*_config` (or `gobby_core::config::CoreContext`) and contains no duplicated env-precedence/`config_store`/`decode_config_value` resolver bodies. `QdrantConfig` and `EmbeddingConfig` are thin re-exports of the gobby-core types; `FalkorConfig` remains a local compatibility wrapper per the §1.5 "Phase 7 compatibility wrapper" subsection. file: `crates/gcode/src/config.rs`.
- 1.5.4 - `crates/gcode/src/db.rs` delegates `connect_readonly`, `connect_readwrite`, and `config_store` reads to `gobby_core::postgres` adapters; no duplicated PostgreSQL client/connect/config-store logic remains. file: `crates/gcode/src/db.rs`.
- 1.5.5 - `crates/gcode/src/falkor.rs` keeps its public facade as an explicit compatibility wrapper (not a pure re-export) per the §1.5 "Phase 7 compatibility wrapper" subsection and routes connection and query plumbing through `gobby_core::falkor::with_graph` / `gobby_core::falkor::GraphClient`; the `"gobby_code"` graph name remains consumer-supplied. file: `crates/gcode/src/falkor.rs`.
- 1.5.6 - `crates/gcode/src/search/semantic.rs` calls `gobby_core::qdrant::with_qdrant`, `gobby_core::qdrant::collection_name(.., CollectionScope::Custom(..))`, and `gobby_core::qdrant::search` for the soft semantic-search path instead of issuing raw Qdrant search REST. file: `crates/gcode/src/search/semantic.rs`.
- 1.5.7 - A consumer-migration regression test asserts that `gobby-code` config resolution, PostgreSQL connection plumbing, Falkor ServiceState boundaries, and non-lifecycle Qdrant operations route through `gobby_core` modules rather than duplicated `gobby-code` wrappers. test: `crates/gcode/src/lib.rs::tests::foundation_consumer_migration`.
- 1.5.8 - `crates/gcode/src/config.rs` defines a `PostgresConfigSource` (or equivalently named consumer adapter) that implements `gobby_core::config::ConfigSource`, reads via `gobby_core::postgres::read_config_value`, decodes via `gobby_core::config::decode_config_value`, and resolves `$secret:NAME` / `${VAR}` patterns via `crate::secrets::resolve_config_value`. Attached-mode callers pass this adapter to `resolve_*_config`; standalone/no-database call sites use `gobby_core::config::EnvOnlySource`. file: `crates/gcode/src/config.rs`, `crates/gcode/src/secrets.rs`.
- 1.5.9 - Env vars take precedence over `config_store` and JSON-encoded `config_store` values are decoded correctly through the adapter pipeline (string values unwrapped, arrays/objects re-serialized, JSON null returns `None`) for FalkorDB host/port/password, Qdrant URL/API key, and embedding URL/model/API key. test: `crates/gcode/src/config.rs::tests::adapter_env_precedence_and_json_decode`.
- 1.5.10 - `$secret:falkordb_password`, `$secret:qdrant_api_key`, and `$secret:embedding_api_key` stored in `config_store` still resolve through the adapter in attached mode via `crate::secrets::resolve_config_value`, yielding decrypted plaintext for the resulting `FalkorConfig.password`, `QdrantConfig.api_key`, and `EmbeddingConfig.api_key` fields. test: `crates/gcode/src/config.rs::tests::adapter_resolves_config_store_secrets`.
- 1.5.11 - `crates/gcode/src/config.rs` defines a local `pub struct FalkorConfig { pub host: String, pub port: u16, pub password: Option<String>, pub graph_name: String }`; `graph_name` is populated from the gcode-owned `FALKORDB_GRAPH_NAME = "gobby_code"` constant; connection-level fields are sourced from `gobby_core::config::resolve_falkordb_config`. The `FalkorConfig { graph_name: String }` shape that the external Phase 7 contract test source-inspects is preserved. test: `crates/gcode/src/config.rs::tests::falkor_config_wrapper_shape`.
- 1.5.12 - `crates/gcode/src/falkor.rs` defines a local `pub struct FalkorClient { graph: SyncGraph }`, an `impl FalkorClient { pub fn from_config(config: &FalkorConfig) -> anyhow::Result<Self> }`, and a free function `pub fn with_falkor<T>(ctx: &Context, default: T, f: impl FnOnce(&mut FalkorClient) -> anyhow::Result<T>) -> anyhow::Result<T>`; the `falkordb::{FalkorClientBuilder, FalkorConnectionInfo, SyncGraph}` import chain remains visible in `falkor.rs`. The wrapper internals delegate to `gobby_core::falkor::with_graph` / `gobby_core::falkor::GraphClient::from_config(&core_config, &config.graph_name)` so behavior routes through gobby-core while the source-inspection shape that the Phase 7 contract test asserts is preserved. test: `crates/gcode/src/falkor.rs::tests::falkor_client_wrapper_shape`.
- 1.5.13 - `crates/gcode/src/falkor.rs` preserves the eight public read helpers (`count_callers`, `count_usages`, `find_callers`, `find_usages`, `find_callers_batch`, `find_callees_batch`, `get_imports`, `blast_radius`) and their sibling Cypher-builder helpers (`count_callers_query`, `count_usages_query`, `find_callers_query`, `find_usages_query`, `find_callers_batch_query`, `find_callees_batch_query`, `get_imports_query`, `blast_radius_query`) at the file's public surface. Internals may delegate to `graph::code_graph` reads (§2.3.4) or `gobby_core::falkor`, but the names and signatures listed in the §1.5 Phase 7 compatibility wrapper subsection remain visible to compile-time references and source-inspection assertions. test: `crates/gcode/src/falkor.rs::tests::phase7_read_helpers_visible`.
- 1.5.14 - `crates/gcode/src/falkor.rs` retains the source fragments the Gobby-repo Phase 7 test asserts: `urlencoding::encode(password)`, the `falkor://:{}@{}:{}` URL literal, `.with_connection_info(conn_info)`, `.with_params(&` (for example `with_params(&params)`), `result.header`, `FalkorValue::None`, `let mut client =`, and `ctx.falkordb`. Wrapper internals may add `gobby_core::falkor` delegation alongside but must not erase the named fragments. test: `crates/gcode/src/falkor.rs::tests::phase7_source_fragments_visible`.
- 1.5.15 - `crates/gcode/src/falkor.rs` exposes a public `Row` type alias declared as `pub type Row = HashMap<String, Value>` where `Value` is `serde_json::Value` imported into scope (`use serde_json::{..., Value};`) so the unqualified name `Value` appears at the alias declaration site exactly as the Gobby-repo Phase 7 test source-inspects (it asserts the literal substring `pub type Row = HashMap<String, Value>`). The file also exposes a public `query(&mut self, cypher: &str, params: Option<HashMap<String, String>>) -> anyhow::Result<Vec<Row>>` method on `FalkorClient` and a `parse_falkor_result` helper for converting Falkor result rows (`FalkorValue` entries from `falkordb`) into the public `Row` type via the internal `falkor_value_to_json` conversion. Wrapper internals may delegate to `gobby_core::falkor::GraphClient::query` but the public type alias declaration, the `query` method shape, and the named `parse_falkor_result` helper remain visible to source-inspection assertions; the local test reuses the same regex/literal-substring assertions the external Phase 7 test applies so the local and external gates stay aligned. test: `crates/gcode/src/falkor.rs::tests::phase7_query_surface_visible`.
- 1.5.16 - `crates/gcode/src/falkor.rs` retains the Cypher-builder helpers (`cypher_string_literal`, `id_list_literal`, `clamp_offset`) and literal fragments (`target:CodeSymbol OR target:UnresolvedCallee OR target:ExternalSymbol`, `SKIP {offset} LIMIT {limit}`, `target.id IN [{ids}]`) the Phase 7 production-read-query test asserts, and the Cypher strings produced by the public `*_query` helpers must not contain unbound `$offset`, `$limit`, or `$ids` parameters; pagination and ID-list values are substituted inline via `clamp_offset`, `cypher_string_literal`, and `id_list_literal`. test: `crates/gcode/src/falkor.rs::tests::phase7_query_helpers_and_literal_fragments_visible`.

## P2: Code Projection Core
`kind: framing`

### 2.1 Define provenance and confidence metadata [category: code] (depends: 1.1)
`kind: deliverable`
Targets: `crates/gcode/src/models.rs`, `crates/gcode/src/graph/code_graph.rs`, `crates/gcode/src/graph/report.rs`, `crates/gcode/src/vector/code_symbols.rs`

Add a shared graph metadata model:

- `provenance`: `EXTRACTED`, `INFERRED`, or `AMBIGUOUS`.
- `confidence`: optional float. Deterministic code edges use `1.0`.
- `source_system`: producer name, such as `gcode`, `gobby-memory`, or `qdrant`.
- Source details such as file path, line, symbol ID, or matching method where available.

Code-derived `CALLS`, `IMPORTS`, and `DEFINES` are always `EXTRACTED` with `source_system = "gcode"`. Code-symbol vector payloads use `source_system = "gcode"` and may include symbol summary text only when already present. Memory-derived and code/memory bridge edges are `INFERRED` or `AMBIGUOUS` and remain memory-owned.

**Acceptance:**

- 2.1.1 - Graph result structs expose optional metadata fields without breaking existing JSON consumers. file: `crates/gcode/src/models.rs`.
- 2.1.2 - Code edge writes stamp `provenance = "EXTRACTED"`, `confidence = 1.0`, and `source_system = "gcode"`. test: `crates/gcode/src/graph/code_graph.rs::tests::code_edges_carry_provenance`.
- 2.1.3 - Report output labels bridge edges as inferred hypotheses when present. test: `crates/gcode/src/graph/report.rs::tests::bridge_edges_are_hypotheses`.

### 2.2 Port code graph writes into the Rust core [category: code] (depends: 1.3, 2.1)
`kind: deliverable`
Targets: `crates/gcode/src/graph/code_graph.rs`, `crates/gcode/src/models.rs`

Implement `CodeGraph` write APIs for the deterministic FalkorDB `gobby_code` projection:

- `ensure_file_node`
- `add_imports`
- `add_definitions`
- `add_calls`
- unresolved and external call target handling
- `delete_file_graph`
- `cleanup_orphans`
- `clear_project`

The write path preserves Python parity where IDs are externally visible. UUID5 generation must continue to match the Python daemon's `Symbol.make_id()` contract for symbols and any parity-sensitive target IDs.

**Acceptance:**

- 2.2.1 - IMPORTS, DEFINES, and CALLS writes match existing graph semantics with metadata added. file: `crates/gcode/src/graph/code_graph.rs`.
- 2.2.2 - Stale edge cleanup preserves still-current symbols and incoming calls from other files. test: `crates/gcode/src/graph/code_graph.rs::tests::delete_preserves_current_symbols`.
- 2.2.3 - Orphan cleanup removes unused module, external, unresolved, and detached symbol nodes scoped to the project. test: `crates/gcode/src/graph/code_graph.rs::tests::cleanup_orphans_is_project_scoped`.
- 2.2.4 - UUID5 parity tests cover all public IDs generated by the write path. test: `crates/gcode/src/models.rs::tests::uuid5_python_parity`.

### 2.3 Port code graph reads into the Rust core [category: code] (depends: 2.2)
`kind: deliverable`
Targets: `crates/gcode/src/graph/code_graph.rs`, `crates/gcode/src/search/graph_boost.rs`, `crates/gcode/src/commands/graph.rs`, `crates/gcode/src/falkor.rs`

Implement reusable read APIs that return stable graph payloads:

- project overview graph
- file graph
- symbol neighbors
- blast radius graph
- graph search/boost helpers needed by existing search commands

These APIs require available FalkorDB for graph reads. Empty graphs are valid only for successful queries against an available graph service.

The existing public read helpers in `crates/gcode/src/falkor.rs` (`count_callers`, `count_usages`, `find_callers`, `find_usages`, `find_callers_batch`, `find_callees_batch`, `get_imports`, `blast_radius`) remain visible per the §1.5 Phase 7 compatibility wrapper. Their internal Falkor query work delegates to the new `graph::code_graph` read APIs after this section lands so query construction has a single canonical owner. The helpers' public signatures, sibling `*_query` Cypher builders, `Row`/`query`/`parse_falkor_result` surface, Cypher-builder helpers (`cypher_string_literal`, `id_list_literal`, `clamp_offset`), literal Cypher fragments (`target:CodeSymbol OR target:UnresolvedCallee OR target:ExternalSymbol`, `SKIP {offset} LIMIT {limit}`, `target.id IN [{ids}]`), the unbound-parameter ban for `$offset` / `$limit` / `$ids` in generated query strings, clamping behavior, and Phase 7 source-inspection fragments listed in §1.5 (including §1.5.13 / §1.5.14 / §1.5.15 / §1.5.16) remain unchanged.

**Acceptance:**

- 2.3.1 - Read APIs return the existing node/link JSON shape with optional metadata on links. file: `crates/gcode/src/graph/code_graph.rs`.
- 2.3.2 - Existing search graph boost behavior still handles missing graph config gracefully where search semantics allow degradation. test: `crates/gcode/src/search/graph_boost.rs::tests`.
- 2.3.3 - Hard graph commands fail non-zero with typed errors when FalkorDB is unavailable. test: `crates/gcode/src/commands/graph.rs::tests::graph_reads_require_falkor`.
- 2.3.4 - Public `falkor.rs` read helpers (`count_callers`, `count_usages`, `find_callers`, `find_usages`, `find_callers_batch`, `find_callees_batch`, `get_imports`, `blast_radius`) delegate their internal Falkor query work to the new `graph::code_graph` read APIs while preserving public signatures, `*_query` siblings, clamping behavior, the `Row` / `query` / `parse_falkor_result` surface, the Cypher-builder helpers and literal fragments, and the unbound-parameter ban pinned by §1.5.13 / §1.5.14 / §1.5.15 / §1.5.16. test: `crates/gcode/src/falkor.rs::tests::read_helpers_delegate_to_code_graph`.

### 2.4 Wrap core operations with gcode graph commands [category: code] (depends: 1.2, 1.4, 2.2, 2.3)
`kind: deliverable`
Targets: `crates/gcode/src/commands/graph.rs`, `crates/gcode/src/db.rs`, `crates/gcode/src/main.rs`, `crates/gcode/tests/graph_standalone.rs`

Add or rewire CLI commands so they call Rust core APIs directly:

- `gcode graph sync-file --file <path>`
- `gcode graph clear`
- `gcode graph rebuild`
- `gcode graph overview`
- `gcode graph file --file <path>`
- `gcode graph neighbors --symbol-id <id> --limit <n>`
- `gcode graph blast-radius [--symbol-id <id> | --file <path>] --depth <n> --limit <n>`

No daemon HTTP calls are allowed from these commands. Output uses the existing global `--format` flag with `output::print_json` and `output::print_text`.

The existing top-level read commands `gcode callers`, `gcode usages`, `gcode imports`, and `gcode blast-radius` remain available as **additive** thin wrappers over the new `graph::code_graph` read APIs introduced by §2.3 — they are not removed, renamed, or replaced by the new `gcode graph overview|file|neighbors|blast-radius` surface. Both surfaces stay available. Each top-level command keeps its current clap surface (positional query argument plus existing flags such as `--limit`, `--offset`, and `--depth` where applicable), routes through `commands::graph::callers` / `commands::graph::usages` / `commands::graph::imports` / `commands::graph::blast_radius`, and preserves its current JSON output shape (field names, payload structure, pagination metadata). New optional metadata fields introduced by §2.1 are added with `#[serde(skip_serializing_if = "Option::is_none")]` so existing JSON consumers continue to parse the responses without changes. The existing parse tests `test_parse_callers_remains_top_level`, `test_parse_usages_remains_top_level`, `test_parse_imports_remains_top_level`, and `test_parse_blast_radius_remains_top_level` in `crates/gcode/src/main.rs` remain green after this section lands.

**Acceptance:**

- 2.4.1 - Lifecycle commands call `CodeGraph` directly and do not depend on the daemon process. file: `crates/gcode/src/commands/graph.rs`.
- 2.4.2 - `sync-file`, `clear`, and `rebuild` update graph sync state in PostgreSQL consistently with existing daemon semantics. file: `crates/gcode/src/db.rs`.
- 2.4.3 - Clap parsing covers all graph subcommands and global format handling. test: `crates/gcode/src/main.rs::tests::parse_graph_commands`.
- 2.4.4 - A daemon-stopped smoke test covers `overview`, `file`, `neighbors`, `blast-radius`, `sync-file`, `clear`, and `rebuild` against PostgreSQL plus FalkorDB. test: `crates/gcode/tests/graph_standalone.rs`.
- 2.4.5 - Existing top-level `gcode callers`, `gcode usages`, `gcode imports`, and `gcode blast-radius` commands remain available as additive wrappers over `graph::code_graph` reads with their current clap surface (positional query plus `--limit`, `--offset`, `--depth` flags as applicable), and the parse tests `test_parse_callers_remains_top_level`, `test_parse_usages_remains_top_level`, `test_parse_imports_remains_top_level`, and `test_parse_blast_radius_remains_top_level` still pass. test: `crates/gcode/src/main.rs::tests::test_parse_callers_remains_top_level`.
- 2.4.6 - JSON output shape for top-level `gcode callers`, `gcode usages`, `gcode imports`, and `gcode blast-radius` (field names, payload structure, pagination metadata) stays compatible with current consumers; new optional metadata fields per §2.1 are tagged with `#[serde(skip_serializing_if = "Option::is_none")]` so existing parsers continue to accept the responses. test: `crates/gcode/src/commands/graph.rs::tests::top_level_read_commands_preserve_json_shape`.

### 2.5 Port code-symbol vector projection into the Rust core [category: code] (depends: 1.1, 1.5, 2.1)
`kind: deliverable`
Targets: `crates/gcode/src/vector/code_symbols.rs`, `crates/gcode/src/search/semantic.rs`, `crates/gcode/src/config.rs`, `crates/gcode/src/commands/vector.rs`, `crates/gcode/tests/vector_projection.rs`

Implement reusable vector projection APIs for Qdrant code-symbol collections:

- Resolve embedding configuration through the standard Gobby config chain via `gobby_core::config::resolve_embedding_config` (env overrides first, then PostgreSQL `config_store`, then hardcoded defaults where a default is valid). Attached mode reaches `config_store` through Gobby bootstrap or the daemon database broker, not through a project `.env`.
- Generate code-symbol vectors by calling OpenAI-compatible `/v1/embeddings` directly from Rust. The daemon embedding service is not used for code-index projection sync.
- Ensure Qdrant collections using the existing `code_symbols_<project_id>` names. The collection name is derived via `gobby_core::qdrant::collection_name(.., CollectionScope::Custom("code_symbols_<project_id>"))` so existing collections are preserved verbatim without migration.
- Build vector payloads from indexed symbol facts: project ID, file path, symbol ID, name, kind, language, signature/docstring where present, source range, and optional existing summary text. Every payload also carries the §2.1 provenance metadata fields: `provenance = "EXTRACTED"`, `confidence = 1.0`, `source_system = "gcode"`, and source-detail fields (file path, source range/line, symbol ID) so vector hits can be distinguished from other vector producers in downstream agents and reports.
- Delete stale vectors by `project_id` plus `file_path` before file-level re-upsert.
- Upsert all current symbols for a file via `gobby_core::qdrant::upsert` after embedding succeeds.
- Clear project vectors and rebuild vectors from PostgreSQL code facts.
- Treat LLM-generated symbol summaries as optional enrichment; missing summaries must not block vector sync.

**Foundation boundary for vector lifecycle** (matches A1's vector projection lifecycle exception):

- `gobby_core::qdrant` exposes connection-level config (`QdrantConfig`), `with_qdrant` (the ServiceState boundary), `collection_name` (caller-controlled naming), `search`, and `upsert`. Collection lifecycle (ensure collection with vector params, delete-by-filter, clear/drop) is not part of the foundation surface and is consumer-owned.
- The ensure-collection, delete-by-filter, and clear-collection HTTP requests live only in `crates/gcode/src/vector/code_symbols.rs`. No other `gobby-code` file may issue raw Qdrant lifecycle REST.
- Even inside `vector/code_symbols.rs`, lifecycle operations resolve config through `gobby_core::config::resolve_qdrant_config`, enter the ServiceState/degradation boundary through `gobby_core::qdrant::with_qdrant`, and reuse `gobby_core::qdrant::collection_name(.., CollectionScope::Custom("code_symbols_<project_id>"))` for naming.
- Non-lifecycle vector operations (upsert after embedding, soft search) call `gobby_core::qdrant::upsert` and `gobby_core::qdrant::search` directly.

**Vector parameter handling for ensure/rebuild lifecycle**:

Qdrant collection creation requires explicit vector parameters (`size` and `distance`), and OpenAI-compatible embedding models can return different dimensions (`text-embedding-3-small` returns 1536, `text-embedding-3-large` returns 3072, third-party models vary). Lifecycle operations in `vector::code_symbols` must derive these parameters deterministically and refuse to migrate or silently rebuild incompatible existing collections.

Vector parameter rules:

- **Distance metric is fixed at `Cosine`** for `code_symbols_<project_id>` collections. The choice is documented in `crates/gcode/src/vector/code_symbols.rs` alongside the ensure-collection helper; it matches the existing Python daemon behavior so attached-mode collections remain compatible.
- **Vector size source order**: an explicit consumer-owned `vector_dim` setting wins when present. The setting lives on a `gobby-code`-owned sibling config type (`CodeVectorSettings { vector_dim: Option<usize> }` in `crates/gcode/src/config.rs`); it is **not** added to `gobby_core::config::EmbeddingConfig`. The value is resolved through the §1.5 `ConfigSource` adapter pipeline: env `GOBBY_EMBEDDING_VECTOR_DIM` first, then `config_store` key `embeddings.vector_dim` decoded via `gobby_core::config::decode_config_value` (JSON integers are accepted; JSON null returns `None`; invalid values return a typed config error). When no explicit value is present, the dimension is probed once by sending a fixed canary prompt (e.g. `"dimension_probe"`) to the configured embedding endpoint and using the response vector length. The probed value is cached on the `vector::code_symbols` lifecycle context for the remainder of the command so a single command does not pay the probe cost more than once.
- **Ensure semantics for missing collection**: `ensure_collection` issues `PUT /collections/<name>` with `vector_size`, `distance: "Cosine"`, and any payload/index settings required for symbol filtering. On success the collection is ready for upsert.
- **Ensure semantics for compatible existing collection**: when the collection already exists and its reported `config.params.vectors.size` plus `config.params.vectors.distance` match the resolved parameters, `ensure_collection` is a no-op. Upsert and delete-by-filter proceed against the existing collection without recreation.
- **Ensure semantics for incompatible existing collection (no migration)**: when the collection already exists but its reported `size` or `distance` does not match the resolved parameters, hard lifecycle commands (`gcode vector sync-file`, `gcode vector rebuild`) fail with a typed `VectorLifecycleError::DimensionMismatch { collection, expected_size, found_size, expected_distance, found_distance }` carrying actionable text. The collection is **not** dropped, cleared, or recreated. `gcode vector clear` deletes all points but does not change the collection's vector schema; it surfaces the same dimension-mismatch error before issuing any destructive HTTP if the resolved schema is being asked to write incompatible vectors.
- **Soft search compatibility**: the soft search path in `search/semantic.rs` does not call `ensure_collection`; it reports missing-collection / dimension-mismatch responses from Qdrant via the shared degradation vocabulary rather than failing the entire `gcode search` invocation.

**Acceptance:**

- 2.5.1 - The embedding client sends OpenAI-compatible requests and parses successful/error responses. test: `crates/gcode/src/vector/code_symbols.rs::tests::embedding_request_response`.
- 2.5.2 - Qdrant REST coverage proves ensure collection, delete-by-file, upsert, clear, and rebuild behavior. test: `crates/gcode/tests/vector_projection.rs`.
- 2.5.3 - Collection naming remains `code_symbols_<project_id>` via `gobby_core::qdrant::collection_name(.., CollectionScope::Custom(..))` and does not require migration. test: `crates/gcode/src/vector/code_symbols.rs::tests::collection_name_compatibility`.
- 2.5.4 - Missing Qdrant or embedding config produces typed degradation for soft search paths and clear non-zero errors for hard vector lifecycle commands. test: `crates/gcode/src/commands/vector.rs::tests::vector_lifecycle_requires_config`.
- 2.5.5 - Missing symbol summaries do not block vector projection sync. test: `crates/gcode/src/vector/code_symbols.rs::tests::summaries_are_optional_enrichment`.
- 2.5.6 - Code-specific Qdrant lifecycle HTTP (ensure collection, delete-by-filter, clear) stays scoped to `crates/gcode/src/vector/code_symbols.rs` and is the only `gobby-code` source file that issues raw Qdrant lifecycle REST requests. test: `crates/gcode/src/vector/code_symbols.rs::tests::lifecycle_http_scoped_to_module`.
- 2.5.7 - Vector projection resolves Qdrant config via `gobby_core::config::resolve_qdrant_config`, enters the ServiceState boundary via `gobby_core::qdrant::with_qdrant`, derives collection names via `gobby_core::qdrant::collection_name(.., CollectionScope::Custom(..))`, and routes search/upsert through `gobby_core::qdrant::search` / `gobby_core::qdrant::upsert`; direct REST is limited to lifecycle ensure/delete-by-filter/clear. test: `crates/gcode/src/vector/code_symbols.rs::tests::routes_through_gobby_core_qdrant`.
- 2.5.8 - `ensure_collection` resolves vector size from the consumer-owned `CodeVectorSettings.vector_dim` (resolved through the §1.5 `ConfigSource` adapter pipeline: env `GOBBY_EMBEDDING_VECTOR_DIM` first, then `config_store` key `embeddings.vector_dim` JSON-decoded via `gobby_core::config::decode_config_value`) when set, otherwise probes the configured embedding endpoint exactly once per lifecycle command; distance is `Cosine`. The probed dimension matches the response vector length for the configured model. The consumer-owned setting does not extend `gobby_core::config::EmbeddingConfig`. test: `crates/gcode/src/vector/code_symbols.rs::tests::ensure_collection_resolves_vector_size_and_distance`, `crates/gcode/src/config.rs::tests::vector_dim_setting_resolves_env_and_config_store`.
- 2.5.9 - Ensuring a missing collection creates it via `PUT /collections/<name>` with the resolved `vector_size` and `Cosine` distance; ensuring an existing collection whose `size`+`distance` match is a no-op (no destructive HTTP, no recreation). test: `crates/gcode/tests/vector_projection.rs::ensure_creates_missing_and_reuses_compatible`.
- 2.5.10 - Ensuring or rebuilding against an existing collection whose `size` or `distance` is incompatible with the resolved parameters fails with `VectorLifecycleError::DimensionMismatch { collection, expected_size, found_size, expected_distance, found_distance }`; no migration, drop, or recreation is performed and `clear` refuses incompatible destructive HTTP before issuing it. test: `crates/gcode/tests/vector_projection.rs::incompatible_existing_collection_errors_without_migration`.
- 2.5.11 - Vector payloads carry the §2.1 provenance metadata fields (`provenance = "EXTRACTED"`, `confidence = 1.0`, `source_system = "gcode"`, plus source-detail fields covering file path, source range, and symbol ID). Payloads round-trip through Qdrant upsert without losing these fields. test: `crates/gcode/src/vector/code_symbols.rs::tests::payloads_carry_provenance_metadata`.

### 2.6 Add projection lifecycle orchestration commands [category: code] (depends: 1.2, 1.4, 2.4, 2.5)
`kind: deliverable`
Targets: `crates/gcode/src/main.rs`, `crates/gcode/src/commands/index.rs`, `crates/gcode/src/commands/vector.rs`, `crates/gcode/src/commands/mod.rs`, `crates/gcode/src/projection/sync.rs`, `crates/gcode/src/db.rs`, `crates/gcode/src/output.rs`, `crates/gcode/tests/projection_standalone.rs`

Expose stable projection lifecycle surfaces for humans and Python transition shims:

- `gcode graph sync-file --file <path>`
- `gcode graph clear`
- `gcode graph rebuild`
- `gcode vector sync-file --file <path>`
- `gcode vector clear`
- `gcode vector rebuild`
- `gcode index --sync-projections`

`gcode index --sync-projections` writes PostgreSQL code facts via the §1.4 library API, then synchronously syncs graph and vector projections for the affected files through `projection::sync`. It is the daemon-triggered indexing path during migration. CLI JSON output is stable enough for Python shell-out shims: each projection reports `status`, `synced_files`, `synced_symbols`, `degraded`, and typed error details when available.

Required JSON shape for `gcode index --sync-projections --format json`:

```json
{
  "indexed_files": 12,
  "skipped_files": 0,
  "symbols_indexed": 348,
  "chunks_indexed": 921,
  "projections": {
    "graph": {
      "status": "ok | degraded | failed",
      "synced_files": 12,
      "synced_symbols": 348,
      "degraded": false,
      "error": null
    },
    "vector": {
      "status": "ok | degraded | failed",
      "synced_files": 12,
      "synced_symbols": 348,
      "degraded": false,
      "error": null
    }
  }
}
```

Hard lifecycle commands fail non-zero when their explicitly requested backing service is unavailable or misconfigured. Search/index paths that can return useful PostgreSQL-only results may return typed degradation instead, but they must make skipped projection work visible in JSON. Text-mode output for `gcode index --sync-projections` must go through `output::print_text` so shell-out consumers get a stable structured payload rather than free-form stderr writes.

**Acceptance:**

- 2.6.1 - Clap parsing covers graph/vector lifecycle commands and `gcode index --sync-projections`. test: `crates/gcode/src/main.rs::tests::parse_projection_lifecycle_commands`.
- 2.6.2 - `index --sync-projections` updates PostgreSQL sync state only after corresponding graph/vector sync succeeds. test: `crates/gcode/src/projection/sync.rs::tests::sync_state_tracks_projection_success`.
- 2.6.3 - JSON output for graph/vector lifecycle commands is stable and includes typed degradation/error fields. test: `crates/gcode/src/commands/vector.rs::tests::lifecycle_json_contract`.
- 2.6.4 - Daemon-stopped smoke tests cover graph plus vector lifecycle commands against PostgreSQL, FalkorDB, Qdrant, and a mock embedding endpoint. test: `crates/gcode/tests/projection_standalone.rs`.
- 2.6.5 - `gcode index --sync-projections --format json` emits indexing counts plus `projections.graph` and `projections.vector` objects with `status`, `synced_files`, `synced_symbols`, `degraded`, and optional `error` fields exactly matching the shape documented above. test: `crates/gcode/src/commands/index.rs::tests::sync_projections_json_contract`.
- 2.6.6 - `gcode index --sync-projections --format text` routes structured payload through `output::print_text` (no raw stderr-only status). test: `crates/gcode/src/commands/index.rs::tests::sync_projections_text_contract`.
- 2.6.7 - `crates/gcode/src/commands/mod.rs` exports the new `vector` command module via `pub mod vector;`, sequenced after §1.2's `pub mod setup;` edit so both command-module exports land in a single owner chain rather than racing on the same file. file: `crates/gcode/src/commands/mod.rs`.

## P3: Report And Daemon Migration Surfaces
`kind: framing`

### 3.1 Generate a project graph report in Rust core [category: code] (depends: 2.3)
`kind: deliverable`
Target: `crates/gcode/src/graph/report.rs`

Add `graph::report::generate_report` as a library API. The report is a derived artifact and can be regenerated at any time.

Report output includes JSON plus a compact Markdown field for humans and agent orientation:

- project ID and generation timestamp
- node and edge counts
- code edge counts by type
- high-degree files/symbols/modules
- incoming-call blast-radius hotspots
- unresolved and external call target frequency
- optional `RELATES_TO_CODE` summary when bridge edges are present
- confidence range for bridge edges when available
- suggested investigation questions
- degradation details for unavailable optional inputs

Keep v1 metrics simple and explainable. Do not add advanced community detection in this plan.

**Acceptance:**

- 3.1.1 - Report generation is available as a library API independent of the CLI. file: `crates/gcode/src/graph/report.rs`.
- 3.1.2 - Report JSON includes summary, hotspots, unresolved targets, optional bridge summaries, degradation details, and markdown. test: `crates/gcode/src/graph/report.rs::tests::report_shape`.
- 3.1.3 - Bridge edges are read-only and clearly marked as inferred. test: `crates/gcode/src/graph/report.rs::tests::bridge_edges_are_read_only`.
- 3.1.4 - Missing optional bridge data does not fail a code-only report; missing required graph service fails with a typed error. test: `crates/gcode/src/graph/report.rs::tests::report_degradation_contract`.

### 3.2 Add gcode graph report CLI wrapper [category: code] (depends: 2.6, 3.1)
`kind: deliverable`
Targets: `crates/gcode/src/commands/graph.rs`, `crates/gcode/src/main.rs`

Expose `gcode graph report --top-n <n>` as a thin wrapper over the Rust report API. It must use global `--format`, print JSON through `output::print_json`, and print structured text through `output::print_text`. Do not print raw Markdown as the whole text response.

**Acceptance:**

- 3.2.1 - `gcode graph report --format json` prints the serialized report. file: `crates/gcode/src/commands/graph.rs`.
- 3.2.2 - `gcode graph report --format text` prints a structured payload that includes `markdown`. test: `crates/gcode/src/commands/graph.rs::tests::report_text_structured_output`.
- 3.2.3 - Missing required graph services fail non-zero with a clear error and no fake empty report. test: `crates/gcode/src/commands/graph.rs::tests::report_requires_graph_service`.
- 3.2.4 - Clap parsing proves `--format` remains global and report-specific args stay minimal. test: `crates/gcode/src/main.rs::tests::parse_graph_report_global_format`.

### 3.3 Document daemon migration contracts [category: docs] (depends: 2.6, 3.2)
`kind: deliverable`
Target: `docs/guides/gcode-graph-core.md`

Document the migration contract for Gobby daemon consumers:

- Future Rust daemon links the library APIs directly.
- Python daemon shims may temporarily shell out to `gcode` JSON commands.
- Python `CodeIndexTrigger` calls `gcode index --sync-projections` for daemon-triggered indexing.
- Python maintenance flows call Rust-owned `gcode graph clear|rebuild` and `gcode vector clear|rebuild`, or stable JSON wrapper functions around those commands.
- After parity, retire Python `CodeGraph`, graph/vector projection code in `sync_worker.py`, and projection lifecycle methods in `CodeIndexContext`.
- Python shims must treat projection/report failures as explicit degraded states.
- The daemon embedding service is bypassed for code-index projection sync; Rust calls OpenAI-compatible embedding endpoints directly.
- LLM-generated symbol summaries remain daemon-side and optional.
- Memory services continue to own memory graph and `RELATES_TO_CODE` writes.
- UI/MCP/HTTP surfaces belong in the daemon repo and should call daemon services, not become `gcode` responsibilities.

**Acceptance:**

- 3.3.1 - Daemon integration notes identify direct Rust linking as the target. file: `docs/guides/gcode-graph-core.md`.
- 3.3.2 - Transitional Python shell-out behavior names `CodeIndexTrigger`, `sync_worker.py`, and `CodeIndexContext` migration points. file: `docs/guides/gcode-graph-core.md`.
- 3.3.3 - Ownership boundaries for PostgreSQL code facts, FalkorDB graph projection, Qdrant vector projection, memory graph, and bridge edges are explicit. file: `docs/guides/gcode-graph-core.md`.
- 3.3.4 - Symbol summaries are documented as daemon-side optional enrichment. file: `docs/guides/gcode-graph-core.md`.

## VS1: Verification
`kind: verification`

- `uv run gobby plans validate .gobby/plans/gcode-graph-enhancements.md`
- `cargo build --workspace --no-default-features`
- `cargo test -p gobby-code --no-default-features`
- `cargo clippy -p gobby-code --no-default-features -- -D warnings`
- `cargo test --workspace`
- `cargo clippy --workspace -- -D warnings`
- Phase 7 contract tests in the Gobby repo pass against the updated `gcode` binary.
- FalkorDB integration tests are gated by `FALKORDB_HOST` and skip with a clear message when unavailable.
- Mock embedding endpoint tests cover code-symbol embedding request and response handling.
- Qdrant REST tests cover ensure collection, delete-by-file, upsert, clear, and rebuild.
- Standalone smoke tests run with the daemon stopped against PostgreSQL, FalkorDB, Qdrant, and a mock embedding endpoint.
- `docs/guides/gcode-graph-core.md` documents the daemon migration contract: future Rust daemon links library APIs directly, transitional Python shims shell out to stable `gcode` JSON commands, and projection/report failures are explicit degraded states. The actual Python shim migration in the Gobby repo (consumer-side `CodeIndexTrigger` / `sync_worker.py` / `CodeIndexContext` rewrites plus corresponding transition tests) is deferred to the Gobby-repo task referenced from `DF1` and is not in scope for this plan's verification.
- Regression tests prove symbol summaries remain optional and do not block projection sync.
- JSON compatibility tests prove current consumers can parse outputs with optional projection metadata.

## AC1: Acceptance Criteria
`kind: verification`

- `gobby-code` library APIs own PostgreSQL code facts, graph/vector projection sync, lifecycle, setup integration, and report generation.
- Shared foundation concerns route through `gobby-core`, not copied `gcode` utilities.
- `gcode` graph and vector commands are CLI wrappers over library APIs.
- `gcode index --sync-projections` is available for daemon-triggered indexing.
- Future Rust daemon can link the same code directly.
- Python daemon shell-outs, if used, are explicitly transitional and expose stable JSON output.
- Standalone mode has explicit setup and does not depend on inherited Gobby-owned migrations.
- Attached mode remains non-destructive to Gobby-owned schema and files.
- Code graph facts and memory graph facts keep separate ownership.
- Qdrant code-symbol collections keep existing `code_symbols_<project_id>` names.
- Rust code-symbol embedding uses OpenAI-compatible embedding endpoints directly.
- LLM-generated symbol summaries remain daemon-owned optional enrichment.
- Provenance/confidence metadata lets agents distinguish extracted code facts from inferred bridge/memory links.
- Projection/report degraded behavior is explicit and never masquerades as successful empty data.
- Existing JSON consumers remain compatible.

## DF1: Deferred Gobby-Repo Python Daemon Shim Transition
`kind: deferred`

The actual Python shim migration in the Gobby repo — rewriting `CodeIndexTrigger`, `gobby/services/code_index/sync_worker.py`, and `gobby/services/code_index/context.py` (`CodeIndexContext`) to shell out to `gcode index --sync-projections`, `gcode graph clear|rebuild`, and `gcode vector clear|rebuild`; removing Python-side `CodeGraph`, graph/vector projection code paths, and projection lifecycle methods; and adding Gobby-repo transition tests proving the shims invoke `gcode` and stop instantiating Python projection code — is out of scope for this `gobby-cli` epic. This plan owns the `gcode` JSON contract (defined in §2.6) and gcode-side migration documentation (defined in §3.3) only.

```yaml
task_ref: "#15147"
reason: "Python shim consumer work (CodeIndexTrigger / sync_worker.py / CodeIndexContext rewrites plus Gobby-repo transition tests) lives in the Gobby repository, not in gobby-cli. This plan's gcode-side scope is the stable JSON contract documented in §2.6 and the migration documentation in §3.3; actually rewriting Python consumers and the corresponding transition tests must happen in the Gobby repo against the gcode binary this plan produces."
owner: "gobby-daemon-team"
original_acceptance_items:
  - item_id: DF1.1
    prose: "Update Python CodeIndexTrigger to shell out to gcode index --sync-projections and treat projection failures as explicit degraded states."
    artifact_kind: file
    artifact_ref: "gobby/services/code_index/trigger.py"
  - item_id: DF1.2
    prose: "Remove Python-side CodeGraph and graph/vector projection code from sync_worker.py; maintenance flows call gcode graph clear|rebuild and gcode vector clear|rebuild instead."
    artifact_kind: file
    artifact_ref: "gobby/services/code_index/sync_worker.py"
  - item_id: DF1.3
    prose: "Remove projection lifecycle methods from CodeIndexContext and route them through stable gcode JSON commands."
    artifact_kind: file
    artifact_ref: "gobby/services/code_index/context.py"
  - item_id: DF1.4
    prose: "Add Gobby-repo transition tests proving Python shims shell out to gcode and do not instantiate Python graph/vector projection code."
    artifact_kind: test
    artifact_ref: "gobby/tests/code_index/test_gcode_shim_transition.py"
```

Provenance label (must be applied to `#15147`): `deferred-from:gcode-graph-enhancements:DF1`.

## V1 Plan Changelog
`kind: verification`

- **R1-R12 (2026-05-24)**: Earlier iterations specified direct `gcode` ownership of graph writes/reads, route-shaped CLI commands, provenance metadata, graph lifecycle cleanup, report output, and Phase 7 compatibility constraints.
- **R13 (2026-05-26)**: Reframed the plan around reusable Rust core/library boundaries with `gcode` as CLI wrapper; made future Rust daemon direct linking the target; limited Python daemon shell-outs to transitional shims; added explicit standalone setup and minimal app-schema creation; preserved provenance/confidence, code-vs-memory ownership, graph report, and degraded behavior concepts; removed stale daemon-backed CLI and inherited-migration framing.
- **R14 (2026-05-26)**: Added dependency on `gobby-core` foundation plan; clarified that `gobby-code` owns code-specific graph APIs while shared context/config, setup, datastore, search/index primitives, and degradation contracts route through `gobby-core`.
- **R15 (2026-05-28)**: Reframed graph work as gcode-owned code projections: PostgreSQL code facts, FalkorDB `gobby_code`, and Qdrant `code_symbols_<project_id>`. Moved code-symbol embedding generation into Rust through OpenAI-compatible endpoints, added vector lifecycle commands, added `gcode index --sync-projections`, and made Python daemon projection code transitional. Left LLM-generated symbol summaries daemon-side.
- **R16 (2026-05-28)**: Normalized framing/verification headings to contract grammar (`O1`, `D1`, `A1`, `N1`, `VS1`, `AC1`, `V1`); added explicit `**Plan ID:** gcode-graph-enhancements` header; added `D1: Dependent Plans` mirroring the foundation plan; promoted `## Task Plan` to `## M1 Task Manifest` with `kind: manifest`; rewrote coverage labels to `covers:gcode-graph-enhancements:<section>:<item>` so the expansion contract resolves plan identity instead of `unknown`.
- **R17 (2026-05-28)**: Addressed Round 16 blocking findings. F1: added `gcode setup --standalone` CLI wiring to §1.2 with `commands/setup.rs` + `main.rs` targets and acceptance items 1.2.5/1.2.6 proving clap parsing and end-to-end command execution. F2: added new §1.4 deliverable for the reusable code-fact indexing library API (`index::api::index_files`/`IndexRequest`/`IndexOutcome`) decomposing PostgreSQL fact writes out of CLI modules, and threaded the dependency through §2.6. F3: added §2.6 JSON shape contract for `gcode index --sync-projections --format json` with acceptance items 2.6.5/2.6.6 covering JSON and text-mode output. Sweeps: added `vector/code_symbols.rs` to §2.1 targets (provenance applies to vector payloads), added `tests/projection_standalone.rs` and `output.rs` to §2.6 targets. Updated M1 manifest to include the §1.4 entry, new §2.6 dependency on §1.4, and expanded covers labels for §1.2/§2.6.
- **R18 (2026-05-28)**: Addressed Round 17 blocking findings on shared-file sequencing. F1 (§2.1 ↔ §2.5 sharing `crates/gcode/src/vector/code_symbols.rs`): added `2.1` to the §2.5 heading and M1 manifest `depends_on`, so the vector projection implementation waits for the provenance/source-system metadata contract that the vector payload path must carry. F2 (CLI/DB shared-file edits): added `1.4` to the §2.4 heading and M1 manifest `depends_on` (both touch `crates/gcode/src/db.rs`; §1.4 owns the reusable DB/helper boundary used by later projection sync work), and added `2.6` to the §3.2 heading and M1 manifest `depends_on` so the report CLI leaf runs after the graph/projection lifecycle CLI rewrites it shares `crates/gcode/src/main.rs` and `crates/gcode/src/commands/graph.rs` with. F2 sweep (whole-plan): re-checked every shared-file pair against the new dependency graph — `main.rs` chain is §1.1 → {§1.2, §1.4} → §2.4 → §2.6 → §3.2 (§1.2 vs §2.4 remain parallel siblings adding independent clap subcommand variants under §1.1's CLI structure; this matches the adversary's explicit scoping of the finding to runtime CLI rewrites §2.4/§2.6/§3.2 and is not flagged); `commands/graph.rs` chain is §1.1 → §2.3 → §2.4 → §3.2 (after F2 fix); `commands/vector.rs` chain is §1.1 → §2.5 → §2.6; `commands/index.rs` chain is §1.4 → §2.6; `db.rs` chain is §1.4 → §2.4 → §2.6 (after F2 fix); `vector/code_symbols.rs` chain is §2.1 → §2.5 (after F1 fix); `graph/code_graph.rs` chain is §2.1 → §2.2 → §2.3; `models.rs` chain is §2.1 → §2.2; `graph/report.rs` chain is §2.1 → §3.1; `falkor.rs` chain is §1.1 → §1.3; `search/semantic.rs` chain is §1.1 → §2.5. No section bodies, acceptance items, or coverage labels changed.
- **R19 (2026-05-28)**: Addressed Round 18 blocking findings. F1 (missing gobby-core consumer migration deliverable): added new §1.5 "Wire gcode to the gobby-core foundation" with targets `crates/gcode/Cargo.toml`, `crates/gcode/src/lib.rs`, `crates/gcode/src/config.rs`, `crates/gcode/src/db.rs`, `crates/gcode/src/falkor.rs`, `crates/gcode/src/search/semantic.rs`. Acceptance items 1.5.1–1.5.7 require Cargo.toml to enable `postgres`/`falkor`/`qdrant`/`search`/`indexing` (or `full`) features on gobby-core, both default and `--no-default-features` builds to succeed, config resolution to delegate to `gobby_core::config::resolve_*_config` / `CoreContext`, PostgreSQL plumbing to delegate to `gobby_core::postgres`, the Phase 7 `falkor.rs` facade to route internals through `gobby_core::falkor::with_graph` / `GraphClient`, the soft semantic-search path in `search/semantic.rs` to use `gobby_core::qdrant::with_qdrant` / `collection_name` / `search`, and a `lib::tests::foundation_consumer_migration` regression test to assert the migration. Threaded §1.5 as a dependency through §1.3 (shares `falkor.rs`), §1.4 (shares `db.rs` and `lib.rs`), and §2.5 (shares `search/semantic.rs` and `config.rs`). F2 (Qdrant lifecycle gap in gobby-core foundation surface): narrowed A1 with a "Vector projection lifecycle exception" bullet that allows code-specific Qdrant lifecycle HTTP (ensure collection, delete-by-filter, clear, rebuild) inside `crates/gcode/src/vector/code_symbols.rs` only, while requiring gobby-core for config (`resolve_qdrant_config`), ServiceState (`with_qdrant`), collection naming (`collection_name(.., CollectionScope::Custom(..))`), and non-lifecycle `search`/`upsert`. Added §2.5 acceptance items 2.5.6 (lifecycle HTTP scoped to `vector::code_symbols`) and 2.5.7 (routing through gobby-core for config/ServiceState/naming/search/upsert), and expanded §2.5 body with an explicit "Foundation boundary for vector lifecycle" subsection. Whole-plan sweeps: F1 sweep — re-verified every gobby-core consumer surface in framing has a deliverable owner; all FalkorDB/Qdrant/PostgreSQL plumbing anchors to §1.5, transitively reached by §1.3 (falkor.rs facade), §1.4 (db.rs helpers), §2.2/§2.3 (graph through `gobby_core::falkor::with_graph` via §1.3 → §1.5), §2.5 (vector through §1.5), and §2.4/§2.6 (CLI through §1.4 → §1.5). F2 sweep — re-verified every datastore adapter usage against the narrowed exception: §2.2/§2.3 graph ops use `gobby_core::falkor::with_graph` only; §2.6 lifecycle reuses §2.5/§2.4 lifecycle APIs and does not introduce new raw Qdrant HTTP outside `vector::code_symbols`; §3.1/§3.2 report paths do no Qdrant calls. Shared-file sequencing sweep (after §1.5): `Cargo.toml` chain is §1.1 → §1.5; `config.rs` chain is §1.5 → §2.5; `db.rs` chain is §1.5 → §1.4 → §2.4 → §2.6; `falkor.rs` chain is §1.1 → §1.5 → §1.3; `search/semantic.rs` chain is §1.1 → §1.5 → §2.5; `lib.rs` chain is §1.1 → §1.5 → §1.4 (both §1.4 and §1.5 add re-exports; §1.4 now depends on §1.5). M1 manifest updated: new §1.5 entry, refreshed §1.3/§1.4/§2.5 depends_on lists and validation criteria, and 2.5.6/2.5.7 covers labels appended.
- **R21 (2026-05-28)**: Addressed Round 20 blocking findings. F1 (bad-sequencing, §2.5 vs §1.5 and gobby-core foundation): chose the consumer-owned wrapper option from the adversary's suggested fix — vector dimension is now owned by a `gobby-code`-side sibling config type (`CodeVectorSettings { vector_dim: Option<usize> }` in `crates/gcode/src/config.rs`) rather than added to `gobby_core::config::EmbeddingConfig`. Updated §1.5 body to spell out that retained `EmbeddingConfig` references stay thin re-exports of the gobby-core type and that code-specific projection settings (such as `vector_dim`) live on sibling consumer-owned types resolved through the same §1.5 `ConfigSource` adapter pipeline. Updated §2.5 "Vector parameter handling" subsection to reference the consumer-owned setting and the `env → config_store JSON-decoded → defaults` resolution order. Updated acceptance 2.5.8 to reference `CodeVectorSettings.vector_dim` (not `EmbeddingConfig.vector_dim`) and added a second covering test `crates/gcode/src/config.rs::tests::vector_dim_setting_resolves_env_and_config_store`. No new deliverable was needed because the consumer-owned setting fits inside the existing §2.5 and §1.5 target inventories (`crates/gcode/src/config.rs` already targeted by both). F2 (weak-testability, §2.1 and §2.5): added provenance fields explicitly to the §2.5 vector payload list (`provenance = "EXTRACTED"`, `confidence = 1.0`, `source_system = "gcode"`, plus source-detail fields covering file path, source range, and symbol ID) and added new acceptance item 2.5.11 with covering test `crates/gcode/src/vector/code_symbols.rs::tests::payloads_carry_provenance_metadata` so the manifest covers labels and validation criteria pin the provenance contract on vector payloads. F3 (traceability, VS1 / §3.3): added new top-level `DF1: Deferred Gobby-Repo Python Daemon Shim Transition` section with typed `deferral` object pointing at open Gobby-repo task `#15147` (`Update daemon graph sync handoff after gcode sync-file contract`); narrowed VS1 to remove the Gobby-repo transition-test bullet that this `gobby-cli` epic cannot satisfy and replaced it with a documentation-scoped bullet plus an explicit pointer to DF1. §3.3 remains the docs-only deliverable that owns the migration contract narrative inside this plan. Whole-plan sweeps: F1 sweep — re-verified that no other deliverable claims `EmbeddingConfig.vector_dim` or adds new fields to gobby-core config types from gobby-code; all code-specific projection settings continue to live in `crates/gcode/src/config.rs` sibling types and resolve through the §1.5 adapter. F2 sweep — re-verified every projection payload writer pins provenance: graph edges already covered by 2.1.2 (`code_edges_carry_provenance`), bridge edges by 2.1.3 (`bridge_edges_are_hypotheses`), and now vector payloads by 2.5.11; no other projection producer is missing a provenance acceptance. F3 sweep — re-verified every VS1 bullet against deliverable coverage; remaining bullets all map to in-scope deliverables (foundation build under `--no-default-features` via §1.5, FalkorDB integration gating via §1.3/§2.2/§2.3, mock embedding tests via §2.5, Qdrant REST tests via §2.5/§2.6, standalone smoke tests via §2.4/§2.6, optional summaries via §2.5.5, JSON compatibility via §2.6/§3.2). M1 Task Manifest updated: §2.5 covers labels expanded to include `2.5.11` and validation_criteria expanded to invoke `vector::code_symbols::tests::payloads_carry_provenance_metadata` and `config::tests::vector_dim_setting_resolves_env_and_config_store`. Plan changelog R21 entry appended.
- **R20 (2026-05-28)**: Addressed Round 19 blocking findings. F1 (missing consumer `ConfigSource` adapter contract, O1/A1/D1/AC1 vs §1.5 and §2.5): added `crates/gcode/src/secrets.rs` to §1.5 targets; added a "Consumer adapter contract" subsection to §1.5 body specifying that `crates/gcode/src/config.rs` defines a PostgreSQL-backed `ConfigSource` implementation that wraps `&mut postgres::Client`, reads via `gobby_core::postgres::read_config_value`, decodes via `gobby_core::config::decode_config_value`, and resolves `$secret:NAME` / `${VAR}` patterns via `crate::secrets::resolve_config_value`; documented `EnvOnlySource` as the no-database baseline, and explicitly pinned the four-step pipeline `env → config_store (JSON-decoded) → $secret:/${VAR} interpolation → defaults`. Added three new acceptance items: 1.5.8 (adapter exists and uses the gobby-core decode pipeline plus `crate::secrets`), 1.5.9 (env precedence and JSON decode pipeline behave correctly for FalkorDB host/port/password, Qdrant URL/API key, embedding URL/model/API key with covering `crates/gcode/src/config.rs::tests::adapter_env_precedence_and_json_decode`), 1.5.10 (`$secret:` resolution still resolves FalkorDB password, Qdrant API key, and embedding API key in attached mode with `crates/gcode/src/config.rs::tests::adapter_resolves_config_store_secrets`). Added a behavioral guarantee stating attached mode resolves service settings from `config_store` plus `$secret:` resolution, not env-only paths. F2 (vector parameter handling for ensure/rebuild lifecycle, §2.5): added a "Vector parameter handling for ensure/rebuild lifecycle" subsection to §2.5 body specifying distance is fixed `Cosine`, vector size source order is explicit `EmbeddingConfig.vector_dim` then one-time per-command probe of the configured embedding endpoint, ensure-collection semantics for missing/compatible/incompatible existing collections, the typed `VectorLifecycleError::DimensionMismatch` (no migration, drop, or recreation), and that soft search reports missing-collection / dimension-mismatch via the shared degradation vocabulary. Added three new acceptance items: 2.5.8 (vector size resolution from explicit config or one-time probe with `Cosine` distance covering `vector::code_symbols::tests::ensure_collection_resolves_vector_size_and_distance`), 2.5.9 (missing-collection PUT/`Cosine` creation and compatible-existing no-op via `tests/vector_projection.rs::ensure_creates_missing_and_reuses_compatible`), 2.5.10 (incompatible-existing collection fails with `DimensionMismatch` and no destructive HTTP via `tests/vector_projection.rs::incompatible_existing_collection_errors_without_migration`). Whole-plan sweeps: F1 sweep — re-verified every gobby-core consumer surface that reads `config_store` values routes through the §1.5 `ConfigSource` adapter; the only attached-mode resolvers are `resolve_falkordb_config` / `resolve_qdrant_config` / `resolve_embedding_config` in §1.5, all consumed by §2.5 (vector lifecycle), §1.3 (Falkor facade), §2.2/§2.3 (graph reads/writes), §2.4 (graph CLI), and §2.6 (projection lifecycle CLI) through §1.5; no other section issues raw `read_config_value`/`decode_config_value`/`resolve_config_value` calls outside the adapter. F2 sweep — re-verified every vector lifecycle path uses the new vector-parameter handling: §2.5's `ensure_collection` is called from `sync-file`, `rebuild`, and the §2.6 `gcode index --sync-projections` projection-sync path; `clear` reuses the same compatibility check before issuing destructive HTTP; soft-search in `search/semantic.rs` does not call `ensure_collection` and surfaces dimension-mismatch via degradation, matching A1's lifecycle exception scope. M1 manifest updated: §1.5 covers labels expanded to 1.5.8/1.5.9/1.5.10 with refreshed validation_criteria pointing at the new adapter tests; §2.5 covers labels expanded to 2.5.8/2.5.9/2.5.10 with refreshed validation_criteria pointing at both unit and integration tests for vector parameter handling.
- **R22 (2026-05-28)**: Addressed Round 21 blocking findings. F1 (Phase 7 compatibility boundary, VS1 / §1.1 and §1.5): chose the compatibility-wrapper option — `crates/gcode/src/config.rs` keeps a local `FalkorConfig { host, port, password, graph_name: String }` (not a pure re-export of `gobby_core::config::FalkorConfig`, which has no `graph_name`) and `crates/gcode/src/falkor.rs` keeps a local `FalkorClient { graph: SyncGraph }` with `from_config(&FalkorConfig)` and free `with_falkor(ctx, ...)` so the external Phase 7 source-inspection contract resolves; wrapper internals delegate to `gobby_core::falkor::with_graph` / `gobby_core::falkor::GraphClient::from_config(&core_config, &config.graph_name)` so behavior still routes through gobby-core. Added a "Phase 7 compatibility wrapper" subsection to §1.5 body documenting the exact local symbols, field shapes, and `falkordb::{FalkorClientBuilder, FalkorConnectionInfo, SyncGraph}` import chain that must remain in `gobby-code` source. Reworked acceptance 1.5.3 to say `QdrantConfig`/`EmbeddingConfig` are thin re-exports while `FalkorConfig` is a wrapper; reworked 1.5.5 to flag `falkor.rs` as an explicit compatibility wrapper. Added new acceptance items 1.5.11 (`config::tests::falkor_config_wrapper_shape` covering the local `FalkorConfig` field shape) and 1.5.12 (`falkor::tests::falkor_client_wrapper_shape` covering the local `FalkorClient`/`with_falkor` symbols and the gobby-core delegation). F2 (manifest validation criteria, multiple sections): rewrote every multi-filter `cargo test` command into `&&`-chained single-filter invocations (Cargo only accepts one `[TESTNAME]` filter per command), and replaced every `main::tests::*` filter with the actual binary-crate filter path `tests::*` (verified via `cargo test -p gobby-code --no-default-features tests::test_parse_graph_clear -- --list`, which resolves to `tests::test_parse_graph_clear: test` from `src/main.rs`). Affected entries: §1.2, §1.4, §1.5, §2.4, §2.5, §2.6, and §3.2. F3 (commands/mod.rs shared-file ownership, §2.6 vs §1.2): added `crates/gcode/src/commands/mod.rs` to §2.6 targets, added `1.2` to the §2.6 heading and M1 manifest `depends_on`, and added acceptance item 2.6.7 requiring `pub mod vector;` to be exported from `commands/mod.rs` after the §1.2 `pub mod setup;` edit lands. Whole-plan sweeps: F1 sweep — re-verified no other deliverable claims `FalkorConfig`/`FalkorClient`/`with_falkor` are pure re-exports of `gobby_core` types; §1.1's compatibility-facade clause for `falkor.rs` and §1.5's wrapper subsection are the only owners of the wrapper shape; no other gcode source file is required by the Phase 7 test. F2 sweep — re-checked every M1 manifest `validation_criteria` string against `cargo test`'s single-filter rule; the remaining entries (§1.1, §1.3, §2.1, §2.2, §2.3, §3.1, §3.3) already use single-filter or non-test commands and were left unchanged. F3 sweep — re-checked shared mod.rs export edits across the plan: `crates/gcode/src/commands/mod.rs` is the only existing mod.rs edited by multiple deliverables (§1.2 adds `pub mod setup;`, §2.6 adds `pub mod vector;`); new directories (`vector/`, `graph/`, `projection/`) each have a single deliverable owner that creates the directory's `mod.rs` alongside its module files, so no further sequencing is needed. `mcp__gobby-plans__validate_plan` reports valid=true.
- **R23 (2026-05-28)**: Addressed Round 22 blocking findings. F1 (Phase 7 source-inspection surface, VS1 / §1.5 and §2.3): expanded the §1.5 "Phase 7 compatibility wrapper" subsection to enumerate the eight public read helpers (`count_callers`, `count_usages`, `find_callers`, `find_usages`, `find_callers_batch`, `find_callees_batch`, `get_imports`, `blast_radius`) and their sibling Cypher-builder helpers (`count_callers_query`, `count_usages_query`, `find_callers_query`, `find_usages_query`, `find_callers_batch_query`, `find_callees_batch_query`, `get_imports_query`, `blast_radius_query`) that must remain in `crates/gcode/src/falkor.rs`, plus the literal source fragments the external test asserts (`urlencoding::encode(password)`, `falkor://:{}@{}:{}`, `.with_connection_info(conn_info)`, `.with_params(&` for example `with_params(&params)`, `result.header`, `FalkorValue::None`). Added acceptance items 1.5.13 (`crates/gcode/src/falkor.rs::tests::phase7_read_helpers_visible` pins read-helper plus `*_query` visibility) and 1.5.14 (`crates/gcode/src/falkor.rs::tests::phase7_source_fragments_visible` pins source-fragment visibility). Added `crates/gcode/src/falkor.rs` to §2.3 targets, added a paragraph to §2.3 body specifying that the public `falkor.rs` read helpers delegate their internal Falkor query work to the new `graph::code_graph` read APIs after §2.3 lands while keeping public signatures, `*_query` siblings, clamping behavior, and Phase 7 source fragments unchanged, and added acceptance 2.3.4 (`crates/gcode/src/falkor.rs::tests::read_helpers_delegate_to_code_graph`). F2 (existing top-level read command compatibility, AC1 / §2.4): added a paragraph to §2.4 body requiring existing top-level `gcode callers|usages|imports|blast-radius` commands to remain available as additive (not replacement) thin wrappers over `graph::code_graph` reads, preserving clap argument names, pagination behavior (`--limit`, `--offset`), `--depth` semantics, JSON field names, payload structure, and pagination metadata; new optional metadata fields per §2.1 are tagged with `#[serde(skip_serializing_if = "Option::is_none")]`. Added acceptance items 2.4.5 (existing parse tests `test_parse_callers_remains_top_level`, `test_parse_usages_remains_top_level`, `test_parse_imports_remains_top_level`, `test_parse_blast_radius_remains_top_level` stay green) and 2.4.6 (`crates/gcode/src/commands/graph.rs::tests::top_level_read_commands_preserve_json_shape` pins JSON shape compatibility). Whole-plan sweeps: F1 sweep — re-confirmed `crates/gcode/src/falkor.rs` is the only `gobby-code` source file the Phase 7 test source-inspects beyond `config.rs` (handled in R22); the read helpers, `*_query` siblings, and connection/query source fragments are now pinned in §1.5 and the §2.3 delegation is the only other plan-side touch point. F2 sweep — re-verified no other top-level CLI surface is at risk in this plan: `gcode index`, `gcode status`, `gcode invalidate`, `gcode search*`, `gcode outline`, `gcode symbol(s)`, `gcode kinds`, `gcode tree`, `gcode repo-outline`, `gcode init`, `gcode projects`, `gcode prune` are either unchanged or explicitly covered (the `gcode graph clear|rebuild` parse tests already exist as sub-commands, and graph/vector sync-file/clear/rebuild remain owned by §2.4/§2.6). M1 Task Manifest updated: §1.5 entry adds covers labels 1.5.13/1.5.14 and chains two new `&&` single-filter `cargo test` invocations; §2.3 entry adds covers label 2.3.4 and a chained single-filter test invocation; §2.4 entry adds covers labels 2.4.5/2.4.6 and chains the four existing parse-test filters plus the new JSON-shape test filter as separate `cargo test` invocations. Manifest still emits one leaf per deliverable; deliverable_count=14.
- **R25 (2026-05-28)**: Addressed all three Round 24 blocking findings. F1 (Phase 7 `Row` shape mismatch, VS1 / §1.5.15): the previous text required `pub type Row = HashMap<String, FalkorValue>`, but the external Phase 7 test source-inspects for the exact substring `pub type Row = HashMap<String, Value>` (with `Value` = `serde_json::Value`, which matches the current `crates/gcode/src/falkor.rs` shape — `use serde_json::{Map, Number, Value};` then `pub type Row = HashMap<String, Value>;`). Updated the §1.5 Phase 7 compatibility wrapper subsection prose and acceptance 1.5.15 to require `pub type Row = HashMap<String, Value>` where `Value` is `serde_json::Value` imported into scope so the unqualified token `Value` appears at the alias declaration site, kept `FalkorValue` for the internal `parse_falkor_result` / `falkor_value_to_json` conversion helper, and aligned the local `phase7_query_surface_visible` test with the external Phase 7 substring assertion. F2 (foundation `StandaloneSetup` contract direction, D1 / §1.2): rewrote §1.2's "Foundation contract requirement" subsection so `crates/gcode/src/setup.rs` implements `gobby_core::setup::StandaloneSetup` (defined in the foundation plan §1.4 as a trait with `namespace`, `owned_objects`, and `create` methods consuming a `SetupContext`) and declares gcode-owned `OwnedObject` entries whose `creator` closures own the literal gcode `CREATE TABLE`/`CREATE INDEX`/`CREATE EXTENSION` strings. gcode-owned DDL stays inside gcode creator callbacks; `gobby-core` is the contract owner (trait, `SetupContext`, `OwnedObject`, `SetupReport`, `SetupError`, `StoreKind`) but does not contain gcode domain DDL. Updated acceptance 1.2.8 to require a `GcodeStandaloneSetup`-like struct implementing the trait, an enumerated `owned_objects()` list with creator closures, namespace plus exclusion-list assertions (refusing Gobby-owned tables, `config_store`, `.gobby/project.json`), and execution of creator closures only through the foundation-supplied `SetupContext`. F3 (forbidden file in deliverable Targets, P1 / §1.2): removed `.gobby/project.json` from §1.2 `Targets` so the leaf is not routed to a file it is explicitly prohibited from modifying. `.gobby/project.json` remains in §1.2 prose, N1, A1, AC1, and acceptance 1.2.4/1.2.6/1.2.8 as a forbidden artifact the setup path must not touch. Whole-plan sweeps: F1 sweep — re-grepped the plan for any other `HashMap<String, FalkorValue>` / `pub type Row =` references; the only remaining `HashMap<String, FalkorValue>` mention is the §R24 changelog entry, which is a historical record of the previous (incorrect) shape and is intentionally left in place. The Phase 7 §2.3.4 cross-reference, §1.5.13/§1.5.14/§1.5.16 acceptance items, and `falkor.rs` source-fragment list reference IDs and other shapes only — no other section needed updating. F2 sweep — re-checked every deliverable for `setup`/`schema`/`DDL` plumbing references; §1.2 is the only deliverable that owns `setup.rs` and DDL execution, so the F2 fix is contained. Re-confirmed §1.5's `gobby-core` Cargo feature list (`postgres`, `falkor`, `qdrant`, `search`, `indexing` or `full`) already enables the `gobby_core::setup` module path because the foundation `setup.rs` is always available behind the `postgres` feature gate for the `pg` field; no Cargo feature change was needed for the F2 fix. F3 sweep — re-grepped every `Targets:` line for forbidden artifacts (`.gobby/project.json`, `config_store`); no other deliverable Targets list mentions either. M1 Task Manifest unchanged: deliverable_count=14, no covers labels changed, no validation_criteria changed (the existing chained `cargo test -p gobby-code --no-default-features setup::tests::standalone_setup_uses_gobby_core_contract` already covers the revised 1.2.8 contract; the existing chained `cargo test -p gobby-code --no-default-features falkor::tests::phase7_query_surface_visible` already covers the revised 1.5.15 contract). `mcp__gobby-plans__validate_plan` is expected to report valid=true.
- **R24 (2026-05-28)**: Addressed all three Round 23 blocking findings. F1 (Phase 7 source-inspection surface still incomplete, VS1 / §1.5 and §2.3): extended the §1.5 "Phase 7 compatibility wrapper" subsection to enumerate the remaining shapes the external Phase 7 test asserts but that R23 did not yet pin — `pub type Row = HashMap<String, FalkorValue>`, `pub fn query(&mut self, cypher: &str, params: Option<HashMap<String, String>>) -> anyhow::Result<Vec<Row>>` on `impl FalkorClient`, `fn parse_falkor_result(...)`, the source fragments `let mut client =` and `ctx.falkordb`, the production-read-query helpers `cypher_string_literal`/`id_list_literal`/`clamp_offset`, and the literal Cypher fragments `target:CodeSymbol OR target:UnresolvedCallee OR target:ExternalSymbol`, `SKIP {offset} LIMIT {limit}`, and `target.id IN [{ids}]`. Documented the unbound-parameter ban: generated Cypher strings produced by the public `*_query` helpers must not contain `$offset`, `$limit`, or `$ids`; pagination and ID-list values are substituted inline via `clamp_offset` / `cypher_string_literal` / `id_list_literal`. Added two new source fragments (`let mut client =`, `ctx.falkordb`) to acceptance 1.5.14. Added acceptance items 1.5.15 (`crates/gcode/src/falkor.rs::tests::phase7_query_surface_visible` pins `Row` / `query` / `parse_falkor_result` shape) and 1.5.16 (`crates/gcode/src/falkor.rs::tests::phase7_query_helpers_and_literal_fragments_visible` pins helper presence, literal Cypher fragments, and unbound-parameter ban). Extended the §2.3 delegation paragraph and acceptance 2.3.4 to cross-reference §1.5.15/§1.5.16 alongside the previously pinned §1.5.13/§1.5.14 so the delegated helpers continue to preserve every Phase 7 source-inspection assertion. F2 (early dispatch + foundation setup contract, P1 / §1.2): added an "Early-dispatch requirement" subsection to §1.2 body stating that `gcode setup --standalone` dispatches from `main.rs` in the early-dispatch block alongside `Init`, `Projects`, and `Prune` before `Context::resolve()` is called, since setup creates the prerequisites that context resolution would otherwise require. Added a "Foundation contract requirement" subsection requiring `crates/gcode/src/setup.rs` to perform standalone schema/DDL work through the shared `gobby_core::setup::StandaloneSetup` (or equivalent foundation contract) boundary rather than bespoke DDL plumbing, with the foundation contract owning all `CREATE TABLE`/`CREATE INDEX`/`CREATE EXTENSION` calls and rejecting any request that would touch Gobby-owned tables, `config_store`, or `.gobby/project.json`. Added acceptance items 1.2.7 (`crates/gcode/src/main.rs::tests::setup_runs_before_context_resolve`) and 1.2.8 (`crates/gcode/src/setup.rs::tests::standalone_setup_uses_gobby_core_contract`). F3 (manifest validation criteria sweep): updated the M1 manifest so every entry whose source section contains a `test:` acceptance item runs each declared test through `validation_criteria`. Specifically: §1.1 adds `cargo test -p gobby-code --no-default-features lib::tests::public_projection_api_is_cli_independent` (covers 1.1.3) and `cargo test -p gobby-code --no-default-features lib::tests::falkor_facade_is_available` (covers 1.1.4 local proxy; the external Phase 7 test remains a VS1 cross-repo gate referenced informationally on acceptance 1.1.4); §1.2 chains the new `setup_runs_before_context_resolve` and `standalone_setup_uses_gobby_core_contract` tests; §1.5 chains the new `phase7_query_surface_visible` and `phase7_query_helpers_and_literal_fragments_visible` tests; §2.1 chains `graph::report::tests::bridge_edges_are_hypotheses` (covers 2.1.3); §2.2 chains `graph::code_graph::tests::cleanup_orphans_is_project_scoped` (covers 2.2.3) and `models::tests::uuid5_python_parity` (covers 2.2.4); §2.3 chains `search::graph_boost::tests` (covers 2.3.2); §2.4 chains `cargo test -p gobby-code --no-default-features --test graph_standalone` (covers 2.4.4); §2.5 chains `vector::code_symbols::tests::collection_name_compatibility` (2.5.3), `commands::vector::tests::vector_lifecycle_requires_config` (2.5.4), and `vector::code_symbols::tests::summaries_are_optional_enrichment` (2.5.5); §2.6 chains `projection::sync::tests::sync_state_tracks_projection_success` (2.6.2), `commands::vector::tests::lifecycle_json_contract` (2.6.3), and `cargo test -p gobby-code --no-default-features --test projection_standalone` (2.6.4); §3.1 chains `graph::report::tests::bridge_edges_are_read_only` (3.1.3) and `graph::report::tests::report_degradation_contract` (3.1.4); §3.2 chains `commands::graph::tests::report_text_structured_output` (3.2.2) and `commands::graph::tests::report_requires_graph_service` (3.2.3). Service-gated integration tests (`--test graph_standalone`, `--test projection_standalone`, `--test vector_projection ...`) keep their env-gated skip behavior but are now invoked at leaf-validation time so the contract is exercised when the required services are present. Whole-plan sweeps: F1 sweep — re-confirmed `crates/gcode/src/falkor.rs` remains the only `gobby-code` source file the Phase 7 test source-inspects; §1.5 now pins every shape, fragment, helper, and unbound-parameter ban that the Gobby-repo test asserts, and §2.3.4 cross-references the full §1.5.13/§1.5.14/§1.5.15/§1.5.16 set so internal delegation must preserve all of them. F2 sweep — re-checked every command for early-dispatch sequencing: `Init`, `Projects`, `Prune`, and now `Setup` are the early-dispatch commands; all other commands (graph/vector lifecycle, index, search, status, etc.) correctly require `Context::resolve()`. F3 sweep — re-verified every M1 entry whose `source_section` contains a `test:` acceptance item: §1.1, §1.2, §1.3, §1.4, §1.5, §2.1, §2.2, §2.3, §2.4, §2.5, §2.6, §3.1, §3.2 now all have validation criteria that run every declared test. §3.3 is docs-only (no `test:` acceptance) and was left unchanged. Manifest covers labels expanded: §1.2 +2 (1.2.7/1.2.8), §1.5 +2 (1.5.15/1.5.16). Manifest still emits one leaf per deliverable; deliverable_count=14.
- **R26 (2026-05-28)**: Addressed both Round 25 blocking findings. F1 (weak-testability — `lib::tests::*` cargo filters match zero tests, M1 manifest §§1.1 and 1.5): tests defined under `#[cfg(test)] mod tests {}` in `crates/gcode/src/lib.rs` are filtered by cargo as `tests::<name>`, not `lib::tests::<name>` (there is no implicit `lib` segment in the test path because `lib.rs` is the crate root; the prior R24 change followed the same pattern that R22 already fixed for `main::tests::*` → `tests::*` in main.rs). Cargo exits success when a filter matches zero tests, so `lib::tests::*` filters silently passed without exercising the underlying lib tests. Rewrote the affected `validation_criteria` strings: §1.1 entry now invokes `cargo test -p gobby-code --no-default-features tests::public_projection_api_is_cli_independent && cargo test -p gobby-code --no-default-features tests::falkor_facade_is_available` (covers 1.1.3 and 1.1.4); §1.5 entry now invokes `cargo test -p gobby-code --no-default-features tests::foundation_consumer_migration` for the consumer-migration regression (covers 1.5.7). Acceptance-item text in §1.1 and §1.5 already uses `file::tests::name` documentation form (`crates/gcode/src/lib.rs::tests::*`) and is unchanged because the acceptance refs are file-rooted descriptors, not cargo filters. F2 (bad-sequencing — §1.2 and §2.4 share `crates/gcode/src/main.rs` with no dependency edge): §1.2 adds the top-level `setup` subcommand plus its early-dispatch handler in `main.rs` (before `Context::resolve()`), while §2.4 adds or rewires the graph subcommand registrations and dispatch arms in the same `Command` enum and `match` block. The previous depends_on (`1.4, 2.2, 2.3`) let expansion schedule the setup and graph leaves in parallel, risking file contention and one rewrite missing the other's match arms. Added `1.2` to the §2.4 heading dependency list (now `(depends: 1.2, 1.4, 2.2, 2.3)`) and to the M1 manifest §2.4 entry `depends_on` list so §2.4 cannot start before §1.2's CLI registration lands. Whole-plan sweeps: F1 sweep — re-grepped every M1 `validation_criteria` for `lib::tests::*` after the §1.1/§1.5 fixes; no other entry references the `lib::tests::` prefix; the remaining manifest entries either use file-rooted module filters (e.g., `commands::graph::tests::*`, `config::tests::*`, `falkor::tests::*`, `vector::code_symbols::tests::*`, `graph::report::tests::*`, `projection::sync::tests::*`, `models::tests::*`, `search::graph_boost::tests`, `setup::tests::*`, `schema::tests::*`, `commands::setup::tests::*`, `commands::vector::tests::*`, `commands::index::tests::*`, `graph::code_graph::tests::*`, `graph::typed_query::tests`, `index::indexer::tests::*`) which match the actual module path of the test, the `tests::*` form for main.rs binary tests that R22 already fixed, or `--test <name>` for integration tests under `crates/gcode/tests/`. F2 sweep — re-checked every deliverable that targets `crates/gcode/src/main.rs` against the dependency graph: §1.1 (foundation, no deps), §1.2 (depends: 1.1), §2.4 (now depends: 1.2, 1.4, 2.2, 2.3 after F2 fix), §2.6 (depends: 1.2, 1.4, 2.4, 2.5 — already sequences after §1.2), §3.2 (depends: 2.6, 3.1 — transitively after §1.2 and §2.4). The chain is now §1.1 → §1.2 → §2.4 → §2.6 → §3.2 with §1.4 a parallel sibling under §1.1 feeding §2.4 and §2.6, so every later leaf inherits the §1.2 edge transitively. No other shared-file pair on `main.rs` is missing a dependency edge. M1 Task Manifest changes: §1.1 entry `validation_criteria` rewritten (no covers-label change); §1.5 entry `validation_criteria` rewritten (no covers-label change); §2.4 entry `depends_on` adds `"1.2"` (no covers-label change). Manifest still emits one leaf per deliverable; deliverable_count=14.

## M1 Task Manifest
`kind: manifest`

```yaml
- title: Create gobby-code projection library boundary
  category: code
  task_type: feature
  depends_on: []
  validation_criteria: "cargo build -p gobby-code --no-default-features && cargo test -p gobby-code --no-default-features tests::public_projection_api_is_cli_independent && cargo test -p gobby-code --no-default-features tests::falkor_facade_is_available"
  labels:
    - covers:gcode-graph-enhancements:1.1:1.1.1
    - covers:gcode-graph-enhancements:1.1:1.1.2
    - covers:gcode-graph-enhancements:1.1:1.1.3
    - covers:gcode-graph-enhancements:1.1:1.1.4
  implementation_domain: backend
  tdd: true
  source_section: "1.1"
- title: Add explicit standalone setup
  category: code
  task_type: feature
  depends_on:
    - "1.1"
  validation_criteria: "cargo test -p gobby-code --no-default-features schema::tests::missing_schema_requires_setup && cargo test -p gobby-code --no-default-features setup::tests::standalone_setup_is_scoped && cargo test -p gobby-code --no-default-features commands::setup::tests::standalone_command_is_scoped && cargo test -p gobby-code --no-default-features tests::parse_setup_standalone && cargo test -p gobby-code --no-default-features tests::setup_runs_before_context_resolve && cargo test -p gobby-code --no-default-features setup::tests::standalone_setup_uses_gobby_core_contract"
  labels:
    - covers:gcode-graph-enhancements:1.2:1.2.1
    - covers:gcode-graph-enhancements:1.2:1.2.2
    - covers:gcode-graph-enhancements:1.2:1.2.3
    - covers:gcode-graph-enhancements:1.2:1.2.4
    - covers:gcode-graph-enhancements:1.2:1.2.5
    - covers:gcode-graph-enhancements:1.2:1.2.6
    - covers:gcode-graph-enhancements:1.2:1.2.7
    - covers:gcode-graph-enhancements:1.2:1.2.8
  implementation_domain: backend
  tdd: true
  source_section: "1.2"
- title: Add typed Falkor query boundary
  category: code
  task_type: feature
  depends_on:
    - "1.1"
    - "1.5"
  validation_criteria: "cargo test -p gobby-code --no-default-features graph::typed_query::tests"
  labels:
    - covers:gcode-graph-enhancements:1.3:1.3.1
    - covers:gcode-graph-enhancements:1.3:1.3.2
    - covers:gcode-graph-enhancements:1.3:1.3.3
  implementation_domain: backend
  tdd: true
  source_section: "1.3"
- title: Add reusable code-fact indexing library API
  category: code
  task_type: feature
  depends_on:
    - "1.1"
    - "1.5"
  validation_criteria: "cargo test -p gobby-code --no-default-features index::indexer::tests::library_api_is_cli_independent && cargo test -p gobby-code --no-default-features index::indexer::tests::library_writes_all_code_facts"
  labels:
    - covers:gcode-graph-enhancements:1.4:1.4.1
    - covers:gcode-graph-enhancements:1.4:1.4.2
    - covers:gcode-graph-enhancements:1.4:1.4.3
    - covers:gcode-graph-enhancements:1.4:1.4.4
  implementation_domain: backend
  tdd: true
  source_section: "1.4"
- title: Wire gcode to the gobby-core foundation
  category: code
  task_type: feature
  depends_on:
    - "1.1"
  validation_criteria: "cargo build -p gobby-code && cargo build -p gobby-code --no-default-features && cargo test -p gobby-code --no-default-features tests::foundation_consumer_migration && cargo test -p gobby-code --no-default-features config::tests::adapter_env_precedence_and_json_decode && cargo test -p gobby-code --no-default-features config::tests::adapter_resolves_config_store_secrets && cargo test -p gobby-code --no-default-features config::tests::falkor_config_wrapper_shape && cargo test -p gobby-code --no-default-features falkor::tests::falkor_client_wrapper_shape && cargo test -p gobby-code --no-default-features falkor::tests::phase7_read_helpers_visible && cargo test -p gobby-code --no-default-features falkor::tests::phase7_source_fragments_visible && cargo test -p gobby-code --no-default-features falkor::tests::phase7_query_surface_visible && cargo test -p gobby-code --no-default-features falkor::tests::phase7_query_helpers_and_literal_fragments_visible"
  labels:
    - covers:gcode-graph-enhancements:1.5:1.5.1
    - covers:gcode-graph-enhancements:1.5:1.5.2
    - covers:gcode-graph-enhancements:1.5:1.5.3
    - covers:gcode-graph-enhancements:1.5:1.5.4
    - covers:gcode-graph-enhancements:1.5:1.5.5
    - covers:gcode-graph-enhancements:1.5:1.5.6
    - covers:gcode-graph-enhancements:1.5:1.5.7
    - covers:gcode-graph-enhancements:1.5:1.5.8
    - covers:gcode-graph-enhancements:1.5:1.5.9
    - covers:gcode-graph-enhancements:1.5:1.5.10
    - covers:gcode-graph-enhancements:1.5:1.5.11
    - covers:gcode-graph-enhancements:1.5:1.5.12
    - covers:gcode-graph-enhancements:1.5:1.5.13
    - covers:gcode-graph-enhancements:1.5:1.5.14
    - covers:gcode-graph-enhancements:1.5:1.5.15
    - covers:gcode-graph-enhancements:1.5:1.5.16
  implementation_domain: backend
  tdd: true
  source_section: "1.5"
- title: Define projection provenance metadata
  category: code
  task_type: feature
  depends_on:
    - "1.1"
  validation_criteria: "cargo test -p gobby-code --no-default-features graph::code_graph::tests::code_edges_carry_provenance && cargo test -p gobby-code --no-default-features graph::report::tests::bridge_edges_are_hypotheses"
  labels:
    - covers:gcode-graph-enhancements:2.1:2.1.1
    - covers:gcode-graph-enhancements:2.1:2.1.2
    - covers:gcode-graph-enhancements:2.1:2.1.3
  implementation_domain: backend
  tdd: true
  source_section: "2.1"
- title: Port code graph writes to Rust core
  category: code
  task_type: feature
  depends_on:
    - "1.3"
    - "2.1"
  validation_criteria: "cargo test -p gobby-code --no-default-features graph::code_graph::tests::delete_preserves_current_symbols && cargo test -p gobby-code --no-default-features graph::code_graph::tests::cleanup_orphans_is_project_scoped && cargo test -p gobby-code --no-default-features models::tests::uuid5_python_parity"
  labels:
    - covers:gcode-graph-enhancements:2.2:2.2.1
    - covers:gcode-graph-enhancements:2.2:2.2.2
    - covers:gcode-graph-enhancements:2.2:2.2.3
    - covers:gcode-graph-enhancements:2.2:2.2.4
  implementation_domain: backend
  tdd: true
  source_section: "2.2"
- title: Port code graph reads to Rust core
  category: code
  task_type: feature
  depends_on:
    - "2.2"
  validation_criteria: "cargo test -p gobby-code --no-default-features commands::graph::tests::graph_reads_require_falkor && cargo test -p gobby-code --no-default-features falkor::tests::read_helpers_delegate_to_code_graph && cargo test -p gobby-code --no-default-features search::graph_boost::tests"
  labels:
    - covers:gcode-graph-enhancements:2.3:2.3.1
    - covers:gcode-graph-enhancements:2.3:2.3.2
    - covers:gcode-graph-enhancements:2.3:2.3.3
    - covers:gcode-graph-enhancements:2.3:2.3.4
  implementation_domain: backend
  tdd: true
  source_section: "2.3"
- title: Wrap graph core with gcode commands
  category: code
  task_type: feature
  depends_on:
    - "1.2"
    - "1.4"
    - "2.2"
    - "2.3"
  validation_criteria: "cargo test -p gobby-code --no-default-features tests::parse_graph_commands && cargo test -p gobby-code --no-default-features tests::test_parse_callers_remains_top_level && cargo test -p gobby-code --no-default-features tests::test_parse_usages_remains_top_level && cargo test -p gobby-code --no-default-features tests::test_parse_imports_remains_top_level && cargo test -p gobby-code --no-default-features tests::test_parse_blast_radius_remains_top_level && cargo test -p gobby-code --no-default-features commands::graph::tests::top_level_read_commands_preserve_json_shape && cargo test -p gobby-code --no-default-features --test graph_standalone"
  labels:
    - covers:gcode-graph-enhancements:2.4:2.4.1
    - covers:gcode-graph-enhancements:2.4:2.4.2
    - covers:gcode-graph-enhancements:2.4:2.4.3
    - covers:gcode-graph-enhancements:2.4:2.4.4
    - covers:gcode-graph-enhancements:2.4:2.4.5
    - covers:gcode-graph-enhancements:2.4:2.4.6
  implementation_domain: backend
  tdd: true
  source_section: "2.4"
- title: Port code-symbol vector projection to Rust core
  category: code
  task_type: feature
  depends_on:
    - "1.1"
    - "1.5"
    - "2.1"
  validation_criteria: "cargo test -p gobby-code --no-default-features vector::code_symbols::tests::embedding_request_response && cargo test -p gobby-code --no-default-features vector::code_symbols::tests::collection_name_compatibility && cargo test -p gobby-code --no-default-features commands::vector::tests::vector_lifecycle_requires_config && cargo test -p gobby-code --no-default-features vector::code_symbols::tests::summaries_are_optional_enrichment && cargo test -p gobby-code --no-default-features vector::code_symbols::tests::lifecycle_http_scoped_to_module && cargo test -p gobby-code --no-default-features vector::code_symbols::tests::routes_through_gobby_core_qdrant && cargo test -p gobby-code --no-default-features vector::code_symbols::tests::ensure_collection_resolves_vector_size_and_distance && cargo test -p gobby-code --no-default-features vector::code_symbols::tests::payloads_carry_provenance_metadata && cargo test -p gobby-code --no-default-features config::tests::vector_dim_setting_resolves_env_and_config_store && cargo test -p gobby-code --no-default-features --test vector_projection ensure_creates_missing_and_reuses_compatible && cargo test -p gobby-code --no-default-features --test vector_projection incompatible_existing_collection_errors_without_migration"
  labels:
    - covers:gcode-graph-enhancements:2.5:2.5.1
    - covers:gcode-graph-enhancements:2.5:2.5.2
    - covers:gcode-graph-enhancements:2.5:2.5.3
    - covers:gcode-graph-enhancements:2.5:2.5.4
    - covers:gcode-graph-enhancements:2.5:2.5.5
    - covers:gcode-graph-enhancements:2.5:2.5.6
    - covers:gcode-graph-enhancements:2.5:2.5.7
    - covers:gcode-graph-enhancements:2.5:2.5.8
    - covers:gcode-graph-enhancements:2.5:2.5.9
    - covers:gcode-graph-enhancements:2.5:2.5.10
    - covers:gcode-graph-enhancements:2.5:2.5.11
  implementation_domain: backend
  tdd: true
  source_section: "2.5"
- title: Add projection lifecycle orchestration commands
  category: code
  task_type: feature
  depends_on:
    - "1.2"
    - "1.4"
    - "2.4"
    - "2.5"
  validation_criteria: "cargo test -p gobby-code --no-default-features tests::parse_projection_lifecycle_commands && cargo test -p gobby-code --no-default-features projection::sync::tests::sync_state_tracks_projection_success && cargo test -p gobby-code --no-default-features commands::vector::tests::lifecycle_json_contract && cargo test -p gobby-code --no-default-features commands::index::tests::sync_projections_json_contract && cargo test -p gobby-code --no-default-features commands::index::tests::sync_projections_text_contract && cargo test -p gobby-code --no-default-features --test projection_standalone"
  labels:
    - covers:gcode-graph-enhancements:2.6:2.6.1
    - covers:gcode-graph-enhancements:2.6:2.6.2
    - covers:gcode-graph-enhancements:2.6:2.6.3
    - covers:gcode-graph-enhancements:2.6:2.6.4
    - covers:gcode-graph-enhancements:2.6:2.6.5
    - covers:gcode-graph-enhancements:2.6:2.6.6
    - covers:gcode-graph-enhancements:2.6:2.6.7
  implementation_domain: backend
  tdd: true
  source_section: "2.6"
- title: Generate project graph report in Rust core
  category: code
  task_type: feature
  depends_on:
    - "2.3"
  validation_criteria: "cargo test -p gobby-code --no-default-features graph::report::tests::report_shape && cargo test -p gobby-code --no-default-features graph::report::tests::bridge_edges_are_read_only && cargo test -p gobby-code --no-default-features graph::report::tests::report_degradation_contract"
  labels:
    - covers:gcode-graph-enhancements:3.1:3.1.1
    - covers:gcode-graph-enhancements:3.1:3.1.2
    - covers:gcode-graph-enhancements:3.1:3.1.3
    - covers:gcode-graph-enhancements:3.1:3.1.4
  implementation_domain: backend
  tdd: true
  source_section: "3.1"
- title: Add gcode graph report CLI wrapper
  category: code
  task_type: feature
  depends_on:
    - "2.6"
    - "3.1"
  validation_criteria: "cargo test -p gobby-code --no-default-features tests::parse_graph_report_global_format && cargo test -p gobby-code --no-default-features commands::graph::tests::report_text_structured_output && cargo test -p gobby-code --no-default-features commands::graph::tests::report_requires_graph_service"
  labels:
    - covers:gcode-graph-enhancements:3.2:3.2.1
    - covers:gcode-graph-enhancements:3.2:3.2.2
    - covers:gcode-graph-enhancements:3.2:3.2.3
    - covers:gcode-graph-enhancements:3.2:3.2.4
  implementation_domain: backend
  tdd: true
  source_section: "3.2"
- title: Document daemon migration contracts
  category: docs
  task_type: documentation
  depends_on:
    - "2.6"
    - "3.2"
  validation_criteria: "docs/guides/gcode-graph-core.md exists and documents direct Rust linking target, transitional Python shell-out shims, code/memory ownership boundaries, and daemon-side optional symbol summaries"
  labels:
    - covers:gcode-graph-enhancements:3.3:3.3.1
    - covers:gcode-graph-enhancements:3.3:3.3.2
    - covers:gcode-graph-enhancements:3.3:3.3.3
    - covers:gcode-graph-enhancements:3.3:3.3.4
  implementation_domain: backend
  tdd: false
  source_section: "3.3"
```
