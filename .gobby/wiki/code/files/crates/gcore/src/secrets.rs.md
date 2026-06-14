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

# crates/gcore/src/secrets.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file implements Gobby’s secret resolution pipeline. It derives a Fernet key from the local machine ID and salt with PBKDF2-HMAC-SHA256, decrypts encrypted secret values, and looks up named secrets from the PostgreSQL `secrets` table before decrypting them. It also resolves configuration strings by expanding `$secret:NAME` placeholders first, then environment-variable patterns, and rejects any unresolved references.

The helper functions support that flow: `validate_secret_name` and the boundary/character predicates enforce safe secret names and placeholder parsing, while `resolve_config_value_with` drives substitution using a caller-provided secret resolver. The test functions cover deterministic key derivation, salt sensitivity, Fernet round-trips, secret and environment expansion behavior, unresolved-reference errors, and protection against leaking secret values in error messages.
[crates/gcore/src/secrets.rs:18-22]
[crates/gcore/src/secrets.rs:24-30]
[crates/gcore/src/secrets.rs:33-63]
[crates/gcore/src/secrets.rs:66-68]
[crates/gcore/src/secrets.rs:70-103]

## API Symbols

- `derive_fernet_key` (function) component `derive_fernet_key [function]` (`3d3ccd99-88a8-5033-a967-2d314c63eddc`) lines 18-22 [crates/gcore/src/secrets.rs:18-22]
  - Signature: `fn derive_fernet_key(machine_id: &str, salt: &[u8]) -> String {`
  - Purpose: Derives a URL-safe base64-encoded Fernet key by applying PBKDF2-HMAC-SHA256 with 600,000 iterations to a machine ID and salt, producing a 32-byte cryptographic key. [crates/gcore/src/secrets.rs:18-22]
- `decrypt_fernet` (function) component `decrypt_fernet [function]` (`d27d6f75-48dc-5c42-b6f8-3b36f07931f3`) lines 24-30 [crates/gcore/src/secrets.rs:24-30]
  - Signature: `fn decrypt_fernet(key: &str, token: &str) -> anyhow::Result<String> {`
  - Purpose: Decrypts a Fernet-encrypted token using the provided key and returns the plaintext as a UTF-8 string, with error propagation for invalid keys, decryption failures, and UTF-8 conversion errors. [crates/gcore/src/secrets.rs:24-30]
- `resolve_secret` (function) component `resolve_secret [function]` (`7c286602-bbb0-5486-a35a-49857a22112d`) lines 33-63 [crates/gcore/src/secrets.rs:33-63]
  - Signature: `pub fn resolve_secret(conn: &mut Client, secret_name: &str) -> anyhow::Result<String> {`
  - Purpose: Retrieves an encrypted secret from a database and decrypts it using a Fernet key derived from a stored machine ID and salt. [crates/gcore/src/secrets.rs:33-63]
- `resolve_config_value` (function) component `resolve_config_value [function]` (`95eeb62b-f968-5aae-b360-ead5d87344d9`) lines 66-68 [crates/gcore/src/secrets.rs:66-68]
  - Signature: `pub fn resolve_config_value(value: &str, conn: &mut Client) -> anyhow::Result<String> {`
  - Purpose: Resolves a configuration value string by delegating to `resolve_config_value_with` with database-backed secret resolution via the provided client connection. [crates/gcore/src/secrets.rs:66-68]
- `resolve_config_value_with` (function) component `resolve_config_value_with [function]` (`da9acaf6-5ba9-5254-9fcf-d03ebfb6f27e`) lines 70-103 [crates/gcore/src/secrets.rs:70-103]
  - Signature: `fn resolve_config_value_with(`
  - Purpose: Replaces `$secret:NAME` references in a configuration string with values obtained from a provided resolver function, then resolves environment variable patterns, returning an error if any patterns remain unresolved. [crates/gcore/src/secrets.rs:70-103]
- `validate_secret_name` (function) component `validate_secret_name [function]` (`4c2ad425-e562-5cbb-9572-167e1914c509`) lines 105-116 [crates/gcore/src/secrets.rs:105-116]
  - Signature: `fn validate_secret_name(name: &str) -> anyhow::Result<()> {`
  - Purpose: Validates a secret name by ensuring it is non-empty, does not exceed `SECRET_NAME_MAX_LEN` characters, and contains only supported characters as determined by the `secret_name_byte` predicate. [crates/gcore/src/secrets.rs:105-116]
