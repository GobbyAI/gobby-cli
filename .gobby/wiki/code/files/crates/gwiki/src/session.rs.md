---
title: crates/gwiki/src/session.rs
type: code_file
provenance:
- file: crates/gwiki/src/session.rs
  ranges:
  - 15-18
  - 20-46
  - 48-57
  - 60-64
  - 68-76
  - 79-87
  - 89-95
  - 97-156
  - 159-166
  - 169-179
  - 182-194
  - 196-313
  - 315-334
  - 336-345
  - 347-352
  - 354-361
  - 363-365
  - 367-383
  - 390-423
  - 426-437
  - 440-452
  - 455-463
  - 466-474
  - 477-502
  - 505-526
  - 529-550
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/session.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file defines the serialized session state and helper types for gwiki’s research workflow. It models research scope as either a project or topic with a shared root path, validates and normalizes code citations, and stores dispatch, accepted notes, and compile-state metadata for a research run. `ResearchSession` ties these pieces together by generating a new session with a prompt, persisting checkpoints atomically under `.gwiki/research-session.json`, and restoring them with scope-root validation against the vault root.
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
  - Purpose: 'ResearchScope' is an enum-backed scope wrapper that constructs either a 'Project' or 'Topic' variant with an associated identifier/name and filesystem root, and provides shared accessors to read or update that root path. [crates/gwiki/src/session.rs:20-46]
- `ResearchScope.project_for_id` (method) component `ResearchScope.project_for_id [method]` (`a88407fe-2279-55c8-bba4-d009159e3066`) lines 21-26 [crates/gwiki/src/session.rs:21-26]
  - Signature: `pub fn project_for_id(project_id: impl Into<String>, root: impl Into<PathBuf>) -> Self {`
  - Purpose: Constructs and returns a 'Self::Project' variant by converting 'project_id' into a 'String' and 'root' into a 'PathBuf'. [crates/gwiki/src/session.rs:21-26]
- `ResearchScope.topic` (method) component `ResearchScope.topic [method]` (`4da0f5af-8b4e-5a85-abe6-4dae1bbcda1c`) lines 28-33 [crates/gwiki/src/session.rs:28-33]
  - Signature: `pub fn topic(name: impl Into<String>, root: impl Into<PathBuf>) -> Self {`
  - Purpose: Constructs and returns a 'Self::Topic' value by converting 'name' into a 'String' and 'root' into a 'PathBuf'. [crates/gwiki/src/session.rs:28-33]
- `ResearchScope.root` (method) component `ResearchScope.root [method]` (`7f8ee952-6560-5959-9b6d-a0ea2da9ae1e`) lines 35-39 [crates/gwiki/src/session.rs:35-39]
  - Signature: `pub fn root(&self) -> &Path {`
  - Purpose: Returns the 'Path' reference stored in the enum variant’s 'root' field, regardless of whether 'self' is 'Project' or 'Topic'. [crates/gwiki/src/session.rs:35-39]
- `ResearchScope.set_root` (method) component `ResearchScope.set_root [method]` (`6988bf97-21bc-5f28-89da-32c00f5315c7`) lines 41-45 [crates/gwiki/src/session.rs:41-45]
  - Signature: `fn set_root(&mut self, new_root: PathBuf) {`
  - Purpose: Mutably replaces the 'root' field of either 'Project' or 'Topic' enum variant with the provided 'new_root' path. [crates/gwiki/src/session.rs:41-45]
- `ResearchScope` (class) component `ResearchScope [class]` (`accee1a5-1d84-5df8-a377-65969a9a010b`) lines 48-57 [crates/gwiki/src/session.rs:48-57]
  - Signature: `impl From<&ResolvedScope> for ResearchScope {`
  - Purpose: 'ResearchScope' implements 'From<&ResolvedScope>' by constructing a topic-scoped research scope from a cloned topic name and root path, or a project-scoped research scope from a cloned project ID and root path, depending on the resolved scope kind. [crates/gwiki/src/session.rs:48-57]
