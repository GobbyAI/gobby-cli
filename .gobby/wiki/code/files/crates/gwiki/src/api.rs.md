---
title: crates/gwiki/src/api.rs
type: code_file
provenance:
- file: crates/gwiki/src/api.rs
  ranges:
  - 11-122
  - 125-128
  - 131-145
  - 148-150
  - 152-155
  - 157-163
  - 167-175
  - 178-183
  - 185-215
  - 219-223
  - 225-263
  - 265-269
  - 273-277
  - 279-287
  - 290-293
  - 295-316
  - 318-322
  - 325-329
  - 332-335
  - 344-360
  - 363-384
  - 387-417
  - 420-437
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/api.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the public API for `gwiki` commands and their supporting configuration types. `Command` enumerates every supported subcommand and carries the scoped inputs and options needed to drive setup, indexing, ingestion, search, reading, graphing, compiling, exporting, and review workflows.

The rest of the file provides the small types that make those commands consistent: `ReadTarget` for read destinations, option structs for setup/benchmark/ingest/review behavior, and the scope model (`ScopeSelection`, `ScopeKind`, `ScopeIdentity`) used to represent global, project, or topic context. `IngestFileOptions` also knows how to project its AI-routing settings into an `AiContext`, while the tests verify scope construction, translation-target handling, routing application, and crate dependency constraints.
[crates/gwiki/src/api.rs:11-122]
[crates/gwiki/src/api.rs:125-128]
[crates/gwiki/src/api.rs:131-145]
[crates/gwiki/src/api.rs:148-150]
[crates/gwiki/src/api.rs:152-155]

## API Symbols

- `Command` (type) component `Command [type]` (`410214b3-aa48-5813-b83e-3e668eb3249c`) lines 11-122 [crates/gwiki/src/api.rs:11-122]
  - Signature: `pub enum Command {`
  - Purpose: Indexed type `Command` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:11-122]
- `ReadTarget` (type) component `ReadTarget [type]` (`7b418672-ae93-5e52-b295-edf04d9cb89f`) lines 125-128 [crates/gwiki/src/api.rs:125-128]
  - Signature: `pub enum ReadTarget {`
  - Purpose: Indexed type `ReadTarget` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:125-128]
- `SetupOptions` (class) component `SetupOptions [class]` (`0895fad2-f88e-5331-b6d3-67acd01cca47`) lines 131-145 [crates/gwiki/src/api.rs:131-145]
  - Signature: `pub struct SetupOptions {`
  - Purpose: 'SetupOptions' is a configuration struct for initializing the system, controlling standalone/service setup and supplying optional database, FalkorDB, Qdrant, and embedding provider connection parameters and model settings. [crates/gwiki/src/api.rs:131-145]
- `BenchmarkOptions` (class) component `BenchmarkOptions [class]` (`dac94230-ae15-584d-9040-cbeeabc29227`) lines 148-150 [crates/gwiki/src/api.rs:148-150]
  - Signature: `pub struct BenchmarkOptions {`
  - Purpose: 'BenchmarkOptions' is a configuration struct containing a single 'usize' field, 'retrieval_candidates', which specifies the number of retrieval candidates to consider during benchmarking. [crates/gwiki/src/api.rs:148-150]
- `BenchmarkOptions` (class) component `BenchmarkOptions [class]` (`62587416-d748-5c04-a1ad-38556256ba26`) lines 152-155 [crates/gwiki/src/api.rs:152-155]
  - Signature: `impl BenchmarkOptions {`
  - Purpose: 'BenchmarkOptions' is an 'impl' block that defines the associated constant 'DEFAULT_RETRIEVAL_CANDIDATES' as an alias of 'crate::benchmark::DEFAULT_RETRIEVAL_PRECISION_CANDIDATES'. [crates/gwiki/src/api.rs:152-155]
