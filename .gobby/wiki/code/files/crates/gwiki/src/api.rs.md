---
title: crates/gwiki/src/api.rs
type: code_file
provenance:
- file: crates/gwiki/src/api.rs
  ranges:
  - 11-121
  - 124-127
  - 130-144
  - 147-149
  - 151-154
  - 156-162
  - 166-174
  - 177-182
  - 184-214
  - 218-222
  - 224-262
  - 264-268
  - 272-276
  - 278-286
  - 289-292
  - 294-315
  - 317-321
  - 324-328
  - 331-334
  - 343-359
  - 362-383
  - 386-416
  - 419-436
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/api.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the gwiki command API: a `Command` enum for all supported CLI actions, plus the option and result types those actions use. It also centralizes scope modeling with `ScopeSelection`, `ScopeKind`, and `ScopeIdentity`, giving constructors, accessors, and string/display conversions so commands can carry either detected, project, or topic scope consistently.

The other structs support configuration and output wiring: `SetupOptions` and `IngestFileOptions` control backend setup and AI-routing behavior, `BenchmarkOptions` sets retrieval benchmark parameters, `ReviewReportOptions` configures report generation, and `CommandOutcome`/`CommandResult` represent execution results. The tests at the end verify the scope constructors, AI option routing, and crate dependency expectations.
[crates/gwiki/src/api.rs:11-121]
[crates/gwiki/src/api.rs:124-127]
[crates/gwiki/src/api.rs:130-144]
[crates/gwiki/src/api.rs:147-149]
[crates/gwiki/src/api.rs:151-154]

## API Symbols

- `Command` (type) component `Command [type]` (`410214b3-aa48-5813-b83e-3e668eb3249c`) lines 11-121 [crates/gwiki/src/api.rs:11-121]
  - Signature: `pub enum Command {`
  - Purpose: Indexed type `Command` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:11-121]
- `ReadTarget` (type) component `ReadTarget [type]` (`67e095dd-d30e-53ea-a3a7-649f4587514e`) lines 124-127 [crates/gwiki/src/api.rs:124-127]
  - Signature: `pub enum ReadTarget {`
  - Purpose: Indexed type `ReadTarget` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:124-127]
- `SetupOptions` (class) component `SetupOptions [class]` (`fb1d5625-577a-5626-b4b6-1aef419dd499`) lines 130-144 [crates/gwiki/src/api.rs:130-144]
  - Signature: `pub struct SetupOptions {`
  - Purpose: 'SetupOptions' is a configuration struct containing optional parameters for initializing application backends including database connectivity, FalkorDB graph database, Qdrant vector store, and embedding provider services. [crates/gwiki/src/api.rs:130-144]
- `BenchmarkOptions` (class) component `BenchmarkOptions [class]` (`1644b539-deeb-5108-8364-309b17bd094f`) lines 147-149 [crates/gwiki/src/api.rs:147-149]
  - Signature: `pub struct BenchmarkOptions {`
  - Purpose: 'BenchmarkOptions' is a public Rust struct that encapsulates a single 'usize' field specifying the number of retrieval candidates for a benchmarking operation. [crates/gwiki/src/api.rs:147-149]
- `BenchmarkOptions` (class) component `BenchmarkOptions [class]` (`c8518de4-17f2-55be-b666-56e9019f00c7`) lines 151-154 [crates/gwiki/src/api.rs:151-154]
  - Signature: `impl BenchmarkOptions {`
  - Purpose: BenchmarkOptions defines a public constant 'DEFAULT_RETRIEVAL_CANDIDATES' that aliases 'DEFAULT_RETRIEVAL_PRECISION_CANDIDATES' from the crate's benchmark module. [crates/gwiki/src/api.rs:151-154]
- `BenchmarkOptions` (class) component `BenchmarkOptions [class]` (`eb850b0c-5f6f-5d5e-b59f-76328ddd8b31`) lines 156-162 [crates/gwiki/src/api.rs:156-162]
  - Signature: `impl Default for BenchmarkOptions {`
  - Purpose: This Default trait implementation initializes BenchmarkOptions with the 'retrieval_candidates' field set to a predefined constant value. [crates/gwiki/src/api.rs:156-162]
- `BenchmarkOptions.default` (method) component `BenchmarkOptions.default [method]` (`789ee749-ac45-5bc3-858e-529d8fb19dc6`) lines 157-161 [crates/gwiki/src/api.rs:157-161]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a default instance of 'Self' with the 'retrieval_candidates' field initialized to the associated constant 'DEFAULT_RETRIEVAL_CANDIDATES'. [crates/gwiki/src/api.rs:157-161]
- `IngestFileOptions` (class) component `IngestFileOptions [class]` (`a536e535-0ec3-520f-aeaa-b769e180f989`) lines 166-174 [crates/gwiki/src/api.rs:166-174]
  - Signature: `pub struct IngestFileOptions {`
  - Purpose: IngestFileOptions is a configuration struct that controls AI processing toggles, language translation settings, video frame extraction interval, and task-specific AI service routing (transcription, vision, text) for file ingestion operations. [crates/gwiki/src/api.rs:166-174]
