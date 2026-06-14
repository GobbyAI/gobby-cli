---
title: crates/gcode/src/setup/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/setup/tests.rs
  ranges:
  - 12-55
  - 58-84
  - 87-128
  - 130-155
  - 157-162
  - 165-180
  - 183-191
  - 194-224
  - 227-231
  - 234-244
  - 247-258
  - 261-274
  - 277-297
  - 300-313
  - 316-321
  - 324-329
  - 340-407
  - 410-422
  - 424-428
  - 430-436
  - 438-443
  - 447-458
  - 462-471
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/setup/tests.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

This file is the test suite for `gcode` standalone setup behavior. It checks that `GcodeStandaloneSetup` exposes the right public code-index objects and Postgres-backed contract, that its DDL and overwrite/reset SQL match the expected catalog rules, and that helper functions and request/status types handle identifier limits, timeouts, redaction, serialization, and destructive-Postgres safeguards correctly.
[crates/gcode/src/setup/tests.rs:12-55]
[crates/gcode/src/setup/tests.rs:58-84]
[crates/gcode/src/setup/tests.rs:59]
[crates/gcode/src/setup/tests.rs:87-128]
[crates/gcode/src/setup/tests.rs:130-155]

## API Symbols

- `standalone_setup_declares_public_daemon_code_index_subset` (function) component `standalone_setup_declares_public_daemon_code_index_subset [function]` (`3f576cbb-ecde-5d08-985b-b905c2f96002`) lines 12-55 [crates/gcode/src/setup/tests.rs:12-55]
  - Signature: `fn standalone_setup_declares_public_daemon_code_index_subset() {`
  - Purpose: This test verifies that a `GcodeStandaloneSetup` with public schema declares the required code-indexing database objects (indexed_files, symbols, content_chunks, idx_cif, bm25) while excluding forbidden sensitive and internal objects. [crates/gcode/src/setup/tests.rs:12-55]
- `standalone_setup_uses_gobby_core_contract` (function) component `standalone_setup_uses_gobby_core_contract [function]` (`e8cfbbad-619b-5c7f-b1d3-c9cba8e7fd66`) lines 58-84 [crates/gcode/src/setup/tests.rs:58-84]
  - Signature: `fn standalone_setup_uses_gobby_core_contract() {`
  - Purpose: Verifies that `GcodeStandaloneSetup` implements the `StandaloneSetup` trait and owns Postgres-backed objects including a `code_symbols` table, BM25 full-text search index, and `pg_search` extension. [crates/gcode/src/setup/tests.rs:58-84]
- `assert_standalone_setup` (function) component `assert_standalone_setup [function]` (`75d487dd-bf32-5d1f-a787-f8ac4f48545b`) lines 59-59 [crates/gcode/src/setup/tests.rs:59]
  - Signature: `fn assert_standalone_setup<T: StandaloneSetup>() {}`
  - Purpose: This is a compile-time assertion function that enforces a type parameter `T` implements the `StandaloneSetup` trait, with no runtime behavior. [crates/gcode/src/setup/tests.rs:59]
- `standalone_setup_ddl_matches_catalog_contracts` (function) component `standalone_setup_ddl_matches_catalog_contracts [function]` (`d80d2822-a0a2-588c-be75-db3e66a9ed5f`) lines 87-128 [crates/gcode/src/setup/tests.rs:87-128]
  - Signature: `fn standalone_setup_ddl_matches_catalog_contracts() {`
  - Purpose: Validates that PostgreSQL DDL definitions extracted from the Gcode standalone setup conform to table and index contracts by asserting matching column schemas, index creation statements, and index methods. [crates/gcode/src/setup/tests.rs:87-128]
- `table_columns` (function) component `table_columns [function]` (`c44b3dce-b26c-56ac-921a-42ac6f9449e7`) lines 130-155 [crates/gcode/src/setup/tests.rs:130-155]
  - Signature: `fn table_columns(sql: &str) -> Vec<&str> {`
  - Purpose: Parses a CREATE TABLE DDL statement and returns the column identifiers by extracting the first token from each column definition line while skipping table-level constraints. [crates/gcode/src/setup/tests.rs:130-155]
- `normalized_sql` (function) component `normalized_sql [function]` (`474e86f6-d808-5308-9be4-3ecbdd4d6ea4`) lines 157-162 [crates/gcode/src/setup/tests.rs:157-162]
  - Signature: `fn normalized_sql(sql: &str) -> String {`
  - Purpose: Normalizes SQL by collapsing consecutive whitespace into single spaces and converting to ASCII lowercase. [crates/gcode/src/setup/tests.rs:157-162]
