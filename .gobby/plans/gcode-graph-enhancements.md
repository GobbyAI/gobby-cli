# gcode graph core: reusable Rust graph with provenance and reports

## Overview
`kind: framing`

`gcode` is the Rust interim landing zone for code-index behavior while the Gobby daemon migrates to Rust. The durable target is not a CLI-owned graph implementation; it is a reusable Rust code-index/graph core that the CLI wraps today and the future Rust daemon links directly. Python daemon shims may shell out to `gcode` during the migration window, but that is a compatibility bridge, not the final architecture.

This plan moves code-graph writes, reads, lifecycle operations, and project graph reporting into Rust library boundaries first. `gcode` remains the user-facing CLI wrapper for those APIs. The code graph must work without the daemon process, and standalone mode gets an explicit setup path for the minimal app schema it needs.

The code/memory boundary stays sharp. Rust code-index modules own deterministic code facts: files, symbols, imports, definitions, calls, unresolved call targets, and code graph reports derived from those facts. Gobby memory services own memories, knowledge graph extraction, and `RELATES_TO_CODE` bridge creation. Rust report code may read bridge edges when present so agents can see hypotheses beside extracted code facts, but it must not create or mutate memory-owned data.

## Architecture Principles
`kind: framing`

- Core first: graph, report, setup, and schema behavior lives behind reusable Rust library APIs. `gcode` parses CLI args, resolves context, calls the library, and formats output.
- Direct linking is the target daemon integration. The future Rust daemon links the same Rust code directly; no daemon HTTP, MCP, or CLI shell boundary is the target internal architecture.
- Python daemon shell-outs are transitional only. If needed before the Rust daemon lands, Python calls stable `gcode` JSON commands and treats failures as explicit degradation.
- Gobby-attached mode remains non-destructive. It validates the externally managed hub schema and must not create, alter, or drop Gobby-owned tables.
- Standalone mode is explicit. A setup command creates only the minimal gcode-owned app schema in a selected standalone database or schema namespace. Runtime graph commands validate prerequisites and never run implicit migrations.
- Code owns code; memory owns memory. `CALLS`, `IMPORTS`, and `DEFINES` are extracted code facts. `RELATES_TO_CODE` and LLM-created memory relationships are inferred memory facts.
- Degraded behavior is honest. Missing PostgreSQL/FalkorDB/Qdrant pieces produce typed errors or degraded report sections; graph commands must not return fake empty success payloads for unavailable services.
- JSON compatibility is preserved. New metadata fields are optional with `#[serde(skip_serializing_if = "Option::is_none")]`.
- Phase 7 contract tests in the Gobby repo remain a compatibility gate until that external source-inspection contract changes.

## Non-Goals
`kind: framing`

- Do not make `gcode` the long-term owner of daemon orchestration, UI, MCP, or memory graph behavior.
- Do not add daemon-backed graph/report CLI commands as the target architecture.
- Do not rely on inherited Gobby-owned migrations as the standalone story.
- Do not write `.gobby/project.json`, mutate `config_store`, or run `gcode invalidate`.
- Do not add Graphify or any third-party graph product as a runtime dependency.
- Do not move code-symbol embedding generation to Rust in this plan.

## P1: Core Boundary And Setup
`kind: framing`

### 1.1 Create the reusable Rust library boundary [category: code]
`kind: deliverable`
Targets: `crates/gcode/Cargo.toml`, `crates/gcode/src/lib.rs`, `crates/gcode/src/main.rs`, `crates/gcode/src/commands/graph.rs`, `crates/gcode/src/falkor.rs`

Add a library target for `gobby-code` and move reusable code-index behavior behind modules callable from both the CLI and a future Rust daemon. The CLI keeps the existing binary surface, but implementation entry points should be library functions with input structs and serializable output structs.

Initial module shape:

- `crates/gcode/src/lib.rs` exports reusable modules.
- `graph::typed_query` owns safe FalkorDB parameter rendering.
- `graph::code_graph` owns code graph writes, reads, and lifecycle operations.
- `graph::report` owns project graph report generation.
- `setup` owns explicit standalone setup.
- `schema` keeps attached-mode validation.

`crates/gcode/src/falkor.rs` remains a compatibility facade for the external Phase 7 contract while implementation moves behind the library boundary. Do not collapse it into a pure re-export until the Gobby-side source-inspection test is revised.

**Acceptance:**

- 1.1.1 - `gobby-code` builds as both a library and `gcode` binary. file: `crates/gcode/Cargo.toml`, `crates/gcode/src/lib.rs`.
- 1.1.2 - `main.rs` and `commands/*` call library APIs rather than owning graph business logic. file: `crates/gcode/src/main.rs`, `crates/gcode/src/commands/graph.rs`.
- 1.1.3 - Library APIs avoid CLI-only types in public input/output contracts. test: `crates/gcode/src/lib.rs::tests::public_graph_api_is_cli_independent`.
- 1.1.4 - Phase 7 compatibility surface in `falkor.rs` remains available. test: `gobby/tests/code_index/test_gcode_phase7_contract.py`.

