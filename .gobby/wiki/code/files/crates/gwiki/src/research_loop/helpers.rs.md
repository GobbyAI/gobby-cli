---
title: crates/gwiki/src/research_loop/helpers.rs
type: code_file
provenance:
- file: crates/gwiki/src/research_loop/helpers.rs
  ranges:
  - 8-19
  - 21-80
  - 82-85
  - 90-102
  - 104-106
  - 108-119
  - 121-137
  - 139-175
  - 177-187
  - 189-203
  - 205-209
  - 211-221
  - 228-237
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research_loop/helpers.rs

Module: [[code/modules/crates/gwiki/src/research_loop|crates/gwiki/src/research_loop]]

## Purpose

`crates/gwiki/src/research_loop/helpers.rs` exposes 13 indexed API symbols.
[crates/gwiki/src/research_loop/helpers.rs:8-19]
[crates/gwiki/src/research_loop/helpers.rs:21-80]
[crates/gwiki/src/research_loop/helpers.rs:82-85]
[crates/gwiki/src/research_loop/helpers.rs:90-102]
[crates/gwiki/src/research_loop/helpers.rs:104-106]

## API Symbols

- `parse_model_action` (function) component `parse_model_action [function]` (`6a44acdd-db53-5bb3-bad9-85b534cb8981`) lines 8-19 [crates/gwiki/src/research_loop/helpers.rs:8-19]
  - Signature: `pub(crate) fn parse_model_action(response: &str) -> Result<ResearchAction, String> {`
  - Purpose: Parses a model response string to deserialize the first complete JSON object into a `ResearchAction`, gracefully handling trailing prose after the JSON. [crates/gwiki/src/research_loop/helpers.rs:8-19]
- `render_model_prompt` (function) component `render_model_prompt [function]` (`e4273117-46ef-56ad-a189-7431ea8d1dad`) lines 21-80 [crates/gwiki/src/research_loop/helpers.rs:21-80]
  - Signature: `pub(crate) fn render_model_prompt(request: &ModelRequest<'_>) -> String {`
  - Purpose: Constructs a formatted prompt string from a ModelRequest that aggregates the research question, progress metrics, resource utilization, constraints, and recent context (observations and gaps) to guide the model's selection of a JSON-formatted action. [crates/gwiki/src/research_loop/helpers.rs:21-80]
- `model_system_prompt` (function) component `model_system_prompt [function]` (`881eeb24-e30a-5007-9373-08f7ab8ab380`) lines 82-85 [crates/gwiki/src/research_loop/helpers.rs:82-85]
  - Signature: `pub(crate) fn model_system_prompt() -> &'static str {`
  - Purpose: Returns a static system prompt string instructing the model to select exactly one source-grounded action in JSON format and defer accepting notes until cited sources are verified. [crates/gwiki/src/research_loop/helpers.rs:82-85]
- `json_candidate` (function) component `json_candidate [function]` (`c744ad37-b215-5d4f-84af-7311e854c216`) lines 90-102 [crates/gwiki/src/research_loop/helpers.rs:90-102]
  - Signature: `fn json_candidate(response: &str) -> Result<&str, String> {`
  - Purpose: Strips markdown code fence delimiters from a response string and returns a borrowed slice starting from the first `{` character, which is expected to be the beginning of a JSON object. [crates/gwiki/src/research_loop/helpers.rs:90-102]
- `action_fingerprint` (function) component `action_fingerprint [function]` (`3996fea4-0cbb-5b44-99c2-c84758ee253c`) lines 104-106 [crates/gwiki/src/research_loop/helpers.rs:104-106]
  - Signature: `pub(crate) fn action_fingerprint(action: &ResearchAction) -> String {`
  - Purpose: Serializes a `ResearchAction` to a JSON string, falling back to its debug representation if serialization fails. [crates/gwiki/src/research_loop/helpers.rs:104-106]
