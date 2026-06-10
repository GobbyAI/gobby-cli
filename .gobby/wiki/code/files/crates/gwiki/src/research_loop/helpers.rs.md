---
title: crates/gwiki/src/research_loop/helpers.rs
type: code_file
provenance:
- file: crates/gwiki/src/research_loop/helpers.rs
  ranges:
  - 8-11
  - 13-72
  - 74-77
  - 79-100
  - 102-104
  - 106-117
  - 119-135
  - 137-173
  - 175-185
  - 187-201
  - 203-207
  - 209-219
  - 226-235
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research_loop/helpers.rs

Module: [[code/modules/crates/gwiki/src/research_loop|crates/gwiki/src/research_loop]]

## Purpose

`crates/gwiki/src/research_loop/helpers.rs` exposes 13 indexed API symbols.
[crates/gwiki/src/research_loop/helpers.rs:8-11]
[crates/gwiki/src/research_loop/helpers.rs:13-72]
[crates/gwiki/src/research_loop/helpers.rs:74-77]
[crates/gwiki/src/research_loop/helpers.rs:79-100]
[crates/gwiki/src/research_loop/helpers.rs:102-104]
[crates/gwiki/src/research_loop/helpers.rs:106-117]
[crates/gwiki/src/research_loop/helpers.rs:119-135]
[crates/gwiki/src/research_loop/helpers.rs:137-173]
[crates/gwiki/src/research_loop/helpers.rs:175-185]
[crates/gwiki/src/research_loop/helpers.rs:187-201]
[crates/gwiki/src/research_loop/helpers.rs:203-207]
[crates/gwiki/src/research_loop/helpers.rs:209-219]
[crates/gwiki/src/research_loop/helpers.rs:226-235]

## API Symbols

- `parse_model_action` (function) component `parse_model_action [function]` (`6a44acdd-db53-5bb3-bad9-85b534cb8981`) lines 8-11 [crates/gwiki/src/research_loop/helpers.rs:8-11]
  - Signature: `pub(crate) fn parse_model_action(response: &str) -> Result<ResearchAction, String> {`
  - Purpose: Extracts a JSON object from a response string and deserializes it into a `ResearchAction` struct, returning a descriptive error message if either extraction or deserialization fails. [crates/gwiki/src/research_loop/helpers.rs:8-11]
- `render_model_prompt` (function) component `render_model_prompt [function]` (`eea217db-9fa9-5223-9fba-f8e8a6d84d89`) lines 13-72 [crates/gwiki/src/research_loop/helpers.rs:13-72]
  - Signature: `pub(crate) fn render_model_prompt(request: &ModelRequest<'_>) -> String {`
  - Purpose: Constructs a formatted prompt string from a ModelRequest by aggregating research task metadata (question, progress metrics, constraints, observations, and gaps) with instructions to return a JSON-formatted action response. [crates/gwiki/src/research_loop/helpers.rs:13-72]
- `model_system_prompt` (function) component `model_system_prompt [function]` (`4fab27f1-63bc-5a58-99e6-b55632845b29`) lines 74-77 [crates/gwiki/src/research_loop/helpers.rs:74-77]
  - Signature: `pub(crate) fn model_system_prompt() -> &'static str {`
  - Purpose: This function returns a static string system prompt that instructs an AI agent to select exactly one source-grounded action formatted as JSON and defer writing notes until cited sources have been observed. [crates/gwiki/src/research_loop/helpers.rs:74-77]
- `extract_json_object` (function) component `extract_json_object [function]` (`a456e449-d0c4-5c67-ab9a-1540cfb0481d`) lines 79-100 [crates/gwiki/src/research_loop/helpers.rs:79-100]
  - Signature: `fn extract_json_object(response: &str) -> Result<&str, String> {`
  - Purpose: Extracts a JSON object substring from a response by removing markdown code fence delimiters and returning the text span from the first `{` to the last `}`, with validation that the object is non-empty. [crates/gwiki/src/research_loop/helpers.rs:79-100]
- `action_fingerprint` (function) component `action_fingerprint [function]` (`f8d80855-7a4b-541e-96af-847458631c1d`) lines 102-104 [crates/gwiki/src/research_loop/helpers.rs:102-104]
  - Signature: `pub(crate) fn action_fingerprint(action: &ResearchAction) -> String {`
  - Purpose: Generates a string representation of a `ResearchAction` by attempting JSON serialization via `serde_json`, falling back to debug formatting if serialization fails. [crates/gwiki/src/research_loop/helpers.rs:102-104]
