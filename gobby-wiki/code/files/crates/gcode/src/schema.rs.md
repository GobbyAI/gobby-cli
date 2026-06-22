---
title: crates/gcode/src/schema.rs
type: code_file
provenance:
- file: crates/gcode/src/schema.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/schema.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/schema.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gcode/src/schema.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `validate_runtime_schema` | function | Validates that the connected PostgreSQL runtime has the 'pg_search' extension, the BM25 score procedure, and all required tables and BM25 indexes, returning an error with a migration hint if any prerequisite is missing. [crates/gcode/src/schema.rs:24-52] |
| `extension_exists` | function | Queries PostgreSQL’s 'pg_extension' catalog to return whether an extension named 'extension' exists, propagating context-rich errors if the lookup or boolean decode fails. [crates/gcode/src/schema.rs:54-63] |
| `procedure_exists` | function | Returns 'true' if PostgreSQL resolves the given procedure name to a valid regprocedure and 'false' otherwise, propagating query or decode errors with context. [crates/gcode/src/schema.rs:65-71] |
| `missing_relations` | function | Checks each relation name against 'DEFAULT_SCHEMA' in PostgreSQL using 'to_regclass', returning a 'Vec<String>' of the input relations that do not exist, or an error if any query or decode step fails. [crates/gcode/src/schema.rs:73-88] |
| `validates_runtime_schema_when_postgres_test_dsn_is_set` | function | Connects to the PostgreSQL test database specified by 'GCODE_POSTGRES_TEST_DATABASE_URL' and asserts that 'validate_runtime_schema' succeeds on the resulting read-write client. [crates/gcode/src/schema.rs:116-123] |

_Verified by 4 in-file unit tests._

