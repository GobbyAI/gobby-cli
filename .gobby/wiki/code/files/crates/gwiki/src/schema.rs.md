---
title: crates/gwiki/src/schema.rs
type: code_file
provenance:
- file: crates/gwiki/src/schema.rs
  ranges:
  - '13'
  - 15-24
  - 26-28
  - 30-36
  - 38-57
  - 59-61
  - 63-75
  - 83-118
  - 121-126
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/schema.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the runtime schema validator for `gwiki`, centered on a zero-sized `GwikiRuntimeSchema` marker that enumerates every required PostgreSQL table and index as attached validation targets. Each required relation is wrapped as a `RequiredObject` whose validator checks for a live PostgreSQL connection, verifies the relation exists via `to_regclass` in the `public` schema, and turns failures into a guided `SetupIssue` that points users to run migrations and `gwiki setup`. The public helper `validate_runtime_schema` runs that validation, and the tests confirm both the expected missing-object behavior and the schema-qualified relation naming.
[crates/gwiki/src/schema.rs:13]
[crates/gwiki/src/schema.rs:15-24]
[crates/gwiki/src/schema.rs:16-23]
[crates/gwiki/src/schema.rs:26-28]
[crates/gwiki/src/schema.rs:30-36]

## API Symbols

- `GwikiRuntimeSchema` (class) component `GwikiRuntimeSchema [class]` (`672609f3-5a03-51fa-bc86-a90eef36aa9a`) lines 13-13 [crates/gwiki/src/schema.rs:13]
  - Signature: `pub struct GwikiRuntimeSchema;`
  - Purpose: 'GwikiRuntimeSchema' is a zero-sized public marker struct representing the runtime schema type. [crates/gwiki/src/schema.rs:13]
- `GwikiRuntimeSchema` (class) component `GwikiRuntimeSchema [class]` (`48f5906b-98e8-544a-9913-170285478c2b`) lines 15-24 [crates/gwiki/src/schema.rs:15-24]
  - Signature: `impl AttachedValidator for GwikiRuntimeSchema {`
  - Purpose: 'GwikiRuntimeSchema' implements 'AttachedValidator' by declaring every PostgreSQL table in 'GWIKI_POSTGRES_TABLES' and every index in 'GWIKI_POSTGRES_INDEXES' as a required relation via 'required_relation', returning them as 'Vec<RequiredObject>'. [crates/gwiki/src/schema.rs:15-24]
- `GwikiRuntimeSchema.required_objects` (method) component `GwikiRuntimeSchema.required_objects [method]` (`1b183599-3634-549f-ab6b-e549792a4828`) lines 16-23 [crates/gwiki/src/schema.rs:16-23]
  - Signature: `fn required_objects(&self) -> Vec<RequiredObject> {`
  - Purpose: Returns a 'Vec<RequiredObject>' by concatenating the names of all 'GWIKI_POSTGRES_TABLES' and all 'GWIKI_POSTGRES_INDEXES', converting each relation name with 'required_relation', and collecting the results. [crates/gwiki/src/schema.rs:16-23]
- `validate_runtime_schema` (function) component `validate_runtime_schema [function]` (`96282ed6-4c0a-5877-87c1-7c8d7ada0908`) lines 26-28 [crates/gwiki/src/schema.rs:26-28]
  - Signature: `pub fn validate_runtime_schema(ctx: &mut ValidationContext<'_>) -> ValidationReport {`
  - Purpose: 'validate_runtime_schema' delegates validation of the current 'ValidationContext' to 'GwikiRuntimeSchema' and returns the resulting 'ValidationReport'. [crates/gwiki/src/schema.rs:26-28]
- `required_relation` (function) component `required_relation [function]` (`1a3c4d96-b70b-5ddf-bd83-d8e18f68a7df`) lines 30-36 [crates/gwiki/src/schema.rs:30-36]
  - Signature: `fn required_relation(relation: &'static str) -> RequiredObject {`
  - Purpose: Constructs a 'RequiredObject' named from the given relation string, fixed to 'StoreKind::Postgres', with a validator closure that calls 'validate_relation(ctx, relation)'. [crates/gwiki/src/schema.rs:30-36]
- `validate_relation` (function) component `validate_relation [function]` (`6ed83ae4-c389-5518-85cc-292c3bf2c7ce`) lines 38-57 [crates/gwiki/src/schema.rs:38-57]
  - Signature: `fn validate_relation(ctx: &mut ValidationContext<'_>, relation: &str) -> Result<(), SetupIssue> {`
  - Purpose: 'validate_relation' checks that a PostgreSQL connection is present, queries 'to_regclass' for the qualified relation name to verify the relation exists, and returns a 'missing_relation_issue' error if the connection is absent, the query fails, or the relation is not found. [crates/gwiki/src/schema.rs:38-57]
- `relation_regclass_name` (function) component `relation_regclass_name [function]` (`a71e209a-f6ad-5f0c-bb3f-24939e4aa3dc`) lines 59-61 [crates/gwiki/src/schema.rs:59-61]
  - Signature: `fn relation_regclass_name(relation: &str) -> String {`
  - Purpose: Returns a schema-qualified regclass name by formatting 'relation' as '"{DEFAULT_SCHEMA}.{relation}"'. [crates/gwiki/src/schema.rs:59-61]
- `missing_relation_issue` (function) component `missing_relation_issue [function]` (`3c8b4c4b-47d9-54b6-af9f-cf7280d7c769`) lines 63-75 [crates/gwiki/src/schema.rs:63-75]
  - Signature: `fn missing_relation_issue(relation: &str, detail: &str) -> SetupIssue {`
  - Purpose: Constructs a 'SetupIssue' for a missing PostgreSQL-backed relation by naming the relation, formatting an unavailable-object error with the provided detail, and attaching remediation guidance to run Gobby hub migrations and verify with 'gwiki setup'. [crates/gwiki/src/schema.rs:63-75]
- `missing_schema_requires_explicit_setup` (function) component `missing_schema_requires_explicit_setup [function]` (`06a54909-c0ed-5e00-ade0-175bdf12d7b5`) lines 83-118 [crates/gwiki/src/schema.rs:83-118]
  - Signature: `fn missing_schema_requires_explicit_setup() {`
  - Purpose: Verifies that 'GwikiRuntimeSchema.validate' reports an unhealthy state with one missing issue per required GWIKI table/index, each pointing to the explicit 'gwiki setup' command, and that the non-test schema source contains no embedded DDL statements. [crates/gwiki/src/schema.rs:83-118]
- `relation_validation_qualifies_public_schema` (function) component `relation_validation_qualifies_public_schema [function]` (`23283e93-074b-5a17-9050-8b9d8de27f0b`) lines 121-126 [crates/gwiki/src/schema.rs:121-126]
  - Signature: `fn relation_validation_qualifies_public_schema() {`
  - Purpose: Verifies that 'relation_regclass_name("gwiki_documents")' resolves to the fully qualified public-schema name '"public.gwiki_documents"'. [crates/gwiki/src/schema.rs:121-126]

