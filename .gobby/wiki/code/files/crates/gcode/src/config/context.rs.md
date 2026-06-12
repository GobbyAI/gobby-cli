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
  - 112-116
  - 119-122
  - 124-134
  - '136'
  - 138-146
  - 150-173
  - 176-185
  - 188-191
  - 194-201
  - 204-211
  - 213-317
  - 319-372
  - 374-428
  - 430-438
  - 440-448
  - 450-458
  - 460-491
  - 493-500
  - 505-529
  - 531-533
  - 541-544
  - 546-582
  - 591-593
  - 595-603
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/config/context.rs

Module: [[code/modules/crates/gcode/src/config|crates/gcode/src/config]]

## Purpose

`crates/gcode/src/config/context.rs` exposes 42 indexed API symbols.
[crates/gcode/src/config/context.rs:26-31]
[crates/gcode/src/config/context.rs:34]
[crates/gcode/src/config/context.rs:37]
[crates/gcode/src/config/context.rs:51-53]
[crates/gcode/src/config/context.rs:55]

## API Symbols

- `FalkorConfig` (class) component `FalkorConfig [class]` (`53926106-6dfb-54e8-98e8-fba4322e5dec`) lines 26-31 [crates/gcode/src/config/context.rs:26-31]
  - Signature: `pub struct FalkorConfig {`
  - Purpose: Indexed class `FalkorConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:26-31]
- `QdrantConfig` (type) component `QdrantConfig [type]` (`64da5dd7-9a46-54c3-856e-22934520004d`) lines 34-34 [crates/gcode/src/config/context.rs:34]
  - Signature: `pub type QdrantConfig = gobby_core::config::QdrantConfig;`
  - Purpose: Indexed type `QdrantConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:34]
- `EmbeddingConfig` (type) component `EmbeddingConfig [type]` (`fa989081-e16b-5255-84da-f2e8958ca42c`) lines 37-37 [crates/gcode/src/config/context.rs:37]
  - Signature: `pub type EmbeddingConfig = gobby_core::config::EmbeddingConfig;`
  - Purpose: Indexed type `EmbeddingConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:37]
- `CodeVectorSettings` (class) component `CodeVectorSettings [class]` (`3c239d5c-acad-5519-8278-7872a54e5164`) lines 51-53 [crates/gcode/src/config/context.rs:51-53]
  - Signature: `pub struct CodeVectorSettings {`
  - Purpose: Indexed class `CodeVectorSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:51-53]
- `IndexingSettings` (type) component `IndexingSettings [type]` (`375d916b-30e4-55bb-9471-2f963f005197`) lines 55-55 [crates/gcode/src/config/context.rs:55]
  - Signature: `pub type IndexingSettings = gobby_core::config::IndexingConfig;`
  - Purpose: Indexed type `IndexingSettings` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:55]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`8627d53f-73ba-53a7-8e99-16b027b0b43a`) lines 58-63 [crates/gcode/src/config/context.rs:58-63]
  - Signature: `pub struct ServiceConfigSelection {`
  - Purpose: Indexed class `ServiceConfigSelection` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:58-63]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`029d25d6-a9f9-55ef-9799-f9ebd8327d6d`) lines 65-110 [crates/gcode/src/config/context.rs:65-110]
  - Signature: `impl ServiceConfigSelection {`
  - Purpose: Indexed class `ServiceConfigSelection` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:65-110]
- `ServiceConfigSelection.all` (method) component `ServiceConfigSelection.all [method]` (`c9a1cb62-7c8b-5590-91d0-babf0631b4b8`) lines 66-73 [crates/gcode/src/config/context.rs:66-73]
  - Signature: `pub const fn all() -> Self {`
  - Purpose: Indexed method `ServiceConfigSelection.all` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:66-73]
