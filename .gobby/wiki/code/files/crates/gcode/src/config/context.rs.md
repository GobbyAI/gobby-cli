---
title: crates/gcode/src/config/context.rs
type: code_file
provenance:
- file: crates/gcode/src/config/context.rs
  ranges:
  - 26-31
  - '34'
  - '37'
  - 51-53
  - '55'
  - 58-63
  - 65-110
  - 66-73
  - 75-82
  - 84-91
  - 93-100
  - 102-109
  - 112-116
  - 113-115
  - 119-122
  - 124-134
  - 125-133
  - '136'
  - 138-146
  - 139-145
  - 150-173
  - 176-185
  - 188-191
  - 194-201
  - 204-211
  - 213-317
  - 215-217
  - 219-284
  - 292-316
  - 319-372
  - 374-439
  - 441-449
  - 451-459
  - 461-469
  - 471-502
  - 504-511
  - 516-540
  - 542-544
  - 552-555
  - 557-593
  - 602-626
  - 628-634
  - 643-645
  - 647-655
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/context.rs

Module: [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]

## Purpose

`crates/gcode/src/config/context.rs` exposes 44 indexed API symbols.
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]
[crates/gcode/src/config/context.rs:51-53]
[crates/gcode/src/config/context.rs:55]

## API Symbols

- `FalkorConfig` (class) component `FalkorConfig [class]` (`53926106-6dfb-54e8-98e8-fba4322e5dec`) lines 26-31 [crates/gcode/src/config/context.rs:26-31]
  - Signature: `pub struct FalkorConfig {`
  - Purpose: `FalkorConfig` is a Rust configuration struct that stores the Falkor graph database endpoint (`host`, `port`), optional authentication `password`, and target `graph_name`. [crates/gcode/src/config/context.rs:26-31]
- `QdrantConfig` (type) component `QdrantConfig [type]` (`64da5dd7-9a46-54c3-856e-22934520004d`) lines 34-34 [crates/gcode/src/config/context.rs:34]
  - Signature: `pub type QdrantConfig = gobby_core::config::QdrantConfig;`
  - Purpose: Indexed type `QdrantConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:34]
- `EmbeddingConfig` (type) component `EmbeddingConfig [type]` (`fa989081-e16b-5255-84da-f2e8958ca42c`) lines 37-37 [crates/gcode/src/config/context.rs:37]
  - Signature: `pub type EmbeddingConfig = gobby_core::config::EmbeddingConfig;`
  - Purpose: Indexed type `EmbeddingConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:37]
- `CodeVectorSettings` (class) component `CodeVectorSettings [class]` (`3c239d5c-acad-5519-8278-7872a54e5164`) lines 51-53 [crates/gcode/src/config/context.rs:51-53]
  - Signature: `pub struct CodeVectorSettings {`
  - Purpose: `CodeVectorSettings` is a configuration struct that optionally specifies the embedding/vector dimensionality for code vectors via `vector_dim: Option<usize>`. [crates/gcode/src/config/context.rs:51-53]
