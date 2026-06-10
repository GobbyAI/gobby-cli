---
title: crates/gwiki/src/research/outcome.rs
type: code_file
provenance:
- file: crates/gwiki/src/research/outcome.rs
  ranges:
  - 15-24
  - 26-41
  - 43-51
  - 53-89
  - 91-99
  - 101-127
  - 129-147
  - 149-152
  - 154-171
  - 173-188
  - 190-200
  - 202-216
  - 221-228
  - 230-252
  - 254-329
  - 331-334
  - 336-344
  - 346-353
  - 360-372
  - 375-385
  - 388-426
  - 429-444
  - 447-457
  - 460-470
  - 473-482
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/research/outcome.rs

Module: [[code/modules/crates/gwiki/src/research|crates/gwiki/src/research]]

## Purpose

`crates/gwiki/src/research/outcome.rs` exposes 25 indexed API symbols.
[crates/gwiki/src/research/outcome.rs:15-24]
[crates/gwiki/src/research/outcome.rs:26-41]
[crates/gwiki/src/research/outcome.rs:43-51]
[crates/gwiki/src/research/outcome.rs:53-89]
[crates/gwiki/src/research/outcome.rs:91-99]
[crates/gwiki/src/research/outcome.rs:101-127]
[crates/gwiki/src/research/outcome.rs:129-147]
[crates/gwiki/src/research/outcome.rs:149-152]
[crates/gwiki/src/research/outcome.rs:154-171]
[crates/gwiki/src/research/outcome.rs:173-188]
[crates/gwiki/src/research/outcome.rs:190-200]
[crates/gwiki/src/research/outcome.rs:202-216]
[crates/gwiki/src/research/outcome.rs:221-228]
[crates/gwiki/src/research/outcome.rs:230-252]
[crates/gwiki/src/research/outcome.rs:254-329]
[crates/gwiki/src/research/outcome.rs:331-334]
[crates/gwiki/src/research/outcome.rs:336-344]
[crates/gwiki/src/research/outcome.rs:346-353]
[crates/gwiki/src/research/outcome.rs:360-372]
[crates/gwiki/src/research/outcome.rs:375-385]
[crates/gwiki/src/research/outcome.rs:388-426]
[crates/gwiki/src/research/outcome.rs:429-444]
[crates/gwiki/src/research/outcome.rs:447-457]
[crates/gwiki/src/research/outcome.rs:460-470]
[crates/gwiki/src/research/outcome.rs:473-482]

## API Symbols

- `observation_from_outcome` (function) component `observation_from_outcome [function]` (`3f73fdeb-40b8-55c5-a707-2ef2588523b9`) lines 15-24 [crates/gwiki/src/research/outcome.rs:15-24]
  - Signature: `pub(crate) fn observation_from_outcome(`
  - Purpose: Constructs a `ResearchObservation` from a `CommandOutcome` by extracting and enriching the result text with sources, code citations, degradations, and changed paths. [crates/gwiki/src/research/outcome.rs:15-24]
- `outcome_sources` (function) component `outcome_sources [function]` (`7feb8773-b9dc-546f-92a2-326263a2697c`) lines 26-41 [crates/gwiki/src/research/outcome.rs:26-41]
  - Signature: `pub(crate) fn outcome_sources(payload: &Value) -> Vec<String> {`
  - Purpose: Collects string values from a `Value` payload matching nine predefined source-identifier keys and returns the deduplicated result. [crates/gwiki/src/research/outcome.rs:26-41]
- `outcome_changed_paths` (function) component `outcome_changed_paths [function]` (`30524709-0f53-567d-97f0-27432eb4f00f`) lines 43-51 [crates/gwiki/src/research/outcome.rs:43-51]
  - Signature: `pub(crate) fn outcome_changed_paths(payload: &Value) -> Vec<PathBuf> {`
  - Purpose: Extracts and deduplicates strings from predefined path-related keys ('absolute_path', 'asset_path', 'raw_path', 'wiki_path') in a JSON payload, returning them as a vector of PathBuf objects. [crates/gwiki/src/research/outcome.rs:43-51]