- `validate_secret_reference_boundary` (function) component `validate_secret_reference_boundary [function]` (`b6aa360b-c040-5c50-8df9-f543a569651a`) lines 118-133 [crates/gcore/src/secrets.rs:118-133]
  - Signature: `fn validate_secret_reference_boundary(`
  - Purpose: # Summary

Validates that a secret variable reference has a proper boundary by ensuring the remainder is either empty, begins with a new secret marker (`$secret:` or `${`), or starts with a boundary character. [crates/gcore/src/secrets.rs:118-133]
- `secret_name_byte` (function) component `secret_name_byte [function]` (`124f314a-6603-58c5-b50a-26eb9091bf96`) lines 135-137 [crates/gcore/src/secrets.rs:135-137]
  - Signature: `fn secret_name_byte(byte: u8) -> bool {`
  - Purpose: Returns true if the byte is an ASCII alphanumeric character or one of the special characters underscore, hyphen, or period. [crates/gcore/src/secrets.rs:135-137]
- `secret_boundary_char` (function) component `secret_boundary_char [function]` (`08f331af-3c82-5b3d-b068-b1987c1781c1`) lines 139-168 [crates/gcore/src/secrets.rs:139-168]
  - Signature: `fn secret_boundary_char(value: char) -> bool {`
  - Purpose: Returns `true` if the input character is either ASCII whitespace or one of a predefined set of special characters commonly used as delimiters in URLs and structured text. [crates/gcore/src/secrets.rs:139-168]
- `derive_fernet_key_is_deterministic` (function) component `derive_fernet_key_is_deterministic [function]` (`73bf51e4-8223-5bd6-892d-c6b608a7059a`) lines 175-181 [crates/gcore/src/secrets.rs:175-181]
  - Signature: `fn derive_fernet_key_is_deterministic() {`
  - Purpose: This test function verifies that `derive_fernet_key` is deterministic by asserting that identical inputs produce identical non-empty cryptographic key outputs. [crates/gcore/src/secrets.rs:175-181]
- `derive_fernet_key_uses_salt` (function) component `derive_fernet_key_uses_salt [function]` (`bca2441f-146f-54f0-9b89-77d8617ae743`) lines 184-189 [crates/gcore/src/secrets.rs:184-189]
  - Signature: `fn derive_fernet_key_uses_salt() {`
  - Purpose: This test verifies that the `derive_fernet_key` function produces distinct keys when given identical machine IDs but different salt values. [crates/gcore/src/secrets.rs:184-189]
- `decrypt_fernet_round_trips` (function) component `decrypt_fernet_round_trips [function]` (`f0a1c24b-8fc2-56c4-bf4d-fe25b05e38c6`) lines 192-200 [crates/gcore/src/secrets.rs:192-200]
  - Signature: `fn decrypt_fernet_round_trips() {`
  - Purpose: This function tests that Fernet encryption and decryption with a derived key successfully recovers the original plaintext in a round-trip operation. [crates/gcore/src/secrets.rs:192-200]
- `resolve_config_value_expands_embedded_secret` (function) component `resolve_config_value_expands_embedded_secret [function]` (`efa12bf0-5ede-59e6-a7d6-6a315cfe1fa2`) lines 203-211 [crates/gcore/src/secrets.rs:203-211]
  - Signature: `fn resolve_config_value_expands_embedded_secret() {`
  - Purpose: A unit test verifying that `resolve_config_value_with` correctly substitutes embedded secret references (e.g., `$secret:DB_PASS`) with their resolved values using a provided secret resolver function. [crates/gcore/src/secrets.rs:203-211]
- `resolve_config_value_expands_leading_whole_value_secret` (function) component `resolve_config_value_expands_leading_whole_value_secret [function]` (`ee583bf2-89f6-5bd1-9173-b76369d88dd7`) lines 214-221 [crates/gcore/src/secrets.rs:214-221]
  - Signature: `fn resolve_config_value_expands_leading_whole_value_secret() {`
  - Purpose: This test verifies that a config value consisting entirely of a `$secret:NAME` reference is correctly resolved to its corresponding secret value. [crates/gcore/src/secrets.rs:214-221]
- `resolve_config_value_expands_multiple_secrets` (function) component `resolve_config_value_expands_multiple_secrets [function]` (`be3ebac1-8051-5932-ad76-b3c42f241a31`) lines 224-232 [crates/gcore/src/secrets.rs:224-232]
  - Signature: `fn resolve_config_value_expands_multiple_secrets() {`
  - Purpose: This unit test verifies that `resolve_config_value_with` correctly resolves and substitutes multiple secret placeholders (e.g., `$secret:USER` and `$secret:PASSWORD`) within a single configuration value string. [crates/gcore/src/secrets.rs:224-232]
