---
title: crates/gwiki/src/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/setup.rs
  ranges:
  - 29-35
  - 37-47
  - 50-54
  - 57-61
  - 64-66
  - 68-237
  - 239-267
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

# crates/gwiki/src/setup.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/setup.rs` exposes 28 indexed API symbols.
[crates/gwiki/src/setup.rs:29-35]
[crates/gwiki/src/setup.rs:37-47]
[crates/gwiki/src/setup.rs:38-46]
[crates/gwiki/src/setup.rs:50-54]
[crates/gwiki/src/setup.rs:57-61]

## API Symbols

- `GwikiTable` (type) component `GwikiTable [type]` (`d41184ea-cd32-5b42-bd2d-27d8eb26657a`) lines 29-35 [crates/gwiki/src/setup.rs:29-35]
  - Signature: `pub enum GwikiTable {`
  - Purpose: Indexed type `GwikiTable` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:29-35]
- `GwikiTable` (class) component `GwikiTable [class]` (`1a097017-58fb-5a60-bebc-1fd56eab31d0`) lines 37-47 [crates/gwiki/src/setup.rs:37-47]
  - Signature: `impl GwikiTable {`
  - Purpose: `GwikiTable` is an enum-backed helper that returns the fixed `&'static str` database table name for each variant (`Documents`, `Chunks`, `Links`, `Sources`, `Ingestions`). [crates/gwiki/src/setup.rs:37-47]
- `GwikiTable.name` (method) component `GwikiTable.name [method]` (`72a4da07-e7d7-5a4e-9370-8717ff764914`) lines 38-46 [crates/gwiki/src/setup.rs:38-46]
  - Signature: `pub fn name(self) -> &'static str {`
  - Purpose: Returns the `&'static str` database/table identifier for the enum variant, mapping each variant to its corresponding `gwiki_*` name. [crates/gwiki/src/setup.rs:38-46]
- `GwikiPostgresObjectKind` (type) component `GwikiPostgresObjectKind [type]` (`02830482-9e01-5fc3-a646-11c401da77a9`) lines 50-54 [crates/gwiki/src/setup.rs:50-54]
  - Signature: `pub enum GwikiPostgresObjectKind {`
  - Purpose: Indexed type `GwikiPostgresObjectKind` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:50-54]
- `GwikiPostgresObject` (class) component `GwikiPostgresObject [class]` (`8659bf2b-0856-556e-8b3f-9bad85a4df58`) lines 57-61 [crates/gwiki/src/setup.rs:57-61]
  - Signature: `pub struct GwikiPostgresObject {`
  - Purpose: `GwikiPostgresObject` is a Rust struct that models a PostgreSQL schema object by storing its static name, its `GwikiPostgresObjectKind` classification, and the SQL text used to define or manage it. [crates/gwiki/src/setup.rs:57-61]
- `GwikiStandaloneSetup` (class) component `GwikiStandaloneSetup [class]` (`3ad73acc-2309-5e6e-a091-2a8a358795eb`) lines 64-66 [crates/gwiki/src/setup.rs:64-66]
  - Signature: `pub struct GwikiStandaloneSetup {`
  - Purpose: `GwikiStandaloneSetup` is a Rust configuration struct that stores a single private `schema: String` used to define the schema for a standalone Gwiki setup. [crates/gwiki/src/setup.rs:64-66]
- `GwikiStandaloneSetup` (class) component `GwikiStandaloneSetup [class]` (`b37955cc-c2ce-5189-92af-bca037efc46f`) lines 68-237 [crates/gwiki/src/setup.rs:68-237]
  - Signature: `impl GwikiStandaloneSetup {`
  - Purpose: `GwikiStandaloneSetup` is a setup builder that stores the default schema and generates the Postgres deployment objects for Gwiki, including a `pg_search` extension preflight check plus table and index DDL. [crates/gwiki/src/setup.rs:68-237]
- `GwikiStandaloneSetup.new` (method) component `GwikiStandaloneSetup.new [method]` (`b992f2e9-5c60-5ca7-bb54-52df6ab1c390`) lines 69-73 [crates/gwiki/src/setup.rs:69-73]
  - Signature: `pub fn new() -> Self {`
  - Purpose: Constructs a new instance with its `schema` field initialized to an owned `String` cloned from `DEFAULT_SCHEMA`. [crates/gwiki/src/setup.rs:69-73]
