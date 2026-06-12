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
  - 169-182
  - 184-189
  - 191-193
  - 195-197
  - 199-209
  - 211-216
  - 219-223
  - 225-240
  - 242-247
  - 249-260
  - 262-278
  - 280-285
  - 292-310
  - 313-334
  - 337-347
  - 350-381
  - 384-391
  - 394-402
  - 405-413
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/postgres.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/postgres.rs` exposes 33 indexed API symbols.
[crates/gcore/src/postgres.rs:16-22]
[crates/gcore/src/postgres.rs:25-27]
[crates/gcore/src/postgres.rs:36-45]
[crates/gcore/src/postgres.rs:49-58]
[crates/gcore/src/postgres.rs:66-71]

## API Symbols

- `connect_readonly` (function) component `connect_readonly [function]` (`f4444839-818e-5c0b-beef-022c9512dbf7`) lines 16-22 [crates/gcore/src/postgres.rs:16-22]
  - Signature: `pub fn connect_readonly(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: Establishes a PostgreSQL `Client` via `connect`, then executes `SET default_transaction_read_only = on` to force the session into read-only mode before returning the client, with any failure wrapped in context. [crates/gcore/src/postgres.rs:16-22]
- `connect_readwrite` (function) component `connect_readwrite [function]` (`2e706e4c-3689-5e20-897f-2ea49a6e83be`) lines 25-27 [crates/gcore/src/postgres.rs:25-27]
  - Signature: `pub fn connect_readwrite(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: `connect_readwrite` is a thin wrapper that calls `connect(database_url)` and returns its `anyhow::Result<Client>` unchanged. [crates/gcore/src/postgres.rs:25-27]
- `read_config_value` (function) component `read_config_value [function]` (`586c4d6b-bcec-5b11-8167-8c04a7f2a097`) lines 36-45 [crates/gcore/src/postgres.rs:36-45]
  - Signature: `pub fn read_config_value(conn: &mut Client, key: &str) -> anyhow::Result<Option<String>> {`
  - Purpose: Reads `config_store.value` for the given key via `query_opt`, returning `Ok(Some(text))` if the row exists and the `value` column is text, `Ok(None)` if no row matches, and an `anyhow`-contextualized error if the query fails or the value is not text. [crates/gcore/src/postgres.rs:36-45]
- `SchemaCheck` (class) component `SchemaCheck [class]` (`683b647c-1560-5e38-949d-48979b60d5e7`) lines 49-58 [crates/gcore/src/postgres.rs:49-58]
  - Signature: `pub struct SchemaCheck {`
  - Purpose: `SchemaCheck` is a schema-validation result struct that records the target object name, the kind of check performed, whether it passed, and an optional failure detail. [crates/gcore/src/postgres.rs:49-58]
- `validate_schema` (function) component `validate_schema [function]` (`b70fcb44-0f5f-5a98-a1b0-50ff49d6a6c2`) lines 66-71 [crates/gcore/src/postgres.rs:66-71]
  - Signature: `pub fn validate_schema(`
  - Purpose: Forwards the mutable `Client` and one-shot validator closure to `run_schema_validator`, returning the resulting `Vec<SchemaCheck>`. [crates/gcore/src/postgres.rs:66-71]
- `connect` (function) component `connect [function]` (`430735e1-76cc-50e4-9f33-8b6374ac965a`) lines 73-101 [crates/gcore/src/postgres.rs:73-101]
  - Signature: `fn connect(database_url: &str) -> anyhow::Result<Client> {`
  - Purpose: Parses the PostgreSQL connection URL after normalizing `sslmode`, resolves the effective SSL policy from the URL or config, and then establishes a `postgres::Client` using the corresponding TLS or `NoTls` connection path with contextualized error handling and a `prefer` fallback to plaintext on TLS failure. [crates/gcore/src/postgres.rs:73-101]
- `RequestedSslMode` (type) component `RequestedSslMode [type]` (`14dd5100-7de6-5292-aadf-eeca2d17b0e4`) lines 104-110 [crates/gcore/src/postgres.rs:104-110]
  - Signature: `enum RequestedSslMode {`
  - Purpose: Indexed type `RequestedSslMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:104-110]
- `requested_ssl_mode_from_config` (function) component `requested_ssl_mode_from_config [function]` (`c76347f6-5a06-5af8-b7f0-36d94f8afca6`) lines 112-119 [crates/gcore/src/postgres.rs:112-119]
  - Signature: `fn requested_ssl_mode_from_config(config: &postgres::Config) -> RequestedSslMode {`
  - Purpose: It converts `config.get_ssl_mode()` from `postgres::Config` into the matching `RequestedSslMode` variant, passing through `Disable`, `Prefer`, and `Require` unchanged and mapping any unhandled mode to `RequestedSslMode::Prefer`. [crates/gcore/src/postgres.rs:112-119]
- `requested_ssl_mode` (function) component `requested_ssl_mode [function]` (`50724927-249f-5a03-ab6c-cc6500644c3a`) lines 121-134 [crates/gcore/src/postgres.rs:121-134]
  - Signature: `fn requested_ssl_mode(database_url: &str) -> Option<RequestedSslMode> {`
  - Purpose: Parses the `sslmode` parameter from a PostgreSQL connection URL and maps recognized values (`disable`, `prefer`, `require`, `verify-ca`, `verify-full`) to the corresponding `RequestedSslMode`, returning `None` and logging a debug message when the parameter is missing or unrecognized so the parser default is used. [crates/gcore/src/postgres.rs:121-134]
- `sslmode_value` (function) component `sslmode_value [function]` (`05fbd161-d826-560f-aa35-03f822224722`) lines 136-150 [crates/gcore/src/postgres.rs:136-150]
  - Signature: `fn sslmode_value(database_url: &str) -> Option<String> {`
  - Purpose: Returns the normalized `sslmode` value from `database_url` by first searching the URL query string for `sslmode=...`, then falling back to keyword-DSN tokens from `crate::libpq::split_keyword_dsn_tokens`, and returns `None` if no such token is present. [crates/gcore/src/postgres.rs:136-150]
- `normalize_sslmode_for_parser` (function) component `normalize_sslmode_for_parser [function]` (`a19b38b6-426a-5ea6-8cf3-cfa3cce073b8`) lines 152-167 [crates/gcore/src/postgres.rs:152-167]
  - Signature: `fn normalize_sslmode_for_parser(database_url: &str) -> String {`
  - Purpose: It rewrites a database URL or libpq-style DSN by applying `normalize_sslmode_pair` to each `&`-separated query parameter when a `?` is present, otherwise to each whitespace-delimited keyword token, then reconstructs the string with the original delimiter format. [crates/gcore/src/postgres.rs:152-167]
- `normalize_sslmode_pair` (function) component `normalize_sslmode_pair [function]` (`00cbc729-855d-5862-882b-0eb46c04e2fb`) lines 169-182 [crates/gcore/src/postgres.rs:169-182]
  - Signature: `fn normalize_sslmode_pair(pair: &str) -> String {`
  - Purpose: Returns the input unchanged unless it is a `sslmode=<value>` pair, in which case it normalizes the value with `normalize_sslmode_token` and rewrites `verify-ca` or `verify-full` to `sslmode=require`. [crates/gcore/src/postgres.rs:169-182]
- `normalize_sslmode_token` (function) component `normalize_sslmode_token [function]` (`60722538-2324-5c6e-ac3a-7e80a0c05e72`) lines 184-189 [crates/gcore/src/postgres.rs:184-189]
  - Signature: `fn normalize_sslmode_token(value: &str) -> String {`
  - Purpose: It trims leading and trailing single or double quote characters from the input, then returns the remaining text converted to ASCII lowercase. [crates/gcore/src/postgres.rs:184-189]
- `connect_with_tls_unverified` (function) component `connect_with_tls_unverified [function]` (`6b39d83c-06d5-5b12-8356-5f1f9b4ba984`) lines 191-193 [crates/gcore/src/postgres.rs:191-193]
  - Signature: `fn connect_with_tls_unverified(config: &postgres::Config) -> anyhow::Result<Client> {`
  - Purpose: It delegates to `connect_with_tls` with `TlsConnectorMode::Unverified` to create a PostgreSQL `Client` from the given `postgres::Config`, propagating any failure as `anyhow::Result<Client>`. [crates/gcore/src/postgres.rs:191-193]
- `connect_with_tls_verify_ca` (function) component `connect_with_tls_verify_ca [function]` (`e482cc23-b738-5542-8a7c-ad624745e4e9`) lines 195-197 [crates/gcore/src/postgres.rs:195-197]
  - Signature: `fn connect_with_tls_verify_ca(config: &postgres::Config) -> anyhow::Result<Client> {`
  - Purpose: Creates a PostgreSQL `Client` by delegating to `connect_with_tls` with the TLS connector configured in `VerifyCa` mode, returning any connection error as `anyhow::Result<Client>`. [crates/gcore/src/postgres.rs:195-197]
- `connect_with_tls_verification` (function) component `connect_with_tls_verification [function]` (`dc78e9bb-bf75-5a1d-8203-5a87a3821b00`) lines 199-209 [crates/gcore/src/postgres.rs:199-209]
  - Signature: `fn connect_with_tls_verification(`
  - Purpose: Creates a PostgreSQL client by choosing `TlsConnectorMode::VerifyFull` when `verify` is `true` or `TlsConnectorMode::Unverified` otherwise, then delegating to `connect_with_tls(config, mode)`. [crates/gcore/src/postgres.rs:199-209]
- `connect_with_tls` (function) component `connect_with_tls [function]` (`2d7a72ba-1185-54d9-915d-bdba018f903f`) lines 211-216 [crates/gcore/src/postgres.rs:211-216]
  - Signature: `fn connect_with_tls(config: &postgres::Config, mode: TlsConnectorMode) -> anyhow::Result<Client> {`
  - Purpose: Creates a TLS connector from `mode`, uses it to connect the given PostgreSQL `Config` into a `Client`, and wraps any connection error with the context `failed to connect to the Gobby PostgreSQL hub`. [crates/gcore/src/postgres.rs:211-216]
- `TlsConnectorMode` (type) component `TlsConnectorMode [type]` (`91dd195a-47a6-54d4-a099-3060e15d1b01`) lines 219-223 [crates/gcore/src/postgres.rs:219-223]
  - Signature: `enum TlsConnectorMode {`
  - Purpose: Indexed type `TlsConnectorMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:219-223]
- `TlsConnectorMode` (class) component `TlsConnectorMode [class]` (`019bd66d-3126-54f9-9d64-182c4e4d3e6d`) lines 225-240 [crates/gcore/src/postgres.rs:225-240]
  - Signature: `impl TlsConnectorMode {`
  - Purpose: `TlsConnectorMode` encodes the TLS validation policy, mapping `Unverified` to `SslVerifyMode::NONE` and `VerifyCa`/`VerifyFull` to `SslVerifyMode::PEER`, while also distinguishing whether default CA paths are used and whether hostname verification is disabled. [crates/gcore/src/postgres.rs:225-240]
- `TlsConnectorMode.verify_mode` (method) component `TlsConnectorMode.verify_mode [method]` (`c60078dd-8934-563c-b320-1d7bc970b981`) lines 226-231 [crates/gcore/src/postgres.rs:226-231]
  - Signature: `fn verify_mode(self) -> SslVerifyMode {`
  - Purpose: `verify_mode` converts the enum into an OpenSSL `SslVerifyMode`, returning `NONE` for `Unverified` and `PEER` for both `VerifyCa` and `VerifyFull`. [crates/gcore/src/postgres.rs:226-231]
- `TlsConnectorMode.uses_default_verify_paths` (method) component `TlsConnectorMode.uses_default_verify_paths [method]` (`536c462c-7a6c-5015-80c1-7f5d62ec4065`) lines 233-235 [crates/gcore/src/postgres.rs:233-235]
  - Signature: `fn uses_default_verify_paths(self) -> bool {`
  - Purpose: Returns `true` only when `self` is `VerifyCa` or `VerifyFull`, and `false` for all other variants. [crates/gcore/src/postgres.rs:233-235]
- `TlsConnectorMode.disables_hostname_verification` (method) component `TlsConnectorMode.disables_hostname_verification [method]` (`74047f41-7a4f-5368-a889-9c50a3f6f4d6`) lines 237-239 [crates/gcore/src/postgres.rs:237-239]
  - Signature: `fn disables_hostname_verification(self) -> bool {`
  - Purpose: Returns `true` only when `self` is `Self::VerifyCa`, meaning hostname verification is disabled in that TLS verification mode. [crates/gcore/src/postgres.rs:237-239]
- `TlsConnectorBuilder` (class) component `TlsConnectorBuilder [class]` (`a6f3f2ae-7d4d-564f-8b70-00c5b95336c7`) lines 242-247 [crates/gcore/src/postgres.rs:242-247]
  - Signature: `struct TlsConnectorBuilder {`
  - Purpose: `TlsConnectorBuilder` is a wrapper around an `SslConnectorBuilder` that also tracks a test-only `SslVerifyMode` and a `disables_hostname_verification` flag for configuring TLS certificate and hostname verification behavior. [crates/gcore/src/postgres.rs:242-247]
- `tls_connector` (function) component `tls_connector [function]` (`24d98d32-a558-5a78-958e-f80a981a7a0a`) lines 249-260 [crates/gcore/src/postgres.rs:249-260]
  - Signature: `fn tls_connector(mode: TlsConnectorMode) -> anyhow::Result<MakeTlsConnector> {`
  - Purpose: Builds a `MakeTlsConnector` from the `TlsConnectorMode`-specific builder and, if hostname verification is disabled, installs a callback that turns off `verify_hostname` on each TLS config before returning the connector. [crates/gcore/src/postgres.rs:249-260]
- `tls_connector_builder` (function) component `tls_connector_builder [function]` (`e9056a8b-a2e7-5f31-9947-177252a6aa16`) lines 262-278 [crates/gcore/src/postgres.rs:262-278]
  - Signature: `fn tls_connector_builder(mode: TlsConnectorMode) -> anyhow::Result<TlsConnectorBuilder> {`
  - Purpose: Indexed function `tls_connector_builder` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:262-278]
- `run_schema_validator` (function) component `run_schema_validator [function]` (`2114f89b-0f4f-50de-a6fb-c12ff92b3522`) lines 280-285 [crates/gcore/src/postgres.rs:280-285]
  - Signature: `fn run_schema_validator<C>(`
  - Purpose: Indexed function `run_schema_validator` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:280-285]
- `attached_validation_is_non_destructive` (function) component `attached_validation_is_non_destructive [function]` (`a0101ac9-c087-5188-a4dd-9520d70f81c4`) lines 292-310 [crates/gcore/src/postgres.rs:292-310]
  - Signature: `fn attached_validation_is_non_destructive() {`
  - Purpose: Indexed function `attached_validation_is_non_destructive` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:292-310]
- `schema_validator_is_domain_supplied` (function) component `schema_validator_is_domain_supplied [function]` (`9973ea29-fcaf-53e7-9636-7b2a8ff42cae`) lines 313-334 [crates/gcore/src/postgres.rs:313-334]
  - Signature: `fn schema_validator_is_domain_supplied() {`
  - Purpose: Indexed function `schema_validator_is_domain_supplied` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:313-334]
- `sslmode_parser_selects_tls_modes` (function) component `sslmode_parser_selects_tls_modes [function]` (`de0e8b90-1c62-54f9-a294-b8fa7fb5d4b9`) lines 337-347 [crates/gcore/src/postgres.rs:337-347]
  - Signature: `fn sslmode_parser_selects_tls_modes() {`
  - Purpose: Indexed function `sslmode_parser_selects_tls_modes` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:337-347]
- `quoted_verify_sslmodes_normalize_for_postgres_parser` (function) component `quoted_verify_sslmodes_normalize_for_postgres_parser [function]` (`21c1fd46-c1e5-5055-9930-2e6e0f37b10c`) lines 350-381 [crates/gcore/src/postgres.rs:350-381]
  - Signature: `fn quoted_verify_sslmodes_normalize_for_postgres_parser() {`
  - Purpose: Indexed function `quoted_verify_sslmodes_normalize_for_postgres_parser` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:350-381]
- `tls_connector_construction_unverified_disables_peer_verification` (function) component `tls_connector_construction_unverified_disables_peer_verification [function]` (`7e15a212-70e7-595a-8be9-2bfbcb15b436`) lines 384-391 [crates/gcore/src/postgres.rs:384-391]
  - Signature: `fn tls_connector_construction_unverified_disables_peer_verification() -> anyhow::Result<()> {`
  - Purpose: Indexed function `tls_connector_construction_unverified_disables_peer_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:384-391]
- `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname` (function) component `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname [function]` (`108599d3-d343-56f4-8e4e-43da727d4e7e`) lines 394-402 [crates/gcore/src/postgres.rs:394-402]
  - Signature: `fn tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname()`
  - Purpose: Indexed function `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:394-402]
- `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification` (function) component `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification [function]` (`f8bbb66d-bddc-5792-a149-6ce0e370fc79`) lines 405-413 [crates/gcore/src/postgres.rs:405-413]
  - Signature: `fn tls_connector_construction_verify_full_keeps_peer_and_hostname_verification()`
  - Purpose: Indexed function `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:405-413]

