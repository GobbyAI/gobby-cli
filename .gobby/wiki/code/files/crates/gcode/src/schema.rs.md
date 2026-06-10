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
  - 112-120
  - 124-129
  - 132-137
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/schema.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/schema.rs` exposes 9 indexed API symbols.
[crates/gcode/src/schema.rs:24-52]
[crates/gcode/src/schema.rs:54-63]
[crates/gcode/src/schema.rs:65-71]
[crates/gcode/src/schema.rs:73-88]
[crates/gcode/src/schema.rs:91-93]
[crates/gcode/src/schema.rs:99-105]
[crates/gcode/src/schema.rs:112-120]
[crates/gcode/src/schema.rs:124-129]
[crates/gcode/src/schema.rs:132-137]

## API Symbols

- `validate_runtime_schema` (function) component `validate_runtime_schema [function]` (`adf75c2a-46db-5cb0-8d2a-eb8bafd87a8d`) lines 24-52 [crates/gcode/src/schema.rs:24-52]
  - Signature: `pub fn validate_runtime_schema(client: &mut Client) -> anyhow::Result<()> {`
  - Purpose: `validate_runtime_schema` checks that the PostgreSQL client’s runtime schema contains the `pg_search` extension, the BM25 score stored procedure, all required tables, and all required BM25 indexes, and returns an error with a migration hint if any prerequisite is missing. [crates/gcode/src/schema.rs:24-52]
- `extension_exists` (function) component `extension_exists [function]` (`5c8c098a-08cb-5d57-a759-20eed195ad0a`) lines 54-63 [crates/gcode/src/schema.rs:54-63]
  - Signature: `fn extension_exists(client: &mut Client, extension: &str) -> anyhow::Result<bool> {`
  - Purpose: Checks PostgreSQL’s `pg_extension` catalog for a row whose `extname` matches the given name and returns `Ok(true)` or `Ok(false)`, attaching context if the query or boolean decode fails. [crates/gcode/src/schema.rs:54-63]
- `procedure_exists` (function) component `procedure_exists [function]` (`ae3f6e6a-a9ed-54bb-9072-7c3b52695f63`) lines 65-71 [crates/gcode/src/schema.rs:65-71]
  - Signature: `fn procedure_exists(client: &mut Client, procedure: &str) -> anyhow::Result<bool> {`
  - Purpose: Executes `SELECT to_regprocedure($1) IS NOT NULL` against PostgreSQL to return `true` when the given procedure name resolves to an existing `regprocedure`, otherwise `false`, while attaching context to query and decode failures. [crates/gcode/src/schema.rs:65-71]
- `missing_relations` (function) component `missing_relations [function]` (`a9cc14ab-1c4e-5309-ba0b-7261c3223c4a`) lines 73-88 [crates/gcode/src/schema.rs:73-88]
  - Signature: `fn missing_relations(client: &mut Client, relations: &[&str]) -> anyhow::Result<Vec<String>> {`
  - Purpose: Checks each relation name against `DEFAULT_SCHEMA` with `SELECT to_regclass($1) IS NOT NULL`, returning a `Vec<String>` of the input relations that do not exist in PostgreSQL, or an error if any existence check query or result decode fails. [crates/gcode/src/schema.rs:73-88]
- `required_relation_regclass_name` (function) component `required_relation_regclass_name [function]` (`d7648799-f584-5d53-9d54-5fb155831fd1`) lines 91-93 [crates/gcode/src/schema.rs:91-93]
  - Signature: `fn required_relation_regclass_name(relation: &str) -> String {`
  - Purpose: It returns the input `relation` prefixed with `DEFAULT_SCHEMA.` to produce a schema-qualified regclass name string. [crates/gcode/src/schema.rs:91-93]
- `required_schema_contract_names_code_index_tables_and_bm25_indexes` (function) component `required_schema_contract_names_code_index_tables_and_bm25_indexes [function]` (`a5d232ea-38f2-543c-a5cc-32837548312c`) lines 99-105 [crates/gcode/src/schema.rs:99-105]
  - Signature: `fn required_schema_contract_names_code_index_tables_and_bm25_indexes() {`
  - Purpose: This function verifies that the schema contract includes the `code_symbols` and `code_content_chunks` tables, the `code_symbols_search_bm25` and `code_content_search_bm25` BM25 indexes, and that `BM25_SCORE_REGPROCEDURE` equals `pdb.score(anyelement)`. [crates/gcode/src/schema.rs:99-105]
- `validates_runtime_schema_when_postgres_test_dsn_is_set` (function) component `validates_runtime_schema_when_postgres_test_dsn_is_set [function]` (`38e653de-169a-5be2-a62e-e6a3c2c14888`) lines 112-120 [crates/gcode/src/schema.rs:112-120]
  - Signature: `fn validates_runtime_schema_when_postgres_test_dsn_is_set() {`
  - Purpose: Returns early unless `GCODE_POSTGRES_TEST_DATABASE_URL` is set, then opens a read-write PostgreSQL connection to that URL and asserts `validate_runtime_schema(&mut client)` succeeds. [crates/gcode/src/schema.rs:112-120]
- `missing_schema_requires_setup` (function) component `missing_schema_requires_setup [function]` (`15e7262d-8f3e-5afe-a928-04f01b3df459`) lines 124-129 [crates/gcode/src/schema.rs:124-129]
  - Signature: `fn missing_schema_requires_setup() {`
  - Purpose: This test asserts that `MIGRATION_HINT` includes `gcode setup --standalone`, enforcing that missing runtime schema guidance directs standalone users to run explicit setup. [crates/gcode/src/schema.rs:124-129]
- `relation_validation_qualifies_public_schema` (function) component `relation_validation_qualifies_public_schema [function]` (`9b645547-0b6c-5fe8-aa8d-069622245b11`) lines 132-137 [crates/gcode/src/schema.rs:132-137]
  - Signature: `fn relation_validation_qualifies_public_schema() {`
  - Purpose: It verifies that `required_relation_regclass_name("code_symbols")` resolves an unqualified relation name to the schema-qualified form `"public.code_symbols"`. [crates/gcode/src/schema.rs:132-137]

