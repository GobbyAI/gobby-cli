---
title: crates/gwiki/src/commands/citation_quality.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/citation_quality.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/citation_quality.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Overview

`crates/gwiki/src/commands/citation_quality.rs` exposes 44 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/citation_quality.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CitationQualityReport` | class | A 'CitationQualityReport' is an internal report object that records the originating command, analysis scope, artifact output path, dependency metadata, per-section citation quality results, and generated markdown summary. [crates/gwiki/src/commands/citation_quality.rs:26-33] |
| `DependencyMetadata` | class | 'DependencyMetadata' is an internal struct that groups dependency identifiers into three static string slices vectors: 'hard', 'optional', and 'multimodal'. [crates/gwiki/src/commands/citation_quality.rs:36-40] |
| `CitationQualitySections` | class | 'CitationQualitySections' is an internal aggregate struct that groups five citation-evaluation subsections: credibility, coverage gaps, contradictions, stale sources, and confidence. [crates/gwiki/src/commands/citation_quality.rs:43-49] |
| `CredibilitySection` | class | 'CredibilitySection' is a crate-visible data structure that records whether credibility information is available, an optional explanatory note, and a list of per-source credibility entries. [crates/gwiki/src/commands/citation_quality.rs:52-56] |
| `SourceCredibility` | class | 'SourceCredibility' is a crate-private data structure that records a source identifier, its location, a 'u8' credibility score, and a list of string-based signals supporting that score. [crates/gwiki/src/commands/citation_quality.rs:59-64] |
| `CoverageGapSection` | class | 'CoverageGapSection' is a crate-visible struct that records whether coverage-gap data is available and, if so, stores the gaps as a 'Vec<CoverageGap>'. [crates/gwiki/src/commands/citation_quality.rs:67-70] |
| `CoverageGap` | class | 'CoverageGap' is a crate-visible struct that records a coverage gap by storing the affected 'section' and a 'reason' explaining why coverage is missing. [crates/gwiki/src/commands/citation_quality.rs:73-76] |
| `ContradictionSection` | class | 'ContradictionSection' is a crate-visible data structure that records whether contradiction analysis is available, an optional explanatory note, and a list of 'ContradictionFinding' entries. [crates/gwiki/src/commands/citation_quality.rs:79-83] |
| `ContradictionFinding` | class | 'ContradictionFinding' is a crate-private struct that represents a detected contradiction as a 'claim' string paired with a list of contributing 'source_ids' strings. [crates/gwiki/src/commands/citation_quality.rs:86-89] |
| `StaleSourceSection` | class | 'StaleSourceSection' is a crate-private record that tracks whether a source section is still available and accumulates any associated 'StaleSourceWarning' entries. [crates/gwiki/src/commands/citation_quality.rs:92-95] |
| `StaleSourceWarning` | class | 'StaleSourceWarning' is an internal warning record that identifies a stale source by its 'source_id' and associated 'location'. [crates/gwiki/src/commands/citation_quality.rs:98-101] |
| `ConfidenceSection` | class | 'ConfidenceSection' is an internal Rust struct that records whether confidence data is available and stores a list of 'OutputConfidence' entries for the section. [crates/gwiki/src/commands/citation_quality.rs:104-107] |
| `OutputConfidence` | class | 'OutputConfidence' is a crate-private struct that pairs a static output string with an optional 'f32' confidence score and a free-form explanatory 'String'. [crates/gwiki/src/commands/citation_quality.rs:110-114] |
| `execute` | function | Validates that the 'gwiki citation-quality' Postgres index is attached, resolves the selection context, detects AI text-generation availability with a warning fallback, builds the citation-quality report, writes its artifact, serializes the report to JSON, and returns a scoped 'CommandOutcome' or 'WikiError'. [crates/gwiki/src/commands/citation_quality.rs:116-146] |
| `text_generation_available` | function | Returns 'Ok(true)' if the resolved AI routing for 'AiCapability::TextGenerate' is either 'Direct' or 'Daemon', and 'Ok(false)' otherwise, after loading the '"gwiki citation-quality"' hub AI config source and resolving the AI context. [crates/gwiki/src/commands/citation_quality.rs:148-162] |
| `build_report` | function | 'build_report' delegates to 'build_report_with_contradiction_detector', passing 'vault_root', 'scope', 'ai_available', and the 'model_contradiction_findings' detector to produce a 'Result<CitationQualityReport, WikiError>'. [crates/gwiki/src/commands/citation_quality.rs:164-175] |
| `build_report_with_contradiction_detector` | function | Build_report_with_contradiction_detector reads vault source, provenance, and health data for a given scope, computes credibility, coverage gaps, contradictions via an injected detector callback, stale-source and confidence sections, renders a citation-quality markdown report, and returns it as a 'CitationQualityReport' with dependency metadata and a fixed output path. [crates/gwiki/src/commands/citation_quality.rs:177-222] |
| `credibility_section` | function | Builds a 'CredibilitySection' by returning unavailable with a note when 'sources' is empty, otherwise evaluating each source’s credibility from type, age, publisher, and corroboration in the 'ProvenanceGraph' and returning the scored per-source results. [crates/gwiki/src/commands/citation_quality.rs:224-264] |
| `credibility_source_type` | function | Maps a 'SourceKind' to a 'CredibilitySourceType' by classifying 'ResearchNote' as 'Academic', 'MediaWiki'/'Markdown' as 'Community', 'Url'/'Html' as 'News', 'Pdf'/'Office'/'GitRepository' as 'Official', and all other variants as 'Unknown'. [crates/gwiki/src/commands/citation_quality.rs:266-276] |
| `source_age_days` | function | Parses 'source.fetched_at' as an RFC3339 timestamp and returns the non-negative whole number of days elapsed since then, clamped to 'u16::MAX', or 'None' if parsing fails. [crates/gwiki/src/commands/citation_quality.rs:278-285] |
| `corroborating_sources` | function | Returns a deduplicated, lexicographically sorted 'Vec<String>' of other source IDs that are linked in the provenance graph to any section referenced by the given 'source'. [crates/gwiki/src/commands/citation_quality.rs:287-302] |
| `coverage_gap_section` | function | Scans all pages within the given scope and returns a 'CoverageGapSection' listing headings whose corresponding section IDs have no provenance section-to-source links, formatting each gap as 'path#slug' with a fixed “No provenance section-to-source links found.” reason. [crates/gwiki/src/commands/citation_quality.rs:304-335] |
| `stale_source_section` | function | Constructs a 'StaleSourceSection' marked 'available: true' and populates its 'warnings' by mapping each 'report.stale_citations' issue into a 'StaleSourceWarning' containing the issue’s cloned 'source_id' and 'location'. [crates/gwiki/src/commands/citation_quality.rs:337-349] |
| `confidence_section` | function | Constructs a 'ConfidenceSection' marked available with four 'OutputConfidence' entries, deriving each output’s confidence from the corresponding section state and helper functions. [crates/gwiki/src/commands/citation_quality.rs:351-383] |

_13 more symbol(s) not shown — run `gcode outline crates/gwiki/src/commands/citation_quality.rs` for the full list._

_Verified by 7 in-file unit tests._