- `standalone_setup_create_propagates_owned_object_errors` (function) component `standalone_setup_create_propagates_owned_object_errors [function]` (`1b5d92ba-2a26-51ae-9d87-72a0ecb95430`) lines 165-180 [crates/gcode/src/setup/tests.rs:165-180]
  - Signature: `fn standalone_setup_create_propagates_owned_object_errors() {`
  - Purpose: This test verifies that `GcodeStandaloneSetup::create()` properly propagates a validation error when an owned object schema identifier exceeds the 63-byte maximum length constraint. [crates/gcode/src/setup/tests.rs:165-180]
- `standalone_setup_rejects_non_public_schema` (function) component `standalone_setup_rejects_non_public_schema [function]` (`c048fcc8-57a3-52fc-8295-5a4d17d5fb4e`) lines 183-191 [crates/gcode/src/setup/tests.rs:183-191]
  - Signature: `fn standalone_setup_rejects_non_public_schema() {`
  - Purpose: This test asserts that `validate_standalone_request` rejects standalone setup requests specifying non-public database schemas by returning an error message containing "public". [crates/gcode/src/setup/tests.rs:183-191]
- `overwrite_reset_sql_is_allowlisted` (function) component `overwrite_reset_sql_is_allowlisted [function]` (`d0c722e3-7152-507e-8f81-3ca442b395dd`) lines 194-224 [crates/gcode/src/setup/tests.rs:194-224]
  - Signature: `fn overwrite_reset_sql_is_allowlisted() {`
  - Purpose: Asserts that the PostgreSQL reset SQL for the "public" schema drops all code-indexed tables and indexes while excluding protected resources (config_store, schema_migrations, secrets, etc.) and CASCADE/DROP DATABASE/SCHEMA operations. [crates/gcode/src/setup/tests.rs:194-224]
- `overwrite_guidance_names_flag` (function) component `overwrite_guidance_names_flag [function]` (`e869ee1d-bcec-5c11-bf30-d510b248d4fc`) lines 227-231 [crates/gcode/src/setup/tests.rs:227-231]
  - Signature: `fn overwrite_guidance_names_flag() {`
  - Purpose: This test function verifies that a newly instantiated `StandaloneSetupRequest` defaults to `overwrite_code_index` being disabled and that the `--overwrite-code-index` flag is documented in the `OVERWRITE_GUIDANCE` constant. [crates/gcode/src/setup/tests.rs:227-231]
- `standalone_setup_request_redacts_password_in_json` (function) component `standalone_setup_request_redacts_password_in_json [function]` (`e0e7d9a3-cc81-59af-92b7-5491b8ff5e61`) lines 234-244 [crates/gcode/src/setup/tests.rs:234-244]
  - Signature: `fn standalone_setup_request_redacts_password_in_json() {`
  - Purpose: Tests that `StandaloneSetupRequest` redacts sensitive fields (`falkordb_password` and `database_url`) during JSON serialization to prevent credential exposure. [crates/gcode/src/setup/tests.rs:234-244]
- `standalone_setup_request_redacts_database_url_in_json` (function) component `standalone_setup_request_redacts_database_url_in_json [function]` (`6da7716e-8b9d-55e0-ab45-a98198c520c7`) lines 247-258 [crates/gcode/src/setup/tests.rs:247-258]
  - Signature: `fn standalone_setup_request_redacts_database_url_in_json() {`
  - Purpose: This unit test verifies that `StandaloneSetupRequest` redacts the database URL field name and secret credentials when serialized to JSON. [crates/gcode/src/setup/tests.rs:247-258]
- `standalone_setup_request_debug_redacts_database_url` (function) component `standalone_setup_request_debug_redacts_database_url [function]` (`206524a3-7595-54bc-a159-5e8f206b82b0`) lines 261-274 [crates/gcode/src/setup/tests.rs:261-274]
  - Signature: `fn standalone_setup_request_debug_redacts_database_url() {`
  - Purpose: Tests that the Debug implementation of `StandaloneSetupRequest` redacts sensitive credentials (database URLs and passwords) by replacing them with `<redacted>` markers. [crates/gcode/src/setup/tests.rs:261-274]
- `standalone_setup_status_serializes_failures_as_objects` (function) component `standalone_setup_status_serializes_failures_as_objects [function]` (`18c1bda4-b878-5b61-b32d-7d57cd5840aa`) lines 277-297 [crates/gcode/src/setup/tests.rs:277-297]
  - Signature: `fn standalone_setup_status_serializes_failures_as_objects() {`
  - Purpose: This test verifies that `StandaloneSetupStatus` serializes failure items as JSON objects (not arrays) with accessible `name` and `reason` fields. [crates/gcode/src/setup/tests.rs:277-297]
