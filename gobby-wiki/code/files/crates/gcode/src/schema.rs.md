---
title: crates/gcode/src/schema.rs
type: code_file
provenance:
- file: crates/gcode/src/schema.rs
  ranges:
  - 24-52
  - 54-63
  - 65-71
  - 73-88
  - 91-93
  - 99-105
  - 116-123
  - 127-132
  - 135-140
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/schema.rs:24-52](crates/gcode/src/schema.rs#L24-L52), [crates/gcode/src/schema.rs:54-63](crates/gcode/src/schema.rs#L54-L63), [crates/gcode/src/schema.rs:65-71](crates/gcode/src/schema.rs#L65-L71), [crates/gcode/src/schema.rs:73-88](crates/gcode/src/schema.rs#L73-L88), [crates/gcode/src/schema.rs:91-93](crates/gcode/src/schema.rs#L91-L93), [crates/gcode/src/schema.rs:99-105](crates/gcode/src/schema.rs#L99-L105), [crates/gcode/src/schema.rs:116-123](crates/gcode/src/schema.rs#L116-L123), [crates/gcode/src/schema.rs:127-132](crates/gcode/src/schema.rs#L127-L132), [crates/gcode/src/schema.rs:135-140](crates/gcode/src/schema.rs#L135-L140)

</details>

# crates/gcode/src/schema.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file validates that a runtime PostgreSQL hub schema is ready for Gobby code indexing. `validate_runtime_schema` checks for the `pg_search` extension, the BM25 scoring procedure, the required code-index tables, and the required BM25 indexes, and returns a clear setup/migration hint when anything is missing. The helper functions `extension_exists`, `procedure_exists`, and `missing_relations` query PostgreSQL metadata to test for those prerequisites, while `required_relation_regclass_name` and the required-table/index constants define the expected objects. The tests confirm the validator behaves correctly when the test DSN is present, reports a missing schema as a setup requirement, and qualifies relation names in the public schema.
[crates/gcode/src/schema.rs:24-52]
[crates/gcode/src/schema.rs:54-63]
[crates/gcode/src/schema.rs:65-71]
[crates/gcode/src/schema.rs:73-88]
[crates/gcode/src/schema.rs:91-93]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `validate_runtime_schema` | function | `pub fn validate_runtime_schema(client: &mut Client) -> anyhow::Result<()> {` | `validate_runtime_schema [function]` | `adf75c2a-46db-5cb0-8d2a-eb8bafd87a8d` | 24-52 [crates/gcode/src/schema.rs:24-52] | Indexed function `validate_runtime_schema` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:24-52] |
| `extension_exists` | function | `fn extension_exists(client: &mut Client, extension: &str) -> anyhow::Result<bool> {` | `extension_exists [function]` | `5c8c098a-08cb-5d57-a759-20eed195ad0a` | 54-63 [crates/gcode/src/schema.rs:54-63] | Indexed function `extension_exists` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:54-63] |
| `procedure_exists` | function | `fn procedure_exists(client: &mut Client, procedure: &str) -> anyhow::Result<bool> {` | `procedure_exists [function]` | `ae3f6e6a-a9ed-54bb-9072-7c3b52695f63` | 65-71 [crates/gcode/src/schema.rs:65-71] | Indexed function `procedure_exists` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:65-71] |
| `missing_relations` | function | `fn missing_relations(client: &mut Client, relations: &[&str]) -> anyhow::Result<Vec<String>> {` | `missing_relations [function]` | `a9cc14ab-1c4e-5309-ba0b-7261c3223c4a` | 73-88 [crates/gcode/src/schema.rs:73-88] | Indexed function `missing_relations` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:73-88] |
| `required_relation_regclass_name` | function | `fn required_relation_regclass_name(relation: &str) -> String {` | `required_relation_regclass_name [function]` | `d7648799-f584-5d53-9d54-5fb155831fd1` | 91-93 [crates/gcode/src/schema.rs:91-93] | Indexed function `required_relation_regclass_name` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:91-93] |
| `required_schema_contract_names_code_index_tables_and_bm25_indexes` | function | `fn required_schema_contract_names_code_index_tables_and_bm25_indexes() {` | `required_schema_contract_names_code_index_tables_and_bm25_indexes [function]` | `a5d232ea-38f2-543c-a5cc-32837548312c` | 99-105 [crates/gcode/src/schema.rs:99-105] | Indexed function `required_schema_contract_names_code_index_tables_and_bm25_indexes` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:99-105] |
| `validates_runtime_schema_when_postgres_test_dsn_is_set` | function | `fn validates_runtime_schema_when_postgres_test_dsn_is_set() {` | `validates_runtime_schema_when_postgres_test_dsn_is_set [function]` | `52413b93-42d7-5ac0-9eae-8ec893e60908` | 116-123 [crates/gcode/src/schema.rs:116-123] | Indexed function `validates_runtime_schema_when_postgres_test_dsn_is_set` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:116-123] |
| `missing_schema_requires_setup` | function | `fn missing_schema_requires_setup() {` | `missing_schema_requires_setup [function]` | `ed4a76b3-0990-507d-be46-0068f4883db9` | 127-132 [crates/gcode/src/schema.rs:127-132] | Indexed function `missing_schema_requires_setup` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:127-132] |
| `relation_validation_qualifies_public_schema` | function | `fn relation_validation_qualifies_public_schema() {` | `relation_validation_qualifies_public_schema [function]` | `cebd5590-90dd-56e5-8214-eba948346301` | 135-140 [crates/gcode/src/schema.rs:135-140] | Indexed function `relation_validation_qualifies_public_schema` in `crates/gcode/src/schema.rs`. [crates/gcode/src/schema.rs:135-140] |
