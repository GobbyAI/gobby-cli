# gobby-core Rust foundation

**Plan ID:** gcore-rust-foundation

## O1: Overview
`kind: framing`

`gobby-core` is the shared Rust migration substrate for Gobby CLI crates and the future Rust daemon. It should hold the boring, reusable platform layer: context and config resolution, attached versus standalone setup contracts, PostgreSQL/FalkorDB/Qdrant adapters, generic indexing/search primitives, and shared error/degradation types.

Domain behavior stays out of this crate. Code graph facts, symbol IDs, language parsing policy, and graph APIs stay in `gobby-code`. Wiki vault layout, llm-wiki UX, ingestion flows, and article synthesis stay in `gobby-wiki`. `gobby-core` exists so those crates stop copying infrastructure while keeping their domain boundaries sharp.

## C1: Constraints
`kind: framing`

- **Non-destructive attached mode**: attached Gobby projects validate externally managed schema and service availability. They do not create, alter, drop, or migrate Gobby-owned objects.
- **Explicit standalone mode**: standalone setup is an explicit opt-in operation. Runtime commands never perform implicit schema creation.
- **Resolution order**: service config resolves from environment variables, then `config_store`, then hardcoded defaults. Consumers must not short-circuit this order.
- **No domain ownership**: `gobby-core` must not know about code symbols, wiki documents, vault UX, task behavior, memories, or daemon workflow semantics.
- **Graceful absence**: FalkorDB and Qdrant are optional dependencies at runtime. Missing services surface typed degradation rather than panics or fake empty success.
- **Small public API**: APIs should expose stable structs, traits, and error enums, not CLI parser types or command-output formatting.

## D1: Dependent Plans
`kind: framing`

This plan is the foundation dependency for `.gobby/plans/gcode-graph-enhancements.md` and `.gobby/plans/gwiki.md`.

`gobby-code` may depend on the context/config, datastore adapter, search fusion, and indexing primitives from `gobby-core`, but it owns code-specific graph APIs and code-index semantics.

`gobby-wiki` may depend on the same primitives, but it owns vault semantics, wiki document models, namespaced storage, ingestion, research, compile, audit, and Obsidian-compatible output.

## P1: Context And Setup Contracts
`kind: framing`

**Goal**: define the shared Rust foundation boundary and the setup modes that every consumer crate can use without inheriting another domain's behavior.

### 1.1 Define the gobby-core public boundary [category: code]
`kind: deliverable`

Targets: `crates/gcore/src/lib.rs`, `docs/guides/gcore-development-guide.md`

Expand the current small `gobby-core` crate into a clearly documented foundation layer. The public module map should describe intended modules for:

- `context` - resolved project root, project id, bootstrap path, database URL, and service configs.
- `config` - env/config-store/default resolution helpers.
- `setup` - attached versus standalone setup contracts.
- `postgres` - PostgreSQL hub connections and config-store reads.
- `falkor` - FalkorDB client config, query execution, and escaping helpers.
- `qdrant` - Qdrant collection/config helpers and vector upsert/search contracts.
- `indexing` - generic walker, hash, chunk, and artifact traits.
- `search` - generic BM25/semantic/graph result contracts and RRF fusion.
- `degradation` - typed optional-service and partial-result states.

The boundary must stay dependency-light where possible and must not expose `gcode` command types, wiki vault structs, or daemon workflow types.

**Acceptance:**

- 1.1.1 - `crates/gcore/src/lib.rs` documents the foundation module map and domain boundary. file: `crates/gcore/src/lib.rs`.
- 1.1.2 - `docs/guides/gcore-development-guide.md` names `gobby-core` as shared substrate, not a code-graph or wiki domain crate. file: `docs/guides/gcore-development-guide.md`.
- 1.1.3 - Public APIs avoid `clap`, command-output, code-symbol, and wiki-vault types. test: `crates/gcore/src/lib.rs::tests::public_api_has_no_domain_types`.
- 1.1.4 - `gobby-core` remains buildable under CI's no-default-features profile. test: `cargo build -p gobby-core --no-default-features`.

### 1.2 Add shared context and config resolution [category: code] (depends: 1.1)
`kind: deliverable`

