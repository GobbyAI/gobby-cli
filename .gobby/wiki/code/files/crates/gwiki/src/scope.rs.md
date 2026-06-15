---
title: crates/gwiki/src/scope.rs
type: code_file
provenance:
- file: crates/gwiki/src/scope.rs
  ranges:
  - 12-16
  - 19-27
  - 29-89
  - 91-94
  - 96-121
  - 123-129
  - 131-152
  - 154-180
  - 182-188
  - 190-206
  - 216-218
  - 220-226
  - 228-236
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

This file defines the scope model and resolution logic for wiki locations. `ResolvedScope` is an immutable wrapper that represents either a topic or a project, carrying the scope kind plus resolved root and registry paths, while `ScopeKind` distinguishes those two variants and supports typed accessors and stable identity strings like `topic:...` or `project:...`. The resolver functions build a scope from a selection by preferring an explicit topic, then an explicit project root, then the nearest project found from the current directory, with helpers for validating names, locating the hub path from environment/config/fallbacks, expanding `~`, and mapping failures to `WikiError`. The test-only `TestConfig` provides a minimal `ConfigSource` stub, and the unit tests cover topic resolution, invalid names, and project-root canonicalization behavior.
[crates/gwiki/src/scope.rs:12-16]
[crates/gwiki/src/scope.rs:19-27]
[crates/gwiki/src/scope.rs:29-89]
[crates/gwiki/src/scope.rs:30-36]
[crates/gwiki/src/scope.rs:38-48]

## API Symbols

- `ResolvedScope` (class) component `ResolvedScope [class]` (`b6881cd1-180e-59ec-a7b0-212f5ced07ef`) lines 12-16 [crates/gwiki/src/scope.rs:12-16]
  - Signature: `pub struct ResolvedScope {`
  - Purpose: 'ResolvedScope' is a Rust struct that represents a resolved scope by storing its 'ScopeKind', the scope root 'PathBuf', and the associated 'registry_path' 'PathBuf'. [crates/gwiki/src/scope.rs:12-16]
- `ScopeKind` (type) component `ScopeKind [type]` (`575e21d1-e0ce-5fcb-be51-56759d4e7d38`) lines 19-27 [crates/gwiki/src/scope.rs:19-27]
  - Signature: `pub enum ScopeKind {`
  - Purpose: Indexed type `ScopeKind` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:19-27]
- `ResolvedScope` (class) component `ResolvedScope [class]` (`778bd417-8546-5230-8688-c7058e6c1e40`) lines 29-89 [crates/gwiki/src/scope.rs:29-89]
  - Signature: `impl ResolvedScope {`
  - Purpose: 'ResolvedScope' is an immutable scope wrapper that represents either a topic or project, stores the resolved root and registry path, derives a stable string identity, and exposes typed accessors for the underlying scope kind and project/topic-specific fields. [crates/gwiki/src/scope.rs:29-89]
- `ResolvedScope.topic` (method) component `ResolvedScope.topic [method]` (`77fb16d7-3240-52b8-80b2-ae698bd465da`) lines 30-36 [crates/gwiki/src/scope.rs:30-36]
  - Signature: `pub fn topic(name: String, root: PathBuf, registry_path: PathBuf) -> Self {`
  - Purpose: Constructs and returns a 'Self' value with 'kind' set to 'ScopeKind::Topic { name }' and the provided 'root' and 'registry_path' paths assigned unchanged. [crates/gwiki/src/scope.rs:30-36]
- `ResolvedScope.project` (method) component `ResolvedScope.project [method]` (`4b631375-70bc-5005-9763-729c06674865`) lines 38-48 [crates/gwiki/src/scope.rs:38-48]
  - Signature: `pub fn project(project_id: String, project_root: PathBuf, root: PathBuf) -> Self {`
  - Purpose: Constructs a 'Self' value with 'kind' set to 'ScopeKind::Project { project_id, project_root }', 'root' set to the provided 'root', and 'registry_path' initialized to 'root.join("wikis.json")'. [crates/gwiki/src/scope.rs:38-48]
