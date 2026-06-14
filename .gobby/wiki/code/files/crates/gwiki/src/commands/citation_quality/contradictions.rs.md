---
title: crates/gwiki/src/commands/citation_quality/contradictions.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/citation_quality/contradictions.rs
  ranges:
  - 15-18
  - 21-24
  - 27-29
  - 31-67
  - 69-117
  - 119-125
  - 127-163
  - 169-180
  - 182-193
  - 195-226
  - 228-234
  - 236-241
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/citation_quality/contradictions.rs

Module: [[code/modules/crates/gwiki/src/commands/citation_quality|crates/gwiki/src/commands/citation_quality]]

## Purpose

This file builds the contradiction-detection pipeline for citation quality checks. It defines small comparison records for section-level claims, groups provenance links into deduplicated multi-source section comparisons, and either returns an unavailable/empty contradiction section or runs an AI-backed detector over those comparisons.

The detector path serializes section comparisons into a prompt, parses the model’s JSON response into contradiction findings, and then sanitizes those findings against the known source IDs by trimming, normalizing, and deduplicating claims before producing the final `ContradictionSection`. An AI error is converted into a `WikiError::Daemon` so failures surface through the wiki error type.
[crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117]

## API Symbols

- `SectionClaimComparison` (class) component `SectionClaimComparison [class]` (`447c2c98-1319-598c-b131-61324a3128dd`) lines 15-18 [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18]
  - Signature: `pub(super) struct SectionClaimComparison {`
  - Purpose: `SectionClaimComparison` is a module-visible data structure that pairs a section identifier (`String`) with the collection of `SourceClaim` values associated with that section for comparison. [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18]
- `SourceClaim` (class) component `SourceClaim [class]` (`f19806e5-805c-5381-aeda-b5a7b540cc4e`) lines 21-24 [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24]
  - Signature: `pub(super) struct SourceClaim {`
  - Purpose: `SourceClaim` is a Rust struct that stores an owned `source_id` and corresponding `claim` text, both as `String` fields. [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24]
- `ContradictionModelOutput` (class) component `ContradictionModelOutput [class]` (`00bc49e9-22cf-564d-a891-453b46e339f5`) lines 27-29 [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29]
  - Signature: `struct ContradictionModelOutput {`
  - Purpose: `ContradictionModelOutput` is a result container struct that holds a `Vec<ContradictionFinding>` in its `findings` field, representing the model’s detected contradiction findings. [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29]
- `contradiction_section` (function) component `contradiction_section [function]` (`3f9168d3-a270-55ea-94b3-869c1e30d867`) lines 31-67 [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67]
  - Signature: `pub(super) fn contradiction_section(`
  - Purpose: Returns a `ContradictionSection` that is marked unavailable with a note when AI detection is disabled, otherwise emits an empty noted section when no multi-source claim comparisons exist, or runs the provided detector on section claim comparisons, sanitizes the findings against known source IDs, and returns them as an available section. [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67]
- `section_claim_comparisons` (function) component `section_claim_comparisons [function]` (`00015808-7660-5129-8df1-45d4b9551ad1`) lines 69-117 [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117]
  - Signature: `fn section_claim_comparisons(provenance: &ProvenanceGraph) -> Vec<SectionClaimComparison> {`
  - Purpose: Groups non-empty claims from `provenance.links()` by `page_path#section_id`, deduplicates them by `(source_id, normalized_claim)`, and returns only the sections that contain claims from at least two distinct sources and at least two distinct normalized claims. [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117]
- `comparison_source_ids` (function) component `comparison_source_ids [function]` (`665293c0-c6e7-5cb4-a1e3-a5a7c619abf8`) lines 119-125 [crates/gwiki/src/commands/citation_quality/contradictions.rs:119-125]
  - Signature: `fn comparison_source_ids(comparisons: &[SectionClaimComparison]) -> BTreeSet<String> {`
  - Purpose: Returns the unique `source_id` values from all claims in the input comparisons, collected into a sorted `BTreeSet<String>`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:119-125]
- `model_contradiction_findings` (function) component `model_contradiction_findings [function]` (`eaa0b0ed-53a0-55a9-ae41-146efef7444b`) lines 127-163 [crates/gwiki/src/commands/citation_quality/contradictions.rs:127-163]
  - Signature: `pub(super) fn model_contradiction_findings(`
  - Purpose: Serializes the input `SectionClaimComparison` slice into a JSON prompt, routes it through the configured AI text generator to detect only direct factual contradictions between source-backed claims from the same section, and parses the JSON response into `Vec<ContradictionFinding>` (or returns an empty vector when AI routing is off/auto). [crates/gwiki/src/commands/citation_quality/contradictions.rs:127-163]
- `parse_contradiction_findings` (function) component `parse_contradiction_findings [function]` (`4d7279dc-fc08-5ad6-b48a-9d2f0055630b`) lines 169-180 [crates/gwiki/src/commands/citation_quality/contradictions.rs:169-180]
  - Signature: `pub(super) fn parse_contradiction_findings(`
  - Purpose: It extracts a JSON payload from `text`, deserializes it into `ContradictionModelOutput`, and returns `output.findings`, converting any JSON parse failure into `WikiError::Json` with action `"parse contradiction detection response"`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:169-180]
- `extract_json_payload` (function) component `extract_json_payload [function]` (`af113876-ae59-5b3e-a8a7-d8ae1ee8e55e`) lines 182-193 [crates/gwiki/src/commands/citation_quality/contradictions.rs:182-193]
  - Signature: `fn extract_json_payload(text: &str) -> &str {`
  - Purpose: Trims the input string and, if it is wrapped in a triple-backtick code fence with optional `json` language tag, returns the fenced contents trimmed; otherwise it returns the trimmed input unchanged. [crates/gwiki/src/commands/citation_quality/contradictions.rs:182-193]
- `sanitize_contradiction_findings` (function) component `sanitize_contradiction_findings [function]` (`42bb8298-cf9c-5f55-bf79-b90f9e029496`) lines 195-226 [crates/gwiki/src/commands/citation_quality/contradictions.rs:195-226]
  - Signature: `fn sanitize_contradiction_findings(`
  - Purpose: It normalizes and filters contradiction findings by trimming the claim, discarding empty claims or entries with fewer than two allowed source IDs, deduplicating source IDs and findings by `(normalize_claim(claim), source_ids)`, and returning only the first unique sanitized findings. [crates/gwiki/src/commands/citation_quality/contradictions.rs:195-226]
- `normalize_claim` (function) component `normalize_claim [function]` (`82f3e4f9-5e64-5f94-84ff-2c0e0dbef37e`) lines 228-234 [crates/gwiki/src/commands/citation_quality/contradictions.rs:228-234]
  - Signature: `fn normalize_claim(claim: &str) -> String {`
  - Purpose: `normalize_claim` collapses all whitespace in `claim` to single spaces, removes leading and trailing whitespace, and converts the resulting string to lowercase. [crates/gwiki/src/commands/citation_quality/contradictions.rs:228-234]
- `ai_error_to_wiki_error` (function) component `ai_error_to_wiki_error [function]` (`d29a8ae5-f587-5f02-9b34-47622bbdc587`) lines 236-241 [crates/gwiki/src/commands/citation_quality/contradictions.rs:236-241]
  - Signature: `fn ai_error_to_wiki_error(error: AiError) -> WikiError {`
  - Purpose: It converts an `AiError` into `WikiError::Daemon` by setting `endpoint` to `"gcore::ai/text-generate"` and `message` to the error’s string representation. [crates/gwiki/src/commands/citation_quality/contradictions.rs:236-241]

