# gobby-core Rust foundation

**Plan ID:** gcore-rust-foundation

## O1: Overview
`kind: framing`

`gobby-core` is the shared Rust migration substrate for Gobby CLI crates and the future Rust daemon. It should hold the boring, reusable platform layer: context and config resolution, attached versus standalone setup contracts, PostgreSQL/FalkorDB/Qdrant adapters, generic indexing/search primitives, and shared error/degradation types.

Domain behavior stays out of this crate. Code graph facts, symbol IDs, language parsing policy, and graph APIs stay in `gobby-code`. Wiki vault layout, llm-wiki UX, ingestion flows, and article synthesis stay in `gobby-wiki`. `gobby-core` exists so those crates stop copying infrastructure while keeping their domain boundaries sharp.

The crate already exists at `crates/gcore/` with three small modules (`project`, `bootstrap`, `daemon_url`, ~250 lines total) consumed by `gobby-code` and `gobby-hooks`. This plan expands it into the full foundation layer behind Cargo feature gates so consumers that only need project discovery continue to get a tiny dependency.

## C1: Constraints
`kind: framing`

- **Non-destructive attached mode**: attached Gobby projects validate externally managed schema and service availability. They do not create, alter, drop, or migrate Gobby-owned objects.
- **Explicit standalone mode**: standalone setup is an explicit opt-in operation. Runtime commands never perform implicit schema creation.
- **Resolution order**: service config resolves from environment variables, then `config_store`, then hardcoded defaults. Consumers must not short-circuit this order.
- **No domain ownership**: `gobby-core` must not know about code symbols, wiki documents, vault UX, task behavior, memories, or daemon workflow semantics.
- **Graceful absence**: FalkorDB and Qdrant are optional dependencies at runtime. Missing services surface typed degradation rather than panics or fake empty success.
- **Small public API**: APIs should expose stable structs, traits, and error enums, not CLI parser types or command-output formatting.
- **Feature-gated heavy dependencies**: the baseline crate (no features) stays dependency-light (`anyhow`, `dirs`, `serde_json`, `serde_yaml`). Heavy dependencies like `postgres`, `falkordb`, and `reqwest` live behind Cargo features. Consumers opt in to only the adapters they need. `gsqz`, `gloc`, and `ghook` must not inherit datastore dependencies they never use.

## D1: Dependent Plans
`kind: framing`

This plan is the foundation dependency for `.gobby/plans/gcode-graph-enhancements.md` and `.gobby/plans/gwiki.md`.

`gobby-code` may depend on the context/config, datastore adapter, search fusion, and indexing primitives from `gobby-core`, but it owns code-specific graph APIs and code-index semantics.

`gobby-wiki` may depend on the same primitives, but it owns vault semantics, wiki document models, namespaced storage, ingestion, research, compile, audit, and Obsidian-compatible output.

## P1: Context And Setup Contracts
`kind: framing`

**Goal**: define the shared Rust foundation boundary, degradation vocabulary, context/config resolution, and setup modes that every consumer crate can use without inheriting another domain's behavior.

### 1.1 Define the gobby-core public boundary [category: code]
`kind: deliverable`

Targets: `crates/gcore/Cargo.toml`, `crates/gcore/src/lib.rs`, `docs/guides/gcore-development-guide.md`

Expand the existing `gobby-core` crate into the documented foundation layer. The crate currently exposes three modules (`project`, `bootstrap`, `daemon_url`). This task adds the module map, Cargo feature gates, and dev-guide updates for the full foundation surface.

**Cargo.toml feature structure:**

```toml
[features]
default = []
postgres = ["dep:postgres", "dep:postgres-types"]
falkor = ["dep:falkordb", "dep:urlencoding"]
qdrant = ["dep:reqwest"]
indexing = ["dep:ignore", "dep:sha2"]
search = []
full = ["postgres", "falkor", "qdrant", "indexing", "search"]

[dependencies]
anyhow = "1"
dirs = "6"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
serde_yaml = "0.9"
thiserror = "2"

# Feature-gated
postgres = { version = "0.19", optional = true }
postgres-types = { version = "0.2", optional = true }
falkordb = { version = "0.3", optional = true }
reqwest = { version = "0.12", features = ["blocking", "json"], optional = true }
ignore = { version = "0.4", optional = true }
sha2 = { version = "0.10", optional = true }
urlencoding = { version = "2", optional = true }
```

The `falkor` feature includes `dep:urlencoding` because `GraphClient::from_config` uses `urlencoding::encode` for password-safe FalkorDB connection URLs. Without this, `cargo build -p gobby-core --features falkor` would fail to compile while `--all-features` would mask the error.

**lib.rs module map (expanded):**

```rust
//! Shared primitives for Gobby CLI tools.

// Always available — existing modules
pub mod bootstrap;
pub mod daemon_url;
pub mod project;

// Always available — new lightweight modules
pub mod config;
pub mod context;
pub mod degradation;
pub mod setup;

// Feature-gated modules
#[cfg(feature = "postgres")]
pub mod postgres;

#[cfg(feature = "falkor")]
pub mod falkor;

#[cfg(feature = "qdrant")]
pub mod qdrant;

#[cfg(feature = "indexing")]
pub mod indexing;

#[cfg(feature = "search")]
pub mod search;
```

Update `docs/guides/gcore-development-guide.md` to document the expanded module map, feature gate rationale, and updated "Adding a New Helper" guidance that accounts for feature-gated modules.

**Acceptance:**

- 1.1.1 - `crates/gcore/Cargo.toml` defines feature gates for `postgres`, `falkor` (including `dep:urlencoding`), `qdrant`, `indexing`, `search`, and `full`. file: `crates/gcore/Cargo.toml`.
- 1.1.2 - `crates/gcore/src/lib.rs` documents the foundation module map with `#[cfg(feature)]` guards on heavy modules. file: `crates/gcore/src/lib.rs`.
- 1.1.3 - `docs/guides/gcore-development-guide.md` describes `gobby-core` as shared substrate with feature gate documentation. file: `docs/guides/gcore-development-guide.md`.
- 1.1.4 - `gobby-core` builds under `--no-default-features` with only the lightweight baseline modules. test: `cargo build -p gobby-core --no-default-features`.
- 1.1.5 - Each individual feature compiles in isolation: `cargo build -p gobby-core --features falkor`, `--features qdrant`, `--features postgres`, `--features indexing`. test: `cargo build -p gobby-core --features falkor && cargo build -p gobby-core --features qdrant && cargo build -p gobby-core --features postgres && cargo build -p gobby-core --features indexing`.

