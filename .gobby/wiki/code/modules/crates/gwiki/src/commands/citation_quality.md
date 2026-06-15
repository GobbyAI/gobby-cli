---
title: crates/gwiki/src/commands/citation_quality
type: code_module
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

# crates/gwiki/src/commands/citation_quality

Parent: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

The citation_quality contradiction module turns provenance data into section-scoped contradiction checks. It defines serializable comparison inputs made of a section name and its source-backed claims, plus a deserializable model output wrapper for findings . Its main entry point, `contradiction_section`, returns an explicit unavailable result when AI is disabled, with a note that no contradictions were fabricated [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-43].

When AI is available, the module builds comparisons from the provenance graph, short-circuiting with a note if there are no multi-source sections with differing claims to evaluate [crates/gwiki/src/commands/citation_quality/contradictions.rs:45-56]. Otherwise it collects the valid source IDs, runs the supplied detector over the comparison batches, sanitizes returned contradiction findings against those source IDs, and assembles an available `ContradictionSection` containing the cleaned findings [crates/gwiki/src/commands/citation_quality/contradictions.rs:58-67].

The file’s helper flow supports that orchestration: `section_claim_comparisons` walks provenance links and groups trimmed, non-empty claims by section and source/claim pair, while later helpers cover source-id extraction, model invocation, JSON payload parsing, finding sanitization, claim normalization, and AI-error conversion as summarized for the same file [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117]. Since this module has no child modules, collaboration happens within the single file between the provenance-to-comparison preparation, the detector/model boundary, and the cleanup step that prevents invalid or duplicate model output from leaking into the final citation-quality report.

## Call Diagram

```mermaid
sequenceDiagram
    participant m_00015808_7660_5129_8df1_45d4b9551ad1 as section_claim_comparisons &#91;function&#93;
    participant m_3f9168d3_a270_55ea_94b3_869c1e30d867 as contradiction_section &#91;function&#93;
    participant m_42bb8298_cf9c_5f55_bf79_b90f9e029496 as sanitize_contradiction_findings &#91;function&#93;
    participant m_4d7279dc_fc08_5ad6_b48a_9d2f0055630b as parse_contradiction_findings &#91;function&#93;
    participant m_665293c0_c6e7_5cb4_a1e3_a5a7c619abf8 as comparison_source_ids &#91;function&#93;
    participant m_82f3e4f9_5e64_5f94_84ff_2c0e0dbef37e as normalize_claim &#91;function&#93;
    participant m_af113876_ae59_5b3e_a8a7_d8ae1ee8e55e as extract_json_payload &#91;function&#93;
    participant m_eaa0b0ed_53a0_55a9_ae41_146efef7444b as model_contradiction_findings &#91;function&#93;
    m_00015808_7660_5129_8df1_45d4b9551ad1->>m_82f3e4f9_5e64_5f94_84ff_2c0e0dbef37e: calls
    m_3f9168d3_a270_55ea_94b3_869c1e30d867->>m_00015808_7660_5129_8df1_45d4b9551ad1: calls
    m_3f9168d3_a270_55ea_94b3_869c1e30d867->>m_42bb8298_cf9c_5f55_bf79_b90f9e029496: calls
    m_3f9168d3_a270_55ea_94b3_869c1e30d867->>m_665293c0_c6e7_5cb4_a1e3_a5a7c619abf8: calls
    m_42bb8298_cf9c_5f55_bf79_b90f9e029496->>m_82f3e4f9_5e64_5f94_84ff_2c0e0dbef37e: calls
    m_4d7279dc_fc08_5ad6_b48a_9d2f0055630b->>m_af113876_ae59_5b3e_a8a7_d8ae1ee8e55e: calls
    m_eaa0b0ed_53a0_55a9_ae41_146efef7444b->>m_4d7279dc_fc08_5ad6_b48a_9d2f0055630b: calls
```

## Files

- [[code/files/crates/gwiki/src/commands/citation_quality/contradictions.rs|crates/gwiki/src/commands/citation_quality/contradictions.rs]] - Implements contradiction detection for citation-quality checks. It groups provenance links into per-section `SectionClaimComparison` batches of `SourceClaim`s, keeps only sections with multiple distinct sources and claims, and either returns an unavailable/note-only `ContradictionSection` when AI is off or runs a detector/model path to produce contradiction findings. The AI path serializes comparisons into a prompt, parses JSON model output, then sanitizes findings against known source IDs by normalizing claims, deduplicating duplicates, and dropping invalid entries before assembling the final section result.
[crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117]

## Components

- `447c2c98-1319-598c-b131-61324a3128dd`
- `f19806e5-805c-5381-aeda-b5a7b540cc4e`
- `00bc49e9-22cf-564d-a891-453b46e339f5`
- `3f9168d3-a270-55ea-94b3-869c1e30d867`
- `00015808-7660-5129-8df1-45d4b9551ad1`
- `665293c0-c6e7-5cb4-a1e3-a5a7c619abf8`
- `eaa0b0ed-53a0-55a9-ae41-146efef7444b`
- `4d7279dc-fc08-5ad6-b48a-9d2f0055630b`
- `af113876-ae59-5b3e-a8a7-d8ae1ee8e55e`
- `42bb8298-cf9c-5f55-bf79-b90f9e029496`
- `82f3e4f9-5e64-5f94-84ff-2c0e0dbef37e`
- `d29a8ae5-f587-5f02-9b34-47622bbdc587`

