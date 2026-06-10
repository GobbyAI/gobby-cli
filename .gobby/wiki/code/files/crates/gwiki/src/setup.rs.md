---
title: crates/gwiki/src/setup.rs
type: code_file
provenance:
- file: crates/gwiki/src/setup.rs
  ranges:
  - 29-35
  - 37-47
  - 38-46
  - 50-54
  - 57-61
  - 64-66
  - 68-236
  - 69-73
  - 75-77
  - 79-100
  - 102-191
  - 193-227
  - 229-235
  - 238-266
  - 239-241
  - 243-249
  - 251-265
  - 268-270
  - 272-278
  - 280-286
  - 288-294
  - 296-304
  - 306-328
  - 330-354
  - 362-453
  - 456-479
  - 482-487
  - 490-495
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
[crates/gwiki/src/setup.rs:64-66]
[crates/gwiki/src/setup.rs:68-236]
[crates/gwiki/src/setup.rs:69-73]
[crates/gwiki/src/setup.rs:75-77]
[crates/gwiki/src/setup.rs:79-100]
[crates/gwiki/src/setup.rs:102-191]
[crates/gwiki/src/setup.rs:193-227]
[crates/gwiki/src/setup.rs:229-235]
[crates/gwiki/src/setup.rs:238-266]
[crates/gwiki/src/setup.rs:239-241]
[crates/gwiki/src/setup.rs:243-249]
[crates/gwiki/src/setup.rs:251-265]
[crates/gwiki/src/setup.rs:268-270]
[crates/gwiki/src/setup.rs:272-278]
[crates/gwiki/src/setup.rs:280-286]
[crates/gwiki/src/setup.rs:288-294]
[crates/gwiki/src/setup.rs:296-304]
[crates/gwiki/src/setup.rs:306-328]
[crates/gwiki/src/setup.rs:330-354]
[crates/gwiki/src/setup.rs:362-453]
[crates/gwiki/src/setup.rs:456-479]
[crates/gwiki/src/setup.rs:482-487]
[crates/gwiki/src/setup.rs:490-495]

## API Symbols

- `GwikiTable` (type) component `GwikiTable [type]` (`d41184ea-cd32-5b42-bd2d-27d8eb26657a`) lines 29-35 [crates/gwiki/src/setup.rs:29-35]
  - Signature: `pub enum GwikiTable {`
  - Purpose: Indexed type `GwikiTable` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:29-35]
- `GwikiTable` (class) component `GwikiTable [class]` (`1a097017-58fb-5a60-bebc-1fd56eab31d0`) lines 37-47 [crates/gwiki/src/setup.rs:37-47]
  - Signature: `impl GwikiTable {`
  - Purpose: `GwikiTable` is an enum implementation that maps variant instances to their corresponding database table name strings via the `name()` method. [crates/gwiki/src/setup.rs:37-47]
- `GwikiTable.name` (method) component `GwikiTable.name [method]` (`72a4da07-e7d7-5a4e-9370-8717ff764914`) lines 38-46 [crates/gwiki/src/setup.rs:38-46]
  - Signature: `pub fn name(self) -> &'static str {`
  - Purpose: This method returns a static string literal corresponding to the enum variant's associated database table name by pattern matching. [crates/gwiki/src/setup.rs:38-46]
- `GwikiPostgresObjectKind` (type) component `GwikiPostgresObjectKind [type]` (`02830482-9e01-5fc3-a646-11c401da77a9`) lines 50-54 [crates/gwiki/src/setup.rs:50-54]
  - Signature: `pub enum GwikiPostgresObjectKind {`
  - Purpose: Indexed type `GwikiPostgresObjectKind` in `crates/gwiki/src/setup.rs`. [crates/gwiki/src/setup.rs:50-54]
- `GwikiPostgresObject` (class) component `GwikiPostgresObject [class]` (`8659bf2b-0856-556e-8b3f-9bad85a4df58`) lines 57-61 [crates/gwiki/src/setup.rs:57-61]
  - Signature: `pub struct GwikiPostgresObject {`
  - Purpose: `GwikiPostgresObject` is a struct that encapsulates metadata for a PostgreSQL database object, consisting of a static name identifier, a `GwikiPostgresObjectKind` type classifier, and its SQL definition string. [crates/gwiki/src/setup.rs:57-61]