- `ServiceConfigSelection.database_only` (method) component `ServiceConfigSelection.database_only [method]` (`b42e3e41-716a-5888-9afa-b816f1a85ee2`) lines 75-82 [crates/gcode/src/config/context.rs:75-82]
  - Signature: `pub const fn database_only() -> Self {`
  - Purpose: Indexed method `ServiceConfigSelection.database_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:75-82]
- `ServiceConfigSelection.falkordb_only` (method) component `ServiceConfigSelection.falkordb_only [method]` (`41215555-256a-53a5-8d44-c0787823aade`) lines 84-91 [crates/gcode/src/config/context.rs:84-91]
  - Signature: `pub const fn falkordb_only() -> Self {`
  - Purpose: Indexed method `ServiceConfigSelection.falkordb_only` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:84-91]
- `ServiceConfigSelection.vectors` (method) component `ServiceConfigSelection.vectors [method]` (`a4c1f2d9-c41a-5cc3-98b1-e00f4ab47425`) lines 93-100 [crates/gcode/src/config/context.rs:93-100]
  - Signature: `pub const fn vectors() -> Self {`
  - Purpose: Indexed method `ServiceConfigSelection.vectors` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:93-100]
- `ServiceConfigSelection.hybrid_search` (method) component `ServiceConfigSelection.hybrid_search [method]` (`5b7522d5-3026-5c24-8928-ec469fc6df71`) lines 102-109 [crates/gcode/src/config/context.rs:102-109]
  - Signature: `pub const fn hybrid_search() -> Self {`
  - Purpose: Indexed method `ServiceConfigSelection.hybrid_search` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:102-109]
- `ServiceConfigSelection` (class) component `ServiceConfigSelection [class]` (`dd4f67d9-d274-5a58-a881-bd28e73acd40`) lines 112-116 [crates/gcode/src/config/context.rs:112-116]
  - Signature: `impl Default for ServiceConfigSelection {`
  - Purpose: Indexed class `ServiceConfigSelection` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:112-116]
- `ServiceConfigSelection.default` (method) component `ServiceConfigSelection.default [method]` (`a4e17f61-3949-5078-9372-85c6c48ce886`) lines 113-115 [crates/gcode/src/config/context.rs:113-115]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `ServiceConfigSelection.default` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:113-115]
- `CodeVectorConfigError` (type) component `CodeVectorConfigError [type]` (`af12f40d-1d4d-5085-9f4f-7290f4a41fce`) lines 119-122 [crates/gcode/src/config/context.rs:119-122]
  - Signature: `pub enum CodeVectorConfigError {`
  - Purpose: Indexed type `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:119-122]
- `CodeVectorConfigError` (class) component `CodeVectorConfigError [class]` (`0e37688d-ceb6-5676-8dbd-7221a7970f7b`) lines 124-134 [crates/gcode/src/config/context.rs:124-134]
  - Signature: `impl fmt::Display for CodeVectorConfigError {`
  - Purpose: Indexed class `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:124-134]
- `CodeVectorConfigError.fmt` (method) component `CodeVectorConfigError.fmt [method]` (`6da2a5dd-5190-5e5b-918d-782ba3edb87e`) lines 125-133 [crates/gcode/src/config/context.rs:125-133]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `CodeVectorConfigError.fmt` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:125-133]
- `CodeVectorConfigError` (class) component `CodeVectorConfigError [class]` (`19890a79-3fe2-53d9-8d1f-f9123bb32ec5`) lines 136-136 [crates/gcode/src/config/context.rs:136]
  - Signature: `impl std::error::Error for CodeVectorConfigError {}`
  - Purpose: Indexed class `CodeVectorConfigError` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:136]
- `FalkorConfig` (class) component `FalkorConfig [class]` (`552aaab0-c0e5-52e0-b933-b3dc69d52831`) lines 138-146 [crates/gcode/src/config/context.rs:138-146]
  - Signature: `impl FalkorConfig {`
  - Purpose: Indexed class `FalkorConfig` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:138-146]
- `FalkorConfig.connection_config` (method) component `FalkorConfig.connection_config [method]` (`1a50772c-a7b4-53dd-8641-b7664ce043f8`) lines 139-145 [crates/gcode/src/config/context.rs:139-145]
  - Signature: `pub fn connection_config(&self) -> gobby_core::config::FalkorConfig {`
  - Purpose: Indexed method `FalkorConfig.connection_config` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:139-145]
- `Context` (class) component `Context [class]` (`7032577f-b11e-5c5d-abab-db0b71de4cdd`) lines 150-173 [crates/gcode/src/config/context.rs:150-173]
  - Signature: `pub struct Context {`
  - Purpose: Indexed class `Context` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:150-173]
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
  - Purpose: Indexed class `ProjectIdentity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:204-211]
- `Context` (class) component `Context [class]` (`df0b5059-b1bc-50e0-b6d6-7bc99f0b4fe5`) lines 213-317 [crates/gcode/src/config/context.rs:213-317]
  - Signature: `impl Context {`
  - Purpose: Indexed class `Context` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:213-317]
- `Context.resolve` (method) component `Context.resolve [method]` (`3228ad40-0817-52f7-88a9-afca5418ea28`) lines 215-217 [crates/gcode/src/config/context.rs:215-217]
  - Signature: `pub fn resolve(project_override: Option<&str>, quiet: bool) -> anyhow::Result<Self> {`
  - Purpose: Indexed method `Context.resolve` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:215-217]
- `Context.resolve_with_services` (method) component `Context.resolve_with_services [method]` (`a2db489f-4ae5-57c7-8ed2-d96c19b2e3e1`) lines 219-284 [crates/gcode/src/config/context.rs:219-284]
  - Signature: `pub fn resolve_with_services(`
  - Purpose: Indexed method `Context.resolve_with_services` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:219-284]
- `Context.resolve_for_project_id` (method) component `Context.resolve_for_project_id [method]` (`8925270f-fc9a-5228-be3a-cdfeb82d97c2`) lines 292-316 [crates/gcode/src/config/context.rs:292-316]
  - Signature: `pub fn resolve_for_project_id(project_id: &str, quiet: bool) -> anyhow::Result<Self> {`
  - Purpose: Indexed method `Context.resolve_for_project_id` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:292-316]
- `resolve_project_identity` (function) component `resolve_project_identity [function]` (`ad7fe1e5-649e-5f27-bc03-74afdc142c75`) lines 319-372 [crates/gcode/src/config/context.rs:319-372]
  - Signature: `pub fn resolve_project_identity(`
  - Purpose: Indexed function `resolve_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:319-372]
- `resolve_non_isolated_project_identity` (function) component `resolve_non_isolated_project_identity [function]` (`6ba92acc-ba28-5a91-8869-73c1cf10c4d6`) lines 374-428 [crates/gcode/src/config/context.rs:374-428]
  - Signature: `fn resolve_non_isolated_project_identity(`
  - Purpose: Indexed function `resolve_non_isolated_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:374-428]
- `is_self_referential_isolation_marker` (function) component `is_self_referential_isolation_marker [function]` (`f811dfcb-2ee3-5ad0-a838-22e770e06aad`) lines 430-438 [crates/gcode/src/config/context.rs:430-438]
  - Signature: `fn is_self_referential_isolation_marker(`
  - Purpose: Indexed function `is_self_referential_isolation_marker` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:430-438]
- `resolve_parent_project_root` (function) component `resolve_parent_project_root [function]` (`c65c753f-2a9a-57c2-969a-17f2332f836e`) lines 440-448 [crates/gcode/src/config/context.rs:440-448]
  - Signature: `fn resolve_parent_project_root(root: &Path, parent_project_path: &str) -> PathBuf {`
  - Purpose: Indexed function `resolve_parent_project_root` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:440-448]
