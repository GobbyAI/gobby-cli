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
  - 65-128
  - 130-134
  - 137-140
  - 142-152
  - '154'
  - 156-164
  - 168-191
  - 194-203
  - 206-209
  - 212-219
  - 222-229
  - 231-335
  - 337-390
  - 392-446
  - 448-456
  - 458-466
  - 468-476
  - 478-509
  - 511-518
  - 523-547
  - 549-551
  - 559-562
  - 564-600
  - 609-611
  - 613-621
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/context.rs

Module: [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]

## Purpose

Configuration resolution for `gcode`: it defines the service and indexing config types used to load FalkorDB, Qdrant, embedding, and code-vector settings from bootstrap/database/config-store sources, then combines them into a runtime `Context`. `ServiceConfigSelection` provides preset feature combinations for selectively enabling config groups, while `FalkorConfig`, `CodeVectorSettings`, and the related error type adapt and validate individual settings. The rest of the file resolves project identity and project roots from CLI, filesystem, Git, and `.gobby` metadata, validates overlay parents, and exposes helpers for name lookup, ID normalization, and absolute-path fallback so `Context` can be assembled consistently.
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]
[crates/gcode/src/config/context.rs:51-53]
[crates/gcode/src/config/context.rs:55]

## API Symbols

- `FalkorConfig` (class) component `FalkorConfig [class]` (`53926106-6dfb-54e8-98e8-fba4322e5dec`) lines 26-31 [crates/gcode/src/config/context.rs:26-31]
  - Signature: `pub struct FalkorConfig {`
  - Purpose: 'FalkorConfig' is a configuration struct that stores the FalkorDB connection endpoint ('host', 'port'), optional authentication credential ('password'), and target graph identifier ('graph_name'). [crates/gcode/src/config/context.rs:26-31]
- `QdrantConfig` (type) component `QdrantConfig [type]` (`64da5dd7-9a46-54c3-856e-22934520004d`) lines 34-34 [crates/gcode/src/config/context.rs:34]
  - Signature: `pub type QdrantConfig = gobby_core::config::QdrantConfig;`
  - Purpose: Indexed type `QdrantConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:34]
- `EmbeddingConfig` (type) component `EmbeddingConfig [type]` (`fa989081-e16b-5255-84da-f2e8958ca42c`) lines 37-37 [crates/gcode/src/config/context.rs:37]
  - Signature: `pub type EmbeddingConfig = gobby_core::config::EmbeddingConfig;`
  - Purpose: Indexed type `EmbeddingConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:37]
- `CodeVectorSettings` (class) component `CodeVectorSettings [class]` (`3c239d5c-acad-5519-8278-7872a54e5164`) lines 51-53 [crates/gcode/src/config/context.rs:51-53]
  - Signature: `pub struct CodeVectorSettings {`
  - Purpose: 'CodeVectorSettings' is a Rust configuration struct that optionally specifies the dimensionality of a code vector via 'vector_dim: Option<usize>'. [crates/gcode/src/config/context.rs:51-53]
