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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18](crates/gwiki/src/commands/citation_quality/contradictions.rs#L15-L18), [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24](crates/gwiki/src/commands/citation_quality/contradictions.rs#L21-L24), [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29](crates/gwiki/src/commands/citation_quality/contradictions.rs#L27-L29), [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67](crates/gwiki/src/commands/citation_quality/contradictions.rs#L31-L67), [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117](crates/gwiki/src/commands/citation_quality/contradictions.rs#L69-L117), [crates/gwiki/src/commands/citation_quality/contradictions.rs:119-125](crates/gwiki/src/commands/citation_quality/contradictions.rs#L119-L125), [crates/gwiki/src/commands/citation_quality/contradictions.rs:127-163](crates/gwiki/src/commands/citation_quality/contradictions.rs#L127-L163), [crates/gwiki/src/commands/citation_quality/contradictions.rs:169-180](crates/gwiki/src/commands/citation_quality/contradictions.rs#L169-L180), [crates/gwiki/src/commands/citation_quality/contradictions.rs:182-193](crates/gwiki/src/commands/citation_quality/contradictions.rs#L182-L193), [crates/gwiki/src/commands/citation_quality/contradictions.rs:195-226](crates/gwiki/src/commands/citation_quality/contradictions.rs#L195-L226), [crates/gwiki/src/commands/citation_quality/contradictions.rs:228-234](crates/gwiki/src/commands/citation_quality/contradictions.rs#L228-L234), [crates/gwiki/src/commands/citation_quality/contradictions.rs:236-241](crates/gwiki/src/commands/citation_quality/contradictions.rs#L236-L241)

</details>

# crates/gwiki/src/commands/citation_quality/contradictions.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds the citation-quality contradiction section from provenance data and an AI detector. It first checks whether AI contradiction detection is available, then groups provenance links into per-section claim comparisons so only multi-source sections with distinct claims are sent to the detector. The detector’s output is parsed from JSON, cleaned against the known source IDs and normalized claims, and wrapped into a `ContradictionSection` result. The helper types model section-level comparisons and per-source claims, while the remaining helpers handle comparison collection, source ID extraction, model-output parsing, claim normalization, and conversion of AI errors into `WikiError`.
[crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SectionClaimComparison` | class | `pub(super) struct SectionClaimComparison {` | `SectionClaimComparison [class]` | `447c2c98-1319-598c-b131-61324a3128dd` | 15-18 [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18] | Indexed class `SectionClaimComparison` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18] |
| `SourceClaim` | class | `pub(super) struct SourceClaim {` | `SourceClaim [class]` | `f19806e5-805c-5381-aeda-b5a7b540cc4e` | 21-24 [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24] | Indexed class `SourceClaim` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24] |
| `ContradictionModelOutput` | class | `struct ContradictionModelOutput {` | `ContradictionModelOutput [class]` | `00bc49e9-22cf-564d-a891-453b46e339f5` | 27-29 [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29] | Indexed class `ContradictionModelOutput` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29] |
| `contradiction_section` | function | `pub(super) fn contradiction_section(` | `contradiction_section [function]` | `3f9168d3-a270-55ea-94b3-869c1e30d867` | 31-67 [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67] | Indexed function `contradiction_section` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67] |
| `section_claim_comparisons` | function | `fn section_claim_comparisons(provenance: &ProvenanceGraph) -> Vec<SectionClaimComparison> {` | `section_claim_comparisons [function]` | `00015808-7660-5129-8df1-45d4b9551ad1` | 69-117 [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117] | Indexed function `section_claim_comparisons` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117] |
| `comparison_source_ids` | function | `fn comparison_source_ids(comparisons: &[SectionClaimComparison]) -> BTreeSet<String> {` | `comparison_source_ids [function]` | `665293c0-c6e7-5cb4-a1e3-a5a7c619abf8` | 119-125 [crates/gwiki/src/commands/citation_quality/contradictions.rs:119-125] | Indexed function `comparison_source_ids` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:119-125] |
| `model_contradiction_findings` | function | `pub(super) fn model_contradiction_findings(` | `model_contradiction_findings [function]` | `eaa0b0ed-53a0-55a9-ae41-146efef7444b` | 127-163 [crates/gwiki/src/commands/citation_quality/contradictions.rs:127-163] | Indexed function `model_contradiction_findings` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:127-163] |
| `parse_contradiction_findings` | function | `pub(super) fn parse_contradiction_findings(` | `parse_contradiction_findings [function]` | `4d7279dc-fc08-5ad6-b48a-9d2f0055630b` | 169-180 [crates/gwiki/src/commands/citation_quality/contradictions.rs:169-180] | Indexed function `parse_contradiction_findings` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:169-180] |
| `extract_json_payload` | function | `fn extract_json_payload(text: &str) -> &str {` | `extract_json_payload [function]` | `af113876-ae59-5b3e-a8a7-d8ae1ee8e55e` | 182-193 [crates/gwiki/src/commands/citation_quality/contradictions.rs:182-193] | Indexed function `extract_json_payload` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:182-193] |
| `sanitize_contradiction_findings` | function | `fn sanitize_contradiction_findings(` | `sanitize_contradiction_findings [function]` | `42bb8298-cf9c-5f55-bf79-b90f9e029496` | 195-226 [crates/gwiki/src/commands/citation_quality/contradictions.rs:195-226] | Indexed function `sanitize_contradiction_findings` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:195-226] |
| `normalize_claim` | function | `fn normalize_claim(claim: &str) -> String {` | `normalize_claim [function]` | `82f3e4f9-5e64-5f94-84ff-2c0e0dbef37e` | 228-234 [crates/gwiki/src/commands/citation_quality/contradictions.rs:228-234] | Indexed function `normalize_claim` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:228-234] |
| `ai_error_to_wiki_error` | function | `fn ai_error_to_wiki_error(error: AiError) -> WikiError {` | `ai_error_to_wiki_error [function]` | `d29a8ae5-f587-5f02-9b34-47622bbdc587` | 236-241 [crates/gwiki/src/commands/citation_quality/contradictions.rs:236-241] | Indexed function `ai_error_to_wiki_error` in `crates/gwiki/src/commands/citation_quality/contradictions.rs`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:236-241] |
