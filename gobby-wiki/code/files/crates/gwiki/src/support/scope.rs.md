---
title: crates/gwiki/src/support/scope.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/scope.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/scope.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/scope.rs` exposes 10 indexed API symbols.

## How it fits

`crates/gwiki/src/support/scope.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `indexed_store_for_selection` | function | Resolves a 'ScopeSelection', loads local index options, optionally indexes the resolved scope root directory into an in-memory wiki store, and returns the resolved scope, output scope identity, search scope, and populated store. [crates/gwiki/src/support/scope.rs:12-36] |
| `ResolvedSelectionContext` | class | 'ResolvedSelectionContext' is an internal struct that bundles the resolved wiki scope, the chosen output scope identity, and the corresponding search scope for a selection operation. [crates/gwiki/src/support/scope.rs:38-42] |
| `resolve_selection_context` | function | Resolves a 'ScopeSelection' into a 'ResolvedSelectionContext' by deriving the command 'scope', its 'output_scope' identity, and a corresponding 'search_scope', then returning them as a single result. [crates/gwiki/src/support/scope.rs:44-55] |
| `search_scope_for_resolved` | function | Returns a 'search::SearchScope' for a resolved wiki scope by applying topic/project precedence, using the topic scope when present, otherwise the project scope, and falling back to 'DEFAULT_PROJECT_ID' for the default project. [crates/gwiki/src/support/scope.rs:60-66] |
| `store_scope_for_search` | function | Converts a 'search::SearchScope' into the corresponding 'store::WikiStoreScope' for 'Project' or 'Topic' scopes, and panics if given 'Global' because it cannot be represented as a scoped wiki store. [crates/gwiki/src/support/scope.rs:68-76] |
| `resolve_command_scope` | function | Resolves a 'ScopeSelection' into a 'wiki_scope::ResolvedScope' by obtaining the process current working directory and delegating to 'wiki_scope::resolve', mapping any 'current_dir' failure into a 'WikiError::Io'. [crates/gwiki/src/support/scope.rs:78-87] |
| `resolved_scope_identity` | function | Returns a 'ScopeIdentity' by applying topic-over-project precedence to a 'ResolvedScope', mapping to the topic identity when a topic wins, to the given project identity when the project wins, or to 'DEFAULT_PROJECT_ID' when the default project applies. [crates/gwiki/src/support/scope.rs:89-95] |
| `scope_includes_page` | function | Returns 'true' for 'ScopeKind::Project' and 'ScopeKind::Global', and for 'ScopeKind::Topic' only when 'path' is under 'knowledge/topics' ('path.starts_with("knowledge/topics")'). [crates/gwiki/src/support/scope.rs:97-102] |
| `ScopePrecedence` | type | Indexed type `ScopePrecedence` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:105-109] |
| `topic_project_precedence` | function | Returns 'ScopePrecedence::Topic(topic)' if 'topic_name' is 'Some', otherwise 'ScopePrecedence::Project(project_id)' if 'project_id' is 'Some', and falls back to 'ScopePrecedence::DefaultProject' when both are 'None'. [crates/gwiki/src/support/scope.rs:111-122] |