- `IndexingSettings` (type) component `IndexingSettings [type]` (`375d916b-30e4-55bb-9471-2f963f005197`) lines 55-55 [crates/gcode/src/config/context.rs:55]
  - Signature: `pub type IndexingSettings = gobby_core::config::IndexingConfig;`
  - Purpose: Indexed type `IndexingSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:55]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`8627d53f-73ba-53a7-8e99-16b027b0b43a`) lines 58-63 [crates/gcode/src/config/context.rs:58-63]
  - Signature: `pub struct ServiceConfigSelection {`
  - Purpose: 'ServiceConfigSelection' is a boolean feature-selection struct that indicates whether 'falkordb', 'qdrant', 'embedding', and 'code_vectors' service configurations are enabled. [crates/gcode/src/config/context.rs:58-63]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`029d25d6-a9f9-55ef-9799-f9ebd8327d6d`) lines 65-128 [crates/gcode/src/config/context.rs:65-128]
  - Signature: `impl ServiceConfigSelection {`
  - Purpose: 'ServiceConfigSelection' is a small configuration selector with 'const fn' constructors that return predefined boolean feature combinations for enabling or disabling 'falkordb', 'qdrant', 'embedding', and 'code_vectors' services. [crates/gcode/src/config/context.rs:65-128]
- `ServiceConfigSelection.all` (method) component `ServiceConfigSelection.all [method]` (`c9a1cb62-7c8b-5590-91d0-babf0631b4b8`) lines 66-73 [crates/gcode/src/config/context.rs:66-73]
  - Signature: `pub const fn all() -> Self {`
  - Purpose: Returns a 'Self' value with all feature flags enabled by setting 'falkordb', 'qdrant', 'embedding', and 'code_vectors' to 'true'. [crates/gcode/src/config/context.rs:66-73]
- `ServiceConfigSelection.database_only` (method) component `ServiceConfigSelection.database_only [method]` (`b42e3e41-716a-5888-9afa-b816f1a85ee2`) lines 75-82 [crates/gcode/src/config/context.rs:75-82]
  - Signature: `pub const fn database_only() -> Self {`
  - Purpose: Returns a 'Self' configuration with all database-related features disabled by setting 'falkordb', 'qdrant', 'embedding', and 'code_vectors' to 'false'. [crates/gcode/src/config/context.rs:75-82]
- `ServiceConfigSelection.falkordb_only` (method) component `ServiceConfigSelection.falkordb_only [method]` (`41215555-256a-53a5-8d44-c0787823aade`) lines 84-91 [crates/gcode/src/config/context.rs:84-91]
  - Signature: `pub const fn falkordb_only() -> Self {`
  - Purpose: Returns a configuration instance with 'falkordb' enabled and 'qdrant', 'embedding', and 'code_vectors' disabled. [crates/gcode/src/config/context.rs:84-91]
- `ServiceConfigSelection.qdrant_only` (method) component `ServiceConfigSelection.qdrant_only [method]` (`d44cbbc0-04e9-56bf-91ba-8ba562319e21`) lines 93-100 [crates/gcode/src/config/context.rs:93-100]
  - Signature: `pub const fn qdrant_only() -> Self {`
  - Purpose: Constructs and returns a 'Self' value configured with only 'qdrant' enabled, while 'falkordb', 'embedding', and 'code_vectors' are all set to 'false'. [crates/gcode/src/config/context.rs:93-100]
- `ServiceConfigSelection.projection_cleanup` (method) component `ServiceConfigSelection.projection_cleanup [method]` (`3349fe55-9b04-504a-a9e7-3bdfb5e169b9`) lines 102-109 [crates/gcode/src/config/context.rs:102-109]
  - Signature: `pub const fn projection_cleanup() -> Self {`
  - Purpose: 'projection_cleanup' is a 'const fn' constructor that returns 'Self' with 'falkordb' and 'qdrant' enabled and 'embedding' and 'code_vectors' disabled. [crates/gcode/src/config/context.rs:102-109]
- `ServiceConfigSelection.vectors` (method) component `ServiceConfigSelection.vectors [method]` (`03212a41-cc6c-5713-b627-83a209fc66e2`) lines 111-118 [crates/gcode/src/config/context.rs:111-118]
  - Signature: `pub const fn vectors() -> Self {`
  - Purpose: Returns a 'Self' value with 'falkordb' disabled and the 'qdrant', 'embedding', and 'code_vectors' feature flags enabled. [crates/gcode/src/config/context.rs:111-118]
- `ServiceConfigSelection.hybrid_search` (method) component `ServiceConfigSelection.hybrid_search [method]` (`d131f6ff-2354-5288-bd28-36e855c70efe`) lines 120-127 [crates/gcode/src/config/context.rs:120-127]
  - Signature: `pub const fn hybrid_search() -> Self {`
  - Purpose: 'hybrid_search' is a 'const' constructor that returns a 'Self' instance configured with 'falkordb', 'qdrant', and 'embedding' enabled while 'code_vectors' is disabled. [crates/gcode/src/config/context.rs:120-127]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`b5535775-36d5-51ed-bb74-2a52131f014d`) lines 130-134 [crates/gcode/src/config/context.rs:130-134]
  - Signature: `impl Default for ServiceConfigSelection {`
  - Purpose: 'ServiceConfigSelection' implements 'Default' by returning 'Self::all()', so the default value selects all service configurations. [crates/gcode/src/config/context.rs:130-134]
- `ServiceConfigSelection.default` (method) component `ServiceConfigSelection.default [method]` (`308f7c78-476f-5d36-850a-328dc71dc624`) lines 131-133 [crates/gcode/src/config/context.rs:131-133]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns 'Self::all()', constructing the default value as the complete/all-inclusive instance of the type. [crates/gcode/src/config/context.rs:131-133]
- `CodeVectorConfigError` (type) component `CodeVectorConfigError [type]` (`3d9e9087-b154-567a-8eb9-dad0ec7045f5`) lines 137-140 [crates/gcode/src/config/context.rs:137-140]
  - Signature: `pub enum CodeVectorConfigError {`
  - Purpose: Indexed type `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:137-140]
- `CodeVectorConfigError` (class) component `CodeVectorConfigError [class]` (`302c98c3-e822-5869-af5b-11a58358b9e8`) lines 142-152 [crates/gcode/src/config/context.rs:142-152]
  - Signature: `impl fmt::Display for CodeVectorConfigError {`
  - Purpose: 'CodeVectorConfigError' is a displayable error type that renders either an invalid code vector dimension as a positive-integer validation failure with its source and value, or a configuration-read failure with the underlying source error. [crates/gcode/src/config/context.rs:142-152]
- `CodeVectorConfigError.fmt` (method) component `CodeVectorConfigError.fmt [method]` (`c28ef263-af5a-5965-8ea5-195137ce9fb8`) lines 143-151 [crates/gcode/src/config/context.rs:143-151]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Formats the enum as a user-facing error message, emitting either an invalid vector dimension message with the source and value or a failed-to-read-config message with the source. [crates/gcode/src/config/context.rs:143-151]
- `CodeVectorConfigError` (class) component `CodeVectorConfigError [class]` (`22983480-0fe3-5146-94ff-d38f0fd5232b`) lines 154-154 [crates/gcode/src/config/context.rs:154]
  - Signature: `impl std::error::Error for CodeVectorConfigError {}`
  - Purpose: 'CodeVectorConfigError' is a Rust error type representing failures related to code vector configuration, exposed as a standard 'std::error::Error' implementation. [crates/gcode/src/config/context.rs:154]
- `FalkorConfig` (class) component `FalkorConfig [class]` (`7421db62-9042-544c-8a54-78e90e700f95`) lines 156-164 [crates/gcode/src/config/context.rs:156-164]
  - Signature: `impl FalkorConfig {`
  - Purpose: 'FalkorConfig' is a Rust configuration wrapper that converts its local 'host', 'port', and 'password' fields into a 'gobby_core::config::FalkorConfig' via 'connection_config()'. [crates/gcode/src/config/context.rs:156-164]
- `FalkorConfig.connection_config` (method) component `FalkorConfig.connection_config [method]` (`e024baa0-26a9-57fd-8f01-3454080ca15f`) lines 157-163 [crates/gcode/src/config/context.rs:157-163]
  - Signature: `pub fn connection_config(&self) -> gobby_core::config::FalkorConfig {`
  - Purpose: Returns a 'gobby_core::config::FalkorConfig' by cloning 'self.host' and 'self.password' and copying 'self.port' into the corresponding connection fields. [crates/gcode/src/config/context.rs:157-163]
- `Context` (class) component `Context [class]` (`f57e9fb3-ef45-5bc0-8ec7-a20ecf40b698`) lines 168-191 [crates/gcode/src/config/context.rs:168-191]
  - Signature: `pub struct Context {`
  - Purpose: 'Context' is a configuration struct that aggregates project identity, filesystem and database connection details, optional FalkorDB/Qdrant/embedding settings, code-vector and indexing options, daemon endpoint, and index scope for the application. [crates/gcode/src/config/context.rs:168-191]
- `ProjectIndexScope` (type) component `ProjectIndexScope [type]` (`7a5353d3-da7f-5160-9017-b32e9548aab8`) lines 194-203 [crates/gcode/src/config/context.rs:194-203]
  - Signature: `pub enum ProjectIndexScope {`
  - Purpose: Indexed type `ProjectIndexScope` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:194-203]
- `MissingIdentity` (type) component `MissingIdentity [type]` (`d0fce310-84e4-5d23-bbaa-1e8dc55ac538`) lines 206-209 [crates/gcode/src/config/context.rs:206-209]
  - Signature: `pub enum MissingIdentity {`
  - Purpose: Indexed type `MissingIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:206-209]
- `ProjectIdentitySource` (type) component `ProjectIdentitySource [type]` (`bff5f934-378e-5722-a8c7-aa3e45ab5c5f`) lines 212-219 [crates/gcode/src/config/context.rs:212-219]
  - Signature: `pub enum ProjectIdentitySource {`
  - Purpose: Indexed type `ProjectIdentitySource` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:212-219]
- `ProjectIdentity` (class) component `ProjectIdentity [class]` (`4328c2c8-aef6-57af-8d4d-acda4afbab80`) lines 222-229 [crates/gcode/src/config/context.rs:222-229]
  - Signature: `pub struct ProjectIdentity {`
  - Purpose: 'ProjectIdentity' is a data container that identifies a project by its 'project_id', filesystem 'root', and 'source', while also carrying an optional 'warning', a 'should_write_gcode_json' flag, and an 'index_scope' controlling indexing behavior. [crates/gcode/src/config/context.rs:222-229]
- `Context` (class) component `Context [class]` (`43ccda88-4c91-59a6-83b2-13e434748844`) lines 231-335 [crates/gcode/src/config/context.rs:231-335]
  - Signature: `impl Context {`
  - Purpose: 'Context' resolves the active project from CLI input or filesystem state, loads its identity and indexing scope, validates the parent code index, and conditionally assembles service configurations and indexing settings from the database and optional standalone config into a single runtime context. [crates/gcode/src/config/context.rs:231-335]
- `Context.resolve` (method) component `Context.resolve [method]` (`79949d65-3a16-5c20-bbf0-6e5df87b1e62`) lines 233-235 [crates/gcode/src/config/context.rs:233-235]
  - Signature: `pub fn resolve(project_override: Option<&str>, quiet: bool) -> anyhow::Result<Self> {`
  - Purpose: 'resolve' constructs and returns the resolved instance by delegating to 'Self::resolve_with_services(project_override, quiet, ServiceConfigSelection::all())', using all service configurations and propagating any error as 'anyhow::Result<Self>'. [crates/gcode/src/config/context.rs:233-235]
- `Context.resolve_with_services` (method) component `Context.resolve_with_services [method]` (`e95640c9-aa2f-5ba7-bba7-48ae9a58781d`) lines 237-302 [crates/gcode/src/config/context.rs:237-302]
  - Signature: `pub fn resolve_with_services(`
  - Purpose: 'resolve_with_services' determines the project root from an override path, PostgreSQL hub name lookup, or autodetection, loads and validates the project identity and parent code index, then best-effort resolves the requested service configurations and indexing/vector settings from the database and optional standalone config before constructing 'Self'. [crates/gcode/src/config/context.rs:237-302]
- `Context.resolve_for_project_id` (method) component `Context.resolve_for_project_id [method]` (`080a3cf9-226c-583b-84d1-37d8144cf37d`) lines 310-334 [crates/gcode/src/config/context.rs:310-334]
  - Signature: `pub fn resolve_for_project_id(project_id: &str, quiet: bool) -> anyhow::Result<Self> {`
  - Purpose: Normalizes 'project_id', resolves the database URL and readonly connection, derives FalkorDB and indexing settings from the database plus optional standalone config, and returns a 'Self' initialized for a single-project scope with an empty 'project_root', default code vector settings, no Qdrant or embedding, and the daemon URL set. [crates/gcode/src/config/context.rs:310-334]
- `resolve_project_identity` (function) component `resolve_project_identity [function]` (`7cfbc9d2-c867-5ffb-87d4-54932a1df488`) lines 337-390 [crates/gcode/src/config/context.rs:337-390]
  - Signature: `pub fn resolve_project_identity(`
  - Purpose: Resolves a 'ProjectIdentity' for 'project_root' by canonicalizing the root, inspecting any isolation marker, rejecting markers with only one of 'parent_project_path'/'parent_project_id' set, delegating self-referential markers to non-isolated resolution, and otherwise returning either an 'IsolatedOverlay' identity with overlay/parent index scope or an 'IsolatedRoot' identity. [crates/gcode/src/config/context.rs:337-390]
- `resolve_non_isolated_project_identity` (function) component `resolve_non_isolated_project_identity [function]` (`18d3460c-76db-5074-b3af-d86fcd0683f7`) lines 392-446 [crates/gcode/src/config/context.rs:392-446]
  - Signature: `fn resolve_non_isolated_project_identity(`
  - Purpose: Resolves a non-isolated 'ProjectIdentity' by preferring a linked Git worktree’s top-level directory, then existing '.gobby/project.json' or '.gobby/gcode.json' metadata, otherwise generating an identity from 'root' when allowed or returning an error if identity is missing. [crates/gcode/src/config/context.rs:392-446]
- `is_self_referential_isolation_marker` (function) component `is_self_referential_isolation_marker [function]` (`0ba6c756-8d10-575b-adba-be13dedfe9cf`) lines 448-456 [crates/gcode/src/config/context.rs:448-456]
  - Signature: `fn is_self_referential_isolation_marker(`
  - Purpose: Returns 'true' only when the marker has a 'parent_project_path' that resolves, relative to 'root', to the same path as 'root' itself, otherwise 'false'. [crates/gcode/src/config/context.rs:448-456]
- `resolve_parent_project_root` (function) component `resolve_parent_project_root [function]` (`9685df1c-b537-5fd4-a2a4-296cabc2ea30`) lines 458-466 [crates/gcode/src/config/context.rs:458-466]
  - Signature: `fn resolve_parent_project_root(root: &Path, parent_project_path: &str) -> PathBuf {`
  - Purpose: Converts 'parent_project_path' into an absolute 'PathBuf' by joining it to 'root' when relative, then returns its canonicalized path if resolution succeeds, otherwise the unresolved path. [crates/gcode/src/config/context.rs:458-466]
- `normalize_project_id` (function) component `normalize_project_id [function]` (`df11b4d5-8541-54fe-ab58-fe0a5ac0557b`) lines 468-476 [crates/gcode/src/config/context.rs:468-476]
  - Signature: `fn normalize_project_id(project_id: &str) -> anyhow::Result<String> {`
  - Purpose: Trims the input 'project_id', rejects it if empty, and otherwise validates it as a UUID, returning the canonical UUID string or an 'anyhow' error with context if parsing fails. [crates/gcode/src/config/context.rs:468-476]
- `validate_parent_code_index` (function) component `validate_parent_code_index [function]` (`41088d8a-c2ff-5f50-9475-d89b67da6e6c`) lines 478-509 [crates/gcode/src/config/context.rs:478-509]
  - Signature: `pub(crate) fn validate_parent_code_index(`
  - Purpose: Checks whether an 'Overlay' scope’s 'parent_project_id' has any rows in 'code_indexed_files' and returns an error if the parent code index is missing, otherwise succeeds (and is a no-op for non-'Overlay' scopes). [crates/gcode/src/config/context.rs:478-509]
- `warn_project_identity` (function) component `warn_project_identity [function]` (`0910fc74-98a8-5ac5-923e-ae7c433cae75`) lines 511-518 [crates/gcode/src/config/context.rs:511-518]
  - Signature: `pub fn warn_project_identity(identity: &ProjectIdentity, quiet: bool) {`
  - Purpose: Prints 'Warning: {warning}' to stderr when 'quiet' is false and 'identity.warning' is present, otherwise returns without output. [crates/gcode/src/config/context.rs:511-518]
- `resolve_project_by_name` (function) component `resolve_project_by_name [function]` (`56db3f05-eb61-57d2-bfa1-b4122a9fe790`) lines 523-547 [crates/gcode/src/config/context.rs:523-547]
  - Signature: `fn resolve_project_by_name(name: &str, database_url: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Resolves a project name to an existing directory 'PathBuf' by querying the 'code_indexed_projects' table for matching 'root_path' values or path-suffix matches, returning the most recently indexed directory that exists on disk or an error if none is found. [crates/gcode/src/config/context.rs:523-547]
- `project_name_suffixes` (function) component `project_name_suffixes [function]` (`fb177664-5c95-501e-835e-de9ee8b4ac6a`) lines 549-551 [crates/gcode/src/config/context.rs:549-551]
  - Signature: `pub(super) fn project_name_suffixes(name: &str) -> (String, String) {`
  - Purpose: Returns a pair of 'String's containing the input 'name' prefixed with '/' and '\', respectively. [crates/gcode/src/config/context.rs:549-551]
- `detect_project_root` (function) component `detect_project_root [function]` (`63d19fa3-f4c6-587c-b5d2-842b7825f487`) lines 559-562 [crates/gcode/src/config/context.rs:559-562]
  - Signature: `pub fn detect_project_root() -> anyhow::Result<PathBuf> {`
  - Purpose: Returns the current working directory’s project root by calling 'std::env::current_dir()' and delegating to 'detect_project_root_from(&cwd)', propagating any error as 'anyhow::Result<PathBuf>'. [crates/gcode/src/config/context.rs:559-562]
- `detect_project_root_from` (function) component `detect_project_root_from [function]` (`50faa516-22bd-5620-8886-6625ef4f17ad`) lines 564-600 [crates/gcode/src/config/context.rs:564-600]
  - Signature: `pub fn detect_project_root_from(start: &Path) -> anyhow::Result<PathBuf> {`
  - Purpose: Resolves a starting path to a canonical project root by normalizing files to their parent directory, then preferring a '.gobby' identity root, otherwise the Git worktree top-level, otherwise the nearest '.git'/'.hg' ancestor, and finally returning the original start path as a last resort. [crates/gcode/src/config/context.rs:564-600]
- `resolve_project_id` (function) component `resolve_project_id [function]` (`3279a046-bbbe-594e-83d8-f146c1faea61`) lines 609-611 [crates/gcode/src/config/context.rs:609-611]
  - Signature: `pub(super) fn resolve_project_id(project_root: &Path) -> anyhow::Result<String> {`
  - Purpose: Returns the project ID for 'project_root' by delegating to 'resolve_project_identity' with 'MissingIdentity::Error' and extracting the 'project_id' field, propagating any error via 'anyhow::Result'. [crates/gcode/src/config/context.rs:609-611]
- `absolute_fallback` (function) component `absolute_fallback [function]` (`ded563af-79a7-5b37-a1c0-90957a3d93d1`) lines 613-621 [crates/gcode/src/config/context.rs:613-621]
  - Signature: `fn absolute_fallback(path: &Path) -> PathBuf {`
  - Purpose: Returns 'path' unchanged when it is already absolute, otherwise joins it to the current working directory, falling back to the system temporary directory if 'current_dir()' fails. [crates/gcode/src/config/context.rs:613-621]

