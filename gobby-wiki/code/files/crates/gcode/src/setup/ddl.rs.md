---
title: crates/gcode/src/setup/ddl.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/ddl.rs
  ranges:
  - 8-10
  - 13-16
  - 19-23
  - 25-27
  - 29-34
  - 36-38
  - 40-278
  - 282-284
  - 286-292
  - 294-308
  - 311-319
  - 321-338
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/ddl.rs:8-10](crates/gcode/src/setup/ddl.rs#L8-L10), [crates/gcode/src/setup/ddl.rs:13-16](crates/gcode/src/setup/ddl.rs#L13-L16), [crates/gcode/src/setup/ddl.rs:19-23](crates/gcode/src/setup/ddl.rs#L19-L23), [crates/gcode/src/setup/ddl.rs:25-27](crates/gcode/src/setup/ddl.rs#L25-L27), [crates/gcode/src/setup/ddl.rs:29-34](crates/gcode/src/setup/ddl.rs#L29-L34), [crates/gcode/src/setup/ddl.rs:36-38](crates/gcode/src/setup/ddl.rs#L36-L38), [crates/gcode/src/setup/ddl.rs:40-278](crates/gcode/src/setup/ddl.rs#L40-L278), [crates/gcode/src/setup/ddl.rs:282-284](crates/gcode/src/setup/ddl.rs#L282-L284), [crates/gcode/src/setup/ddl.rs:286-292](crates/gcode/src/setup/ddl.rs#L286-L292), [crates/gcode/src/setup/ddl.rs:294-308](crates/gcode/src/setup/ddl.rs#L294-L308), [crates/gcode/src/setup/ddl.rs:311-319](crates/gcode/src/setup/ddl.rs#L311-L319), [crates/gcode/src/setup/ddl.rs:321-338](crates/gcode/src/setup/ddl.rs#L321-L338)

</details>

# crates/gcode/src/setup/ddl.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

Defines the standalone DDL setup for Gcode, centered on `GcodeStandaloneSetup`, which stores a target schema and exposes helpers to build and run the database objects needed for indexing and query support. `postgres_object_definitions` assembles the ordered list of PostgreSQL DDL statements, using `qualified` and `object_definition` to name and scope tables, views, functions, and extensions under the configured schema. `namespace`, `owned_objects`, and `create` connect that definition list to the setup framework, while `owned_object` and `execute_postgres_ddl` wrap individual DDL items and execute them against the database.
[crates/gcode/src/setup/ddl.rs:8-10]
[crates/gcode/src/setup/ddl.rs:13-16]
[crates/gcode/src/setup/ddl.rs:19-23]
[crates/gcode/src/setup/ddl.rs:25-27]
[crates/gcode/src/setup/ddl.rs:29-34]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GcodeStandaloneSetup` | class | `pub struct GcodeStandaloneSetup {` | `GcodeStandaloneSetup [class]` | `9d89a3c7-ff2f-5843-9957-308da7bc90dc` | 8-10 [crates/gcode/src/setup/ddl.rs:8-10] | Indexed class `GcodeStandaloneSetup` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:8-10] |
| `PostgresObjectDefinition` | class | `pub(crate) struct PostgresObjectDefinition {` | `PostgresObjectDefinition [class]` | `7bf17f1b-e251-5ae1-9785-fb35b7232180` | 13-16 [crates/gcode/src/setup/ddl.rs:13-16] | Indexed class `PostgresObjectDefinition` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:13-16] |
| `GcodeStandaloneSetup::new` | method | `pub fn new(schema: impl Into<String>) -> Self {` | `GcodeStandaloneSetup::new [method]` | `a4642703-80eb-5e5b-aef5-33f2df381ef0` | 19-23 [crates/gcode/src/setup/ddl.rs:19-23] | Indexed method `GcodeStandaloneSetup::new` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:19-23] |
| `GcodeStandaloneSetup::schema` | method | `pub fn schema(&self) -> &str {` | `GcodeStandaloneSetup::schema [method]` | `a1fa7ca1-014e-537e-afa0-cd78a8cbb7d8` | 25-27 [crates/gcode/src/setup/ddl.rs:25-27] | Indexed method `GcodeStandaloneSetup::schema` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:25-27] |
| `GcodeStandaloneSetup::object_definition` | method | `fn object_definition(&self, name: &str, sql: String) -> PostgresObjectDefinition {` | `GcodeStandaloneSetup::object_definition [method]` | `1ca00410-c8f8-5461-8e55-9ac9cf188575` | 29-34 [crates/gcode/src/setup/ddl.rs:29-34] | Indexed method `GcodeStandaloneSetup::object_definition` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:29-34] |
| `GcodeStandaloneSetup::qualified` | method | `fn qualified(&self, relation: &str) -> Result<String, SetupError> {` | `GcodeStandaloneSetup::qualified [method]` | `e818b83f-2486-5a5b-b41c-a79fe05cc710` | 36-38 [crates/gcode/src/setup/ddl.rs:36-38] | Indexed method `GcodeStandaloneSetup::qualified` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:36-38] |
| `GcodeStandaloneSetup::postgres_object_definitions` | method | `pub(crate) fn postgres_object_definitions(` | `GcodeStandaloneSetup::postgres_object_definitions [method]` | `abcd285d-32d4-5b4a-90d7-7bd3b4d8f080` | 40-278 [crates/gcode/src/setup/ddl.rs:40-278] | Indexed method `GcodeStandaloneSetup::postgres_object_definitions` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:40-278] |
| `GcodeStandaloneSetup::namespace` | method | `fn namespace(&self) -> &str {` | `GcodeStandaloneSetup::namespace [method]` | `3d7170f2-8a8f-5942-8751-b187964b3a33` | 282-284 [crates/gcode/src/setup/ddl.rs:282-284] | Indexed method `GcodeStandaloneSetup::namespace` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:282-284] |
| `GcodeStandaloneSetup::owned_objects` | method | `fn owned_objects(&self) -> Result<Vec<OwnedObject>, SetupError> {` | `GcodeStandaloneSetup::owned_objects [method]` | `ed46b380-73b5-5734-a9de-d3146f45110c` | 286-292 [crates/gcode/src/setup/ddl.rs:286-292] | Indexed method `GcodeStandaloneSetup::owned_objects` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:286-292] |
| `GcodeStandaloneSetup::create` | method | `fn create(&self, ctx: &mut SetupContext<'_>) -> Result<SetupReport, SetupError> {` | `GcodeStandaloneSetup::create [method]` | `b5b176ea-cc9d-569b-adad-7ab7ebefefe2` | 294-308 [crates/gcode/src/setup/ddl.rs:294-308] | Indexed method `GcodeStandaloneSetup::create` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:294-308] |
| `owned_object` | function | `fn owned_object(definition: PostgresObjectDefinition) -> OwnedObject {` | `owned_object [function]` | `04f9b064-f6ae-5ba7-983e-1f3fa73ed2e6` | 311-319 [crates/gcode/src/setup/ddl.rs:311-319] | Indexed function `owned_object` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:311-319] |
| `execute_postgres_ddl` | function | `fn execute_postgres_ddl(` | `execute_postgres_ddl [function]` | `f1d0f16c-4daf-543b-abaf-fcdf4db86dff` | 321-338 [crates/gcode/src/setup/ddl.rs:321-338] | Indexed function `execute_postgres_ddl` in `crates/gcode/src/setup/ddl.rs`. [crates/gcode/src/setup/ddl.rs:321-338] |
