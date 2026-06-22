---
title: crates/gwiki/src/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/setup.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/setup.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/setup.rs` exposes 25 indexed API symbols.

## How it fits

`crates/gwiki/src/setup.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GwikiTable` | type | Indexed type `GwikiTable` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:29-35] |
| `GwikiTable::name` | method | Returns the static table name string corresponding to the enum variant ('Documents', 'Chunks', 'Links', 'Sources', or 'Ingestions'). [crates/gwiki/src/setup.rs:38-46] |
| `GwikiPostgresObjectKind` | type | Indexed type `GwikiPostgresObjectKind` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:50-54] |
| `GwikiPostgresObject` | class | 'GwikiPostgresObject' is a PostgreSQL object descriptor holding a static object name, an object kind enum, and the SQL definition string for that object. [crates/gwiki/src/setup.rs:57-61] |
| `GwikiStandaloneSetup` | class | 'GwikiStandaloneSetup' is a Rust struct that encapsulates a single private 'schema: String' field, representing setup state for a standalone Gwiki configuration. [crates/gwiki/src/setup.rs:64-66] |
| `GwikiStandaloneSetup::new` | method | Creates and returns a new 'Self' instance with its 'schema' field initialized to 'DEFAULT_SCHEMA.to_string()'. [crates/gwiki/src/setup.rs:69-73] |
| `GwikiStandaloneSetup::schema` | method | Returns an immutable string slice view of the instance’s 'schema' field. [crates/gwiki/src/setup.rs:76-78] |
| `GwikiStandaloneSetup::postgres_objects` | method | Builds and returns a 'Vec<GwikiPostgresObject>' containing a preflight check that requires the 'pg_search' extension, followed by table definitions for all 'GWIKI_POSTGRES_TABLES' and index definitions for all 'GWIKI_POSTGRES_INDEXES', propagating any 'SetupError' from SQL generation. [crates/gwiki/src/setup.rs:80-101] |
| `GwikiStandaloneSetup::table_sql` | method | Builds and returns a PostgreSQL 'CREATE TABLE IF NOT EXISTS' DDL string for the specified 'GwikiTable' variant, using a qualified relation name and variant-specific column definitions, or propagates 'SetupError' if the name cannot be qualified. [crates/gwiki/src/setup.rs:103-192] |
| `GwikiStandaloneSetup::index_sql` | method | Builds and returns the 'CREATE INDEX' SQL for a fixed set of named 'gwiki' PostgreSQL indexes by quoting the index identifier, qualifying the 'documents'/'chunks'/'links'/'sources' table names, and otherwise returning 'SetupError::CreationFailed' for an unknown index name. [crates/gwiki/src/setup.rs:194-228] |
| `GwikiStandaloneSetup::qualified_relation_name` | method | Returns a schema-qualified relation name by quoting the schema and relation identifiers with the appropriate labels and concatenating them as 'schema.relation', propagating any 'SetupError' from identifier quoting. [crates/gwiki/src/setup.rs:230-236] |
| `GwikiStandaloneSetup::namespace` | method | Returns the 'NAMESPACE' constant as an immutable '&str' reference. [crates/gwiki/src/setup.rs:240-242] |
| `GwikiStandaloneSetup::owned_objects` | method | Returns the current setup’s PostgreSQL objects as a 'Vec<OwnedObject>' by calling 'postgres_objects()', mapping each item through 'owned_object', collecting the results, and propagating any 'SetupError'. [crates/gwiki/src/setup.rs:244-250] |
| `GwikiStandaloneSetup::create` | method | Creates each owned object in order via its creator callback, recording successful names in 'report.created', logging the first failure in 'report.failed', stopping on error, and returning the accumulated 'SetupReport' while relying on 'IF NOT EXISTS' for idempotency. [crates/gwiki/src/setup.rs:252-266] |
| `default_setup` | function | Constructs and returns a new 'GwikiStandaloneSetup' by calling 'GwikiStandaloneSetup::new()'. [crates/gwiki/src/setup.rs:269-271] |
| `table` | function | Constructs and returns a 'GwikiPostgresObject' representing a table, using the provided static name and SQL string and setting 'kind' to 'GwikiPostgresObjectKind::Table'. [crates/gwiki/src/setup.rs:273-279] |
| `index` | function | Constructs and returns a 'GwikiPostgresObject' representing a PostgreSQL index, using the provided static 'name' and 'sql' string and setting 'kind' to 'GwikiPostgresObjectKind::Index'. [crates/gwiki/src/setup.rs:281-287] |
| `preflight` | function | Constructs and returns a 'GwikiPostgresObject' tagged as 'Preflight' with the provided static 'name' and 'sql' string. [crates/gwiki/src/setup.rs:289-295] |
| `owned_object` | function | Constructs an 'OwnedObject' for a PostgreSQL-backed object by cloning its name, tagging the store as 'Postgres', and installing a closure that executes the object's DDL via 'execute_postgres_ddl' with the captured name and SQL. [crates/gwiki/src/setup.rs:297-305] |
| `execute_postgres_ddl` | function | Executes a PostgreSQL DDL batch against the setup context’s optional 'pg' connection, returning 'ConnectionFailed' if no connection is present and mapping any execution error into 'SetupError::CreationFailed' using the database error message when available. [crates/gwiki/src/setup.rs:307-329] |
| `quote_identifier` | function | Trims the input identifier, rejects empty or NUL-containing values and values exceeding 'POSTGRES_IDENTIFIER_MAX_BYTES', escapes embedded double quotes by doubling them, and returns the result wrapped in PostgreSQL double quotes. [crates/gwiki/src/setup.rs:331-355] |

_Verified by 4 in-file unit tests._