- `GwikiStandaloneSetup` (class) component `GwikiStandaloneSetup [class]` (`3ad73acc-2309-5e6e-a091-2a8a358795eb`) lines 64-66 [crates/gwiki/src/setup.rs:64-66]
  - Signature: `pub struct GwikiStandaloneSetup {`
  - Purpose: GwikiStandaloneSetup is a Rust struct that encapsulates a schema String for configuring a standalone Gwiki instance. [crates/gwiki/src/setup.rs:64-66]
- `GwikiStandaloneSetup` (class) component `GwikiStandaloneSetup [class]` (`b37955cc-c2ce-5189-92af-bca037efc46f`) lines 68-236 [crates/gwiki/src/setup.rs:68-236]
  - Signature: `impl GwikiStandaloneSetup {`
  - Purpose: GwikiStandaloneSetup generates PostgreSQL DDL objects (tables, indexes, and extension preflight checks) required to initialize a standalone gwiki full-text search document storage system. [crates/gwiki/src/setup.rs:68-236]
- `GwikiStandaloneSetup.new` (method) component `GwikiStandaloneSetup.new [method]` (`b992f2e9-5c60-5ca7-bb54-52df6ab1c390`) lines 69-73 [crates/gwiki/src/setup.rs:69-73]
  - Signature: `pub fn new() -> Self {`
  - Purpose: A constructor that instantiates a new object with the `schema` field initialized to the String representation of `DEFAULT_SCHEMA`. [crates/gwiki/src/setup.rs:69-73]
- `GwikiStandaloneSetup.schema` (method) component `GwikiStandaloneSetup.schema [method]` (`5be92185-4bf8-5b78-ad2b-d67c124e5de2`) lines 75-77 [crates/gwiki/src/setup.rs:75-77]
  - Signature: `pub fn schema(&self) -> &str {`
  - Purpose: This method is a getter that returns an immutable reference to the internal `schema` string field. [crates/gwiki/src/setup.rs:75-77]
- `GwikiStandaloneSetup.postgres_objects` (method) component `GwikiStandaloneSetup.postgres_objects [method]` (`4550576f-f0dc-5d9a-bffa-922c666f0ecf`) lines 79-100 [crates/gwiki/src/setup.rs:79-100]
  - Signature: `pub fn postgres_objects(&self) -> Result<Vec<GwikiPostgresObject>, SetupError> {`
  - Purpose: Returns a `Result` containing a vector of PostgreSQL database objects—an extension preflight check for `pg_search`, gwiki tables, and their corresponding BM25 indexes. [crates/gwiki/src/setup.rs:79-100]
- `GwikiStandaloneSetup.table_sql` (method) component `GwikiStandaloneSetup.table_sql [method]` (`1bcbb2d8-35f3-5a07-9db6-2f94beb4eabb`) lines 102-191 [crates/gwiki/src/setup.rs:102-191]
  - Signature: `fn table_sql(&self, table: GwikiTable) -> Result<String, SetupError> {`
  - Purpose: # Summary

This method generates a schema-qualified SQL `CREATE TABLE` DDL statement corresponding to the specified `GwikiTable` enum variant (Documents, Chunks, Links, or Sources), with type-specific column definitions and defaults. [crates/gwiki/src/setup.rs:102-191]
- `GwikiStandaloneSetup.index_sql` (method) component `GwikiStandaloneSetup.index_sql [method]` (`ae92d173-906d-56c8-934b-68c2d03ca155`) lines 193-227 [crates/gwiki/src/setup.rs:193-227]
  - Signature: `fn index_sql(&self, index_name: &str) -> Result<String, SetupError> {`
  - Purpose: Returns a SQL CREATE INDEX statement for a specified gwiki PostgreSQL index name via pattern matching, or a SetupError if the index name is unrecognized. [crates/gwiki/src/setup.rs:193-227]