- `resolve_config_value_expands_secret_then_environment` (function) component `resolve_config_value_expands_secret_then_environment [function]` (`48896a36-b577-53dd-acca-5c5fe5a26a90`) lines 236-249 [crates/gcore/src/secrets.rs:236-249]
  - Signature: `fn resolve_config_value_expands_secret_then_environment() {`
  - Purpose: Unit test that verifies `resolve_config_value_with()` correctly expands both environment variable placeholders (`${VAR}`) and secret references (`$secret:KEY`) within a configuration template string. [crates/gcore/src/secrets.rs:236-249]
- `resolve_config_value_rejects_unresolved_secret` (function) component `resolve_config_value_rejects_unresolved_secret [function]` (`3a90a7df-fe6f-5672-9d59-3b959ad176f6`) lines 252-257 [crates/gcore/src/secrets.rs:252-257]
  - Signature: `fn resolve_config_value_rejects_unresolved_secret() {`
  - Purpose: This test verifies that `resolve_config_value_with` properly rejects an unresolved secret reference by asserting the returned error message contains the expected missing secret identifier. [crates/gcore/src/secrets.rs:252-257]
- `resolve_config_value_rejects_invalid_secret_names` (function) component `resolve_config_value_rejects_invalid_secret_names [function]` (`a9a8791d-6db2-5bc9-a479-a093eb09a60b`) lines 260-274 [crates/gcore/src/secrets.rs:260-274]
  - Signature: `fn resolve_config_value_rejects_invalid_secret_names() {`
  - Purpose: This test function verifies that `resolve_config_value_with` correctly rejects secret references containing invalid boundary characters and those exceeding the maximum allowed secret name length. [crates/gcore/src/secrets.rs:260-274]
- `validate_secret_name_rejects_empty_and_unsupported_names` (function) component `validate_secret_name_rejects_empty_and_unsupported_names [function]` (`46d2c9b6-f385-523d-a945-dc55f6588372`) lines 277-282 [crates/gcore/src/secrets.rs:277-282]
  - Signature: `fn validate_secret_name_rejects_empty_and_unsupported_names() {`
  - Purpose: This test asserts that the `validate_secret_name` function rejects empty strings and names containing forward slashes or spaces, while accepting names with alphanumerics, dots, and hyphens. [crates/gcore/src/secrets.rs:277-282]
- `resolve_config_value_rejects_unresolved_environment` (function) component `resolve_config_value_rejects_unresolved_environment [function]` (`327a9d10-72e5-5cab-bf62-8e4fd242473f`) lines 285-290 [crates/gcore/src/secrets.rs:285-290]
  - Signature: `fn resolve_config_value_rejects_unresolved_environment() {`
  - Purpose: This test asserts that `resolve_config_value_with` rejects unresolved environment variable patterns by returning an error containing the message "unresolved environment pattern". [crates/gcore/src/secrets.rs:285-290]
- `unresolved_environment_omits_expanded_secret_output` (function) component `unresolved_environment_omits_expanded_secret_output [function]` (`49c284eb-6fdd-56b4-bd2b-5630f419cec9`) lines 293-304 [crates/gcore/src/secrets.rs:293-304]
  - Signature: `fn unresolved_environment_omits_expanded_secret_output() {`
  - Purpose: This test verifies that when config value resolution fails due to an unresolved environment variable, the resulting error message omits both the secret placeholder and its expanded value to prevent credential leakage. [crates/gcore/src/secrets.rs:293-304]
- `resolve_config_value_plain_value_uses_fast_path` (function) component `resolve_config_value_plain_value_uses_fast_path [function]` (`6c449785-7f46-589a-92d8-84f3d1666d9f`) lines 307-314 [crates/gcore/src/secrets.rs:307-314]
  - Signature: `fn resolve_config_value_plain_value_uses_fast_path() {`
  - Purpose: This test verifies that `resolve_config_value_with` successfully resolves plain string values without invoking the provided secret resolver callback. [crates/gcore/src/secrets.rs:307-314]
- `test_secret_resolver` (function) component `test_secret_resolver [function]` (`3fdf848d-2957-50c0-9afe-cc4a454a753e`) lines 316-324 [crates/gcore/src/secrets.rs:316-324]
  - Signature: `fn test_secret_resolver(name: &str) -> anyhow::Result<String> {`
  - Purpose: Returns a hardcoded test secret string for a given name, or an error if the name doesn't match one of the four predefined secrets (API_KEY, DB_PASS, PASSWORD, USER). [crates/gcore/src/secrets.rs:316-324]

