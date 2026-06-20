---
title: crates/gcode/src/setup/ddl.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/ddl.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/ddl.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Overview

`crates/gcode/src/setup/ddl.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gcode/src/setup/ddl.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GcodeStandaloneSetup` | class | 'GcodeStandaloneSetup' is a Rust struct that stores a single 'String' field, 'schema', presumably holding the G-code schema configuration for standalone setup. [crates/gcode/src/setup/ddl.rs:8-10] |
| `PostgresObjectDefinition` | class | 'PostgresObjectDefinition' is a crate-visible struct that stores the 'name' and raw SQL text for a PostgreSQL object definition. [crates/gcode/src/setup/ddl.rs:13-16] |
| `GcodeStandaloneSetup::new` | method | Constructs a new instance by converting the provided 'schema' into a 'String' and storing it in the struct’s 'schema' field. [crates/gcode/src/setup/ddl.rs:19-23] |
| `GcodeStandaloneSetup::schema` | method | Returns an immutable '&str' reference to the struct’s 'schema' field. [crates/gcode/src/setup/ddl.rs:25-27] |
| `GcodeStandaloneSetup::object_definition` | method | Constructs and returns a 'PostgresObjectDefinition' by cloning 'name' into an owned 'String' and storing it together with the provided 'sql' string. [crates/gcode/src/setup/ddl.rs:29-34] |
| `GcodeStandaloneSetup::qualified` | method | Returns a qualified relation string by delegating to 'qualified_relation' with 'self.schema', the provided 'relation', and the context label '"relation"', propagating any 'SetupError'. [crates/gcode/src/setup/ddl.rs:36-38] |
| `GcodeStandaloneSetup::postgres_object_definitions` | method | Builds and returns a 'Result<Vec<PostgresObjectDefinition>, SetupError>' containing PostgreSQL setup DDL for the 'pg_search' extension and several schema objects, using qualified table names for the code indexing tables. [crates/gcode/src/setup/ddl.rs:40-278] |
| `GcodeStandaloneSetup::namespace` | method | Returns the 'NAMESPACE' constant as an immutable string slice reference ('&str'). [crates/gcode/src/setup/ddl.rs:282-284] |
| `GcodeStandaloneSetup::owned_objects` | method | Returns a 'Result' containing a 'Vec<OwnedObject>' built by fetching PostgreSQL object definitions, mapping each definition through 'owned_object', and collecting the results, propagating any 'SetupError'. [crates/gcode/src/setup/ddl.rs:286-292] |
| `GcodeStandaloneSetup::create` | method | Creates a 'SetupReport' by iterating through owned objects in order, invoking each object’s 'creator' with the provided 'SetupContext', recording successful names in 'created', and on the first error recording that failure, marking all remaining objects as 'skipped', and returning the accumulated report without propagating the error. [crates/gcode/src/setup/ddl.rs:294-308] |
| `owned_object` | function | Constructs an 'OwnedObject' from a 'PostgresObjectDefinition' by cloning its name, marking the store as 'StoreKind::Postgres', and packaging a closure that runs 'execute_postgres_ddl' with the captured name and SQL. [crates/gcode/src/setup/ddl.rs:311-319] |
| `execute_postgres_ddl` | function | Executes the provided PostgreSQL DDL SQL against the setup context’s connection, returning 'ConnectionFailed' if no PostgreSQL connection is present and mapping any 'batch_execute' error to 'SetupError::CreationFailed' for the named object. [crates/gcode/src/setup/ddl.rs:321-338] |