- `GwikiStandaloneSetup.qualified_relation_name` (method) component `GwikiStandaloneSetup.qualified_relation_name [method]` (`728ba77a-f414-5a6a-9b9d-389d3822da39`) lines 229-235 [crates/gwiki/src/setup.rs:229-235]
  - Signature: `fn qualified_relation_name(&self, relation: &str, label: &str) -> Result<String, SetupError> {`
  - Purpose: Constructs a schema-qualified relation name by concatenating the quoted schema identifier with the quoted relation identifier separated by a dot, propagating any identifier-quoting errors. [crates/gwiki/src/setup.rs:229-235]
- `GwikiStandaloneSetup` (class) component `GwikiStandaloneSetup [class]` (`a18f8ad5-d639-501e-9727-4c3f9f58c8b8`) lines 238-266 [crates/gwiki/src/setup.rs:238-266]
  - Signature: `impl StandaloneSetup for GwikiStandaloneSetup {`
  - Purpose: GwikiStandaloneSetup implements the StandaloneSetup trait to idempotently create gwiki-owned PostgreSQL schema objects with error tracking and fail-fast termination on creation failures. [crates/gwiki/src/setup.rs:238-266]
- `GwikiStandaloneSetup.namespace` (method) component `GwikiStandaloneSetup.namespace [method]` (`b45bbe14-e803-5a3b-9085-630d8b73a062`) lines 239-241 [crates/gwiki/src/setup.rs:239-241]
  - Signature: `fn namespace(&self) -> &str {`
  - Purpose: Returns an immutable reference to a static `NAMESPACE` string constant. [crates/gwiki/src/setup.rs:239-241]
- `GwikiStandaloneSetup.owned_objects` (method) component `GwikiStandaloneSetup.owned_objects [method]` (`e93950a0-228d-502c-a723-0b133d5b472e`) lines 243-249 [crates/gwiki/src/setup.rs:243-249]
  - Signature: `fn owned_objects(&self) -> Result<Vec<OwnedObject>, SetupError> {`
  - Purpose: Retrieves PostgreSQL objects and transforms each into an `OwnedObject` instance by mapping through the `owned_object` function, returning the collected vector or propagating any error. [crates/gwiki/src/setup.rs:243-249]
- `GwikiStandaloneSetup.create` (method) component `GwikiStandaloneSetup.create [method]` (`91eb98a2-e2f7-58c9-9cd3-5e864e65dec5`) lines 251-265 [crates/gwiki/src/setup.rs:251-265]
  - Signature: `fn create(&self, ctx: &mut SetupContext<'_>) -> Result<SetupReport, SetupError> {`
  - Purpose: This method sequentially invokes creator functions for each owned database object within the provided context, populating a SetupReport with successful creations and terminating on the first error. [crates/gwiki/src/setup.rs:251-265]
- `default_setup` (function) component `default_setup [function]` (`fa0e31c3-afff-5c49-abde-ba870fe5279d`) lines 268-270 [crates/gwiki/src/setup.rs:268-270]
  - Signature: `pub fn default_setup() -> GwikiStandaloneSetup {`
  - Purpose: Returns a new `GwikiStandaloneSetup` instance by invoking its constructor. [crates/gwiki/src/setup.rs:268-270]
- `table` (function) component `table [function]` (`aa1621c4-6b2c-52d2-bb0c-faae764bae7d`) lines 272-278 [crates/gwiki/src/setup.rs:272-278]
  - Signature: `fn table(name: &'static str, sql: String) -> GwikiPostgresObject {`
  - Purpose: Constructs a `GwikiPostgresObject` of `Table` kind from a static name and SQL definition string. [crates/gwiki/src/setup.rs:272-278]
- `index` (function) component `index [function]` (`1ee5a873-3642-5e4b-8902-e66048b8f7ca`) lines 280-286 [crates/gwiki/src/setup.rs:280-286]
  - Signature: `fn index(name: &'static str, sql: String) -> GwikiPostgresObject {`
  - Purpose: Constructs a `GwikiPostgresObject` with `Index` kind from a static name and SQL definition string. [crates/gwiki/src/setup.rs:280-286]
- `preflight` (function) component `preflight [function]` (`48515f98-c3dd-5580-8118-99ca57c00b3d`) lines 288-294 [crates/gwiki/src/setup.rs:288-294]
  - Signature: `fn preflight(name: &'static str, sql: String) -> GwikiPostgresObject {`
  - Purpose: Creates a `GwikiPostgresObject` configured with the `Preflight` kind, wrapping the provided static name and SQL statement. [crates/gwiki/src/setup.rs:288-294]
