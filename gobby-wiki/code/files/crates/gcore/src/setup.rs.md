---
title: crates/gcore/src/setup.rs
type: code_file
provenance:
- file: crates/gcore/src/setup.rs
  ranges:
  - 11-18
  - 26-34
  - 38-43
  - 47-49
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/setup.rs:11-18](crates/gcore/src/setup.rs#L11-L18), [crates/gcore/src/setup.rs:26-34](crates/gcore/src/setup.rs#L26-L34), [crates/gcore/src/setup.rs:38-43](crates/gcore/src/setup.rs#L38-L43), [crates/gcore/src/setup.rs:47-49](crates/gcore/src/setup.rs#L47-L49), [crates/gcore/src/setup.rs:53-54](crates/gcore/src/setup.rs#L53-L54), [crates/gcore/src/setup.rs:57-64](crates/gcore/src/setup.rs#L57-L64), [crates/gcore/src/setup.rs:69-84](crates/gcore/src/setup.rs#L69-L84), [crates/gcore/src/setup.rs:90-100](crates/gcore/src/setup.rs#L90-L100), [crates/gcore/src/setup.rs:104-107](crates/gcore/src/setup.rs#L104-L107), [crates/gcore/src/setup.rs:111-113](crates/gcore/src/setup.rs#L111-L113), [crates/gcore/src/setup.rs:118-120](crates/gcore/src/setup.rs#L118-L120), [crates/gcore/src/setup.rs:125-132](crates/gcore/src/setup.rs#L125-L132), [crates/gcore/src/setup.rs:136-156](crates/gcore/src/setup.rs#L136-L156), [crates/gcore/src/setup.rs:159](crates/gcore/src/setup.rs#L159), [crates/gcore/src/setup.rs:162-169](crates/gcore/src/setup.rs#L162-L169), [crates/gcore/src/setup.rs:172-181](crates/gcore/src/setup.rs#L172-L181), [crates/gcore/src/setup.rs:190-245](crates/gcore/src/setup.rs#L190-L245), [crates/gcore/src/setup.rs:248-274](crates/gcore/src/setup.rs#L248-L274), [crates/gcore/src/setup.rs:277-315](crates/gcore/src/setup.rs#L277-L315)

</details>

# crates/gcore/src/setup.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Shared setup-mode boundary for `gcore`: it defines the types and helpers used to validate externally managed datastore state instead of creating schema or services implicitly. The file centers on `StoreKind`, `ValidationContext`, and `ValidationReport` for describing which backends are available and whether required objects are present, then uses `RequiredObject`, `AttachedValidator`, and `RuntimeValidator` to run consumer-supplied checks and collect `SetupIssue`s into a setup report. It also includes the setup/ownership types and error aliases for attached and standalone setup flows, plus helper functions for executing batches and for guiding runtime validation behavior.
[crates/gcore/src/setup.rs:11-18]
[crates/gcore/src/setup.rs:26-34]
[crates/gcore/src/setup.rs:38-43]
[crates/gcore/src/setup.rs:47-49]
[crates/gcore/src/setup.rs:53-54]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `StoreKind` | type | `pub enum StoreKind {` | `StoreKind [type]` | `0310c686-fbdc-5058-b3f7-12cb1ed5910b` | 11-18 [crates/gcore/src/setup.rs:11-18] | Indexed type `StoreKind` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:11-18] |
| `ValidationContext` | class | `pub struct ValidationContext<'a> {` | `ValidationContext [class]` | `d9a5cd90-d44a-54d2-9b97-a434ad020217` | 26-34 [crates/gcore/src/setup.rs:26-34] | Indexed class `ValidationContext` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:26-34] |
| `ValidationReport` | class | `pub struct ValidationReport {` | `ValidationReport [class]` | `ecd78645-0e4d-53b0-84e7-b3a31816a2ac` | 38-43 [crates/gcore/src/setup.rs:38-43] | Indexed class `ValidationReport` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:38-43] |
| `ValidationReport::is_healthy` | method | `pub fn is_healthy(&self) -> bool {` | `ValidationReport::is_healthy [method]` | `cb47481d-b34b-5970-8443-d3a9143e461b` | 47-49 [crates/gcore/src/setup.rs:47-49] | Indexed method `ValidationReport::is_healthy` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:47-49] |
| `RequiredValidator` | type | `pub type RequiredValidator =` | `RequiredValidator [type]` | `5b518140-09bb-5d08-971a-3ffe22b99866` | 53-54 [crates/gcore/src/setup.rs:53-54] | Indexed type `RequiredValidator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:53-54] |
| `RequiredObject` | class | `pub struct RequiredObject {` | `RequiredObject [class]` | `78fb8755-58dd-56c9-84a6-289624818116` | 57-64 [crates/gcore/src/setup.rs:57-64] | Indexed class `RequiredObject` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:57-64] |
| `AttachedValidator` | type | `pub trait AttachedValidator {` | `AttachedValidator [type]` | `6ffd4a9f-58eb-5bbc-aeba-b16a8d6b5d66` | 69-84 [crates/gcore/src/setup.rs:69-84] | Indexed type `AttachedValidator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:69-84] |
| `AttachedValidator.validate` | method | `fn validate(&self, ctx: &mut ValidationContext<'_>) -> ValidationReport {` | `AttachedValidator.validate [method]` | `26143e4a-9dac-5e5e-97f9-14f699054c8c` | 74-83 [crates/gcore/src/setup.rs:74-83] | Indexed method `AttachedValidator.validate` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:74-83] |
| `SetupContext` | class | `pub struct SetupContext<'a> {` | `SetupContext [class]` | `a3a2fa08-8b1d-5e57-b3a0-67814a636dd5` | 90-100 [crates/gcore/src/setup.rs:90-100] | Indexed class `SetupContext` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:90-100] |
| `SetupPostgresExecutor` | type | `pub trait SetupPostgresExecutor {` | `SetupPostgresExecutor [type]` | `7b8aab67-a177-56c7-897c-63ebd1fab2a8` | 104-107 [crates/gcore/src/setup.rs:104-107] | Indexed type `SetupPostgresExecutor` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:104-107] |
| `batch_execute` | function | `fn batch_execute(&mut self, sql: &str) -> Result<(), postgres::Error> {` | `batch_execute [function]` | `32c3250f-f9a2-5036-824b-12661a9f5554` | 111-113 [crates/gcore/src/setup.rs:111-113] | Indexed function `batch_execute` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:111-113] |
| `batch_execute` | function | `fn batch_execute(&mut self, sql: &str) -> Result<(), postgres::Error> {` | `batch_execute [function]` | `88bed2da-bb74-544f-9e8e-79fc5578c318` | 118-120 [crates/gcore/src/setup.rs:118-120] | Indexed function `batch_execute` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:118-120] |
| `SetupReport` | class | `pub struct SetupReport {` | `SetupReport [class]` | `15f62e3d-9367-54f4-a452-60e6e264fbae` | 125-132 [crates/gcore/src/setup.rs:125-132] | Indexed class `SetupReport` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:125-132] |
| `SetupError` | type | `pub enum SetupError {` | `SetupError [type]` | `0566ffe3-2482-5410-a138-ec404aa3230e` | 136-156 [crates/gcore/src/setup.rs:136-156] | Indexed type `SetupError` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:136-156] |
| `OwnedCreator` | type | `pub type OwnedCreator = dyn for<'ctx> FnMut(&mut SetupContext<'ctx>) -> Result<(), SetupError>;` | `OwnedCreator [type]` | `3167f988-403b-524f-9808-ebee76bbbe87` | 159-159 [crates/gcore/src/setup.rs:159] | Indexed type `OwnedCreator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:159] |
| `OwnedObject` | class | `pub struct OwnedObject {` | `OwnedObject [class]` | `20d53cf5-1b03-5d8d-9378-5d7a34f36526` | 162-169 [crates/gcore/src/setup.rs:162-169] | Indexed class `OwnedObject` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:162-169] |
| `StandaloneSetup` | type | `pub trait StandaloneSetup {` | `StandaloneSetup [type]` | `6cbd6b81-6d40-57e4-91f4-eb68afdda3ee` | 172-181 [crates/gcore/src/setup.rs:172-181] | Indexed type `StandaloneSetup` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:172-181] |
| `runtime_validation_reports_setup_guidance` | function | `fn runtime_validation_reports_setup_guidance() {` | `runtime_validation_reports_setup_guidance [function]` | `798d588e-dc8d-58d3-9c4c-1888611c85c7` | 190-245 [crates/gcore/src/setup.rs:190-245] | Indexed function `runtime_validation_reports_setup_guidance` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:190-245] |
| `RuntimeValidator` | class | `struct RuntimeValidator;` | `RuntimeValidator [class]` | `ab2c15de-0fae-50c3-afc1-2cbc08baaa0e` | 191-191 [crates/gcore/src/setup.rs:191] | Indexed class `RuntimeValidator` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:191] |
| `RuntimeValidator::required_objects` | method | `fn required_objects(&self) -> Vec<RequiredObject> {` | `RuntimeValidator::required_objects [method]` | `b5aeeba6-b19c-5e06-a297-6d97945ace49` | 194-217 [crates/gcore/src/setup.rs:194-217] | Indexed method `RuntimeValidator::required_objects` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:194-217] |
| `validator_can_query_through_mutable_context` | function | `fn validator_can_query_through_mutable_context() {` | `validator_can_query_through_mutable_context [function]` | `6c64f7a1-d575-565a-ac5c-7260412a63e8` | 248-274 [crates/gcore/src/setup.rs:248-274] | Indexed function `validator_can_query_through_mutable_context` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:248-274] |
| `creator_executes_without_moving_ownership` | function | `fn creator_executes_without_moving_ownership() {` | `creator_executes_without_moving_ownership [function]` | `d8b0c79c-8ad3-5c0b-87b3-e7b435e41ffe` | 277-315 [crates/gcore/src/setup.rs:277-315] | Indexed function `creator_executes_without_moving_ownership` in `crates/gcore/src/setup.rs`. [crates/gcore/src/setup.rs:277-315] |
