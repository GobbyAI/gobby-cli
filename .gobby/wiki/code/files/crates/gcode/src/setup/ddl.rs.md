---
title: crates/gcode/src/setup/ddl.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/ddl.rs
  ranges:
  - 8-10
  - 13-16
  - 18-279
  - 19-23
  - 25-27
  - 29-34
  - 36-38
  - 40-278
  - 281-309
  - 282-284
  - 286-292
  - 294-308
  - 311-319
  - 321-338
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/ddl.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

`crates/gcode/src/setup/ddl.rs` exposes 14 indexed API symbols.
[crates/gcode/src/setup/ddl.rs:8-10]
[crates/gcode/src/setup/ddl.rs:13-16]
[crates/gcode/src/setup/ddl.rs:18-279]
[crates/gcode/src/setup/ddl.rs:19-23]
[crates/gcode/src/setup/ddl.rs:25-27]
[crates/gcode/src/setup/ddl.rs:29-34]
[crates/gcode/src/setup/ddl.rs:36-38]
[crates/gcode/src/setup/ddl.rs:40-278]
[crates/gcode/src/setup/ddl.rs:281-309]
[crates/gcode/src/setup/ddl.rs:282-284]
[crates/gcode/src/setup/ddl.rs:286-292]
[crates/gcode/src/setup/ddl.rs:294-308]
[crates/gcode/src/setup/ddl.rs:311-319]
[crates/gcode/src/setup/ddl.rs:321-338]

## API Symbols

- `GcodeStandaloneSetup` (class) component `GcodeStandaloneSetup [class]` (`9d89a3c7-ff2f-5843-9957-308da7bc90dc`) lines 8-10 [crates/gcode/src/setup/ddl.rs:8-10]
  - Signature: `pub struct GcodeStandaloneSetup {`
  - Purpose: GcodeStandaloneSetup is a struct containing a single String field representing a schema configuration for independent gcode operations. [crates/gcode/src/setup/ddl.rs:8-10]
- `PostgresObjectDefinition` (class) component `PostgresObjectDefinition [class]` (`7bf17f1b-e251-5ae1-9785-fb35b7232180`) lines 13-16 [crates/gcode/src/setup/ddl.rs:13-16]
  - Signature: `pub(crate) struct PostgresObjectDefinition {`
  - Purpose: `PostgresObjectDefinition` is a crate-internal struct that encapsulates a PostgreSQL database object's name and its corresponding SQL definition statement. [crates/gcode/src/setup/ddl.rs:13-16]
- `GcodeStandaloneSetup` (class) component `GcodeStandaloneSetup [class]` (`b0770f1a-cb75-5231-9bfd-90d9c2f6cef3`) lines 18-279 [crates/gcode/src/setup/ddl.rs:18-279]
  - Signature: `impl GcodeStandaloneSetup {`
  - Purpose: **GcodeStandaloneSetup generates schema-qualified PostgreSQL object definitions for creating a code indexing database infrastructure.** [crates/gcode/src/setup/ddl.rs:18-279]
- `GcodeStandaloneSetup.new` (method) component `GcodeStandaloneSetup.new [method]` (`a4642703-80eb-5e5b-aef5-33f2df381ef0`) lines 19-23 [crates/gcode/src/setup/ddl.rs:19-23]
  - Signature: `pub fn new(schema: impl Into<String>) -> Self {`
  - Purpose: Constructs a new instance with the `schema` field initialized from the provided parameter via the `Into<String>` trait. [crates/gcode/src/setup/ddl.rs:19-23]
- `GcodeStandaloneSetup.schema` (method) component `GcodeStandaloneSetup.schema [method]` (`a1fa7ca1-014e-537e-afa0-cd78a8cbb7d8`) lines 25-27 [crates/gcode/src/setup/ddl.rs:25-27]
  - Signature: `pub fn schema(&self) -> &str {`
  - Purpose: A public getter method that returns an immutable reference to the schema field as a string slice. [crates/gcode/src/setup/ddl.rs:25-27]
- `GcodeStandaloneSetup.object_definition` (method) component `GcodeStandaloneSetup.object_definition [method]` (`1ca00410-c8f8-5461-8e55-9ac9cf188575`) lines 29-34 [crates/gcode/src/setup/ddl.rs:29-34]
  - Signature: `fn object_definition(&self, name: &str, sql: String) -> PostgresObjectDefinition {`
  - Purpose: Constructs a `PostgresObjectDefinition` by wrapping the provided object name and SQL definition string. [crates/gcode/src/setup/ddl.rs:29-34]
