---
title: crates/gwiki/src/support/scope.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/scope.rs
  ranges:
  - 12-36
  - 38-42
  - 44-55
  - 60-66
  - 68-76
  - 78-87
  - 89-95
  - 97-102
  - 105-109
  - 111-122
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/scope.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

Provides scope-resolution helpers for gwiki commands: it turns a user’s `ScopeSelection` into a resolved wiki scope, an output `ScopeIdentity`, and a matching search scope, then optionally indexes the vault root into an in-memory wiki store. The helpers keep topic/project precedence consistent across search and storage, map resolved scopes back to identities, and enforce that global search scopes are not converted into scoped stores.
[crates/gwiki/src/support/scope.rs:12-36]
[crates/gwiki/src/support/scope.rs:38-42]
[crates/gwiki/src/support/scope.rs:44-55]
[crates/gwiki/src/support/scope.rs:60-66]
[crates/gwiki/src/support/scope.rs:68-76]

## API Symbols

- `indexed_store_for_selection` (function) component `indexed_store_for_selection [function]` (`8f54063e-8084-55f1-b7d1-bf23dfd5fb0c`) lines 12-36 [crates/gwiki/src/support/scope.rs:12-36]
  - Signature: `pub(crate) fn indexed_store_for_selection(`
  - Purpose: Resolves a scope selection and returns the resolved scope context along with an in-memory wiki store indexed from the vault root directory. [crates/gwiki/src/support/scope.rs:12-36]
- `ResolvedSelectionContext` (class) component `ResolvedSelectionContext [class]` (`821fcfba-0b58-5df4-bb53-99251b725b62`) lines 38-42 [crates/gwiki/src/support/scope.rs:38-42]
  - Signature: `pub(crate) struct ResolvedSelectionContext {`
  - Purpose: A crate-private struct that aggregates a resolved wiki scope, output scope identity, and search scope for selection context. [crates/gwiki/src/support/scope.rs:38-42]
- `resolve_selection_context` (function) component `resolve_selection_context [function]` (`c6b77ff9-7bf5-59cd-a76d-7e4e64dd367e`) lines 44-55 [crates/gwiki/src/support/scope.rs:44-55]
  - Signature: `pub(crate) fn resolve_selection_context(`
  - Purpose: Resolves a 'ScopeSelection' into a 'ResolvedSelectionContext' by deriving the command 'scope', its 'output_scope' identity, and the corresponding 'search_scope', or returns a 'WikiError' if scope resolution fails. [crates/gwiki/src/support/scope.rs:44-55]
- `search_scope_for_resolved` (function) component `search_scope_for_resolved [function]` (`48263c4e-f642-5b7b-9ebd-554b1bf614e9`) lines 60-66 [crates/gwiki/src/support/scope.rs:60-66]
  - Signature: `pub(crate) fn search_scope_for_resolved(scope: &wiki_scope::ResolvedScope) -> search::SearchScope {`
  - Purpose: Converts a 'ResolvedScope' into a 'SearchScope' by evaluating topic-project precedence and returning the appropriate topic-scoped, project-scoped, or default-project-scoped search context. [crates/gwiki/src/support/scope.rs:60-66]
- `store_scope_for_search` (function) component `store_scope_for_search [function]` (`f7e64c9b-bd8c-56a3-85e1-a58a9e27c5ec`) lines 68-76 [crates/gwiki/src/support/scope.rs:68-76]
  - Signature: `pub(crate) fn store_scope_for_search(scope: &search::SearchScope) -> store::WikiStoreScope {`
  - Purpose: Converts a non-Global 'search::SearchScope' to 'store::WikiStoreScope' by delegating Project and Topic variants to their corresponding constructors, panicking on Global scope. [crates/gwiki/src/support/scope.rs:68-76]
- `resolve_command_scope` (function) component `resolve_command_scope [function]` (`1a05aa2b-117b-54d7-849b-2696e6197f32`) lines 78-87 [crates/gwiki/src/support/scope.rs:78-87]
  - Signature: `pub(crate) fn resolve_command_scope(`
  - Purpose: Reads the process current directory, converts any 'std::env::current_dir' failure into 'WikiError::Io { action: "read current directory" }', and then resolves the given 'ScopeSelection' via 'wiki_scope::resolve(selection, &cwd)'. [crates/gwiki/src/support/scope.rs:78-87]
- `resolved_scope_identity` (function) component `resolved_scope_identity [function]` (`b5b3766e-efe7-5e0f-a92e-2813c361acfd`) lines 89-95 [crates/gwiki/src/support/scope.rs:89-95]
  - Signature: `pub(crate) fn resolved_scope_identity(scope: &wiki_scope::ResolvedScope) -> ScopeIdentity {`
  - Purpose: Maps a 'wiki_scope::ResolvedScope' to a 'ScopeIdentity' by applying 'topic_project_precedence' to its topic name and project ID, yielding a topic identity, a project identity, or the 'DEFAULT_PROJECT_ID' project identity for the default case. [crates/gwiki/src/support/scope.rs:89-95]
- `scope_includes_page` (function) component `scope_includes_page [function]` (`cfa277c0-f6f7-5eed-8532-63622bc7b822`) lines 97-102 [crates/gwiki/src/support/scope.rs:97-102]
  - Signature: `pub(crate) fn scope_includes_page(scope: &ScopeIdentity, path: &Path) -> bool {`
  - Purpose: 'scope_includes_page' returns 'true' for all 'Project' and 'Global' scopes, and for 'Topic' scopes only when 'path' starts with 'knowledge/topics'. [crates/gwiki/src/support/scope.rs:97-102]
- `ScopePrecedence` (type) component `ScopePrecedence [type]` (`0b81337a-18a6-53c5-b6fa-fd3e0d49c61c`) lines 105-109 [crates/gwiki/src/support/scope.rs:105-109]
  - Signature: `enum ScopePrecedence<'a> {`
  - Purpose: Indexed type `ScopePrecedence` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:105-109]
- `topic_project_precedence` (function) component `topic_project_precedence [function]` (`3bcc6db3-11eb-5919-8bfe-ee76e46c64b8`) lines 111-122 [crates/gwiki/src/support/scope.rs:111-122]
  - Signature: `fn topic_project_precedence<'a>(`
  - Purpose: Returns 'ScopePrecedence::Topic(topic)' if 'topic_name' is 'Some', otherwise 'ScopePrecedence::Project(project_id)' if 'project_id' is 'Some', and 'ScopePrecedence::DefaultProject' when both are 'None'. [crates/gwiki/src/support/scope.rs:111-122]

