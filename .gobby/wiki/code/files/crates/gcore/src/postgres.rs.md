---
title: crates/gcore/src/postgres.rs
type: code_file
provenance:
- file: crates/gcore/src/postgres.rs
  ranges:
  - 16-22
  - 25-27
  - 36-45
  - 49-58
  - 66-71
  - 73-101
  - 104-110
  - 112-119
  - 121-134
  - 136-150
  - 152-167
  - 169-207
  - 209-222
  - 224-229
  - 231-233
  - 235-240
  - 242-254
  - 256-261
  - 263-276
  - 278-283
  - 290-308
  - 311-332
  - 335-345
  - 348-379
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/postgres.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/postgres.rs` exposes 24 indexed API symbols.
[crates/gcore/src/postgres.rs:16-22]
[crates/gcore/src/postgres.rs:25-27]
[crates/gcore/src/postgres.rs:36-45]
[crates/gcore/src/postgres.rs:49-58]
[crates/gcore/src/postgres.rs:66-71]

## API Symbols

- `connect_readonly` (function) component `connect_readonly [function]` (`b6ae4827-a3bd-53c4-b6d5-4559dacbccaf`) lines 16-22 [crates/gcore/src/postgres.rs:16-22]
  - Signature: `pub fn connect_readonly(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: Establishes and returns a read-only PostgreSQL client connection by setting `default_transaction_read_only = on` after connecting to the specified database URL. [crates/gcore/src/postgres.rs:16-22]
- `connect_readwrite` (function) component `connect_readwrite [function]` (`08dc312a-ceb4-5ee6-afba-542006539117`) lines 25-27 [crates/gcore/src/postgres.rs:25-27]
  - Signature: `pub fn connect_readwrite(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: Establishes a database connection for read-write operations by delegating to the `connect` function, returning an `anyhow::Result` containing a `Client` instance. [crates/gcore/src/postgres.rs:25-27]
- `read_config_value` (function) component `read_config_value [function]` (`3c95270a-cf64-5a37-b25d-4a9e0e1e5550`) lines 36-45 [crates/gcore/src/postgres.rs:36-45]
  - Signature: `pub fn read_config_value(conn: &mut Client, key: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Queries a PostgreSQL config_store table to fetch an optional string value for a given key, with error handling for query and deserialization failures. [crates/gcore/src/postgres.rs:36-45]
- `SchemaCheck` (class) component `SchemaCheck [class]` (`f2b3b2c3-dd1f-5b6c-8973-ffe748d79633`) lines 49-58 [crates/gcore/src/postgres.rs:49-58]
  - Signature: `pub struct SchemaCheck {`
  - Purpose: SchemaCheck is a struct that encapsulates the result of a database schema validation check, storing the checked object name, the type of check performed, its pass/fail status, and optional failure details. [crates/gcore/src/postgres.rs:49-58]
- `validate_schema` (function) component `validate_schema [function]` (`962e2dbd-e6fc-58a1-bddd-d6189ab94f20`) lines 66-71 [crates/gcore/src/postgres.rs:66-71]
  - Signature: `pub fn validate_schema(`
  - Purpose: # validate_schema

Executes a one-time validator closure against a mutable database client and delegates the result to `run_schema_validator`, returning a vector of schema validation checks. [crates/gcore/src/postgres.rs:66-71]
- `connect` (function) component `connect [function]` (`0cef6de5-fda4-5e26-b187-93108786a96e`) lines 73-101 [crates/gcore/src/postgres.rs:73-101]
  - Signature: `fn connect(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: Establishes a PostgreSQL Client connection by parsing the database URL and applying the appropriate TLS configuration based on the requested sslmode parameter, with a fallback to unencrypted connection for `sslmode=prefer`. [crates/gcore/src/postgres.rs:73-101]
- `RequestedSslMode` (type) component `RequestedSslMode [type]` (`c6d2e5e5-f769-5090-88ac-b0cccfc256d3`) lines 104-110 [crates/gcore/src/postgres.rs:104-110]
  - Signature: `enum RequestedSslMode {`
  - Purpose: Indexed type `RequestedSslMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:104-110]
- `requested_ssl_mode_from_config` (function) component `requested_ssl_mode_from_config [function]` (`d04d2210-79fd-56b3-a77a-66a30f686098`) lines 112-119 [crates/gcore/src/postgres.rs:112-119]
  - Signature: `fn requested_ssl_mode_from_config(config: &postgres::Config) -> RequestedSslMode {`
  - Purpose: This function converts a PostgreSQL configuration's SSL mode setting to a `RequestedSslMode` enum, directly mapping `Disable`, `Prefer`, and `Require` modes while defaulting to `Prefer` for any unmatched variants. [crates/gcore/src/postgres.rs:112-119]
- `requested_ssl_mode` (function) component `requested_ssl_mode [function]` (`9d8d5c4d-4046-5537-a53b-c46a37e0ce7d`) lines 121-134 [crates/gcore/src/postgres.rs:121-134]
  - Signature: `fn requested_ssl_mode(database_url: &str) -> Option<RequestedSslMode> {`
  - Purpose: Parses the PostgreSQL `sslmode` parameter from a database URL string into its corresponding `RequestedSslMode` enum variant, returning `None` for unrecognized values. [crates/gcore/src/postgres.rs:121-134]
- `sslmode_value` (function) component `sslmode_value [function]` (`b33bf823-0b2f-534f-a810-4173c96dbae9`) lines 136-150 [crates/gcore/src/postgres.rs:136-150]
  - Signature: `fn sslmode_value(database_url: &str) -> Option<String> {`
  - Purpose: Extracts and normalizes the `sslmode` connection parameter from a database URL, supporting both query string and libpq keyword token formats. [crates/gcore/src/postgres.rs:136-150]
- `normalize_sslmode_for_parser` (function) component `normalize_sslmode_for_parser [function]` (`603f89a0-3657-5c86-aa32-7b04f484de4a`) lines 152-167 [crates/gcore/src/postgres.rs:152-167]
  - Signature: `fn normalize_sslmode_for_parser(database_url: &str) -> String {`
  - Purpose: Normalizes sslmode parameters in PostgreSQL database URLs by parsing and transforming both URL query string and libpq keyword-value formats. [crates/gcore/src/postgres.rs:152-167]
- `split_libpq_keyword_tokens` (function) component `split_libpq_keyword_tokens [function]` (`50e3522f-b746-51ef-a501-1569c6925932`) lines 169-207 [crates/gcore/src/postgres.rs:169-207]
  - Signature: `fn split_libpq_keyword_tokens(database_url: &str) -> Vec<&str> {`
  - Purpose: Tokenizes a libpq connection string by splitting on whitespace while respecting single-quoted substrings and backslash escape sequences. [crates/gcore/src/postgres.rs:169-207]
- `normalize_sslmode_pair` (function) component `normalize_sslmode_pair [function]` (`c586293a-9621-5bed-a6a2-5d1912bbb5f1`) lines 209-222 [crates/gcore/src/postgres.rs:209-222]
  - Signature: `fn normalize_sslmode_pair(pair: &str) -> String {`
  - Purpose: Normalizes an SSL mode configuration pair by converting `sslmode=verify-ca` or `sslmode=verify-full` to `sslmode=require`, applies token normalization to other sslmode values, and returns non-sslmode pairs unchanged. [crates/gcore/src/postgres.rs:209-222]
- `normalize_sslmode_token` (function) component `normalize_sslmode_token [function]` (`29a467c4-479e-5257-852f-789111055064`) lines 224-229 [crates/gcore/src/postgres.rs:224-229]
  - Signature: `fn normalize_sslmode_token(value: &str) -> String {`
  - Purpose: Strips leading and trailing single and double quotes from the input string and converts the result to lowercase ASCII characters. [crates/gcore/src/postgres.rs:224-229]
- `connect_with_tls_unverified` (function) component `connect_with_tls_unverified [function]` (`6b32b819-1610-5e1d-bb3a-a09b04d4a739`) lines 231-233 [crates/gcore/src/postgres.rs:231-233]
  - Signature: `fn connect_with_tls_unverified(config: &postgres::Config) -> anyhow::Result<Client> {`
  - Purpose: Establishes a PostgreSQL client connection with TLS enabled but server certificate verification disabled by delegating to `connect_with_tls_verification` with verification set to `false`. [crates/gcore/src/postgres.rs:231-233]
- `connect_with_tls_verify_ca` (function) component `connect_with_tls_verify_ca [function]` (`b2941dd7-f238-5daa-ab44-4c796859d748`) lines 235-240 [crates/gcore/src/postgres.rs:235-240]
  - Signature: `fn connect_with_tls_verify_ca(config: &postgres::Config) -> anyhow::Result<Client> {`
  - Purpose: Establishes a PostgreSQL client connection using a verified TLS connector configured from the provided configuration, wrapping connection errors with contextual messaging. [crates/gcore/src/postgres.rs:235-240]
- `connect_with_tls_verification` (function) component `connect_with_tls_verification [function]` (`2a99a1d2-1537-5e80-a626-d80205af022b`) lines 242-254 [crates/gcore/src/postgres.rs:242-254]
  - Signature: `fn connect_with_tls_verification(`
  - Purpose: Establishes a PostgreSQL client connection with conditional TLS certificate verification determined by the `verify` parameter. [crates/gcore/src/postgres.rs:242-254]
- `unverified_tls_connector` (function) component `unverified_tls_connector [function]` (`ca0ac180-e136-5d51-883e-9a35abf15676`) lines 256-261 [crates/gcore/src/postgres.rs:256-261]
  - Signature: `fn unverified_tls_connector() -> anyhow::Result<MakeTlsConnector> {`
  - Purpose: Constructs a PostgreSQL TLS connector with certificate verification disabled, returning it wrapped in a `MakeTlsConnector`. [crates/gcore/src/postgres.rs:256-261]
- `verified_tls_connector` (function) component `verified_tls_connector [function]` (`1a7cee9c-ef05-544c-8fbd-b5ad412a1a72`) lines 263-276 [crates/gcore/src/postgres.rs:263-276]
  - Signature: `fn verified_tls_connector(verify_hostname: bool) -> anyhow::Result<MakeTlsConnector> {`
  - Purpose: Constructs a PostgreSQL TLS connector with mandatory peer certificate verification, optionally disabling hostname verification based on the input parameter. [crates/gcore/src/postgres.rs:263-276]
- `run_schema_validator` (function) component `run_schema_validator [function]` (`a7dbce47-93ff-59ce-90cf-971b3c792ea5`) lines 278-283 [crates/gcore/src/postgres.rs:278-283]
  - Signature: `fn run_schema_validator<C>(`
  - Purpose: This generic function executes a provided validator closure once on a mutable connection reference and returns the resulting `Vec<SchemaCheck>`. [crates/gcore/src/postgres.rs:278-283]
- `attached_validation_is_non_destructive` (function) component `attached_validation_is_non_destructive [function]` (`f1171750-9308-5a33-ae69-0f2a5912158c`) lines 290-308 [crates/gcore/src/postgres.rs:290-308]
  - Signature: `fn attached_validation_is_non_destructive() {`
  - Purpose: Verifies that `run_schema_validator` non-destructively appends validator side effects to the connection state while returning schema validation results. [crates/gcore/src/postgres.rs:290-308]
- `schema_validator_is_domain_supplied` (function) component `schema_validator_is_domain_supplied [function]` (`ac2dcfe2-00a8-537a-a6f0-b176f4ac1371`) lines 311-332 [crates/gcore/src/postgres.rs:311-332]
  - Signature: `fn schema_validator_is_domain_supplied() {`
  - Purpose: Tests that `run_schema_validator` correctly maps the supplied domain objects ("domain_symbols" and "domain_bm25_idx") to schema checks with matching object names and consumer-supplied status. [crates/gcore/src/postgres.rs:311-332]
- `sslmode_parser_selects_tls_modes` (function) component `sslmode_parser_selects_tls_modes [function]` (`5b8b94d9-26a1-5988-8b0f-ef14a9a8edae`) lines 335-345 [crates/gcore/src/postgres.rs:335-345]
  - Signature: `fn sslmode_parser_selects_tls_modes() {`
  - Purpose: This test function verifies that the PostgreSQL connection string parser correctly maps `sslmode` query parameter values to their corresponding `SslMode` enum variants. [crates/gcore/src/postgres.rs:335-345]
- `quoted_verify_sslmodes_normalize_for_postgres_parser` (function) component `quoted_verify_sslmodes_normalize_for_postgres_parser [function]` (`e7d1f069-42a2-53c0-b3ca-bc78a2784d63`) lines 348-379 [crates/gcore/src/postgres.rs:348-379]
  - Signature: `fn quoted_verify_sslmodes_normalize_for_postgres_parser() {`
  - Purpose: This test validates the parsing and normalization of PostgreSQL connection strings with quoted sslmode parameters, verifying that quotes are removed and verify-ca/verify-full modes are normalized to require. [crates/gcore/src/postgres.rs:348-379]

