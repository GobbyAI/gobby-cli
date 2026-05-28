# gcode Graph Core Migration Contract

This guide defines the contract between `gcode` and Gobby daemon consumers while
code graph and vector projection ownership moves into Rust.

## Target Integration

The target architecture is direct Rust linking. A future Rust daemon should call
the `gobby-code` library APIs directly instead of shelling out through the CLI.
The stable daemon-facing boundaries are the library modules that already avoid
CLI output and `clap` types:

- `index::api` for code fact indexing.
- `projection::sync` for graph and vector projection sync reports.
- `graph::code_graph` and `graph::report` for graph lifecycle, graph reads, and
  project graph reports.
- `vector::code_symbols` for code-symbol vector lifecycle and search helpers.

The CLI commands remain compatibility wrappers over these APIs. They are useful
for temporary Python shims and operator workflows, but they are not the long-term
daemon integration surface.

## Transitional Python Shims

Python daemon consumers may temporarily shell out to stable `gcode` JSON
commands while the daemon is still Python-owned.

`CodeIndexTrigger` is the daemon-triggered indexing entry point. During the
transition it should invoke:

```bash
gcode index --sync-projections --format json
```

The JSON response contains indexing counts plus `projections.graph` and
`projections.vector` reports. Each report includes:

- `status`: `ok`, `degraded`, or `failed`.
- `synced_files`.
- `synced_symbols`.
- `degraded`.
- `error`: `null` or an object with `kind` and `message`.

Python maintenance flows that previously owned projection lifecycle work should
call Rust-owned lifecycle commands, or stable JSON wrapper functions around the
same commands:

```bash
gcode graph clear --format json
gcode graph rebuild --format json
gcode vector clear --format json
gcode vector rebuild --format json
```

Migration points in the Python daemon:

- `CodeIndexTrigger` calls `gcode index --sync-projections` for daemon-triggered
  indexing.
- `sync_worker.py` stops rebuilding graph and vector projections directly and
  delegates clear/rebuild work to Rust.
- `CodeIndexContext` drops projection lifecycle methods once callers route
  through the Rust commands or direct Rust library APIs.
- Python `CodeGraph` is retired after parity with Rust graph lifecycle, read,
  and report behavior.

Temporary shell-out wrappers must parse JSON stdout and preserve failure state.
A non-zero exit, invalid JSON payload, `status: "degraded"`, `status: "failed"`,
or `degraded: true` must become an explicit daemon degraded state with the Rust
`error.kind` and `error.message` attached when available. Shims must not report a
successful daemon sync when graph, vector, or report generation returned a
degraded or failed Rust result.

## Ownership Boundaries

| Surface | Owner | Contract |
|---------|-------|----------|
| PostgreSQL code facts | `gcode` Rust indexing APIs | Rust writes and updates code symbols, indexed files, content chunks, imports, calls, and sync flags. The PostgreSQL hub schema is Gobby-managed and externally migrated; `gcode` validates and uses it but does not create, alter, or drop Gobby-owned tables. |
| FalkorDB code graph projection | `gcode` Rust graph APIs | Rust clears, rebuilds, and syncs the code graph projection from PostgreSQL code facts. Python projection code delegates here during transition and is removed after parity. |
| Qdrant code-symbol vector projection | `gcode` Rust vector APIs | Rust owns collection lifecycle and vector upserts/deletes for code symbols. Projection sync calls OpenAI-compatible embedding endpoints directly from Rust. |
| Daemon embedding service | Gobby daemon, outside code projection sync | Code-index projection sync bypasses the daemon embedding service. Runtime config may still come from Gobby-managed config, but embedding HTTP calls for code vectors are performed by Rust. |
| Symbol summaries | Gobby daemon enrichment | LLM-generated summaries remain daemon-side and optional. `gcode` may read existing summaries for BM25/vector text, but it must treat missing summaries as normal and must not require LLM generation for indexing or projection sync. |
| Memory graph | Gobby memory services | Memory services continue to own memory nodes, memory relationships, and memory lifecycle. |
| `RELATES_TO_CODE` bridge edges | Gobby memory services | Bridge edges are memory-owned hints. `gcode graph report` may read and display them as inferred, optional report input; it must not create, update, or delete them. |
| UI, MCP, and HTTP surfaces | Gobby daemon repo | User-facing daemon APIs, MCP tools, and HTTP routes call daemon services. They should not become `gcode` CLI responsibilities. |

## Report And Degradation Contract

`gcode graph report --format json` is the daemon-readable report surface for
code graph summaries. Missing required graph services fail the command instead
of returning a fake empty report. Optional inputs, such as memory-owned
`RELATES_TO_CODE` bridge data, appear as report degradation details when they are
unavailable.

Daemon consumers should preserve three states:

- `ok`: Rust completed the requested operation and no degraded flag is present.
- `degraded`: Rust completed part of the operation or produced a report with
  unavailable optional input; callers should surface the degraded reason.
- `failed`: Rust could not complete the required operation; callers should keep
  the previous projection/report state or mark it stale.

The Python shim period ends when the daemon can link the Rust APIs directly and
all callers have moved off Python `CodeGraph`, Python graph/vector projection
code in `sync_worker.py`, and projection lifecycle methods on
`CodeIndexContext`.