- `ReviewReportOptions` (class) component `ReviewReportOptions [class]` (`4423e5a3-60b5-517f-bb00-d147f308e32d`) lines 177-182 [crates/gwiki/src/api.rs:177-182]
  - Signature: `pub struct ReviewReportOptions {`
  - Purpose: 'ReviewReportOptions' is a configuration struct that encapsulates the parameters needed to generate a review report, including a list of files and symbols to review, an optional diff file path, and an output destination. [crates/gwiki/src/api.rs:177-182]
- `IngestFileOptions` (class) component `IngestFileOptions [class]` (`776cae82-8455-520f-a0c7-063119de1077`) lines 184-214 [crates/gwiki/src/api.rs:184-214]
  - Signature: `impl IngestFileOptions {`
  - Purpose: 'IngestFileOptions::apply_to_ai_context' configures AI feature routing (audio transcription/translation, vision extraction, text generation) in an 'AiContext' based on option flags, or disables all AI processing if 'no_ai' is set. [crates/gwiki/src/api.rs:184-214]
- `IngestFileOptions.apply_to_ai_context` (method) component `IngestFileOptions.apply_to_ai_context [method]` (`7c4bd883-0123-5074-bdff-f4728fbc357a`) lines 185-213 [crates/gwiki/src/api.rs:185-213]
  - Signature: `pub fn apply_to_ai_context(&self, context: &mut AiContext) {`
  - Purpose: Conditionally applies routing and target language configurations to AI service bindings in the context, or disables all AI services based on the 'no_ai' flag. [crates/gwiki/src/api.rs:185-213]
- `ScopeSelection` (type) component `ScopeSelection [type]` (`aef2e4b8-ca21-5280-a477-6c88c39fe70e`) lines 218-222 [crates/gwiki/src/api.rs:218-222]
  - Signature: `pub enum ScopeSelection {`
  - Purpose: Indexed type `ScopeSelection` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:218-222]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`26876ee0-74f6-5038-b692-7684b7a23429`) lines 224-262 [crates/gwiki/src/api.rs:224-262]
  - Signature: `impl ScopeSelection {`
  - Purpose: ScopeSelection provides factory constructors and pattern-matched accessors for a three-variant enum supporting automatic detection, project-root-based, or topic-based scoping modes. [crates/gwiki/src/api.rs:224-262]
- `ScopeSelection.detect` (method) component `ScopeSelection.detect [method]` (`08dbb894-f305-5266-bed1-c43cdfd8b2f1`) lines 225-227 [crates/gwiki/src/api.rs:225-227]
  - Signature: `pub fn detect() -> Self {`
  - Purpose: Returns the 'Detect' enum variant of the enclosing type. [crates/gwiki/src/api.rs:225-227]
- `ScopeSelection.project` (method) component `ScopeSelection.project [method]` (`e6a2e082-d49b-57ee-a465-081cb7595ffd`) lines 229-231 [crates/gwiki/src/api.rs:229-231]
  - Signature: `pub fn project(root: impl Into<PathBuf>) -> Self {`
  - Purpose: Constructs and returns a 'Self::ProjectRoot' enum variant by converting the provided root argument into a 'PathBuf'. [crates/gwiki/src/api.rs:229-231]
- `ScopeSelection.topic` (method) component `ScopeSelection.topic [method]` (`f3b69bcf-2bde-5c50-aacb-9707ca43bc62`) lines 233-235 [crates/gwiki/src/api.rs:233-235]
  - Signature: `pub fn topic(topic: impl Into<String>) -> Self {`
  - Purpose: Constructs a 'Self::Topic' enum variant by converting the generic parameter into a 'String' via the 'Into' trait. [crates/gwiki/src/api.rs:233-235]
- `ScopeSelection.identity` (method) component `ScopeSelection.identity [method]` (`1a48ac14-1fe8-51b0-acac-a2b61ab4f6f3`) lines 237-243 [crates/gwiki/src/api.rs:237-243]
  - Signature: `pub fn identity(&self) -> ScopeIdentity {`
  - Purpose: Maps the enum variant into its corresponding 'ScopeIdentity' representation: 'Detect' to global scope, 'ProjectRoot' to project-scoped with stringified path, and 'Topic' to topic-scoped identity. [crates/gwiki/src/api.rs:237-243]
