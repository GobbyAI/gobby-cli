---
title: crates/gcode/src/index/import_resolution/parser/mod.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/mod.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/mod.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_import_statement` | function | Dispatches a language-specific import-statement parser based on 'language', updates 'extracted' with resolved or unparsed imports using 'rel_path' and 'import_context', and returns 'Ok(())' unless a delegated parser or unparsed-record insertion fails. [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69] |
| `push_unparsed_import` | function | Validates that a trimmed fallback import string is non-empty and single-line, then records it in 'extracted.imports' as an 'ImportRelation' whose 'module_name' is prefixed with 'UNPARSED_IMPORT_PREFIX', returning an error otherwise. [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89] |
| `seed_import_bindings` | function | Seeds 'bindings.external_roots' from the 'import_context' for supported languages by inserting qualifier-derived 'ExternalRootBinding's for Rust external roots and for Elixir external roots plus non-conflicting overrides, skipping roots shadowed by local module roots. [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141] |
| `resolve_external_callee` | function | Resolves a PHP call expression to an 'ExternalCallTarget' by checking local symbols first and then matching either bare-call imports/wildcard imports or qualified/member imports, returning 'None' when the callee is local or the import source is ambiguous. [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218] |
| `resolve_local_callee` | function | Returns the cloned 'LocalCallBinding' for a bare call name from 'import_bindings.local_bare' only when 'is_bare_call' is true and no symbol with the same name exists in 'symbols', otherwise 'None'. [crates/gcode/src/index/import_resolution/parser/mod.rs:220-233] |
| `resolve_local_member_callee` | function | Returns a 'LocalCallBinding' for a member-call callee only when 'is_member_call' is true, 'root_alias' is present and not shadowed by any local 'Symbol', and 'import_bindings.local_member' contains entries for that alias; otherwise it returns 'None'. [crates/gcode/src/index/import_resolution/parser/mod.rs:235-254] |
| `resolve_ruby_local_member_callee` | function | Returns a 'LocalCallBinding' for a Ruby member call only when 'is_member_call' is true, 'root_alias' is present, no same-file symbol shadows that alias, and the alias resolves to one or more Ruby constant files, using 'root_alias' as the target name for 'new' calls and 'callee_name' otherwise. [crates/gcode/src/index/import_resolution/parser/mod.rs:265-291] |
| `resolve_php_local_member_callee` | function | Returns a 'LocalCallBinding' for a PHP member call only when 'is_member_call' is true and 'qualifier_path' is a non-rooted namespace path containing at least one '\', using the import context’s candidate files for that class path; otherwise it returns 'None'. [crates/gcode/src/index/import_resolution/parser/mod.rs:302-323] |
| `resolve_swift_local_callee` | function | Returns a 'LocalCallBinding' for a bare Swift call by resolving candidate module files from 'ImportResolutionContext' and binding them to 'callee_name', but only when 'is_bare_call' is true and at least one candidate file exists. [crates/gcode/src/index/import_resolution/parser/mod.rs:334-351] |
| `resolve_dart_local_callee` | function | Returns a named 'LocalCallBinding' for a bare call only when there are imported local Dart files and no same-file symbol matches the callee name, after sorting and deduplicating the candidate file list; otherwise it returns 'None'. [crates/gcode/src/index/import_resolution/parser/mod.rs:360-384] |
| `resolve_elixir_local_callee` | function | Resolves an Elixir local callee to a 'LocalCallBinding' by returning the module files for a qualified member call or the deduplicated imported local files for an unqualified bare call, while rejecting non-bare calls, missing imports, empty candidates, and same-file symbols. [crates/gcode/src/index/import_resolution/parser/mod.rs:402-439] |
| `resolve_rust_local_qualified_callee` | function | Returns a qualified local Rust call binding only for member calls by requiring a qualifier path and delegating to 'import_context.rust_qualified_candidate(rel_path, qualifier_path, callee_name)', otherwise returning 'None'. [crates/gcode/src/index/import_resolution/parser/mod.rs:441-453] |
| `resolve_csharp_local_member_callee` | function | Returns a 'LocalCallBinding' for a C# member call only when 'is_member_call' is true, both 'qualifier_path' and 'root_alias' are present, 'root_alias' is not a local symbol, and the qualifier resolves to one or more candidate type files via the import context or local namespaces; otherwise it returns 'None'. [crates/gcode/src/index/import_resolution/parser/mod.rs:469-507] |