- `ResolvedScope.kind` (method) component `ResolvedScope.kind [method]` (`1b17d6da-7efc-5c05-9574-038d1e65b423`) lines 50-52 [crates/gwiki/src/scope.rs:50-52]
  - Signature: `pub fn kind(&self) -> &ScopeKind {`
  - Purpose: Returns an immutable reference to the 'ScopeKind' stored in 'self.kind'. [crates/gwiki/src/scope.rs:50-52]
- `ResolvedScope.root` (method) component `ResolvedScope.root [method]` (`37dfd9b0-081a-5bce-8f6d-5818a8fade56`) lines 54-56 [crates/gwiki/src/scope.rs:54-56]
  - Signature: `pub fn root(&self) -> &Path {`
  - Purpose: Returns an immutable reference to the 'Path' stored in 'self.root'. [crates/gwiki/src/scope.rs:54-56]
- `ResolvedScope.registry_path` (method) component `ResolvedScope.registry_path [method]` (`f21f4274-cdee-5186-9324-a4ddcc9fe196`) lines 58-60 [crates/gwiki/src/scope.rs:58-60]
  - Signature: `pub fn registry_path(&self) -> &Path {`
  - Purpose: Returns an immutable '&Path' reference to the instance’s 'registry_path' field. [crates/gwiki/src/scope.rs:58-60]
- `ResolvedScope.identity` (method) component `ResolvedScope.identity [method]` (`2b30364a-e0f4-5707-a30e-75d6d29f96a9`) lines 62-67 [crates/gwiki/src/scope.rs:62-67]
  - Signature: `pub fn identity(&self) -> String {`
  - Purpose: Returns a 'String' encoding the scope identity as 'topic:{name}' for 'ScopeKind::Topic' or 'project:{project_id}' for 'ScopeKind::Project'. [crates/gwiki/src/scope.rs:62-67]
- `ResolvedScope.topic_name` (method) component `ResolvedScope.topic_name [method]` (`63d82ca1-2701-57df-9f88-9ea8bd9177c1`) lines 69-74 [crates/gwiki/src/scope.rs:69-74]
  - Signature: `pub fn topic_name(&self) -> Option<&str> {`
  - Purpose: Returns 'Some(&str)' containing the topic name when 'self.kind' is 'ScopeKind::Topic', and 'None' when it is 'ScopeKind::Project'. [crates/gwiki/src/scope.rs:69-74]
- `ResolvedScope.project_id` (method) component `ResolvedScope.project_id [method]` (`c6220f0e-1409-502f-8914-bbae838dd237`) lines 76-81 [crates/gwiki/src/scope.rs:76-81]
  - Signature: `pub fn project_id(&self) -> Option<&str> {`
  - Purpose: Returns the project ID string slice for 'ScopeKind::Project' variants and 'None' for 'ScopeKind::Topic' variants. [crates/gwiki/src/scope.rs:76-81]
- `ResolvedScope.project_root` (method) component `ResolvedScope.project_root [method]` (`acf3301d-7ab1-52c5-9628-a15cec64ed55`) lines 83-88 [crates/gwiki/src/scope.rs:83-88]
  - Signature: `pub fn project_root(&self) -> Option<&Path> {`
  - Purpose: Returns 'None' for 'ScopeKind::Topic' and 'Some(project_root)' for 'ScopeKind::Project', exposing the scope’s project root path when the scope represents a project. [crates/gwiki/src/scope.rs:83-88]
- `resolve` (function) component `resolve [function]` (`f988ece6-c5c2-50af-b4b5-9b0299a8fd2d`) lines 91-94 [crates/gwiki/src/scope.rs:91-94]
  - Signature: `pub fn resolve(selection: &ScopeSelection, cwd: &Path) -> Result<ResolvedScope, WikiError> {`
  - Purpose: 'resolve' constructs an 'EnvOnlySource' and delegates to 'resolve_with_source' to resolve the given 'ScopeSelection' against 'cwd', returning a 'ResolvedScope' or 'WikiError'. [crates/gwiki/src/scope.rs:91-94]