- `owned_object` (function) component `owned_object [function]` (`2e627d85-9f8a-5027-ba20-ad8e939a7e6c`) lines 296-304 [crates/gwiki/src/setup.rs:296-304]
  - Signature: `fn owned_object(object: GwikiPostgresObject) -> OwnedObject {`
  - Purpose: Transforms a `GwikiPostgresObject` into an `OwnedObject` by extracting its name and SQL, storing the kind as Postgres, and providing a closure-based DDL executor. [crates/gwiki/src/setup.rs:296-304]
- `execute_postgres_ddl` (function) component `execute_postgres_ddl [function]` (`d01a8437-8612-5b01-971e-90951f485f38`) lines 306-328 [crates/gwiki/src/setup.rs:306-328]
  - Signature: `fn execute_postgres_ddl(`
  - Purpose: Executes a PostgreSQL DDL statement from the setup context's database connection, returning a `ConnectionFailed` error if the connection is unavailable or a `CreationFailed` error if SQL execution fails. [crates/gwiki/src/setup.rs:306-328]
- `quote_identifier` (function) component `quote_identifier [function]` (`dced8ab7-388d-5b45-bc63-4c7d69b42898`) lines 330-354 [crates/gwiki/src/setup.rs:330-354]
  - Signature: `fn quote_identifier(value: &str, label: &str) -> Result<String, SetupError> {`
  - Purpose: Validates a PostgreSQL identifier by checking for empty strings, NUL bytes, and maximum byte length, escapes internal double quotes, and returns the quoted identifier as a double-quoted string. [crates/gwiki/src/setup.rs:330-354]
- `setup_creates_only_gwiki_owned_objects` (function) component `setup_creates_only_gwiki_owned_objects [function]` (`e76d570c-6b38-5476-a727-e20b5bc7d454`) lines 362-453 [crates/gwiki/src/setup.rs:362-453]
  - Signature: `fn setup_creates_only_gwiki_owned_objects() {`
  - Purpose: This test verifies that `GwikiStandaloneSetup` generates exclusively gwiki-prefixed PostgreSQL objects (tables and indexes) while excluding forbidden external dependencies and unnecessary schema/extension DDL statements. [crates/gwiki/src/setup.rs:362-453]
- `published_lists_match_generated_objects` (function) component `published_lists_match_generated_objects [function]` (`a5020c41-622e-56d5-a571-b85ec127313a`) lines 456-479 [crates/gwiki/src/setup.rs:456-479]
  - Signature: `fn published_lists_match_generated_objects() {`
  - Purpose: This test function asserts that the PostgreSQL table and index objects generated by `GwikiStandaloneSetup` match the published constants `GWIKI_POSTGRES_TABLES` and `GWIKI_POSTGRES_INDEXES`. [crates/gwiki/src/setup.rs:456-479]
- `quote_identifier_rejects_names_over_postgres_byte_limit` (function) component `quote_identifier_rejects_names_over_postgres_byte_limit [function]` (`619c9983-9631-5f06-a85c-365e9b0a7934`) lines 482-487 [crates/gwiki/src/setup.rs:482-487]
  - Signature: `fn quote_identifier_rejects_names_over_postgres_byte_limit() {`
  - Purpose: This test verifies that `quote_identifier` rejects identifiers exceeding PostgreSQL's 63-byte limit and returns an error message specifying the maximum allowed length. [crates/gwiki/src/setup.rs:482-487]
- `quote_identifier_rejects_escaped_names_over_postgres_byte_limit` (function) component `quote_identifier_rejects_escaped_names_over_postgres_byte_limit [function]` (`b71b01e6-72ac-5907-8758-05d7ef7be977`) lines 490-495 [crates/gwiki/src/setup.rs:490-495]
  - Signature: `fn quote_identifier_rejects_escaped_names_over_postgres_byte_limit() {`
  - Purpose: This test verifies that `quote_identifier` rejects identifiers that exceed PostgreSQL's 63-byte limit when escaped. [crates/gwiki/src/setup.rs:490-495]

