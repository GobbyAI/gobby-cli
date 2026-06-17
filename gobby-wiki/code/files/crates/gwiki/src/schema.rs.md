---
title: crates/gwiki/src/schema.rs
type: code_file
provenance:
- file: crates/gwiki/src/schema.rs
  ranges:
  - '13'
  - 16-23
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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/schema.rs:13](crates/gwiki/src/schema.rs#L13), [crates/gwiki/src/schema.rs:16-23](crates/gwiki/src/schema.rs#L16-L23), [crates/gwiki/src/schema.rs:26-28](crates/gwiki/src/schema.rs#L26-L28), [crates/gwiki/src/schema.rs:30-36](crates/gwiki/src/schema.rs#L30-L36), [crates/gwiki/src/schema.rs:38-57](crates/gwiki/src/schema.rs#L38-L57), [crates/gwiki/src/schema.rs:59-61](crates/gwiki/src/schema.rs#L59-L61), [crates/gwiki/src/schema.rs:63-75](crates/gwiki/src/schema.rs#L63-L75), [crates/gwiki/src/schema.rs:83-118](crates/gwiki/src/schema.rs#L83-L118), [crates/gwiki/src/schema.rs:121-126](crates/gwiki/src/schema.rs#L121-L126)

</details>

# crates/gwiki/src/schema.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines runtime validation for gwiki-owned PostgreSQL schema objects. `GwikiRuntimeSchema` collects the required tables and indexes, `validate_runtime_schema` runs the attached validator, and the helper functions check each relation through PostgreSQL `to_regclass`, qualify names in the `public` schema, and return setup issues with migration guidance when a required object is missing or no database connection is available.
[crates/gwiki/src/schema.rs:13]
[crates/gwiki/src/schema.rs:16-23]
[crates/gwiki/src/schema.rs:26-28]
[crates/gwiki/src/schema.rs:30-36]
[crates/gwiki/src/schema.rs:38-57]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GwikiRuntimeSchema` | class | `pub struct GwikiRuntimeSchema;` | `GwikiRuntimeSchema [class]` | `672609f3-5a03-51fa-bc86-a90eef36aa9a` | 13-13 [crates/gwiki/src/schema.rs:13] | Indexed class `GwikiRuntimeSchema` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:13] |
| `GwikiRuntimeSchema::required_objects` | method | `fn required_objects(&self) -> Vec<RequiredObject> {` | `GwikiRuntimeSchema::required_objects [method]` | `1b183599-3634-549f-ab6b-e549792a4828` | 16-23 [crates/gwiki/src/schema.rs:16-23] | Indexed method `GwikiRuntimeSchema::required_objects` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:16-23] |
| `validate_runtime_schema` | function | `pub fn validate_runtime_schema(ctx: &mut ValidationContext<'_>) -> ValidationReport {` | `validate_runtime_schema [function]` | `96282ed6-4c0a-5877-87c1-7c8d7ada0908` | 26-28 [crates/gwiki/src/schema.rs:26-28] | Indexed function `validate_runtime_schema` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:26-28] |
| `required_relation` | function | `fn required_relation(relation: &'static str) -> RequiredObject {` | `required_relation [function]` | `1a3c4d96-b70b-5ddf-bd83-d8e18f68a7df` | 30-36 [crates/gwiki/src/schema.rs:30-36] | Indexed function `required_relation` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:30-36] |
| `validate_relation` | function | `fn validate_relation(ctx: &mut ValidationContext<'_>, relation: &str) -> Result<(), SetupIssue> {` | `validate_relation [function]` | `6ed83ae4-c389-5518-85cc-292c3bf2c7ce` | 38-57 [crates/gwiki/src/schema.rs:38-57] | Indexed function `validate_relation` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:38-57] |
| `relation_regclass_name` | function | `fn relation_regclass_name(relation: &str) -> String {` | `relation_regclass_name [function]` | `a71e209a-f6ad-5f0c-bb3f-24939e4aa3dc` | 59-61 [crates/gwiki/src/schema.rs:59-61] | Indexed function `relation_regclass_name` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:59-61] |
| `missing_relation_issue` | function | `fn missing_relation_issue(relation: &str, detail: &str) -> SetupIssue {` | `missing_relation_issue [function]` | `3c8b4c4b-47d9-54b6-af9f-cf7280d7c769` | 63-75 [crates/gwiki/src/schema.rs:63-75] | Indexed function `missing_relation_issue` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:63-75] |
| `missing_schema_requires_explicit_setup` | function | `fn missing_schema_requires_explicit_setup() {` | `missing_schema_requires_explicit_setup [function]` | `06a54909-c0ed-5e00-ade0-175bdf12d7b5` | 83-118 [crates/gwiki/src/schema.rs:83-118] | Indexed function `missing_schema_requires_explicit_setup` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:83-118] |
| `relation_validation_qualifies_public_schema` | function | `fn relation_validation_qualifies_public_schema() {` | `relation_validation_qualifies_public_schema [function]` | `23283e93-074b-5a17-9050-8b9d8de27f0b` | 121-126 [crates/gwiki/src/schema.rs:121-126] | Indexed function `relation_validation_qualifies_public_schema` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:121-126] |
