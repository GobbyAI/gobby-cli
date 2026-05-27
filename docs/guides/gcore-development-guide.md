# gobby-core Development Guide

Technical internals for developers and agents working in the `gobby-core` crate (`crates/gcore/`).

## What gobby-core Is

`gobby-core` is the shared Rust migration substrate for Gobby CLI crates and future Rust daemon work. It holds the boring, reusable platform layer: project discovery, bootstrap and daemon addressing, shared context/config contracts, setup boundaries, degradation vocabulary, optional datastore adapters, and generic indexing/search primitives.

Domain behavior stays out of this crate. Code graph facts, symbol IDs, language parsing policy, wiki vault layout, task behavior, memory behavior, and CLI output formatting belong to consumer crates.

The baseline crate remains dependency-light. Consumers that only need project discovery and daemon helpers do not inherit PostgreSQL, FalkorDB, Qdrant, reqwest, ignore, or sha2 unless they opt in through Cargo features.

## Module Map

`crates/gcore/src/`:

| Module | Feature | Responsibility |
|--------|---------|----------------|
| `project` | always | Walk up from a starting directory to find a `.gobby/` directory containing `project.json` or `gcode.json`. Read the `id` (or legacy `project_id`) field from `project.json`. |
| `bootstrap` | always | Read `~/.gobby/bootstrap.yaml` to get the daemon's listen endpoint (`bind_host`, `daemon_port`). Falls back to `127.0.0.1:60887` when the file is missing or malformed. |
| `daemon_url` | always | Compose a dial URL from a `DaemonEndpoint`, normalizing wildcard listen addresses (`0.0.0.0`, `::`, `::0`) to `127.0.0.1`. |
| `config` | always | Shared configuration-resolution contracts. Environment variables, `config_store`, and defaults are represented here as the foundation expands. |
| `context` | always | Shared runtime context contracts for project identity, daemon URL, and optional service configuration. Consumer-specific CLI state stays outside. |
| `degradation` | always | Shared vocabulary for optional-service absence, partial search, stale indexes, skipped artifacts, and fatal core errors. |
| `setup` | always | Attached and standalone setup contracts. Runtime commands validate externally managed resources and do not implicitly migrate them. |
| `postgres` | `postgres` | PostgreSQL hub adapter boundary. Validates Gobby-owned schema and BM25 requirements without creating, altering, or dropping managed objects. |
| `falkor` | `falkor` | FalkorDB adapter boundary. Graph connection helpers live here without making FalkorDB a baseline dependency. |
| `qdrant` | `qdrant` | Qdrant adapter boundary for vector search/storage integration. |
| `indexing` | `indexing` | Generic file walking, hashing, and indexing primitives that are not tied to one domain model. |
| `search` | `search` | Generic search result and fusion primitives. Code-specific or wiki-specific search behavior stays in consumers. |

Feature-gated modules are part of the public module map but compile only when their feature is selected.

## Public API

### `project`

```rust
pub fn find_project_root(start: &Path) -> Option<PathBuf>;
pub fn read_project_id(project_root: &Path) -> anyhow::Result<String>;
```

`find_project_root` walks up from `start` looking for a `.gobby/project.json` (Gobby-managed) or `.gobby/gcode.json` (gcode-standalone). Returns the directory *containing* `.gobby/`, not `.gobby/` itself. Returns `None` when neither marker is found before hitting the filesystem root.

`read_project_id` reads `<root>/.gobby/project.json` and extracts the `id` field, falling back to the legacy `project_id` key. Errors if the file is missing, malformed, or the field isn't present.

```rust
let cwd = std::env::current_dir()?;
if let Some(root) = gobby_core::project::find_project_root(&cwd) {
    let id = gobby_core::project::read_project_id(&root)?;
    println!("project {id} at {}", root.display());
}
```

### `bootstrap`

```rust
pub const DEFAULT_DAEMON_PORT: u16 = 60887;
pub const DEFAULT_BIND_HOST: &str = "127.0.0.1";

pub struct DaemonEndpoint { pub host: String, pub port: u16 }

pub fn bootstrap_path() -> Option<PathBuf>;
pub fn read_daemon_endpoint() -> DaemonEndpoint;
pub fn read_daemon_endpoint_at(path: &Path) -> DaemonEndpoint;
```

`read_daemon_endpoint` is the lookup callers want. `read_daemon_endpoint_at` exists for tests and for callers who already know the path. Both return `DaemonEndpoint::default()` (loopback + 60887) on any failure — missing file, unreadable, malformed YAML, missing fields, no home directory. **No errors are surfaced**; clients should always get *something* usable.