- `normalize_project_id` (function) component `normalize_project_id [function]` (`333f3f6e-ca4f-5144-a592-03f2b3dc57ed`) lines 450-458 [crates/gcode/src/config/context.rs:450-458]
  - Signature: `fn normalize_project_id(project_id: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `normalize_project_id` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:450-458]
- `validate_parent_code_index` (function) component `validate_parent_code_index [function]` (`44e72b20-3011-5fcc-9159-0aed0561089c`) lines 460-491 [crates/gcode/src/config/context.rs:460-491]
  - Signature: `pub(crate) fn validate_parent_code_index(`
  - Purpose: Indexed function `validate_parent_code_index` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:460-491]
- `warn_project_identity` (function) component `warn_project_identity [function]` (`cd92b4a3-a201-5d1a-8007-b3d9f7378989`) lines 493-500 [crates/gcode/src/config/context.rs:493-500]
  - Signature: `pub fn warn_project_identity(identity: &ProjectIdentity, quiet: bool) {`
  - Purpose: Indexed function `warn_project_identity` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:493-500]
- `resolve_project_by_name` (function) component `resolve_project_by_name [function]` (`b120d217-6932-535c-8f35-469a34721d30`) lines 505-529 [crates/gcode/src/config/context.rs:505-529]
  - Signature: `fn resolve_project_by_name(name: &str, database_url: &str) -> anyhow::Result<PathBuf> {`
  - Purpose: Indexed function `resolve_project_by_name` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:505-529]
- `project_name_suffixes` (function) component `project_name_suffixes [function]` (`dee35a40-bd82-52ef-97d8-51250e249dbc`) lines 531-533 [crates/gcode/src/config/context.rs:531-533]
  - Signature: `pub(super) fn project_name_suffixes(name: &str) -> (String, String) {`
  - Purpose: Indexed function `project_name_suffixes` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:531-533]
- `detect_project_root` (function) component `detect_project_root [function]` (`e5e06d33-9c2c-5658-8719-dfa876c4c58d`) lines 541-544 [crates/gcode/src/config/context.rs:541-544]
  - Signature: `pub fn detect_project_root() -> anyhow::Result<PathBuf> {`
  - Purpose: Indexed function `detect_project_root` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:541-544]
- `detect_project_root_from` (function) component `detect_project_root_from [function]` (`23acf395-4676-5a04-8dc0-73b6dbc090c5`) lines 546-582 [crates/gcode/src/config/context.rs:546-582]
  - Signature: `pub fn detect_project_root_from(start: &Path) -> anyhow::Result<PathBuf> {`
  - Purpose: Indexed function `detect_project_root_from` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:546-582]
- `resolve_project_id` (function) component `resolve_project_id [function]` (`a654028b-aee7-5326-9f1e-69f3bcfbce62`) lines 591-593 [crates/gcode/src/config/context.rs:591-593]
  - Signature: `pub(super) fn resolve_project_id(project_root: &Path) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_project_id` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:591-593]
- `absolute_fallback` (function) component `absolute_fallback [function]` (`4d74e04a-7a2f-562c-89bb-95dadec574fb`) lines 595-603 [crates/gcode/src/config/context.rs:595-603]
  - Signature: `fn absolute_fallback(path: &Path) -> PathBuf {`
  - Purpose: Indexed function `absolute_fallback` in `crates/gcode/src/config/context.rs`. [crates/gcode/src/config/context.rs:595-603]

