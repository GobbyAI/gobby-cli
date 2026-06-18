---
title: crates/gcode/src/graph/typed_query.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/typed_query.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/typed_query.rs

Module: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Overview

`crates/gcode/src/graph/typed_query.rs` exposes 25 indexed API symbols.

## How it fits

`crates/gcode/src/graph/typed_query.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TypedQuery` | class | Indexed class `TypedQuery` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:7-10] |
| `TypedValue` | type | Indexed type `TypedValue` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:13-21] |
| `IdentifierKind` | type | Indexed type `IdentifierKind` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:24-27] |
| `TypedQueryError` | type | Indexed type `TypedQueryError` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:30-38] |
| `TypedQuery::new` | method | Indexed method `TypedQuery::new` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:41-46] |
| `TypedQuery::with_params` | method | Indexed method `TypedQuery::with_params` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:48-58] |
| `TypedQuery::insert_param` | method | Indexed method `TypedQuery::insert_param` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:60-70] |
| `cypher_string_literal` | function | Indexed function `cypher_string_literal` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:73-75] |
| `render_cypher_value` | function | Indexed function `render_cypher_value` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:77-98] |
| `string_params` | function | Indexed function `string_params` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:100-105] |
| `clamp_limit` | function | Indexed function `clamp_limit` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:107-109] |
| `clamp_offset` | function | Indexed function `clamp_offset` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:111-113] |
| `id_list_literal` | function | Indexed function `id_list_literal` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:115-120] |
| `validate_identifier` | function | Indexed function `validate_identifier` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:122-141] |
| `render_string_literal` | function | Indexed function `render_string_literal` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:143-145] |
| `escape_string_contents` | function | Indexed function `escape_string_contents` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:147-164] |
| `render_float` | function | Indexed function `render_float` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:166-178] |
| `IdentifierKind::fmt` | method | Indexed method `IdentifierKind::fmt` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:181-186] |
| `TypedQueryError::fmt` | method | Indexed method `TypedQueryError::fmt` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:190-200] |
| `typed_params_render_nested_safe_cypher_literals` | function | Indexed function `typed_params_render_nested_safe_cypher_literals` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:211-276] |
| `string_literals_escape_both_quote_delimiters` | function | Indexed function `string_literals_escape_both_quote_delimiters` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:279-284] |
| `string_literals_escape_control_characters` | function | Indexed function `string_literals_escape_control_characters` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:287-297] |
| `nested_string_values_escape_control_characters` | function | Indexed function `nested_string_values_escape_control_characters` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:300-315] |
| `invalid_identifiers_return_typed_errors` | function | Indexed function `invalid_identifiers_return_typed_errors` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:318-341] |
| `unsafe_values_return_typed_errors` | function | Indexed function `unsafe_values_return_typed_errors` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:344-350] |