- `ResearchScope.from` (method) component `ResearchScope.from [method]` (`4b031344-69e0-5a30-bc3d-0ee5e874e65d`) lines 49-56 [crates/gwiki/src/session.rs:49-56]
  - Signature: `fn from(scope: &ResolvedScope) -> Self {`
  - Purpose: Constructs a 'Self' from a 'ResolvedScope' by matching on its kind: for 'Topic', it clones the topic name and root path to create a topic scope, and for 'Project', it clones the project ID and root path to create a project-by-ID scope. [crates/gwiki/src/session.rs:49-56]
- `DaemonDispatch` (class) component `DaemonDispatch [class]` (`8786f3d3-8940-5edd-870b-d6a09a562e10`) lines 60-64 [crates/gwiki/src/session.rs:60-64]
  - Signature: `pub struct DaemonDispatch {`
  - Purpose: 'DaemonDispatch' is a data container that identifies a daemon-side dispatch by 'dispatch_id', records the daemon endpoint in 'daemon_base_url', and tracks associated agent run IDs in 'agent_run_ids'. [crates/gwiki/src/session.rs:60-64]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`848bacba-97d0-545f-9adb-3928884d2393`) lines 68-76 [crates/gwiki/src/session.rs:68-76]
  - Signature: `pub struct ResearchCodeCitation {`
  - Purpose: 'ResearchCodeCitation' is a serialized citation record that identifies a source file and optionally a line number, symbol name, and provenance list for tracing research-derived code references. [crates/gwiki/src/session.rs:68-76]
- `ResearchCodeCitationUnchecked` (class) component `ResearchCodeCitationUnchecked [class]` (`7426a58b-3a12-5b3e-be54-faeb406f847e`) lines 79-87 [crates/gwiki/src/session.rs:79-87]
  - Signature: `struct ResearchCodeCitationUnchecked {`
  - Purpose: 'ResearchCodeCitationUnchecked' is an untrusted data container for a code citation, storing a file path plus optional line number and symbol metadata, along with a provenance list. [crates/gwiki/src/session.rs:79-87]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`197f1d19-d6c7-5f3c-b833-87bdcb0395ca`) lines 89-95 [crates/gwiki/src/session.rs:89-95]
  - Signature: `impl TryFrom<ResearchCodeCitationUnchecked> for ResearchCodeCitation {`
  - Purpose: 'ResearchCodeCitation' implements 'TryFrom<ResearchCodeCitationUnchecked>' by converting unchecked 'file', 'line', 'symbol', and 'provenance' fields through 'from_parts', returning a 'String' error on validation failure. [crates/gwiki/src/session.rs:89-95]
- `ResearchCodeCitation.Error` (type) component `ResearchCodeCitation.Error [type]` (`daa59587-004b-5d84-ba7f-d98bab48e98f`) lines 90-90 [crates/gwiki/src/session.rs:90]
  - Signature: `type Error = String;`
  - Purpose: Indexed type `ResearchCodeCitation.Error` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:90]
- `ResearchCodeCitation.try_from` (method) component `ResearchCodeCitation.try_from [method]` (`049f2fce-ca39-5af4-9394-a9ba74703653`) lines 92-94 [crates/gwiki/src/session.rs:92-94]
  - Signature: `fn try_from(value: ResearchCodeCitationUnchecked) -> Result<Self, Self::Error> {`
  - Purpose: Converts a 'ResearchCodeCitationUnchecked' into a validated 'Self' by delegating its 'file', 'line', 'symbol', and 'provenance' fields to 'Self::from_parts', returning the resulting success or error. [crates/gwiki/src/session.rs:92-94]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`65efdf7d-27ab-5197-8a87-afeba0172f4c`) lines 97-156 [crates/gwiki/src/session.rs:97-156]
  - Signature: `impl ResearchCodeCitation {`
  - Purpose: 'ResearchCodeCitation' is a validated value object that stores a non-empty, path-safe code 'file' reference with optional 'line' and 'symbol' metadata plus a non-empty 'provenance' list, exposing read-only accessors and converting validation failures into 'WikiError::InvalidInput'. [crates/gwiki/src/session.rs:97-156]