- `outcome_code_citations` (function) component `outcome_code_citations [function]` (`267a61df-4660-57e7-8002-45bafb2a723c`) lines 53-89 [crates/gwiki/src/research/outcome.rs:53-89]
  - Signature: `pub(crate) fn outcome_code_citations(`
  - Purpose: Parses code citation entries from a JSON payload, sanitizes file paths, constructs deduplicated `ResearchCodeCitation` objects with the provided provenance, and filters out invalid entries. [crates/gwiki/src/research/outcome.rs:53-89]
- `outcome_degradations` (function) component `outcome_degradations [function]` (`0de40973-2b45-5ccb-94c4-a204d4782919`) lines 91-99 [crates/gwiki/src/research/outcome.rs:91-99]
  - Signature: `pub(crate) fn outcome_degradations(payload: &Value) -> Vec<String> {`
  - Purpose: Collects strings from a JSON value under the keys 'degradation', 'degradations', and 'degraded_sources', then returns a deduplicated vector. [crates/gwiki/src/research/outcome.rs:91-99]
- `dedup_code_citations` (function) component `dedup_code_citations [function]` (`81ffca0c-119d-5a66-ace4-8391f76fd9b4`) lines 101-127 [crates/gwiki/src/research/outcome.rs:101-127]
  - Signature: `pub(crate) fn dedup_code_citations(`
  - Purpose: Deduplicates code citations by (file, line, symbol) identity while merging unique provenance entries from duplicate citations into the first occurrence. [crates/gwiki/src/research/outcome.rs:101-127]
- `sanitize_code_path` (function) component `sanitize_code_path [function]` (`3bcd02ad-92fc-5a8f-a498-c43f23c2f089`) lines 129-147 [crates/gwiki/src/research/outcome.rs:129-147]
  - Signature: `pub(crate) fn sanitize_code_path(path: &str) -> Option<String> {`
  - Purpose: # Summary

Validates and sanitizes a relative file path by rejecting absolute paths and path traversal sequences (parent directory and root references), returning a normalized forward-slash-separated string or `None` if invalid. [crates/gwiki/src/research/outcome.rs:129-147]
- `dedup_code_citation_provenance` (function) component `dedup_code_citation_provenance [function]` (`943d2eac-a830-5792-acf5-2e7b28cfd20e`) lines 149-152 [crates/gwiki/src/research/outcome.rs:149-152]
  - Signature: `fn dedup_code_citation_provenance(provenance: &mut Vec<String>) {`
  - Purpose: Removes duplicate provenance strings in-place by retaining only the first occurrence of each source, using a HashSet to track seen values. [crates/gwiki/src/research/outcome.rs:149-152]
- `collect_keyed_strings` (function) component `collect_keyed_strings [function]` (`b0ffd1cb-2a0a-56b8-9d66-36231fe1560a`) lines 154-171 [crates/gwiki/src/research/outcome.rs:154-171]
  - Signature: `pub(crate) fn collect_keyed_strings(value: &Value, keys: &[&str], out: &mut Vec<String>) {`
  - Purpose: Recursively traverses a nested JSON Value structure, extracting and collecting strings from all values whose keys match the provided identifiers into an output vector. [crates/gwiki/src/research/outcome.rs:154-171]
- `collect_strings` (function) component `collect_strings [function]` (`6c6d19ef-3312-5994-abb8-995d91517426`) lines 173-188 [crates/gwiki/src/research/outcome.rs:173-188]
  - Signature: `pub(crate) fn collect_strings(value: &Value, out: &mut Vec<String>) {`
  - Purpose: Recursively traverses a `Value` structure and collects all non-empty trimmed strings from it and its nested arrays and objects into an output vector. [crates/gwiki/src/research/outcome.rs:173-188]
- `dedup_strings` (function) component `dedup_strings [function]` (`2e751191-f2fe-5fa7-bf0e-8177b8228116`) lines 190-200 [crates/gwiki/src/research/outcome.rs:190-200]
  - Signature: `pub(crate) fn dedup_strings(values: Vec<String>) -> Vec<String> {`
  - Purpose: Removes duplicate strings from the input vector while preserving the order of their first occurrence. [crates/gwiki/src/research/outcome.rs:190-200]
