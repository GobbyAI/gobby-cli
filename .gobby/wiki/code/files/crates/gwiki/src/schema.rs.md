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

`crates/gwiki/src/schema.rs` exposes 10 indexed API symbols.
[crates/gwiki/src/schema.rs:13]
[crates/gwiki/src/schema.rs:15-24]
[crates/gwiki/src/schema.rs:16-23]
[crates/gwiki/src/schema.rs:26-28]
[crates/gwiki/src/schema.rs:30-36]

## API Symbols

- `GwikiRuntimeSchema` (class) component `GwikiRuntimeSchema [class]` (`672609f3-5a03-51fa-bc86-a90eef36aa9a`) lines 13-13 [crates/gwiki/src/schema.rs:13]
  - Signature: `pub struct GwikiRuntimeSchema;`
  - Purpose: Indexed class `GwikiRuntimeSchema` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:13]
- `GwikiRuntimeSchema` (class) component `GwikiRuntimeSchema [class]` (`48f5906b-98e8-544a-9913-170285478c2b`) lines 15-24 [crates/gwiki/src/schema.rs:15-24]
  - Signature: `impl AttachedValidator for GwikiRuntimeSchema {`
  - Purpose: Indexed class `GwikiRuntimeSchema` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:15-24]
- `GwikiRuntimeSchema.required_objects` (method) component `GwikiRuntimeSchema.required_objects [method]` (`1b183599-3634-549f-ab6b-e549792a4828`) lines 16-23 [crates/gwiki/src/schema.rs:16-23]
  - Signature: `fn required_objects(&self) -> Vec<RequiredObject> {`
  - Purpose: Indexed method `GwikiRuntimeSchema.required_objects` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:16-23]
- `validate_runtime_schema` (function) component `validate_runtime_schema [function]` (`96282ed6-4c0a-5877-87c1-7c8d7ada0908`) lines 26-28 [crates/gwiki/src/schema.rs:26-28]
  - Signature: `pub fn validate_runtime_schema(ctx: &mut ValidationContext<'_>) -> ValidationReport {`
  - Purpose: Indexed function `validate_runtime_schema` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:26-28]
- `required_relation` (function) component `required_relation [function]` (`1a3c4d96-b70b-5ddf-bd83-d8e18f68a7df`) lines 30-36 [crates/gwiki/src/schema.rs:30-36]
  - Signature: `fn required_relation(relation: &'static str) -> RequiredObject {`
  - Purpose: Indexed function `required_relation` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:30-36]
- `validate_relation` (function) component `validate_relation [function]` (`6ed83ae4-c389-5518-85cc-292c3bf2c7ce`) lines 38-57 [crates/gwiki/src/schema.rs:38-57]
  - Signature: `fn validate_relation(ctx: &mut ValidationContext<'_>, relation: &str) -> Result<(), SetupIssue> {`
  - Purpose: Indexed function `validate_relation` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:38-57]
- `relation_regclass_name` (function) component `relation_regclass_name [function]` (`a71e209a-f6ad-5f0c-bb3f-24939e4aa3dc`) lines 59-61 [crates/gwiki/src/schema.rs:59-61]
  - Signature: `fn relation_regclass_name(relation: &str) -> String {`
  - Purpose: Indexed function `relation_regclass_name` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:59-61]
- `missing_relation_issue` (function) component `missing_relation_issue [function]` (`3c8b4c4b-47d9-54b6-af9f-cf7280d7c769`) lines 63-75 [crates/gwiki/src/schema.rs:63-75]
  - Signature: `fn missing_relation_issue(relation: &str, detail: &str) -> SetupIssue {`
  - Purpose: Indexed function `missing_relation_issue` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:63-75]
- `missing_schema_requires_explicit_setup` (function) component `missing_schema_requires_explicit_setup [function]` (`06a54909-c0ed-5e00-ade0-175bdf12d7b5`) lines 83-118 [crates/gwiki/src/schema.rs:83-118]
  - Signature: `fn missing_schema_requires_explicit_setup() {`
  - Purpose: Indexed function `missing_schema_requires_explicit_setup` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:83-118]
- `relation_validation_qualifies_public_schema` (function) component `relation_validation_qualifies_public_schema [function]` (`23283e93-074b-5a17-9050-8b9d8de27f0b`) lines 121-126 [crates/gwiki/src/schema.rs:121-126]
  - Signature: `fn relation_validation_qualifies_public_schema() {`
  - Purpose: Indexed function `relation_validation_qualifies_public_schema` in `crates/gwiki/src/schema.rs`. [crates/gwiki/src/schema.rs:121-126]

