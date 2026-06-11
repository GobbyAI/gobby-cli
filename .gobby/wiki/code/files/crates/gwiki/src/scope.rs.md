---
title: crates/gwiki/src/scope.rs
type: code_file
provenance:
- file: crates/gwiki/src/scope.rs
  ranges:
  - 12-16
  - 19-27
  - 29-89
  - 30-36
  - 38-48
  - 50-52
  - 54-56
  - 58-60
  - 62-67
  - 69-74
  - 76-81
  - 83-88
  - 91-94
  - 96-121
  - 123-129
  - 131-152
  - 154-180
  - 182-188
  - 190-206
  - 216-218
  - 220-226
  - 221-225
  - 228-236
  - 229-231
  - 233-235
  - 240-256
  - 259-273
  - 276-312
  - 315-341
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/scope.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/scope.rs` exposes 29 indexed API symbols.
[crates/gwiki/src/scope.rs:12-16]
[crates/gwiki/src/scope.rs:19-27]
[crates/gwiki/src/scope.rs:29-89]
[crates/gwiki/src/scope.rs:30-36]
[crates/gwiki/src/scope.rs:38-48]

## API Symbols

- `ResolvedScope` (class) component `ResolvedScope [class]` (`b6881cd1-180e-59ec-a7b0-212f5ced07ef`) lines 12-16 [crates/gwiki/src/scope.rs:12-16]
  - Signature: `pub struct ResolvedScope {`
  - Purpose: Indexed class `ResolvedScope` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:12-16]
- `ScopeKind` (type) component `ScopeKind [type]` (`575e21d1-e0ce-5fcb-be51-56759d4e7d38`) lines 19-27 [crates/gwiki/src/scope.rs:19-27]
  - Signature: `pub enum ScopeKind {`
  - Purpose: Indexed type `ScopeKind` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:19-27]
- `ResolvedScope` (class) component `ResolvedScope [class]` (`778bd417-8546-5230-8688-c7058e6c1e40`) lines 29-89 [crates/gwiki/src/scope.rs:29-89]
  - Signature: `impl ResolvedScope {`
  - Purpose: Indexed class `ResolvedScope` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:29-89]
- `ResolvedScope.topic` (method) component `ResolvedScope.topic [method]` (`77fb16d7-3240-52b8-80b2-ae698bd465da`) lines 30-36 [crates/gwiki/src/scope.rs:30-36]
  - Signature: `pub fn topic(name: String, root: PathBuf, registry_path: PathBuf) -> Self {`
  - Purpose: Indexed method `ResolvedScope.topic` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:30-36]
- `ResolvedScope.project` (method) component `ResolvedScope.project [method]` (`4b631375-70bc-5005-9763-729c06674865`) lines 38-48 [crates/gwiki/src/scope.rs:38-48]
  - Signature: `pub fn project(project_id: String, project_root: PathBuf, root: PathBuf) -> Self {`
  - Purpose: Indexed method `ResolvedScope.project` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:38-48]
- `ResolvedScope.kind` (method) component `ResolvedScope.kind [method]` (`1b17d6da-7efc-5c05-9574-038d1e65b423`) lines 50-52 [crates/gwiki/src/scope.rs:50-52]
  - Signature: `pub fn kind(&self) -> &ScopeKind {`
  - Purpose: Indexed method `ResolvedScope.kind` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:50-52]
- `ResolvedScope.root` (method) component `ResolvedScope.root [method]` (`37dfd9b0-081a-5bce-8f6d-5818a8fade56`) lines 54-56 [crates/gwiki/src/scope.rs:54-56]
  - Signature: `pub fn root(&self) -> &Path {`
  - Purpose: Indexed method `ResolvedScope.root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:54-56]
- `ResolvedScope.registry_path` (method) component `ResolvedScope.registry_path [method]` (`f21f4274-cdee-5186-9324-a4ddcc9fe196`) lines 58-60 [crates/gwiki/src/scope.rs:58-60]
  - Signature: `pub fn registry_path(&self) -> &Path {`
  - Purpose: Indexed method `ResolvedScope.registry_path` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:58-60]
- `ResolvedScope.identity` (method) component `ResolvedScope.identity [method]` (`2b30364a-e0f4-5707-a30e-75d6d29f96a9`) lines 62-67 [crates/gwiki/src/scope.rs:62-67]
  - Signature: `pub fn identity(&self) -> String {`
  - Purpose: Indexed method `ResolvedScope.identity` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:62-67]
- `ResolvedScope.topic_name` (method) component `ResolvedScope.topic_name [method]` (`63d82ca1-2701-57df-9f88-9ea8bd9177c1`) lines 69-74 [crates/gwiki/src/scope.rs:69-74]
  - Signature: `pub fn topic_name(&self) -> Option<&str> {`
  - Purpose: Indexed method `ResolvedScope.topic_name` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:69-74]
- `ResolvedScope.project_id` (method) component `ResolvedScope.project_id [method]` (`c6220f0e-1409-502f-8914-bbae838dd237`) lines 76-81 [crates/gwiki/src/scope.rs:76-81]
  - Signature: `pub fn project_id(&self) -> Option<&str> {`
  - Purpose: Indexed method `ResolvedScope.project_id` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:76-81]
- `ResolvedScope.project_root` (method) component `ResolvedScope.project_root [method]` (`acf3301d-7ab1-52c5-9628-a15cec64ed55`) lines 83-88 [crates/gwiki/src/scope.rs:83-88]
  - Signature: `pub fn project_root(&self) -> Option<&Path> {`
  - Purpose: Indexed method `ResolvedScope.project_root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:83-88]
- `resolve` (function) component `resolve [function]` (`f988ece6-c5c2-50af-b4b5-9b0299a8fd2d`) lines 91-94 [crates/gwiki/src/scope.rs:91-94]
  - Signature: `pub fn resolve(selection: &ScopeSelection, cwd: &Path) -> Result<ResolvedScope, WikiError> {`
  - Purpose: Indexed function `resolve` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:91-94]
- `resolve_with_source` (function) component `resolve_with_source [function]` (`5246780f-b12a-546b-ac46-5b9a56036486`) lines 96-121 [crates/gwiki/src/scope.rs:96-121]
  - Signature: `pub fn resolve_with_source(`
  - Purpose: Indexed function `resolve_with_source` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:96-121]
- `resolve_topic` (function) component `resolve_topic [function]` (`8369adf2-f7a2-5cee-b10c-7b5d88268db6`) lines 123-129 [crates/gwiki/src/scope.rs:123-129]
  - Signature: `fn resolve_topic(topic: &str, source: &mut impl ConfigSource) -> Result<ResolvedScope, WikiError> {`
  - Purpose: Indexed function `resolve_topic` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:123-129]
- `resolve_project_from_root` (function) component `resolve_project_from_root [function]` (`e9dddd38-4c0e-5808-8d51-d5967cdccf70`) lines 131-152 [crates/gwiki/src/scope.rs:131-152]
  - Signature: `fn resolve_project_from_root(project_root: &Path) -> Result<ResolvedScope, WikiError> {`
  - Purpose: Indexed function `resolve_project_from_root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:131-152]
- `resolve_hub_path` (function) component `resolve_hub_path [function]` (`42aef1ba-d6bc-5ba4-b174-a56bc8939fff`) lines 154-180 [crates/gwiki/src/scope.rs:154-180]
  - Signature: `fn resolve_hub_path(source: &mut impl ConfigSource) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `resolve_hub_path` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:154-180]
- `default_hub_path` (function) component `default_hub_path [function]` (`b39a0513-2779-50cb-a55b-4ceb6aed2124`) lines 182-188 [crates/gwiki/src/scope.rs:182-188]
  - Signature: `fn default_hub_path() -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `default_hub_path` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:182-188]
- `expand_home` (function) component `expand_home [function]` (`16b08497-6491-5c32-936f-7d3bf6c40bf5`) lines 190-206 [crates/gwiki/src/scope.rs:190-206]
  - Signature: `fn expand_home(path: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `expand_home` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:190-206]
- `TestConfig` (class) component `TestConfig [class]` (`148044f9-8dde-5104-8861-b238d61f687c`) lines 216-218 [crates/gwiki/src/scope.rs:216-218]
  - Signature: `struct TestConfig {`
  - Purpose: Indexed class `TestConfig` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:216-218]
- `TestConfig` (class) component `TestConfig [class]` (`efc0e285-50b8-56d8-b559-e2a3d4d90335`) lines 220-226 [crates/gwiki/src/scope.rs:220-226]
  - Signature: `impl TestConfig {`
  - Purpose: Indexed class `TestConfig` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:220-226]
- `TestConfig.with` (method) component `TestConfig.with [method]` (`46ea0008-11bd-5079-af81-5c0dd0d499ea`) lines 221-225 [crates/gwiki/src/scope.rs:221-225]
  - Signature: `fn with(key: &str, value: impl Into<String>) -> Self {`
  - Purpose: Indexed method `TestConfig.with` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:221-225]
- `TestConfig` (class) component `TestConfig [class]` (`f9a70748-882b-5a6f-bffc-f7170c5de579`) lines 228-236 [crates/gwiki/src/scope.rs:228-236]
  - Signature: `impl ConfigSource for TestConfig {`
  - Purpose: Indexed class `TestConfig` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:228-236]
- `TestConfig.config_value` (method) component `TestConfig.config_value [method]` (`96d52b82-2504-5f4d-af92-452cbe1aa3a3`) lines 229-231 [crates/gwiki/src/scope.rs:229-231]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed method `TestConfig.config_value` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:229-231]
- `TestConfig.resolve_value` (method) component `TestConfig.resolve_value [method]` (`ca4748d1-1bf8-504f-9827-2e68aa15db5f`) lines 233-235 [crates/gwiki/src/scope.rs:233-235]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `TestConfig.resolve_value` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:233-235]
- `resolves_global_topic` (function) component `resolves_global_topic [function]` (`a10ecaf4-5970-5a31-acdd-d94bc10e2a25`) lines 240-256 [crates/gwiki/src/scope.rs:240-256]
  - Signature: `fn resolves_global_topic() {`
  - Purpose: Indexed function `resolves_global_topic` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:240-256]
- `rejects_invalid_topic_names` (function) component `rejects_invalid_topic_names [function]` (`7a70fca3-3c59-5dfc-bc45-c6945aef777e`) lines 259-273 [crates/gwiki/src/scope.rs:259-273]
  - Signature: `fn rejects_invalid_topic_names() {`
  - Purpose: Indexed function `rejects_invalid_topic_names` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:259-273]
- `resolves_project_scope_read_only` (function) component `resolves_project_scope_read_only [function]` (`20cff83d-6afa-5dd4-8e40-3f1e575704ce`) lines 276-312 [crates/gwiki/src/scope.rs:276-312]
  - Signature: `fn resolves_project_scope_read_only() {`
  - Purpose: Indexed function `resolves_project_scope_read_only` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:276-312]
- `project_dot_resolves_to_absolute_project_wiki_root` (function) component `project_dot_resolves_to_absolute_project_wiki_root [function]` (`d43d526a-0a92-5523-bce9-af627dbba0b9`) lines 315-341 [crates/gwiki/src/scope.rs:315-341]
  - Signature: `fn project_dot_resolves_to_absolute_project_wiki_root() {`
  - Purpose: Indexed function `project_dot_resolves_to_absolute_project_wiki_root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:315-341]