### 1.2 Add shared error and degradation contracts [category: code] (depends: 1.1)
`kind: deliverable`

Targets: `crates/gcore/src/degradation.rs`, `docs/guides/gcore-development-guide.md`

Define shared error and degradation contracts used by datastore adapters, setup contracts, indexing, and search. This module is always available (no feature gate) so even lightweight consumers can use the vocabulary. It must be defined before the setup contracts (§1.4), datastore adapters (§2.2, §2.3), and search fusion (§3.2) that consume its types.

**degradation.rs — error and degradation types:**

```rust
use serde::{Serialize, Deserialize};

/// Service availability state, returned alongside results from adapters.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub enum ServiceState {
    /// Service is connected and responding.
    Available,
    /// Service is not configured (no config found from any source).
    NotConfigured,
    /// Service is configured but unreachable.
    Unreachable { message: String },
}

impl ServiceState {
    pub fn is_available(&self) -> bool {
        matches!(self, Self::Available)
    }
}

/// Setup validation issue with actionable guidance.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SetupIssue {
    pub object_name: String,
    pub store: String,
    pub guidance: Guidance,
}

/// Structured guidance text for setup issues.
///
/// Callers render these; `gobby-core` does not format CLI output.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Guidance {
    /// What is missing or wrong.
    pub problem: String,
    /// What the user should do.
    pub action: String,
    /// Optional command suggestion.
    pub command_hint: Option<String>,
}

/// Fatal errors that prevent a command from completing.
#[derive(Debug, thiserror::Error)]
pub enum CoreError {
    #[error("invalid configuration: {0}")]
    InvalidConfig(String),
    #[error("required service unavailable: {service} — {message}")]
    RequiredServiceUnavailable { service: String, message: String },
    #[error("write failed: {0}")]
    WriteFailed(String),
    #[error("corrupted input: {0}")]
    CorruptedInput(String),
}

/// Degradation states for partial results.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum DegradationKind {
    /// An optional service was unavailable during this operation.
    ServiceUnavailable { service: String, state: ServiceState },
    /// Search completed with fewer sources than requested.
    PartialSearch { available: Vec<String>, unavailable: Vec<String> },
    /// Index data may be stale (content hash mismatch or age threshold).
    StaleIndex { paths: Vec<String> },
    /// Some artifacts were skipped during indexing.
    SkippedArtifacts { count: usize, reason: String },
}
```

Consumers decide which services are required versus optional for each command. `gobby-core` supplies the vocabulary, serialization, and structured guidance.

**Acceptance:**

- 1.2.1 - `ServiceState`, `CoreError`, `DegradationKind`, and `Guidance` are documented and `Serialize + Deserialize`. file: `crates/gcore/src/degradation.rs`.
- 1.2.2 - `ServiceState::NotConfigured` and `ServiceState::Unreachable` are distinct from `CoreError::RequiredServiceUnavailable`. test: `crates/gcore/src/degradation.rs::tests::optional_service_degradation_is_not_fatal`.
- 1.2.3 - `Guidance` carries structured `problem`, `action`, and optional `command_hint` fields. test: `crates/gcore/src/degradation.rs::tests::guidance_is_structured`.
- 1.2.4 - Development guide documents how `gobby-code` and `gobby-wiki` consume degradation contracts. file: `docs/guides/gcore-development-guide.md`.

### 1.3 Add shared context and config resolution [category: code] (depends: 1.1)
`kind: deliverable`

Targets: `crates/gcore/src/context.rs`, `crates/gcore/src/config.rs`, `crates/gcore/src/bootstrap.rs`, `crates/gcore/src/project.rs`

Extend the existing `bootstrap.rs` and `project.rs` modules and create new `context.rs` and `config.rs` modules for shared context resolution. The existing project-root and bootstrap helpers remain unchanged; this task adds service config resolution on top.

`gcode` currently resolves its own `Context` struct (at `crates/gcode/src/config.rs:43`) with project root, database URL, and optional `FalkorConfig`/`QdrantConfig`/`EmbeddingConfig`. The shared `CoreContext` generalizes this pattern so `gobby-wiki` can resolve the same services without duplicating resolution logic.

**context.rs — shared context struct:**

```rust
use std::path::PathBuf;

/// Resolved runtime context for any gobby-core consumer.
///
/// Built by `CoreContext::resolve()`. Contains project identity and
/// optional service configs. Domain-specific fields (quiet flags,
/// output format) stay in consumer crates.
pub struct CoreContext {
    /// Project root directory (contains `.gobby/`)
    pub project_root: PathBuf,
    /// Project ID from `.gobby/project.json`
    pub project_id: String,
    /// PostgreSQL hub DSN (from env or bootstrap.yaml)
    pub database_url: Option<String>,
    /// FalkorDB config (None when service is absent)
    pub falkordb: Option<FalkorConfig>,
    /// Qdrant config (None when service is absent)
    pub qdrant: Option<QdrantConfig>,
    /// Embedding API config (None → no semantic search)
    pub embedding: Option<EmbeddingConfig>,
    /// Gobby daemon base URL
    pub daemon_url: Option<String>,
}
```

**config.rs — service config types, value decoding, and resolution:**

```rust
/// FalkorDB connection configuration.
#[derive(Debug, Clone)]
pub struct FalkorConfig {
    pub host: String,
    pub port: u16,
    pub password: Option<String>,
    pub graph_name: String,
}

/// Qdrant connection configuration.
#[derive(Debug, Clone)]
pub struct QdrantConfig {
    pub url: Option<String>,
    pub api_key: Option<String>,
    pub collection_prefix: String,
}

/// Embedding API configuration (OpenAI-compatible endpoint).
#[derive(Debug, Clone)]
pub struct EmbeddingConfig {
    pub api_base: String,
    pub model: String,
    pub api_key: Option<String>,
}

/// Decode a config_store value from its stored representation.
///
/// The Gobby config_store stores values as raw strings that may be
/// JSON-encoded. This function handles:
/// - JSON strings (`"http://host:7474"`) → inner value (`http://host:7474`)
/// - Plain strings (`http://host:7474`) → pass-through
/// - JSON arrays/objects → `None` (not a scalar config value)
///
/// Matches the behavior of `gcode`'s `decode_config_value`.
pub fn decode_config_value(raw: &str) -> Option<String> {
    match serde_json::from_str::<serde_json::Value>(raw) {
        Ok(serde_json::Value::String(s)) => Some(s),
        Ok(serde_json::Value::Number(n)) => Some(n.to_string()),
        Ok(serde_json::Value::Bool(b)) => Some(b.to_string()),
        Ok(_) => None, // arrays, objects, null
        Err(_) => Some(raw.to_string()), // plain string
    }
}