### 1.2 Add explicit standalone setup [category: code] (depends: 1.1)
`kind: deliverable`
Targets: `crates/gcode/src/schema.rs`, `crates/gcode/src/setup.rs`

Separate attached-mode validation from standalone setup:

- Attached mode validates the Gobby hub schema, `pg_search`, and BM25 indexes without creating or migrating Gobby-owned objects.
- Standalone setup is an explicit user action, for example `gcode setup --standalone`, that creates only the minimal gcode-owned app schema needed for indexing, graph sync state, and search in a selected database/schema namespace.
- Runtime commands fail with clear setup guidance when prerequisites are missing.

Standalone setup must not write `.gobby/project.json`, `config_store`, Gobby migrations, or daemon-owned metadata. It may create only gcode-owned objects after explicit opt-in.

**Acceptance:**

- 1.2.1 - Attached-mode schema validation remains read-only. file: `crates/gcode/src/schema.rs`.
- 1.2.2 - Standalone setup is implemented in a separate module from runtime validation. file: `crates/gcode/src/setup.rs`.
- 1.2.3 - Missing standalone prerequisites produce an actionable error instead of implicit creation. test: `crates/gcode/src/schema.rs::tests::missing_schema_requires_setup`.
- 1.2.4 - Standalone setup creates only gcode-owned objects and never touches `config_store` or `.gobby/project.json`. test: `crates/gcode/src/setup.rs::tests::standalone_setup_is_scoped`.

### 1.3 Add safe typed FalkorDB query rendering [category: code] (depends: 1.1)
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

## P2: Code Graph Core
`kind: framing`

### 2.1 Define provenance and confidence metadata [category: code] (depends: 1.1)
`kind: deliverable`
Targets: `crates/gcode/src/models.rs`, `crates/gcode/src/graph/code_graph.rs`, `crates/gcode/src/graph/report.rs`

Add a shared graph metadata model:

- `provenance`: `EXTRACTED`, `INFERRED`, or `AMBIGUOUS`.
- `confidence`: optional float. Deterministic code edges use `1.0`.
- `source_system`: producer name, such as `gcode`, `gobby-memory`, or `qdrant`.
- Source details such as file path, line, symbol ID, or matching method where available.

Code-derived `CALLS`, `IMPORTS`, and `DEFINES` are always `EXTRACTED` with `source_system = "gcode"`. Memory-derived and code/memory bridge edges are `INFERRED` or `AMBIGUOUS` and remain memory-owned.

**Acceptance:**

- 2.1.1 - Graph result structs expose optional metadata fields without breaking existing JSON consumers. file: `crates/gcode/src/models.rs`.
- 2.1.2 - Code edge writes stamp `provenance = "EXTRACTED"`, `confidence = 1.0`, and `source_system = "gcode"`. test: `crates/gcode/src/graph/code_graph.rs::tests::code_edges_carry_provenance`.
- 2.1.3 - Report output labels bridge edges as inferred hypotheses when present. test: `crates/gcode/src/graph/report.rs::tests::bridge_edges_are_hypotheses`.

### 2.2 Port code graph writes into the Rust core [category: code] (depends: 1.3, 2.1)
`kind: deliverable`
Targets: `crates/gcode/src/graph/code_graph.rs`, `crates/gcode/src/models.rs`

Implement `CodeGraph` write APIs for deterministic code graph projection:

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
Targets: `crates/gcode/src/graph/code_graph.rs`, `crates/gcode/src/search/graph_boost.rs`, `crates/gcode/src/commands/graph.rs`

Implement reusable read APIs that return stable graph payloads:

- project overview graph
- file graph
- symbol neighbors
- blast radius graph
- graph search/boost helpers needed by existing search commands

These APIs require available FalkorDB for graph reads. Empty graphs are valid only for successful queries against an available graph service.

**Acceptance:**

- 2.3.1 - Read APIs return the existing node/link JSON shape with optional metadata on links. file: `crates/gcode/src/graph/code_graph.rs`.
- 2.3.2 - Existing search graph boost behavior still handles missing graph config gracefully where search semantics allow degradation. test: `crates/gcode/src/search/graph_boost.rs::tests`.
- 2.3.3 - Hard graph commands fail non-zero with typed errors when FalkorDB is unavailable. test: `crates/gcode/src/commands/graph.rs::tests::graph_reads_require_falkor`.

### 2.4 Wrap core operations with gcode graph commands [category: code] (depends: 2.2, 2.3)
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

**Acceptance:**