- `IndexingSettings` (type) component `IndexingSettings [type]` (`375d916b-30e4-55bb-9471-2f963f005197`) lines 55-55 [crates/gcode/src/config/context.rs:55]
  - Signature: `pub type IndexingSettings = gobby_core::config::IndexingConfig;`
  - Purpose: Indexed type `IndexingSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:55]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`8627d53f-73ba-53a7-8e99-16b027b0b43a`) lines 58-63 [crates/gcode/src/config/context.rs:58-63]
  - Signature: `pub struct ServiceConfigSelection {`
  - Purpose: `ServiceConfigSelection` is a Rust struct of four boolean feature flags that selects whether FalkorDB, Qdrant, embedding, and code-vector services are enabled. [crates/gcode/src/config/context.rs:58-63]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`029d25d6-a9f9-55ef-9799-f9ebd8327d6d`) lines 65-110 [crates/gcode/src/config/context.rs:65-110]
  - Signature: `impl ServiceConfigSelection {`
  - Purpose: `ServiceConfigSelection` is a Rust configuration helper that exposes `const` preset constructors for toggling the `falkordb`, `qdrant`, `embedding`, and `code_vectors` service flags in predefined combinations (`all`, `database_only`, `falkordb_only`, `vectors`, and `hybrid_search`). [crates/gcode/src/config/context.rs:65-110]
- `ServiceConfigSelection.all` (method) component `ServiceConfigSelection.all [method]` (`c9a1cb62-7c8b-5590-91d0-babf0631b4b8`) lines 66-73 [crates/gcode/src/config/context.rs:66-73]
  - Signature: `pub const fn all() -> Self {`
  - Purpose: Returns a `Self` instance with all four flags (`falkordb`, `qdrant`, `embedding`, and `code_vectors`) set to `true` at compile time. [crates/gcode/src/config/context.rs:66-73]
- `ServiceConfigSelection.database_only` (method) component `ServiceConfigSelection.database_only [method]` (`b42e3e41-716a-5888-9afa-b816f1a85ee2`) lines 75-82 [crates/gcode/src/config/context.rs:75-82]
  - Signature: `pub const fn database_only() -> Self {`
  - Purpose: `database_only()` returns a configuration instance with all optional components disabled by setting `falkordb`, `qdrant`, `embedding`, and `code_vectors` to `false`. [crates/gcode/src/config/context.rs:75-82]
- `ServiceConfigSelection.falkordb_only` (method) component `ServiceConfigSelection.falkordb_only [method]` (`41215555-256a-53a5-8d44-c0787823aade`) lines 84-91 [crates/gcode/src/config/context.rs:84-91]
  - Signature: `pub const fn falkordb_only() -> Self {`
  - Purpose: Returns a `Self` instance configured to enable only `falkordb` while disabling `qdrant`, `embedding`, and `code_vectors`. [crates/gcode/src/config/context.rs:84-91]
- `ServiceConfigSelection.vectors` (method) component `ServiceConfigSelection.vectors [method]` (`a4c1f2d9-c41a-5cc3-98b1-e00f4ab47425`) lines 93-100 [crates/gcode/src/config/context.rs:93-100]
  - Signature: `pub const fn vectors() -> Self {`
  - Purpose: Constructs and returns a `Self` value configured for vector support by setting `falkordb` to `false` and `qdrant`, `embedding`, and `code_vectors` to `true`. [crates/gcode/src/config/context.rs:93-100]
- `ServiceConfigSelection.hybrid_search` (method) component `ServiceConfigSelection.hybrid_search [method]` (`5b7522d5-3026-5c24-8928-ec469fc6df71`) lines 102-109 [crates/gcode/src/config/context.rs:102-109]
  - Signature: `pub const fn hybrid_search() -> Self {`
  - Purpose: `hybrid_search()` is a `const` constructor that returns a `Self` configuration with `falkordb`, `qdrant`, and `embedding` enabled, while leaving `code_vectors` disabled. [crates/gcode/src/config/context.rs:102-109]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`dd4f67d9-d274-5a58-a881-bd28e73acd40`) lines 112-116 [crates/gcode/src/config/context.rs:112-116]
  - Signature: `impl Default for ServiceConfigSelection {`
  - Purpose: `ServiceConfigSelection` implements `Default` by delegating `default()` to `Self::all()`, so the default value represents the complete selection of service configurations. [crates/gcode/src/config/context.rs:112-116]
- `ServiceConfigSelection.default` (method) component `ServiceConfigSelection.default [method]` (`a4e17f61-3949-5078-9372-85c6c48ce886`) lines 113-115 [crates/gcode/src/config/context.rs:113-115]
  - Signature: `fn default() -> Self {`
  - Purpose: `default` constructs the type’s default value by delegating to `Self::all()`, returning the full/all-inclusive instance. [crates/gcode/src/config/context.rs:113-115]
- `CodeVectorConfigError` (type) component `CodeVectorConfigError [type]` (`af12f40d-1d4d-5085-9f4f-7290f4a41fce`) lines 119-122 [crates/gcode/src/config/context.rs:119-122]
  - Signature: `pub enum CodeVectorConfigError {`
  - Purpose: Indexed type `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:119-122]
- `CodeVectorConfigError` (class) component `CodeVectorConfigError [class]` (`0e37688d-ceb6-5676-8dbd-7221a7970f7b`) lines 124-134 [crates/gcode/src/config/context.rs:124-134]
  - Signature: `impl fmt::Display for CodeVectorConfigError {`
  - Purpose: `CodeVectorConfigError`’s `Display` implementation renders either a validation error for a non-positive code vector dimension or a config-read failure, including the underlying source error and offending value where applicable. [crates/gcode/src/config/context.rs:124-134]
- `CodeVectorConfigError.fmt` (method) component `CodeVectorConfigError.fmt [method]` (`6da2a5dd-5190-5e5b-918d-782ba3edb87e`) lines 125-133 [crates/gcode/src/config/context.rs:125-133]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Formats the enum as a human-readable error message by matching on `InvalidVectorDim` and `Read` and writing the corresponding variant-specific string, including embedded `source` and `value` details where applicable. [crates/gcode/src/config/context.rs:125-133]
- `CodeVectorConfigError` (class) component `CodeVectorConfigError [class]` (`19890a79-3fe2-53d9-8d1f-f9123bb32ec5`) lines 136-136 [crates/gcode/src/config/context.rs:136]
  - Signature: `impl std::error::Error for CodeVectorConfigError {}`
  - Purpose: `CodeVectorConfigError` is a Rust error type that implements `std::error::Error`, indicating it serves as a standard error value for code vector configuration failures. [crates/gcode/src/config/context.rs:136]
- `FalkorConfig` (class) component `FalkorConfig [class]` (`552aaab0-c0e5-52e0-b933-b3dc69d52831`) lines 138-146 [crates/gcode/src/config/context.rs:138-146]
  - Signature: `impl FalkorConfig {`
  - Purpose: `FalkorConfig` is a thin adapter that exposes `connection_config()`, constructing a `gobby_core::config::FalkorConfig` by cloning `host` and `password` and copying `port` from `self`. [crates/gcode/src/config/context.rs:138-146]
- `FalkorConfig.connection_config` (method) component `FalkorConfig.connection_config [method]` (`1a50772c-a7b4-53dd-8641-b7664ce043f8`) lines 139-145 [crates/gcode/src/config/context.rs:139-145]
  - Signature: `pub fn connection_config(&self) -> gobby_core::config::FalkorConfig {`
  - Purpose: Returns a `gobby_core::config::FalkorConfig` populated from `self` by cloning `host` and `password` and copying `port`. [crates/gcode/src/config/context.rs:139-145]
- `Context` (class) component `Context [class]` (`7032577f-b11e-5c5d-abab-db0b71de4cdd`) lines 150-173 [crates/gcode/src/config/context.rs:150-173]
  - Signature: `pub struct Context {`
  - Purpose: `Context` is a project-scoped configuration bundle that carries the database DSN, project root/ID, daemon URL, and optional FalkorDB/Qdrant/embedding settings plus code-vector and indexing parameters used to drive indexing and search behavior. [crates/gcode/src/config/context.rs:150-173]
- `ProjectIndexScope` (type) component `ProjectIndexScope [type]` (`46d8d301-b9e3-5346-9c0e-28f3b7dda935`) lines 176-185 [crates/gcode/src/config/context.rs:176-185]
  - Signature: `pub enum ProjectIndexScope {`
  - Purpose: Indexed type `ProjectIndexScope` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:176-185]
- `MissingIdentity` (type) component `MissingIdentity [type]` (`cc6ed12b-94b2-53a7-bbfe-eeada184d113`) lines 188-191 [crates/gcode/src/config/context.rs:188-191]
  - Signature: `pub enum MissingIdentity {`
  - Purpose: Indexed type `MissingIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:188-191]
- `ProjectIdentitySource` (type) component `ProjectIdentitySource [type]` (`90458d54-1a28-5701-9b35-d51a64d8ab85`) lines 194-201 [crates/gcode/src/config/context.rs:194-201]
  - Signature: `pub enum ProjectIdentitySource {`
  - Purpose: Indexed type `ProjectIdentitySource` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:194-201]
- `ProjectIdentity` (class) component `ProjectIdentity [class]` (`c47ec3db-5553-5238-823a-156d04d3a0f6`) lines 204-211 [crates/gcode/src/config/context.rs:204-211]
  - Signature: `pub struct ProjectIdentity {`
  - Purpose: `ProjectIdentity` is a Rust data structure that encapsulates a project’s identity and indexing metadata, including its stable `project_id`, filesystem `root`, provenance `source`, optional `warning`, `should_write_gcode_json` flag, and `index_scope`. [crates/gcode/src/config/context.rs:204-211]
- `Context` (class) component `Context [class]` (`df0b5059-b1bc-50e0-b6d6-7bc99f0b4fe5`) lines 213-317 [crates/gcode/src/config/context.rs:213-317]
  - Signature: `impl Context {`
  - Purpose: `Context` resolves and validates the current project’s runtime state by canonicalizing or locating the project root, loading its identity and index scope, and conditionally assembling service configuration from the database/config store. [crates/gcode/src/config/context.rs:213-317]
- `Context.resolve` (method) component `Context.resolve [method]` (`3228ad40-0817-52f7-88a9-afca5418ea28`) lines 215-217 [crates/gcode/src/config/context.rs:215-217]
  - Signature: `pub fn resolve(project_override: Option<&str>, quiet: bool) -> anyhow::Result<Self> {`
  - Purpose: It resolves and returns a `Self` by delegating to `Self::resolve_with_services(project_override, quiet, ServiceConfigSelection::all())`, using the optional project override and quiet flag with all service configurations enabled. [crates/gcode/src/config/context.rs:215-217]
- `Context.resolve_with_services` (method) component `Context.resolve_with_services [method]` (`a2db489f-4ae5-57c7-8ed2-d96c19b2e3e1`) lines 219-284 [crates/gcode/src/config/context.rs:219-284]
  - Signature: `pub fn resolve_with_services(`
  - Purpose: It resolves the project root from an override or auto-detection, loads and validates the project identity and database-backed settings, and constructs `Self` by conditionally resolving only the requested service configurations from the database plus optional standalone config. [crates/gcode/src/config/context.rs:219-284]
- `Context.resolve_for_project_id` (method) component `Context.resolve_for_project_id [method]` (`342481bd-9542-5f02-a1b9-ff15ad6c82d5`) lines 292-316 [crates/gcode/src/config/context.rs:292-316]
  - Signature: `pub fn resolve_for_project_id(project_id: &str, quiet: bool) -> anyhow::Result<Self> {`
  - Purpose: It normalizes the supplied `project_id`, resolves the database URL, opens a read-only database connection to derive FalkorDB and indexing settings from the optional standalone config, resolves the daemon URL, and returns a `Self` initialized for `ProjectIndexScope::Single` with default code-vector settings and no `qdrant` or `embedding` client. [crates/gcode/src/config/context.rs:292-316]
- `resolve_project_identity` (function) component `resolve_project_identity [function]` (`3597452f-13b4-5430-a083-abb2c3094c3e`) lines 319-372 [crates/gcode/src/config/context.rs:319-372]
  - Signature: `pub fn resolve_project_identity(`
  - Purpose: `resolve_project_identity` canonicalizes the project root, reads any `.gobby/project.json` isolation marker, rejects markers that set only one of `parent_project_path` or `parent_project_id`, and then resolves the project as a non-isolated identity, an isolated overlay with parent scope, or an isolated root identity depending on whether the marker is self-referential and whether parent metadata is present. [crates/gcode/src/config/context.rs:319-372]
- `resolve_non_isolated_project_identity` (function) component `resolve_non_isolated_project_identity [function]` (`b2e5d850-372b-5ef6-adec-3577f415052a`) lines 374-439 [crates/gcode/src/config/context.rs:374-439]
  - Signature: `fn resolve_non_isolated_project_identity(`
  - Purpose: This function determines a non-isolated project's `ProjectIdentity` by preferring the top-level code-index ID for linked git worktrees (warning if a copied `.gobby/project.json` ID disagrees), otherwise reading `.gobby/project.json` or `.gobby/gcode.json`, and then falling back to the `missing` policy when no identity file exists. [crates/gcode/src/config/context.rs:374-439]
- `is_self_referential_isolation_marker` (function) component `is_self_referential_isolation_marker [function]` (`f3a344ec-05f7-5986-9254-ab959faeda53`) lines 441-449 [crates/gcode/src/config/context.rs:441-449]
  - Signature: `fn is_self_referential_isolation_marker(`
  - Purpose: Returns `true` only when the marker has a `parent_project_path` and resolving that path against `root` points back to `root`, indicating the isolation marker is self-referential. [crates/gcode/src/config/context.rs:441-449]
- `resolve_parent_project_root` (function) component `resolve_parent_project_root [function]` (`7ba2a606-b5eb-57ba-bab2-097c58f768a8`) lines 451-459 [crates/gcode/src/config/context.rs:451-459]
  - Signature: `fn resolve_parent_project_root(root: &Path, parent_project_path: &str) -> PathBuf {`
  - Purpose: Returns the absolute path to a parent project by treating `parent_project_path` as relative to `root` when needed, then canonicalizing it and falling back to the non-canonicalized path if canonicalization fails. [crates/gcode/src/config/context.rs:451-459]
- `normalize_project_id` (function) component `normalize_project_id [function]` (`477a0067-214d-5666-87df-d3dfbf362830`) lines 461-469 [crates/gcode/src/config/context.rs:461-469]
  - Signature: `fn normalize_project_id(project_id: &str) -> anyhow::Result<String> {`
  - Purpose: Trims `project_id`, rejects an empty value, and returns the canonical UUID string if `Uuid::parse_str` succeeds, otherwise propagating an `anyhow` error with context that `--project-id` must be a UUID. [crates/gcode/src/config/context.rs:461-469]
- `validate_parent_code_index` (function) component `validate_parent_code_index [function]` (`01ab95bd-a9dd-5723-a320-4047d3d2c44f`) lines 471-502 [crates/gcode/src/config/context.rs:471-502]
  - Signature: `pub(crate) fn validate_parent_code_index(`
  - Purpose: If `scope` is an `Overlay`, this function checks whether `code_indexed_files` contains at least one row for `parent_project_id` and returns an error naming `parent_root` and the short project ID if none exist; otherwise it is a no-op. [crates/gcode/src/config/context.rs:471-502]
- `warn_project_identity` (function) component `warn_project_identity [function]` (`5a2f2657-4867-5a29-bbf2-b269582568df`) lines 504-511 [crates/gcode/src/config/context.rs:504-511]
  - Signature: `pub fn warn_project_identity(identity: &ProjectIdentity, quiet: bool) {`
  - Purpose: Returns immediately when `quiet` is `true`; otherwise, if `identity.warning` is `Some`, it writes `Warning: {warning}` to stderr. [crates/gcode/src/config/context.rs:504-511]
- `resolve_project_by_name` (function) component `resolve_project_by_name [function]` (`0d9013c4-b309-5bbb-ac01-4cde99959f6a`) lines 516-540 [crates/gcode/src/config/context.rs:516-540]
  - Signature: `fn resolve_project_by_name(name: &str, database_url: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: `resolve_project_by_name` opens a read-only database connection, queries `code_indexed_projects` for a `root_path` matching the given name exactly or as a trailing path suffix with either slash style, returns the first matching path that exists as a directory, and otherwise raises an error instructing the user to run `gcode projects`. [crates/gcode/src/config/context.rs:516-540]
- `project_name_suffixes` (function) component `project_name_suffixes [function]` (`672c2525-2537-58eb-99cc-e7f345240dab`) lines 542-544 [crates/gcode/src/config/context.rs:542-544]
  - Signature: `pub(super) fn project_name_suffixes(name: &str) -> (String, String) {`
  - Purpose: Returns a pair of `String`s containing the project name prefixed as a Unix-style suffix (`"/{name}"`) and a Windows-style suffix (`"\\{name}"`). [crates/gcode/src/config/context.rs:542-544]
- `detect_project_root` (function) component `detect_project_root [function]` (`a86f8ebd-bdc8-5c7b-9b9f-8682681a3f89`) lines 552-555 [crates/gcode/src/config/context.rs:552-555]
  - Signature: `pub fn detect_project_root() -> anyhow::Result<PathBuf> {`
  - Purpose: Returns the current process working directory as a `PathBuf` and delegates to `detect_project_root_from` to resolve the project root from that path. [crates/gcode/src/config/context.rs:552-555]
- `detect_project_root_from` (function) component `detect_project_root_from [function]` (`83c15d6b-b0b1-532a-9659-4524925af101`) lines 557-593 [crates/gcode/src/config/context.rs:557-593]
  - Signature: `pub fn detect_project_root_from(start: &Path) -> anyhow::Result<PathBuf> {`
  - Purpose: Resolves `start` to an absolute directory path, then returns the first matching project root by preferring a `.gobby/project.json` or `.gobby/gcode.json` identity file, otherwise the Git worktree top-level, otherwise the nearest ancestor containing `.git` or `.hg`, and finally `start` itself as a last resort. [crates/gcode/src/config/context.rs:557-593]
- `resolve_daemon_url` (function) component `resolve_daemon_url [function]` (`856ab946-1671-5244-891d-7aa3fe2a358d`) lines 602-626 [crates/gcode/src/config/context.rs:602-626]
  - Signature: `pub(crate) fn resolve_daemon_url() -> Option<String> {`
  - Purpose: It resolves the daemon URL by preferring a non-empty `GOBBY_PORT` environment override, then `bootstrap.yaml`’s `daemon_port` plus optional `bind_host` normalized through `client_daemon_host`, and otherwise falling back to `http://localhost:60887` (so it effectively always returns `Some`). [crates/gcode/src/config/context.rs:602-626]
- `client_daemon_host` (function) component `client_daemon_host [function]` (`07633b2b-d79d-54b3-bf65-63691bead465`) lines 628-634 [crates/gcode/src/config/context.rs:628-634]
  - Signature: `fn client_daemon_host(host: &str) -> String {`
  - Purpose: It trims the input host, maps empty or unspecified addresses (`""`, `0.0.0.0`, `::`, `[::]`) to `localhost`, brackets any unbracketed colon-containing host as an IPv6 literal, and otherwise returns the trimmed host unchanged. [crates/gcode/src/config/context.rs:628-634]
- `resolve_project_id` (function) component `resolve_project_id [function]` (`52463b27-8c45-5e92-86c1-b72dc4c2a023`) lines 643-645 [crates/gcode/src/config/context.rs:643-645]
  - Signature: `pub(super) fn resolve_project_id(project_root: &Path) -> anyhow::Result<String> {`
  - Purpose: Resolves the project identity for `project_root` with `MissingIdentity::Error` and returns its `project_id`, propagating any failure as `anyhow::Result<String>`. [crates/gcode/src/config/context.rs:643-645]
- `absolute_fallback` (function) component `absolute_fallback [function]` (`89872601-7281-53c4-982e-90201bb58a01`) lines 647-655 [crates/gcode/src/config/context.rs:647-655]
  - Signature: `fn absolute_fallback(path: &Path) -> PathBuf {`
  - Purpose: Returns `path` unchanged if it is already absolute; otherwise it resolves the relative path against `std::env::current_dir()` and falls back to `std::env::temp_dir()` if the current directory cannot be obtained, returning the joined `PathBuf`. [crates/gcode/src/config/context.rs:647-655]