/// Resolve `${VAR}` and `${VAR:-default}` environment variable patterns.
///
/// Returns `Ok(None)` when the var is unset and no default is provided.
/// Returns `Ok(Some(value))` with the resolved value.
/// Non-pattern strings pass through unchanged.
pub fn resolve_env_pattern(value: &str) -> anyhow::Result<Option<String>> {
    if !value.contains("${") {
        return Ok(Some(value.to_string()));
    }
    // Handle ${VAR:-default} and ${VAR} patterns
    // (regex or manual parsing of the pattern)
    todo!("implementation")
}

/// Consumer-supplied value resolver for `$secret:NAME` and other
/// interpolation patterns.
///
/// `gcode` passes its `secrets::resolve_config_value` which decrypts
/// Fernet-encrypted secrets from the `secrets` table using machine_id
/// and secret_salt. `gobby-wiki` will use the same resolver.
///
/// The resolver receives the raw value string after `decode_config_value`
/// and returns the fully resolved value. `gobby-core` calls
/// `decode_config_value` first, then passes the decoded value to the
/// resolver if one is provided.
pub type ValueResolver = Box<dyn Fn(&str) -> anyhow::Result<String>>;

/// Resolve FalkorDB config from env → config_store → defaults.
///
/// Env vars: GOBBY_FALKORDB_HOST, GOBBY_FALKORDB_PORT,
///           GOBBY_FALKORDB_PASSWORD, GOBBY_FALKORDB_GRAPH
///
/// The `value_resolver` callback handles `$secret:NAME` and `${VAR}`
/// patterns found in config_store values. Consumers supply their own
/// resolver (e.g. `gcode` passes `secrets::resolve_config_value`).
/// Pass `None` to skip interpolation and use raw decoded values.
///
/// Returns None when no host is configured from any source.
#[cfg(feature = "postgres")]
pub fn resolve_falkordb_config(
    conn: &mut postgres::Client,
    value_resolver: Option<&ValueResolver>,
) -> Option<FalkorConfig> { /* ... */ }

/// Resolve Qdrant config from env → config_store → defaults.
///
/// Env vars: GOBBY_QDRANT_URL, GOBBY_QDRANT_API_KEY,
///           GOBBY_QDRANT_COLLECTION_PREFIX
///
/// Same resolver semantics as `resolve_falkordb_config`.
#[cfg(feature = "postgres")]
pub fn resolve_qdrant_config(
    conn: &mut postgres::Client,
    value_resolver: Option<&ValueResolver>,
) -> Option<QdrantConfig> { /* ... */ }

/// Resolve embedding API config from env → config_store → defaults.
///
/// Env vars: GOBBY_EMBEDDING_API_BASE, GOBBY_EMBEDDING_MODEL,
///           GOBBY_EMBEDDING_API_KEY
///
/// Same resolver semantics as `resolve_falkordb_config`.
#[cfg(feature = "postgres")]
pub fn resolve_embedding_config(
    conn: &mut postgres::Client,
    value_resolver: Option<&ValueResolver>,
) -> Option<EmbeddingConfig> { /* ... */ }
```

The resolution functions that read `config_store` require the `postgres` feature. When `postgres` is not enabled, consumers supply their own config structs or resolve from environment only. `resolve_from_env_only()` variants are always available.

**Config value pipeline:** `read_config_value` reads the raw string from `config_store` → `decode_config_value` unwraps JSON encoding → the consumer-supplied `ValueResolver` handles `$secret:NAME` and remaining `${VAR}` patterns. This preserves the existing `gcode` resolution semantics (env → config_store with JSON decode → secret/env interpolation → defaults) without pulling Fernet crypto dependencies into `gobby-core`.

**Existing modules — no breaking changes:**

- `bootstrap.rs`: no API changes. The existing `DaemonEndpoint`, `read_daemon_endpoint`, and `bootstrap_path` remain as-is.
- `project.rs`: no API changes. The existing `find_project_root` and `read_project_id` remain as-is.

**Acceptance:**

- 1.3.1 - `CoreContext` struct holds project root, project id, database URL, and optional service configs. file: `crates/gcore/src/context.rs`.
- 1.3.2 - FalkorDB and Qdrant resolution preserves env-var precedence over `config_store` over defaults. test: `crates/gcore/src/config.rs::tests::env_overrides_config_store`.
- 1.3.3 - Missing optional service config is represented as `None` and does not panic. test: `crates/gcore/src/context.rs::tests::missing_optional_services_are_none`.
- 1.3.4 - Existing `bootstrap.rs` and `project.rs` public APIs are unchanged. test: `crates/gcore/src/project.rs::tests::read_project_id_is_non_destructive`.
- 1.3.5 - `decode_config_value` unwraps JSON strings, passes through plain strings, and returns `None` for JSON arrays/objects. test: `crates/gcore/src/config.rs::tests::decode_config_value_handles_json_and_plain`.
- 1.3.6 - `resolve_env_pattern` resolves `${VAR}` and `${VAR:-default}` patterns from environment variables. test: `crates/gcore/src/config.rs::tests::resolve_env_pattern_with_defaults`.
- 1.3.7 - Resolution functions accept a consumer-supplied `ValueResolver` for `$secret:NAME` interpolation; passing `None` uses raw decoded values. test: `crates/gcore/src/config.rs::tests::resolver_callback_handles_secrets`.

### 1.4 Define attached and standalone setup contracts [category: code] (depends: 1.2, 1.3)
`kind: deliverable`

Targets: `crates/gcore/src/setup.rs`, `docs/guides/gcore-development-guide.md`

Add shared setup contracts that domain crates implement without copying policy. `gcode` currently validates schema in its own schema module with inline checks; `gobby-wiki` will need similar validation for `gwiki_*` tables. The shared contract generalizes the validation/creation boundary.

**setup.rs — contract traits and types:**

```rust
use crate::degradation::{SetupIssue, Guidance};

/// Datastore kind for object classification.
pub enum StoreKind {
    Postgres,
    FalkorDB,
    Qdrant,
}

/// Context supplied to validation callbacks.
///
/// Contains optional mutable connections to each datastore. Consumers
/// use whichever connection their validator needs; `None` means the
/// service is not configured. The mutable references are required
/// because `postgres::Client::query` takes `&mut self`.
pub struct ValidationContext<'a> {
    #[cfg(feature = "postgres")]
    pub pg: Option<&'a mut postgres::Client>,
    pub falkor_config: Option<&'a crate::config::FalkorConfig>,
    pub qdrant_config: Option<&'a crate::config::QdrantConfig>,
}