- `ScopeSelection.is_project` (method) component `ScopeSelection.is_project [method]` (`408e5c75-0f02-503e-afc6-0463e13ca519`) lines 245-247 [crates/gwiki/src/api.rs:245-247]
  - Signature: `pub fn is_project(&self) -> bool {`
  - Purpose: Returns a boolean indicating whether the enum instance is a 'ProjectRoot' variant. [crates/gwiki/src/api.rs:245-247]
- `ScopeSelection.project_root` (method) component `ScopeSelection.project_root [method]` (`53acedf8-a6fc-5e5f-91d9-966ad6b26f59`) lines 249-254 [crates/gwiki/src/api.rs:249-254]
  - Signature: `pub fn project_root(&self) -> Option<&Path> {`
  - Purpose: Returns a path reference if 'self' is the 'ProjectRoot' variant, otherwise returns 'None'. [crates/gwiki/src/api.rs:249-254]
- `ScopeSelection.topic_name` (method) component `ScopeSelection.topic_name [method]` (`8db351e8-a52c-51fb-9c6d-c85626420409`) lines 256-261 [crates/gwiki/src/api.rs:256-261]
  - Signature: `pub fn topic_name(&self) -> Option<&str> {`
  - Purpose: Returns an optional string slice reference from the enum's 'Topic' variant, or 'None' for 'Detect' and 'ProjectRoot' variants. [crates/gwiki/src/api.rs:256-261]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`fbbb4c2b-16c4-5d67-9619-45f93a4af4b1`) lines 264-268 [crates/gwiki/src/api.rs:264-268]
  - Signature: `impl Default for ScopeSelection {`
  - Purpose: 'ScopeSelection' implements the 'Default' trait by delegating to its 'detect()' method. [crates/gwiki/src/api.rs:264-268]
- `ScopeSelection.default` (method) component `ScopeSelection.default [method]` (`b74db015-df9d-5865-97a2-bb224408deb0`) lines 265-267 [crates/gwiki/src/api.rs:265-267]
  - Signature: `fn default() -> Self {`
  - Purpose: The 'default()' method provides a default instance of 'Self' by delegating to the 'detect()' associated function. [crates/gwiki/src/api.rs:265-267]
- `ScopeKind` (type) component `ScopeKind [type]` (`59f7cb4b-2b86-5bcf-aa87-43e8f9013e64`) lines 272-276 [crates/gwiki/src/api.rs:272-276]
  - Signature: `pub enum ScopeKind {`
  - Purpose: Indexed type `ScopeKind` in `crates/gwiki/src/api.rs`. [crates/gwiki/src/api.rs:272-276]
- `ScopeKind` (class) component `ScopeKind [class]` (`5ecd8f27-5724-5213-964a-21635d6a0144`) lines 278-286 [crates/gwiki/src/api.rs:278-286]
  - Signature: `impl ScopeKind {`
  - Purpose: Implements a method that converts 'ScopeKind' enum variants into their static string representations via exhaustive pattern matching. [crates/gwiki/src/api.rs:278-286]
- `ScopeKind.as_str` (method) component `ScopeKind.as_str [method]` (`7118f8e6-dd0c-5a43-8445-21ab0f99d529`) lines 279-285 [crates/gwiki/src/api.rs:279-285]
  - Signature: `pub fn as_str(self) -> &'static str {`
  - Purpose: This method consumes 'self' and returns the static string representation of the enum variant via exhaustive pattern matching. [crates/gwiki/src/api.rs:279-285]
- `ScopeIdentity` (class) component `ScopeIdentity [class]` (`a29cc12c-69a5-59fd-a40f-6cc9c7083afa`) lines 289-292 [crates/gwiki/src/api.rs:289-292]
  - Signature: `pub struct ScopeIdentity {`
  - Purpose: 'ScopeIdentity' is a struct that combines a 'ScopeKind' discriminator with a 'String' identifier to uniquely identify a scope. [crates/gwiki/src/api.rs:289-292]
- `ScopeIdentity` (class) component `ScopeIdentity [class]` (`36296235-7b99-5a23-a466-fa82cc5b0406`) lines 294-315 [crates/gwiki/src/api.rs:294-315]
  - Signature: `impl ScopeIdentity {`
  - Purpose: ScopeIdentity impl block provides factory methods to construct Global, Project, and Topic-scoped identities, each with an associated string identifier. [crates/gwiki/src/api.rs:294-315]
- `ScopeIdentity.global` (method) component `ScopeIdentity.global [method]` (`f8f16407-87ff-54e4-b747-0afeb5d767e3`) lines 295-300 [crates/gwiki/src/api.rs:295-300]
  - Signature: `pub fn global() -> Self {`
  - Purpose: This method constructs and returns a new scope instance with 'ScopeKind::Global' and an identifier of '"default"'. [crates/gwiki/src/api.rs:295-300]