- `BenchmarkOptions` (class) component `BenchmarkOptions [class]` (`4d72bbdd-e7af-5d60-a646-c742d8cb374a`) lines 157-163 [crates/gwiki/src/api.rs:157-163]
  - Signature: `impl Default for BenchmarkOptions {`
  - Purpose: 'BenchmarkOptions' implements 'Default' by constructing a value whose 'retrieval_candidates' field is initialized to 'Self::DEFAULT_RETRIEVAL_CANDIDATES'. [crates/gwiki/src/api.rs:157-163]
- `BenchmarkOptions.default` (method) component `BenchmarkOptions.default [method]` (`d1b1198a-701e-5dbd-8262-dbd542c96d2f`) lines 158-162 [crates/gwiki/src/api.rs:158-162]
  - Signature: `fn default() -> Self {`
  - Purpose: Constructs and returns a 'Self' instance with 'retrieval_candidates' initialized to 'Self::DEFAULT_RETRIEVAL_CANDIDATES'. [crates/gwiki/src/api.rs:158-162]
- `IngestFileOptions` (class) component `IngestFileOptions [class]` (`b99021db-3183-501c-98cf-cd75e293473b`) lines 167-175 [crates/gwiki/src/api.rs:167-175]
  - Signature: `pub struct IngestFileOptions {`
  - Purpose: 'IngestFileOptions' is a configuration struct for file ingestion that toggles AI usage and translation, optionally sets a target language, controls video frame extraction cadence, and supplies per-modality AI routing overrides for transcription, vision, and text processing. [crates/gwiki/src/api.rs:167-175]
- `ReviewReportOptions` (class) component `ReviewReportOptions [class]` (`3f3800ef-b44a-50d9-b4ef-e39641dc585f`) lines 178-183 [crates/gwiki/src/api.rs:178-183]
  - Signature: `pub struct ReviewReportOptions {`
  - Purpose: 'ReviewReportOptions' is a configuration struct that carries the target file and symbol lists, an optional diff file path, and the output destination or format string for generating a review report. [crates/gwiki/src/api.rs:178-183]
- `IngestFileOptions` (class) component `IngestFileOptions [class]` (`b8ca1b51-747b-55f7-a8e9-7af32a6b7675`) lines 185-215 [crates/gwiki/src/api.rs:185-215]
  - Signature: `impl IngestFileOptions {`
  - Purpose: 'IngestFileOptions' configures AI ingestion behavior by selectively applying transcription, translation, vision, and text routing settings to an 'AiContext', or disabling all AI bindings when 'no_ai' is set. [crates/gwiki/src/api.rs:185-215]
- `IngestFileOptions.apply_to_ai_context` (method) component `IngestFileOptions.apply_to_ai_context [method]` (`1addaf5d-5bfd-5192-8082-48701de197dd`) lines 186-214 [crates/gwiki/src/api.rs:186-214]
  - Signature: `pub fn apply_to_ai_context(&self, context: &mut AiContext) {`
  - Purpose: 'apply_to_ai_context' copies the instance’s configured AI routing fields into the corresponding 'AiContext' bindings, sets 'audio_translate.target_lang' when translating, and if 'no_ai' is enabled disables all AI bindings by forcing their routing to 'AiRouting::Off'. [crates/gwiki/src/api.rs:186-214]
- `ScopeSelection` (type) component `ScopeSelection [type]` (`b677bde7-6f0b-57e2-9c7d-801d3c764f61`) lines 219-223 [crates/gwiki/src/api.rs:219-223]
  - Signature: `pub enum ScopeSelection {`
  - Purpose: Indexed type `ScopeSelection` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:219-223]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`32390077-9ae2-5c75-8e35-b5b9da9ed946`) lines 225-263 [crates/gwiki/src/api.rs:225-263]
  - Signature: `impl ScopeSelection {`
  - Purpose: 'ScopeSelection' is an enum-backed scope selector that constructs detect/project/topic variants, derives a corresponding 'ScopeIdentity', and exposes typed accessors for project-root and topic-specific state. [crates/gwiki/src/api.rs:225-263]
- `ScopeSelection.detect` (method) component `ScopeSelection.detect [method]` (`5f70a942-b763-51f5-a7e9-5f336511f1c0`) lines 226-228 [crates/gwiki/src/api.rs:226-228]
  - Signature: `pub fn detect() -> Self {`
  - Purpose: 'detect()' returns the 'Self::Detect' variant of the enclosing type. [crates/gwiki/src/api.rs:226-228]
