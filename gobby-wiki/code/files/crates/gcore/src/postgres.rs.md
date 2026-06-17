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
  - 226-231
  - 233-235
  - 237-239
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/postgres.rs:16-22](crates/gcore/src/postgres.rs#L16-L22), [crates/gcore/src/postgres.rs:25-27](crates/gcore/src/postgres.rs#L25-L27), [crates/gcore/src/postgres.rs:36-45](crates/gcore/src/postgres.rs#L36-L45), [crates/gcore/src/postgres.rs:49-58](crates/gcore/src/postgres.rs#L49-L58), [crates/gcore/src/postgres.rs:66-71](crates/gcore/src/postgres.rs#L66-L71), [crates/gcore/src/postgres.rs:73-101](crates/gcore/src/postgres.rs#L73-L101), [crates/gcore/src/postgres.rs:104-110](crates/gcore/src/postgres.rs#L104-L110), [crates/gcore/src/postgres.rs:112-119](crates/gcore/src/postgres.rs#L112-L119), [crates/gcore/src/postgres.rs:121-134](crates/gcore/src/postgres.rs#L121-L134), [crates/gcore/src/postgres.rs:136-150](crates/gcore/src/postgres.rs#L136-L150), [crates/gcore/src/postgres.rs:152-167](crates/gcore/src/postgres.rs#L152-L167), [crates/gcore/src/postgres.rs:169-182](crates/gcore/src/postgres.rs#L169-L182), [crates/gcore/src/postgres.rs:184-189](crates/gcore/src/postgres.rs#L184-L189), [crates/gcore/src/postgres.rs:191-193](crates/gcore/src/postgres.rs#L191-L193), [crates/gcore/src/postgres.rs:195-197](crates/gcore/src/postgres.rs#L195-L197), [crates/gcore/src/postgres.rs:199-209](crates/gcore/src/postgres.rs#L199-L209), [crates/gcore/src/postgres.rs:211-216](crates/gcore/src/postgres.rs#L211-L216), [crates/gcore/src/postgres.rs:219-223](crates/gcore/src/postgres.rs#L219-L223), [crates/gcore/src/postgres.rs:226-231](crates/gcore/src/postgres.rs#L226-L231), [crates/gcore/src/postgres.rs:233-235](crates/gcore/src/postgres.rs#L233-L235), [crates/gcore/src/postgres.rs:237-239](crates/gcore/src/postgres.rs#L237-L239), [crates/gcore/src/postgres.rs:242-247](crates/gcore/src/postgres.rs#L242-L247), [crates/gcore/src/postgres.rs:249-260](crates/gcore/src/postgres.rs#L249-L260), [crates/gcore/src/postgres.rs:262-278](crates/gcore/src/postgres.rs#L262-L278), [crates/gcore/src/postgres.rs:280-285](crates/gcore/src/postgres.rs#L280-L285), [crates/gcore/src/postgres.rs:292-310](crates/gcore/src/postgres.rs#L292-L310), [crates/gcore/src/postgres.rs:313-334](crates/gcore/src/postgres.rs#L313-L334), [crates/gcore/src/postgres.rs:337-347](crates/gcore/src/postgres.rs#L337-L347), [crates/gcore/src/postgres.rs:350-381](crates/gcore/src/postgres.rs#L350-L381), [crates/gcore/src/postgres.rs:384-391](crates/gcore/src/postgres.rs#L384-L391), [crates/gcore/src/postgres.rs:394-402](crates/gcore/src/postgres.rs#L394-L402), [crates/gcore/src/postgres.rs:405-413](crates/gcore/src/postgres.rs#L405-L413)

</details>

# crates/gcore/src/postgres.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Provides the PostgreSQL adapter boundary for Gobby, with helpers for opening hub connections, reading config values, validating externally managed schema objects, and building TLS connectors. `connect_readonly` and `connect_readwrite` wrap the core connection path, `read_config_value` reads raw `config_store` entries without mutating them, `SchemaCheck` and `validate_schema` model and run schema checks, and the `RequestedSslMode`/`TlsConnectorMode`/TLS helper functions translate config-driven SSL settings into `postgres`/OpenSSL connector settings. The test functions exercise the schema-validation behavior, SSL-mode parsing, and TLS connector construction to ensure validation stays non-destructive and verification modes are applied correctly.
[crates/gcore/src/postgres.rs:16-22]
[crates/gcore/src/postgres.rs:25-27]
[crates/gcore/src/postgres.rs:36-45]
[crates/gcore/src/postgres.rs:49-58]
[crates/gcore/src/postgres.rs:66-71]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `connect_readonly` | function | `pub fn connect_readonly(database_url: &str) -> anyhow::Result<Client> {` | `connect_readonly [function]` | `f4444839-818e-5c0b-beef-022c9512dbf7` | 16-22 [crates/gcore/src/postgres.rs:16-22] | Indexed function `connect_readonly` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:16-22] |
| `connect_readwrite` | function | `pub fn connect_readwrite(database_url: &str) -> anyhow::Result<Client> {` | `connect_readwrite [function]` | `2e706e4c-3689-5e20-897f-2ea49a6e83be` | 25-27 [crates/gcore/src/postgres.rs:25-27] | Indexed function `connect_readwrite` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:25-27] |
| `read_config_value` | function | `pub fn read_config_value(conn: &mut Client, key: &str) -> anyhow::Result<Option<String>> {` | `read_config_value [function]` | `586c4d6b-bcec-5b11-8167-8c04a7f2a097` | 36-45 [crates/gcore/src/postgres.rs:36-45] | Indexed function `read_config_value` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:36-45] |
| `SchemaCheck` | class | `pub struct SchemaCheck {` | `SchemaCheck [class]` | `683b647c-1560-5e38-949d-48979b60d5e7` | 49-58 [crates/gcore/src/postgres.rs:49-58] | Indexed class `SchemaCheck` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:49-58] |
| `validate_schema` | function | `pub fn validate_schema(` | `validate_schema [function]` | `b70fcb44-0f5f-5a98-a1b0-50ff49d6a6c2` | 66-71 [crates/gcore/src/postgres.rs:66-71] | Indexed function `validate_schema` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:66-71] |
| `connect` | function | `fn connect(database_url: &str) -> anyhow::Result<Client> {` | `connect [function]` | `430735e1-76cc-50e4-9f33-8b6374ac965a` | 73-101 [crates/gcore/src/postgres.rs:73-101] | Indexed function `connect` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:73-101] |
| `RequestedSslMode` | type | `enum RequestedSslMode {` | `RequestedSslMode [type]` | `14dd5100-7de6-5292-aadf-eeca2d17b0e4` | 104-110 [crates/gcore/src/postgres.rs:104-110] | Indexed type `RequestedSslMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:104-110] |
| `requested_ssl_mode_from_config` | function | `fn requested_ssl_mode_from_config(config: &postgres::Config) -> RequestedSslMode {` | `requested_ssl_mode_from_config [function]` | `c76347f6-5a06-5af8-b7f0-36d94f8afca6` | 112-119 [crates/gcore/src/postgres.rs:112-119] | Indexed function `requested_ssl_mode_from_config` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:112-119] |
| `requested_ssl_mode` | function | `fn requested_ssl_mode(database_url: &str) -> Option<RequestedSslMode> {` | `requested_ssl_mode [function]` | `50724927-249f-5a03-ab6c-cc6500644c3a` | 121-134 [crates/gcore/src/postgres.rs:121-134] | Indexed function `requested_ssl_mode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:121-134] |
| `sslmode_value` | function | `fn sslmode_value(database_url: &str) -> Option<String> {` | `sslmode_value [function]` | `05fbd161-d826-560f-aa35-03f822224722` | 136-150 [crates/gcore/src/postgres.rs:136-150] | Indexed function `sslmode_value` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:136-150] |
| `normalize_sslmode_for_parser` | function | `fn normalize_sslmode_for_parser(database_url: &str) -> String {` | `normalize_sslmode_for_parser [function]` | `a19b38b6-426a-5ea6-8cf3-cfa3cce073b8` | 152-167 [crates/gcore/src/postgres.rs:152-167] | Indexed function `normalize_sslmode_for_parser` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:152-167] |
| `normalize_sslmode_pair` | function | `fn normalize_sslmode_pair(pair: &str) -> String {` | `normalize_sslmode_pair [function]` | `00cbc729-855d-5862-882b-0eb46c04e2fb` | 169-182 [crates/gcore/src/postgres.rs:169-182] | Indexed function `normalize_sslmode_pair` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:169-182] |
| `normalize_sslmode_token` | function | `fn normalize_sslmode_token(value: &str) -> String {` | `normalize_sslmode_token [function]` | `60722538-2324-5c6e-ac3a-7e80a0c05e72` | 184-189 [crates/gcore/src/postgres.rs:184-189] | Indexed function `normalize_sslmode_token` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:184-189] |
| `connect_with_tls_unverified` | function | `fn connect_with_tls_unverified(config: &postgres::Config) -> anyhow::Result<Client> {` | `connect_with_tls_unverified [function]` | `6b39d83c-06d5-5b12-8356-5f1f9b4ba984` | 191-193 [crates/gcore/src/postgres.rs:191-193] | Indexed function `connect_with_tls_unverified` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:191-193] |
| `connect_with_tls_verify_ca` | function | `fn connect_with_tls_verify_ca(config: &postgres::Config) -> anyhow::Result<Client> {` | `connect_with_tls_verify_ca [function]` | `e482cc23-b738-5542-8a7c-ad624745e4e9` | 195-197 [crates/gcore/src/postgres.rs:195-197] | Indexed function `connect_with_tls_verify_ca` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:195-197] |
| `connect_with_tls_verification` | function | `fn connect_with_tls_verification(` | `connect_with_tls_verification [function]` | `dc78e9bb-bf75-5a1d-8203-5a87a3821b00` | 199-209 [crates/gcore/src/postgres.rs:199-209] | Indexed function `connect_with_tls_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:199-209] |
| `connect_with_tls` | function | `fn connect_with_tls(config: &postgres::Config, mode: TlsConnectorMode) -> anyhow::Result<Client> {` | `connect_with_tls [function]` | `2d7a72ba-1185-54d9-915d-bdba018f903f` | 211-216 [crates/gcore/src/postgres.rs:211-216] | Indexed function `connect_with_tls` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:211-216] |
| `TlsConnectorMode` | type | `enum TlsConnectorMode {` | `TlsConnectorMode [type]` | `91dd195a-47a6-54d4-a099-3060e15d1b01` | 219-223 [crates/gcore/src/postgres.rs:219-223] | Indexed type `TlsConnectorMode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:219-223] |
| `TlsConnectorMode::verify_mode` | method | `fn verify_mode(self) -> SslVerifyMode {` | `TlsConnectorMode::verify_mode [method]` | `c60078dd-8934-563c-b320-1d7bc970b981` | 226-231 [crates/gcore/src/postgres.rs:226-231] | Indexed method `TlsConnectorMode::verify_mode` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:226-231] |
| `TlsConnectorMode::uses_default_verify_paths` | method | `fn uses_default_verify_paths(self) -> bool {` | `TlsConnectorMode::uses_default_verify_paths [method]` | `536c462c-7a6c-5015-80c1-7f5d62ec4065` | 233-235 [crates/gcore/src/postgres.rs:233-235] | Indexed method `TlsConnectorMode::uses_default_verify_paths` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:233-235] |
| `TlsConnectorMode::disables_hostname_verification` | method | `fn disables_hostname_verification(self) -> bool {` | `TlsConnectorMode::disables_hostname_verification [method]` | `74047f41-7a4f-5368-a889-9c50a3f6f4d6` | 237-239 [crates/gcore/src/postgres.rs:237-239] | Indexed method `TlsConnectorMode::disables_hostname_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:237-239] |
| `TlsConnectorBuilder` | class | `struct TlsConnectorBuilder {` | `TlsConnectorBuilder [class]` | `a6f3f2ae-7d4d-564f-8b70-00c5b95336c7` | 242-247 [crates/gcore/src/postgres.rs:242-247] | Indexed class `TlsConnectorBuilder` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:242-247] |
| `tls_connector` | function | `fn tls_connector(mode: TlsConnectorMode) -> anyhow::Result<MakeTlsConnector> {` | `tls_connector [function]` | `24d98d32-a558-5a78-958e-f80a981a7a0a` | 249-260 [crates/gcore/src/postgres.rs:249-260] | Indexed function `tls_connector` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:249-260] |
| `tls_connector_builder` | function | `fn tls_connector_builder(mode: TlsConnectorMode) -> anyhow::Result<TlsConnectorBuilder> {` | `tls_connector_builder [function]` | `e9056a8b-a2e7-5f31-9947-177252a6aa16` | 262-278 [crates/gcore/src/postgres.rs:262-278] | Indexed function `tls_connector_builder` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:262-278] |
| `run_schema_validator` | function | `fn run_schema_validator<C>(` | `run_schema_validator [function]` | `2114f89b-0f4f-50de-a6fb-c12ff92b3522` | 280-285 [crates/gcore/src/postgres.rs:280-285] | Indexed function `run_schema_validator` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:280-285] |
| `attached_validation_is_non_destructive` | function | `fn attached_validation_is_non_destructive() {` | `attached_validation_is_non_destructive [function]` | `a0101ac9-c087-5188-a4dd-9520d70f81c4` | 292-310 [crates/gcore/src/postgres.rs:292-310] | Indexed function `attached_validation_is_non_destructive` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:292-310] |
| `schema_validator_is_domain_supplied` | function | `fn schema_validator_is_domain_supplied() {` | `schema_validator_is_domain_supplied [function]` | `9973ea29-fcaf-53e7-9636-7b2a8ff42cae` | 313-334 [crates/gcore/src/postgres.rs:313-334] | Indexed function `schema_validator_is_domain_supplied` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:313-334] |
| `sslmode_parser_selects_tls_modes` | function | `fn sslmode_parser_selects_tls_modes() {` | `sslmode_parser_selects_tls_modes [function]` | `de0e8b90-1c62-54f9-a294-b8fa7fb5d4b9` | 337-347 [crates/gcore/src/postgres.rs:337-347] | Indexed function `sslmode_parser_selects_tls_modes` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:337-347] |
| `quoted_verify_sslmodes_normalize_for_postgres_parser` | function | `fn quoted_verify_sslmodes_normalize_for_postgres_parser() {` | `quoted_verify_sslmodes_normalize_for_postgres_parser [function]` | `21c1fd46-c1e5-5055-9930-2e6e0f37b10c` | 350-381 [crates/gcore/src/postgres.rs:350-381] | Indexed function `quoted_verify_sslmodes_normalize_for_postgres_parser` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:350-381] |
| `tls_connector_construction_unverified_disables_peer_verification` | function | `fn tls_connector_construction_unverified_disables_peer_verification() -> anyhow::Result<()> {` | `tls_connector_construction_unverified_disables_peer_verification [function]` | `7e15a212-70e7-595a-8be9-2bfbcb15b436` | 384-391 [crates/gcore/src/postgres.rs:384-391] | Indexed function `tls_connector_construction_unverified_disables_peer_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:384-391] |
| `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname` | function | `fn tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname()` | `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname [function]` | `108599d3-d343-56f4-8e4e-43da727d4e7e` | 394-402 [crates/gcore/src/postgres.rs:394-402] | Indexed function `tls_connector_construction_verify_ca_keeps_peer_verification_without_hostname` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:394-402] |
| `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification` | function | `fn tls_connector_construction_verify_full_keeps_peer_and_hostname_verification()` | `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification [function]` | `f8bbb66d-bddc-5792-a149-6ce0e370fc79` | 405-413 [crates/gcore/src/postgres.rs:405-413] | Indexed function `tls_connector_construction_verify_full_keeps_peer_and_hostname_verification` in `crates/gcore/src/postgres.rs`. [crates/gcore/src/postgres.rs:405-413] |
