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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/scope.rs:12-36](crates/gwiki/src/support/scope.rs#L12-L36), [crates/gwiki/src/support/scope.rs:38-42](crates/gwiki/src/support/scope.rs#L38-L42), [crates/gwiki/src/support/scope.rs:44-55](crates/gwiki/src/support/scope.rs#L44-L55), [crates/gwiki/src/support/scope.rs:60-66](crates/gwiki/src/support/scope.rs#L60-L66), [crates/gwiki/src/support/scope.rs:68-76](crates/gwiki/src/support/scope.rs#L68-L76), [crates/gwiki/src/support/scope.rs:78-87](crates/gwiki/src/support/scope.rs#L78-L87), [crates/gwiki/src/support/scope.rs:89-95](crates/gwiki/src/support/scope.rs#L89-L95), [crates/gwiki/src/support/scope.rs:97-102](crates/gwiki/src/support/scope.rs#L97-L102), [crates/gwiki/src/support/scope.rs:105-109](crates/gwiki/src/support/scope.rs#L105-L109), [crates/gwiki/src/support/scope.rs:111-122](crates/gwiki/src/support/scope.rs#L111-L122)

</details>

# crates/gwiki/src/support/scope.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Resolves a user’s `ScopeSelection` into the concrete vault scope, output identity, and search scope used by the wiki, then uses that resolution to build an in-memory indexed store when the selected root is a directory. The helpers in the file translate between resolved vault scopes, search/store scope representations, and command precedence rules, with topic scopes taking priority over project scopes and a default project fallback of `"current"`.
[crates/gwiki/src/support/scope.rs:12-36]
[crates/gwiki/src/support/scope.rs:38-42]
[crates/gwiki/src/support/scope.rs:44-55]
[crates/gwiki/src/support/scope.rs:60-66]
[crates/gwiki/src/support/scope.rs:68-76]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `indexed_store_for_selection` | function | `pub(crate) fn indexed_store_for_selection(` | `indexed_store_for_selection [function]` | `8f54063e-8084-55f1-b7d1-bf23dfd5fb0c` | 12-36 [crates/gwiki/src/support/scope.rs:12-36] | Indexed function `indexed_store_for_selection` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:12-36] |
| `ResolvedSelectionContext` | class | `pub(crate) struct ResolvedSelectionContext {` | `ResolvedSelectionContext [class]` | `821fcfba-0b58-5df4-bb53-99251b725b62` | 38-42 [crates/gwiki/src/support/scope.rs:38-42] | Indexed class `ResolvedSelectionContext` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:38-42] |
| `resolve_selection_context` | function | `pub(crate) fn resolve_selection_context(` | `resolve_selection_context [function]` | `c6b77ff9-7bf5-59cd-a76d-7e4e64dd367e` | 44-55 [crates/gwiki/src/support/scope.rs:44-55] | Indexed function `resolve_selection_context` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:44-55] |
| `search_scope_for_resolved` | function | `pub(crate) fn search_scope_for_resolved(scope: &wiki_scope::ResolvedScope) -> search::SearchScope {` | `search_scope_for_resolved [function]` | `48263c4e-f642-5b7b-9ebd-554b1bf614e9` | 60-66 [crates/gwiki/src/support/scope.rs:60-66] | Indexed function `search_scope_for_resolved` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:60-66] |
| `store_scope_for_search` | function | `pub(crate) fn store_scope_for_search(scope: &search::SearchScope) -> store::WikiStoreScope {` | `store_scope_for_search [function]` | `f7e64c9b-bd8c-56a3-85e1-a58a9e27c5ec` | 68-76 [crates/gwiki/src/support/scope.rs:68-76] | Indexed function `store_scope_for_search` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:68-76] |
| `resolve_command_scope` | function | `pub(crate) fn resolve_command_scope(` | `resolve_command_scope [function]` | `1a05aa2b-117b-54d7-849b-2696e6197f32` | 78-87 [crates/gwiki/src/support/scope.rs:78-87] | Indexed function `resolve_command_scope` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:78-87] |
| `resolved_scope_identity` | function | `pub(crate) fn resolved_scope_identity(scope: &wiki_scope::ResolvedScope) -> ScopeIdentity {` | `resolved_scope_identity [function]` | `b5b3766e-efe7-5e0f-a92e-2813c361acfd` | 89-95 [crates/gwiki/src/support/scope.rs:89-95] | Indexed function `resolved_scope_identity` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:89-95] |
| `scope_includes_page` | function | `pub(crate) fn scope_includes_page(scope: &ScopeIdentity, path: &Path) -> bool {` | `scope_includes_page [function]` | `cfa277c0-f6f7-5eed-8532-63622bc7b822` | 97-102 [crates/gwiki/src/support/scope.rs:97-102] | Indexed function `scope_includes_page` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:97-102] |
| `ScopePrecedence` | type | `enum ScopePrecedence<'a> {` | `ScopePrecedence [type]` | `0b81337a-18a6-53c5-b6fa-fd3e0d49c61c` | 105-109 [crates/gwiki/src/support/scope.rs:105-109] | Indexed type `ScopePrecedence` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:105-109] |
| `topic_project_precedence` | function | `fn topic_project_precedence<'a>(` | `topic_project_precedence [function]` | `3bcc6db3-11eb-5919-8bfe-ee76e46c64b8` | 111-122 [crates/gwiki/src/support/scope.rs:111-122] | Indexed function `topic_project_precedence` in `crates/gwiki/src/support/scope.rs`. [crates/gwiki/src/support/scope.rs:111-122] |
