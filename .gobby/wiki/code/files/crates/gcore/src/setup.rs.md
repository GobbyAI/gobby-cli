---
title: crates/gcore/src/setup.rs
type: code_file
provenance:
- file: crates/gcore/src/setup.rs
  ranges:
  - 11-18
  - 26-34
  - 38-43
  - 45-50
  - 53-54
  - 57-64
  - 69-84
  - 90-100
  - 104-107
  - 111-113
  - 118-120
  - 125-132
  - 136-156
  - '159'
  - 162-169
  - 172-181
  - 190-245
  - 248-274
  - 277-315
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/setup.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file defines the shared setup boundary for gobby: it classifies setup resources by `StoreKind`, provides validation and setup contexts that carry optional datastore/config handles, and wraps validation results in `ValidationReport` with an `is_healthy` check. It also defines the callback types and object descriptors for consumer-supplied validation and creation (`RequiredValidator`, `RequiredObject`, `AttachedValidator`, `OwnedObject`, `SetupPostgresExecutor`, `StandaloneSetup`, `SetupError`, `SetupReport`), so attached-mode checks and standalone provisioning can share the same setup abstractions. The included tests verify runtime validation guidance, mutable-context access inside validator closures, and creator closures executing without moving shared ownership.
[crates/gcore/src/setup.rs:11-18]
[crates/gcore/src/setup.rs:26-34]
[crates/gcore/src/setup.rs:38-43]
[crates/gcore/src/setup.rs:45-50]
[crates/gcore/src/setup.rs:47-49]

## API Symbols

- `StoreKind` (type) component `StoreKind [type]` (`0310c686-fbdc-5058-b3f7-12cb1ed5910b`) lines 11-18 [crates/gcore/src/setup.rs:11-18]
  - Signature: `pub enum StoreKind {`
  - Purpose: Indexed type `StoreKind` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:11-18]
- `ValidationContext` (class) component `ValidationContext [class]` (`d9a5cd90-d44a-54d2-9b97-a434ad020217`) lines 26-34 [crates/gcore/src/setup.rs:26-34]
  - Signature: `pub struct ValidationContext<'a> {`
  - Purpose: `ValidationContext` is a generic struct that holds optional references to PostgreSQL, FalkorDB, and Qdrant database connections and configurations for use during validation operations. [crates/gcore/src/setup.rs:26-34]
- `ValidationReport` (class) component `ValidationReport [class]` (`ecd78645-0e4d-53b0-84e7-b3a31816a2ac`) lines 38-43 [crates/gcore/src/setup.rs:38-43]
  - Signature: `pub struct ValidationReport {`
  - Purpose: ValidationReport partitions validation results into passed object names (`present`) and failed objects paired with their structured `SetupIssue` details (`missing`). [crates/gcore/src/setup.rs:38-43]
- `ValidationReport` (class) component `ValidationReport [class]` (`7597c836-a220-5fc7-aa50-b6a68a0ade40`) lines 45-50 [crates/gcore/src/setup.rs:45-50]
  - Signature: `impl ValidationReport {`
  - Purpose: Provides an `is_healthy()` method that returns `true` if and only if the `missing` collection is empty, indicating all required objects passed validation. [crates/gcore/src/setup.rs:45-50]
- `ValidationReport.is_healthy` (method) component `ValidationReport.is_healthy [method]` (`cb47481d-b34b-5970-8443-d3a9143e461b`) lines 47-49 [crates/gcore/src/setup.rs:47-49]
  - Signature: `pub fn is_healthy(&self) -> bool {`
  - Purpose: Returns `true` if the `missing` field is empty, indicating a healthy state; otherwise returns `false`. [crates/gcore/src/setup.rs:47-49]