- `ResearchCodeCitation.new` (method) component `ResearchCodeCitation.new [method]` (`d9897627-5d63-57a1-905b-41701b00bc3f`) lines 98-110 [crates/gwiki/src/session.rs:98-110]
  - Signature: `pub fn new(`
  - Purpose: Constructs a 'Self' by converting 'file' into a 'String' and delegating to 'Self::from_parts', mapping any returned error message into 'WikiError::InvalidInput { field: "code_citations", ... }'. [crates/gwiki/src/session.rs:98-110]
- `ResearchCodeCitation.from_parts` (method) component `ResearchCodeCitation.from_parts [method]` (`8c3d8521-6753-5fdf-82ec-360def624ce9`) lines 112-139 [crates/gwiki/src/session.rs:112-139]
  - Signature: `fn from_parts(`
  - Purpose: Constructs a citation object from 'file', 'line', 'symbol', and 'provenance' after validating that 'file' is non-empty, contains no '..' path components, and that 'provenance' is a non-empty list of non-empty strings, otherwise returning an error string. [crates/gwiki/src/session.rs:112-139]
- `ResearchCodeCitation.file` (method) component `ResearchCodeCitation.file [method]` (`04bc8c33-97a7-58df-940d-1b2e2db7e4da`) lines 141-143 [crates/gwiki/src/session.rs:141-143]
  - Signature: `pub fn file(&self) -> &str {`
  - Purpose: Returns an immutable string slice reference to the 'file' field stored in 'self'. [crates/gwiki/src/session.rs:141-143]
- `ResearchCodeCitation.line` (method) component `ResearchCodeCitation.line [method]` (`a2dc0b6f-486a-574b-9c15-8d5ac00566c8`) lines 145-147 [crates/gwiki/src/session.rs:145-147]
  - Signature: `pub fn line(&self) -> Option<usize> {`
  - Purpose: Returns the stored 'line' field as an 'Option<usize>', exposing the line number if present. [crates/gwiki/src/session.rs:145-147]
- `ResearchCodeCitation.symbol` (method) component `ResearchCodeCitation.symbol [method]` (`2097b105-c186-5a4a-a38e-ad07ec5aaaf6`) lines 149-151 [crates/gwiki/src/session.rs:149-151]
  - Signature: `pub fn symbol(&self) -> Option<&str> {`
  - Purpose: Returns the internal 'symbol' field as an 'Option<&str>' by borrowing its contents via 'as_deref()'. [crates/gwiki/src/session.rs:149-151]
- `ResearchCodeCitation.provenance` (method) component `ResearchCodeCitation.provenance [method]` (`086fdf1a-8fbe-5dac-ba71-e8d6475573f7`) lines 153-155 [crates/gwiki/src/session.rs:153-155]
  - Signature: `pub fn provenance(&self) -> &[String] {`
  - Purpose: Returns an immutable slice reference to the struct’s internal 'provenance' string vector. [crates/gwiki/src/session.rs:153-155]
- `AcceptedResearchNote` (class) component `AcceptedResearchNote [class]` (`eeee9703-20ec-5cf2-bad7-38e27c167591`) lines 159-166 [crates/gwiki/src/session.rs:159-166]
  - Signature: `pub struct AcceptedResearchNote {`
  - Purpose: 'AcceptedResearchNote' is a serialized Rust data structure representing an accepted research note with a title, filesystem path, optional code citations, and an optional degradation message. [crates/gwiki/src/session.rs:159-166]
- `CompileState` (class) component `CompileState [class]` (`f8374798-95ad-5e36-b227-f563bc53b4e3`) lines 169-179 [crates/gwiki/src/session.rs:169-179]
  - Signature: `pub struct CompileState {`
  - Purpose: 'CompileState' is a data container for a compilation pass that tracks the handoff metadata, target bundle path, selected notes and source titles, accumulated citations, conflict and evidence gaps, and a flag indicating whether the operation intends to write output. [crates/gwiki/src/session.rs:169-179]