- `GwikiStandaloneSetup.schema` (method) component `GwikiStandaloneSetup.schema [method]` (`2c86de7e-e28e-59a6-9720-6ba8f1393cca`) lines 76-78 [crates/gwiki/src/setup.rs:76-78]
  - Signature: `pub fn schema(&self) -> &str {`
  - Purpose: Returns an immutable `&str` view of the value stored in `self.schema`. [crates/gwiki/src/setup.rs:76-78]
- `GwikiStandaloneSetup.postgres_objects` (method) component `GwikiStandaloneSetup.postgres_objects [method]` (`3847722d-09ed-5f22-8fe7-ed21bba70c04`) lines 80-101 [crates/gwiki/src/setup.rs:80-101]
  - Signature: `pub fn postgres_objects(&self) -> Result<Vec<GwikiPostgresObject>, SetupError> {`
  - Purpose: Builds and returns a `Vec<GwikiPostgresObject>` containing a `pg_search` extension preflight check plus all GWiki table and index definitions generated from `table_sql` and `index_sql`, or propagates any `SetupError` encountered while rendering them. [crates/gwiki/src/setup.rs:80-101]
- `GwikiStandaloneSetup.table_sql` (method) component `GwikiStandaloneSetup.table_sql [method]` (`1b835d4c-0d62-5436-97ff-d8951c7756b8`) lines 103-192 [crates/gwiki/src/setup.rs:103-192]
  - Signature: `fn table_sql(&self, table: GwikiTable) -> Result<String, SetupError> {`
  - Purpose: This method resolves the fully qualified relation name for the given `GwikiTable` and returns a variant-specific `CREATE TABLE IF NOT EXISTS` SQL statement as a `String`, or propagates a `SetupError` if relation qualification fails. [crates/gwiki/src/setup.rs:103-192]
- `GwikiStandaloneSetup.index_sql` (method) component `GwikiStandaloneSetup.index_sql [method]` (`46a60cce-48b0-5a0e-b444-b7abd61a6511`) lines 194-228 [crates/gwiki/src/setup.rs:194-228]
  - Signature: `fn index_sql(&self, index_name: &str) -> Result<String, SetupError> {`
  - Purpose: `index_sql` returns a database-specific `CREATE INDEX` or `CREATE UNIQUE INDEX` statement for a known `gwiki` index name by quoting the index identifier and resolving the fully qualified table names, or returns `SetupError::CreationFailed` if the name is unrecognized. [crates/gwiki/src/setup.rs:194-228]
- `GwikiStandaloneSetup.qualified_relation_name` (method) component `GwikiStandaloneSetup.qualified_relation_name [method]` (`18510e65-ff02-5d42-80fc-bc6c2ffd98d1`) lines 230-236 [crates/gwiki/src/setup.rs:230-236]
  - Signature: `fn qualified_relation_name(&self, relation: &str, label: &str) -> Result<String, SetupError> {`
  - Purpose: Returns a `Result<String, SetupError>` containing the schema-qualified relation name formatted as `"<quoted schema>.<quoted relation>"`, with both parts passed through `quote_identifier` and any quoting failure propagated. [crates/gwiki/src/setup.rs:230-236]