`DaemonEndpoint` returns the raw endpoint as written. `0.0.0.0` and `::` are valid listen addresses but invalid dial addresses — normalization is the caller's job, or the `daemon_url` module's, not this one's.

### `daemon_url`

```rust
pub fn daemon_url() -> String;
pub fn daemon_url_at(path: &Path) -> String;
```

Composes `http://{host}:{port}` from a bootstrap-derived endpoint, with one rewrite: wildcard listen hosts (`0.0.0.0`, `::`, `::0`) become `127.0.0.1`. Hostnames, named interfaces, and explicit IPv4/IPv6 literals pass through unchanged.

```rust
let url = gobby_core::daemon_url::daemon_url();
// "http://127.0.0.1:60887" for default bootstrap
// "http://10.0.0.5:61234" if bootstrap has bind_host: 10.0.0.5
// "http://127.0.0.1:60887" if bootstrap has bind_host: 0.0.0.0
ureq::post(&format!("{url}/api/hooks/execute")).send_string(body)?;
```

Bracketing IPv6 literals for URL embedding is **not** handled here — in practice `bootstrap.yaml` is always `localhost`, an IPv4 literal, or a wildcard. If that ever stops being true, this is the place to add it.

## Boundary Rules

Each module exists because multiple Rust consumers need the same infrastructure contract, and getting it slightly wrong in one crate would silently misbehave.

| Boundary | Consumers | What stays out |
|----------|-----------|----------------|
| Project/bootstrap/daemon helpers | `gcode`, `ghook`, future Rust consumers | CLI rendering, command dispatch, daemon workflow semantics. |
| Context/config/setup/degradation contracts | `gcode`, `gobby-wiki`, future daemon work | Domain-specific flags, output formats, setup UX, and task/memory behavior. |
| Datastore adapters | Consumers that opt in to `postgres`, `falkor`, or `qdrant` | Schema ownership, migrations, code graph facts, vector content policy. |
| Indexing/search primitives | Consumers that opt in to `indexing` or `search` | Code symbol IDs, language parsing policy, wiki document models, ranking UX. |

`gobby-core` can validate attached-mode resources, but it must not create, alter, drop, or migrate Gobby-owned resources during normal runtime commands.

## Feature Gates

The crate's default feature set is empty:

```toml
[features]
default = []
postgres = ["dep:postgres", "dep:postgres-types"]
falkor = ["dep:falkordb", "dep:urlencoding"]
qdrant = ["dep:reqwest"]
indexing = ["dep:ignore", "dep:sha2"]
search = []
full = ["postgres", "falkor", "qdrant", "indexing", "search"]
```

Feature rationale:

| Feature | Enables | Why gated |
|---------|---------|-----------|
| `postgres` | `postgres`, `postgres-types` | Hub validation and adapter code are only needed by datastore consumers. Lightweight binaries should not inherit PostgreSQL. |
| `falkor` | `falkordb`, `urlencoding` | Graph helpers need FalkorDB. `urlencoding` is included because FalkorDB connection URLs must encode passwords safely. |
| `qdrant` | `reqwest` with `blocking` and `json` | Vector search/storage helpers need HTTP. Other consumers should not pull reqwest. |
| `indexing` | `ignore`, `sha2` | File walking and content hashing are useful for indexing consumers only. |
| `search` | no extra dependency today | Search fusion contracts are lightweight, but still opt-in so the public surface remains explicit. |
| `full` | all feature modules | Convenience feature for development and consumers that need the whole foundation layer. |

Every individual feature must compile in isolation. Do not rely on `--all-features` to hide missing feature dependencies.

## Versioning Policy

`gobby-core` is `0.x`. The contract:

- **Patch bumps (0.1.x)** — bug fixes, doc changes, internal refactors with no public API change.
- **Minor bumps (0.x.0)** — additive public API (new functions, new fields). Existing consumers stay compatible.
- **Pre-1.0 breaking changes** — bump the minor and bump *every* consumer crate's gobby-core dep in the same release. Don't strand consumers on an old gobby-core.

Consumers pin to a minor version (`gobby-core = "0.1"`) so patch updates are picked up automatically but additive changes require a coordinated bump.

## How to Consume

### In-tree (workspace crates)

```toml
[dependencies]
gobby-core = { path = "../gcore", version = "0.1" }
```

The `path` is for local workspace builds; `version` is required by `cargo publish` and gets used when consumers install the crate from crates.io. Don't drop the `version` field — `cargo publish` will reject the consumer's manifest.

