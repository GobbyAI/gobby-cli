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

`crates/gcode/src/graph/typed_query.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TypedQuery` | class | 'TypedQuery' is a Rust struct that encapsulates a Cypher query string together with a 'HashMap<String, String>' of named string parameters for the query. [crates/gcode/src/graph/typed_query.rs:7-10] |
| `TypedValue` | type | Indexed type `TypedValue` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:13-21] |
| `IdentifierKind` | type | Indexed type `IdentifierKind` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:24-27] |
| `TypedQueryError` | type | Indexed type `TypedQueryError` in `crates/gcode/src/graph/typed_query.rs`. [crates/gcode/src/graph/typed_query.rs:30-38] |
| `TypedQuery::new` | method | Creates a new instance by converting the provided 'cypher' into a 'String' and initializing 'params' as an empty 'HashMap'. [crates/gcode/src/graph/typed_query.rs:41-46] |
| `TypedQuery::with_params` | method | Constructs a new query from the given Cypher string and inserts each '(name, TypedValue)' pair from the provided iterator via 'insert_param', returning the assembled 'Self' or a 'TypedQueryError' if any parameter insertion fails. [crates/gcode/src/graph/typed_query.rs:48-58] |
| `TypedQuery::insert_param` | method | Validates the provided parameter name as a parameter identifier, renders the 'TypedValue' into a Cypher value string, inserts the resulting name/value pair into 'self.params', and returns 'Ok(())' or a 'TypedQueryError' if validation or rendering fails. [crates/gcode/src/graph/typed_query.rs:60-70] |
| `cypher_string_literal` | function | Returns a Cypher string literal by wrapping the escaped contents of 's' in single quotes. [crates/gcode/src/graph/typed_query.rs:73-75] |
| `render_cypher_value` | function | 'render_cypher_value' converts a 'TypedValue' into a Cypher literal string by recursively rendering scalars, lists, and maps, validating map keys as identifiers, and propagating any formatting or validation errors as 'TypedQueryError'. [crates/gcode/src/graph/typed_query.rs:77-98] |
| `string_params` | function | Converts a slice of '(&str, &str)' pairs into a 'HashMap<String, String>' by cloning each key to 'String' and mapping each value through 'cypher_string_literal' before collecting. [crates/gcode/src/graph/typed_query.rs:100-105] |
| `clamp_limit` | function | Returns 'limit' clamped to the inclusive range '[1, max]', ensuring the result is at least '1' and at most 'max'. [crates/gcode/src/graph/typed_query.rs:107-109] |
| `clamp_offset` | function | Returns the smaller of 'offset' and 'max', clamping 'offset' so the result never exceeds 'max'. [crates/gcode/src/graph/typed_query.rs:111-113] |
| `id_list_literal` | function | Returns a comma-separated string of Cypher-escaped string literals for each 'String' in 'ids'. [crates/gcode/src/graph/typed_query.rs:115-120] |
| `validate_identifier` | function | Returns 'Ok(())' only if 'identifier' is non-empty, starts with an ASCII letter or '_', and every subsequent character is an ASCII alphanumeric or '_'; otherwise it returns 'TypedQueryError::InvalidIdentifier' containing the given 'kind' and the original identifier string. [crates/gcode/src/graph/typed_query.rs:122-141] |
| `render_string_literal` | function | Returns the Cypher-escaped string literal for the input 'value' wrapped in 'Ok', without performing any additional validation or transformation. [crates/gcode/src/graph/typed_query.rs:143-145] |
| `escape_string_contents` | function | Returns a new string with backslash, quote, newline, carriage return, tab, backspace, form-feed, and other control characters escaped using Rust-style sequences, leaving all other characters unchanged. [crates/gcode/src/graph/typed_query.rs:147-164] |
| `render_float` | function | Returns a 'String' representation of a finite 'f64', appending '.0' to whole-number forms that lack a decimal point or exponent, and returns 'TypedQueryError::NonFiniteFloat' for 'NaN' or infinite values. [crates/gcode/src/graph/typed_query.rs:166-178] |
| `IdentifierKind::fmt` | method | Implements 'Display'/formatting by matching on 'self' and writing the fixed string '"parameter name"' for 'ParameterName' or '"map key"' for 'MapKey' to the formatter. [crates/gcode/src/graph/typed_query.rs:181-186] |
| `TypedQueryError::fmt` | method | Formats the enum as a human-readable validation error, emitting either 'invalid {kind} '{identifier}'; expected ^[A-Za-z_][A-Za-z0-9_]*$' for 'InvalidIdentifier' or 'non-finite float '{value}' is not allowed' for 'NonFiniteFloat'. [crates/gcode/src/graph/typed_query.rs:190-200] |

_Verified by 6 in-file unit tests._

