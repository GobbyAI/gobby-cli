---
title: crates/gcode/src/index/parser/calls.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser/calls.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser/calls.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CallExtractionContext` | class | 'CallExtractionContext<'a>' is a borrowed, internal context bundle that supplies language, Tree-sitter grammar, file/path metadata, symbol table, and import-resolution state needed to extract calls from a source file. [crates/gcode/src/index/parser/calls.rs:26-35] |
| `CallSite` | class | 'CallSite' is a struct that records the resolved callee identity and source-location metadata for a call expression, including the callee name, optional qualifier path, byte offsets for the name and scope, line number, and the call syntax kind. [crates/gcode/src/index/parser/calls.rs:38-45] |
| `extract_calls` | function | Dispatches call extraction to the Dart textual extractor, the Objective-C AST extractor, or the generic AST extractor based on 'ctx.language', returning a 'Vec<CallRelation>' or an error. [crates/gcode/src/index/parser/calls.rs:47-61] |
| `materialize_call` | function | 'materialize_call' resolves a call site into a 'CallRelation' by identifying the enclosing caller symbol, normalizing Lua 'require' qualifiers, resolving same-file and external callees while accounting for import bindings and shadowing, and then materializing the relation from those candidates. [crates/gcode/src/index/parser/calls.rs:63-443] |
| `lua_require_qualifier_before_name` | function | Returns the trimmed text immediately preceding 'name_byte' on the same line only if it ends with '.' or ':' and the remaining qualifier starts with '"require"', otherwise 'None'. [crates/gcode/src/index/parser/calls.rs:445-464] |