- `ScopeIdentity.project` (method) component `ScopeIdentity.project [method]` (`582b75ae-cd5e-5c5e-8e18-086e73364942`) lines 302-307 [crates/gwiki/src/api.rs:302-307]
  - Signature: `pub fn project(id: impl Into<String>) -> Self {`
  - Purpose: Creates a new Self instance with 'kind' set to 'ScopeKind::Project' and 'id' initialized from the provided 'Into<String>' parameter. [crates/gwiki/src/api.rs:302-307]
- `ScopeIdentity.topic` (method) component `ScopeIdentity.topic [method]` (`ed30d4c0-3875-5ca3-9403-27486249532d`) lines 309-314 [crates/gwiki/src/api.rs:309-314]
  - Signature: `pub fn topic(id: impl Into<String>) -> Self {`
  - Purpose: Constructs a new instance with 'ScopeKind::Topic' and the provided generic 'id' parameter converted to 'String'. [crates/gwiki/src/api.rs:309-314]
- `ScopeIdentity` (class) component `ScopeIdentity [class]` (`18cd64e4-9318-5eb6-b49b-70e887aefcf7`) lines 317-321 [crates/gwiki/src/api.rs:317-321]
  - Signature: `impl fmt::Display for ScopeIdentity {`
  - Purpose: Implements the 'Display' trait for 'ScopeIdentity', formatting instances as a colon-separated string of the scope kind and id. [crates/gwiki/src/api.rs:317-321]
- `ScopeIdentity.fmt` (method) component `ScopeIdentity.fmt [method]` (`db8b26be-c852-537a-8746-c3aab8b8fef7`) lines 318-320 [crates/gwiki/src/api.rs:318-320]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: This method implements the 'Display' (or 'Debug') trait by formatting the object as a colon-separated string of its 'kind' field (converted to string) and 'id' field. [crates/gwiki/src/api.rs:318-320]
- `CommandOutcome` (class) component `CommandOutcome [class]` (`1413b515-b5b1-5116-b765-2b262d1f416a`) lines 324-328 [crates/gwiki/src/api.rs:324-328]
  - Signature: `pub struct CommandOutcome {`
  - Purpose: 'CommandOutcome' is a struct that encapsulates a command's execution result, comprising a vector of status messages, a 'CommandResult' value, and a numeric exit code. [crates/gwiki/src/api.rs:324-328]
- `CommandResult` (class) component `CommandResult [class]` (`c0a77f88-c718-5ffb-ace6-a158956e885a`) lines 331-334 [crates/gwiki/src/api.rs:331-334]
  - Signature: `pub struct CommandResult {`
  - Purpose: 'CommandResult' is a struct that encapsulates command output with two fields: an untyped JSON payload and a text string representation. [crates/gwiki/src/api.rs:331-334]
- `scope_selection_constructors_express_allowed_states` (function) component `scope_selection_constructors_express_allowed_states [function]` (`db6b20fb-cda3-5672-95f6-b20446aaae4a`) lines 343-359 [crates/gwiki/src/api.rs:343-359]
  - Signature: `fn scope_selection_constructors_express_allowed_states() {`
  - Purpose: This test function verifies that the three 'ScopeSelection' constructors ('detect', 'project', and 'topic') correctly initialize distinct scope types with their respective identifying properties and state behaviors. [crates/gwiki/src/api.rs:343-359]
- `target_lang_requires_translate_flag` (function) component `target_lang_requires_translate_flag [function]` (`9a622aca-9ee1-5d73-b8a7-3fe1ccd12615`) lines 362-383 [crates/gwiki/src/api.rs:362-383]
  - Signature: `fn target_lang_requires_translate_flag() {`
  - Purpose: Tests that setting a 'target_lang' in 'IngestFileOptions' only populates the audio translation context's target language when the 'translate' flag is explicitly enabled. [crates/gwiki/src/api.rs:362-383]
- `transcription_routing_applies_to_active_audio_capability` (function) component `transcription_routing_applies_to_active_audio_capability [function]` (`cfa649d0-3af3-583b-a299-a4ce1f64b0a3`) lines 386-416 [crates/gwiki/src/api.rs:386-416]
  - Signature: `fn transcription_routing_applies_to_active_audio_capability() {`
  - Purpose: This test verifies that 'IngestFileOptions.transcription_routing' applies to the currently active audio capability (either 'audio_transcribe' or 'audio_translate' depending on which processing mode is enabled). [crates/gwiki/src/api.rs:386-416]
- `crate_has_no_gcode_dependency` (function) component `crate_has_no_gcode_dependency [function]` (`a8c990fa-2870-54fe-ba8b-24f5f38eaa44`) lines 419-436 [crates/gwiki/src/api.rs:419-436]
  - Signature: `fn crate_has_no_gcode_dependency() {`
  - Purpose: This test function validates that the containing crate's Cargo.toml manifest declares gobby-core as a dependency while explicitly excluding gobby-code. [crates/gwiki/src/api.rs:419-436]