- `RequiredValidator` (type) component `RequiredValidator [type]` (`5b518140-09bb-5d08-971a-3ffe22b99866`) lines 53-54 [crates/gcore/src/setup.rs:53-54]
  - Signature: `pub type RequiredValidator =`
  - Purpose: Indexed type `RequiredValidator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:53-54]
- `RequiredObject` (class) component `RequiredObject [class]` (`78fb8755-58dd-56c9-84a6-289624818116`) lines 57-64 [crates/gcore/src/setup.rs:57-64]
  - Signature: `pub struct RequiredObject {`
  - Purpose: RequiredObject is a struct that encapsulates a required data object's metadata—comprising a human-readable name, its owning StoreKind, and a boxed validator callback—to enable consumer-supplied validation logic. [crates/gcore/src/setup.rs:57-64]
- `AttachedValidator` (type) component `AttachedValidator [type]` (`6ffd4a9f-58eb-5bbc-aeba-b16a8d6b5d66`) lines 69-84 [crates/gcore/src/setup.rs:69-84]
  - Signature: `pub trait AttachedValidator {`
  - Purpose: Indexed type `AttachedValidator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:69-84]
- `AttachedValidator.validate` (method) component `AttachedValidator.validate [method]` (`26143e4a-9dac-5e5e-97f9-14f699054c8c`) lines 74-83 [crates/gcore/src/setup.rs:74-83]
  - Signature: `fn validate(&self, ctx: &mut ValidationContext<'_>) -> ValidationReport {`
  - Purpose: Validates each required object by executing its associated validator function against the provided context, populating the returned report's `present` list for successful validations and `missing` list for failures with their error details. [crates/gcore/src/setup.rs:74-83]
- `SetupContext` (class) component `SetupContext [class]` (`a3a2fa08-8b1d-5e57-b3a0-67814a636dd5`) lines 90-100 [crates/gcore/src/setup.rs:90-100]
  - Signature: `pub struct SetupContext<'a> {`
  - Purpose: SetupContext<'a> is a lifetime-bounded configuration struct containing optional borrowed references to PostgreSQL, FalkorDB, and Qdrant connectors/configs with a non-interactive mode flag. [crates/gcore/src/setup.rs:90-100]
- `SetupPostgresExecutor` (type) component `SetupPostgresExecutor [type]` (`7b8aab67-a177-56c7-897c-63ebd1fab2a8`) lines 104-107 [crates/gcore/src/setup.rs:104-107]
  - Signature: `pub trait SetupPostgresExecutor {`
  - Purpose: Indexed type `SetupPostgresExecutor` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:104-107]
- `batch_execute` (function) component `batch_execute [function]` (`32c3250f-f9a2-5036-824b-12661a9f5554`) lines 111-113 [crates/gcore/src/setup.rs:111-113]
  - Signature: `fn batch_execute(&mut self, sql: &str) -> Result<(), postgres::Error> {`
  - Purpose: Executes a batch of SQL statements via the underlying PostgreSQL client, delegating to `postgres::Client::batch_execute` and returning a `Result` indicating either success or a `postgres::Error`. [crates/gcore/src/setup.rs:111-113]
- `batch_execute` (function) component `batch_execute [function]` (`88bed2da-bb74-544f-9e8e-79fc5578c318`) lines 118-120 [crates/gcore/src/setup.rs:118-120]
  - Signature: `fn batch_execute(&mut self, sql: &str) -> Result<(), postgres::Error> {`
  - Purpose: Executes multiple SQL statements in a single batch within a PostgreSQL transaction, delegating to the underlying `postgres::Transaction` implementation and returning success or a postgres error. [crates/gcore/src/setup.rs:118-120]
- `SetupReport` (class) component `SetupReport [class]` (`15f62e3d-9367-54f4-a452-60e6e264fbae`) lines 125-132 [crates/gcore/src/setup.rs:125-132]
  - Signature: `pub struct SetupReport {`
  - Purpose: SetupReport aggregates setup operation results into three categories: successfully created objects, skipped pre-existing objects, and failures paired with error details. [crates/gcore/src/setup.rs:125-132]
- `SetupError` (type) component `SetupError [type]` (`0566ffe3-2482-5410-a138-ec404aa3230e`) lines 136-156 [crates/gcore/src/setup.rs:136-156]
  - Signature: `pub enum SetupError {`
  - Purpose: Indexed type `SetupError` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:136-156]
