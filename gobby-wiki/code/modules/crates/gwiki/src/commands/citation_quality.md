---
title: crates/gwiki/src/commands/citation_quality
type: code_module
provenance:
- file: crates/gwiki/src/commands/citation_quality/contradictions.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/citation_quality

Parent: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

`crates/gwiki/src/commands/citation_quality/contradictions.rs` builds the contradiction-detection portion of citation quality reporting. Its main entry point, `contradiction_section`, accepts a `ProvenanceGraph`, an AI availability flag, and an injected detector callback, then returns a `ContradictionSection` for the parent command layer (crates/gwiki/src/commands/citation_quality/contradictions.rs:27-65). It explicitly avoids inventing results when AI is unavailable, returning an unavailable section with a note and no findings (crates/gwiki/src/commands/citation_quality/contradictions.rs:31-41).

The core flow derives per-section source claim comparisons from provenance, skips sections that do not have usable multi-source claim data, gathers valid source IDs, invokes the detector, and sanitizes returned findings against those source IDs before exposing them (crates/gwiki/src/commands/citation_quality/contradictions.rs:43-65). The module’s data contracts are small: `SectionClaimComparison` groups claims by section, while `SourceClaim` records each contributing `source_id` and claim text (crates/gwiki/src/commands/citation_quality/contradictions.rs:12-23). Model output is deserialized through `ContradictionModelOutput`, which contains a list of `ContradictionFinding` values (crates/gwiki/src/commands/citation_quality/contradictions.rs:25-26).

Within the wider system, this module collaborates with the citation-quality parent module through `ContradictionFinding` and `ContradictionSection`, imports provenance data from `crate::provenance::ProvenanceGraph`, and reports failures using `crate::WikiError` (crates/gwiki/src/commands/citation_quality/contradictions.rs:8-11). It also imports Gobby AI routing, daemon, text, context, capability, routing, and error types, indicating that contradiction detection can be backed by the shared AI infrastructure (crates/gwiki/src/commands/citation_quality/contradictions.rs:3-7).

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SectionClaimComparison` | Struct | Groups source claims for one section (crates/gwiki/src/commands/citation_quality/contradictions.rs:12-16). |
| `SourceClaim` | Struct | Holds a `source_id` and claim string (crates/gwiki/src/commands/citation_quality/contradictions.rs:19-23). |
| `ContradictionModelOutput` | Struct | Deserializes model findings (crates/gwiki/src/commands/citation_quality/contradictions.rs:25-26). |
| `contradiction_section` | Function | Produces the contradiction report section from provenance and detector output (crates/gwiki/src/commands/citation_quality/contradictions.rs:27-65). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/commands/citation_quality/contradictions.rs\|crates/gwiki/src/commands/citation_quality/contradictions.rs]] | `crates/gwiki/src/commands/citation_quality/contradictions.rs` exposes 12 indexed API symbols. |