- `ScopeSelection.project` (method) component `ScopeSelection.project [method]` (`b0f015a1-cc14-539b-8473-3c0c028a449a`) lines 230-232 [crates/gwiki/src/api.rs:230-232]
  - Signature: `pub fn project(root: impl Into<PathBuf>) -> Self {`
  - Purpose: Creates and returns a 'Self::ProjectRoot' variant initialized with the provided 'root' path converted into a 'PathBuf'. [crates/gwiki/src/api.rs:230-232]
- `ScopeSelection.topic` (method) component `ScopeSelection.topic [method]` (`eb787157-5d99-5d65-b3ae-62c99c8b2de1`) lines 234-236 [crates/gwiki/src/api.rs:234-236]
  - Signature: `pub fn topic(topic: impl Into<String>) -> Self {`
  - Purpose: Constructs and returns a 'Self::Topic' variant by converting the provided 'topic' argument into a 'String'. [crates/gwiki/src/api.rs:234-236]
- `ScopeSelection.identity` (method) component `ScopeSelection.identity [method]` (`bc293dfc-0cc3-5a77-b7c3-1ca660a8335a`) lines 238-244 [crates/gwiki/src/api.rs:238-244]
  - Signature: `pub fn identity(&self) -> ScopeIdentity {`
  - Purpose: Returns a 'ScopeIdentity' derived from the enum variant, mapping 'Detect' to 'ScopeIdentity::global()', 'ProjectRoot(root)' to 'ScopeIdentity::project(root.display().to_string())', and 'Topic(topic)' to 'ScopeIdentity::topic(topic.clone())'. [crates/gwiki/src/api.rs:238-244]
- `ScopeSelection.is_project` (method) component `ScopeSelection.is_project [method]` (`56bd4cf1-e8c0-581d-ad56-a53c50f930f6`) lines 246-248 [crates/gwiki/src/api.rs:246-248]
  - Signature: `pub fn is_project(&self) -> bool {`
  - Purpose: Returns 'true' when 'self' is the 'ProjectRoot' variant and 'false' for all other variants. [crates/gwiki/src/api.rs:246-248]
- `ScopeSelection.project_root` (method) component `ScopeSelection.project_root [method]` (`1ed96646-f9a1-531a-8432-c06dba94e484`) lines 250-255 [crates/gwiki/src/api.rs:250-255]
  - Signature: `pub fn project_root(&self) -> Option<&Path> {`
  - Purpose: Returns 'Some(&Path)' for the 'ProjectRoot' variant by borrowing the stored path, and 'None' for 'Detect' and 'Topic(_)' variants. [crates/gwiki/src/api.rs:250-255]
- `ScopeSelection.topic_name` (method) component `ScopeSelection.topic_name [method]` (`8996b7ad-6a05-591f-bf33-577389512d0f`) lines 257-262 [crates/gwiki/src/api.rs:257-262]
  - Signature: `pub fn topic_name(&self) -> Option<&str> {`
  - Purpose: Returns 'Some(&str)' with the topic string when 'self' is 'Self::Topic', and 'None' for 'Self::Detect' or 'Self::ProjectRoot(_)'. [crates/gwiki/src/api.rs:257-262]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`27edf9c5-644f-5d11-a462-e449221fdfe1`) lines 265-269 [crates/gwiki/src/api.rs:265-269]
  - Signature: `impl Default for ScopeSelection {`
  - Purpose: 'ScopeSelection' implements 'Default' by delegating to 'ScopeSelection::detect()', so the default value is the result of automatic scope detection. [crates/gwiki/src/api.rs:265-269]