- `GwikiStandaloneSetup` (class) component `GwikiStandaloneSetup [class]` (`e1239896-f18e-5f42-9411-69e99f63791e`) lines 239-267 [crates/gwiki/src/setup.rs:239-267]
  - Signature: `impl StandaloneSetup for GwikiStandaloneSetup {`
  - Purpose: `GwikiStandaloneSetup` implements `StandaloneSetup` by exposing a fixed namespace, converting its PostgreSQL-defined objects into `OwnedObject`s, and creating them idempotently in sequence while accumulating a `SetupReport` and aborting on the first creation error.` [crates/gwiki/src/setup.rs:239-267]
- `GwikiStandaloneSetup.namespace` (method) component `GwikiStandaloneSetup.namespace [method]` (`a02e08f8-cea0-5add-9830-3931fa54fb63`) lines 240-242 [crates/gwiki/src/setup.rs:240-242]
  - Signature: `fn namespace(&self) -> &str {`
  - Purpose: Returns the compile-time `NAMESPACE` constant as a borrowed `&str`, exposing this type’s namespace identifier without allocation or transformation. [crates/gwiki/src/setup.rs:240-242]
- `GwikiStandaloneSetup.owned_objects` (method) component `GwikiStandaloneSetup.owned_objects [method]` (`e8251a09-ede7-5f57-9e4a-03e37f222408`) lines 244-250 [crates/gwiki/src/setup.rs:244-250]
  - Signature: `fn owned_objects(&self) -> Result<Vec<OwnedObject>, SetupError> {`
  - Purpose: It fetches the result of `self.postgres_objects()`, transforms each returned object with `owned_object`, collects the mapped values into a `Vec<OwnedObject>`, and returns them as `Ok(...)` while propagating any `SetupError` from `postgres_objects()`. [crates/gwiki/src/setup.rs:244-250]
- `GwikiStandaloneSetup.create` (method) component `GwikiStandaloneSetup.create [method]` (`23763266-dd63-5042-bbc7-c4a5fd2c73ed`) lines 252-266 [crates/gwiki/src/setup.rs:252-266]
  - Signature: `fn create(&self, ctx: &mut SetupContext<'_>) -> Result<SetupReport, SetupError> {`
  - Purpose: Initializes a `SetupReport`, iterates through all owned setup objects in order, invokes each object’s creator with the mutable `SetupContext`, records successful object names in `created`, stops at the first error after recording it in `failed`, and returns the aggregated report. [crates/gwiki/src/setup.rs:252-266]
- `default_setup` (function) component `default_setup [function]` (`d9c37a09-ff86-58bf-9330-d0e9e2209660`) lines 269-271 [crates/gwiki/src/setup.rs:269-271]
  - Signature: `pub fn default_setup() -> GwikiStandaloneSetup {`
  - Purpose: `default_setup` constructs and returns a fresh `GwikiStandaloneSetup` instance by delegating directly to `GwikiStandaloneSetup::new()`. [crates/gwiki/src/setup.rs:269-271]
- `table` (function) component `table [function]` (`a39fbe96-f60e-59e1-bd60-744dcf914621`) lines 273-279 [crates/gwiki/src/setup.rs:273-279]
  - Signature: `fn table(name: &'static str, sql: String) -> GwikiPostgresObject {`
  - Purpose: Constructs and returns a `GwikiPostgresObject` representing a table, using the provided static `name` and `sql` string and setting `kind` to `GwikiPostgresObjectKind::Table`. [crates/gwiki/src/setup.rs:273-279]
- `index` (function) component `index [function]` (`f722cdb6-98e6-513c-aa73-35c6a0bbe99e`) lines 281-287 [crates/gwiki/src/setup.rs:281-287]
  - Signature: `fn index(name: &'static str, sql: String) -> GwikiPostgresObject {`
  - Purpose: Constructs a `GwikiPostgresObject` for a PostgreSQL index by assigning the given `name`, setting `kind` to `GwikiPostgresObjectKind::Index`, and storing the provided SQL string. [crates/gwiki/src/setup.rs:281-287]
- `preflight` (function) component `preflight [function]` (`a84e5d95-286e-5ed2-81f1-6b109cde678b`) lines 289-295 [crates/gwiki/src/setup.rs:289-295]
  - Signature: `fn preflight(name: &'static str, sql: String) -> GwikiPostgresObject {`
  - Purpose: Constructs and returns a `GwikiPostgresObject` whose `kind` is `GwikiPostgresObjectKind::Preflight`, initialized with the provided static `name` and `sql` string. [crates/gwiki/src/setup.rs:289-295]
- `owned_object` (function) component `owned_object [function]` (`646ea3d9-6317-53ba-a7a2-402065fcd6ff`) lines 297-305 [crates/gwiki/src/setup.rs:297-305]
  - Signature: `fn owned_object(object: GwikiPostgresObject) -> OwnedObject {`
  - Purpose: Converts a `GwikiPostgresObject` into an `OwnedObject` by cloning its name, setting `store` to `StoreKind::Postgres`, and storing a boxed closure that executes `execute_postgres_ddl` with the captured name and SQL against the provided context. [crates/gwiki/src/setup.rs:297-305]
- `execute_postgres_ddl` (function) component `execute_postgres_ddl [function]` (`2100c1c4-b9cc-5913-a350-b01c995b1730`) lines 307-329 [crates/gwiki/src/setup.rs:307-329]
  - Signature: `fn execute_postgres_ddl(`
  - Purpose: `execute_postgres_ddl` requires a PostgreSQL connection in `SetupContext`, runs the provided SQL with `batch_execute`, and maps a missing connection to `SetupError::ConnectionFailed` or any execution failure to `SetupError::CreationFailed` for the named object. [crates/gwiki/src/setup.rs:307-329]
- `quote_identifier` (function) component `quote_identifier [function]` (`82344abb-c3a9-5f3e-ba2a-5af8643896a2`) lines 331-355 [crates/gwiki/src/setup.rs:331-355]
  - Signature: `fn quote_identifier(value: &str, label: &str) -> Result<String, SetupError> {`
  - Purpose: Trims the input, rejects empty or NUL-containing identifiers, escapes embedded `"` by doubling them, enforces `POSTGRES_IDENTIFIER_MAX_BYTES`, and returns the value wrapped in double quotes or a `SetupError::CreationFailed` tagged with `label`. [crates/gwiki/src/setup.rs:331-355]
- `setup_creates_only_gwiki_owned_objects` (function) component `setup_creates_only_gwiki_owned_objects [function]` (`c7319056-b5b1-50e4-83d6-cf43507155e0`) lines 363-454 [crates/gwiki/src/setup.rs:363-454]
  - Signature: `fn setup_creates_only_gwiki_owned_objects() {`
  - Purpose: Validates that `GwikiStandaloneSetup::new()` produces only `gwiki_`-prefixed PostgreSQL setup objects in `public`, including at least one table and one index, while excluding unrelated relations and any explicit `CREATE EXTENSION` or `CREATE SCHEMA` statements. [crates/gwiki/src/setup.rs:363-454]
- `published_lists_match_generated_objects` (function) component `published_lists_match_generated_objects [function]` (`3bf2176d-60c2-5a29-b92b-8004812c4e9d`) lines 457-480 [crates/gwiki/src/setup.rs:457-480]
  - Signature: `fn published_lists_match_generated_objects() {`
  - Purpose: It verifies that the PostgreSQL objects produced by `GwikiStandaloneSetup::postgres_objects()` contain exactly the same table names as `GWIKI_POSTGRES_TABLES` and the same index names as `GWIKI_POSTGRES_INDEXES`. [crates/gwiki/src/setup.rs:457-480]
- `quote_identifier_rejects_names_over_postgres_byte_limit` (function) component `quote_identifier_rejects_names_over_postgres_byte_limit [function]` (`d89634df-9b72-5370-87c9-1f24ef9a975e`) lines 483-488 [crates/gwiki/src/setup.rs:483-488]
  - Signature: `fn quote_identifier_rejects_names_over_postgres_byte_limit() {`
  - Purpose: It verifies that `quote_identifier` rejects an identifier longer than PostgreSQL’s 63-byte limit by returning an error whose message contains `at most 63 bytes`. [crates/gwiki/src/setup.rs:483-488]
- `quote_identifier_rejects_escaped_names_over_postgres_byte_limit` (function) component `quote_identifier_rejects_escaped_names_over_postgres_byte_limit [function]` (`dbee1402-9bbf-58a0-9d8d-72065361df9e`) lines 491-496 [crates/gwiki/src/setup.rs:491-496]
  - Signature: `fn quote_identifier_rejects_escaped_names_over_postgres_byte_limit() {`
  - Purpose: It verifies that `quote_identifier` returns an error mentioning the PostgreSQL 63-byte limit when an identifier containing an embedded double quote becomes too long after escaping. [crates/gwiki/src/setup.rs:491-496]

