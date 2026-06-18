---
title: crates/gcode/src/index/parser/calls/ast.rs
type: code_file
provenance:
- file: crates/gcode/src/index/parser/calls/ast.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/parser/calls/ast.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/parser/calls/ast.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/index/parser/calls/ast.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `extract_ast_calls` | function | Runs the language-specific Tree-sitter call query over the parsed AST, extracts 'name'/'call' captures into 'CallRelation' values, and filters out ignored or non-call constructs such as definition heads before returning the collected call relations. [crates/gcode/src/index/parser/calls/ast.rs:17-103] |
| `is_elixir_definition_head_call` | function | Returns 'true' only when the node is an Elixir 'call' that appears as the head of a 'def', 'defp', or 'defmacro' definition by walking up through 'arguments'/'binary_operator' parents and checking the enclosing call’s target keyword. [crates/gcode/src/index/parser/calls/ast.rs:105-135] |
| `extract_js_calls` | function | Parses the given JavaScript source with tree-sitter, constructs a JavaScript language spec and call-extraction context, and returns the extracted 'CallRelation' values by delegating to 'extract_ast_calls'. [crates/gcode/src/index/parser/calls/ast.rs:148-179] |
| `js_bindings` | function | Parses a JavaScript import statement from 'import_text' using a default 'ImportResolutionContext', stores the extracted imports via 'parse_import_statement', and returns the resulting 'ImportBindings'. [crates/gcode/src/index/parser/calls/ast.rs:181-193] |
| `skips_matches_without_name_capture` | function | Verifies that 'extract_js_calls' returns no results for a JavaScript call expression when the query matches the callee but does not provide the expected name capture. [crates/gcode/src/index/parser/calls/ast.rs:196-205] |
| `ignores_qualified_keyword_callee_after_split` | function | Verifies that 'extract_js_calls' returns no matches for the Dart snippet 'obj.await();' when the callee is a qualified keyword-like member expression, i.e. such calls are ignored after splitting. [crates/gcode/src/index/parser/calls/ast.rs:208-217] |
| `member_call_uses_qualifier_path_from_call_node` | function | Verifies that a JavaScript member call like 'fs.readFile()' is extracted with the property name as 'callee_name', the correct source line, and the imported qualifier 'fs' recorded as an external module target. [crates/gcode/src/index/parser/calls/ast.rs:220-235] |
| `bare_detected_syntax_upgrades_to_member_when_qualified_name_is_captured` | function | Verifies that when a JavaScript import binding captures the qualified name, a bare 'fs.readFile()' call is recognized as a single external member call with callee name 'readFile', target kind 'External', and external module 'fs'. [crates/gcode/src/index/parser/calls/ast.rs:238-252] |