- `resolve_with_source` (function) component `resolve_with_source [function]` (`5246780f-b12a-546b-ac46-5b9a56036486`) lines 96-121 [crates/gwiki/src/scope.rs:96-121]
  - Signature: `pub fn resolve_with_source(`
  - Purpose: Resolves a wiki scope by preferring an explicit topic, then an explicit project root normalized against 'cwd', then the nearest project root discovered from 'cwd', and returns 'InvalidScope' if none is available. [crates/gwiki/src/scope.rs:96-121]
- `resolve_topic` (function) component `resolve_topic [function]` (`8369adf2-f7a2-5cee-b10c-7b5d88268db6`) lines 123-129 [crates/gwiki/src/scope.rs:123-129]
  - Signature: `fn resolve_topic(topic: &str, source: &mut impl ConfigSource) -> Result<ResolvedScope, WikiError> {`
  - Purpose: Validates the topic name, resolves the hub path from the config source, and returns a 'ResolvedScope' for the topic using 'hub/topics/<topic>' as the root and 'hub/wikis.json' as the wiki index path. [crates/gwiki/src/scope.rs:123-129]
- `resolve_project_from_root` (function) component `resolve_project_from_root [function]` (`e9dddd38-4c0e-5808-8d51-d5967cdccf70`) lines 131-152 [crates/gwiki/src/scope.rs:131-152]
  - Signature: `fn resolve_project_from_root(project_root: &Path) -> Result<ResolvedScope, WikiError> {`
  - Purpose: Canonicalizes 'project_root', reads and validates the project ID from that directory, constructs the wiki root at '<project_root>/.gobby/wiki', and returns a 'ResolvedScope::project' or maps any failure to 'WikiError::InvalidScope'. [crates/gwiki/src/scope.rs:131-152]
- `resolve_hub_path` (function) component `resolve_hub_path [function]` (`42aef1ba-d6bc-5ba4-b174-a56bc8939fff`) lines 154-180 [crates/gwiki/src/scope.rs:154-180]
  - Signature: `fn resolve_hub_path(source: &mut impl ConfigSource) -> Result<PathBuf, WikiError> {`
  - Purpose: Resolves the hub path by preferring a non-empty 'HUB_ENV' environment variable, then the first non-blank resolved config value from 'HUB_CONFIG_KEYS' with '~' expansion, and finally falling back to 'default_hub_path()', returning a 'WikiError::Config' if config resolution fails. [crates/gwiki/src/scope.rs:154-180]
- `default_hub_path` (function) component `default_hub_path [function]` (`b39a0513-2779-50cb-a55b-4ceb6aed2124`) lines 182-188 [crates/gwiki/src/scope.rs:182-188]
  - Signature: `fn default_hub_path() -> Result<PathBuf, WikiError> {`
  - Purpose: Returns the user’s home directory joined with 'wiki', or a 'WikiError::Config' if 'dirs::home_dir()' cannot determine 'HOME'. [crates/gwiki/src/scope.rs:182-188]
- `expand_home` (function) component `expand_home [function]` (`16b08497-6491-5c32-936f-7d3bf6c40bf5`) lines 190-206 [crates/gwiki/src/scope.rs:190-206]
  - Signature: `fn expand_home(path: &str) -> Result<PathBuf, WikiError> {`
  - Purpose: Expands a leading '~' or '~/' in 'path' to the current user's home directory, returning a 'WikiError::Config' if 'HOME' is unavailable, and otherwise returns the original path as a 'PathBuf' unchanged. [crates/gwiki/src/scope.rs:190-206]
- `TestConfig` (class) component `TestConfig [class]` (`148044f9-8dde-5104-8861-b238d61f687c`) lines 216-218 [crates/gwiki/src/scope.rs:216-218]
  - Signature: `struct TestConfig {`
  - Purpose: 'TestConfig' is a struct that stores configuration entries as a 'HashMap<String, String>' named 'values'. [crates/gwiki/src/scope.rs:216-218]
- `TestConfig` (class) component `TestConfig [class]` (`efc0e285-50b8-56d8-b559-e2a3d4d90335`) lines 220-226 [crates/gwiki/src/scope.rs:220-226]
  - Signature: `impl TestConfig {`
  - Purpose: 'TestConfig' is a helper constructor wrapper that creates a configuration instance whose 'values' field is initialized to a single 'key -> value' entry in a 'HashMap'. [crates/gwiki/src/scope.rs:220-226]