- `ScopeSelection.default` (method) component `ScopeSelection.default [method]` (`37b10230-533d-5aff-b52f-464c0ad4e8b8`) lines 266-268 [crates/gwiki/src/api.rs:266-268]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns 'Self::detect()', making 'default()' construct the type by delegating to its detection logic. [crates/gwiki/src/api.rs:266-268]
- `ScopeKind` (type) component `ScopeKind [type]` (`76c69d03-ebf1-5a52-b8ff-359d52f17662`) lines 273-277 [crates/gwiki/src/api.rs:273-277]
  - Signature: `pub enum ScopeKind {`
  - Purpose: Indexed type `ScopeKind` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:273-277]
- `ScopeKind` (class) component `ScopeKind [class]` (`c3b2628a-b81f-52fc-8c99-d958a7d1a3ba`) lines 279-287 [crates/gwiki/src/api.rs:279-287]
  - Signature: `impl ScopeKind {`
  - Purpose: 'ScopeKind' is an enum-backed type whose 'as_str' method returns the canonical lowercase string representation for each variant: '"global"', '"project"', or '"topic"'. [crates/gwiki/src/api.rs:279-287]
- `ScopeKind.as_str` (method) component `ScopeKind.as_str [method]` (`c0890894-3e6f-51d2-b3e2-8391c88dcd76`) lines 280-286 [crates/gwiki/src/api.rs:280-286]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: Returns the ''static' string literal corresponding to the enum variant, mapping 'Global' to '"global"', 'Project' to '"project"', and 'Topic' to '"topic"'. [crates/gwiki/src/api.rs:280-286]
- `ScopeIdentity` (class) component `ScopeIdentity [class]` (`03df46e5-3012-5b93-87f3-479704b6c831`) lines 290-293 [crates/gwiki/src/api.rs:290-293]
  - Signature: `pub struct ScopeIdentity {`
  - Purpose: 'ScopeIdentity' is a public struct that identifies a scope by pairing a 'ScopeKind' value with a string 'id'. [crates/gwiki/src/api.rs:290-293]
- `ScopeIdentity` (class) component `ScopeIdentity [class]` (`054bd410-b19c-5f98-8f79-f1958c3851d2`) lines 295-316 [crates/gwiki/src/api.rs:295-316]
  - Signature: `impl ScopeIdentity {`
  - Purpose: 'ScopeIdentity' is a small constructor-only type that creates scope identifiers for the 'Global', 'Project', or 'Topic' variants of 'ScopeKind', with a fixed '"default"' id for the global scope and caller-provided string ids for project/topic scopes. [crates/gwiki/src/api.rs:295-316]
- `ScopeIdentity.global` (method) component `ScopeIdentity.global [method]` (`4f2f1ef8-20f6-5218-9710-108501aed06d`) lines 296-301 [crates/gwiki/src/api.rs:296-301]
  - Signature: `pub fn global() -> Self {`
  - Purpose: Constructs and returns a 'Self' instance initialized as the global scope, with 'kind' set to 'ScopeKind::Global' and 'id' set to '"default"'. [crates/gwiki/src/api.rs:296-301]
- `ScopeIdentity.project` (method) component `ScopeIdentity.project [method]` (`321aec9d-e756-53b7-b50f-d134b2ea232e`) lines 303-308 [crates/gwiki/src/api.rs:303-308]
  - Signature: `pub fn project(id: impl Into<String>) -> Self {`
  - Purpose: Constructs and returns a 'Self' value with 'kind' set to 'ScopeKind::Project' and 'id' initialized from the provided 'id' via 'Into<String>'. [crates/gwiki/src/api.rs:303-308]
- `ScopeIdentity.topic` (method) component `ScopeIdentity.topic [method]` (`4451fcdb-96fb-5796-ac7c-a712ff1305c2`) lines 310-315 [crates/gwiki/src/api.rs:310-315]
  - Signature: `pub fn topic(id: impl Into<String>) -> Self {`
  - Purpose: Creates and returns a 'Self' value with 'kind' set to 'ScopeKind::Topic' and 'id' initialized from the provided 'id' after converting it into a 'String'. [crates/gwiki/src/api.rs:310-315]