- `OwnedCreator` (type) component `OwnedCreator [type]` (`3167f988-403b-524f-9808-ebee76bbbe87`) lines 159-159 [crates/gcore/src/setup.rs:159]
  - Signature: `pub type OwnedCreator = dyn for<'ctx> FnMut(&mut SetupContext<'ctx>) -> Result<(), SetupError>;`
  - Purpose: Indexed type `OwnedCreator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:159]
- `OwnedObject` (class) component `OwnedObject [class]` (`20d53cf5-1b03-5d8d-9378-5d7a34f36526`) lines 162-169 [crates/gcore/src/setup.rs:162-169]
  - Signature: `pub struct OwnedObject {`
  - Purpose: `OwnedObject` is a struct representing a store-managed resource with a human-readable name, owning `StoreKind`, and a boxed consumer-supplied creation function. [crates/gcore/src/setup.rs:162-169]
- `StandaloneSetup` (type) component `StandaloneSetup [type]` (`6cbd6b81-6d40-57e4-91f4-eb68afdda3ee`) lines 172-181 [crates/gcore/src/setup.rs:172-181]
  - Signature: `pub trait StandaloneSetup {`
  - Purpose: Indexed type `StandaloneSetup` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:172-181]
- `runtime_validation_reports_setup_guidance` (function) component `runtime_validation_reports_setup_guidance [function]` (`798d588e-dc8d-58d3-9c4c-1888611c85c7`) lines 190-245 [crates/gcore/src/setup.rs:190-245]
  - Signature: `fn runtime_validation_reports_setup_guidance() {`
  - Purpose: This function tests a RuntimeValidator that implements AttachedValidator to validate required PostgreSQL objects and asserts the validation report correctly identifies the missing BM25 index with setup guidance. [crates/gcore/src/setup.rs:190-245]
- `RuntimeValidator` (class) component `RuntimeValidator [class]` (`ab2c15de-0fae-50c3-afc1-2cbc08baaa0e`) lines 191-191 [crates/gcore/src/setup.rs:191]
  - Signature: `struct RuntimeValidator;`
  - Purpose: # RuntimeValidator

A struct that encapsulates validation logic to be executed at runtime, likely for checking constraints or invariants during program execution. [crates/gcore/src/setup.rs:191]
- `RuntimeValidator` (class) component `RuntimeValidator [class]` (`3e0dbd62-89b3-5db5-9657-1579b8fb35eb`) lines 193-218 [crates/gcore/src/setup.rs:193-218]
  - Signature: `impl AttachedValidator for RuntimeValidator {`
  - Purpose: RuntimeValidator implements `AttachedValidator` to specify two required PostgreSQL-backed objects—a symbols table with a passing validator and a BM25 index with a failing validator that directs users to execute the `gobby setup standalone` command. [crates/gcore/src/setup.rs:193-218]
- `RuntimeValidator.required_objects` (method) component `RuntimeValidator.required_objects [method]` (`b5aeeba6-b19c-5e06-a297-6d97945ace49`) lines 194-217 [crates/gcore/src/setup.rs:194-217]
  - Signature: `fn required_objects(&self) -> Vec<RequiredObject> {`
  - Purpose: Returns a vector specifying two required Postgres objects—a symbols table with a no-op validator and a BM25 index with a validator that mandates external setup via the "gobby setup standalone" command. [crates/gcore/src/setup.rs:194-217]
- `validator_can_query_through_mutable_context` (function) component `validator_can_query_through_mutable_context [function]` (`6c64f7a1-d575-565a-ac5c-7260412a63e8`) lines 248-274 [crates/gcore/src/setup.rs:248-274]
  - Signature: `fn validator_can_query_through_mutable_context() {`
  - Purpose: Tests that a validator closure can query and capture configuration values from a mutable `ValidationContext` parameter through closure-based interior mutability. [crates/gcore/src/setup.rs:248-274]
- `creator_executes_without_moving_ownership` (function) component `creator_executes_without_moving_ownership [function]` (`d8b0c79c-8ad3-5c0b-87b3-e7b435e41ffe`) lines 277-315 [crates/gcore/src/setup.rs:277-315]
  - Signature: `fn creator_executes_without_moving_ownership() {`
  - Purpose: Verifies that multiple creator closures can execute with mutable context borrowing and shared interior-mutable state via `Rc<RefCell<>>` without transferring ownership between them. [crates/gcore/src/setup.rs:277-315]

