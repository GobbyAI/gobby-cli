---
title: crates/gwiki/src/session.rs
type: code_file
provenance:
- file: crates/gwiki/src/session.rs
  ranges:
  - 15-18
  - 20-46
  - 21-26
  - 28-33
  - 35-39
  - 41-45
  - 48-57
  - 49-56
  - 60-64
  - 68-76
  - 79-87
  - 89-95
  - '90'
  - 92-94
  - 97-160
  - 98-110
  - 112-139
  - 141-143
  - 145-147
  - 149-151
  - 153-155
  - 157-159
  - 163-170
  - 173-183
  - 186-198
  - 200-317
  - 201-228
  - 230-232
  - 234-293
  - 295-311
  - 313-316
  - 319-338
  - 340-348
  - 350-352
  - 354-361
  - 363-372
  - 374-379
  - 381-388
  - 390-392
  - 394-410
  - 417-450
  - 453-464
  - 467-479
  - 482-490
  - 493-501
  - 504-524
  - 527-548
  - 551-572
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/session.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/session.rs` exposes 48 indexed API symbols.
[crates/gwiki/src/session.rs:15-18]
[crates/gwiki/src/session.rs:20-46]
[crates/gwiki/src/session.rs:21-26]
[crates/gwiki/src/session.rs:28-33]
[crates/gwiki/src/session.rs:35-39]

## API Symbols

- `ResearchScope` (type) component `ResearchScope [type]` (`1808b916-b517-58f9-8b5b-768d4e88c30b`) lines 15-18 [crates/gwiki/src/session.rs:15-18]
  - Signature: `pub enum ResearchScope {`
  - Purpose: Indexed type `ResearchScope` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:15-18]
- `ResearchScope` (class) component `ResearchScope [class]` (`75d3efcd-a3ad-50f9-843d-66063a2ee929`) lines 20-46 [crates/gwiki/src/session.rs:20-46]
  - Signature: `impl ResearchScope {`
  - Purpose: # Summary

ResearchScope is an enum with Project and Topic variants; this implementation provides factory constructors for each variant and common accessors/mutators for their root filesystem paths. [crates/gwiki/src/session.rs:20-46]
- `ResearchScope.project_for_id` (method) component `ResearchScope.project_for_id [method]` (`a88407fe-2279-55c8-bba4-d009159e3066`) lines 21-26 [crates/gwiki/src/session.rs:21-26]
  - Signature: `pub fn project_for_id(project_id: impl Into<String>, root: impl Into<PathBuf>) -> Self {`
  - Purpose: Constructs a `Self::Project` enum variant by converting the provided project ID and root path via their `Into` trait implementations. [crates/gwiki/src/session.rs:21-26]
- `ResearchScope.topic` (method) component `ResearchScope.topic [method]` (`4da0f5af-8b4e-5a85-abe6-4dae1bbcda1c`) lines 28-33 [crates/gwiki/src/session.rs:28-33]
  - Signature: `pub fn topic(name: impl Into<String>, root: impl Into<PathBuf>) -> Self {`
  - Purpose: This method constructs a `Topic` enum variant by converting the provided `name` and `root` parameters into `String` and `PathBuf` types, respectively. [crates/gwiki/src/session.rs:28-33]
- `ResearchScope.root` (method) component `ResearchScope.root [method]` (`7f8ee952-6560-5959-9b6d-a0ea2da9ae1e`) lines 35-39 [crates/gwiki/src/session.rs:35-39]
  - Signature: `pub fn root(&self) -> &Path {`
  - Purpose: This method extracts and returns a reference to the `root` Path field from either the `Project` or `Topic` variant of an enum via pattern matching. [crates/gwiki/src/session.rs:35-39]
- `ResearchScope.set_root` (method) component `ResearchScope.set_root [method]` (`6988bf97-21bc-5f28-89da-32c00f5315c7`) lines 41-45 [crates/gwiki/src/session.rs:41-45]
  - Signature: `fn set_root(&mut self, new_root: PathBuf) {`
  - Purpose: Mutates the `root` field to the provided `PathBuf` value for both `Project` and `Topic` enum variants. [crates/gwiki/src/session.rs:41-45]
- `ResearchScope` (class) component `ResearchScope [class]` (`accee1a5-1d84-5df8-a377-65969a9a010b`) lines 48-57 [crates/gwiki/src/session.rs:48-57]
  - Signature: `impl From<&ResolvedScope> for ResearchScope {`
  - Purpose: Implements the `From` trait to convert a `ResolvedScope` reference into a `ResearchScope` by pattern matching on scope kind and invoking the appropriate constructor (`topic` or `project_for_id`) with the extracted identifier and root path. [crates/gwiki/src/session.rs:48-57]
- `ResearchScope.from` (method) component `ResearchScope.from [method]` (`4b031344-69e0-5a30-bc3d-0ee5e874e65d`) lines 49-56 [crates/gwiki/src/session.rs:49-56]
  - Signature: `fn from(scope: &ResolvedScope) -> Self {`
  - Purpose: Converts a `ResolvedScope` into `Self` by pattern matching on its kind and delegating to either the `topic()` or `project_for_id()` factory method with the extracted identifier and root path. [crates/gwiki/src/session.rs:49-56]
- `DaemonDispatch` (class) component `DaemonDispatch [class]` (`8786f3d3-8940-5edd-870b-d6a09a562e10`) lines 60-64 [crates/gwiki/src/session.rs:60-64]
  - Signature: `pub struct DaemonDispatch {`
  - Purpose: `DaemonDispatch` is a struct that represents a dispatch operation to a daemon service, containing a unique dispatch identifier, the daemon's base URL, and a collection of associated agent run IDs. [crates/gwiki/src/session.rs:60-64]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`848bacba-97d0-545f-9adb-3928884d2393`) lines 68-76 [crates/gwiki/src/session.rs:68-76]
  - Signature: `pub struct ResearchCodeCitation {`
  - Purpose: ResearchCodeCitation is a Rust struct that encapsulates a code citation record comprising a required file path, optional line number and symbol identifiers, and a provenance vector for tracking origin metadata. [crates/gwiki/src/session.rs:68-76]
- `ResearchCodeCitationUnchecked` (class) component `ResearchCodeCitationUnchecked [class]` (`7426a58b-3a12-5b3e-be54-faeb406f847e`) lines 79-87 [crates/gwiki/src/session.rs:79-87]
  - Signature: `struct ResearchCodeCitationUnchecked {`
  - Purpose: An unvalidated citation reference to source code containing a required file path and optional line number, symbol name, and provenance metadata. [crates/gwiki/src/session.rs:79-87]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`197f1d19-d6c7-5f3c-b833-87bdcb0395ca`) lines 89-95 [crates/gwiki/src/session.rs:89-95]
  - Signature: `impl TryFrom<ResearchCodeCitationUnchecked> for ResearchCodeCitation {`
  - Purpose: Provides fallible conversion from `ResearchCodeCitationUnchecked` to `ResearchCodeCitation` by delegating field extraction and validation to the `from_parts` constructor method. [crates/gwiki/src/session.rs:89-95]
- `ResearchCodeCitation.Error` (type) component `ResearchCodeCitation.Error [type]` (`daa59587-004b-5d84-ba7f-d98bab48e98f`) lines 90-90 [crates/gwiki/src/session.rs:90]
  - Signature: `type Error = String;`
  - Purpose: Indexed type `ResearchCodeCitation.Error` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:90]
- `ResearchCodeCitation.try_from` (method) component `ResearchCodeCitation.try_from [method]` (`049f2fce-ca39-5af4-9394-a9ba74703653`) lines 92-94 [crates/gwiki/src/session.rs:92-94]
  - Signature: `fn try_from(value: ResearchCodeCitationUnchecked) -> Result<Self, Self::Error> {`
  - Purpose: Implements `TryFrom` to convert an `ResearchCodeCitationUnchecked` into a validated instance by delegating construction to the `from_parts()` method with the extracted fields. [crates/gwiki/src/session.rs:92-94]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`65efdf7d-27ab-5197-8a87-afeba0172f4c`) lines 97-160 [crates/gwiki/src/session.rs:97-160]
  - Signature: `impl ResearchCodeCitation {`
  - Purpose: # Summary

`ResearchCodeCitation` is a validated struct that stores code location references (file path, optional line number and symbol) with mandatory non-empty provenance metadata, enforcing path security by rejecting parent directory traversal attempts. [crates/gwiki/src/session.rs:97-160]
- `ResearchCodeCitation.new` (method) component `ResearchCodeCitation.new [method]` (`d9897627-5d63-57a1-905b-41701b00bc3f`) lines 98-110 [crates/gwiki/src/session.rs:98-110]
  - Signature: `pub fn new(`
  - Purpose: Creates a new instance from a file path, optional line number, optional symbol, and provenance vector by delegating to `from_parts`, converting any validation errors to `WikiError::InvalidInput`. [crates/gwiki/src/session.rs:98-110]
- `ResearchCodeCitation.from_parts` (method) component `ResearchCodeCitation.from_parts [method]` (`8c3d8521-6753-5fdf-82ec-360def624ce9`) lines 112-139 [crates/gwiki/src/session.rs:112-139]
  - Signature: `fn from_parts(`
  - Purpose: Constructs a code citation instance after validating that the file path is non-empty with no parent directory traversal components and that the provenance vector contains at least one non-empty entry. [crates/gwiki/src/session.rs:112-139]
- `ResearchCodeCitation.file` (method) component `ResearchCodeCitation.file [method]` (`04bc8c33-97a7-58df-940d-1b2e2db7e4da`) lines 141-143 [crates/gwiki/src/session.rs:141-143]
  - Signature: `pub fn file(&self) -> &str {`
  - Purpose: Returns an immutable reference to the struct's internal `file` field as a string slice. [crates/gwiki/src/session.rs:141-143]
- `ResearchCodeCitation.line` (method) component `ResearchCodeCitation.line [method]` (`a2dc0b6f-486a-574b-9c15-8d5ac00566c8`) lines 145-147 [crates/gwiki/src/session.rs:145-147]
  - Signature: `pub fn line(&self) -> Option<usize> {`
  - Purpose: This method returns an optional unsigned integer (`Option<usize>`) representing the line number, or `None` if not set. [crates/gwiki/src/session.rs:145-147]
- `ResearchCodeCitation.symbol` (method) component `ResearchCodeCitation.symbol [method]` (`2097b105-c186-5a4a-a38e-ad07ec5aaaf6`) lines 149-151 [crates/gwiki/src/session.rs:149-151]
  - Signature: `pub fn symbol(&self) -> Option<&str> {`
  - Purpose: Returns an optional borrowed string reference to the internal symbol field, converting from `Option<String>` to `Option<&str>` via deref coercion. [crates/gwiki/src/session.rs:149-151]
- `ResearchCodeCitation.provenance` (method) component `ResearchCodeCitation.provenance [method]` (`086fdf1a-8fbe-5dac-ba71-e8d6475573f7`) lines 153-155 [crates/gwiki/src/session.rs:153-155]
  - Signature: `pub fn provenance(&self) -> &[String] {`
  - Purpose: Returns an immutable slice reference to the provenance string vector. [crates/gwiki/src/session.rs:153-155]
- `ResearchCodeCitation.provenance_mut` (method) component `ResearchCodeCitation.provenance_mut [method]` (`d4c88106-7471-5aa5-b2b7-ee4392274b8a`) lines 157-159 [crates/gwiki/src/session.rs:157-159]
  - Signature: `pub(crate) fn provenance_mut(&mut self) -> &mut Vec<String> {`
  - Purpose: Provides mutable access to the internal `provenance` field, a vector of strings, allowing callers to modify its contents. [crates/gwiki/src/session.rs:157-159]
- `AcceptedResearchNote` (class) component `AcceptedResearchNote [class]` (`c930b788-7c22-58aa-b133-8372aff6a016`) lines 163-170 [crates/gwiki/src/session.rs:163-170]
  - Signature: `pub struct AcceptedResearchNote {`
  - Purpose: `AcceptedResearchNote` is a serializable data structure that encapsulates a research note with its title, file path, optional code citations, and optional degradation status. [crates/gwiki/src/session.rs:163-170]
- `CompileState` (class) component `CompileState [class]` (`56415b0e-6f1c-5d8a-9893-43aa6480c021`) lines 173-183 [crates/gwiki/src/session.rs:173-183]
  - Signature: `pub struct CompileState {`
  - Purpose: # CompileState Summary

A state structure managing a document compilation operation that tracks selected note sources, citations, and identified conflicts or evidence gaps. [crates/gwiki/src/session.rs:173-183]
- `ResearchSession` (class) component `ResearchSession [class]` (`e27de505-c6f0-5680-8c3f-96d75cf86826`) lines 186-198 [crates/gwiki/src/session.rs:186-198]
  - Signature: `pub struct ResearchSession {`
  - Purpose: ResearchSession encapsulates a multi-agent research task with a question, scoped constraints on sources, optional daemon dispatcher integration, and a collection of accepted research notes. [crates/gwiki/src/session.rs:186-198]
- `ResearchSession` (class) component `ResearchSession [class]` (`574300e3-bf43-5b06-9bd7-480009899e8c`) lines 200-317 [crates/gwiki/src/session.rs:200-317]
  - Signature: `impl ResearchSession {`
  - Purpose: ResearchSession manages a multi-agent research session with configurable scope and source constraints, persisting session state atomically to JSON checkpoints. [crates/gwiki/src/session.rs:200-317]
- `ResearchSession.new` (method) component `ResearchSession.new [method]` (`e1fc863b-ec9b-5c0a-ae6b-02f9a3e262e6`) lines 201-228 [crates/gwiki/src/session.rs:201-228]
  - Signature: `pub fn new(`
  - Purpose: # Summary

Constructs a new research session instance after validating `agent_count > 0` and initializing a unique `session_id` and `research_prompt` from the provided question, scope, and constraints. [crates/gwiki/src/session.rs:201-228]
- `ResearchSession.checkpoint_path` (method) component `ResearchSession.checkpoint_path [method]` (`53d9d661-bce3-5ae1-88e6-6e69f9071b61`) lines 230-232 [crates/gwiki/src/session.rs:230-232]
  - Signature: `pub fn checkpoint_path(vault_root: &Path) -> PathBuf {`
  - Purpose: `checkpoint_path` constructs and returns a `PathBuf` for the research session checkpoint file located at `<vault_root>/.gwiki/research-session.json`. [crates/gwiki/src/session.rs:230-232]
- `ResearchSession.save_checkpoint` (method) component `ResearchSession.save_checkpoint [method]` (`35e9aaaa-f348-57c2-bf51-f58f37cbe958`) lines 234-293 [crates/gwiki/src/session.rs:234-293]
  - Signature: `pub fn save_checkpoint(&self) -> Result<(), WikiError> {`
  - Purpose: Atomically writes the instance state to a JSON checkpoint file using temporary file creation and atomic rename to ensure crash safety and durability. [crates/gwiki/src/session.rs:234-293]
- `ResearchSession.load_checkpoint` (method) component `ResearchSession.load_checkpoint [method]` (`6bd5e793-532a-5651-9527-0a8d65729887`) lines 295-311 [crates/gwiki/src/session.rs:295-311]
  - Signature: `pub fn load_checkpoint(vault_root: &Path) -> Result<Self, WikiError> {`
  - Purpose: Deserializes a checkpoint from a JSON file at a derived path, validates and normalizes its scope root relative to the provided vault root, then returns the reconstructed session. [crates/gwiki/src/session.rs:295-311]
- `ResearchSession.record_compile_state` (method) component `ResearchSession.record_compile_state [method]` (`0b55ff06-a73f-5ddd-9cb2-171e4e1e1cd1`) lines 313-316 [crates/gwiki/src/session.rs:313-316]
  - Signature: `pub fn record_compile_state(&mut self, state: CompileState) -> Result<(), WikiError> {`
  - Purpose: Stores the provided `CompileState` in the instance field and persists it by saving a checkpoint, returning a `Result` that may contain a `WikiError`. [crates/gwiki/src/session.rs:313-316]
- `validate_checkpoint_scope_root` (function) component `validate_checkpoint_scope_root [function]` (`3e4d94a5-a3ca-5cc2-9a22-3122bf9ebb76`) lines 319-338 [crates/gwiki/src/session.rs:319-338]
  - Signature: `fn validate_checkpoint_scope_root(`
  - Purpose: Validates that a loaded research checkpoint's scope root matches the expected scope root by comparing normalized paths, returning the expected root PathBuf on success or an InvalidScope WikiError if mismatched. [crates/gwiki/src/session.rs:319-338]
- `legacy_project_vault_root_matches` (function) component `legacy_project_vault_root_matches [function]` (`89f9556a-536e-5f2a-b25d-8f29a2a5b0d0`) lines 340-348 [crates/gwiki/src/session.rs:340-348]
  - Signature: `fn legacy_project_vault_root_matches(expected_root: &Path, loaded_root: &Path) -> bool {`
  - Purpose: This function validates that `loaded_root` is a legacy project vault relative root and that `expected_root` canonically matches the `.gobby/wiki` subdirectory of its parent project. [crates/gwiki/src/session.rs:340-348]
- `is_legacy_project_vault_relative_root` (function) component `is_legacy_project_vault_relative_root [function]` (`af9496f8-852e-5e6a-ae23-70c0b0f625db`) lines 350-352 [crates/gwiki/src/session.rs:350-352]
  - Signature: `fn is_legacy_project_vault_relative_root(path: &Path) -> bool {`
  - Purpose: Returns true if the given path exactly matches the relative path `.gobby/wiki`, identifying a legacy project vault root. [crates/gwiki/src/session.rs:350-352]
- `project_root_for_vault` (function) component `project_root_for_vault [function]` (`2f0d02dc-7273-5695-b289-a664f85821da`) lines 354-361 [crates/gwiki/src/session.rs:354-361]
  - Signature: `fn project_root_for_vault(vault_root: &Path) -> Option<&Path> {`
  - Purpose: This function returns the project root directory (the grandparent of `vault_root`) if the path matches the `.gobby/wiki/` directory structure pattern, otherwise returns `None`. [crates/gwiki/src/session.rs:354-361]
- `comparable_path` (function) component `comparable_path [function]` (`81087daa-d83f-55ec-b08e-2ef2588e9d05`) lines 363-372 [crates/gwiki/src/session.rs:363-372]
  - Signature: `fn comparable_path(path: &Path, relative_base: Option<&Path>) -> PathBuf {`
  - Purpose: Canonicalizes and resolves a path relative to an optional base path, with fallback to the non-canonical form on canonicalization failure. [crates/gwiki/src/session.rs:363-372]
- `checkpoint_vault_root` (function) component `checkpoint_vault_root [function]` (`546f00e3-e72d-50d0-bb66-0fbefa38c9c7`) lines 374-379 [crates/gwiki/src/session.rs:374-379]
  - Signature: `fn checkpoint_vault_root(checkpoint_path: &Path) -> Option<PathBuf> {`
  - Purpose: Returns the grandparent directory (vault root) of the given checkpoint path as an owned `PathBuf`, or `None` if either parent directory is absent. [crates/gwiki/src/session.rs:374-379]
- `new_session_id` (function) component `new_session_id [function]` (`4b5e1218-328f-55a7-8a84-a0e16cc2c2b0`) lines 381-388 [crates/gwiki/src/session.rs:381-388]
  - Signature: `fn new_session_id() -> Result<String, WikiError> {`
  - Purpose: Generates a unique session identifier by concatenating the string "research-", the current Unix timestamp in milliseconds, and the first 8 characters of a randomly generated UUID v4. [crates/gwiki/src/session.rs:381-388]
- `unix_timestamp_ms` (function) component `unix_timestamp_ms [function]` (`e6e9e567-964d-568c-a370-0b8f62bbd9a3`) lines 390-392 [crates/gwiki/src/session.rs:390-392]
  - Signature: `fn unix_timestamp_ms() -> Result<u64, WikiError> {`
  - Purpose: Returns the current Unix timestamp in milliseconds wrapped in `Result<u64, WikiError>`. [crates/gwiki/src/session.rs:390-392]
- `research_prompt` (function) component `research_prompt [function]` (`1f4d1fa8-d1ce-5d9e-b192-98812bcd896a`) lines 394-410 [crates/gwiki/src/session.rs:394-410]
  - Signature: `pub(crate) fn research_prompt(`
  - Purpose: Constructs a formatted research prompt string containing a research question, agent count, and optional source constraints formatted as bullet points. [crates/gwiki/src/session.rs:394-410]
- `compile_state_is_resumable` (function) component `compile_state_is_resumable [function]` (`2ea97082-aa4f-5a34-92fe-7c80fbb7ee76`) lines 417-450 [crates/gwiki/src/session.rs:417-450]
  - Signature: `fn compile_state_is_resumable() {`
  - Purpose: Tests that a `ResearchSession` correctly persists `CompileState` to a checkpoint file and successfully restores all metadata fields upon reload. [crates/gwiki/src/session.rs:417-450]
- `research_code_citation_rejects_empty_provenance` (function) component `research_code_citation_rejects_empty_provenance [function]` (`161f5e95-0840-532c-9278-b362a02c0132`) lines 453-464 [crates/gwiki/src/session.rs:453-464]
  - Signature: `fn research_code_citation_rejects_empty_provenance() {`
  - Purpose: Unit test asserting that `ResearchCodeCitation::new()` rejects construction with empty provenance by returning a `WikiError::InvalidInput` with field "code_citations". [crates/gwiki/src/session.rs:453-464]
- `research_code_citation_rejects_parent_path_components` (function) component `research_code_citation_rejects_parent_path_components [function]` (`8827ef73-02e5-539c-93df-6cb917fc92a6`) lines 467-479 [crates/gwiki/src/session.rs:467-479]
  - Signature: `fn research_code_citation_rejects_parent_path_components() {`
  - Purpose: This test verifies that `ResearchCodeCitation::new()` rejects file paths containing parent directory traversal sequences (`../`) and returns a `WikiError::InvalidInput` validation error. [crates/gwiki/src/session.rs:467-479]
- `research_code_citation_deserialization_rejects_empty_provenance` (function) component `research_code_citation_deserialization_rejects_empty_provenance [function]` (`6db71cb0-0cfa-5f5b-b28d-99e9eccab455`) lines 482-490 [crates/gwiki/src/session.rs:482-490]
  - Signature: `fn research_code_citation_deserialization_rejects_empty_provenance() {`
  - Purpose: This unit test verifies that deserializing a `ResearchCodeCitation` struct with an empty provenance array fails and produces an error message containing "provenance". [crates/gwiki/src/session.rs:482-490]
- `research_code_citation_deserialization_rejects_parent_path_components` (function) component `research_code_citation_deserialization_rejects_parent_path_components [function]` (`28a9827d-4b48-5747-a5de-94b98c9ef621`) lines 493-501 [crates/gwiki/src/session.rs:493-501]
  - Signature: `fn research_code_citation_deserialization_rejects_parent_path_components() {`
  - Purpose: This test verifies that `ResearchCodeCitation` deserialization validation rejects file paths containing parent directory traversal components (`..`) and confirms the error message identifies them. [crates/gwiki/src/session.rs:493-501]
- `load_checkpoint_migrates_legacy_project_vault_relative_scope_root` (function) component `load_checkpoint_migrates_legacy_project_vault_relative_scope_root [function]` (`03fbd64c-38d1-56b2-a345-b20e66cb6920`) lines 504-524 [crates/gwiki/src/session.rs:504-524]
  - Signature: `fn load_checkpoint_migrates_legacy_project_vault_relative_scope_root() {`
  - Purpose: This test verifies that deserializing a checkpoint with a legacy relative project vault path correctly migrates and canonicalizes the scope root to its absolute path. [crates/gwiki/src/session.rs:504-524]
- `load_checkpoint_rejects_mismatched_scope_root` (function) component `load_checkpoint_rejects_mismatched_scope_root [function]` (`f994322b-2630-5cef-9aab-970f6b862e80`) lines 527-548 [crates/gwiki/src/session.rs:527-548]
  - Signature: `fn load_checkpoint_rejects_mismatched_scope_root() {`
  - Purpose: This test verifies that `ResearchSession::load_checkpoint()` rejects a checkpoint when the serialized scope root directory differs from the checkpoint's storage location, returning an `InvalidScope` error. [crates/gwiki/src/session.rs:527-548]
- `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault` (function) component `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault [function]` (`75054b2a-a565-5606-9206-3a03d234724e`) lines 551-572 [crates/gwiki/src/session.rs:551-572]
  - Signature: `fn load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault() {`
  - Purpose: Tests that `ResearchSession::load_checkpoint` normalizes a relative scope root against the checkpoint vault directory to its absolute canonical path. [crates/gwiki/src/session.rs:551-572]