- `GcodeStandaloneSetup.qualified` (method) component `GcodeStandaloneSetup.qualified [method]` (`e818b83f-2486-5a5b-b41c-a79fe05cc710`) lines 36-38 [crates/gcode/src/setup/ddl.rs:36-38]
  - Signature: `fn qualified(&self, relation: &str) -> Result<String, SetupError> {`
  - Purpose: Returns a schema-qualified relation name by delegating to the `qualified_relation` function with the instance's schema. [crates/gcode/src/setup/ddl.rs:36-38]
- `GcodeStandaloneSetup.postgres_object_definitions` (method) component `GcodeStandaloneSetup.postgres_object_definitions [method]` (`abcd285d-32d4-5b4a-90d7-7bd3b4d8f080`) lines 40-278 [crates/gcode/src/setup/ddl.rs:40-278]
  - Signature: `pub(crate) fn postgres_object_definitions(`
  - Purpose: Returns PostgreSQL object definitions containing DDL statements for creating the pg_search extension and six code-indexing tables (projects, files, symbols, chunks, imports, calls). [crates/gcode/src/setup/ddl.rs:40-278]
- `GcodeStandaloneSetup` (class) component `GcodeStandaloneSetup [class]` (`185f2dd0-8dae-5a46-9624-f2a19d9c5bf2`) lines 281-309 [crates/gcode/src/setup/ddl.rs:281-309]
  - Signature: `impl StandaloneSetup for GcodeStandaloneSetup {`
  - Purpose: GcodeStandaloneSetup implements the StandaloneSetup trait to sequentially execute creator functions for PostgreSQL objects and generate a report tracking successful creations, failures, and cascading skips. [crates/gcode/src/setup/ddl.rs:281-309]
- `GcodeStandaloneSetup.namespace` (method) component `GcodeStandaloneSetup.namespace [method]` (`3d7170f2-8a8f-5942-8751-b187964b3a33`) lines 282-284 [crates/gcode/src/setup/ddl.rs:282-284]
  - Signature: `fn namespace(&self) -> &str {`
  - Purpose: Returns an immutable string slice reference to the constant `NAMESPACE` value. [crates/gcode/src/setup/ddl.rs:282-284]
- `GcodeStandaloneSetup.owned_objects` (method) component `GcodeStandaloneSetup.owned_objects [method]` (`ed46b380-73b5-5734-a9de-d3146f45110c`) lines 286-292 [crates/gcode/src/setup/ddl.rs:286-292]
  - Signature: `fn owned_objects(&self) -> Result<Vec<OwnedObject>, SetupError> {`
  - Purpose: This method transforms PostgreSQL object definitions into a vector of `OwnedObject` instances via the `owned_object` mapping function, propagating any `SetupError`. [crates/gcode/src/setup/ddl.rs:286-292]
- `GcodeStandaloneSetup.create` (method) component `GcodeStandaloneSetup.create [method]` (`b5b176ea-cc9d-569b-adad-7ab7ebefefe2`) lines 294-308 [crates/gcode/src/setup/ddl.rs:294-308]
  - Signature: `fn create(&self, ctx: &mut SetupContext<'_>) -> Result<SetupReport, SetupError> {`
  - Purpose: Sequentially executes the creator function for each owned object, aggregating successful creations and error details in a `SetupReport` while short-circuiting on the first failure to mark remaining objects as skipped. [crates/gcode/src/setup/ddl.rs:294-308]
- `owned_object` (function) component `owned_object [function]` (`04f9b064-f6ae-5ba7-983e-1f3fa73ed2e6`) lines 311-319 [crates/gcode/src/setup/ddl.rs:311-319]
  - Signature: `fn owned_object(definition: PostgresObjectDefinition) -> OwnedObject {`
  - Purpose: Converts a PostgresObjectDefinition into an OwnedObject by wrapping its name and SQL DDL statement in a closure-based creator that executes the PostgreSQL DDL when invoked. [crates/gcode/src/setup/ddl.rs:311-319]
- `execute_postgres_ddl` (function) component `execute_postgres_ddl [function]` (`f1d0f16c-4daf-543b-abaf-fcdf4db86dff`) lines 321-338 [crates/gcode/src/setup/ddl.rs:321-338]
  - Signature: `fn execute_postgres_ddl(`
  - Purpose: Executes DDL SQL statements on a PostgreSQL connection extracted from the setup context, returning a `SetupError` if the connection is absent or batch execution fails. [crates/gcode/src/setup/ddl.rs:321-338]

