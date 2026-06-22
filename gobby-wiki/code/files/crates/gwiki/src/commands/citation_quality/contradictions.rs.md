---
title: crates/gwiki/src/commands/citation_quality/contradictions.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/citation_quality/contradictions.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/citation_quality/contradictions.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/citation_quality/contradictions.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/citation_quality/contradictions.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SectionClaimComparison` | class | 'SectionClaimComparison' is a visibility-restricted struct that groups a section identifier ('String') with the set of associated source claims ('Vec<SourceClaim>'). [crates/gwiki/src/commands/citation_quality/contradictions.rs:15-18] |
| `SourceClaim` | class | 'SourceClaim' is an internal struct that pairs a 'source_id: String' with a 'claim: String', representing a claim attributed to a specific source. [crates/gwiki/src/commands/citation_quality/contradictions.rs:21-24] |
| `ContradictionModelOutput` | class | 'ContradictionModelOutput' is a struct that encapsulates a collection of 'ContradictionFinding' values in its 'findings' field. [crates/gwiki/src/commands/citation_quality/contradictions.rs:27-29] |
| `contradiction_section` | function | Builds a 'ContradictionSection' by short-circuiting when AI detection is unavailable or there are no multi-source conflicting claims, otherwise generating section claim comparisons, running the provided detector, sanitizing the findings against source IDs, and returning the available findings with no note. [crates/gwiki/src/commands/citation_quality/contradictions.rs:31-67] |
| `section_claim_comparisons` | function | Builds a section-keyed, deduplicated map of nonempty claims from 'provenance.links()', then returns only those sections that have at least two distinct sources and at least two distinct normalized claims as 'SectionClaimComparison' records. [crates/gwiki/src/commands/citation_quality/contradictions.rs:69-117] |
| `comparison_source_ids` | function | Returns a 'BTreeSet<String>' containing the unique 'source_id' values cloned from all claims across all provided 'SectionClaimComparison' entries. [crates/gwiki/src/commands/citation_quality/contradictions.rs:119-125] |
| `model_contradiction_findings` | function | Builds a JSON prompt from 'SectionClaimComparison' inputs, routes it to the AI text generator when enabled, and parses the response into 'Vec<ContradictionFinding>', returning an empty list if AI routing is off or auto. [crates/gwiki/src/commands/citation_quality/contradictions.rs:127-163] |
| `parse_contradiction_findings` | function | Extracts a JSON payload from 'text', deserializes it into 'ContradictionModelOutput', maps any parse failure to 'WikiError::Json' with action '"parse contradiction detection response"', and returns 'output.findings'. [crates/gwiki/src/commands/citation_quality/contradictions.rs:169-180] |
| `extract_json_payload` | function | Returns the input trimmed of surrounding whitespace, and if it is wrapped in triple single quotes optionally prefixed with 'json', returns the inner content trimmed as a presumed JSON payload. [crates/gwiki/src/commands/citation_quality/contradictions.rs:182-193] |
| `sanitize_contradiction_findings` | function | Removes empty or under-supported contradiction findings by trimming the claim and source IDs, keeping only allowed source IDs, requiring at least two unique sources, and deduplicating results by normalized claim plus sorted source ID list. [crates/gwiki/src/commands/citation_quality/contradictions.rs:195-226] |
| `normalize_claim` | function | Returns a lowercase copy of 'claim' with all runs of whitespace collapsed to single spaces and leading/trailing whitespace removed. [crates/gwiki/src/commands/citation_quality/contradictions.rs:228-234] |
| `ai_error_to_wiki_error` | function | Converts an 'AiError' into a 'WikiError::Daemon' with the fixed endpoint 'gcore::ai/text-generate' and the error’s stringified message. [crates/gwiki/src/commands/citation_quality/contradictions.rs:236-241] |

