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
  - 89-96
  - 98-104
  - 106-111
  - 114-118
  - 120-131
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/scope.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

`crates/gwiki/src/support/scope.rs` exposes 11 indexed API symbols.
[crates/gwiki/src/support/scope.rs:12-36]
[crates/gwiki/src/support/scope.rs:38-42]
[crates/gwiki/src/support/scope.rs:44-55]
[crates/gwiki/src/support/scope.rs:60-66]
[crates/gwiki/src/support/scope.rs:68-76]

## API Symbols

- `indexed_store_for_selection` (function) component `indexed_store_for_selection [function]` (`df141688-ee38-5b52-bd23-fc11a48ce4d9`) lines 12-36 [crates/gwiki/src/support/scope.rs:12-36]
  - Signature: `pub(crate) fn indexed_store_for_selection(`
  - Purpose: Indexed function `indexed_store_for_selection` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:12-36]
- `ResolvedSelectionContext` (class) component `ResolvedSelectionContext [class]` (`1d240702-63f1-5372-b4ca-5c3c97aa6710`) lines 38-42 [crates/gwiki/src/support/scope.rs:38-42]
  - Signature: `pub(crate) struct ResolvedSelectionContext {`
  - Purpose: Indexed class `ResolvedSelectionContext` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:38-42]
- `resolve_selection_context` (function) component `resolve_selection_context [function]` (`ab45668c-9fc1-537d-a96d-8f07bce81dff`) lines 44-55 [crates/gwiki/src/support/scope.rs:44-55]
  - Signature: `pub(crate) fn resolve_selection_context(`
  - Purpose: Indexed function `resolve_selection_context` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:44-55]
- `search_scope_for_resolved` (function) component `search_scope_for_resolved [function]` (`25edf047-b574-5d44-ba5d-42891d7cc8f1`) lines 60-66 [crates/gwiki/src/support/scope.rs:60-66]
  - Signature: `pub(crate) fn search_scope_for_resolved(scope: &wiki_scope::ResolvedScope) -> search::SearchScope {`
  - Purpose: Indexed function `search_scope_for_resolved` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:60-66]
- `store_scope_for_search` (function) component `store_scope_for_search [function]` (`c5a00368-428f-5a21-a914-ad69e9e221b6`) lines 68-76 [crates/gwiki/src/support/scope.rs:68-76]
  - Signature: `pub(crate) fn store_scope_for_search(scope: &search::SearchScope) -> store::WikiStoreScope {`
  - Purpose: Indexed function `store_scope_for_search` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:68-76]
- `resolve_command_scope` (function) component `resolve_command_scope [function]` (`118423b2-f7d5-5894-9213-cc544048ccdd`) lines 78-87 [crates/gwiki/src/support/scope.rs:78-87]
  - Signature: `pub(crate) fn resolve_command_scope(`
  - Purpose: Indexed function `resolve_command_scope` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:78-87]
- `research_scope_identity` (function) component `research_scope_identity [function]` (`9b22dbcb-071f-5cd1-a54b-31ba0a2d822d`) lines 89-96 [crates/gwiki/src/support/scope.rs:89-96]
  - Signature: `pub(crate) fn research_scope_identity(scope: &session::ResearchScope) -> ScopeIdentity {`
  - Purpose: Indexed function `research_scope_identity` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:89-96]
- `resolved_scope_identity` (function) component `resolved_scope_identity [function]` (`cdee2a59-85c5-5e73-aa95-10ee01910ed1`) lines 98-104 [crates/gwiki/src/support/scope.rs:98-104]
  - Signature: `pub(crate) fn resolved_scope_identity(scope: &wiki_scope::ResolvedScope) -> ScopeIdentity {`
  - Purpose: Indexed function `resolved_scope_identity` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:98-104]
- `scope_includes_page` (function) component `scope_includes_page [function]` (`b8f5ad0f-186e-5868-9916-49a43410ac45`) lines 106-111 [crates/gwiki/src/support/scope.rs:106-111]
  - Signature: `pub(crate) fn scope_includes_page(scope: &ScopeIdentity, path: &Path) -> bool {`
  - Purpose: Indexed function `scope_includes_page` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:106-111]
- `ScopePrecedence` (type) component `ScopePrecedence [type]` (`c3447c4f-1834-5fe7-9778-2f7f050e52ad`) lines 114-118 [crates/gwiki/src/support/scope.rs:114-118]
  - Signature: `enum ScopePrecedence<'a> {`
  - Purpose: Indexed type `ScopePrecedence` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:114-118]
- `topic_project_precedence` (function) component `topic_project_precedence [function]` (`8aff6269-e2ef-544a-affd-1f6e579c81b1`) lines 120-131 [crates/gwiki/src/support/scope.rs:120-131]
  - Signature: `fn topic_project_precedence<'a>(`
  - Purpose: Indexed function `topic_project_precedence` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:120-131]