- `normalize_sources` (function) component `normalize_sources [function]` (`b82a21c1-7bd9-5497-b9f8-28f2459aab03`) lines 108-119 [crates/gwiki/src/research_loop/helpers.rs:108-119]
  - Signature: `pub(crate) fn normalize_sources(sources: &[String]) -> Vec<String> {`
  - Purpose: Deduplicates and trims whitespace from input source strings, returning a vector with empty entries removed while preserving insertion order. [crates/gwiki/src/research_loop/helpers.rs:108-119]
- `validate_source_reference` (function) component `validate_source_reference [function]` (`698e5060-8dfc-518a-a96f-a32a9b0cd55b`) lines 121-137 [crates/gwiki/src/research_loop/helpers.rs:121-137]
  - Signature: `pub(crate) fn validate_source_reference(root: &Path, source: &str) -> Result<(), String> {`
  - Purpose: Validates a source reference by accepting HTTP(S) URLs or delegating file paths (file URLs or local paths) to root-relative validation. [crates/gwiki/src/research_loop/helpers.rs:121-137]
- `validate_source_path` (function) component `validate_source_path [function]` (`8ac81616-4a1a-5f57-be45-314824f68b0c`) lines 139-175 [crates/gwiki/src/research_loop/helpers.rs:139-175]
  - Signature: `fn validate_source_path(root: &Path, path: &Path) -> Result<(), String> {`
  - Purpose: Validates that a source path is non-empty, contains no parent directory traversal (`..`), and resolves canonically within a specified root directory scope to prevent path escape attacks. [crates/gwiki/src/research_loop/helpers.rs:139-175]
- `source_evidence` (function) component `source_evidence [function]` (`561042f9-1d36-54eb-a083-57214fac1f12`) lines 177-187 [crates/gwiki/src/research_loop/helpers.rs:177-187]
  - Signature: `pub(crate) fn source_evidence(root: &Path, source: &str) -> Vec<PathBuf> {`
  - Purpose: Resolves a source string to an absolute path relative to a root directory, returning an empty vector if the source is empty or a valid URL. [crates/gwiki/src/research_loop/helpers.rs:177-187]
- `source_path_aliases` (function) component `source_path_aliases [function]` (`ddffa667-26a2-5bf7-aa1b-00f0b6686471`) lines 189-203 [crates/gwiki/src/research_loop/helpers.rs:189-203]
  - Signature: `pub(crate) fn source_path_aliases(root: &Path, source: &str) -> Vec<String> {`
  - Purpose: Generates normalized path aliases by converting absolute paths to relative forms or relative paths to absolute forms within a root directory, excluding URLs. [crates/gwiki/src/research_loop/helpers.rs:189-203]
- `sorted_sources` (function) component `sorted_sources [function]` (`0bb295d5-9fd7-56e2-a1ef-46f18f87196c`) lines 205-209 [crates/gwiki/src/research_loop/helpers.rs:205-209]
  - Signature: `pub(crate) fn sorted_sources(sources: &HashSet<String>) -> Vec<String> {`
  - Purpose: Converts an unordered `HashSet<String>` into a lexicographically sorted `Vec<String>` by cloning elements and applying in-place sorting. [crates/gwiki/src/research_loop/helpers.rs:205-209]
- `default_stop_message` (function) component `default_stop_message [function]` (`b681f955-8248-5ab3-82fc-a048627028a5`) lines 211-221 [crates/gwiki/src/research_loop/helpers.rs:211-221]
  - Signature: `pub(crate) fn default_stop_message(stop_reason: ResearchStopReason) -> &'static str {`
  - Purpose: This function maps a `ResearchStopReason` enum variant to its corresponding static message string describing why a research session terminated. [crates/gwiki/src/research_loop/helpers.rs:211-221]
- `action_fingerprint_uses_stable_json` (function) component `action_fingerprint_uses_stable_json [function]` (`6118c832-ec29-54a3-bdbf-4ae18a9876f8`) lines 228-237 [crates/gwiki/src/research_loop/helpers.rs:228-237]
  - Signature: `fn action_fingerprint_uses_stable_json() {`
  - Purpose: This test verifies that `action_fingerprint()` generates a stable, deterministic JSON string representation of a `ResearchAction` enum variant. [crates/gwiki/src/research_loop/helpers.rs:228-237]