- `ScopeIdentity` (class) component `ScopeIdentity [class]` (`b7dc03dc-4ff5-5790-8311-22fe7fc08aa0`) lines 318-322 [crates/gwiki/src/api.rs:318-322]
  - Signature: `impl fmt::Display for ScopeIdentity {`
  - Purpose: 'ScopeIdentity' implements 'fmt::Display' by formatting itself as '"<kind>:<id>"', using 'self.kind.as_str()' and 'self.id' separated by a colon. [crates/gwiki/src/api.rs:318-322]
- `ScopeIdentity.fmt` (method) component `ScopeIdentity.fmt [method]` (`e6dc5e72-91af-512a-b281-2f942eeb0319`) lines 319-321 [crates/gwiki/src/api.rs:319-321]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Formats the value by writing '"{kind}:{id}"' to the provided formatter, using 'self.kind.as_str()' and 'self.id'. [crates/gwiki/src/api.rs:319-321]
- `CommandOutcome` (class) component `CommandOutcome [class]` (`9824bed2-2da0-576c-b687-bb73bb121570`) lines 325-329 [crates/gwiki/src/api.rs:325-329]
  - Signature: `pub struct CommandOutcome {`
  - Purpose: 'CommandOutcome' is a Rust struct that aggregates a command’s 'status_messages', its 'result' as a 'CommandResult', and an 'exit_code' stored as 'u8'. [crates/gwiki/src/api.rs:325-329]
- `CommandResult` (class) component `CommandResult [class]` (`db5dfff1-f011-548d-a18f-2c6a625bd860`) lines 332-335 [crates/gwiki/src/api.rs:332-335]
  - Signature: `pub struct CommandResult {`
  - Purpose: 'CommandResult' is a Rust struct that encapsulates a command’s output as both a structured JSON 'payload' ('serde_json::Value') and a plain-text 'text' string. [crates/gwiki/src/api.rs:332-335]
- `scope_selection_constructors_express_allowed_states` (function) component `scope_selection_constructors_express_allowed_states [function]` (`f2af94f9-8936-5037-8272-a0bc7f5442d3`) lines 344-360 [crates/gwiki/src/api.rs:344-360]
  - Signature: `fn scope_selection_constructors_express_allowed_states() {`
  - Purpose: Verifies that 'ScopeSelection::detect()', 'ScopeSelection::project("/repo")', and 'ScopeSelection::topic("ops")' construct the expected allowed states, identities, and accessors for global, project, and topic scopes. [crates/gwiki/src/api.rs:344-360]
- `target_lang_requires_translate_flag` (function) component `target_lang_requires_translate_flag [function]` (`91352f2a-445c-519f-8196-b08384bc6b08`) lines 363-384 [crates/gwiki/src/api.rs:363-384]
  - Signature: `fn target_lang_requires_translate_flag() {`
  - Purpose: Verifies that 'IngestFileOptions::target_lang' is ignored unless 'translate' is 'true', and when both are set the AI context’s 'audio_translate.target_lang' is populated with '"fr"'. [crates/gwiki/src/api.rs:363-384]
- `transcription_routing_applies_to_active_audio_capability` (function) component `transcription_routing_applies_to_active_audio_capability [function]` (`69f90c5f-77a5-53ee-b0da-640f513f1944`) lines 387-417 [crates/gwiki/src/api.rs:387-417]
  - Signature: `fn transcription_routing_applies_to_active_audio_capability() {`
  - Purpose: Verifies that 'IngestFileOptions::transcription_routing' is applied to whichever audio binding is active in 'AiContext' ('audio_transcribe' by default, 'audio_translate' when 'translate: true') without changing the inactive binding’s routing. [crates/gwiki/src/api.rs:387-417]
- `crate_has_no_gcode_dependency` (function) component `crate_has_no_gcode_dependency [function]` (`9eb8e3cc-89f0-5ce7-9ff9-4de462a94255`) lines 420-437 [crates/gwiki/src/api.rs:420-437]
  - Signature: `fn crate_has_no_gcode_dependency() {`
  - Purpose: Reads the crate’s 'Cargo.toml', parses its '[dependencies]' table, and asserts that 'gobby-core' is present while 'gobby-code' is absent. [crates/gwiki/src/api.rs:420-437]