- `setup_test_database_url_adds_connect_timeout` (function) component `setup_test_database_url_adds_connect_timeout [function]` (`cbddf32b-fe2f-5bfb-a80a-61a6c133a5e5`) lines 300-313 [crates/gcode/src/setup/tests.rs:300-313]
  - Signature: `fn setup_test_database_url_adds_connect_timeout() {`
  - Purpose: This test verifies that `database_url_with_connect_timeout` correctly appends a default 5-second connection timeout to PostgreSQL database URLs while properly handling existing query parameters and preserving pre-existing timeout values. [crates/gcode/src/setup/tests.rs:300-313]
- `quote_identifier_rejects_names_over_postgres_byte_limit` (function) component `quote_identifier_rejects_names_over_postgres_byte_limit [function]` (`99c06abf-0932-5669-a2fd-10c7075a852b`) lines 316-321 [crates/gcode/src/setup/tests.rs:316-321]
  - Signature: `fn quote_identifier_rejects_names_over_postgres_byte_limit() {`
  - Purpose: This test verifies that `quote_identifier` rejects identifiers exceeding PostgreSQL's 63-byte limit and returns an error message indicating this constraint. [crates/gcode/src/setup/tests.rs:316-321]
- `quote_identifier_accepts_raw_limit_even_when_escaping_expands` (function) component `quote_identifier_accepts_raw_limit_even_when_escaping_expands [function]` (`71b3132f-835a-541a-a5e4-42a0601d3e0f`) lines 324-329 [crates/gcode/src/setup/tests.rs:324-329]
  - Signature: `fn quote_identifier_accepts_raw_limit_even_when_escaping_expands() {`
  - Purpose: # Summary

This test verifies that `quote_identifier` validates the raw input length (not the post-escaping length) when enforcing identifier length limits, allowing a 62-character identifier with a trailing quote character to pass validation even though escaping doubles the quote in the output. [crates/gcode/src/setup/tests.rs:324-329]
- `overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table` (function) component `overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table [function]` (`5b29f6f8-b8fb-5aea-9096-ccb9e71da0c1`) lines 340-407 [crates/gcode/src/setup/tests.rs:340-407]
  - Signature: `fn overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table() {`
  - Purpose: Indexed function `overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:340-407]
- `destructive_postgres_test_allowed` (function) component `destructive_postgres_test_allowed [function]` (`a8708006-b143-57ac-8ea7-a7d766ad09ee`) lines 410-422 [crates/gcode/src/setup/tests.rs:410-422]
  - Signature: `fn destructive_postgres_test_allowed(database_url: &str) -> Result<(), String> {`
  - Purpose: Indexed function `destructive_postgres_test_allowed` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:410-422]
- `destructive_postgres_test_override_enabled` (function) component `destructive_postgres_test_override_enabled [function]` (`904f2572-f1c8-5101-8733-89e0659c09a4`) lines 424-428 [crates/gcode/src/setup/tests.rs:424-428]
  - Signature: `fn destructive_postgres_test_override_enabled() -> bool {`
  - Purpose: Indexed function `destructive_postgres_test_override_enabled` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:424-428]
- `database_url_with_connect_timeout` (function) component `database_url_with_connect_timeout [function]` (`da5ff6a6-14ef-5c25-a891-84f4d333e60f`) lines 430-436 [crates/gcode/src/setup/tests.rs:430-436]
  - Signature: `fn database_url_with_connect_timeout(database_url: &str) -> String {`
  - Purpose: Indexed function `database_url_with_connect_timeout` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:430-436]
- `cleanup_code_index_relations` (function) component `cleanup_code_index_relations [function]` (`40902f66-8497-5989-b560-fdf1f294aa39`) lines 438-443 [crates/gcode/src/setup/tests.rs:438-443]
  - Signature: `fn cleanup_code_index_relations(client: &mut Client) {`
  - Purpose: Indexed function `cleanup_code_index_relations` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:438-443]
- `destructive_postgres_guard_requires_test_database_name` (function) component `destructive_postgres_guard_requires_test_database_name [function]` (`67c8249e-ec85-5b2b-b71e-7f1e5073e638`) lines 447-458 [crates/gcode/src/setup/tests.rs:447-458]
  - Signature: `fn destructive_postgres_guard_requires_test_database_name() {`
  - Purpose: Indexed function `destructive_postgres_guard_requires_test_database_name` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:447-458]
- `destructive_postgres_guard_accepts_explicit_override_values` (function) component `destructive_postgres_guard_accepts_explicit_override_values [function]` (`4e5cf3ef-d937-5eb7-bfab-2b61c84a53eb`) lines 462-471 [crates/gcode/src/setup/tests.rs:462-471]
  - Signature: `fn destructive_postgres_guard_accepts_explicit_override_values() {`
  - Purpose: Indexed function `destructive_postgres_guard_accepts_explicit_override_values` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:462-471]

