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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/setup/tests.rs:12-55](crates/gcode/src/setup/tests.rs#L12-L55), [crates/gcode/src/setup/tests.rs:58-84](crates/gcode/src/setup/tests.rs#L58-L84), [crates/gcode/src/setup/tests.rs:87-128](crates/gcode/src/setup/tests.rs#L87-L128), [crates/gcode/src/setup/tests.rs:130-155](crates/gcode/src/setup/tests.rs#L130-L155), [crates/gcode/src/setup/tests.rs:157-162](crates/gcode/src/setup/tests.rs#L157-L162), [crates/gcode/src/setup/tests.rs:165-180](crates/gcode/src/setup/tests.rs#L165-L180), [crates/gcode/src/setup/tests.rs:183-191](crates/gcode/src/setup/tests.rs#L183-L191), [crates/gcode/src/setup/tests.rs:194-224](crates/gcode/src/setup/tests.rs#L194-L224), [crates/gcode/src/setup/tests.rs:227-231](crates/gcode/src/setup/tests.rs#L227-L231), [crates/gcode/src/setup/tests.rs:234-244](crates/gcode/src/setup/tests.rs#L234-L244), [crates/gcode/src/setup/tests.rs:247-258](crates/gcode/src/setup/tests.rs#L247-L258), [crates/gcode/src/setup/tests.rs:261-274](crates/gcode/src/setup/tests.rs#L261-L274), [crates/gcode/src/setup/tests.rs:277-297](crates/gcode/src/setup/tests.rs#L277-L297), [crates/gcode/src/setup/tests.rs:300-313](crates/gcode/src/setup/tests.rs#L300-L313), [crates/gcode/src/setup/tests.rs:316-321](crates/gcode/src/setup/tests.rs#L316-L321), [crates/gcode/src/setup/tests.rs:324-329](crates/gcode/src/setup/tests.rs#L324-L329), [crates/gcode/src/setup/tests.rs:340-407](crates/gcode/src/setup/tests.rs#L340-L407), [crates/gcode/src/setup/tests.rs:410-422](crates/gcode/src/setup/tests.rs#L410-L422), [crates/gcode/src/setup/tests.rs:424-428](crates/gcode/src/setup/tests.rs#L424-L428), [crates/gcode/src/setup/tests.rs:430-436](crates/gcode/src/setup/tests.rs#L430-L436), [crates/gcode/src/setup/tests.rs:438-443](crates/gcode/src/setup/tests.rs#L438-L443), [crates/gcode/src/setup/tests.rs:447-458](crates/gcode/src/setup/tests.rs#L447-L458), [crates/gcode/src/setup/tests.rs:462-471](crates/gcode/src/setup/tests.rs#L462-L471)

</details>

# crates/gcode/src/setup/tests.rs

Module: [[code/modules/crates/gcode/src/setup|crates/gcode/src/setup]]

## Purpose

`crates/gcode/src/setup/tests.rs` is a test module for the Gcode standalone setup and its PostgreSQL setup helpers. The tests verify that `GcodeStandaloneSetup` exposes the expected public daemon subset, satisfies the `gobby_core` `StandaloneSetup` contract, produces DDL and overwrite SQL that match catalog and contract rules, redacts sensitive connection data in serialized requests, handles identifier-length and connect-timeout edge cases, and enforces the destructive Postgres guard and cleanup behavior for incompatible code index relations.
[crates/gcode/src/setup/tests.rs:12-55]
[crates/gcode/src/setup/tests.rs:58-84]
[crates/gcode/src/setup/tests.rs:59]
[crates/gcode/src/setup/tests.rs:87-128]
[crates/gcode/src/setup/tests.rs:130-155]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `standalone_setup_declares_public_daemon_code_index_subset` | function | `fn standalone_setup_declares_public_daemon_code_index_subset() {` | `standalone_setup_declares_public_daemon_code_index_subset [function]` | `3f576cbb-ecde-5d08-985b-b905c2f96002` | 12-55 [crates/gcode/src/setup/tests.rs:12-55] | Indexed function `standalone_setup_declares_public_daemon_code_index_subset` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:12-55] |
| `standalone_setup_uses_gobby_core_contract` | function | `fn standalone_setup_uses_gobby_core_contract() {` | `standalone_setup_uses_gobby_core_contract [function]` | `e8cfbbad-619b-5c7f-b1d3-c9cba8e7fd66` | 58-84 [crates/gcode/src/setup/tests.rs:58-84] | Indexed function `standalone_setup_uses_gobby_core_contract` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:58-84] |
| `assert_standalone_setup` | function | `fn assert_standalone_setup<T: StandaloneSetup>() {}` | `assert_standalone_setup [function]` | `75d487dd-bf32-5d1f-a787-f8ac4f48545b` | 59-59 [crates/gcode/src/setup/tests.rs:59] | Indexed function `assert_standalone_setup` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:59] |
| `standalone_setup_ddl_matches_catalog_contracts` | function | `fn standalone_setup_ddl_matches_catalog_contracts() {` | `standalone_setup_ddl_matches_catalog_contracts [function]` | `d80d2822-a0a2-588c-be75-db3e66a9ed5f` | 87-128 [crates/gcode/src/setup/tests.rs:87-128] | Indexed function `standalone_setup_ddl_matches_catalog_contracts` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:87-128] |
| `table_columns` | function | `fn table_columns(sql: &str) -> Vec<&str> {` | `table_columns [function]` | `c44b3dce-b26c-56ac-921a-42ac6f9449e7` | 130-155 [crates/gcode/src/setup/tests.rs:130-155] | Indexed function `table_columns` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:130-155] |
| `normalized_sql` | function | `fn normalized_sql(sql: &str) -> String {` | `normalized_sql [function]` | `474e86f6-d808-5308-9be4-3ecbdd4d6ea4` | 157-162 [crates/gcode/src/setup/tests.rs:157-162] | Indexed function `normalized_sql` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:157-162] |
| `standalone_setup_create_propagates_owned_object_errors` | function | `fn standalone_setup_create_propagates_owned_object_errors() {` | `standalone_setup_create_propagates_owned_object_errors [function]` | `1b5d92ba-2a26-51ae-9d87-72a0ecb95430` | 165-180 [crates/gcode/src/setup/tests.rs:165-180] | Indexed function `standalone_setup_create_propagates_owned_object_errors` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:165-180] |
| `standalone_setup_rejects_non_public_schema` | function | `fn standalone_setup_rejects_non_public_schema() {` | `standalone_setup_rejects_non_public_schema [function]` | `c048fcc8-57a3-52fc-8295-5a4d17d5fb4e` | 183-191 [crates/gcode/src/setup/tests.rs:183-191] | Indexed function `standalone_setup_rejects_non_public_schema` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:183-191] |
| `overwrite_reset_sql_is_allowlisted` | function | `fn overwrite_reset_sql_is_allowlisted() {` | `overwrite_reset_sql_is_allowlisted [function]` | `d0c722e3-7152-507e-8f81-3ca442b395dd` | 194-224 [crates/gcode/src/setup/tests.rs:194-224] | Indexed function `overwrite_reset_sql_is_allowlisted` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:194-224] |
| `overwrite_guidance_names_flag` | function | `fn overwrite_guidance_names_flag() {` | `overwrite_guidance_names_flag [function]` | `e869ee1d-bcec-5c11-bf30-d510b248d4fc` | 227-231 [crates/gcode/src/setup/tests.rs:227-231] | Indexed function `overwrite_guidance_names_flag` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:227-231] |
| `standalone_setup_request_redacts_password_in_json` | function | `fn standalone_setup_request_redacts_password_in_json() {` | `standalone_setup_request_redacts_password_in_json [function]` | `e0e7d9a3-cc81-59af-92b7-5491b8ff5e61` | 234-244 [crates/gcode/src/setup/tests.rs:234-244] | Indexed function `standalone_setup_request_redacts_password_in_json` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:234-244] |
| `standalone_setup_request_redacts_database_url_in_json` | function | `fn standalone_setup_request_redacts_database_url_in_json() {` | `standalone_setup_request_redacts_database_url_in_json [function]` | `6da7716e-8b9d-55e0-ab45-a98198c520c7` | 247-258 [crates/gcode/src/setup/tests.rs:247-258] | Indexed function `standalone_setup_request_redacts_database_url_in_json` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:247-258] |
| `standalone_setup_request_debug_redacts_database_url` | function | `fn standalone_setup_request_debug_redacts_database_url() {` | `standalone_setup_request_debug_redacts_database_url [function]` | `206524a3-7595-54bc-a159-5e8f206b82b0` | 261-274 [crates/gcode/src/setup/tests.rs:261-274] | Indexed function `standalone_setup_request_debug_redacts_database_url` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:261-274] |
| `standalone_setup_status_serializes_failures_as_objects` | function | `fn standalone_setup_status_serializes_failures_as_objects() {` | `standalone_setup_status_serializes_failures_as_objects [function]` | `18c1bda4-b878-5b61-b32d-7d57cd5840aa` | 277-297 [crates/gcode/src/setup/tests.rs:277-297] | Indexed function `standalone_setup_status_serializes_failures_as_objects` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:277-297] |
| `setup_test_database_url_adds_connect_timeout` | function | `fn setup_test_database_url_adds_connect_timeout() {` | `setup_test_database_url_adds_connect_timeout [function]` | `cbddf32b-fe2f-5bfb-a80a-61a6c133a5e5` | 300-313 [crates/gcode/src/setup/tests.rs:300-313] | Indexed function `setup_test_database_url_adds_connect_timeout` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:300-313] |
| `quote_identifier_rejects_names_over_postgres_byte_limit` | function | `fn quote_identifier_rejects_names_over_postgres_byte_limit() {` | `quote_identifier_rejects_names_over_postgres_byte_limit [function]` | `99c06abf-0932-5669-a2fd-10c7075a852b` | 316-321 [crates/gcode/src/setup/tests.rs:316-321] | Indexed function `quote_identifier_rejects_names_over_postgres_byte_limit` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:316-321] |
| `quote_identifier_accepts_raw_limit_even_when_escaping_expands` | function | `fn quote_identifier_accepts_raw_limit_even_when_escaping_expands() {` | `quote_identifier_accepts_raw_limit_even_when_escaping_expands [function]` | `71b3132f-835a-541a-a5e4-42a0601d3e0f` | 324-329 [crates/gcode/src/setup/tests.rs:324-329] | Indexed function `quote_identifier_accepts_raw_limit_even_when_escaping_expands` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:324-329] |
| `overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table` | function | `fn overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table() {` | `overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table [function]` | `5b29f6f8-b8fb-5aea-9096-ccb9e71da0c1` | 340-407 [crates/gcode/src/setup/tests.rs:340-407] | Indexed function `overwrite_recreates_incompatible_code_index_and_preserves_sentinel_table` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:340-407] |
| `destructive_postgres_test_allowed` | function | `fn destructive_postgres_test_allowed(database_url: &str) -> Result<(), String> {` | `destructive_postgres_test_allowed [function]` | `a8708006-b143-57ac-8ea7-a7d766ad09ee` | 410-422 [crates/gcode/src/setup/tests.rs:410-422] | Indexed function `destructive_postgres_test_allowed` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:410-422] |
| `destructive_postgres_test_override_enabled` | function | `fn destructive_postgres_test_override_enabled() -> bool {` | `destructive_postgres_test_override_enabled [function]` | `904f2572-f1c8-5101-8733-89e0659c09a4` | 424-428 [crates/gcode/src/setup/tests.rs:424-428] | Indexed function `destructive_postgres_test_override_enabled` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:424-428] |
| `database_url_with_connect_timeout` | function | `fn database_url_with_connect_timeout(database_url: &str) -> String {` | `database_url_with_connect_timeout [function]` | `da5ff6a6-14ef-5c25-a891-84f4d333e60f` | 430-436 [crates/gcode/src/setup/tests.rs:430-436] | Indexed function `database_url_with_connect_timeout` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:430-436] |
| `cleanup_code_index_relations` | function | `fn cleanup_code_index_relations(client: &mut Client) {` | `cleanup_code_index_relations [function]` | `40902f66-8497-5989-b560-fdf1f294aa39` | 438-443 [crates/gcode/src/setup/tests.rs:438-443] | Indexed function `cleanup_code_index_relations` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:438-443] |
| `destructive_postgres_guard_requires_test_database_name` | function | `fn destructive_postgres_guard_requires_test_database_name() {` | `destructive_postgres_guard_requires_test_database_name [function]` | `67c8249e-ec85-5b2b-b71e-7f1e5073e638` | 447-458 [crates/gcode/src/setup/tests.rs:447-458] | Indexed function `destructive_postgres_guard_requires_test_database_name` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:447-458] |
| `destructive_postgres_guard_accepts_explicit_override_values` | function | `fn destructive_postgres_guard_accepts_explicit_override_values() {` | `destructive_postgres_guard_accepts_explicit_override_values [function]` | `4e5cf3ef-d937-5eb7-bfab-2b61c84a53eb` | 462-471 [crates/gcode/src/setup/tests.rs:462-471] | Indexed function `destructive_postgres_guard_accepts_explicit_override_values` in `crates/gcode/src/setup/tests.rs`. [crates/gcode/src/setup/tests.rs:462-471] |
