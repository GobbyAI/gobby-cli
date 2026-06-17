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
  - 66-73
  - 75-82
  - 84-91
  - 93-100
  - 102-109
  - 111-118
  - 120-127
  - 131-133
  - 137-140
  - 143-151
  - 157-163
  - 168-191
  - 194-203
  - 206-209
  - 212-219
  - 222-229
  - 233-235
  - 237-302
  - 305-352
  - 355-408
  - 410-464
  - 466-474
  - 476-484
  - 486-494
  - 496-527
  - 529-536
  - 541-565
  - 567-569
  - 577-580
  - 582-618
  - 627-629
  - 631-639
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/config/context.rs:26-31](crates/gcode/src/config/context.rs#L26-L31), [crates/gcode/src/config/context.rs:34](crates/gcode/src/config/context.rs#L34), [crates/gcode/src/config/context.rs:37](crates/gcode/src/config/context.rs#L37), [crates/gcode/src/config/context.rs:51-53](crates/gcode/src/config/context.rs#L51-L53), [crates/gcode/src/config/context.rs:55](crates/gcode/src/config/context.rs#L55), [crates/gcode/src/config/context.rs:58-63](crates/gcode/src/config/context.rs#L58-L63), [crates/gcode/src/config/context.rs:66-73](crates/gcode/src/config/context.rs#L66-L73), [crates/gcode/src/config/context.rs:75-82](crates/gcode/src/config/context.rs#L75-L82), [crates/gcode/src/config/context.rs:84-91](crates/gcode/src/config/context.rs#L84-L91), [crates/gcode/src/config/context.rs:93-100](crates/gcode/src/config/context.rs#L93-L100), [crates/gcode/src/config/context.rs:102-109](crates/gcode/src/config/context.rs#L102-L109), [crates/gcode/src/config/context.rs:111-118](crates/gcode/src/config/context.rs#L111-L118), [crates/gcode/src/config/context.rs:120-127](crates/gcode/src/config/context.rs#L120-L127), [crates/gcode/src/config/context.rs:131-133](crates/gcode/src/config/context.rs#L131-L133), [crates/gcode/src/config/context.rs:137-140](crates/gcode/src/config/context.rs#L137-L140), [crates/gcode/src/config/context.rs:143-151](crates/gcode/src/config/context.rs#L143-L151), [crates/gcode/src/config/context.rs:157-163](crates/gcode/src/config/context.rs#L157-L163), [crates/gcode/src/config/context.rs:168-191](crates/gcode/src/config/context.rs#L168-L191), [crates/gcode/src/config/context.rs:194-203](crates/gcode/src/config/context.rs#L194-L203), [crates/gcode/src/config/context.rs:206-209](crates/gcode/src/config/context.rs#L206-L209), [crates/gcode/src/config/context.rs:212-219](crates/gcode/src/config/context.rs#L212-L219), [crates/gcode/src/config/context.rs:222-229](crates/gcode/src/config/context.rs#L222-L229), [crates/gcode/src/config/context.rs:233-235](crates/gcode/src/config/context.rs#L233-L235), [crates/gcode/src/config/context.rs:237-302](crates/gcode/src/config/context.rs#L237-L302), [crates/gcode/src/config/context.rs:305-352](crates/gcode/src/config/context.rs#L305-L352), [crates/gcode/src/config/context.rs:355-408](crates/gcode/src/config/context.rs#L355-L408), [crates/gcode/src/config/context.rs:410-464](crates/gcode/src/config/context.rs#L410-L464), [crates/gcode/src/config/context.rs:466-474](crates/gcode/src/config/context.rs#L466-L474), [crates/gcode/src/config/context.rs:476-484](crates/gcode/src/config/context.rs#L476-L484), [crates/gcode/src/config/context.rs:486-494](crates/gcode/src/config/context.rs#L486-L494), [crates/gcode/src/config/context.rs:496-527](crates/gcode/src/config/context.rs#L496-L527), [crates/gcode/src/config/context.rs:529-536](crates/gcode/src/config/context.rs#L529-L536), [crates/gcode/src/config/context.rs:541-565](crates/gcode/src/config/context.rs#L541-L565), [crates/gcode/src/config/context.rs:567-569](crates/gcode/src/config/context.rs#L567-L569), [crates/gcode/src/config/context.rs:577-580](crates/gcode/src/config/context.rs#L577-L580), [crates/gcode/src/config/context.rs:582-618](crates/gcode/src/config/context.rs#L582-L618), [crates/gcode/src/config/context.rs:627-629](crates/gcode/src/config/context.rs#L627-L629), [crates/gcode/src/config/context.rs:631-639](crates/gcode/src/config/context.rs#L631-L639)

</details>

# crates/gcode/src/config/context.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file centralizes gcode’s configuration resolution. It defines the local FalkorDB connection struct plus type aliases for Qdrant, embedding, and indexing configs, then groups service toggles in `ServiceConfigSelection` so callers can request all services or just subsets like database, vectors, or hybrid search. The `Context` and project-identity types drive resolution of a project’s config from bootstrap and workspace state, while the helper functions handle root detection, project-name lookup, parent-index validation, ID normalization, and fallback behavior when the project cannot be resolved cleanly.
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]
[crates/gcode/src/config/context.rs:51-53]
[crates/gcode/src/config/context.rs:55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FalkorConfig` | class | `pub struct FalkorConfig {` | `FalkorConfig [class]` | `53926106-6dfb-54e8-98e8-fba4322e5dec` | 26-31 [crates/gcode/src/config/context.rs:26-31] | Indexed class `FalkorConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:26-31] |
| `QdrantConfig` | type | `pub type QdrantConfig = gobby_core::config::QdrantConfig;` | `QdrantConfig [type]` | `64da5dd7-9a46-54c3-856e-22934520004d` | 34-34 [crates/gcode/src/config/context.rs:34] | Indexed type `QdrantConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:34] |
| `EmbeddingConfig` | type | `pub type EmbeddingConfig = gobby_core::config::EmbeddingConfig;` | `EmbeddingConfig [type]` | `fa989081-e16b-5255-84da-f2e8958ca42c` | 37-37 [crates/gcode/src/config/context.rs:37] | Indexed type `EmbeddingConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:37] |
| `CodeVectorSettings` | class | `pub struct CodeVectorSettings {` | `CodeVectorSettings [class]` | `3c239d5c-acad-5519-8278-7872a54e5164` | 51-53 [crates/gcode/src/config/context.rs:51-53] | Indexed class `CodeVectorSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:51-53] |
| `IndexingSettings` | type | `pub type IndexingSettings = gobby_core::config::IndexingConfig;` | `IndexingSettings [type]` | `375d916b-30e4-55bb-9471-2f963f005197` | 55-55 [crates/gcode/src/config/context.rs:55] | Indexed type `IndexingSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:55] |
| `ServiceConfigSelection` | class | `pub struct ServiceConfigSelection {` | `ServiceConfigSelection [class]` | `8627d53f-73ba-53a7-8e99-16b027b0b43a` | 58-63 [crates/gcode/src/config/context.rs:58-63] | Indexed class `ServiceConfigSelection` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:58-63] |
| `ServiceConfigSelection::all` | method | `pub const fn all() -> Self {` | `ServiceConfigSelection::all [method]` | `c9a1cb62-7c8b-5590-91d0-babf0631b4b8` | 66-73 [crates/gcode/src/config/context.rs:66-73] | Indexed method `ServiceConfigSelection::all` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:66-73] |
| `ServiceConfigSelection::database_only` | method | `pub const fn database_only() -> Self {` | `ServiceConfigSelection::database_only [method]` | `b42e3e41-716a-5888-9afa-b816f1a85ee2` | 75-82 [crates/gcode/src/config/context.rs:75-82] | Indexed method `ServiceConfigSelection::database_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:75-82] |
| `ServiceConfigSelection::falkordb_only` | method | `pub const fn falkordb_only() -> Self {` | `ServiceConfigSelection::falkordb_only [method]` | `41215555-256a-53a5-8d44-c0787823aade` | 84-91 [crates/gcode/src/config/context.rs:84-91] | Indexed method `ServiceConfigSelection::falkordb_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:84-91] |
| `ServiceConfigSelection::qdrant_only` | method | `pub const fn qdrant_only() -> Self {` | `ServiceConfigSelection::qdrant_only [method]` | `d44cbbc0-04e9-56bf-91ba-8ba562319e21` | 93-100 [crates/gcode/src/config/context.rs:93-100] | Indexed method `ServiceConfigSelection::qdrant_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:93-100] |
| `ServiceConfigSelection::projection_cleanup` | method | `pub const fn projection_cleanup() -> Self {` | `ServiceConfigSelection::projection_cleanup [method]` | `3349fe55-9b04-504a-a9e7-3bdfb5e169b9` | 102-109 [crates/gcode/src/config/context.rs:102-109] | Indexed method `ServiceConfigSelection::projection_cleanup` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:102-109] |
| `ServiceConfigSelection::vectors` | method | `pub const fn vectors() -> Self {` | `ServiceConfigSelection::vectors [method]` | `03212a41-cc6c-5713-b627-83a209fc66e2` | 111-118 [crates/gcode/src/config/context.rs:111-118] | Indexed method `ServiceConfigSelection::vectors` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:111-118] |
| `ServiceConfigSelection::hybrid_search` | method | `pub const fn hybrid_search() -> Self {` | `ServiceConfigSelection::hybrid_search [method]` | `d131f6ff-2354-5288-bd28-36e855c70efe` | 120-127 [crates/gcode/src/config/context.rs:120-127] | Indexed method `ServiceConfigSelection::hybrid_search` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:120-127] |
| `ServiceConfigSelection::default` | method | `fn default() -> Self {` | `ServiceConfigSelection::default [method]` | `308f7c78-476f-5d36-850a-328dc71dc624` | 131-133 [crates/gcode/src/config/context.rs:131-133] | Indexed method `ServiceConfigSelection::default` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:131-133] |
| `CodeVectorConfigError` | type | `pub enum CodeVectorConfigError {` | `CodeVectorConfigError [type]` | `3d9e9087-b154-567a-8eb9-dad0ec7045f5` | 137-140 [crates/gcode/src/config/context.rs:137-140] | Indexed type `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:137-140] |
| `CodeVectorConfigError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `CodeVectorConfigError::fmt [method]` | `c28ef263-af5a-5965-8ea5-195137ce9fb8` | 143-151 [crates/gcode/src/config/context.rs:143-151] | Indexed method `CodeVectorConfigError::fmt` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:143-151] |
| `FalkorConfig::connection_config` | method | `pub fn connection_config(&self) -> gobby_core::config::FalkorConfig {` | `FalkorConfig::connection_config [method]` | `e024baa0-26a9-57fd-8f01-3454080ca15f` | 157-163 [crates/gcode/src/config/context.rs:157-163] | Indexed method `FalkorConfig::connection_config` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:157-163] |
| `Context` | class | `pub struct Context {` | `Context [class]` | `f57e9fb3-ef45-5bc0-8ec7-a20ecf40b698` | 168-191 [crates/gcode/src/config/context.rs:168-191] | Indexed class `Context` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:168-191] |
| `ProjectIndexScope` | type | `pub enum ProjectIndexScope {` | `ProjectIndexScope [type]` | `7a5353d3-da7f-5160-9017-b32e9548aab8` | 194-203 [crates/gcode/src/config/context.rs:194-203] | Indexed type `ProjectIndexScope` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:194-203] |
| `MissingIdentity` | type | `pub enum MissingIdentity {` | `MissingIdentity [type]` | `d0fce310-84e4-5d23-bbaa-1e8dc55ac538` | 206-209 [crates/gcode/src/config/context.rs:206-209] | Indexed type `MissingIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:206-209] |
| `ProjectIdentitySource` | type | `pub enum ProjectIdentitySource {` | `ProjectIdentitySource [type]` | `bff5f934-378e-5722-a8c7-aa3e45ab5c5f` | 212-219 [crates/gcode/src/config/context.rs:212-219] | Indexed type `ProjectIdentitySource` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:212-219] |
| `ProjectIdentity` | class | `pub struct ProjectIdentity {` | `ProjectIdentity [class]` | `4328c2c8-aef6-57af-8d4d-acda4afbab80` | 222-229 [crates/gcode/src/config/context.rs:222-229] | Indexed class `ProjectIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:222-229] |
| `Context::resolve` | method | `pub fn resolve(project_override: Option<&str>, quiet: bool) -> anyhow::Result<Self> {` | `Context::resolve [method]` | `79949d65-3a16-5c20-bbf0-6e5df87b1e62` | 233-235 [crates/gcode/src/config/context.rs:233-235] | Indexed method `Context::resolve` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:233-235] |
| `Context::resolve_with_services` | method | `pub fn resolve_with_services(` | `Context::resolve_with_services [method]` | `e95640c9-aa2f-5ba7-bba7-48ae9a58781d` | 237-302 [crates/gcode/src/config/context.rs:237-302] | Indexed method `Context::resolve_with_services` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:237-302] |
| `Context::resolve_for_project_id_with_services` | method | `pub fn resolve_for_project_id_with_services(` | `Context::resolve_for_project_id_with_services [method]` | `e28cf06f-8d8a-5d73-9aa4-448c153e5282` | 305-352 [crates/gcode/src/config/context.rs:305-352] | Indexed method `Context::resolve_for_project_id_with_services` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:305-352] |
| `resolve_project_identity` | function | `pub fn resolve_project_identity(` | `resolve_project_identity [function]` | `c16a506e-0836-521f-a333-18c58479e2e7` | 355-408 [crates/gcode/src/config/context.rs:355-408] | Indexed function `resolve_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:355-408] |
| `resolve_non_isolated_project_identity` | function | `fn resolve_non_isolated_project_identity(` | `resolve_non_isolated_project_identity [function]` | `be53020f-4090-5a99-b3eb-175cf5b8f008` | 410-464 [crates/gcode/src/config/context.rs:410-464] | Indexed function `resolve_non_isolated_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:410-464] |
| `is_self_referential_isolation_marker` | function | `fn is_self_referential_isolation_marker(` | `is_self_referential_isolation_marker [function]` | `339b011b-98d8-5d8f-b836-5a3b8cfe16ef` | 466-474 [crates/gcode/src/config/context.rs:466-474] | Indexed function `is_self_referential_isolation_marker` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:466-474] |
| `resolve_parent_project_root` | function | `fn resolve_parent_project_root(root: &Path, parent_project_path: &str) -> PathBuf {` | `resolve_parent_project_root [function]` | `2a22b831-610e-5442-851e-1104373160e0` | 476-484 [crates/gcode/src/config/context.rs:476-484] | Indexed function `resolve_parent_project_root` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:476-484] |
| `normalize_project_id` | function | `fn normalize_project_id(project_id: &str) -> anyhow::Result<String> {` | `normalize_project_id [function]` | `dfaf96cb-f000-58e3-8505-e26501faf934` | 486-494 [crates/gcode/src/config/context.rs:486-494] | Indexed function `normalize_project_id` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:486-494] |
| `validate_parent_code_index` | function | `pub(crate) fn validate_parent_code_index(` | `validate_parent_code_index [function]` | `5bd35579-5aa2-5c54-9998-165847b805f4` | 496-527 [crates/gcode/src/config/context.rs:496-527] | Indexed function `validate_parent_code_index` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:496-527] |
| `warn_project_identity` | function | `pub fn warn_project_identity(identity: &ProjectIdentity, quiet: bool) {` | `warn_project_identity [function]` | `e921ff52-bfd9-5e31-91e8-098ebc78d498` | 529-536 [crates/gcode/src/config/context.rs:529-536] | Indexed function `warn_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:529-536] |
| `resolve_project_by_name` | function | `fn resolve_project_by_name(name: &str, database_url: &str) -> anyhow::Result<PathBuf> {` | `resolve_project_by_name [function]` | `c101f802-bb35-546d-993d-93a6bdfd6d98` | 541-565 [crates/gcode/src/config/context.rs:541-565] | Indexed function `resolve_project_by_name` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:541-565] |
| `project_name_suffixes` | function | `pub(super) fn project_name_suffixes(name: &str) -> (String, String) {` | `project_name_suffixes [function]` | `f1dfe0c1-ecba-554b-9da6-94fcd8493113` | 567-569 [crates/gcode/src/config/context.rs:567-569] | Indexed function `project_name_suffixes` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:567-569] |
| `detect_project_root` | function | `pub fn detect_project_root() -> anyhow::Result<PathBuf> {` | `detect_project_root [function]` | `edb5edf1-6aa4-5169-87ea-afc33b1a6031` | 577-580 [crates/gcode/src/config/context.rs:577-580] | Indexed function `detect_project_root` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:577-580] |
| `detect_project_root_from` | function | `pub fn detect_project_root_from(start: &Path) -> anyhow::Result<PathBuf> {` | `detect_project_root_from [function]` | `bd38792f-4fe7-5434-877a-a315c412dedd` | 582-618 [crates/gcode/src/config/context.rs:582-618] | Indexed function `detect_project_root_from` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:582-618] |
| `resolve_project_id` | function | `pub(super) fn resolve_project_id(project_root: &Path) -> anyhow::Result<String> {` | `resolve_project_id [function]` | `7e538a11-cd71-5054-a07b-62f379c3fcd2` | 627-629 [crates/gcode/src/config/context.rs:627-629] | Indexed function `resolve_project_id` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:627-629] |
| `absolute_fallback` | function | `fn absolute_fallback(path: &Path) -> PathBuf {` | `absolute_fallback [function]` | `610ff3cd-6440-5be0-ab50-d864c640c089` | 631-639 [crates/gcode/src/config/context.rs:631-639] | Indexed function `absolute_fallback` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:631-639] |