/// Result of running all attached-mode validators.
#[derive(Debug, Default)]
pub struct ValidationReport {
    /// Names of objects that passed validation.
    pub present: Vec<String>,
    /// Objects that failed validation, with structured issue details.
    pub missing: Vec<(String, SetupIssue)>,
}

impl ValidationReport {
    pub fn is_healthy(&self) -> bool {
        self.missing.is_empty()
    }
}

/// Required object that a consumer crate declares for setup validation.
pub struct RequiredObject {
    /// Human-readable name (e.g. "symbols table", "wiki_docs table")
    pub name: String,
    /// Store kind: Postgres, FalkorDB, Qdrant
    pub store: StoreKind,
    /// Consumer-supplied check function (mutable for database queries)
    pub validator: Box<dyn FnMut(&mut ValidationContext<'_>) -> Result<(), SetupIssue>>,
}

/// Attached-mode validation: check that externally managed resources exist.
/// Never creates, alters, or drops anything.
pub trait AttachedValidator {
    /// Declare the objects this consumer requires.
    fn required_objects(&self) -> Vec<RequiredObject>;

    /// Run all validators and return a report of present/missing objects.
    fn validate(&self, ctx: &mut ValidationContext<'_>) -> ValidationReport {
        let mut report = ValidationReport::default();
        for mut obj in self.required_objects() {
            match (obj.validator)(ctx) {
                Ok(()) => report.present.push(obj.name.clone()),
                Err(issue) => report.missing.push((obj.name.clone(), issue)),
            }
        }
        report
    }
}

/// Context supplied to standalone setup creation callbacks.
///
/// Mutable references are required because `postgres::Client::execute`
/// takes `&mut self` for DDL/DML operations.
pub struct SetupContext<'a> {
    #[cfg(feature = "postgres")]
    pub pg: Option<&'a mut postgres::Client>,
    pub falkor_config: Option<&'a crate::config::FalkorConfig>,
    pub qdrant_config: Option<&'a crate::config::QdrantConfig>,
    /// If true, skip prompts and apply defaults.
    pub non_interactive: bool,
}

/// Report from a standalone setup creation run.
#[derive(Debug, Default)]
pub struct SetupReport {
    /// Objects successfully created.
    pub created: Vec<String>,
    /// Objects that already existed and were skipped.
    pub skipped: Vec<String>,
    /// Objects that failed creation, with error detail.
    pub failed: Vec<(String, String)>,
}

/// Error from standalone setup creation.
#[derive(Debug, thiserror::Error)]
pub enum SetupError {
    #[error("connection failed for {store}: {message}")]
    ConnectionFailed { store: String, message: String },
    #[error("creation failed for {object}: {message}")]
    CreationFailed { object: String, message: String },
    #[error("setup refused in attached mode — use standalone setup")]
    AttachedModeRefused,
}

/// An object that a consumer crate owns and can create in standalone mode.
pub struct OwnedObject {
    /// Human-readable name (e.g. "gcode_symbols table")
    pub name: String,
    /// Store kind: Postgres, FalkorDB, Qdrant
    pub store: StoreKind,
    /// Consumer-supplied creation function (mutable for DDL execution)
    pub creator: Box<dyn FnMut(&mut SetupContext<'_>) -> Result<(), SetupError>>,
}

/// Standalone-mode setup: explicit opt-in creation of consumer-owned resources.
pub trait StandaloneSetup {
    /// Namespace prefix for this consumer's owned resources (e.g. "gcode", "gwiki").
    fn namespace(&self) -> &str;

    /// Declare what this consumer owns and can create.
    fn owned_objects(&self) -> Vec<OwnedObject>;

