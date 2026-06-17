---
title: crates/gwiki/src/commands/citation_quality.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/citation_quality.rs
  ranges:
  - 26-33
  - 36-40
  - 43-49
  - 52-56
  - 59-64
  - 67-70
  - 73-76
  - 79-83
  - 86-89
  - 92-95
  - 98-101
  - 104-107
  - 110-114
  - 116-146
  - 148-162
  - 164-175
  - 177-222
  - 224-264
  - 266-276
  - 278-285
  - 287-302
  - 304-335
  - 337-349
  - 351-383
  - 385-395
  - 397-403
  - 405-416
  - 418-428
  - 430-454
  - 456-470
  - 472-483
  - 485-504
  - 506-517
  - 519-532
  - 534-548
  - 562-572
  - 575-639
  - 642-716
  - 719-769
  - 772-786
  - 789-818
  - 822-841
  - 843-847
  - 849-864
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/citation_quality.rs:26-33](crates/gwiki/src/commands/citation_quality.rs#L26-L33), [crates/gwiki/src/commands/citation_quality.rs:36-40](crates/gwiki/src/commands/citation_quality.rs#L36-L40), [crates/gwiki/src/commands/citation_quality.rs:43-49](crates/gwiki/src/commands/citation_quality.rs#L43-L49), [crates/gwiki/src/commands/citation_quality.rs:52-56](crates/gwiki/src/commands/citation_quality.rs#L52-L56), [crates/gwiki/src/commands/citation_quality.rs:59-64](crates/gwiki/src/commands/citation_quality.rs#L59-L64), [crates/gwiki/src/commands/citation_quality.rs:67-70](crates/gwiki/src/commands/citation_quality.rs#L67-L70), [crates/gwiki/src/commands/citation_quality.rs:73-76](crates/gwiki/src/commands/citation_quality.rs#L73-L76), [crates/gwiki/src/commands/citation_quality.rs:79-83](crates/gwiki/src/commands/citation_quality.rs#L79-L83), [crates/gwiki/src/commands/citation_quality.rs:86-89](crates/gwiki/src/commands/citation_quality.rs#L86-L89), [crates/gwiki/src/commands/citation_quality.rs:92-95](crates/gwiki/src/commands/citation_quality.rs#L92-L95), [crates/gwiki/src/commands/citation_quality.rs:98-101](crates/gwiki/src/commands/citation_quality.rs#L98-L101), [crates/gwiki/src/commands/citation_quality.rs:104-107](crates/gwiki/src/commands/citation_quality.rs#L104-L107), [crates/gwiki/src/commands/citation_quality.rs:110-114](crates/gwiki/src/commands/citation_quality.rs#L110-L114), [crates/gwiki/src/commands/citation_quality.rs:116-146](crates/gwiki/src/commands/citation_quality.rs#L116-L146), [crates/gwiki/src/commands/citation_quality.rs:148-162](crates/gwiki/src/commands/citation_quality.rs#L148-L162), [crates/gwiki/src/commands/citation_quality.rs:164-175](crates/gwiki/src/commands/citation_quality.rs#L164-L175), [crates/gwiki/src/commands/citation_quality.rs:177-222](crates/gwiki/src/commands/citation_quality.rs#L177-L222), [crates/gwiki/src/commands/citation_quality.rs:224-264](crates/gwiki/src/commands/citation_quality.rs#L224-L264), [crates/gwiki/src/commands/citation_quality.rs:266-276](crates/gwiki/src/commands/citation_quality.rs#L266-L276), [crates/gwiki/src/commands/citation_quality.rs:278-285](crates/gwiki/src/commands/citation_quality.rs#L278-L285), [crates/gwiki/src/commands/citation_quality.rs:287-302](crates/gwiki/src/commands/citation_quality.rs#L287-L302), [crates/gwiki/src/commands/citation_quality.rs:304-335](crates/gwiki/src/commands/citation_quality.rs#L304-L335), [crates/gwiki/src/commands/citation_quality.rs:337-349](crates/gwiki/src/commands/citation_quality.rs#L337-L349), [crates/gwiki/src/commands/citation_quality.rs:351-383](crates/gwiki/src/commands/citation_quality.rs#L351-L383), [crates/gwiki/src/commands/citation_quality.rs:385-395](crates/gwiki/src/commands/citation_quality.rs#L385-L395), [crates/gwiki/src/commands/citation_quality.rs:397-403](crates/gwiki/src/commands/citation_quality.rs#L397-L403), [crates/gwiki/src/commands/citation_quality.rs:405-416](crates/gwiki/src/commands/citation_quality.rs#L405-L416), [crates/gwiki/src/commands/citation_quality.rs:418-428](crates/gwiki/src/commands/citation_quality.rs#L418-L428), [crates/gwiki/src/commands/citation_quality.rs:430-454](crates/gwiki/src/commands/citation_quality.rs#L430-L454), [crates/gwiki/src/commands/citation_quality.rs:456-470](crates/gwiki/src/commands/citation_quality.rs#L456-L470), [crates/gwiki/src/commands/citation_quality.rs:472-483](crates/gwiki/src/commands/citation_quality.rs#L472-L483), [crates/gwiki/src/commands/citation_quality.rs:485-504](crates/gwiki/src/commands/citation_quality.rs#L485-L504), [crates/gwiki/src/commands/citation_quality.rs:506-517](crates/gwiki/src/commands/citation_quality.rs#L506-L517), [crates/gwiki/src/commands/citation_quality.rs:519-532](crates/gwiki/src/commands/citation_quality.rs#L519-L532), [crates/gwiki/src/commands/citation_quality.rs:534-548](crates/gwiki/src/commands/citation_quality.rs#L534-L548), [crates/gwiki/src/commands/citation_quality.rs:562-572](crates/gwiki/src/commands/citation_quality.rs#L562-L572), [crates/gwiki/src/commands/citation_quality.rs:575-639](crates/gwiki/src/commands/citation_quality.rs#L575-L639), [crates/gwiki/src/commands/citation_quality.rs:642-716](crates/gwiki/src/commands/citation_quality.rs#L642-L716), [crates/gwiki/src/commands/citation_quality.rs:719-769](crates/gwiki/src/commands/citation_quality.rs#L719-L769), [crates/gwiki/src/commands/citation_quality.rs:772-786](crates/gwiki/src/commands/citation_quality.rs#L772-L786), [crates/gwiki/src/commands/citation_quality.rs:789-818](crates/gwiki/src/commands/citation_quality.rs#L789-L818), [crates/gwiki/src/commands/citation_quality.rs:822-841](crates/gwiki/src/commands/citation_quality.rs#L822-L841), [crates/gwiki/src/commands/citation_quality.rs:843-847](crates/gwiki/src/commands/citation_quality.rs#L843-L847), [crates/gwiki/src/commands/citation_quality.rs:849-864](crates/gwiki/src/commands/citation_quality.rs#L849-L864)

</details>

# crates/gwiki/src/commands/citation_quality.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds and writes a citation-quality report for a wiki scope, combining source credibility, coverage gaps, contradiction detection, stale-source warnings, and an overall confidence assessment into both structured data and rendered markdown. `execute` orchestrates the workflow, `build_report` and `build_report_with_contradiction_detector` assemble the report depending on AI availability, and the section helpers compute each subsection from source records, provenance, and scope selection. The rendering and artifact-writing helpers turn that report into a page/file output, while the tests verify scope handling, PostgreSQL index requirements, AI-driven contradiction detection, parsing, and degradation behavior.
[crates/gwiki/src/commands/citation_quality.rs:26-33]
[crates/gwiki/src/commands/citation_quality.rs:36-40]
[crates/gwiki/src/commands/citation_quality.rs:43-49]
[crates/gwiki/src/commands/citation_quality.rs:52-56]
[crates/gwiki/src/commands/citation_quality.rs:59-64]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CitationQualityReport` | class | `pub(crate) struct CitationQualityReport {` | `CitationQualityReport [class]` | `1e9a9421-24e0-5dae-bb74-d6756d087444` | 26-33 [crates/gwiki/src/commands/citation_quality.rs:26-33] | Indexed class `CitationQualityReport` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:26-33] |
| `DependencyMetadata` | class | `pub(crate) struct DependencyMetadata {` | `DependencyMetadata [class]` | `cc451b9b-2526-535b-a6d9-433d5b71f671` | 36-40 [crates/gwiki/src/commands/citation_quality.rs:36-40] | Indexed class `DependencyMetadata` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:36-40] |
| `CitationQualitySections` | class | `pub(crate) struct CitationQualitySections {` | `CitationQualitySections [class]` | `047a286f-3032-5f5a-bfb2-d061fc6dd9d8` | 43-49 [crates/gwiki/src/commands/citation_quality.rs:43-49] | Indexed class `CitationQualitySections` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:43-49] |
| `CredibilitySection` | class | `pub(crate) struct CredibilitySection {` | `CredibilitySection [class]` | `48ff1b20-b7ae-59d5-8e0c-7d87b14a97a3` | 52-56 [crates/gwiki/src/commands/citation_quality.rs:52-56] | Indexed class `CredibilitySection` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:52-56] |
| `SourceCredibility` | class | `pub(crate) struct SourceCredibility {` | `SourceCredibility [class]` | `4b2ee9e1-8f33-5020-b23a-9db616cedba9` | 59-64 [crates/gwiki/src/commands/citation_quality.rs:59-64] | Indexed class `SourceCredibility` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:59-64] |
| `CoverageGapSection` | class | `pub(crate) struct CoverageGapSection {` | `CoverageGapSection [class]` | `ec16f50d-f01b-51dd-955a-c90e1d412d55` | 67-70 [crates/gwiki/src/commands/citation_quality.rs:67-70] | Indexed class `CoverageGapSection` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:67-70] |
| `CoverageGap` | class | `pub(crate) struct CoverageGap {` | `CoverageGap [class]` | `2eb27a02-0545-57a5-a96e-0fead9b9f817` | 73-76 [crates/gwiki/src/commands/citation_quality.rs:73-76] | Indexed class `CoverageGap` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:73-76] |
| `ContradictionSection` | class | `pub(crate) struct ContradictionSection {` | `ContradictionSection [class]` | `39a6da3b-bb8c-55b9-a609-499e6d712fa5` | 79-83 [crates/gwiki/src/commands/citation_quality.rs:79-83] | Indexed class `ContradictionSection` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:79-83] |
| `ContradictionFinding` | class | `pub(crate) struct ContradictionFinding {` | `ContradictionFinding [class]` | `146f86bf-e6e6-528e-8a87-17ebbcf0070c` | 86-89 [crates/gwiki/src/commands/citation_quality.rs:86-89] | Indexed class `ContradictionFinding` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:86-89] |
| `StaleSourceSection` | class | `pub(crate) struct StaleSourceSection {` | `StaleSourceSection [class]` | `fc52cc3b-9bcb-599e-a612-4312aac13ba0` | 92-95 [crates/gwiki/src/commands/citation_quality.rs:92-95] | Indexed class `StaleSourceSection` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:92-95] |
| `StaleSourceWarning` | class | `pub(crate) struct StaleSourceWarning {` | `StaleSourceWarning [class]` | `86298599-2f1e-5efb-acee-56fffcfdf4df` | 98-101 [crates/gwiki/src/commands/citation_quality.rs:98-101] | Indexed class `StaleSourceWarning` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:98-101] |
| `ConfidenceSection` | class | `pub(crate) struct ConfidenceSection {` | `ConfidenceSection [class]` | `0b670d02-a812-51e8-8d74-455b8a5e3baa` | 104-107 [crates/gwiki/src/commands/citation_quality.rs:104-107] | Indexed class `ConfidenceSection` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:104-107] |
| `OutputConfidence` | class | `pub(crate) struct OutputConfidence {` | `OutputConfidence [class]` | `8149901e-badb-5820-8205-3042c3b968c9` | 110-114 [crates/gwiki/src/commands/citation_quality.rs:110-114] | Indexed class `OutputConfidence` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:110-114] |
| `execute` | function | `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {` | `execute [function]` | `f66e3760-ebdc-5cf9-b01d-edc74c3d9679` | 116-146 [crates/gwiki/src/commands/citation_quality.rs:116-146] | Indexed function `execute` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:116-146] |
| `text_generation_available` | function | `fn text_generation_available() -> Result<bool, WikiError> {` | `text_generation_available [function]` | `354ac887-a1e7-54dc-9922-65e6d0beb061` | 148-162 [crates/gwiki/src/commands/citation_quality.rs:148-162] | Indexed function `text_generation_available` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:148-162] |
| `build_report` | function | `pub(crate) fn build_report(` | `build_report [function]` | `e0b154d3-59d8-53ac-ba7b-6d506e070027` | 164-175 [crates/gwiki/src/commands/citation_quality.rs:164-175] | Indexed function `build_report` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:164-175] |
| `build_report_with_contradiction_detector` | function | `fn build_report_with_contradiction_detector<F>(` | `build_report_with_contradiction_detector [function]` | `e2963772-05f1-523b-96b9-439ab519c7b0` | 177-222 [crates/gwiki/src/commands/citation_quality.rs:177-222] | Indexed function `build_report_with_contradiction_detector` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:177-222] |
| `credibility_section` | function | `fn credibility_section(` | `credibility_section [function]` | `f912fc0f-8c03-52ff-a29e-778b1cb3cf3c` | 224-264 [crates/gwiki/src/commands/citation_quality.rs:224-264] | Indexed function `credibility_section` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:224-264] |
| `credibility_source_type` | function | `fn credibility_source_type(kind: &SourceKind) -> CredibilitySourceType {` | `credibility_source_type [function]` | `27af47be-5e91-51a0-8e29-b47a9725a4fb` | 266-276 [crates/gwiki/src/commands/citation_quality.rs:266-276] | Indexed function `credibility_source_type` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:266-276] |
| `source_age_days` | function | `fn source_age_days(source: &SourceRecord) -> Option<u16> {` | `source_age_days [function]` | `cb21ed28-d217-573a-9cdf-fdf6faf71c7f` | 278-285 [crates/gwiki/src/commands/citation_quality.rs:278-285] | Indexed function `source_age_days` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:278-285] |
| `corroborating_sources` | function | `fn corroborating_sources(source: &SourceRecord, provenance: &ProvenanceGraph) -> Vec<String> {` | `corroborating_sources [function]` | `b5d40b7a-5463-517c-a63f-0c7b249703ac` | 287-302 [crates/gwiki/src/commands/citation_quality.rs:287-302] | Indexed function `corroborating_sources` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:287-302] |
| `coverage_gap_section` | function | `fn coverage_gap_section(` | `coverage_gap_section [function]` | `7a2af10b-aa2e-5810-865f-8e71f719f466` | 304-335 [crates/gwiki/src/commands/citation_quality.rs:304-335] | Indexed function `coverage_gap_section` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:304-335] |
| `stale_source_section` | function | `fn stale_source_section(report: &health::HealthReport) -> StaleSourceSection {` | `stale_source_section [function]` | `95d87f46-7972-5fd3-b723-b5159cd9ab05` | 337-349 [crates/gwiki/src/commands/citation_quality.rs:337-349] | Indexed function `stale_source_section` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:337-349] |
| `confidence_section` | function | `fn confidence_section(` | `confidence_section [function]` | `02bf7786-fd03-506c-8d59-8c3659f22bfd` | 351-383 [crates/gwiki/src/commands/citation_quality.rs:351-383] | Indexed function `confidence_section` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:351-383] |
| `average_credibility` | function | `fn average_credibility(section: &CredibilitySection) -> Option<f32> {` | `average_credibility [function]` | `fd90408b-86db-56c9-a640-5fb4931af0f6` | 385-395 [crates/gwiki/src/commands/citation_quality.rs:385-395] | Indexed function `average_credibility` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:385-395] |
| `confidence_explanation` | function | `fn confidence_explanation(available: bool) -> String {` | `confidence_explanation [function]` | `63709a04-a849-5343-ac1e-44212fa67613` | 397-403 [crates/gwiki/src/commands/citation_quality.rs:397-403] | Indexed function `confidence_explanation` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:397-403] |
| `section_id_for` | function | `fn section_id_for(page_path: &Path, heading: &str) -> String {` | `section_id_for [function]` | `b8e26556-2147-59be-861b-13daa5c2b5fd` | 405-416 [crates/gwiki/src/commands/citation_quality.rs:405-416] | Indexed function `section_id_for` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:405-416] |
| `page_slugify` | function | `fn page_slugify(value: &str) -> String {` | `page_slugify [function]` | `db74ba73-8cc4-5f03-8e59-39fbb2cbe5ee` | 418-428 [crates/gwiki/src/commands/citation_quality.rs:418-428] | Indexed function `page_slugify` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:418-428] |
| `render_markdown` | function | `fn render_markdown(` | `render_markdown [function]` | `280a6922-d472-5f76-aef0-bfb0bed71797` | 430-454 [crates/gwiki/src/commands/citation_quality.rs:430-454] | Indexed function `render_markdown` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:430-454] |
| `render_credibility` | function | `fn render_credibility(markdown: &mut String, section: &CredibilitySection) {` | `render_credibility [function]` | `4b488d69-3eaa-5346-b901-dc8d746428d0` | 456-470 [crates/gwiki/src/commands/citation_quality.rs:456-470] | Indexed function `render_credibility` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:456-470] |
| `render_coverage` | function | `fn render_coverage(markdown: &mut String, section: &CoverageGapSection) {` | `render_coverage [function]` | `bb544b4b-e2cf-5f9b-a4c5-f210e3a7b997` | 472-483 [crates/gwiki/src/commands/citation_quality.rs:472-483] | Indexed function `render_coverage` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:472-483] |
| `render_contradictions` | function | `fn render_contradictions(markdown: &mut String, section: &ContradictionSection) {` | `render_contradictions [function]` | `0a7ff010-0292-5eca-80f5-be2948f56406` | 485-504 [crates/gwiki/src/commands/citation_quality.rs:485-504] | Indexed function `render_contradictions` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:485-504] |
| `render_stale_sources` | function | `fn render_stale_sources(markdown: &mut String, section: &StaleSourceSection) {` | `render_stale_sources [function]` | `9aae3683-0eaa-553e-8de0-ab0e1331892c` | 506-517 [crates/gwiki/src/commands/citation_quality.rs:506-517] | Indexed function `render_stale_sources` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:506-517] |
| `render_confidence` | function | `fn render_confidence(markdown: &mut String, section: &ConfidenceSection) {` | `render_confidence [function]` | `80f36ad8-4e25-5c4c-8706-f7d4409620d2` | 519-532 [crates/gwiki/src/commands/citation_quality.rs:519-532] | Indexed function `render_confidence` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:519-532] |
| `write_artifact` | function | `fn write_artifact(root: &Path, relative_path: &Path, markdown: &str) -> Result<(), WikiError> {` | `write_artifact [function]` | `7dce2f2c-b96b-523c-b35b-ab98dffe9084` | 534-548 [crates/gwiki/src/commands/citation_quality.rs:534-548] | Indexed function `write_artifact` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:534-548] |
| `citation_quality_execute_requires_postgresql_index` | function | `fn citation_quality_execute_requires_postgresql_index() {` | `citation_quality_execute_requires_postgresql_index [function]` | `714c7e53-14b6-5945-a346-09b0811f3292` | 562-572 [crates/gwiki/src/commands/citation_quality.rs:562-572] | Indexed function `citation_quality_execute_requires_postgresql_index` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:562-572] |
| `citation_quality_report_covers_sections_and_degradation` | function | `fn citation_quality_report_covers_sections_and_degradation() {` | `citation_quality_report_covers_sections_and_degradation [function]` | `5bb885c9-6387-5384-ab14-2310aaad8983` | 575-639 [crates/gwiki/src/commands/citation_quality.rs:575-639] | Indexed function `citation_quality_report_covers_sections_and_degradation` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:575-639] |
| `citation_quality_report_detects_ai_contradictions_when_available` | function | `fn citation_quality_report_detects_ai_contradictions_when_available() {` | `citation_quality_report_detects_ai_contradictions_when_available [function]` | `d2869ddf-13be-5172-86ac-faf15c720d31` | 642-716 [crates/gwiki/src/commands/citation_quality.rs:642-716] | Indexed function `citation_quality_report_detects_ai_contradictions_when_available` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:642-716] |
| `citation_quality_report_ignores_repeated_support_when_ai_available` | function | `fn citation_quality_report_ignores_repeated_support_when_ai_available() {` | `citation_quality_report_ignores_repeated_support_when_ai_available [function]` | `c85950a2-34ac-54a7-8641-f95bbf894bde` | 719-769 [crates/gwiki/src/commands/citation_quality.rs:719-769] | Indexed function `citation_quality_report_ignores_repeated_support_when_ai_available` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:719-769] |
| `citation_quality_parses_fenced_contradiction_json` | function | `fn citation_quality_parses_fenced_contradiction_json() {` | `citation_quality_parses_fenced_contradiction_json [function]` | `283896ab-ead9-551e-a988-4a7553050b68` | 772-786 [crates/gwiki/src/commands/citation_quality.rs:772-786] | Indexed function `citation_quality_parses_fenced_contradiction_json` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:772-786] |
| `citation_quality_coverage_gaps_apply_selected_scope` | function | `fn citation_quality_coverage_gaps_apply_selected_scope() {` | `citation_quality_coverage_gaps_apply_selected_scope [function]` | `7571597e-4c01-506a-a985-1cb39aac41d4` | 789-818 [crates/gwiki/src/commands/citation_quality.rs:789-818] | Indexed function `citation_quality_coverage_gaps_apply_selected_scope` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:789-818] |
| `citation_quality_requires_configured_postgres_index` | function | `fn citation_quality_requires_configured_postgres_index() {` | `citation_quality_requires_configured_postgres_index [function]` | `1b37caaa-a95a-530c-97d2-57370d80d0e2` | 822-841 [crates/gwiki/src/commands/citation_quality.rs:822-841] | Indexed function `citation_quality_requires_configured_postgres_index` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:822-841] |
| `write_page` | function | `fn write_page(root: &std::path::Path, relative: &str, markdown: &str) {` | `write_page [function]` | `3ce73178-c265-52a6-ba20-2981b22a6d46` | 843-847 [crates/gwiki/src/commands/citation_quality.rs:843-847] | Indexed function `write_page` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:843-847] |
| `source_record` | function | `fn source_record(id: &str, location: &str, fetched_at: &str) -> SourceRecord {` | `source_record [function]` | `e104c9da-f522-51d8-b75d-0b0455d4473f` | 849-864 [crates/gwiki/src/commands/citation_quality.rs:849-864] | Indexed function `source_record` in `crates/gwiki/src/commands/citation_quality.rs`. [crates/gwiki/src/commands/citation_quality.rs:849-864] |
