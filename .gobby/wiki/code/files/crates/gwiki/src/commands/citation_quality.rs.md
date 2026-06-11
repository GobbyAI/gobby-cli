---
title: crates/gwiki/src/commands/citation_quality.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/citation_quality.rs
  ranges:
  - 20-27
  - 30-34
  - 37-43
  - 46-50
  - 53-58
  - 61-64
  - 67-70
  - 73-77
  - 80-83
  - 86-89
  - 92-95
  - 98-101
  - 104-108
  - 110-140
  - 142-156
  - 158-198
  - 200-240
  - 242-252
  - 254-261
  - 263-278
  - 280-311
  - 313-342
  - 344-356
  - 358-390
  - 392-402
  - 404-410
  - 412-423
  - 425-435
  - 437-461
  - 463-477
  - 479-490
  - 492-511
  - 513-524
  - 526-539
  - 541-555
  - 569-579
  - 582-646
  - 649-693
  - 696-725
  - 729-748
  - 750-754
  - 756-771
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/citation_quality.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/citation_quality.rs` exposes 42 indexed API symbols.
[crates/gwiki/src/commands/citation_quality.rs:20-27]
[crates/gwiki/src/commands/citation_quality.rs:30-34]
[crates/gwiki/src/commands/citation_quality.rs:37-43]
[crates/gwiki/src/commands/citation_quality.rs:46-50]
[crates/gwiki/src/commands/citation_quality.rs:53-58]

## API Symbols

- `CitationQualityReport` (class) component `CitationQualityReport [class]` (`0626884e-2a39-5b13-b8be-fe2a57a323b5`) lines 20-27 [crates/gwiki/src/commands/citation_quality.rs:20-27]
  - Signature: `pub(crate) struct CitationQualityReport {`
  - Purpose: `CitationQualityReport` is a crate-private struct that encapsulates citation quality assessment data, comprising command metadata, scope identity, artifact path, dependency metadata, quality sections, and markdown representation. [crates/gwiki/src/commands/citation_quality.rs:20-27]
- `DependencyMetadata` (class) component `DependencyMetadata [class]` (`4d6ab4f4-97a7-5bbf-90a5-02351c47012a`) lines 30-34 [crates/gwiki/src/commands/citation_quality.rs:30-34]
  - Signature: `pub(crate) struct DependencyMetadata {`
  - Purpose: `DependencyMetadata` is a crate-private struct that categorizes static string references into three dependency types—hard (required), optional, and multimodal—via separate vector fields. [crates/gwiki/src/commands/citation_quality.rs:30-34]
- `CitationQualitySections` (class) component `CitationQualitySections [class]` (`b6893647-b28f-52f7-b4cb-e8b387a066d1`) lines 37-43 [crates/gwiki/src/commands/citation_quality.rs:37-43]
  - Signature: `pub(crate) struct CitationQualitySections {`
  - Purpose: A crate-scoped aggregate struct that consolidates five citation quality assessment sections evaluating credibility, coverage gaps, contradictions, source staleness, and confidence. [crates/gwiki/src/commands/citation_quality.rs:37-43]
- `CredibilitySection` (class) component `CredibilitySection [class]` (`eab22ee9-b78f-5362-8512-c02750d592ed`) lines 46-50 [crates/gwiki/src/commands/citation_quality.rs:46-50]
  - Signature: `pub(crate) struct CredibilitySection {`
  - Purpose: `CredibilitySection` is a crate-private struct that aggregates credibility metadata comprising an availability flag, an optional descriptive note, and a vector of source credibility objects. [crates/gwiki/src/commands/citation_quality.rs:46-50]
- `SourceCredibility` (class) component `SourceCredibility [class]` (`41de8c78-cd5c-5125-b118-36c75c4a16cd`) lines 53-58 [crates/gwiki/src/commands/citation_quality.rs:53-58]
  - Signature: `pub(crate) struct SourceCredibility {`
  - Purpose: `SourceCredibility` is a crate-private struct that encapsulates credibility assessment metadata for an information source, including its identifier, geographic location, a byte-valued credibility score (0-255), and supporting evidence signals. [crates/gwiki/src/commands/citation_quality.rs:53-58]
- `CoverageGapSection` (class) component `CoverageGapSection [class]` (`8842ec53-618e-537f-8190-dfcdc6b6320e`) lines 61-64 [crates/gwiki/src/commands/citation_quality.rs:61-64]
  - Signature: `pub(crate) struct CoverageGapSection {`
  - Purpose: CoverageGapSection is a crate-private struct that aggregates an availability flag with a vector of CoverageGap instances. [crates/gwiki/src/commands/citation_quality.rs:61-64]
- `CoverageGap` (class) component `CoverageGap [class]` (`ed3d3b65-5f63-5cd4-8b36-f0a86463f567`) lines 67-70 [crates/gwiki/src/commands/citation_quality.rs:67-70]
  - Signature: `pub(crate) struct CoverageGap {`
  - Purpose: `CoverageGap` is a crate-private struct that encapsulates a coverage gap with two String fields identifying the affected section and the reason for the gap. [crates/gwiki/src/commands/citation_quality.rs:67-70]
- `ContradictionSection` (class) component `ContradictionSection [class]` (`5e572abe-a3f9-54a3-a16f-19d452378a59`) lines 73-77 [crates/gwiki/src/commands/citation_quality.rs:73-77]
  - Signature: `pub(crate) struct ContradictionSection {`
  - Purpose: `ContradictionSection` is a crate-private struct that encapsulates contradiction analysis results, consisting of an availability flag, optional descriptive note, and a vector of individual contradiction findings. [crates/gwiki/src/commands/citation_quality.rs:73-77]
- `ContradictionFinding` (class) component `ContradictionFinding [class]` (`8e617206-485c-50ee-92ce-fa8a8677d58b`) lines 80-83 [crates/gwiki/src/commands/citation_quality.rs:80-83]
  - Signature: `pub(crate) struct ContradictionFinding {`
  - Purpose: `ContradictionFinding` is a crate-scoped struct that encapsulates a contradictory claim paired with a vector of source identifiers that refute it. [crates/gwiki/src/commands/citation_quality.rs:80-83]
- `StaleSourceSection` (class) component `StaleSourceSection [class]` (`70df4638-9e5b-5f9f-a13d-e015e7271c66`) lines 86-89 [crates/gwiki/src/commands/citation_quality.rs:86-89]
  - Signature: `pub(crate) struct StaleSourceSection {`
  - Purpose: A crate-private struct that encapsulates an availability flag and a collection of staleness warnings for a source section. [crates/gwiki/src/commands/citation_quality.rs:86-89]
- `StaleSourceWarning` (class) component `StaleSourceWarning [class]` (`83031209-71fe-54c0-bb2e-ea5a5564f899`) lines 92-95 [crates/gwiki/src/commands/citation_quality.rs:92-95]
  - Signature: `pub(crate) struct StaleSourceWarning {`
  - Purpose: `StaleSourceWarning` is a crate-private struct that encapsulates a warning about an outdated data source, storing its identifier and location as `String` fields. [crates/gwiki/src/commands/citation_quality.rs:92-95]
- `ConfidenceSection` (class) component `ConfidenceSection [class]` (`0f069f69-41dd-59c9-a031-239e2cc75c1d`) lines 98-101 [crates/gwiki/src/commands/citation_quality.rs:98-101]
  - Signature: `pub(crate) struct ConfidenceSection {`
  - Purpose: A crate-private struct that groups a boolean availability indicator with a vector of `OutputConfidence` elements. [crates/gwiki/src/commands/citation_quality.rs:98-101]
- `OutputConfidence` (class) component `OutputConfidence [class]` (`a195ed81-8b38-5a14-bd6b-dcfd0b301a29`) lines 104-108 [crates/gwiki/src/commands/citation_quality.rs:104-108]
  - Signature: `pub(crate) struct OutputConfidence {`
  - Purpose: `OutputConfidence` is a crate-internal struct that bundles a static string output with an optional floating-point confidence score and an explanatory string. [crates/gwiki/src/commands/citation_quality.rs:104-108]
- `execute` (function) component `execute [function]` (`1e42fbe5-22cc-5759-830d-ebf26d9a3e21`) lines 110-140 [crates/gwiki/src/commands/citation_quality.rs:110-140]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Generates, persists, and returns a serialized citation-quality report for a resolved scope selection with optional AI diagnostics. [crates/gwiki/src/commands/citation_quality.rs:110-140]
- `text_generation_available` (function) component `text_generation_available [function]` (`7596b9e5-83f6-531d-9ce2-018430bcc015`) lines 142-156 [crates/gwiki/src/commands/citation_quality.rs:142-156]
  - Signature: `fn text_generation_available() -> Result<bool, WikiError> {`
  - Purpose: Verifies text generation availability by checking whether the effective AI route for TextGenerate capability is Direct or Daemon. [crates/gwiki/src/commands/citation_quality.rs:142-156]
- `build_report` (function) component `build_report [function]` (`0990c152-2b93-596f-87c6-2ef0a3ed9e1d`) lines 158-198 [crates/gwiki/src/commands/citation_quality.rs:158-198]
  - Signature: `pub(crate) fn build_report(`
  - Purpose: Generates a CitationQualityReport by analyzing vault provenance, health, and manifest data to assess citation credibility, coverage gaps, contradictions, source staleness, and aggregate confidence metrics. [crates/gwiki/src/commands/citation_quality.rs:158-198]
- `credibility_section` (function) component `credibility_section [function]` (`c897a3f9-4a94-5875-b486-7e6a712abbfa`) lines 200-240 [crates/gwiki/src/commands/citation_quality.rs:200-240]
  - Signature: `fn credibility_section(`
  - Purpose: Evaluates credibility scores and signals for each source record using a CredibilityScore evaluator, returning a CredibilitySection containing scored sources or an unavailability notification if no sources exist. [crates/gwiki/src/commands/citation_quality.rs:200-240]
- `credibility_source_type` (function) component `credibility_source_type [function]` (`fc6d3878-6985-56ee-ad0b-3e03a1cbe250`) lines 242-252 [crates/gwiki/src/commands/citation_quality.rs:242-252]
  - Signature: `fn credibility_source_type(kind: &SourceKind) -> CredibilitySourceType {`
  - Purpose: Maps `SourceKind` variants to corresponding `CredibilitySourceType` classifications (Academic, Community, News, Official, or Unknown) through exhaustive pattern matching. [crates/gwiki/src/commands/citation_quality.rs:242-252]
- `source_age_days` (function) component `source_age_days [function]` (`90944aa9-9f86-53d6-b27c-2831af608c9d`) lines 254-261 [crates/gwiki/src/commands/citation_quality.rs:254-261]
  - Signature: `fn source_age_days(source: &SourceRecord) -> Option<u16> {`
  - Purpose: Calculates the number of days elapsed since a `SourceRecord` was fetched, clamping the result to `u16::MAX` and returning `None` if the RFC3339 timestamp cannot be parsed. [crates/gwiki/src/commands/citation_quality.rs:254-261]
- `corroborating_sources` (function) component `corroborating_sources [function]` (`78069b76-6b5d-5b35-a827-b621bf7ad99c`) lines 263-278 [crates/gwiki/src/commands/citation_quality.rs:263-278]
  - Signature: `fn corroborating_sources(source: &SourceRecord, provenance: &ProvenanceGraph) -> Vec<String> {`
  - Purpose: Returns a deduplicated vector of all source IDs (excluding the input source) that reference at least one of the same sections in the provenance graph. [crates/gwiki/src/commands/citation_quality.rs:263-278]
- `coverage_gap_section` (function) component `coverage_gap_section [function]` (`9da63a7d-cfb0-5b78-89c4-d7196be2fd57`) lines 280-311 [crates/gwiki/src/commands/citation_quality.rs:280-311]
  - Signature: `fn coverage_gap_section(`
  - Purpose: Identifies all page sections within a specified scope that lack provenance section-to-source links and returns them as coverage gaps. [crates/gwiki/src/commands/citation_quality.rs:280-311]
- `contradiction_section` (function) component `contradiction_section [function]` (`29a3503d-7ef2-560f-ae80-ff22017c0f92`) lines 313-342 [crates/gwiki/src/commands/citation_quality.rs:313-342]
  - Signature: `fn contradiction_section(`
  - Purpose: Returns a `ContradictionSection` marked as unavailable with empty findings, either because AI is unavailable or because the contradiction detection feature is not yet implemented. [crates/gwiki/src/commands/citation_quality.rs:313-342]
- `stale_source_section` (function) component `stale_source_section [function]` (`eb5a04cf-4496-5e9e-b530-02d5362fc11c`) lines 344-356 [crates/gwiki/src/commands/citation_quality.rs:344-356]
  - Signature: `fn stale_source_section(report: &health::HealthReport) -> StaleSourceSection {`
  - Purpose: Maps stale citations from a `HealthReport` into a `StaleSourceSection` containing warnings with cloned source IDs and locations. [crates/gwiki/src/commands/citation_quality.rs:344-356]
- `confidence_section` (function) component `confidence_section [function]` (`cd112861-f84d-5fa7-a6c6-f27d2ed2259e`) lines 358-390 [crates/gwiki/src/commands/citation_quality.rs:358-390]
  - Signature: `fn confidence_section(`
  - Purpose: Constructs a `ConfidenceSection` by computing and aggregating confidence scores and explanations for credibility, coverage gaps, contradictions, and stale sources from their respective input assessment sections. [crates/gwiki/src/commands/citation_quality.rs:358-390]
- `average_credibility` (function) component `average_credibility [function]` (`edc9c408-4130-5875-b270-bb9922b14a4d`) lines 392-402 [crates/gwiki/src/commands/citation_quality.rs:392-402]
  - Signature: `fn average_credibility(section: &CredibilitySection) -> Option<f32> {`
  - Purpose: Returns the average of normalized credibility scores (scaled to 0–1 range) from a section's sources, or `None` if the section is unavailable or lacks sources. [crates/gwiki/src/commands/citation_quality.rs:392-402]
- `confidence_explanation` (function) component `confidence_explanation [function]` (`c5a784e1-5b36-5340-9262-9cb2d4707c7d`) lines 404-410 [crates/gwiki/src/commands/citation_quality.rs:404-410]
  - Signature: `fn confidence_explanation(available: bool) -> String {`
  - Purpose: This function returns a diagnostic message string indicating whether optional input signals are available, returning a nominal status message if true or a degradation notification if false. [crates/gwiki/src/commands/citation_quality.rs:404-410]
- `section_id_for` (function) component `section_id_for [function]` (`268b404c-fc69-5458-aa32-ad59a5d166b3`) lines 412-423 [crates/gwiki/src/commands/citation_quality.rs:412-423]
  - Signature: `fn section_id_for(page_path: &Path, heading: &str) -> String {`
  - Purpose: Generates a section ID by slugifying the page filename for "Overview" headings to ensure page-level uniqueness, otherwise slugifies the heading text directly. [crates/gwiki/src/commands/citation_quality.rs:412-423]
- `page_slugify` (function) component `page_slugify [function]` (`1d19baa0-950a-58e5-8bda-1fe3b3eab775`) lines 425-435 [crates/gwiki/src/commands/citation_quality.rs:425-435]
  - Signature: `fn page_slugify(value: &str) -> String {`
  - Purpose: Converts a string to a lowercase URL-friendly slug by retaining ASCII alphanumeric characters, collapsing non-alphanumeric sequences into single hyphens, and trimming boundary hyphens. [crates/gwiki/src/commands/citation_quality.rs:425-435]
- `render_markdown` (function) component `render_markdown [function]` (`24ded5e4-8e5b-5063-9134-6e7a0d0d3f50`) lines 437-461 [crates/gwiki/src/commands/citation_quality.rs:437-461]
  - Signature: `fn render_markdown(`
  - Purpose: Constructs and returns a markdown-formatted citation quality report that aggregates scope identification, dependency classification, and quality assessment sections (credibility, coverage gaps, contradictions, stale sources, and confidence metrics). [crates/gwiki/src/commands/citation_quality.rs:437-461]
- `render_credibility` (function) component `render_credibility [function]` (`ae2cd9ba-0679-5081-8da5-934c8579a7fa`) lines 463-477 [crates/gwiki/src/commands/citation_quality.rs:463-477]
  - Signature: `fn render_credibility(markdown: &mut String, section: &CredibilitySection) {`
  - Purpose: Renders a credibility section into markdown format by appending an availability status, optional note, and a formatted list of sources with their identifiers, scores, and locations to a string. [crates/gwiki/src/commands/citation_quality.rs:463-477]
- `render_coverage` (function) component `render_coverage [function]` (`94402ab5-5e26-51eb-86b6-12e5d1b1b9e5`) lines 479-490 [crates/gwiki/src/commands/citation_quality.rs:479-490]
  - Signature: `fn render_coverage(markdown: &mut String, section: &CoverageGapSection) {`
  - Purpose: Appends a markdown-formatted coverage gaps section to a mutable string, including availability status and either a formatted list of detected gaps or a no-gaps message. [crates/gwiki/src/commands/citation_quality.rs:479-490]
- `render_contradictions` (function) component `render_contradictions [function]` (`db583e89-4c59-55ae-b707-af3e2f6dd28b`) lines 492-511 [crates/gwiki/src/commands/citation_quality.rs:492-511]
  - Signature: `fn render_contradictions(markdown: &mut String, section: &ContradictionSection) {`
  - Purpose: Appends a markdown-formatted contradictions section to a string buffer, containing availability status, optional notes, and a list of claims paired with their conflicting source IDs. [crates/gwiki/src/commands/citation_quality.rs:492-511]
- `render_stale_sources` (function) component `render_stale_sources [function]` (`c160fbdf-7ede-5730-8983-cce3fc53cc6b`) lines 513-524 [crates/gwiki/src/commands/citation_quality.rs:513-524]
  - Signature: `fn render_stale_sources(markdown: &mut String, section: &StaleSourceSection) {`
  - Purpose: Appends a markdown-formatted "Stale Source Warnings" section to a string, listing each warning's source ID and location or indicating no stale sources if the warnings list is empty. [crates/gwiki/src/commands/citation_quality.rs:513-524]
- `render_confidence` (function) component `render_confidence [function]` (`c2c5650f-3299-571d-bec8-dad5ca48fd93`) lines 526-539 [crates/gwiki/src/commands/citation_quality.rs:526-539]
  - Signature: `fn render_confidence(markdown: &mut String, section: &ConfidenceSection) {`
  - Purpose: Appends a markdown-formatted confidence report to a String by iterating through outputs in a ConfidenceSection and formatting each output's confidence value (to 2 decimal places or "n/a") with its explanation. [crates/gwiki/src/commands/citation_quality.rs:526-539]
- `write_artifact` (function) component `write_artifact [function]` (`da0c555c-8859-59fb-b9c6-f5f25ec9fa67`) lines 541-555 [crates/gwiki/src/commands/citation_quality.rs:541-555]
  - Signature: `fn write_artifact(root: &Path, relative_path: &Path, markdown: &str) -> Result<(), WikiError> {`
  - Purpose: Writes markdown content to a file at the path formed by joining `root` and `relative_path`, creating parent directories as needed and returning a `WikiError` on I/O failure. [crates/gwiki/src/commands/citation_quality.rs:541-555]
- `citation_quality_execute_requires_postgresql_index` (function) component `citation_quality_execute_requires_postgresql_index [function]` (`55fc8cf0-0de7-5e3f-96f5-2aabfc861b4d`) lines 569-579 [crates/gwiki/src/commands/citation_quality.rs:569-579]
  - Signature: `fn citation_quality_execute_requires_postgresql_index() {`
  - Purpose: This test verifies that the `execute()` function fails with a `WikiError::Config` containing "PostgreSQL index is required" when PostgreSQL database configuration environment variables are unset. [crates/gwiki/src/commands/citation_quality.rs:569-579]
- `citation_quality_report_covers_sections_and_degradation` (function) component `citation_quality_report_covers_sections_and_degradation [function]` (`65cdbf4d-9d36-570b-91d4-215fe2b39a9f`) lines 582-646 [crates/gwiki/src/commands/citation_quality.rs:582-646]
  - Signature: `fn citation_quality_report_covers_sections_and_degradation() {`
  - Purpose: This test function verifies that `build_report()` correctly generates a citation quality report that identifies unsourced sections (coverage gaps) and tracks citation degradation across multiple wiki pages in the provenance graph. [crates/gwiki/src/commands/citation_quality.rs:582-646]
- `citation_quality_report_ignores_repeated_support_when_ai_available` (function) component `citation_quality_report_ignores_repeated_support_when_ai_available [function]` (`335de342-e361-5101-b6bd-999ede97b45e`) lines 649-693 [crates/gwiki/src/commands/citation_quality.rs:649-693]
  - Signature: `fn citation_quality_report_ignores_repeated_support_when_ai_available() {`
  - Purpose: # Summary

This test verifies that the citation quality report builder deduplicates identical claims supported by multiple sources when AI analysis is enabled, suppressing redundant citation detection. [crates/gwiki/src/commands/citation_quality.rs:649-693]
- `citation_quality_coverage_gaps_apply_selected_scope` (function) component `citation_quality_coverage_gaps_apply_selected_scope [function]` (`d5f96ff7-6caf-58d8-8806-2a69dc1b40b8`) lines 696-725 [crates/gwiki/src/commands/citation_quality.rs:696-725]
  - Signature: `fn citation_quality_coverage_gaps_apply_selected_scope() {`
  - Purpose: This test verifies that coverage gap analysis correctly applies scope filtering to include only missing citations from selected resource types (topics) while excluding unselected types (concepts). [crates/gwiki/src/commands/citation_quality.rs:696-725]
- `citation_quality_requires_configured_postgres_index` (function) component `citation_quality_requires_configured_postgres_index [function]` (`488c0e48-0dcd-5b75-a9c9-a017830605e1`) lines 729-748 [crates/gwiki/src/commands/citation_quality.rs:729-748]
  - Signature: `fn citation_quality_requires_configured_postgres_index() {`
  - Purpose: This unit test verifies that the citation-quality indexing feature properly fails with an appropriate error when PostgreSQL database connectivity is unavailable. [crates/gwiki/src/commands/citation_quality.rs:729-748]
- `write_page` (function) component `write_page [function]` (`45b73007-069d-5f30-99a3-e54b7d25c8a7`) lines 750-754 [crates/gwiki/src/commands/citation_quality.rs:750-754]
  - Signature: `fn write_page(root: &std::path::Path, relative: &str, markdown: &str) {`
  - Purpose: Writes markdown content to a file at a path constructed by joining a root directory with a relative path component, creating all necessary parent directories. [crates/gwiki/src/commands/citation_quality.rs:750-754]
- `source_record` (function) component `source_record [function]` (`9ab7d097-37d1-5c7b-a280-c27d993aa85a`) lines 756-771 [crates/gwiki/src/commands/citation_quality.rs:756-771]
  - Signature: `fn source_record(id: &str, location: &str, fetched_at: &str) -> SourceRecord {`
  - Purpose: Creates a `SourceRecord` instance from provided id, location, and fetched_at parameters, initializing remaining fields with hardcoded placeholder values. [crates/gwiki/src/commands/citation_quality.rs:756-771]

