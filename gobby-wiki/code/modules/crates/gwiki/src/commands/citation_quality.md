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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18](crates/gwiki/src/commands/citation_quality/contradictions.rs#L15-L18), [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24](crates/gwiki/src/commands/citation_quality/contradictions.rs#L21-L24), [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29](crates/gwiki/src/commands/citation_quality/contradictions.rs#L27-L29), [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67](crates/gwiki/src/commands/citation_quality/contradictions.rs#L31-L67), [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117](crates/gwiki/src/commands/citation_quality/contradictions.rs#L69-L117), [crates/gwiki/src/commands/citation_quality/contradictions.rs:119-125](crates/gwiki/src/commands/citation_quality/contradictions.rs#L119-L125), [crates/gwiki/src/commands/citation_quality/contradictions.rs:127-163](crates/gwiki/src/commands/citation_quality/contradictions.rs#L127-L163), [crates/gwiki/src/commands/citation_quality/contradictions.rs:169-180](crates/gwiki/src/commands/citation_quality/contradictions.rs#L169-L180), [crates/gwiki/src/commands/citation_quality/contradictions.rs:182-193](crates/gwiki/src/commands/citation_quality/contradictions.rs#L182-L193), [crates/gwiki/src/commands/citation_quality/contradictions.rs:195-226](crates/gwiki/src/commands/citation_quality/contradictions.rs#L195-L226), [crates/gwiki/src/commands/citation_quality/contradictions.rs:228-234](crates/gwiki/src/commands/citation_quality/contradictions.rs#L228-L234), [crates/gwiki/src/commands/citation_quality/contradictions.rs:236-241](crates/gwiki/src/commands/citation_quality/contradictions.rs#L236-L241)

</details>

# crates/gwiki/src/commands/citation_quality

Parent: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

The citation_quality module identifies and builds citation-quality contradiction sections from provenance data and an AI-assisted contradiction detector [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18, 31-35]. In its key flow, the module evaluates whether AI-based contradiction detection is active [crates/gwiki/src/commands/citation_quality/contradictions.rs:36-40]. If enabled, it aggregates provenance links into per-section claim comparisons, isolating multi-source sections with distinct claims to submit to the AI detector [crates/gwiki/src/commands/citation_quality/contradictions.rs:48-52, 69-75].

For collaboration, this module acts as a bridge between the core provenance model and AI services, mapping `ProvenanceGraph` inputs to structured types like `SectionClaimComparison` and `SourceClaim` . It cleanses the detector's findings against known source IDs, normalizes claims, and safely propagates AI failures by translating them into the domain-specific `WikiError` results [crates/gwiki/src/commands/citation_quality/contradictions.rs:59-67].

| Module Symbol | Type | Description |
| --- | --- | --- |
| contradiction_section | Function | Evaluates provenance data for contradictions using an AI detector. [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-35] |
| SectionClaimComparison | Struct | Groups claims by section for multi-source AI comparison. [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18] |
| SourceClaim | Struct | Models a specific source ID and its corresponding text claim. [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/commands/citation_quality/contradictions.rs\|crates/gwiki/src/commands/citation_quality/contradictions.rs]] | Builds the citation-quality contradiction section from provenance data and an AI detector. It first checks whether AI contradiction detection is available, then groups provenance links into per-section claim comparisons so only multi-source sections with distinct claims are sent to the detector. The detector’s output is parsed from JSON, cleaned against the known source IDs and normalized claims, and wrapped into a `ContradictionSection` result. The helper types model section-level comparisons and per-source claims, while the remaining helpers handle comparison collection, source ID extraction, model-output parsing, claim normalization, and conversion of AI errors into `WikiError`. [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18] [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24] [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29] [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67] [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117] |

## Components

| Component ID |
| --- |
| `447c2c98-1319-598c-b131-61324a3128dd` |
| `f19806e5-805c-5381-aeda-b5a7b540cc4e` |
| `00bc49e9-22cf-564d-a891-453b46e339f5` |
| `3f9168d3-a270-55ea-94b3-869c1e30d867` |
| `00015808-7660-5129-8df1-45d4b9551ad1` |
| `665293c0-c6e7-5cb4-a1e3-a5a7c619abf8` |
| `eaa0b0ed-53a0-55a9-ae41-146efef7444b` |
| `4d7279dc-fc08-5ad6-b48a-9d2f0055630b` |
| `af113876-ae59-5b3e-a8a7-d8ae1ee8e55e` |
| `42bb8298-cf9c-5f55-bf79-b90f9e029496` |
| `82f3e4f9-5e64-5f94-84ff-2c0e0dbef37e` |
| `d29a8ae5-f587-5f02-9b34-47622bbdc587` |