- `scope_selection_from_research_scope` (function) component `scope_selection_from_research_scope [function]` (`d15b1643-f85e-5196-98de-6525165bfb2c`) lines 202-216 [crates/gwiki/src/research/outcome.rs:202-216]
  - Signature: `pub(crate) fn scope_selection_from_research_scope(scope: &ResearchScope) -> ScopeSelection {`
  - Purpose: This function converts a `ResearchScope` enum into a `ScopeSelection` by extracting the project root (two directory levels above the stored vault root) or cloning the topic name, depending on the input variant. [crates/gwiki/src/research/outcome.rs:202-216]
- `estimate_tokens` (function) component `estimate_tokens [function]` (`83785a6f-5462-5830-9a43-cc2684b4c0c1`) lines 221-228 [crates/gwiki/src/research/outcome.rs:221-228]
  - Signature: `pub(crate) fn estimate_tokens(text: &str) -> usize {`
  - Purpose: Estimates a text string's token count by applying the formula `(word_count × 13 + 9) / 10` to its whitespace-separated word count. [crates/gwiki/src/research/outcome.rs:221-228]
- `load_or_create_session` (function) component `load_or_create_session [function]` (`c286c89d-836d-571a-bfd0-36f12439799e`) lines 230-252 [crates/gwiki/src/research/outcome.rs:230-252]
  - Signature: `pub(crate) fn load_or_create_session(`
  - Purpose: Loads an existing ResearchSession from a checkpoint if available, otherwise creates a new one, then resets its configuration fields and regenerates the research prompt based on the provided options. [crates/gwiki/src/research/outcome.rs:230-252]
- `deterministic_audit_findings` (function) component `deterministic_audit_findings [function]` (`5c4741f3-51f8-5941-b093-806815b6a0dc`) lines 254-329 [crates/gwiki/src/research/outcome.rs:254-329]
  - Signature: `pub(crate) fn deterministic_audit_findings(`
  - Purpose: Generates audit findings by scanning markdown research notes in a vault's raw research directory to identify those with stale "materializing" status in their YAML frontmatter. [crates/gwiki/src/research/outcome.rs:254-329]
- `audit_fingerprint` (function) component `audit_fingerprint [function]` (`0032b8e7-e67d-5a56-b577-9a5672bf23ed`) lines 331-334 [crates/gwiki/src/research/outcome.rs:331-334]
  - Signature: `pub(crate) fn audit_fingerprint(kind: &str, path: &Path) -> String {`
  - Purpose: Generates a deterministic UUID v5 fingerprint by hashing a concatenated kind identifier and file path using a fixed research note namespace. [crates/gwiki/src/research/outcome.rs:331-334]
- `resolve_scope` (function) component `resolve_scope [function]` (`2a9413c4-421f-51e7-992e-6ae55479173c`) lines 336-344 [crates/gwiki/src/research/outcome.rs:336-344]
  - Signature: `pub fn resolve_scope(selection: &ScopeSelection) -> Result<ResearchScope, WikiError> {`
  - Purpose: Resolves a `ScopeSelection` into a `ResearchScope` by determining the current working directory and delegating to the scope resolver, propagating any IO errors as `WikiError`. [crates/gwiki/src/research/outcome.rs:336-344]
- `research_scope_from_resolved` (function) component `research_scope_from_resolved [function]` (`44de0153-3b36-5444-8d45-1c93c694114d`) lines 346-353 [crates/gwiki/src/research/outcome.rs:346-353]
  - Signature: `pub fn research_scope_from_resolved(scope: &scope::ResolvedScope) -> ResearchScope {`
  - Purpose: This function converts a `ResolvedScope` into a `ResearchScope` by pattern matching on its kind field to construct either a topic-based or project-based `ResearchScope` variant with the corresponding identifier and root directory path. [crates/gwiki/src/research/outcome.rs:346-353]