- `ResearchSession` (class) component `ResearchSession [class]` (`d50bae3a-1c79-575e-b4e6-86dbf4f56ae4`) lines 182-194 [crates/gwiki/src/session.rs:182-194]
  - Signature: `pub struct ResearchSession {`
  - Purpose: 'ResearchSession' is a serialized session record that captures a research job’s identity, query and prompt text, scope, source constraints, agent fan-out configuration, optional dispatch metadata, accepted notes, and optional compile state. [crates/gwiki/src/session.rs:182-194]
- `ResearchSession` (class) component `ResearchSession [class]` (`3d7bff01-c074-5cb8-8a5e-96c90a1334ad`) lines 196-313 [crates/gwiki/src/session.rs:196-313]
  - Signature: `impl ResearchSession {`
  - Purpose: 'ResearchSession' is a serializable research-workflow state holder that validates 'agent_count > 0', generates a new session ID, builds the session prompt from the question and source constraints, tracks dispatch/notes/compile state, and persists checkpoints under '.gwiki/research-session.json' in the vault root. [crates/gwiki/src/session.rs:196-313]
- `ResearchSession.new` (method) component `ResearchSession.new [method]` (`8a539915-4364-5cc3-9c42-f8698563cc04`) lines 197-224 [crates/gwiki/src/session.rs:197-224]
  - Signature: `pub fn new(`
  - Purpose: Creates a new research session by validating that 'agent_count' is nonzero, generating a fresh session ID and research prompt from the question, source constraints, and worker count, and initializing the remaining fields to their default empty or 'None' states. [crates/gwiki/src/session.rs:197-224]
- `ResearchSession.checkpoint_path` (method) component `ResearchSession.checkpoint_path [method]` (`abbad0d5-a7da-53d6-b16c-044a1ca3ba0f`) lines 226-228 [crates/gwiki/src/session.rs:226-228]
  - Signature: `pub fn checkpoint_path(vault_root: &Path) -> PathBuf {`
  - Purpose: 'checkpoint_path' returns the path to the vault’s session checkpoint file by appending '.gwiki/research-session.json' to the provided 'vault_root'. [crates/gwiki/src/session.rs:226-228]
- `ResearchSession.save_checkpoint` (method) component `ResearchSession.save_checkpoint [method]` (`b9196d71-81b3-5493-af62-96df968cc8a0`) lines 230-289 [crates/gwiki/src/session.rs:230-289]
  - Signature: `pub fn save_checkpoint(&self) -> Result<(), WikiError> {`
  - Purpose: 'save_checkpoint' persists the current checkpoint state by ensuring the parent directory exists, serializing 'self' to pretty JSON, writing it to a unique temporary file, syncing it to disk, and atomically renaming it into place while mapping I/O and serialization failures to 'WikiError' and cleaning up the temp file on error. [crates/gwiki/src/session.rs:230-289]
- `ResearchSession.load_checkpoint` (method) component `ResearchSession.load_checkpoint [method]` (`af9b87b7-98ac-58d7-8994-2357193c2b13`) lines 291-307 [crates/gwiki/src/session.rs:291-307]
  - Signature: `pub fn load_checkpoint(vault_root: &Path) -> Result<Self, WikiError> {`
  - Purpose: Loads the checkpoint JSON from the vault’s checkpoint file, maps read/parse failures into 'WikiError::Io'/'WikiError::Json', validates and normalizes the session scope root against 'vault_root', updates the in-memory scope root, and returns the reconstructed session. [crates/gwiki/src/session.rs:291-307]
- `ResearchSession.record_compile_state` (method) component `ResearchSession.record_compile_state [method]` (`155c09a6-abca-5a3b-921b-1b30b0e9b394`) lines 309-312 [crates/gwiki/src/session.rs:309-312]
  - Signature: `pub fn record_compile_state(&mut self, state: CompileState) -> Result<(), WikiError> {`
  - Purpose: Stores the provided 'CompileState' in 'self.compile_state' as 'Some(state)' and then persists the checkpoint by returning the result of 'self.save_checkpoint()'. [crates/gwiki/src/session.rs:309-312]