- `normalize_sources` (function) component `normalize_sources [function]` (`a1a889d9-ef6f-5646-be78-d36e17ca6017`) lines 106-117 [crates/gwiki/src/research_loop/helpers.rs:106-117]
  - Signature: `pub(crate) fn normalize_sources(sources: &[String]) -> Vec<String> {`
  - Purpose: Deduplicates and trims whitespace from a list of source strings, removing empty entries while preserving the order of first occurrence. [crates/gwiki/src/research_loop/helpers.rs:106-117]
- `validate_source_reference` (function) component `validate_source_reference [function]` (`27fa2776-7135-5b0b-8709-63775eb726c4`) lines 119-135 [crates/gwiki/src/research_loop/helpers.rs:119-135]
  - Signature: `pub(crate) fn validate_source_reference(root: &Path, source: &str) -> Result<(), String> {`
  - Purpose: Validates a source reference as either an HTTP(S) URL or a file-system path, with file paths verified against a root directory. [crates/gwiki/src/research_loop/helpers.rs:119-135]
- `validate_source_path` (function) component `validate_source_path [function]` (`82e4ad62-f703-5776-baa2-db16c16fd518`) lines 137-173 [crates/gwiki/src/research_loop/helpers.rs:137-173]
  - Signature: `fn validate_source_path(root: &Path, path: &Path) -> Result<(), String> {`
  - Purpose: Validates that a source path does not escape a designated root directory through parent traversal, absolute paths, or canonical path resolution. [crates/gwiki/src/research_loop/helpers.rs:137-173]
- `source_evidence` (function) component `source_evidence [function]` (`bec1e788-79fa-58b9-86c7-4c86d60f5bd1`) lines 175-185 [crates/gwiki/src/research_loop/helpers.rs:175-185]
  - Signature: `pub(crate) fn source_evidence(root: &Path, source: &str) -> Vec<PathBuf> {`
  - Purpose: Converts a source string to a single-element PathBuf vector containing the absolute path (resolving relative paths against root), or returns an empty vector for empty strings and URLs. [crates/gwiki/src/research_loop/helpers.rs:175-185]
- `source_path_aliases` (function) component `source_path_aliases [function]` (`28821539-972d-5d73-a3ea-6053931cc288`) lines 187-201 [crates/gwiki/src/research_loop/helpers.rs:187-201]
  - Signature: `pub(crate) fn source_path_aliases(root: &Path, source: &str) -> Vec<String> {`
  - Purpose: Generates path aliases by converting absolute source paths to root-relative equivalents or expanding relative source paths against the root directory, excluding URL sources. [crates/gwiki/src/research_loop/helpers.rs:187-201]
- `sorted_sources` (function) component `sorted_sources [function]` (`3373af2e-e884-5e25-b6d4-73f176f73a6c`) lines 203-207 [crates/gwiki/src/research_loop/helpers.rs:203-207]
  - Signature: `pub(crate) fn sorted_sources(sources: &HashSet<String>) -> Vec<String> {`
  - Purpose: Converts a HashSet of Strings into a lexicographically sorted Vec by cloning and ordering its elements. [crates/gwiki/src/research_loop/helpers.rs:203-207]
- `default_stop_message` (function) component `default_stop_message [function]` (`310135d3-8fb3-5473-9660-63d5bc925613`) lines 209-219 [crates/gwiki/src/research_loop/helpers.rs:209-219]
  - Signature: `pub(crate) fn default_stop_message(stop_reason: ResearchStopReason) -> &'static str {`
  - Purpose: Returns a static string message corresponding to the given `ResearchStopReason` enum variant, describing why a research session terminated. [crates/gwiki/src/research_loop/helpers.rs:209-219]
- `action_fingerprint_uses_stable_json` (function) component `action_fingerprint_uses_stable_json [function]` (`fcfcc0bb-9421-5dcf-861f-d0e01bb19d56`) lines 226-235 [crates/gwiki/src/research_loop/helpers.rs:226-235]
  - Signature: `fn action_fingerprint_uses_stable_json() {`
  - Purpose: This test function verifies that `action_fingerprint()` generates a deterministic, stable JSON serialization of a `ResearchAction::Search` instance. [crates/gwiki/src/research_loop/helpers.rs:226-235]