Opt in to heavier modules explicitly:

```toml
[dependencies]
gobby-core = { path = "../gcore", version = "0.1", features = ["postgres", "search"] }
```

Small binaries should keep the default empty feature set unless they directly use a feature-gated module.

### Out-of-tree

```toml
[dependencies]
gobby-core = "0.1"
```

Resolves against crates.io. The default crate has no datastore dependencies. It will not pull in PostgreSQL, FalkorDB, Qdrant, reqwest, ignore, sha2, tokio, tracing, or anything else heavy unless the consumer selects the matching feature.

## Adding a New Helper

Before adding a module or function to `gobby-core`, check:

1. **Do at least two binaries need it?** If only one does, keep it in that binary.
2. **Does it belong in an existing boundary?** Prefer `config`, `context`, `degradation`, `setup`, `postgres`, `falkor`, `qdrant`, `indexing`, or `search` before adding a new top-level module.
3. **Is it dependency-light, or properly feature-gated?** New baseline deps propagate to *every* binary. Heavy deps belong behind a narrowly named feature.
4. **Does it respect setup mode?** Attached-mode helpers validate externally managed state. Standalone setup helpers run only through explicit setup flows.
5. **Is it stateless or near-stateless?** `gobby-core` functions are pure or do narrow I/O (read one file, return result). A module that holds connection pools or background workers belongs elsewhere.
6. **Is the public surface small?** A few focused functions and structs per module is the right order of magnitude. If you find yourself adding a builder, a config object, and an `init()` function, reconsider.

If yes to all checks, add the helper:

1. Add it to the appropriate module with `//!` or item docs.
2. For a new lightweight module, add `pub mod <name>;` to `crates/gcore/src/lib.rs`.
3. For a new heavy module, add an optional dependency, a feature entry, and a `#[cfg(feature = "<feature>")] pub mod <name>;` guard.
4. Write tests that pin behavior under the failure modes the consumer cares about (missing input, malformed input, edge-case values).
5. Update this guide's module map and feature gate table when the public boundary changes.
6. Bump `gobby-core` to the next minor version (`0.2.0`) since you're adding public API.
7. Update consumer crates to use the new helper, replacing any duplicated implementation. Bump their versions too.

## Testing

Behavioral modules use `#[cfg(test)] mod tests` with `tempfile::tempdir()` for filesystem isolation:

- **project**: implicitly tested via consumer binaries (`gcode`, `ghook`); the module mirrors `gcode/src/project.rs` line-for-line.
- **bootstrap**: missing/malformed/empty files all return defaults; custom port/host parsing; out-of-range port falls back to default.
- **daemon_url**: wildcard IPv4/IPv6 normalize to loopback; localhost passes through; custom host+port composes correctly.
- **public_boundary**: integration test that pins feature gates, `lib.rs` module guards, and this guide's boundary documentation.

```bash
cargo test -p gobby-core --no-default-features
```

Baseline tests are fast, perform no network I/O, and keep filesystem writes inside temporary directories.

## Design Decisions

### Why Infallible Defaults Instead of `Result`

`read_daemon_endpoint` and friends return `DaemonEndpoint` (not `Result<DaemonEndpoint>`). The reasoning:

- Every consumer wants *some* endpoint to dial. Erroring at startup because `~/.gobby/bootstrap.yaml` doesn't exist would force every binary to handle the error identically (fall back to loopback + 60887). Centralizing that fallback here is the right move.
- The daemon defaults are well-known and stable. There's no "right" error message to surface — "use loopback" is always the answer.
- If a binary genuinely needs to know whether the file existed (e.g. for a setup-wizard prompt), it can call `bootstrap_path()` and `Path::exists()` directly.

`read_project_id` *does* return `Result` because there's no sane default for "I asked for a project ID and there isn't one" — the caller has to decide what that means.

### Why Listen-Address Normalization Lives in `daemon_url`, Not `bootstrap`

`bootstrap` returns the raw endpoint as written so callers can distinguish "user configured `0.0.0.0` for LAN exposure" from "user configured `127.0.0.1`." `daemon_url` is the layer concerned with *dialing*, so that's where the rewrite happens. Diagnostic tooling that wants to display the actual `bind_host` (e.g. `ghook --diagnose`) reads from `bootstrap` directly.

### Why Not Re-Export from a Prelude

There's no `gobby_core::prelude`. The crate is small enough that explicit imports (`use gobby_core::project::find_project_root`) are clearer than a glob. Keep it that way until the public surface grows past ~10 items.