- `validate_checkpoint_scope_root` (function) component `validate_checkpoint_scope_root [function]` (`89484546-b51f-5390-a6c3-2a9f40b9dbca`) lines 315-334 [crates/gwiki/src/session.rs:315-334]
  - Signature: `fn validate_checkpoint_scope_root(`
  - Purpose: It normalizes the expected and loaded scope-root paths relative to the checkpoint’s vault root, returns the normalized expected root when they match, and otherwise raises 'WikiError::InvalidScope' identifying the checkpoint, loaded root, and expected root. [crates/gwiki/src/session.rs:315-334]
- `comparable_path` (function) component `comparable_path [function]` (`98fc7de2-941f-508d-ab65-681426c09c1e`) lines 336-345 [crates/gwiki/src/session.rs:336-345]
  - Signature: `fn comparable_path(path: &Path, relative_base: Option<&Path>) -> PathBuf {`
  - Purpose: Returns an absolute, comparable 'PathBuf' by first resolving a relative 'path' against 'relative_base' when provided, then canonicalizing it and falling back to the unresolved path if canonicalization fails. [crates/gwiki/src/session.rs:336-345]
- `checkpoint_vault_root` (function) component `checkpoint_vault_root [function]` (`2ad606ed-735e-515b-8efa-83c466994295`) lines 347-352 [crates/gwiki/src/session.rs:347-352]
  - Signature: `fn checkpoint_vault_root(checkpoint_path: &Path) -> Option<PathBuf> {`
  - Purpose: Returns the grandparent directory of 'checkpoint_path' as a 'PathBuf', or 'None' if the path has fewer than two ancestors. [crates/gwiki/src/session.rs:347-352]
- `new_session_id` (function) component `new_session_id [function]` (`8fc3a09f-6cfd-531f-bed9-f6f70ee8ac1a`) lines 354-361 [crates/gwiki/src/session.rs:354-361]
  - Signature: `fn new_session_id() -> Result<String, WikiError> {`
  - Purpose: Generates a session ID string of the form 'research-<unix_timestamp_ms>-<8-char UUID suffix>' by combining the current millisecond UNIX timestamp with the first 8 hexadecimal characters of a newly generated UUID, returning a 'WikiError' if timestamp retrieval fails. [crates/gwiki/src/session.rs:354-361]
- `unix_timestamp_ms` (function) component `unix_timestamp_ms [function]` (`92bde559-866b-562d-a39b-adc4b4df8c04`) lines 363-365 [crates/gwiki/src/session.rs:363-365]
  - Signature: `fn unix_timestamp_ms() -> Result<u64, WikiError> {`
  - Purpose: Returns the current Unix timestamp in milliseconds by delegating to 'time::unix_timestamp_ms()' and propagating any 'WikiError'. [crates/gwiki/src/session.rs:363-365]
- `research_prompt` (function) component `research_prompt [function]` (`a8cb78dd-fc49-52a1-ae37-18ebb8b72b8b`) lines 367-383 [crates/gwiki/src/session.rs:367-383]
  - Signature: `pub(crate) fn research_prompt(`
  - Purpose: Builds a research prompt string from a question, worker count, and optional source constraints by formatting a fixed instruction header and appending each constraint as a bulleted line. [crates/gwiki/src/session.rs:367-383]
- `compile_state_is_resumable` (function) component `compile_state_is_resumable [function]` (`36f6d594-e200-5587-a13d-469bc5d0d11f`) lines 390-423 [crates/gwiki/src/session.rs:390-423]
  - Signature: `fn compile_state_is_resumable() {`
  - Purpose: Creates a research session, records a 'CompileState', reloads the checkpoint from disk, and asserts that the compile state is persisted and restored with the expected fields intact. [crates/gwiki/src/session.rs:390-423]
