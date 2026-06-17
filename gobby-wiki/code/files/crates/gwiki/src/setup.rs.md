---
title: crates/gwiki/src/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/setup.rs
  ranges:
  - 29-35
  - 38-46
  - 50-54
  - 57-61
  - 64-66
  - 69-73
  - 76-78
  - 80-101
  - 103-192
  - 194-228
  - 230-236
  - 240-242
  - 244-250
  - 252-266
  - 269-271
  - 273-279
  - 281-287
  - 289-295
  - 297-305
  - 307-329
  - 331-355
  - 363-454
  - 457-480
  - 483-488
  - 491-496
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/setup.rs:29-35](crates/gwiki/src/setup.rs#L29-L35), [crates/gwiki/src/setup.rs:38-46](crates/gwiki/src/setup.rs#L38-L46), [crates/gwiki/src/setup.rs:50-54](crates/gwiki/src/setup.rs#L50-L54), [crates/gwiki/src/setup.rs:57-61](crates/gwiki/src/setup.rs#L57-L61), [crates/gwiki/src/setup.rs:64-66](crates/gwiki/src/setup.rs#L64-L66), [crates/gwiki/src/setup.rs:69-73](crates/gwiki/src/setup.rs#L69-L73), [crates/gwiki/src/setup.rs:76-78](crates/gwiki/src/setup.rs#L76-L78), [crates/gwiki/src/setup.rs:80-101](crates/gwiki/src/setup.rs#L80-L101), [crates/gwiki/src/setup.rs:103-192](crates/gwiki/src/setup.rs#L103-L192), [crates/gwiki/src/setup.rs:194-228](crates/gwiki/src/setup.rs#L194-L228), [crates/gwiki/src/setup.rs:230-236](crates/gwiki/src/setup.rs#L230-L236), [crates/gwiki/src/setup.rs:240-242](crates/gwiki/src/setup.rs#L240-L242), [crates/gwiki/src/setup.rs:244-250](crates/gwiki/src/setup.rs#L244-L250), [crates/gwiki/src/setup.rs:252-266](crates/gwiki/src/setup.rs#L252-L266), [crates/gwiki/src/setup.rs:269-271](crates/gwiki/src/setup.rs#L269-L271), [crates/gwiki/src/setup.rs:273-279](crates/gwiki/src/setup.rs#L273-L279), [crates/gwiki/src/setup.rs:281-287](crates/gwiki/src/setup.rs#L281-L287), [crates/gwiki/src/setup.rs:289-295](crates/gwiki/src/setup.rs#L289-L295), [crates/gwiki/src/setup.rs:297-305](crates/gwiki/src/setup.rs#L297-L305), [crates/gwiki/src/setup.rs:307-329](crates/gwiki/src/setup.rs#L307-L329), [crates/gwiki/src/setup.rs:331-355](crates/gwiki/src/setup.rs#L331-L355), [crates/gwiki/src/setup.rs:363-454](crates/gwiki/src/setup.rs#L363-L454), [crates/gwiki/src/setup.rs:457-480](crates/gwiki/src/setup.rs#L457-L480), [crates/gwiki/src/setup.rs:483-488](crates/gwiki/src/setup.rs#L483-L488), [crates/gwiki/src/setup.rs:491-496](crates/gwiki/src/setup.rs#L491-L496)

</details>

# crates/gwiki/src/setup.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the `gwiki` standalone setup for Postgres: it names the namespace/schema, lists the owned tables and indexes, and models setup outputs as `GwikiPostgresObject` entries with a kind and SQL payload. `GwikiStandaloneSetup` ties the pieces together by building the preflight/table/index DDL, qualifying relation names, tracking owned objects, and exposing a `create` flow, while helper functions handle object construction, DDL execution, identifier quoting, and tests that verify ownership, published object lists, and Postgres identifier length limits.
[crates/gwiki/src/setup.rs:29-35]
[crates/gwiki/src/setup.rs:38-46]
[crates/gwiki/src/setup.rs:50-54]
[crates/gwiki/src/setup.rs:57-61]
[crates/gwiki/src/setup.rs:64-66]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GwikiTable` | type | `pub enum GwikiTable {` | `GwikiTable [type]` | `d41184ea-cd32-5b42-bd2d-27d8eb26657a` | 29-35 [crates/gwiki/src/setup.rs:29-35] | Indexed type `GwikiTable` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:29-35] |
| `GwikiTable::name` | method | `pub fn name(self) -> &'static str {` | `GwikiTable::name [method]` | `72a4da07-e7d7-5a4e-9370-8717ff764914` | 38-46 [crates/gwiki/src/setup.rs:38-46] | Indexed method `GwikiTable::name` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:38-46] |
| `GwikiPostgresObjectKind` | type | `pub enum GwikiPostgresObjectKind {` | `GwikiPostgresObjectKind [type]` | `02830482-9e01-5fc3-a646-11c401da77a9` | 50-54 [crates/gwiki/src/setup.rs:50-54] | Indexed type `GwikiPostgresObjectKind` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:50-54] |
| `GwikiPostgresObject` | class | `pub struct GwikiPostgresObject {` | `GwikiPostgresObject [class]` | `8659bf2b-0856-556e-8b3f-9bad85a4df58` | 57-61 [crates/gwiki/src/setup.rs:57-61] | Indexed class `GwikiPostgresObject` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:57-61] |
| `GwikiStandaloneSetup` | class | `pub struct GwikiStandaloneSetup {` | `GwikiStandaloneSetup [class]` | `3ad73acc-2309-5e6e-a091-2a8a358795eb` | 64-66 [crates/gwiki/src/setup.rs:64-66] | Indexed class `GwikiStandaloneSetup` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:64-66] |
| `GwikiStandaloneSetup::new` | method | `pub fn new() -> Self {` | `GwikiStandaloneSetup::new [method]` | `b992f2e9-5c60-5ca7-bb54-52df6ab1c390` | 69-73 [crates/gwiki/src/setup.rs:69-73] | Indexed method `GwikiStandaloneSetup::new` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:69-73] |
| `GwikiStandaloneSetup::schema` | method | `pub fn schema(&self) -> &str {` | `GwikiStandaloneSetup::schema [method]` | `2c86de7e-e28e-59a6-9720-6ba8f1393cca` | 76-78 [crates/gwiki/src/setup.rs:76-78] | Indexed method `GwikiStandaloneSetup::schema` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:76-78] |
| `GwikiStandaloneSetup::postgres_objects` | method | `pub fn postgres_objects(&self) -> Result<Vec<GwikiPostgresObject>, SetupError> {` | `GwikiStandaloneSetup::postgres_objects [method]` | `3847722d-09ed-5f22-8fe7-ed21bba70c04` | 80-101 [crates/gwiki/src/setup.rs:80-101] | Indexed method `GwikiStandaloneSetup::postgres_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:80-101] |
| `GwikiStandaloneSetup::table_sql` | method | `fn table_sql(&self, table: GwikiTable) -> Result<String, SetupError> {` | `GwikiStandaloneSetup::table_sql [method]` | `1b835d4c-0d62-5436-97ff-d8951c7756b8` | 103-192 [crates/gwiki/src/setup.rs:103-192] | Indexed method `GwikiStandaloneSetup::table_sql` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:103-192] |
| `GwikiStandaloneSetup::index_sql` | method | `fn index_sql(&self, index_name: &str) -> Result<String, SetupError> {` | `GwikiStandaloneSetup::index_sql [method]` | `46a60cce-48b0-5a0e-b444-b7abd61a6511` | 194-228 [crates/gwiki/src/setup.rs:194-228] | Indexed method `GwikiStandaloneSetup::index_sql` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:194-228] |
| `GwikiStandaloneSetup::qualified_relation_name` | method | `fn qualified_relation_name(&self, relation: &str, label: &str) -> Result<String, SetupError> {` | `GwikiStandaloneSetup::qualified_relation_name [method]` | `18510e65-ff02-5d42-80fc-bc6c2ffd98d1` | 230-236 [crates/gwiki/src/setup.rs:230-236] | Indexed method `GwikiStandaloneSetup::qualified_relation_name` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:230-236] |
| `GwikiStandaloneSetup::namespace` | method | `fn namespace(&self) -> &str {` | `GwikiStandaloneSetup::namespace [method]` | `a02e08f8-cea0-5add-9830-3931fa54fb63` | 240-242 [crates/gwiki/src/setup.rs:240-242] | Indexed method `GwikiStandaloneSetup::namespace` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:240-242] |
| `GwikiStandaloneSetup::owned_objects` | method | `fn owned_objects(&self) -> Result<Vec<OwnedObject>, SetupError> {` | `GwikiStandaloneSetup::owned_objects [method]` | `e8251a09-ede7-5f57-9e4a-03e37f222408` | 244-250 [crates/gwiki/src/setup.rs:244-250] | Indexed method `GwikiStandaloneSetup::owned_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:244-250] |
| `GwikiStandaloneSetup::create` | method | `fn create(&self, ctx: &mut SetupContext<'_>) -> Result<SetupReport, SetupError> {` | `GwikiStandaloneSetup::create [method]` | `23763266-dd63-5042-bbc7-c4a5fd2c73ed` | 252-266 [crates/gwiki/src/setup.rs:252-266] | Indexed method `GwikiStandaloneSetup::create` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:252-266] |
| `default_setup` | function | `pub fn default_setup() -> GwikiStandaloneSetup {` | `default_setup [function]` | `d9c37a09-ff86-58bf-9330-d0e9e2209660` | 269-271 [crates/gwiki/src/setup.rs:269-271] | Indexed function `default_setup` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:269-271] |
| `table` | function | `fn table(name: &'static str, sql: String) -> GwikiPostgresObject {` | `table [function]` | `a39fbe96-f60e-59e1-bd60-744dcf914621` | 273-279 [crates/gwiki/src/setup.rs:273-279] | Indexed function `table` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:273-279] |
| `index` | function | `fn index(name: &'static str, sql: String) -> GwikiPostgresObject {` | `index [function]` | `f722cdb6-98e6-513c-aa73-35c6a0bbe99e` | 281-287 [crates/gwiki/src/setup.rs:281-287] | Indexed function `index` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:281-287] |
| `preflight` | function | `fn preflight(name: &'static str, sql: String) -> GwikiPostgresObject {` | `preflight [function]` | `a84e5d95-286e-5ed2-81f1-6b109cde678b` | 289-295 [crates/gwiki/src/setup.rs:289-295] | Indexed function `preflight` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:289-295] |
| `owned_object` | function | `fn owned_object(object: GwikiPostgresObject) -> OwnedObject {` | `owned_object [function]` | `646ea3d9-6317-53ba-a7a2-402065fcd6ff` | 297-305 [crates/gwiki/src/setup.rs:297-305] | Indexed function `owned_object` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:297-305] |
| `execute_postgres_ddl` | function | `fn execute_postgres_ddl(` | `execute_postgres_ddl [function]` | `2100c1c4-b9cc-5913-a350-b01c995b1730` | 307-329 [crates/gwiki/src/setup.rs:307-329] | Indexed function `execute_postgres_ddl` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:307-329] |
| `quote_identifier` | function | `fn quote_identifier(value: &str, label: &str) -> Result<String, SetupError> {` | `quote_identifier [function]` | `82344abb-c3a9-5f3e-ba2a-5af8643896a2` | 331-355 [crates/gwiki/src/setup.rs:331-355] | Indexed function `quote_identifier` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:331-355] |
| `setup_creates_only_gwiki_owned_objects` | function | `fn setup_creates_only_gwiki_owned_objects() {` | `setup_creates_only_gwiki_owned_objects [function]` | `c7319056-b5b1-50e4-83d6-cf43507155e0` | 363-454 [crates/gwiki/src/setup.rs:363-454] | Indexed function `setup_creates_only_gwiki_owned_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:363-454] |
| `published_lists_match_generated_objects` | function | `fn published_lists_match_generated_objects() {` | `published_lists_match_generated_objects [function]` | `3bf2176d-60c2-5a29-b92b-8004812c4e9d` | 457-480 [crates/gwiki/src/setup.rs:457-480] | Indexed function `published_lists_match_generated_objects` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:457-480] |
| `quote_identifier_rejects_names_over_postgres_byte_limit` | function | `fn quote_identifier_rejects_names_over_postgres_byte_limit() {` | `quote_identifier_rejects_names_over_postgres_byte_limit [function]` | `d89634df-9b72-5370-87c9-1f24ef9a975e` | 483-488 [crates/gwiki/src/setup.rs:483-488] | Indexed function `quote_identifier_rejects_names_over_postgres_byte_limit` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:483-488] |
| `quote_identifier_rejects_escaped_names_over_postgres_byte_limit` | function | `fn quote_identifier_rejects_escaped_names_over_postgres_byte_limit() {` | `quote_identifier_rejects_escaped_names_over_postgres_byte_limit [function]` | `dbee1402-9bbf-58a0-9d8d-72065361df9e` | 491-496 [crates/gwiki/src/setup.rs:491-496] | Indexed function `quote_identifier_rejects_escaped_names_over_postgres_byte_limit` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:491-496] |
