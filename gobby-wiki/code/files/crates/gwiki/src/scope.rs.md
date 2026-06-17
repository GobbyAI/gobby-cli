---
title: crates/gwiki/src/scope.rs
type: code_file
provenance:
- file: crates/gwiki/src/scope.rs
  ranges:
  - 12-16
  - 19-27
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
  - 221-225
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/scope.rs:12-16](crates/gwiki/src/scope.rs#L12-L16), [crates/gwiki/src/scope.rs:19-27](crates/gwiki/src/scope.rs#L19-L27), [crates/gwiki/src/scope.rs:30-36](crates/gwiki/src/scope.rs#L30-L36), [crates/gwiki/src/scope.rs:38-48](crates/gwiki/src/scope.rs#L38-L48), [crates/gwiki/src/scope.rs:50-52](crates/gwiki/src/scope.rs#L50-L52), [crates/gwiki/src/scope.rs:54-56](crates/gwiki/src/scope.rs#L54-L56), [crates/gwiki/src/scope.rs:58-60](crates/gwiki/src/scope.rs#L58-L60), [crates/gwiki/src/scope.rs:62-67](crates/gwiki/src/scope.rs#L62-L67), [crates/gwiki/src/scope.rs:69-74](crates/gwiki/src/scope.rs#L69-L74), [crates/gwiki/src/scope.rs:76-81](crates/gwiki/src/scope.rs#L76-L81), [crates/gwiki/src/scope.rs:83-88](crates/gwiki/src/scope.rs#L83-L88), [crates/gwiki/src/scope.rs:91-94](crates/gwiki/src/scope.rs#L91-L94), [crates/gwiki/src/scope.rs:96-121](crates/gwiki/src/scope.rs#L96-L121), [crates/gwiki/src/scope.rs:123-129](crates/gwiki/src/scope.rs#L123-L129), [crates/gwiki/src/scope.rs:131-152](crates/gwiki/src/scope.rs#L131-L152), [crates/gwiki/src/scope.rs:154-180](crates/gwiki/src/scope.rs#L154-L180), [crates/gwiki/src/scope.rs:182-188](crates/gwiki/src/scope.rs#L182-L188), [crates/gwiki/src/scope.rs:190-206](crates/gwiki/src/scope.rs#L190-L206), [crates/gwiki/src/scope.rs:216-218](crates/gwiki/src/scope.rs#L216-L218), [crates/gwiki/src/scope.rs:221-225](crates/gwiki/src/scope.rs#L221-L225), [crates/gwiki/src/scope.rs:229-231](crates/gwiki/src/scope.rs#L229-L231), [crates/gwiki/src/scope.rs:233-235](crates/gwiki/src/scope.rs#L233-L235), [crates/gwiki/src/scope.rs:240-256](crates/gwiki/src/scope.rs#L240-L256), [crates/gwiki/src/scope.rs:259-273](crates/gwiki/src/scope.rs#L259-L273), [crates/gwiki/src/scope.rs:276-312](crates/gwiki/src/scope.rs#L276-L312), [crates/gwiki/src/scope.rs:315-341](crates/gwiki/src/scope.rs#L315-L341)

</details>

# crates/gwiki/src/scope.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Resolves wiki scope selections into a normalized `ResolvedScope` for either a topic or a project, carrying the scope kind plus its root and registry path. `ResolvedScope` exposes accessors and derived identifiers so callers can inspect the resolved scope without pattern matching on `ScopeKind` directly. The helper functions handle resolution from config and environment, topic validation, project-root lookup, hub-path expansion, and home-directory expansion, while the test helpers verify global topic resolution, invalid topic rejection, and project-scope behavior.
[crates/gwiki/src/scope.rs:12-16]
[crates/gwiki/src/scope.rs:19-27]
[crates/gwiki/src/scope.rs:30-36]
[crates/gwiki/src/scope.rs:38-48]
[crates/gwiki/src/scope.rs:50-52]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ResolvedScope` | class | `pub struct ResolvedScope {` | `ResolvedScope [class]` | `b6881cd1-180e-59ec-a7b0-212f5ced07ef` | 12-16 [crates/gwiki/src/scope.rs:12-16] | Indexed class `ResolvedScope` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:12-16] |
| `ScopeKind` | type | `pub enum ScopeKind {` | `ScopeKind [type]` | `575e21d1-e0ce-5fcb-be51-56759d4e7d38` | 19-27 [crates/gwiki/src/scope.rs:19-27] | Indexed type `ScopeKind` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:19-27] |
| `ResolvedScope::topic` | method | `pub fn topic(name: String, root: PathBuf, registry_path: PathBuf) -> Self {` | `ResolvedScope::topic [method]` | `77fb16d7-3240-52b8-80b2-ae698bd465da` | 30-36 [crates/gwiki/src/scope.rs:30-36] | Indexed method `ResolvedScope::topic` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:30-36] |
| `ResolvedScope::project` | method | `pub fn project(project_id: String, project_root: PathBuf, root: PathBuf) -> Self {` | `ResolvedScope::project [method]` | `4b631375-70bc-5005-9763-729c06674865` | 38-48 [crates/gwiki/src/scope.rs:38-48] | Indexed method `ResolvedScope::project` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:38-48] |
| `ResolvedScope::kind` | method | `pub fn kind(&self) -> &ScopeKind {` | `ResolvedScope::kind [method]` | `1b17d6da-7efc-5c05-9574-038d1e65b423` | 50-52 [crates/gwiki/src/scope.rs:50-52] | Indexed method `ResolvedScope::kind` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:50-52] |
| `ResolvedScope::root` | method | `pub fn root(&self) -> &Path {` | `ResolvedScope::root [method]` | `37dfd9b0-081a-5bce-8f6d-5818a8fade56` | 54-56 [crates/gwiki/src/scope.rs:54-56] | Indexed method `ResolvedScope::root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:54-56] |
| `ResolvedScope::registry_path` | method | `pub fn registry_path(&self) -> &Path {` | `ResolvedScope::registry_path [method]` | `f21f4274-cdee-5186-9324-a4ddcc9fe196` | 58-60 [crates/gwiki/src/scope.rs:58-60] | Indexed method `ResolvedScope::registry_path` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:58-60] |
| `ResolvedScope::identity` | method | `pub fn identity(&self) -> String {` | `ResolvedScope::identity [method]` | `2b30364a-e0f4-5707-a30e-75d6d29f96a9` | 62-67 [crates/gwiki/src/scope.rs:62-67] | Indexed method `ResolvedScope::identity` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:62-67] |
| `ResolvedScope::topic_name` | method | `pub fn topic_name(&self) -> Option<&str> {` | `ResolvedScope::topic_name [method]` | `63d82ca1-2701-57df-9f88-9ea8bd9177c1` | 69-74 [crates/gwiki/src/scope.rs:69-74] | Indexed method `ResolvedScope::topic_name` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:69-74] |
| `ResolvedScope::project_id` | method | `pub fn project_id(&self) -> Option<&str> {` | `ResolvedScope::project_id [method]` | `c6220f0e-1409-502f-8914-bbae838dd237` | 76-81 [crates/gwiki/src/scope.rs:76-81] | Indexed method `ResolvedScope::project_id` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:76-81] |
| `ResolvedScope::project_root` | method | `pub fn project_root(&self) -> Option<&Path> {` | `ResolvedScope::project_root [method]` | `acf3301d-7ab1-52c5-9628-a15cec64ed55` | 83-88 [crates/gwiki/src/scope.rs:83-88] | Indexed method `ResolvedScope::project_root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:83-88] |
| `resolve` | function | `pub fn resolve(selection: &ScopeSelection, cwd: &Path) -> Result<ResolvedScope, WikiError> {` | `resolve [function]` | `f988ece6-c5c2-50af-b4b5-9b0299a8fd2d` | 91-94 [crates/gwiki/src/scope.rs:91-94] | Indexed function `resolve` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:91-94] |
| `resolve_with_source` | function | `pub fn resolve_with_source(` | `resolve_with_source [function]` | `5246780f-b12a-546b-ac46-5b9a56036486` | 96-121 [crates/gwiki/src/scope.rs:96-121] | Indexed function `resolve_with_source` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:96-121] |
| `resolve_topic` | function | `fn resolve_topic(topic: &str, source: &mut impl ConfigSource) -> Result<ResolvedScope, WikiError> {` | `resolve_topic [function]` | `8369adf2-f7a2-5cee-b10c-7b5d88268db6` | 123-129 [crates/gwiki/src/scope.rs:123-129] | Indexed function `resolve_topic` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:123-129] |
| `resolve_project_from_root` | function | `fn resolve_project_from_root(project_root: &Path) -> Result<ResolvedScope, WikiError> {` | `resolve_project_from_root [function]` | `e9dddd38-4c0e-5808-8d51-d5967cdccf70` | 131-152 [crates/gwiki/src/scope.rs:131-152] | Indexed function `resolve_project_from_root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:131-152] |
| `resolve_hub_path` | function | `fn resolve_hub_path(source: &mut impl ConfigSource) -> Result<PathBuf, WikiError> {` | `resolve_hub_path [function]` | `42aef1ba-d6bc-5ba4-b174-a56bc8939fff` | 154-180 [crates/gwiki/src/scope.rs:154-180] | Indexed function `resolve_hub_path` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:154-180] |
| `default_hub_path` | function | `fn default_hub_path() -> Result<PathBuf, WikiError> {` | `default_hub_path [function]` | `b39a0513-2779-50cb-a55b-4ceb6aed2124` | 182-188 [crates/gwiki/src/scope.rs:182-188] | Indexed function `default_hub_path` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:182-188] |
| `expand_home` | function | `fn expand_home(path: &str) -> Result<PathBuf, WikiError> {` | `expand_home [function]` | `16b08497-6491-5c32-936f-7d3bf6c40bf5` | 190-206 [crates/gwiki/src/scope.rs:190-206] | Indexed function `expand_home` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:190-206] |
| `TestConfig` | class | `struct TestConfig {` | `TestConfig [class]` | `148044f9-8dde-5104-8861-b238d61f687c` | 216-218 [crates/gwiki/src/scope.rs:216-218] | Indexed class `TestConfig` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:216-218] |
| `TestConfig::with` | method | `fn with(key: &str, value: impl Into<String>) -> Self {` | `TestConfig::with [method]` | `46ea0008-11bd-5079-af81-5c0dd0d499ea` | 221-225 [crates/gwiki/src/scope.rs:221-225] | Indexed method `TestConfig::with` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:221-225] |
| `TestConfig::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `TestConfig::config_value [method]` | `96d52b82-2504-5f4d-af92-452cbe1aa3a3` | 229-231 [crates/gwiki/src/scope.rs:229-231] | Indexed method `TestConfig::config_value` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:229-231] |
| `TestConfig::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `TestConfig::resolve_value [method]` | `ca4748d1-1bf8-504f-9827-2e68aa15db5f` | 233-235 [crates/gwiki/src/scope.rs:233-235] | Indexed method `TestConfig::resolve_value` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:233-235] |
| `resolves_global_topic` | function | `fn resolves_global_topic() {` | `resolves_global_topic [function]` | `a10ecaf4-5970-5a31-acdd-d94bc10e2a25` | 240-256 [crates/gwiki/src/scope.rs:240-256] | Indexed function `resolves_global_topic` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:240-256] |
| `rejects_invalid_topic_names` | function | `fn rejects_invalid_topic_names() {` | `rejects_invalid_topic_names [function]` | `7a70fca3-3c59-5dfc-bc45-c6945aef777e` | 259-273 [crates/gwiki/src/scope.rs:259-273] | Indexed function `rejects_invalid_topic_names` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:259-273] |
| `resolves_project_scope_read_only` | function | `fn resolves_project_scope_read_only() {` | `resolves_project_scope_read_only [function]` | `20cff83d-6afa-5dd4-8e40-3f1e575704ce` | 276-312 [crates/gwiki/src/scope.rs:276-312] | Indexed function `resolves_project_scope_read_only` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:276-312] |
| `project_dot_resolves_to_absolute_project_wiki_root` | function | `fn project_dot_resolves_to_absolute_project_wiki_root() {` | `project_dot_resolves_to_absolute_project_wiki_root [function]` | `d43d526a-0a92-5523-bce9-af627dbba0b9` | 315-341 [crates/gwiki/src/scope.rs:315-341] | Indexed function `project_dot_resolves_to_absolute_project_wiki_root` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:315-341] |