- `research_code_citation_rejects_empty_provenance` (function) component `research_code_citation_rejects_empty_provenance [function]` (`17bf2072-3673-5bc2-a482-705ca996fcdf`) lines 426-437 [crates/gwiki/src/session.rs:426-437]
  - Signature: `fn research_code_citation_rejects_empty_provenance() {`
  - Purpose: Verifies that 'ResearchCodeCitation::new("src/lib.rs", None, None, Vec::new())' fails with 'WikiError::InvalidInput' for the 'code_citations' field when provenance is empty. [crates/gwiki/src/session.rs:426-437]
- `research_code_citation_rejects_parent_path_components` (function) component `research_code_citation_rejects_parent_path_components [function]` (`3fd0abe0-236a-56b3-9c4a-2b293a2fb97a`) lines 440-452 [crates/gwiki/src/session.rs:440-452]
  - Signature: `fn research_code_citation_rejects_parent_path_components() {`
  - Purpose: Verifies that 'ResearchCodeCitation::new' rejects a citation path containing parent directory components ('..') by returning 'WikiError::InvalidInput' for the 'code_citations' field. [crates/gwiki/src/session.rs:440-452]
- `research_code_citation_deserialization_rejects_empty_provenance` (function) component `research_code_citation_deserialization_rejects_empty_provenance [function]` (`f034753b-66c4-503a-9751-6f4050fbeb23`) lines 455-463 [crates/gwiki/src/session.rs:455-463]
  - Signature: `fn research_code_citation_deserialization_rejects_empty_provenance() {`
  - Purpose: Verifies that deserializing a 'ResearchCodeCitation' with an empty 'provenance' array fails and that the resulting error message mentions 'provenance'. [crates/gwiki/src/session.rs:455-463]
- `research_code_citation_deserialization_rejects_parent_path_components` (function) component `research_code_citation_deserialization_rejects_parent_path_components [function]` (`8385f8c9-8fe9-5e70-8038-7c553b67f27e`) lines 466-474 [crates/gwiki/src/session.rs:466-474]
  - Signature: `fn research_code_citation_deserialization_rejects_parent_path_components() {`
  - Purpose: Verifies that deserializing a 'ResearchCodeCitation' with a file path containing '..' fails and produces an error message mentioning the invalid parent path component. [crates/gwiki/src/session.rs:466-474]
- `load_checkpoint_rejects_legacy_project_vault_relative_scope_root` (function) component `load_checkpoint_rejects_legacy_project_vault_relative_scope_root [function]` (`9f3ec953-1ca8-5218-936f-f692e1bec553`) lines 477-502 [crates/gwiki/src/session.rs:477-502]
  - Signature: `fn load_checkpoint_rejects_legacy_project_vault_relative_scope_root() {`
  - Purpose: Verifies that 'ResearchSession::load_checkpoint' rejects a checkpoint whose legacy 'project-vault'-relative 'scope_root' resolves to '.gobby/wiki', returning 'WikiError::InvalidScope' and including both the legacy path and the canonical checkpoint root in the error detail. [crates/gwiki/src/session.rs:477-502]
- `load_checkpoint_rejects_mismatched_scope_root` (function) component `load_checkpoint_rejects_mismatched_scope_root [function]` (`c71d8a0c-ab8b-5557-be7e-12d7156ebb75`) lines 505-526 [crates/gwiki/src/session.rs:505-526]
  - Signature: `fn load_checkpoint_rejects_mismatched_scope_root() {`
  - Purpose: Verifies that 'ResearchSession::load_checkpoint' returns 'WikiError::InvalidScope' when a checkpoint’s serialized project scope root points to a different directory than the checkpoint’s expected root. [crates/gwiki/src/session.rs:505-526]
- `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault` (function) component `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault [function]` (`3bcf2e89-5b28-5a08-9ca8-7f5d3d730d3b`) lines 529-550 [crates/gwiki/src/session.rs:529-550]
  - Signature: `fn load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault() {`
  - Purpose: Verifies that 'ResearchSession::load_checkpoint' rewrites a relative 'scope.root' to the canonical absolute checkpoint vault directory when restoring a session from disk. [crates/gwiki/src/session.rs:529-550]