- 2.4.1 - Lifecycle commands call `CodeGraph` directly and do not depend on the daemon process. file: `crates/gcode/src/commands/graph.rs`.
- 2.4.2 - `sync-file`, `clear`, and `rebuild` update graph sync state in PostgreSQL consistently with existing daemon semantics. file: `crates/gcode/src/db.rs`.
- 2.4.3 - Clap parsing covers all graph subcommands and global format handling. test: `crates/gcode/src/main.rs::tests::parse_graph_commands`.
- 2.4.4 - A daemon-stopped smoke test covers `overview`, `file`, `neighbors`, `blast-radius`, `sync-file`, `clear`, and `rebuild` against PostgreSQL plus FalkorDB. test: `crates/gcode/tests/graph_standalone.rs`.

## P3: Report And Migration Surfaces
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

### 3.2 Add gcode graph report CLI wrapper [category: code] (depends: 3.1)
`kind: deliverable`
Targets: `crates/gcode/src/commands/graph.rs`, `crates/gcode/src/main.rs`

Expose `gcode graph report --top-n <n>` as a thin wrapper over the Rust report API. It must use global `--format`, print JSON through `output::print_json`, and print structured text through `output::print_text`. Do not print raw Markdown as the whole text response.

**Acceptance:**

- 3.2.1 - `gcode graph report --format json` prints the serialized report. file: `crates/gcode/src/commands/graph.rs`.
- 3.2.2 - `gcode graph report --format text` prints a structured payload that includes `markdown`. test: `crates/gcode/src/commands/graph.rs::tests::report_text_structured_output`.
- 3.2.3 - Missing required graph services fail non-zero with a clear error and no fake empty report. test: `crates/gcode/src/commands/graph.rs::tests::report_requires_graph_service`.
- 3.2.4 - Clap parsing proves `--format` remains global and report-specific args stay minimal. test: `crates/gcode/src/main.rs::tests::parse_graph_report_global_format`.

### 3.3 Document daemon migration contracts [category: docs] (depends: 2.4, 3.2)
`kind: deliverable`
Target: `docs/guides/gcode-graph-core.md`

Document the migration contract for Gobby daemon consumers:

- Future Rust daemon links the library APIs directly.
- Python daemon shims may temporarily shell out to `gcode` JSON commands.
- Python shims must treat graph/report failures as explicit degraded states.
- Memory services continue to own memory graph and `RELATES_TO_CODE` writes.
- UI/MCP/HTTP surfaces belong in the daemon repo and should call daemon services, not become `gcode` responsibilities.

**Acceptance:**

- 3.3.1 - Daemon integration notes identify direct Rust linking as the target. file: `docs/guides/gcode-graph-core.md`.
- 3.3.2 - Transitional Python shell-out behavior is documented as temporary. file: `docs/guides/gcode-graph-core.md`.
- 3.3.3 - Ownership boundaries for code graph, memory graph, and bridge edges are explicit. file: `docs/guides/gcode-graph-core.md`.

## Test Plan
`kind: framing`

- `cargo build --workspace --no-default-features`
- `cargo test -p gobby-code --no-default-features`
- `cargo clippy -p gobby-code --no-default-features -- -D warnings`
- `cargo test --workspace`
- `cargo clippy --workspace -- -D warnings`
- Phase 7 contract tests in the Gobby repo pass against the updated `gcode` binary.
- FalkorDB integration tests are gated by `FALKORDB_HOST` and skip with a clear message when unavailable.
- Standalone smoke tests run with the daemon stopped against PostgreSQL plus FalkorDB.
- JSON compatibility tests prove current consumers can parse outputs with optional graph metadata.

## Acceptance Criteria
`kind: framing`

- Reusable Rust library APIs own code graph writes, reads, lifecycle, setup, and report generation.
- `gcode` graph commands are CLI wrappers over library APIs.
- Future Rust daemon can link the same code directly.
- Python daemon shell-outs, if used, are explicitly transitional.
- Standalone mode has explicit setup and does not depend on inherited Gobby-owned migrations.
- Attached mode remains non-destructive to Gobby-owned schema and files.
- Code graph facts and memory graph facts keep separate ownership.
- Provenance/confidence metadata lets agents distinguish extracted code facts from inferred bridge/memory links.
- Graph/report degraded behavior is explicit and never masquerades as successful empty data.
- Existing JSON consumers remain compatible.

## Plan Changelog
`kind: framing`

- **R1-R12 (2026-05-24)**: Earlier iterations specified direct `gcode` ownership of graph writes/reads, route-shaped CLI commands, provenance metadata, graph lifecycle cleanup, report output, and Phase 7 compatibility constraints.
- **R13 (2026-05-26)**: Reframed the plan around reusable Rust core/library boundaries with `gcode` as CLI wrapper; made future Rust daemon direct linking the target; limited Python daemon shell-outs to transitional shims; added explicit standalone setup and minimal app-schema creation; preserved provenance/confidence, code-vs-memory ownership, graph report, and degraded behavior concepts; removed stale daemon-backed CLI and inherited-migration framing.