- `project_research_scope_selection_uses_project_root` (function) component `project_research_scope_selection_uses_project_root [function]` (`803e1430-93c2-59f0-9ff6-1b8a38f41c97`) lines 360-372 [crates/gwiki/src/research/outcome.rs:360-372]
  - Signature: `fn project_research_scope_selection_uses_project_root() {`
  - Purpose: This test verifies that `scope_selection_from_research_scope()` correctly derives the project root path by stripping the `.gobby/wiki` suffix from a ResearchScope's wiki directory path. [crates/gwiki/src/research/outcome.rs:360-372]
- `dedup_strings_preserves_first_seen_order` (function) component `dedup_strings_preserves_first_seen_order [function]` (`5f2ea15f-b7df-54aa-9cc6-fd25a47ebca9`) lines 375-385 [crates/gwiki/src/research/outcome.rs:375-385]
  - Signature: `fn dedup_strings_preserves_first_seen_order() {`
  - Purpose: This test verifies that `dedup_strings` removes duplicate strings while preserving the order of their first occurrence. [crates/gwiki/src/research/outcome.rs:375-385]
- `dedup_code_citations_preserves_first_seen_order` (function) component `dedup_code_citations_preserves_first_seen_order [function]` (`bd215855-2bfb-51af-b331-6059420ed755`) lines 388-426 [crates/gwiki/src/research/outcome.rs:388-426]
  - Signature: `fn dedup_code_citations_preserves_first_seen_order() {`
  - Purpose: # Summary

Tests that `dedup_code_citations` merges code citations sharing the same location while deduplicating tags in order of first appearance and preserves the sequence of first-encountered distinct citations. [crates/gwiki/src/research/outcome.rs:388-426]
- `outcome_code_citations_rejects_unsafe_paths` (function) component `outcome_code_citations_rejects_unsafe_paths [function]` (`5927f5ca-cf9a-554d-8634-34adf496068f`) lines 429-444 [crates/gwiki/src/research/outcome.rs:429-444]
  - Signature: `fn outcome_code_citations_rejects_unsafe_paths() {`
  - Purpose: Validates that `outcome_code_citations` filters code citation file paths, rejecting unsafe paths (absolute paths, parent-directory traversals, whitespace-padded entries, and empty strings) while normalizing valid relative paths. [crates/gwiki/src/research/outcome.rs:429-444]
- `sanitize_code_path_strips_current_dir_components` (function) component `sanitize_code_path_strips_current_dir_components [function]` (`b2272a0d-a49f-56f9-a1cc-7fe96a8fa0b4`) lines 447-457 [crates/gwiki/src/research/outcome.rs:447-457]
  - Signature: `fn sanitize_code_path_strips_current_dir_components() {`
  - Purpose: This test verifies that `sanitize_code_path` normalizes file paths by removing current directory (`.`) components and consecutive slashes, returning `None` for non-file paths. [crates/gwiki/src/research/outcome.rs:447-457]
- `outcome_code_citations_skip_empty_provenance` (function) component `outcome_code_citations_skip_empty_provenance [function]` (`179e1b62-c5b0-51b3-8b10-d38374ed5943`) lines 460-470 [crates/gwiki/src/research/outcome.rs:460-470]
  - Signature: `fn outcome_code_citations_skip_empty_provenance() {`
  - Purpose: This function tests that `outcome_code_citations()` returns an empty collection when code citations are provided but the provenance parameter is an empty string. [crates/gwiki/src/research/outcome.rs:460-470]
- `estimate_tokens_uses_one_point_three_word_heuristic` (function) component `estimate_tokens_uses_one_point_three_word_heuristic [function]` (`c302f376-befe-5b5f-b907-1d1a6c6b02c9`) lines 473-482 [crates/gwiki/src/research/outcome.rs:473-482]
  - Signature: `fn estimate_tokens_uses_one_point_three_word_heuristic() {`
  - Purpose: This test function validates that `estimate_tokens()` estimates token count by multiplying word count by approximately 1.3x. [crates/gwiki/src/research/outcome.rs:473-482]

