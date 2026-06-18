---
title: crates/gwiki/src/scope.rs
type: code_file
provenance:
- file: crates/gwiki/src/scope.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/scope.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/scope.rs` exposes 26 indexed API symbols.

## How it fits

`crates/gwiki/src/scope.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ResolvedScope` | class | 'ResolvedScope' is a struct representing a fully resolved scope, identified by a 'ScopeKind' and two filesystem paths: 'root' and 'registry_path'. [crates/gwiki/src/scope.rs:12-16] |
| `ScopeKind` | type | Indexed type `ScopeKind` in `crates/gwiki/src/scope.rs`. [crates/gwiki/src/scope.rs:19-27] |
| `ResolvedScope::topic` | method | Constructs and returns a 'Self' value representing a 'Topic' scope by setting 'kind' to 'ScopeKind::Topic { name }' and storing the provided 'root' and 'registry_path' paths. [crates/gwiki/src/scope.rs:30-36] |
| `ResolvedScope::project` | method | Constructs and returns a 'Self' value for a project scope by storing 'project_id' and 'project_root' in 'ScopeKind::Project', preserving 'root', and setting 'registry_path' to 'root.join("wikis.json")'. [crates/gwiki/src/scope.rs:38-48] |
| `ResolvedScope::kind` | method | Returns an immutable reference to the 'ScopeKind' stored in 'self.kind'. [crates/gwiki/src/scope.rs:50-52] |
| `ResolvedScope::root` | method | Returns an immutable reference to the 'Path' stored in 'self.root'. [crates/gwiki/src/scope.rs:54-56] |
| `ResolvedScope::registry_path` | method | Returns an immutable '&Path' reference to the 'registry_path' field of 'self'. [crates/gwiki/src/scope.rs:58-60] |
| `ResolvedScope::identity` | method | Returns a 'String' identifier for the scope, formatted as 'topic:{name}' when 'self.kind' is 'ScopeKind::Topic' and 'project:{project_id}' when it is 'ScopeKind::Project'. [crates/gwiki/src/scope.rs:62-67] |
| `ResolvedScope::topic_name` | method | Returns 'Some(&str)' with the topic name when 'self.kind' is 'ScopeKind::Topic { name }', and 'None' when 'self.kind' is 'ScopeKind::Project { .. }'. [crates/gwiki/src/scope.rs:69-74] |
| `ResolvedScope::project_id` | method | Returns 'None' when 'self.kind' is 'ScopeKind::Topic' and 'Some(project_id)' when it is 'ScopeKind::Project', exposing the project's ID as an 'Option<&str>'. [crates/gwiki/src/scope.rs:76-81] |
| `ResolvedScope::project_root` | method | Returns 'Some(&Path)' containing the stored project root when the scope is 'Project', and 'None' when the scope is 'Topic'. [crates/gwiki/src/scope.rs:83-88] |
| `resolve` | function | 'resolve' constructs an 'EnvOnlySource' and delegates to 'resolve_with_source(selection, cwd, &mut source)' to produce a 'Result<ResolvedScope, WikiError>'. [crates/gwiki/src/scope.rs:91-94] |
| `resolve_with_source` | function | Resolves a 'ScopeSelection' to a 'ResolvedScope' by preferring an explicit topic, then an explicit project root normalized against 'cwd' if relative, then the nearest project root discovered from 'cwd', and otherwise returns 'WikiError::InvalidScope'. [crates/gwiki/src/scope.rs:96-121] |
| `resolve_topic` | function | Validates the topic name, resolves the hub path from the config source, builds the topic root at 'hub/topics/<topic>', and returns a 'ResolvedScope::topic' using that root and 'hub/wikis.json'. [crates/gwiki/src/scope.rs:123-129] |
| `resolve_project_from_root` | function | Canonicalizes 'project_root', reads and validates the project ID from that directory, constructs the wiki root at 'project_root/gobby-wiki', and returns 'ResolvedScope::project परियोजना_id, project_root, root', mapping any failure to 'WikiError::InvalidScope' with context. [crates/gwiki/src/scope.rs:131-152] |
| `resolve_hub_path` | function | Returns the hub path from the non-empty 'HUB_ENV' environment variable if set, expanding a leading '~'/'~/', otherwise scans configured keys for the first non-empty resolved value and expands its home reference, falling back to 'default_hub_path()', with config resolution failures wrapped in 'WikiError::Config'. [crates/gwiki/src/scope.rs:154-180] |
| `default_hub_path` | function | Returns the current user’s home directory joined with 'wiki', or a 'WikiError::Config' if 'dirs::home_dir()' cannot determine 'HOME'. [crates/gwiki/src/scope.rs:182-188] |
| `expand_home` | function | Expands a path by replacing '~' or '~/...' with the current home directory from 'dirs::home_dir()', returning a 'WikiError::Config' if 'HOME' is unset, and otherwise leaving non-home-prefixed paths unchanged as a 'PathBuf'. [crates/gwiki/src/scope.rs:190-206] |
| `TestConfig` | class | 'TestConfig' is a struct that stores configuration entries as a 'HashMap<String, String>' named 'values'. [crates/gwiki/src/scope.rs:216-218] |
| `TestConfig::with` | method | Constructs and returns a new 'Self' whose 'values' field is a 'HashMap' initialized with a single entry mapping 'key.to_string()' to 'value.into()'. [crates/gwiki/src/scope.rs:221-225] |
| `TestConfig::config_value` | method | Returns a cloned 'String' from 'self.values' for the given 'key' if present, otherwise 'None'. [crates/gwiki/src/scope.rs:229-231] |
| `TestConfig::resolve_value` | method | 'resolve_value' takes a string slice and returns an 'Ok'-wrapped owned 'String' containing the same value unchanged. [crates/gwiki/src/scope.rs:233-235] |
| `resolves_global_topic` | function | Verifies that resolving the topic scope 'rust-async' with 'HUB_ENV' unset uses the configured hub path to produce a 'topic:rust-async' scope rooted at '<hub>/topics/rust-async' with registry path '<hub>/wikis.json'. [crates/gwiki/src/scope.rs:240-256] |
| `rejects_invalid_topic_names` | function | Verifies that 'resolve_with_source' rejects invalid topic scope names ('.', '..', path separators, and ':') by returning 'WikiError::InvalidScope' for each case. [crates/gwiki/src/scope.rs:259-273] |
| `resolves_project_scope_read_only` | function | Verifies that resolving a project scope from a nested path returns the canonical 'gobby-wiki' root and 'project:project-123' identity without modifying '.gobby/gcode.json' or initializing a 'gobby-wiki' vault under the project. [crates/gwiki/src/scope.rs:276-312] |
| `project_dot_resolves_to_absolute_project_wiki_root` | function | It verifies that resolving a project scope from '.' returns an absolute wiki root under the canonicalized project directory ('<project>/gobby-wiki') and that 'project_root()' matches the canonical project path. [crates/gwiki/src/scope.rs:315-341] |

