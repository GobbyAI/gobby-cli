---
title: crates/gcore/src/secrets.rs
type: code_file
provenance:
- file: crates/gcore/src/secrets.rs
  ranges:
  - 18-22
  - 24-30
  - 33-63
  - 66-68
  - 70-103
  - 105-116
  - 118-133
  - 135-137
  - 139-168
  - 175-181
  - 184-189
  - 192-200
  - 203-211
  - 214-221
  - 224-232
  - 236-249
  - 252-257
  - 260-274
  - 277-282
  - 285-290
  - 293-304
  - 307-314
  - 316-324
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/secrets.rs:18-22](crates/gcore/src/secrets.rs#L18-L22), [crates/gcore/src/secrets.rs:24-30](crates/gcore/src/secrets.rs#L24-L30), [crates/gcore/src/secrets.rs:33-63](crates/gcore/src/secrets.rs#L33-L63), [crates/gcore/src/secrets.rs:66-68](crates/gcore/src/secrets.rs#L66-L68), [crates/gcore/src/secrets.rs:70-103](crates/gcore/src/secrets.rs#L70-L103), [crates/gcore/src/secrets.rs:105-116](crates/gcore/src/secrets.rs#L105-L116), [crates/gcore/src/secrets.rs:118-133](crates/gcore/src/secrets.rs#L118-L133), [crates/gcore/src/secrets.rs:135-137](crates/gcore/src/secrets.rs#L135-L137), [crates/gcore/src/secrets.rs:139-168](crates/gcore/src/secrets.rs#L139-L168), [crates/gcore/src/secrets.rs:175-181](crates/gcore/src/secrets.rs#L175-L181), [crates/gcore/src/secrets.rs:184-189](crates/gcore/src/secrets.rs#L184-L189), [crates/gcore/src/secrets.rs:192-200](crates/gcore/src/secrets.rs#L192-L200), [crates/gcore/src/secrets.rs:203-211](crates/gcore/src/secrets.rs#L203-L211), [crates/gcore/src/secrets.rs:214-221](crates/gcore/src/secrets.rs#L214-L221), [crates/gcore/src/secrets.rs:224-232](crates/gcore/src/secrets.rs#L224-L232), [crates/gcore/src/secrets.rs:236-249](crates/gcore/src/secrets.rs#L236-L249), [crates/gcore/src/secrets.rs:252-257](crates/gcore/src/secrets.rs#L252-L257), [crates/gcore/src/secrets.rs:260-274](crates/gcore/src/secrets.rs#L260-L274), [crates/gcore/src/secrets.rs:277-282](crates/gcore/src/secrets.rs#L277-L282), [crates/gcore/src/secrets.rs:285-290](crates/gcore/src/secrets.rs#L285-L290), [crates/gcore/src/secrets.rs:293-304](crates/gcore/src/secrets.rs#L293-L304), [crates/gcore/src/secrets.rs:307-314](crates/gcore/src/secrets.rs#L307-L314), [crates/gcore/src/secrets.rs:316-324](crates/gcore/src/secrets.rs#L316-L324)

</details>

# crates/gcore/src/secrets.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides secret resolution for Gobby by deriving a Fernet key from the local machine ID and secret salt, then decrypting encrypted values stored in the PostgreSQL `secrets` table. `resolve_secret` reads and validates the local inputs, normalizes the secret name, fetches the matching encrypted value, and decrypts it; `resolve_config_value` and `resolve_config_value_with` build on that to expand secret references inside config strings while enforcing name validation and boundary rules. The helper validators and byte/boundary checks keep secret references well-formed, and the tests verify deterministic key derivation, decryption, embedded and whole-value expansion, multiple secret handling, environment fallback, and rejection of invalid or unresolved references.
[crates/gcore/src/secrets.rs:18-22]
[crates/gcore/src/secrets.rs:24-30]
[crates/gcore/src/secrets.rs:33-63]
[crates/gcore/src/secrets.rs:66-68]
[crates/gcore/src/secrets.rs:70-103]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `derive_fernet_key` | function | `fn derive_fernet_key(machine_id: &str, salt: &[u8]) -> String {` | `derive_fernet_key [function]` | `3d3ccd99-88a8-5033-a967-2d314c63eddc` | 18-22 [crates/gcore/src/secrets.rs:18-22] | Indexed function `derive_fernet_key` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:18-22] |
| `decrypt_fernet` | function | `fn decrypt_fernet(key: &str, token: &str) -> anyhow::Result<String> {` | `decrypt_fernet [function]` | `d27d6f75-48dc-5c42-b6f8-3b36f07931f3` | 24-30 [crates/gcore/src/secrets.rs:24-30] | Indexed function `decrypt_fernet` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:24-30] |
| `resolve_secret` | function | `pub fn resolve_secret(conn: &mut Client, secret_name: &str) -> anyhow::Result<String> {` | `resolve_secret [function]` | `7c286602-bbb0-5486-a35a-49857a22112d` | 33-63 [crates/gcore/src/secrets.rs:33-63] | Indexed function `resolve_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:33-63] |
| `resolve_config_value` | function | `pub fn resolve_config_value(value: &str, conn: &mut Client) -> anyhow::Result<String> {` | `resolve_config_value [function]` | `95eeb62b-f968-5aae-b360-ead5d87344d9` | 66-68 [crates/gcore/src/secrets.rs:66-68] | Indexed function `resolve_config_value` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:66-68] |
| `resolve_config_value_with` | function | `fn resolve_config_value_with(` | `resolve_config_value_with [function]` | `da9acaf6-5ba9-5254-9fcf-d03ebfb6f27e` | 70-103 [crates/gcore/src/secrets.rs:70-103] | Indexed function `resolve_config_value_with` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:70-103] |
| `validate_secret_name` | function | `fn validate_secret_name(name: &str) -> anyhow::Result<()> {` | `validate_secret_name [function]` | `4c2ad425-e562-5cbb-9572-167e1914c509` | 105-116 [crates/gcore/src/secrets.rs:105-116] | Indexed function `validate_secret_name` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:105-116] |
| `validate_secret_reference_boundary` | function | `fn validate_secret_reference_boundary(` | `validate_secret_reference_boundary [function]` | `b6aa360b-c040-5c50-8df9-f543a569651a` | 118-133 [crates/gcore/src/secrets.rs:118-133] | Indexed function `validate_secret_reference_boundary` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:118-133] |
| `secret_name_byte` | function | `fn secret_name_byte(byte: u8) -> bool {` | `secret_name_byte [function]` | `124f314a-6603-58c5-b50a-26eb9091bf96` | 135-137 [crates/gcore/src/secrets.rs:135-137] | Indexed function `secret_name_byte` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:135-137] |
| `secret_boundary_char` | function | `fn secret_boundary_char(value: char) -> bool {` | `secret_boundary_char [function]` | `08f331af-3c82-5b3d-b068-b1987c1781c1` | 139-168 [crates/gcore/src/secrets.rs:139-168] | Indexed function `secret_boundary_char` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:139-168] |
| `derive_fernet_key_is_deterministic` | function | `fn derive_fernet_key_is_deterministic() {` | `derive_fernet_key_is_deterministic [function]` | `73bf51e4-8223-5bd6-892d-c6b608a7059a` | 175-181 [crates/gcore/src/secrets.rs:175-181] | Indexed function `derive_fernet_key_is_deterministic` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:175-181] |
| `derive_fernet_key_uses_salt` | function | `fn derive_fernet_key_uses_salt() {` | `derive_fernet_key_uses_salt [function]` | `bca2441f-146f-54f0-9b89-77d8617ae743` | 184-189 [crates/gcore/src/secrets.rs:184-189] | Indexed function `derive_fernet_key_uses_salt` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:184-189] |
| `decrypt_fernet_round_trips` | function | `fn decrypt_fernet_round_trips() {` | `decrypt_fernet_round_trips [function]` | `f0a1c24b-8fc2-56c4-bf4d-fe25b05e38c6` | 192-200 [crates/gcore/src/secrets.rs:192-200] | Indexed function `decrypt_fernet_round_trips` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:192-200] |
| `resolve_config_value_expands_embedded_secret` | function | `fn resolve_config_value_expands_embedded_secret() {` | `resolve_config_value_expands_embedded_secret [function]` | `efa12bf0-5ede-59e6-a7d6-6a315cfe1fa2` | 203-211 [crates/gcore/src/secrets.rs:203-211] | Indexed function `resolve_config_value_expands_embedded_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:203-211] |
| `resolve_config_value_expands_leading_whole_value_secret` | function | `fn resolve_config_value_expands_leading_whole_value_secret() {` | `resolve_config_value_expands_leading_whole_value_secret [function]` | `ee583bf2-89f6-5bd1-9173-b76369d88dd7` | 214-221 [crates/gcore/src/secrets.rs:214-221] | Indexed function `resolve_config_value_expands_leading_whole_value_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:214-221] |
| `resolve_config_value_expands_multiple_secrets` | function | `fn resolve_config_value_expands_multiple_secrets() {` | `resolve_config_value_expands_multiple_secrets [function]` | `be3ebac1-8051-5932-ad76-b3c42f241a31` | 224-232 [crates/gcore/src/secrets.rs:224-232] | Indexed function `resolve_config_value_expands_multiple_secrets` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:224-232] |
| `resolve_config_value_expands_secret_then_environment` | function | `fn resolve_config_value_expands_secret_then_environment() {` | `resolve_config_value_expands_secret_then_environment [function]` | `48896a36-b577-53dd-acca-5c5fe5a26a90` | 236-249 [crates/gcore/src/secrets.rs:236-249] | Indexed function `resolve_config_value_expands_secret_then_environment` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:236-249] |
| `resolve_config_value_rejects_unresolved_secret` | function | `fn resolve_config_value_rejects_unresolved_secret() {` | `resolve_config_value_rejects_unresolved_secret [function]` | `3a90a7df-fe6f-5672-9d59-3b959ad176f6` | 252-257 [crates/gcore/src/secrets.rs:252-257] | Indexed function `resolve_config_value_rejects_unresolved_secret` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:252-257] |
| `resolve_config_value_rejects_invalid_secret_names` | function | `fn resolve_config_value_rejects_invalid_secret_names() {` | `resolve_config_value_rejects_invalid_secret_names [function]` | `a9a8791d-6db2-5bc9-a479-a093eb09a60b` | 260-274 [crates/gcore/src/secrets.rs:260-274] | Indexed function `resolve_config_value_rejects_invalid_secret_names` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:260-274] |
| `validate_secret_name_rejects_empty_and_unsupported_names` | function | `fn validate_secret_name_rejects_empty_and_unsupported_names() {` | `validate_secret_name_rejects_empty_and_unsupported_names [function]` | `46d2c9b6-f385-523d-a945-dc55f6588372` | 277-282 [crates/gcore/src/secrets.rs:277-282] | Indexed function `validate_secret_name_rejects_empty_and_unsupported_names` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:277-282] |
| `resolve_config_value_rejects_unresolved_environment` | function | `fn resolve_config_value_rejects_unresolved_environment() {` | `resolve_config_value_rejects_unresolved_environment [function]` | `327a9d10-72e5-5cab-bf62-8e4fd242473f` | 285-290 [crates/gcore/src/secrets.rs:285-290] | Indexed function `resolve_config_value_rejects_unresolved_environment` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:285-290] |
| `unresolved_environment_omits_expanded_secret_output` | function | `fn unresolved_environment_omits_expanded_secret_output() {` | `unresolved_environment_omits_expanded_secret_output [function]` | `49c284eb-6fdd-56b4-bd2b-5630f419cec9` | 293-304 [crates/gcore/src/secrets.rs:293-304] | Indexed function `unresolved_environment_omits_expanded_secret_output` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:293-304] |
| `resolve_config_value_plain_value_uses_fast_path` | function | `fn resolve_config_value_plain_value_uses_fast_path() {` | `resolve_config_value_plain_value_uses_fast_path [function]` | `6c449785-7f46-589a-92d8-84f3d1666d9f` | 307-314 [crates/gcore/src/secrets.rs:307-314] | Indexed function `resolve_config_value_plain_value_uses_fast_path` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:307-314] |
| `test_secret_resolver` | function | `fn test_secret_resolver(name: &str) -> anyhow::Result<String> {` | `test_secret_resolver [function]` | `3fdf848d-2957-50c0-9afe-cc4a454a753e` | 316-324 [crates/gcore/src/secrets.rs:316-324] | Indexed function `test_secret_resolver` in `crates/gcore/src/secrets.rs`. [crates/gcore/src/secrets.rs:316-324] |