## Task Plan
`kind: framing`

```yaml
- title: Create reusable Rust library boundary
  category: code
  task_type: feature
  depends_on: []
  validation_criteria: "cargo build -p gobby-code --no-default-features"
  labels:
  - covers:unknown:1.1:1.1.1
  - covers:unknown:1.1:1.1.2
  - covers:unknown:1.1:1.1.3
  - covers:unknown:1.1:1.1.4
  tdd: true
  source_section: '1.1'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Add explicit standalone setup
  category: code
  task_type: feature
  depends_on:
  - '1.1'
  validation_criteria: "crates/gcode/src/setup.rs::tests::standalone_setup_is_scoped"
  labels:
  - covers:unknown:1.2:1.2.1
  - covers:unknown:1.2:1.2.2
  - covers:unknown:1.2:1.2.3
  - covers:unknown:1.2:1.2.4
  tdd: true
  source_section: '1.2'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Add typed Falkor query boundary
  category: code
  task_type: feature
  depends_on:
  - '1.1'
  validation_criteria: "crates/gcode/src/graph/typed_query.rs::tests"
  labels:
  - covers:unknown:1.3:1.3.1
  - covers:unknown:1.3:1.3.2
  - covers:unknown:1.3:1.3.3
  tdd: true
  source_section: '1.3'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Define graph provenance metadata
  category: code
  task_type: feature
  depends_on:
  - '1.1'
  validation_criteria: "crates/gcode/src/graph/code_graph.rs::tests::code_edges_carry_provenance"
  labels:
  - covers:unknown:2.1:2.1.1
  - covers:unknown:2.1:2.1.2
  - covers:unknown:2.1:2.1.3
  tdd: true
  source_section: '2.1'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Port code graph writes to Rust core
  category: code
  task_type: feature
  depends_on:
  - '1.3'
  - '2.1'
  validation_criteria: "crates/gcode/src/graph/code_graph.rs::tests::delete_preserves_current_symbols"
  labels:
  - covers:unknown:2.2:2.2.1
  - covers:unknown:2.2:2.2.2
  - covers:unknown:2.2:2.2.3
  - covers:unknown:2.2:2.2.4
  tdd: true
  source_section: '2.2'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Port code graph reads to Rust core
  category: code
  task_type: feature
  depends_on:
  - '2.2'
  validation_criteria: "crates/gcode/src/commands/graph.rs::tests::graph_reads_require_falkor"
  labels:
  - covers:unknown:2.3:2.3.1
  - covers:unknown:2.3:2.3.2
  - covers:unknown:2.3:2.3.3
  tdd: true
  source_section: '2.3'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Wrap graph core with gcode commands
  category: code
  task_type: feature
  depends_on:
  - '2.2'
  - '2.3'
  validation_criteria: "crates/gcode/src/main.rs::tests::parse_graph_commands"
  labels:
  - covers:unknown:2.4:2.4.1
  - covers:unknown:2.4:2.4.2
  - covers:unknown:2.4:2.4.3
  - covers:unknown:2.4:2.4.4
  tdd: true
  source_section: '2.4'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Generate project graph report in Rust core
  category: code
  task_type: feature
  depends_on:
  - '2.3'
  validation_criteria: "crates/gcode/src/graph/report.rs::tests::report_shape"
  labels:
  - covers:unknown:3.1:3.1.1
  - covers:unknown:3.1:3.1.2
  - covers:unknown:3.1:3.1.3
  - covers:unknown:3.1:3.1.4
  tdd: true
  source_section: '3.1'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Add gcode graph report CLI wrapper
  category: code
  task_type: feature
  depends_on:
  - '3.1'
  validation_criteria: "crates/gcode/src/main.rs::tests::parse_graph_report_global_format"
  labels:
  - covers:unknown:3.2:3.2.1
  - covers:unknown:3.2:3.2.2
  - covers:unknown:3.2:3.2.3
  - covers:unknown:3.2:3.2.4
  tdd: true
  source_section: '3.2'
  implementation_domain: backend
  assigned_agent: backend-developer
- title: Document daemon migration contracts
  category: docs
  task_type: documentation
  depends_on:
  - '2.4'
  - '3.2'
  validation_criteria: "docs/guides/gcode-graph-core.md documents direct Rust linking target"
  labels:
  - covers:unknown:3.3:3.3.1
  - covers:unknown:3.3:3.3.2
  - covers:unknown:3.3:3.3.3
  tdd: false
  source_section: '3.3'
  implementation_domain: backend
  assigned_agent: backend-developer
```