    /// Create consumer-owned resources. Called only on explicit `setup` command.
    fn create(&self, ctx: &mut SetupContext<'_>) -> Result<SetupReport, SetupError>;
}
```

`SetupIssue` and `Guidance` are imported from `crate::degradation` (defined in §1.2, always available without feature gates).

`gobby-core` provides the contract traits and validation helpers. It does not hardcode `gcode_*`, `gwiki_*`, `Symbol`, `WikiDoc`, or any domain-owned objects.

**Acceptance:**

- 1.4.1 - `AttachedValidator` trait exposes read-only validation hooks that never mutate datastore schema. file: `crates/gcore/src/setup.rs`.
- 1.4.2 - `StandaloneSetup` trait requires explicit namespace and consumer-owned object declarations. file: `crates/gcore/src/setup.rs`.
- 1.4.3 - `ValidationReport` returns typed `SetupIssue` with actionable guidance text. test: `crates/gcore/src/setup.rs::tests::runtime_validation_reports_setup_guidance`.
- 1.4.4 - Setup docs state that `gobby-core` does not create Gobby-owned schema in attached mode. file: `docs/guides/gcore-development-guide.md`.
- 1.4.5 - `ValidationContext` and `SetupContext` supply mutable references, allowing consumer validators to query and creators to execute against the supplied PostgreSQL connection. test: `crates/gcore/src/setup.rs::tests::validator_can_query_through_mutable_context`.
- 1.4.6 - A standalone creator can execute DDL through the mutable `SetupContext` without moving ownership from subsequent callbacks. test: `crates/gcore/src/setup.rs::tests::creator_executes_without_moving_ownership`.

## P2: Datastore Adapters
`kind: framing`

**Goal**: centralize client plumbing and safety contracts for PostgreSQL, FalkorDB, and Qdrant while leaving schemas, labels, and payload semantics to consumers.

### 2.1 Add PostgreSQL hub adapter [category: code] (depends: P1)
`kind: deliverable`

Targets: `crates/gcore/src/postgres.rs`, `crates/gcore/src/config.rs`

Provide shared PostgreSQL connection helpers and read-only config-store access behind the `postgres` feature gate. `gcode` currently has these at `crates/gcode/src/db.rs` (649 lines) with `resolve_database_url`, `connect_readonly`, `connect_readwrite`, and config-store reads. The shared module extracts the domain-independent parts.

**postgres.rs — connection helpers (feature = "postgres"):**

```rust
use postgres::{Client, NoTls};

/// Connect to the PostgreSQL hub in read-only mode.
///
/// Sets `default_transaction_read_only = on` to guard against accidental writes.
pub fn connect_readonly(database_url: &str) -> anyhow::Result<Client> {
    let mut client = Client::connect(database_url, NoTls)?;
    client.execute("SET default_transaction_read_only = on", &[])?;
    Ok(client)
}

/// Connect to the PostgreSQL hub with write access.
pub fn connect_readwrite(database_url: &str) -> anyhow::Result<Client> {
    Client::connect(database_url, NoTls)
        .map_err(|e| anyhow::anyhow!("PostgreSQL connection failed: {e}"))
}

/// Read a raw config value from the Gobby `config_store` table.
///
/// Returns the raw stored value (may be JSON-encoded). Callers should
/// pipe the result through `config::decode_config_value` to unwrap
/// JSON string encoding, then through their value resolver for
/// `$secret:NAME` and `${VAR}` interpolation.
///
/// Returns `None` for missing keys. Does not write.
pub fn read_config_value(
    conn: &mut Client,
    key: &str,
) -> anyhow::Result<Option<String>> {
    let row = conn
        .query_opt("SELECT value FROM config_store WHERE key = $1", &[&key])?;
    Ok(row.map(|r| r.get(0)))
}

/// Result of a single schema object check (table, index, column, etc.).
#[derive(Debug, Clone)]
pub struct SchemaCheck {
    /// Object name (e.g. "symbols", "bm25_symbols_idx")
    pub object_name: String,
    /// What was checked (e.g. "table exists", "index exists", "column type")
    pub check_kind: String,
    /// Whether the check passed
    pub passed: bool,
    /// Detail on failure (e.g. "table 'symbols' not found")
    pub detail: Option<String>,
}

/// Consumer-supplied schema validator for attached-mode checks.
///
/// The callback receives a mutable connection (required by
/// `postgres::Client::query`) and returns validation results.
/// `gobby-core` runs the callback; it does not know which tables to check.
pub fn validate_schema(
    conn: &mut Client,
    validator: impl FnOnce(&mut Client) -> Vec<SchemaCheck>,
) -> Vec<SchemaCheck> {
    validator(conn)
}
```

Domain crates remain responsible for their own table names, indexes, and standalone creation callbacks. `gobby-core` supplies connection wrappers and config-store reads.

**Acceptance:**

- 2.1.1 - Read-only and read-write connection helpers share consistent error context. file: `crates/gcore/src/postgres.rs`.
- 2.1.2 - `read_config_value` reads raw `config_store` values without write access; callers decode via `config::decode_config_value`. file: `crates/gcore/src/postgres.rs`.
- 2.1.3 - `validate_schema` accepts consumer-supplied validators and never runs its own migrations. test: `crates/gcore/src/postgres.rs::tests::attached_validation_is_non_destructive`.
- 2.1.4 - Domain table names are supplied by consumers, not embedded in `gobby-core`. test: `crates/gcore/src/postgres.rs::tests::schema_validator_is_domain_supplied`.

### 2.2 Add FalkorDB adapter and query safety boundary [category: code] (depends: P1)
`kind: deliverable`

Targets: `crates/gcore/src/falkor.rs`

Provide a shared FalkorDB adapter behind the `falkor` feature gate. `gcode` currently has `FalkorClient` at `crates/gcode/src/falkor.rs` (558 lines) with `from_config`, `query`, and `with_falkor` degradation. The shared adapter extracts the domain-independent connection, query execution, and escaping parts.

The `degradation.rs` module is owned by §1.2; this task consumes `ServiceState` from it but does not modify the file.

**falkor.rs — adapter (feature = "falkor"):**

```rust
use std::collections::HashMap;
use falkordb::{FalkorClientBuilder, FalkorConnectionInfo, SyncGraph};
use serde_json::Value;

use crate::config::FalkorConfig;
use crate::degradation::ServiceState;

pub type Row = HashMap<String, Value>;

/// Blocking FalkorDB graph client.
///
/// Owns a connection to a named graph. Domain crates supply Cypher queries;
/// this adapter handles connection lifecycle and result parsing.
pub struct GraphClient {
    graph: SyncGraph,
}

impl GraphClient {
    pub fn from_config(config: &FalkorConfig) -> anyhow::Result<Self> {
        let password = config.password.as_deref().unwrap_or_default();
        let url = format!(
            "falkor://:{}@{}:{}",
            urlencoding::encode(password),
            config.host,
            config.port,
        );
        let conn_info: FalkorConnectionInfo = url.as_str().try_into()?;
        let client = FalkorClientBuilder::new()
            .with_connection_info(conn_info)
            .build()?;
        Ok(Self {
            graph: client.select_graph(&config.graph_name),
        })
    }

