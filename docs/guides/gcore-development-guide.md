# gobby-core Development Guide

Technical internals for developers and agents working in the `gobby-core` crate (`crates/gcore/`).

## What gobby-core Is

`gobby-core` is a small, dependency-light shared-primitives crate consumed by every Gobby CLI binary (`gcode`, `gsqz`, `gloc`, `ghook`). It exists so the binaries don't reimplement the same project-discovery and daemon-addressing logic four times — and so a behavior change (e.g. how the daemon URL is normalized) propagates with one PR instead of four.

It has no CLI. It has no public state. It's a library — that's the whole shape.

## Module Map

`crates/gcore/src/`:

| Module | Responsibility |
|--------|----------------|
| `project` | Walk up from a starting directory to find a `.gobby/` directory containing `project.json` or `gcode.json`. Read the `id` (or legacy `project_id`) field from `project.json`. |
| `bootstrap` | Read `~/.gobby/bootstrap.yaml` to get the daemon's listen endpoint (`bind_host`, `daemon_port`). Falls back to `127.0.0.1:60887` when the file is missing or malformed. |
| `daemon_url` | Compose a dial URL from a `DaemonEndpoint`, normalizing wildcard listen addresses (`0.0.0.0`, `::`, `::0`) to `127.0.0.1`. |

Roughly 250 lines of source total. Adding a fourth module should require justification.

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

## Why These Three Modules Specifically

Each module exists because at least two binaries need exactly this logic, and getting it slightly wrong in one of them would silently misbehave:

| Module | Consumers (today) | What goes wrong if duplicated |
|--------|-------------------|-------------------------------|
| `project` | `gcode`, `ghook` (and `gsqz`/`gloc` could use it) | Project discovery walks up across mounts, weird symlink loops, race conditions with `.gobby/` creation. One implementation = one set of edge cases. |
| `bootstrap` | `gcode`, `ghook` | YAML field naming, fallback semantics. Easy for two implementations to disagree on whether a missing field is fatal. |
| `daemon_url` | `ghook` (and `gcode` daemon RPC) | Wildcard-host normalization is non-obvious. A binary that POSTs to `0.0.0.0` will hang for the connect timeout instead of failing fast. |

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

### Out-of-tree

```toml
[dependencies]
gobby-core = "0.1"
```

Resolves against crates.io. The crate has no opinionated dependencies — `anyhow`, `dirs`, `serde_json`, `serde_yaml`, and `tempfile` (dev-only). It will not pull in tokio, reqwest, tracing, or anything else heavy.

## Adding a New Helper

Before adding a module or function to `gobby-core`, check:

1. **Do at least two binaries need it?** If only one does, keep it in that binary.
2. **Is it dependency-light?** New deps in `gobby-core` propagate to *every* binary. Adding `tokio` here would 5x the binary size of `ghook` for zero benefit. If the helper needs heavy deps, it probably belongs in a separate shared crate.
3. **Is it stateless or near-stateless?** `gobby-core` functions are pure or do narrow I/O (read one file, return result). A module that holds connection pools or background workers belongs elsewhere.
4. **Is the public surface small?** Three functions + a `DaemonEndpoint` struct is the right order of magnitude. If you find yourself adding a builder, a config object, and an `init()` function, reconsider.

If yes to all four, add the module:

1. Create `crates/gcore/src/<name>.rs` with `//!` module docs.
2. Add `pub mod <name>;` to `crates/gcore/src/lib.rs`.
3. Write tests that pin behavior under the failure modes the consumer cares about (missing input, malformed input, edge-case values).
4. Update this guide's module map.
5. Bump `gobby-core` to the next minor version (`0.2.0`) since you're adding public API.
6. Update consumer crates to use the new helper, replacing any duplicated implementation. Bump their versions too.

## Testing

Each module has `#[cfg(test)] mod tests` with `tempfile::tempdir()` for filesystem isolation:

- **project**: implicitly tested via consumer binaries (`gcode`, `ghook`); the module mirrors `gcode/src/project.rs` line-for-line.
- **bootstrap**: missing/malformed/empty files all return defaults; custom port/host parsing; out-of-range port falls back to default.
- **daemon_url**: wildcard IPv4/IPv6 normalize to loopback; localhost passes through; custom host+port composes correctly.

```bash
cargo test -p gobby-core
```

Fast, no I/O outside `tempdir()`, no network. Should run in well under a second.

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
