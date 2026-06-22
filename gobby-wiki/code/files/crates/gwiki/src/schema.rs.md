---
title: crates/gwiki/src/schema.rs
type: code_file
provenance:
- file: crates/gwiki/src/schema.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/schema.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/schema.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/schema.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GwikiRuntimeSchema` | class | 'GwikiRuntimeSchema' is a zero-sized Rust unit struct that serves as a marker type for the runtime schema. [crates/gwiki/src/schema.rs:13] |
| `GwikiRuntimeSchema::required_objects` | method | It constructs a 'Vec<RequiredObject>' by collecting 'RequiredObject's for every PostgreSQL table name in 'GWIKI_POSTGRES_TABLES' and every entry in 'GWIKI_POSTGRES_INDEXES', applying 'required_relation' to each relation name. [crates/gwiki/src/schema.rs:16-23] |
| `validate_runtime_schema` | function | Delegates runtime-schema validation to 'GwikiRuntimeSchema.validate(ctx)' and returns the resulting 'ValidationReport'. [crates/gwiki/src/schema.rs:26-28] |
| `required_relation` | function | Constructs a 'RequiredObject' for a given relation name by storing the name as a 'String', fixing the backend to 'StoreKind::Postgres', and attaching a validator closure that calls 'validate_relation(ctx, relation)'. [crates/gwiki/src/schema.rs:30-36] |
| `validate_relation` | function | Checks that a PostgreSQL connection is present, resolves the given relation name to a regclass-qualified identifier, verifies via 'to_regclass($1) IS NOT NULL' that the relation exists, and returns a 'SetupIssue' if the connection is missing, the query fails, or the relation is absent. [crates/gwiki/src/schema.rs:38-57] |
| `relation_regclass_name` | function | Returns a fully qualified relation name by prefixing the input 'relation' with 'DEFAULT_SCHEMA' and a dot using string formatting. [crates/gwiki/src/schema.rs:59-61] |
| `missing_relation_issue` | function | Constructs a 'SetupIssue' for a missing PostgreSQL datastore relation, setting the object name and guidance message to report the unavailable 'gwiki' object, recommend running Gobby hub migrations and 'gwiki setup', and include 'gwiki setup' as a command hint. [crates/gwiki/src/schema.rs:63-75] |

_Verified by 2 in-file unit tests._