    pub fn query(
        &mut self,
        cypher: &str,
        params: Option<HashMap<String, String>>,
    ) -> anyhow::Result<Vec<Row>> { /* parse FalkorDB result into rows */ }
}

/// Run a closure with a FalkorDB client, with typed degradation.
///
/// Degradation contract:
/// - Config missing (`None`)      → `Ok((default, ServiceState::NotConfigured))`
/// - Connection failure           → `Ok((default, ServiceState::Unreachable{...}))`
/// - Closure returns `Ok(value)`  → `Ok((value, ServiceState::Available))`
/// - Closure returns `Err(e)`     → `Err(e)` (propagated — consumer decides
///                                   whether to degrade or fail)
///
/// This gives consumers explicit control: optional search-boost paths can
/// `.unwrap_or((default, ServiceState::...))`, while hard graph commands
/// (e.g. `gcode callers`) can `?` the error to surface it.
pub fn with_graph<T>(
    config: Option<&FalkorConfig>,
    default: T,
    f: impl FnOnce(&mut GraphClient) -> anyhow::Result<T>,
) -> anyhow::Result<(T, ServiceState)> {
    let Some(cfg) = config else {
        return Ok((default, ServiceState::NotConfigured));
    };
    let mut client = match GraphClient::from_config(cfg) {
        Ok(c) => c,
        Err(e) => {
            return Ok((default, ServiceState::Unreachable {
                message: e.to_string(),
            }));
        }
    };
    let value = f(&mut client)?;
    Ok((value, ServiceState::Available))
}

// --- Escaping helpers (no domain labels) ---

/// Escape a graph label for safe Cypher embedding.
pub fn escape_label(label: &str) -> String { /* backtick-wrap */ }

/// Escape a relationship type for safe Cypher embedding.
pub fn escape_rel_type(rel: &str) -> String { /* backtick-wrap */ }

/// Escape a property key for safe Cypher embedding.
pub fn escape_property(key: &str) -> String { /* backtick-wrap */ }

/// Escape a string parameter value for Cypher.
pub fn escape_string(value: &str) -> String { /* single-quote, escape internal quotes */ }
```

The adapter has no hardcoded code labels (`CodeSymbol`, `CALLS`, `IMPORTS`) or wiki labels (`WikiDoc`, `LINKS_TO`). Domain crates build Cypher with their own labels and call `GraphClient::query`.

**Acceptance:**

- 2.2.1 - `with_graph` returns `Ok((default, ServiceState::NotConfigured))` when config is `None`, `Ok((default, ServiceState::Unreachable))` on connection failure, `Ok((value, ServiceState::Available))` on success, and propagates `Err` from the closure. test: `crates/gcore/src/falkor.rs::tests::with_graph_degradation_contract`.
- 2.2.2 - Escaping helpers cover labels, relation types, property keys, and string parameters. test: `crates/gcore/src/falkor.rs::tests::escapes_graph_tokens`.
- 2.2.3 - The adapter source contains no code-graph or wiki-graph label strings. test: `crates/gcore/src/falkor.rs::tests::no_domain_labels_in_adapter`.
- 2.2.4 - `with_graph` distinguishes `ServiceState::NotConfigured`, `ServiceState::Unreachable`, and `ServiceState::Available` — consumers can differentiate unavailable-service from successful-empty-result. test: `crates/gcore/src/falkor.rs::tests::graph_unavailable_is_not_empty_success`.

### 2.3 Add Qdrant and embedding configuration adapter [category: code] (depends: P1)
`kind: deliverable`

Targets: `crates/gcore/src/qdrant.rs`, `crates/gcore/src/config.rs`

Provide shared Qdrant and embedding configuration primitives behind the `qdrant` feature gate. `gcode` currently resolves these configs inline in `crates/gcode/src/config.rs` and uses them in `crates/gcode/src/search/semantic.rs`.

The `degradation.rs` module is owned by §1.2; this task consumes `ServiceState` from it but does not modify the file.

**Runtime contract:** The adapter uses `reqwest::blocking` for HTTP calls to Qdrant's REST API, matching `gcode`'s existing approach (`crates/gcode/src/search/semantic.rs` lines 22, 76). All functions are synchronous. No Tokio runtime is required. This keeps CLI consumers simple and avoids async/sync boundary confusion. The `qdrant` Cargo feature pulls in `reqwest` (with `blocking` + `json` features), not `qdrant-client` or `tokio`.

**Collection naming and `gcode` migration:** Current `gcode` uses `code_symbols_<project_id>` via `collection_prefix + project_id` concatenation. The shared adapter introduces `CollectionScope` for caller-scoped naming. `gcode` uses `CollectionScope::Custom("code_symbols_<project_id>")` to preserve its existing collection names — no migration required. New consumers like `gwiki` use `CollectionScope::Project` or `CollectionScope::Topic` for canonical scoped naming.

**qdrant.rs — adapter (feature = "qdrant"):**

```rust
use crate::config::{QdrantConfig, EmbeddingConfig};
use crate::degradation::ServiceState;
use serde_json::Value;

/// Scope for a Qdrant collection, allowing caller-controlled naming.
pub enum CollectionScope<'a> {
    /// `{namespace}:project:{id}` — per-project vector store.
    Project(&'a str),
    /// `{namespace}:topic:{name}` — topic-scoped store (e.g. gwiki topics).
    Topic(&'a str),
    /// Arbitrary suffix — preserves legacy naming (e.g. gcode's
    /// `code_symbols_<project_id>`).
    Custom(&'a str),
}

/// Build a collection name from namespace and scope.
///
/// Examples:
///   collection_name("gwiki", CollectionScope::Project("abc-123"))
///       → "gwiki:project:abc-123"
///   collection_name("gwiki", CollectionScope::Topic("rust-async"))
///       → "gwiki:topic:rust-async"
///   collection_name("gcode", CollectionScope::Custom("code_symbols_abc-123"))
///       → "gcode:code_symbols_abc-123"
pub fn collection_name(namespace: &str, scope: CollectionScope<'_>) -> String {
    match scope {
        CollectionScope::Project(id) => format!("{namespace}:project:{id}"),
        CollectionScope::Topic(name) => format!("{namespace}:topic:{name}"),
        CollectionScope::Custom(suffix) => format!("{namespace}:{suffix}"),
    }
}

/// Vector upsert request with opaque domain payload.
pub struct UpsertRequest {
    pub id: String,
    pub vector: Vec<f32>,
    /// Domain-specific payload (code symbols, wiki docs, etc.)
    pub payload: serde_json::Map<String, Value>,
}

/// Vector search request with opaque domain filter.
pub struct SearchRequest {
    pub vector: Vec<f32>,
    pub limit: usize,
    /// Domain-specific filter conditions
    pub filter: Option<Value>,
}

/// Vector search result with score and opaque payload.
pub struct SearchHit {
    pub id: String,
    pub score: f32,
    pub payload: serde_json::Map<String, Value>,
}

/// Execute a vector search via Qdrant REST API (synchronous).
///
/// Uses `reqwest::blocking::Client` to POST to `/collections/{collection}/points/search`.
/// Returns `ServiceState` alongside results for degradation tracking.
pub fn search(
    config: &QdrantConfig,
    collection: &str,
    request: SearchRequest,
) -> anyhow::Result<(Vec<SearchHit>, ServiceState)> {
    let Some(url) = &config.url else {
        return Ok((vec![], ServiceState::NotConfigured));
    };
    let client = reqwest::blocking::Client::builder()
        .timeout(std::time::Duration::from_secs(5))
        .build()?;
    let mut req = client.post(format!(
        "{url}/collections/{collection}/points/search"
    ));
    if let Some(key) = &config.api_key {
        req = req.header("api-key", key);
    }
    // Build search body from request fields
    let body = serde_json::json!({
        "vector": request.vector,
        "limit": request.limit,
        "filter": request.filter,
        "with_payload": true,
    });
    match req.json(&body).send() {
        Ok(resp) if resp.status().is_success() => {
            // Parse response into SearchHit vec
            // (implementation parses Qdrant JSON response format)
            Ok((/* parsed hits */, ServiceState::Available))
        }
        Ok(resp) => Err(anyhow::anyhow!(
            "Qdrant search failed: HTTP {}", resp.status()
        )),
        Err(e) => Ok((vec![], ServiceState::Unreachable {
            message: e.to_string(),
        })),
    }
}

/// Execute a batch vector upsert via Qdrant REST API (synchronous).
pub fn upsert(
    config: &QdrantConfig,
    collection: &str,
    points: Vec<UpsertRequest>,
) -> anyhow::Result<()> { /* PUT /collections/{collection}/points */ }
```

`gobby-core` does not choose model names, embed text, or define code/wiki payload schemas. Embedding is performed by the consumer or a configured embedding API; the adapter handles only the Qdrant client surface.

**Acceptance:**

- 2.3.1 - Qdrant and embedding configs follow the shared env → `config_store` → default resolution order. test: `crates/gcore/src/config.rs::tests::qdrant_and_embedding_resolution_order`.
- 2.3.2 - `collection_name` accepts `CollectionScope::Project`, `CollectionScope::Topic`, and `CollectionScope::Custom` for caller-controlled naming. test: `crates/gcore/src/qdrant.rs::tests::collection_name_covers_all_scopes`.
- 2.3.3 - `UpsertRequest` and `SearchRequest` accept domain payloads without knowing their schema. test: `crates/gcore/src/qdrant.rs::tests::payload_schema_is_opaque`.
- 2.3.4 - Missing Qdrant or embedding API surfaces typed `ServiceState` degradation. test: `crates/gcore/src/degradation.rs::tests::vector_services_degrade_explicitly`.
- 2.3.5 - All Qdrant adapter functions are synchronous (`reqwest::blocking`); no Tokio runtime is required. test: `crates/gcore/src/qdrant.rs::tests::sync_search_from_cli_path`.

## P3: Generic Indexing And Search Primitives
`kind: framing`

**Goal**: share mechanics that are genuinely generic while keeping parsing, graph extraction, and UX in domain crates.

### 3.1 Add generic indexing primitives [category: code] (depends: P2)
`kind: deliverable`

Targets: `crates/gcore/src/indexing.rs`, `crates/gcore/src/lib.rs`

Extract or define generic primitives for file discovery, content hashing, chunk identity, and index event flow behind the `indexing` feature gate. `gcode` currently implements these in `crates/gcode/src/index/` (walker, hasher, chunker, indexer) with code-specific parsing baked in. The shared module extracts the domain-independent parts.

**indexing.rs — generic primitives (feature = "indexing"):**

```rust
use std::path::PathBuf;
use ignore::WalkBuilder;
use sha2::{Sha256, Digest};

/// Walker configuration that consumers can extend with domain-specific rules.
pub struct WalkerSettings {
    pub root: PathBuf,
    pub respect_gitignore: bool,
    pub max_filesize: Option<u64>,
    /// Extra ignore patterns (e.g. "*.pyc", "node_modules/")
    pub extra_ignores: Vec<String>,
}

impl WalkerSettings {
    /// Build an `ignore::WalkBuilder` from these settings.
    pub fn into_walker(self) -> WalkBuilder { /* ... */ }
}

/// SHA-256 content hash for incremental indexing.
pub fn content_hash(data: &[u8]) -> String {
    let mut hasher = Sha256::new();
    hasher.update(data);
    format!("{:x}", hasher.finalize())
}

/// A content chunk with byte range and opaque domain metadata.
pub struct Chunk {
    pub file_path: PathBuf,
    pub byte_start: usize,
    pub byte_end: usize,
    pub heading: Option<String>,
    /// Opaque domain payload (symbol refs, wiki links, etc.)
    pub metadata: serde_json::Value,
}

/// Index lifecycle events for incremental indexing.
pub enum IndexEvent {
    Added(PathBuf),
    Changed(PathBuf),
    Unchanged(PathBuf),
    Deleted(PathBuf),
    Skipped { path: PathBuf, reason: String },
}
```

Language parsing, markdown parsing, symbol extraction, wiki link extraction, and domain write models stay in `gobby-code` or `gobby-wiki`. The generic module provides only the file discovery, hashing, chunking structure, and event vocabulary.

**Acceptance:**

- 3.1.1 - `WalkerSettings` supports consumer extension without code/wiki-specific defaults. file: `crates/gcore/src/indexing.rs`.
- 3.1.2 - `Chunk` carries opaque `serde_json::Value` metadata without domain-specific fields. test: `crates/gcore/src/indexing.rs::tests::chunk_metadata_is_opaque`.
- 3.1.3 - `IndexEvent` distinguishes `Added`, `Changed`, `Unchanged`, `Deleted`, and `Skipped` with reason. test: `crates/gcore/src/indexing.rs::tests::index_events_cover_incremental_cases`.
- 3.1.4 - The indexing module does not depend on tree-sitter or any language grammar crate. test: `crates/gcore/src/indexing.rs::tests::no_domain_parser_dependency`.

### 3.2 Add generic search fusion primitives [category: code] (depends: P2)
`kind: deliverable`

Targets: `crates/gcore/src/search.rs`

Provide reusable search result and fusion primitives behind the `search` feature gate. `gcode` currently has RRF fusion at `crates/gcode/src/search/rrf.rs` (133 lines) as a pure function operating on string IDs. The shared version generalizes this to work for any consumer.

The `degradation.rs` module is owned by §1.2; this task consumes `ServiceState` and `DegradationKind` from it but does not modify the file.

**search.rs — generic fusion (feature = "search"):**

```rust
use std::collections::HashMap;
use serde::{Serialize, Deserialize};
use crate::degradation::ServiceState;

/// RRF constant — matches Python RRF_K in code_index/searcher.py.
const RRF_K: f64 = 60.0;

/// A search result from any source, with opaque identity and metadata.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SearchResult {
    /// Opaque identifier (symbol UUID, doc UUID, chunk ID, etc.)
    pub id: String,
    /// Combined score after fusion
    pub score: f64,
    /// Which sources contributed this result
    pub sources: Vec<String>,
    /// Source-level explanations for debugging
    #[serde(skip_serializing_if = "Vec::is_empty")]
    pub explanations: Vec<SourceExplanation>,
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SourceExplanation {
    pub source: String,
    pub rank: usize,
    pub score: f64,
}

/// Degradation metadata for a search that had unavailable sources.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct SearchDegradation {
    pub unavailable_sources: Vec<String>,
    pub available_sources: Vec<String>,
}

/// Merge multiple ranked lists using Reciprocal Rank Fusion.
///
/// Each source is a `(name, ranked_ids)` pair where index 0 = most relevant.
/// Returns results sorted by combined RRF score descending.
pub fn rrf_merge(
    sources: Vec<(&str, Vec<String>)>,
) -> Vec<SearchResult> {
    let mut entries: HashMap<String, Vec<SourceExplanation>> = HashMap::new();
    for (source_name, ids) in &sources {
        for (rank, id) in ids.iter().enumerate() {
            let score = 1.0 / (RRF_K + rank as f64);
            entries.entry(id.clone()).or_default().push(SourceExplanation {
                source: source_name.to_string(),
                rank,
                score,
            });
        }
    }
    let mut results: Vec<SearchResult> = entries
        .into_iter()
        .map(|(id, explanations)| {
            let score = explanations.iter().map(|e| e.score).sum();
            let sources = explanations.iter().map(|e| e.source.clone()).collect();
            SearchResult { id, score, sources, explanations }
        })
        .collect();
    results.sort_by(|a, b| b.score.partial_cmp(&a.score)
        .unwrap_or(std::cmp::Ordering::Equal)
        .then_with(|| a.id.cmp(&b.id)));
    results
}
```

PostgreSQL query SQL, Qdrant payload filters, graph boost semantics, and user-facing output remain consumer-specific. The shared module provides the fusion algorithm and result types.

**Acceptance:**

- 3.2.1 - `rrf_merge` is available from `gobby_core::search` behind the `search` feature. file: `crates/gcore/src/search.rs`.
- 3.2.2 - `SearchResult` preserves per-source explanations and `SearchDegradation` tracks unavailable sources. test: `crates/gcore/src/search.rs::tests::rrf_preserves_explanations_and_degradation`.
- 3.2.3 - `SearchResult` is `Serialize + Deserialize` without CLI formatting types. test: `crates/gcore/src/search.rs::tests::search_result_is_cli_independent`.
- 3.2.4 - The search module source contains no domain-specific SQL, graph labels, or payload filter code. test: `crates/gcore/src/search.rs::tests::search_core_has_no_domain_queries`.

## VS1: Verification
`kind: verification`

Validation for this plan:

- `uv run gobby plans validate .gobby/plans/gcore-rust-foundation.md`
- `cargo build -p gobby-core --no-default-features`
- `cargo build -p gobby-core --features postgres`
- `cargo build -p gobby-core --features falkor`
- `cargo build -p gobby-core --features qdrant`
- `cargo build -p gobby-core --features indexing`
- `cargo build -p gobby-core --all-features`
- `cargo test -p gobby-core --all-features`
- `cargo clippy -p gobby-core --all-features -- -D warnings`

Integration validation after dependent plans land:

- `cargo build -p gobby-code --no-default-features`
- `cargo build -p gobby-wiki --no-default-features`
- Focused tests proving `gobby-code` and `gobby-wiki` consume shared primitives without moving domain behavior into `gobby-core`.

## AC1: Acceptance Criteria
`kind: verification`

- `gobby-core` exposes shared context/config, setup, datastore, indexing, search, and degradation primitives behind feature gates.
- Baseline `gobby-core` (no features) stays dependency-light and builds without datastore crates.
- Attached mode remains non-destructive to Gobby-owned schema, files, and `config_store`.
- Standalone setup is explicit and scoped to consumer-owned resources.
- `gobby-code` keeps code graph and code-index domain APIs.
- `gobby-wiki` keeps llm-wiki vault UX, wiki domain APIs, and namespaced data ownership.
- FalkorDB and Qdrant absence is represented through typed degradation wherever those services are optional.

## V1 Plan Changelog
`kind: verification`

- **R1 (2026-05-26)**: Created the foundation plan for shared Rust substrate work. Scoped shared primitives to `gobby-core`; kept code graph behavior in `gobby-code` and wiki vault behavior in `gobby-wiki`; defined attached/standalone setup, datastore adapters, generic indexing/search primitives, and shared degradation contracts.
- **R2 (2026-05-26)**: Added Cargo feature-gate strategy to constraints and task 1.1; concrete code examples (struct/trait/function signatures) to all deliverable sections; acknowledged existing `bootstrap.rs`/`project.rs` modules in task 1.2; added `Cargo.toml` as target for 1.1; added `--all-features` build/test to verification; clarified config-store resolution requires `postgres` feature.
- **R3 (2026-05-26)**: Addressed R2 adversary findings F1–F4. (F1) Fixed `with_graph` return type to `anyhow::Result<(T, ServiceState)>` with explicit four-state degradation contract; updated acceptance 2.2.1/2.2.4. (F2) Replaced `collection_name(namespace, id)` with `CollectionScope` enum supporting `Project`, `Topic`, and `Custom` scopes; documented gcode's legacy `code_symbols_` preservation via `Custom`; added acceptance 2.3.2 covering all scopes. (F3) Replaced `qdrant-client` + `tokio` with `reqwest::blocking` matching gcode's existing sync HTTP pattern; documented runtime contract; added acceptance 2.3.5 for sync CLI path. (F4) Added concrete definitions for `ValidationContext`, `ValidationReport`, `SetupContext`, `SetupReport`, `SetupError`, `OwnedObject` in §1.3 and `SchemaCheck` in §2.1. Swept: updated §1.1 Cargo.toml features; fixed §3.3 dependency from `(depends: 3.1, 3.2)` to `(depends: 1.1)` since degradation.rs is always-available and consumed by P1/P2 tasks.
- **R4 (2026-05-26)**: Addressed R3 adversary findings F1–F4. (F1) Moved degradation contract from §3.3/P3 to §1.2/P1 so it precedes all consumers (§1.4, §2.2, §2.3, §3.2); renumbered §1.2→§1.3, §1.3→§1.4; removed `degradation.rs` from §2.2, §2.3, §3.2 targets to prevent multi-agent edits to the same file; §1.4 now depends on both §1.2 and §1.3. (F2) Changed `ValidationContext`/`SetupContext` to use `&'a mut postgres::Client` mutable borrows instead of owned `postgres::Client`; changed validators to `FnMut(&mut ValidationContext<'_>)` and creators to `FnMut(&mut SetupContext<'_>)`; added acceptance items 1.4.5/1.4.6 proving mutable query and DDL execution. (F3) Added `dep:urlencoding` to `falkor` feature in Cargo.toml; added acceptance 1.1.5 for per-feature isolation builds. (F4) Added `decode_config_value` (JSON string unwrapping), `resolve_env_pattern` (`${VAR}`/`${VAR:-default}`), and `ValueResolver` callback type to §1.3; resolution functions accept consumer-supplied resolver for `$secret:NAME` interpolation; documented config value pipeline; updated `read_config_value` docs to reference decode step; added acceptance items 1.3.5/1.3.6/1.3.7. Swept all deliverables for same finding classes: verified no other shared type definitions are consumed before being defined; verified all targets correctly reflect file ownership.