Targets: `crates/gcore/src/context.rs`, `crates/gcore/src/config.rs`, `crates/gcore/src/bootstrap.rs`, `crates/gcore/src/project.rs`

Create a shared context resolver that consumer crates can call before opening datastore clients. It should combine the existing project-root and bootstrap helpers with service config resolution:

- Resolve project root and project id from `.gobby/project.json` without writing that file.
- Resolve PostgreSQL DSN from environment or `bootstrap.yaml`.
- Resolve FalkorDB and Qdrant config from environment, then `config_store`, then defaults.
- Preserve explicit absence for optional services instead of manufacturing usable configs.
- Return a reusable context struct that is independent of any CLI command enum.

Config-store reads belong behind a PostgreSQL connection supplied by the caller or built from the resolved DSN. The helper may read `config_store`; it must not write it.

**Acceptance:**

- 1.2.1 - Context resolution returns project root, project id, database URL, and optional service configs. file: `crates/gcore/src/context.rs`.
- 1.2.2 - FalkorDB and Qdrant resolution preserves env-var precedence over `config_store` over defaults. test: `crates/gcore/src/config.rs::tests::env_overrides_config_store`.
- 1.2.3 - Missing optional service config is represented explicitly and does not panic. test: `crates/gcore/src/context.rs::tests::missing_optional_services_are_none`.
- 1.2.4 - Project identity is read-only and never writes `.gobby/project.json`. test: `crates/gcore/src/project.rs::tests::read_project_id_is_non_destructive`.

### 1.3 Define attached and standalone setup contracts [category: code] (depends: 1.2)
`kind: deliverable`

Targets: `crates/gcore/src/setup.rs`, `docs/guides/gcore-development-guide.md`

Add shared setup contracts that domain crates can implement without copying policy:

- `AttachedMode` validates externally managed Gobby resources and never creates or migrates them.
- `StandaloneMode` is an explicit setup operation that may create only consumer-owned resources in a selected database/schema/collection namespace.
- Runtime validation reports missing prerequisites with actionable setup guidance.
- Domain crates supply ownership rules, required objects, and creation callbacks for standalone mode.

`gobby-core` should provide the contract and guardrails. It should not hardcode `gcode_*`, `gwiki_*`, `Symbol`, `WikiDoc`, or any other domain-owned objects.

**Acceptance:**

- 1.3.1 - Attached-mode setup exposes read-only validation hooks. file: `crates/gcore/src/setup.rs`.
- 1.3.2 - Standalone setup requires explicit opt-in and consumer-owned object declarations. file: `crates/gcore/src/setup.rs`.
- 1.3.3 - Runtime validation returns a typed missing-prerequisite error with setup guidance. test: `crates/gcore/src/setup.rs::tests::runtime_validation_reports_setup_guidance`.
- 1.3.4 - Setup docs state that `gobby-core` does not create Gobby-owned schema in attached mode. file: `docs/guides/gcore-development-guide.md`.

## P2: Datastore Adapters
`kind: framing`

**Goal**: centralize client plumbing and safety contracts for PostgreSQL, FalkorDB, and Qdrant while leaving schemas, labels, and payload semantics to consumers.

### 2.1 Add PostgreSQL hub adapter [category: code] (depends: P1)
`kind: deliverable`

Targets: `crates/gcore/src/postgres.rs`, `crates/gcore/src/config.rs`, `crates/gcore/src/degradation.rs`

Provide shared PostgreSQL connection helpers and read-only config-store access:

- `connect_readonly` and `connect_readwrite` wrappers with consistent error context.
- A typed config-store reader that parses service config values without mutating rows.
- Schema validation helpers that accept consumer-supplied validators.
- No built-in migrations, `CREATE TABLE`, `ALTER TABLE`, or `DROP TABLE` behavior for attached mode.

Domain crates remain responsible for their own table names, indexes, and standalone creation callbacks.

**Acceptance:**

- 2.1.1 - Read-only and read-write connection helpers share consistent error context. file: `crates/gcore/src/postgres.rs`.
- 2.1.2 - `config_store` reads are available without write helpers. file: `crates/gcore/src/config.rs`.
- 2.1.3 - Attached schema validation helpers reject migration callbacks. test: `crates/gcore/src/postgres.rs::tests::attached_validation_is_non_destructive`.
- 2.1.4 - Domain table names are supplied by consumers, not embedded in `gobby-core`. test: `crates/gcore/src/postgres.rs::tests::schema_validator_is_domain_supplied`.

