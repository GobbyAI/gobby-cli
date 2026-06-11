---
title: crates/gwiki/src/schema.rs
type: code_file
provenance:
- file: crates/gwiki/src/schema.rs
  ranges:
  - '12'
  - 14-23
  - 15-22
  - 25-27
  - 29-35
  - 37-56
  - 58-60
  - 62-74
  - 82-117
  - 120-125
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/schema.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/schema.rs` exposes 10 indexed API symbols.
[crates/gwiki/src/schema.rs:12]
[crates/gwiki/src/schema.rs:14-23]
[crates/gwiki/src/schema.rs:15-22]
[crates/gwiki/src/schema.rs:25-27]
[crates/gwiki/src/schema.rs:29-35]

## API Symbols

- `GwikiRuntimeSchema` (class) component `GwikiRuntimeSchema [class]` (`8bc428bf-f184-5bc1-8ac8-9169ac5dc464`) lines 12-12 [crates/gwiki/src/schema.rs:12]
  - Signature: `pub struct GwikiRuntimeSchema;`
  - Purpose: GwikiRuntimeSchema is a public, zero-sized unit struct serving as a marker type for Gwiki runtime schema representation. [crates/gwiki/src/schema.rs:12]
- `GwikiRuntimeSchema` (class) component `GwikiRuntimeSchema [class]` (`37418929-29b3-5473-86aa-b6a0103e3b39`) lines 14-23 [crates/gwiki/src/schema.rs:14-23]
  - Signature: `impl AttachedValidator for GwikiRuntimeSchema {`
  - Purpose: GwikiRuntimeSchema implements AttachedValidator to declare all PostgreSQL tables and indexes from the application configuration as required runtime dependencies for schema validation. [crates/gwiki/src/schema.rs:14-23]
- `GwikiRuntimeSchema.required_objects` (method) component `GwikiRuntimeSchema.required_objects [method]` (`cc81297a-f5a1-50ad-8ff8-b504eaccd986`) lines 15-22 [crates/gwiki/src/schema.rs:15-22]
  - Signature: `fn required_objects(&self) -> Vec<RequiredObject> {`
  - Purpose: Constructs a `Vec<RequiredObject>` by mapping PostgreSQL table names and index references from static constants through the `required_relation` function. [crates/gwiki/src/schema.rs:15-22]
- `validate_runtime_schema` (function) component `validate_runtime_schema [function]` (`c5079966-114b-5fa9-94c9-fcb6cbf7ac6d`) lines 25-27 [crates/gwiki/src/schema.rs:25-27]
  - Signature: `pub fn validate_runtime_schema(ctx: &mut ValidationContext<'_>) -> ValidationReport {`
  - Purpose: Validates the GwikiRuntimeSchema against a provided ValidationContext, returning a ValidationReport. [crates/gwiki/src/schema.rs:25-27]
- `required_relation` (function) component `required_relation [function]` (`757c24f8-6ba8-5430-9187-8191f7159655`) lines 29-35 [crates/gwiki/src/schema.rs:29-35]
  - Signature: `fn required_relation(relation: &'static str) -> RequiredObject {`
  - Purpose: Creates a `RequiredObject` that specifies a required PostgreSQL relation with a boxed validator closure parameterized by the relation name. [crates/gwiki/src/schema.rs:29-35]
- `validate_relation` (function) component `validate_relation [function]` (`b4004dab-844b-5e8c-8258-179b6813ced9`) lines 37-56 [crates/gwiki/src/schema.rs:37-56]
  - Signature: `fn validate_relation(ctx: &mut ValidationContext<'_>, relation: &str) -> Result<(), SetupIssue> {`
  - Purpose: Verifies a PostgreSQL relation exists by executing a `to_regclass` query against the provided database connection, returning `Ok(())` on success or a `SetupIssue` error if the relation is missing or the connection is unavailable. [crates/gwiki/src/schema.rs:37-56]
- `relation_regclass_name` (function) component `relation_regclass_name [function]` (`34dc523c-c05f-5b59-865b-d703009ce06d`) lines 58-60 [crates/gwiki/src/schema.rs:58-60]
  - Signature: `fn relation_regclass_name(relation: &str) -> String {`
  - Purpose: Constructs a schema-qualified relation name by prepending a `DEFAULT_SCHEMA` constant to the input relation identifier. [crates/gwiki/src/schema.rs:58-60]
- `missing_relation_issue` (function) component `missing_relation_issue [function]` (`3e2a2c20-a8a9-5501-a449-6af4c55f4bad`) lines 62-74 [crates/gwiki/src/schema.rs:62-74]
  - Signature: `fn missing_relation_issue(relation: &str, detail: &str) -> SetupIssue {`
  - Purpose: Constructs a `SetupIssue` for a missing PostgreSQL datastore relation, populated with diagnostic problem description, remediation action (Gobby hub migrations + gwiki setup validation), and a command hint. [crates/gwiki/src/schema.rs:62-74]
- `missing_schema_requires_explicit_setup` (function) component `missing_schema_requires_explicit_setup [function]` (`acba4173-f248-599d-9e6c-4db023c56947`) lines 82-117 [crates/gwiki/src/schema.rs:82-117]
  - Signature: `fn missing_schema_requires_explicit_setup() {`
  - Purpose: This test validates that `GwikiRuntimeSchema` validation fails appropriately with all missing PostgreSQL tables and indexes when database configuration is absent, directing users to explicit `gwiki setup` command rather than relying on inline DDL statements. [crates/gwiki/src/schema.rs:82-117]
- `relation_validation_qualifies_public_schema` (function) component `relation_validation_qualifies_public_schema [function]` (`637cec79-6c6a-5f98-a24a-1219ae29e082`) lines 120-125 [crates/gwiki/src/schema.rs:120-125]
  - Signature: `fn relation_validation_qualifies_public_schema() {`
  - Purpose: This test verifies that `relation_regclass_name()` qualifies an unqualified relation name ("gwiki_documents") with the "public" schema prefix. [crates/gwiki/src/schema.rs:120-125]

