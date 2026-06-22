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

## `crates/gwiki/src/commands/citation_quality/contradictions`

This module is the AI-assisted contradiction-detection engine within the `citation_quality` command family. Its central responsibility is to examine a wiki's `ProvenanceGraph`, extract per-section claims attributed to distinct sources, invoke an AI detector, and return a structured `ContradictionSection` that the parent command can embed in a quality report. Because the module is entirely `pub(super)`, it acts as an internal implementation detail of the `citation_quality` command and exposes no surface area to the wider crate or binary.

The primary entry point is `contradiction_section` (contradictions.rs:30–62). When called it first gates on the `ai_available` flag; if AI is unavailable it returns early with a sentinel `ContradictionSection { available: false, … }` rather than fabricating findings (contradictions.rs:33–43). When AI is available it calls the private `section_claim_comparisons` helper (contradictions.rs:64+) to walk every link in the `ProvenanceGraph` and group `SourceClaim` records by section heading, producing a `Vec<SectionClaimComparison>`. Empty results short-circuit with an informational note (contradictions.rs:44–56). Non-empty comparisons are forwarded to a caller-supplied `detector` closure — a `FnMut(&[SectionClaimComparison]) -> Result<Vec<ContradictionFinding>, WikiError>` — which decouples the HTTP/daemon AI call from the logic here. Results are post-processed through `sanitize_contradiction_findings`, which filters any model-hallucinated source IDs against the canonical set gathered by `comparison_source_ids`.

The module collaborates outward through several `gobby_core` packages. It imports AI routing primitives (`daemon`, `effective_route`, `text`) from `gobby_core::ai` and context types from `gobby_core::ai_context` and `gobby_core::ai_types` (contradictions.rs:3–6), suggesting that the concrete detector closure passed in by the parent module wires those primitives to the actual model call. Configuration capability and routing enums (`AiCapability`, `AiRouting`) arrive from `gobby_core::config` (contradictions.rs:6). Inward, it depends on `crate::provenance::ProvenanceGraph` (contradictions.rs:9) to iterate citation links, and on `super::ContradictionFinding` and `super::ContradictionSection` (contradictions.rs:12) for the shared output types defined by the parent `citation_quality` module.

### Public (super) API symbols

| Symbol | Kind | Role |
|---|---|---|
| `SectionClaimComparison` | struct (Serialize) | Bundles a section heading with all per-source claims for AI input |
| `SectionClaimComparison::section` | field `String` | Section heading key |
| `SectionClaimComparison::claims` | field `Vec<SourceClaim>` | Ordered list of source claims for the section |
| `SourceClaim` | struct (Serialize) | Single source-attributed claim within a section |
| `SourceClaim::source_id` | field `String` | Identifier of the provenance source |
| `SourceClaim::claim` | field `String` | Extracted claim text |
| `contradiction_section` | fn `pub(super)` | Orchestrates detection; accepts provenance graph, AI flag, and detector closure |

### Key internal helpers (private)

| Symbol | Role |
|---|---|
| `ContradictionModelOutput` | Deserialize target for raw AI JSON (`findings` array) |
| `section_claim_comparisons` | Builds `Vec<SectionClaimComparison>` from `ProvenanceGraph` links |
| `comparison_source_ids` | Derives canonical `BTreeSet` of source IDs from comparisons |
| `sanitize_contradiction_findings` | Removes findings that reference source IDs not in the canonical set |
[crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67]
[crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/commands/citation_quality/contradictions.rs\|crates/gwiki/src/commands/citation_quality/contradictions.rs]] | `crates/gwiki/src/commands/citation_quality/contradictions.rs` exposes 12 indexed API symbols. |