### 2.2 Add FalkorDB adapter and query safety boundary [category: code] (depends: P1)
`kind: deliverable`

Targets: `crates/gcore/src/falkor.rs`, `crates/gcore/src/degradation.rs`

Provide a shared FalkorDB adapter that handles connection config, request execution, parameter escaping, and unavailable-service degradation. It must make safe query construction easy without owning graph semantics.

The adapter may expose small typed helpers for escaped labels, relation names, property keys, and parameters. It must not define code graph APIs such as `CALLS`, `IMPORTS`, `DEFINES`, or wiki APIs such as `LINKS_TO`; those belong to consumer crates.

**Acceptance:**

- 2.2.1 - FalkorDB config and connection errors map to typed degradation states. file: `crates/gcore/src/falkor.rs`.
- 2.2.2 - Query escaping helpers cover labels, relation names, property keys, and string parameters. test: `crates/gcore/src/falkor.rs::tests::escapes_graph_tokens`.
- 2.2.3 - The adapter has no hardcoded code or wiki labels. test: `crates/gcore/src/falkor.rs::tests::no_domain_labels_in_adapter`.
- 2.2.4 - Consumers can distinguish unavailable graph service from a successful empty graph result. test: `crates/gcore/src/degradation.rs::tests::graph_unavailable_is_not_empty_success`.

### 2.3 Add Qdrant and embedding configuration adapter [category: code] (depends: P1)
`kind: deliverable`

Targets: `crates/gcore/src/qdrant.rs`, `crates/gcore/src/config.rs`, `crates/gcore/src/degradation.rs`

Provide shared Qdrant and embedding configuration primitives:

- Resolve Qdrant endpoint and embedding endpoint/API key with env/config-store/default precedence.
- Build collection names from consumer-supplied namespaces.
- Provide vector upsert/search request types that carry opaque payload maps.
- Represent missing embeddings or Qdrant as optional-service degradation.

`gobby-core` should not choose model names for domains, embed text itself unless the consumer passes a configured embedding client, or define code/wiki payload schemas.

**Acceptance:**

- 2.3.1 - Qdrant and embedding configs follow the shared resolution order. test: `crates/gcore/src/config.rs::tests::qdrant_and_embedding_resolution_order`.
- 2.3.2 - Collection names require a caller-supplied namespace prefix. file: `crates/gcore/src/qdrant.rs`.
- 2.3.3 - Vector upsert/search contracts accept domain payloads without knowing their schema. test: `crates/gcore/src/qdrant.rs::tests::payload_schema_is_opaque`.
- 2.3.4 - Missing embeddings or Qdrant surfaces typed degradation. test: `crates/gcore/src/degradation.rs::tests::vector_services_degrade_explicitly`.

## P3: Generic Indexing And Search Primitives
`kind: framing`

**Goal**: share mechanics that are genuinely generic while keeping parsing, graph extraction, and UX in domain crates.

### 3.1 Add generic indexing primitives [category: code] (depends: P2)
`kind: deliverable`

Targets: `crates/gcore/src/indexing.rs`, `crates/gcore/src/lib.rs`

Extract or define generic primitives for file discovery, content hashing, chunk identity, and index event flow:

- Filesystem walker settings and ignore rules that consumers can extend.
- SHA-256 content hashing.
- Chunk records with byte ranges, heading/context metadata, and opaque domain payload.
- Index events for added, changed, unchanged, deleted, and skipped artifacts.

Language parsing, markdown parsing, symbol extraction, wiki link extraction, and domain write models stay in `gobby-code` or `gobby-wiki`.

**Acceptance:**

- 3.1.1 - Generic walker settings support consumer extension without code/wiki-specific defaults. file: `crates/gcore/src/indexing.rs`.
- 3.1.2 - Hashing and chunk records are reusable with opaque domain metadata. test: `crates/gcore/src/indexing.rs::tests::chunk_metadata_is_opaque`.
- 3.1.3 - Index events distinguish unchanged, changed, deleted, and skipped artifacts. test: `crates/gcore/src/indexing.rs::tests::index_events_cover_incremental_cases`.
- 3.1.4 - `gobby-core` does not import tree-sitter language grammars. test: `crates/gcore/src/indexing.rs::tests::no_domain_parser_dependency`.