- `TestConfig.with` (method) component `TestConfig.with [method]` (`46ea0008-11bd-5079-af81-5c0dd0d499ea`) lines 221-225 [crates/gwiki/src/scope.rs:221-225]
  - Signature: `fn with(key: &str, value: impl Into<String>) -> Self {`
  - Purpose: Constructs and returns a new 'Self' instance whose 'values' field is initialized to a 'HashMap' containing a single entry mapping 'key.to_string()' to 'value.into()'. [crates/gwiki/src/scope.rs:221-225]
- `TestConfig` (class) component `TestConfig [class]` (`f9a70748-882b-5a6f-bffc-f7170c5de579`) lines 228-236 [crates/gwiki/src/scope.rs:228-236]
  - Signature: `impl ConfigSource for TestConfig {`
  - Purpose: 'TestConfig' is a 'ConfigSource' test double that returns cloned values from an internal key-value map via 'config_value' and performs no resolution, passing 'resolve_value' inputs through unchanged as 'Ok(String)'. [crates/gwiki/src/scope.rs:228-236]
- `TestConfig.config_value` (method) component `TestConfig.config_value [method]` (`96d52b82-2504-5f4d-af92-452cbe1aa3a3`) lines 229-231 [crates/gwiki/src/scope.rs:229-231]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Returns a cloned 'String' from 'self.values' for the given 'key', or 'None' if the key is absent. [crates/gwiki/src/scope.rs:229-231]
- `TestConfig.resolve_value` (method) component `TestConfig.resolve_value [method]` (`ca4748d1-1bf8-504f-9827-2e68aa15db5f`) lines 233-235 [crates/gwiki/src/scope.rs:233-235]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Returns an owned 'String' by cloning the input '&str' and wrapping it in 'Ok' without performing any resolution or transformation. [crates/gwiki/src/scope.rs:233-235]
- `resolves_global_topic` (function) component `resolves_global_topic [function]` (`a10ecaf4-5970-5a31-acdd-d94bc10e2a25`) lines 240-256 [crates/gwiki/src/scope.rs:240-256]
  - Signature: `fn resolves_global_topic() {`
  - Purpose: Verifies that resolving a topic scope without 'HUB_ENV' uses the configured hub path to produce the global topic identity 'topic:rust-async', with its root at '<hub>/topics/rust-async' and registry at '<hub>/wikis.json'. [crates/gwiki/src/scope.rs:240-256]
- `rejects_invalid_topic_names` (function) component `rejects_invalid_topic_names [function]` (`7a70fca3-3c59-5dfc-bc45-c6945aef777e`) lines 259-273 [crates/gwiki/src/scope.rs:259-273]
  - Signature: `fn rejects_invalid_topic_names() {`
  - Purpose: Verifies that resolving a topic scope rejects invalid topic names such as '"."', '".."', path-separators, and '":"' by returning 'WikiError::InvalidScope'. [crates/gwiki/src/scope.rs:259-273]
- `resolves_project_scope_read_only` (function) component `resolves_project_scope_read_only [function]` (`20cff83d-6afa-5dd4-8e40-3f1e575704ce`) lines 276-312 [crates/gwiki/src/scope.rs:276-312]
  - Signature: `fn resolves_project_scope_read_only() {`
  - Purpose: Verifies that resolving a project scope from a nested path yields the canonical '.gobby/wiki' root and 'project:project-123' identity without modifying 'gcode.json' or initializing the vault on disk. [crates/gwiki/src/scope.rs:276-312]
- `project_dot_resolves_to_absolute_project_wiki_root` (function) component `project_dot_resolves_to_absolute_project_wiki_root [function]` (`d43d526a-0a92-5523-bce9-af627dbba0b9`) lines 315-341 [crates/gwiki/src/scope.rs:315-341]
  - Signature: `fn project_dot_resolves_to_absolute_project_wiki_root() {`
  - Purpose: Verifies that resolving 'ScopeSelection::project(".")' for a project with '.gobby/gcode.json' yields the canonical project root and an absolute wiki root at '<project>/.gobby/wiki', not a relative path. [crates/gwiki/src/scope.rs:315-341]

