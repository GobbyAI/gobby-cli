---
title: crates/gwiki/src/api.rs
type: code_file
provenance:
- file: crates/gwiki/src/api.rs
  ranges:
  - 11-126
  - 129-132
  - 135-149
  - 152-154
  - 162-166
  - 171-179
  - 182-185
  - 188-193
  - 196-224
  - 229-233
  - 236-238
  - 240-242
  - 244-246
  - 248-254
  - 256-258
  - 260-265
  - 267-272
  - 276-278
  - 283-287
  - 290-296
  - 300-303
  - 306-311
  - 313-318
  - 320-325
  - 329-331
  - 335-339
  - 342-345
  - 354-370
  - 373-394
  - 397-427
  - 430-447
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/api.rs:11-126](crates/gwiki/src/api.rs#L11-L126), [crates/gwiki/src/api.rs:129-132](crates/gwiki/src/api.rs#L129-L132), [crates/gwiki/src/api.rs:135-149](crates/gwiki/src/api.rs#L135-L149), [crates/gwiki/src/api.rs:152-154](crates/gwiki/src/api.rs#L152-L154), [crates/gwiki/src/api.rs:162-166](crates/gwiki/src/api.rs#L162-L166), [crates/gwiki/src/api.rs:171-179](crates/gwiki/src/api.rs#L171-L179), [crates/gwiki/src/api.rs:182-185](crates/gwiki/src/api.rs#L182-L185), [crates/gwiki/src/api.rs:188-193](crates/gwiki/src/api.rs#L188-L193), [crates/gwiki/src/api.rs:196-224](crates/gwiki/src/api.rs#L196-L224), [crates/gwiki/src/api.rs:229-233](crates/gwiki/src/api.rs#L229-L233), [crates/gwiki/src/api.rs:236-238](crates/gwiki/src/api.rs#L236-L238), [crates/gwiki/src/api.rs:240-242](crates/gwiki/src/api.rs#L240-L242), [crates/gwiki/src/api.rs:244-246](crates/gwiki/src/api.rs#L244-L246), [crates/gwiki/src/api.rs:248-254](crates/gwiki/src/api.rs#L248-L254), [crates/gwiki/src/api.rs:256-258](crates/gwiki/src/api.rs#L256-L258), [crates/gwiki/src/api.rs:260-265](crates/gwiki/src/api.rs#L260-L265), [crates/gwiki/src/api.rs:267-272](crates/gwiki/src/api.rs#L267-L272), [crates/gwiki/src/api.rs:276-278](crates/gwiki/src/api.rs#L276-L278), [crates/gwiki/src/api.rs:283-287](crates/gwiki/src/api.rs#L283-L287), [crates/gwiki/src/api.rs:290-296](crates/gwiki/src/api.rs#L290-L296), [crates/gwiki/src/api.rs:300-303](crates/gwiki/src/api.rs#L300-L303), [crates/gwiki/src/api.rs:306-311](crates/gwiki/src/api.rs#L306-L311), [crates/gwiki/src/api.rs:313-318](crates/gwiki/src/api.rs#L313-L318), [crates/gwiki/src/api.rs:320-325](crates/gwiki/src/api.rs#L320-L325), [crates/gwiki/src/api.rs:329-331](crates/gwiki/src/api.rs#L329-L331), [crates/gwiki/src/api.rs:335-339](crates/gwiki/src/api.rs#L335-L339), [crates/gwiki/src/api.rs:342-345](crates/gwiki/src/api.rs#L342-L345), [crates/gwiki/src/api.rs:354-370](crates/gwiki/src/api.rs#L354-L370), [crates/gwiki/src/api.rs:373-394](crates/gwiki/src/api.rs#L373-L394), [crates/gwiki/src/api.rs:397-427](crates/gwiki/src/api.rs#L397-L427), [crates/gwiki/src/api.rs:430-447](crates/gwiki/src/api.rs#L430-L447)

</details>

# crates/gwiki/src/api.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the `gwiki` command API: a parsed `Command` enum for all supported CLI operations, plus the option and result types those commands carry. It also models scope selection and identity, with helpers for choosing project/topic/global scope, naming scopes, and checking scope state. The remaining functions are validation rules that enforce allowed command combinations and environment constraints, such as when translation is required, how transcription routing depends on audio capability, and whether the crate has the expected `gcode` dependency.
[crates/gwiki/src/api.rs:11-126]
[crates/gwiki/src/api.rs:129-132]
[crates/gwiki/src/api.rs:135-149]
[crates/gwiki/src/api.rs:152-154]
[crates/gwiki/src/api.rs:162-166]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Command` | type | `pub enum Command {` | `Command [type]` | `410214b3-aa48-5813-b83e-3e668eb3249c` | 11-126 [crates/gwiki/src/api.rs:11-126] | Indexed type `Command` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:11-126] |
| `ReadTarget` | type | `pub enum ReadTarget {` | `ReadTarget [type]` | `9def0375-8851-5247-a0c5-2acc21712b66` | 129-132 [crates/gwiki/src/api.rs:129-132] | Indexed type `ReadTarget` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:129-132] |
| `SetupOptions` | class | `pub struct SetupOptions {` | `SetupOptions [class]` | `66312d87-9fc8-5af6-8c6b-8097d04b9944` | 135-149 [crates/gwiki/src/api.rs:135-149] | Indexed class `SetupOptions` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:135-149] |
| `BenchmarkOptions` | class | `pub struct BenchmarkOptions {` | `BenchmarkOptions [class]` | `3bdda600-2794-5866-bfa7-78cc8f97642d` | 152-154 [crates/gwiki/src/api.rs:152-154] | Indexed class `BenchmarkOptions` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:152-154] |
| `BenchmarkOptions::default` | method | `fn default() -> Self {` | `BenchmarkOptions::default [method]` | `1fca76d5-bd09-54e5-95a7-9b02c7096932` | 162-166 [crates/gwiki/src/api.rs:162-166] | Indexed method `BenchmarkOptions::default` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:162-166] |
| `IngestFileOptions` | class | `pub struct IngestFileOptions {` | `IngestFileOptions [class]` | `70f5fa2d-9aef-599e-8e2d-09367298e18b` | 171-179 [crates/gwiki/src/api.rs:171-179] | Indexed class `IngestFileOptions` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:171-179] |
| `SyncSessionsOptions` | class | `pub struct SyncSessionsOptions {` | `SyncSessionsOptions [class]` | `c19d4c4d-f2af-5ff9-bd02-309ffc2dbecc` | 182-185 [crates/gwiki/src/api.rs:182-185] | Indexed class `SyncSessionsOptions` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:182-185] |
| `ReviewReportOptions` | class | `pub struct ReviewReportOptions {` | `ReviewReportOptions [class]` | `e35e3312-c8a9-5915-8578-9feb7b6a5442` | 188-193 [crates/gwiki/src/api.rs:188-193] | Indexed class `ReviewReportOptions` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:188-193] |
| `IngestFileOptions::apply_to_ai_context` | method | `pub fn apply_to_ai_context(&self, context: &mut AiContext) {` | `IngestFileOptions::apply_to_ai_context [method]` | `41d7320e-1377-57b6-ba11-65ca132a3333` | 196-224 [crates/gwiki/src/api.rs:196-224] | Indexed method `IngestFileOptions::apply_to_ai_context` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:196-224] |
| `ScopeSelection` | type | `pub enum ScopeSelection {` | `ScopeSelection [type]` | `8f665b31-c2b3-5f7a-a087-7f6c361048df` | 229-233 [crates/gwiki/src/api.rs:229-233] | Indexed type `ScopeSelection` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:229-233] |
| `ScopeSelection::detect` | method | `pub fn detect() -> Self {` | `ScopeSelection::detect [method]` | `69ace879-af2a-5539-aee6-fe5380ed959a` | 236-238 [crates/gwiki/src/api.rs:236-238] | Indexed method `ScopeSelection::detect` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:236-238] |
| `ScopeSelection::project` | method | `pub fn project(root: impl Into<PathBuf>) -> Self {` | `ScopeSelection::project [method]` | `a4ebd891-37e4-55d1-a33f-2d54e91122e3` | 240-242 [crates/gwiki/src/api.rs:240-242] | Indexed method `ScopeSelection::project` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:240-242] |
| `ScopeSelection::topic` | method | `pub fn topic(topic: impl Into<String>) -> Self {` | `ScopeSelection::topic [method]` | `ff3c67aa-0bbf-57bf-a455-cd69bf66d414` | 244-246 [crates/gwiki/src/api.rs:244-246] | Indexed method `ScopeSelection::topic` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:244-246] |
| `ScopeSelection::identity` | method | `pub fn identity(&self) -> ScopeIdentity {` | `ScopeSelection::identity [method]` | `2f32904a-39d2-5c4f-bc1d-725fb9b34918` | 248-254 [crates/gwiki/src/api.rs:248-254] | Indexed method `ScopeSelection::identity` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:248-254] |
| `ScopeSelection::is_project` | method | `pub fn is_project(&self) -> bool {` | `ScopeSelection::is_project [method]` | `20f877bf-d7ba-5c25-9db1-08c4ae6eb839` | 256-258 [crates/gwiki/src/api.rs:256-258] | Indexed method `ScopeSelection::is_project` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:256-258] |
| `ScopeSelection::project_root` | method | `pub fn project_root(&self) -> Option<&Path> {` | `ScopeSelection::project_root [method]` | `dcb76e93-103c-53a7-8ed6-0498158f287d` | 260-265 [crates/gwiki/src/api.rs:260-265] | Indexed method `ScopeSelection::project_root` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:260-265] |
| `ScopeSelection::topic_name` | method | `pub fn topic_name(&self) -> Option<&str> {` | `ScopeSelection::topic_name [method]` | `242db19f-a9fa-5bc1-a008-c1bd73f4a76e` | 267-272 [crates/gwiki/src/api.rs:267-272] | Indexed method `ScopeSelection::topic_name` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:267-272] |
| `ScopeSelection::default` | method | `fn default() -> Self {` | `ScopeSelection::default [method]` | `95ee0568-fb99-5867-9e1f-c36ac43747d5` | 276-278 [crates/gwiki/src/api.rs:276-278] | Indexed method `ScopeSelection::default` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:276-278] |
| `ScopeKind` | type | `pub enum ScopeKind {` | `ScopeKind [type]` | `ec828b3c-f5a8-5f81-aad7-a63bb122c2ee` | 283-287 [crates/gwiki/src/api.rs:283-287] | Indexed type `ScopeKind` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:283-287] |
| `ScopeKind::as_str` | method | `pub fn as_str(self) -> &'static str {` | `ScopeKind::as_str [method]` | `434f73d4-41ae-532b-b751-04feece0b35d` | 290-296 [crates/gwiki/src/api.rs:290-296] | Indexed method `ScopeKind::as_str` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:290-296] |
| `ScopeIdentity` | class | `pub struct ScopeIdentity {` | `ScopeIdentity [class]` | `f2b1ba88-4dd9-538a-8495-c3a553fe8481` | 300-303 [crates/gwiki/src/api.rs:300-303] | Indexed class `ScopeIdentity` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:300-303] |
| `ScopeIdentity::global` | method | `pub fn global() -> Self {` | `ScopeIdentity::global [method]` | `adea1fe2-8ce0-51bd-8a44-50021da33a07` | 306-311 [crates/gwiki/src/api.rs:306-311] | Indexed method `ScopeIdentity::global` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:306-311] |
| `ScopeIdentity::project` | method | `pub fn project(id: impl Into<String>) -> Self {` | `ScopeIdentity::project [method]` | `5732af34-2fa5-58ee-84a0-222be3074bad` | 313-318 [crates/gwiki/src/api.rs:313-318] | Indexed method `ScopeIdentity::project` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:313-318] |
| `ScopeIdentity::topic` | method | `pub fn topic(id: impl Into<String>) -> Self {` | `ScopeIdentity::topic [method]` | `d706d6b5-b48e-52e6-b388-135e363876d9` | 320-325 [crates/gwiki/src/api.rs:320-325] | Indexed method `ScopeIdentity::topic` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:320-325] |
| `ScopeIdentity::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `ScopeIdentity::fmt [method]` | `91c28986-b042-5b17-91e2-0a0baf51ad68` | 329-331 [crates/gwiki/src/api.rs:329-331] | Indexed method `ScopeIdentity::fmt` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:329-331] |
| `CommandOutcome` | class | `pub struct CommandOutcome {` | `CommandOutcome [class]` | `f6906339-7c14-5389-bbab-300724b2520d` | 335-339 [crates/gwiki/src/api.rs:335-339] | Indexed class `CommandOutcome` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:335-339] |
| `CommandResult` | class | `pub struct CommandResult {` | `CommandResult [class]` | `c79e5dcf-71ca-5b80-92e1-9ea2ca17024d` | 342-345 [crates/gwiki/src/api.rs:342-345] | Indexed class `CommandResult` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:342-345] |
| `scope_selection_constructors_express_allowed_states` | function | `fn scope_selection_constructors_express_allowed_states() {` | `scope_selection_constructors_express_allowed_states [function]` | `7e04208b-e053-5a47-bf63-ce1220be0850` | 354-370 [crates/gwiki/src/api.rs:354-370] | Indexed function `scope_selection_constructors_express_allowed_states` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:354-370] |
| `target_lang_requires_translate_flag` | function | `fn target_lang_requires_translate_flag() {` | `target_lang_requires_translate_flag [function]` | `0df945e6-e480-5b90-be8f-2a75920bcd5e` | 373-394 [crates/gwiki/src/api.rs:373-394] | Indexed function `target_lang_requires_translate_flag` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:373-394] |
| `transcription_routing_applies_to_active_audio_capability` | function | `fn transcription_routing_applies_to_active_audio_capability() {` | `transcription_routing_applies_to_active_audio_capability [function]` | `ce32c3ae-ccee-5206-b673-1b190574cb6e` | 397-427 [crates/gwiki/src/api.rs:397-427] | Indexed function `transcription_routing_applies_to_active_audio_capability` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:397-427] |
| `crate_has_no_gcode_dependency` | function | `fn crate_has_no_gcode_dependency() {` | `crate_has_no_gcode_dependency [function]` | `847cd3f9-c34a-5790-bb7e-cec4d724a2ff` | 430-447 [crates/gwiki/src/api.rs:430-447] | Indexed function `crate_has_no_gcode_dependency` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:430-447] |