### 3.2 Add generic search fusion primitives [category: code] (depends: P2)
`kind: deliverable`

Targets: `crates/gcore/src/search.rs`, `crates/gcore/src/degradation.rs`

Provide reusable search result and fusion primitives:

- Common result identity, score, source, and explanation fields.
- RRF fusion over BM25, semantic, and graph-ranked result lists.
- Degradation metadata when one source is unavailable.
- Stable JSON-serializable structs that domain CLIs can wrap.

PostgreSQL query SQL, Qdrant payload filters, graph boost semantics, and user-facing output remain consumer-specific.

**Acceptance:**

- 3.2.1 - RRF fusion is available from `gobby_core::search`. file: `crates/gcore/src/search.rs`.
- 3.2.2 - Fusion preserves source explanations and unavailable-source degradation. test: `crates/gcore/src/search.rs::tests::rrf_preserves_explanations_and_degradation`.
- 3.2.3 - Result structs are serializable without CLI formatting types. test: `crates/gcore/src/search.rs::tests::search_result_is_cli_independent`.
- 3.2.4 - Domain-specific SQL, graph labels, and payload filters are absent from the shared search module. test: `crates/gcore/src/search.rs::tests::search_core_has_no_domain_queries`.

### 3.3 Add shared error and degradation contracts [category: code] (depends: 3.1, 3.2)
`kind: deliverable`

Targets: `crates/gcore/src/degradation.rs`, `docs/guides/gcore-development-guide.md`

Define shared error and degradation contracts used by datastore adapters, indexing, and search:

- Fatal errors for corrupted inputs, invalid config, unavailable required services, and write failures.
- Degradation states for unavailable optional services, partial search sources, stale indexes, and skipped artifacts.
- Caller-facing guidance text that command crates can render without parsing error strings.
- JSON-friendly representations for machine consumers.

Consumers decide which services are required for each command. `gobby-core` supplies the vocabulary and serialization.

**Acceptance:**

- 3.3.1 - Shared error and degradation enums are serializable and documented. file: `crates/gcore/src/degradation.rs`.
- 3.3.2 - Optional-service degradation is distinct from fatal command failure. test: `crates/gcore/src/degradation.rs::tests::optional_service_degradation_is_not_fatal`.
- 3.3.3 - Guidance text is structured, not string-parsed by callers. test: `crates/gcore/src/degradation.rs::tests::guidance_is_structured`.
- 3.3.4 - Development guide documents how `gobby-code` and `gobby-wiki` consume the shared contracts. file: `docs/guides/gcore-development-guide.md`.

## VS1: Verification
`kind: verification`

Validation for this plan:

- `uv run gobby plans validate .gobby/plans/gcore-rust-foundation.md`
- `cargo build -p gobby-core --no-default-features`
- `cargo test -p gobby-core --no-default-features`
- `cargo clippy -p gobby-core --no-default-features -- -D warnings`

Integration validation after dependent plans land:

- `cargo build -p gobby-code --no-default-features`
- `cargo build -p gobby-wiki --no-default-features`
- Focused tests proving `gobby-code` and `gobby-wiki` consume shared primitives without moving domain behavior into `gobby-core`.

## AC1: Acceptance Criteria
`kind: verification`

- `gobby-core` exposes shared context/config, setup, datastore, indexing, search, and degradation primitives.
- Attached mode remains non-destructive to Gobby-owned schema, files, and `config_store`.
- Standalone setup is explicit and scoped to consumer-owned resources.
- `gobby-code` keeps code graph and code-index domain APIs.
- `gobby-wiki` keeps llm-wiki vault UX, wiki domain APIs, and namespaced data ownership.
- FalkorDB and Qdrant absence is represented through typed degradation wherever those services are optional.

## V1 Plan Changelog
`kind: verification`

- **R1 (2026-05-26)**: Created the foundation plan for shared Rust substrate work. Scoped shared primitives to `gobby-core`; kept code graph behavior in `gobby-code` and wiki vault behavior in `gobby-wiki`; defined attached/standalone setup, datastore adapters, generic indexing/search primitives, and shared degradation contracts.
