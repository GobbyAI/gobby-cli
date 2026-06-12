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

# crates/gwiki/src/commands/citation_quality.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

`crates/gwiki/src/commands/citation_quality.rs` exposes 44 indexed API symbols.
[crates/gwiki/src/commands/citation_quality.rs:26-33]
[crates/gwiki/src/commands/citation_quality.rs:36-40]
[crates/gwiki/src/commands/citation_quality.rs:43-49]
[crates/gwiki/src/commands/citation_quality.rs:52-56]
[crates/gwiki/src/commands/citation_quality.rs:59-64]

## API Symbols

- `CitationQualityReport` (class) component `CitationQualityReport [class]` (`1e9a9421-24e0-5dae-bb74-d6756d087444`) lines 26-33 [crates/gwiki/src/commands/citation_quality.rs:26-33]
  - Signature: `pub(crate) struct CitationQualityReport {`
  - Purpose: `CitationQualityReport` is a crate-private aggregate that encapsulates the originating command, scope identity, artifact path, dependency metadata, section-level citation quality results, and the rendered markdown for a citation quality analysis report. [crates/gwiki/src/commands/citation_quality.rs:26-33]
- `DependencyMetadata` (class) component `DependencyMetadata [class]` (`cc451b9b-2526-535b-a6d9-433d5b71f671`) lines 36-40 [crates/gwiki/src/commands/citation_quality.rs:36-40]
  - Signature: `pub(crate) struct DependencyMetadata {`
  - Purpose: `DependencyMetadata` is an internal metadata container that groups dependency identifiers into three `Vec<&'static str>` categories: `hard`, `optional`, and `multimodal`. [crates/gwiki/src/commands/citation_quality.rs:36-40]
- `CitationQualitySections` (class) component `CitationQualitySections [class]` (`047a286f-3032-5f5a-bfb2-d061fc6dd9d8`) lines 43-49 [crates/gwiki/src/commands/citation_quality.rs:43-49]
  - Signature: `pub(crate) struct CitationQualitySections {`
  - Purpose: `CitationQualitySections` is a composite data structure that groups five citation-quality analysis sections: `credibility`, `coverage_gaps`, `contradictions`, `stale_sources`, and `confidence`. [crates/gwiki/src/commands/citation_quality.rs:43-49]
- `CredibilitySection` (class) component `CredibilitySection [class]` (`48ff1b20-b7ae-59d5-8e0c-7d87b14a97a3`) lines 52-56 [crates/gwiki/src/commands/citation_quality.rs:52-56]
  - Signature: `pub(crate) struct CredibilitySection {`
  - Purpose: `CredibilitySection` is an internal record type that indicates whether credibility data is available and carries an optional note plus a vector of `SourceCredibility` entries. [crates/gwiki/src/commands/citation_quality.rs:52-56]
- `SourceCredibility` (class) component `SourceCredibility [class]` (`4b2ee9e1-8f33-5020-b23a-9db616cedba9`) lines 59-64 [crates/gwiki/src/commands/citation_quality.rs:59-64]
  - Signature: `pub(crate) struct SourceCredibility {`
  - Purpose: `SourceCredibility` is an internal record that ties a `source_id` and `location` to an 8-bit credibility `score` and the string `signals` used to justify it. [crates/gwiki/src/commands/citation_quality.rs:59-64]
- `CoverageGapSection` (class) component `CoverageGapSection [class]` (`ec16f50d-f01b-51dd-955a-c90e1d412d55`) lines 67-70 [crates/gwiki/src/commands/citation_quality.rs:67-70]
  - Signature: `pub(crate) struct CoverageGapSection {`
  - Purpose: `CoverageGapSection` is a Rust data container that records whether coverage-gap information is available and stores the associated `CoverageGap` entries in a vector. [crates/gwiki/src/commands/citation_quality.rs:67-70]
- `CoverageGap` (class) component `CoverageGap [class]` (`2eb27a02-0545-57a5-a96e-0fead9b9f817`) lines 73-76 [crates/gwiki/src/commands/citation_quality.rs:73-76]
  - Signature: `pub(crate) struct CoverageGap {`
  - Purpose: `CoverageGap` is a crate-visible record type that represents a coverage deficiency by storing the affected `section` name and a `reason` string explaining the gap. [crates/gwiki/src/commands/citation_quality.rs:73-76]
- `ContradictionSection` (class) component `ContradictionSection [class]` (`39a6da3b-bb8c-55b9-a609-499e6d712fa5`) lines 79-83 [crates/gwiki/src/commands/citation_quality.rs:79-83]
  - Signature: `pub(crate) struct ContradictionSection {`
  - Purpose: `ContradictionSection` is an internal data container that tracks whether contradiction details are available, an optional explanatory note, and a collection of `ContradictionFinding` entries. [crates/gwiki/src/commands/citation_quality.rs:79-83]
- `ContradictionFinding` (class) component `ContradictionFinding [class]` (`146f86bf-e6e6-528e-8a87-17ebbcf0070c`) lines 86-89 [crates/gwiki/src/commands/citation_quality.rs:86-89]
  - Signature: `pub(crate) struct ContradictionFinding {`
  - Purpose: `ContradictionFinding` is an internal record type that stores a contradiction `claim` as a `String` together with the `source_ids` of the evidence sources that support it. [crates/gwiki/src/commands/citation_quality.rs:86-89]
- `StaleSourceSection` (class) component `StaleSourceSection [class]` (`fc52cc3b-9bcb-599e-a612-4312aac13ba0`) lines 92-95 [crates/gwiki/src/commands/citation_quality.rs:92-95]
  - Signature: `pub(crate) struct StaleSourceSection {`
  - Purpose: `StaleSourceSection` is an internal data structure that records whether a source section is currently available and stores the set of `StaleSourceWarning` values associated with it. [crates/gwiki/src/commands/citation_quality.rs:92-95]
- `StaleSourceWarning` (class) component `StaleSourceWarning [class]` (`86298599-2f1e-5efb-acee-56fffcfdf4df`) lines 98-101 [crates/gwiki/src/commands/citation_quality.rs:98-101]
  - Signature: `pub(crate) struct StaleSourceWarning {`
  - Purpose: `StaleSourceWarning` is a crate-visible record that identifies a stale source by its `source_id` and the `location` where the warning was raised. [crates/gwiki/src/commands/citation_quality.rs:98-101]
- `ConfidenceSection` (class) component `ConfidenceSection [class]` (`0b670d02-a812-51e8-8d74-455b8a5e3baa`) lines 104-107 [crates/gwiki/src/commands/citation_quality.rs:104-107]
  - Signature: `pub(crate) struct ConfidenceSection {`
  - Purpose: `ConfidenceSection` is a crate-visible data holder that tracks whether confidence data is available and stores the associated `OutputConfidence` values in a `Vec`. [crates/gwiki/src/commands/citation_quality.rs:104-107]
- `OutputConfidence` (class) component `OutputConfidence [class]` (`8149901e-badb-5820-8205-3042c3b968c9`) lines 110-114 [crates/gwiki/src/commands/citation_quality.rs:110-114]
  - Signature: `pub(crate) struct OutputConfidence {`
  - Purpose: `OutputConfidence` is a crate-private Rust struct that bundles a static output string with an optional `f32` confidence score and a human-readable explanation. [crates/gwiki/src/commands/citation_quality.rs:110-114]
- `execute` (function) component `execute [function]` (`f66e3760-ebdc-5cf9-b01d-edc74c3d9679`) lines 116-146 [crates/gwiki/src/commands/citation_quality.rs:116-146]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: It verifies the `gwiki` Postgres index is attached, resolves the requested scope, probes text-generation availability with a warning-and-fallback to `false` on error, builds and writes a citation-quality report artifact, serializes the report to JSON, and returns a scoped `CommandOutcome` for `citation-quality`. [crates/gwiki/src/commands/citation_quality.rs:116-146]
- `text_generation_available` (function) component `text_generation_available [function]` (`354ac887-a1e7-54dc-9922-65e6d0beb061`) lines 148-162 [crates/gwiki/src/commands/citation_quality.rs:148-162]
  - Signature: `fn text_generation_available() -> Result<bool, WikiError> {`
  - Purpose: It resolves the AI context from the `gwiki citation-quality` hub config with `no_ai` disabled and no forced routing, then returns `true` iff `AiCapability::TextGenerate` is routed `Direct` or `Daemon`, otherwise `false`, propagating any config or resolution failure as `WikiError`. [crates/gwiki/src/commands/citation_quality.rs:148-162]
- `build_report` (function) component `build_report [function]` (`e0b154d3-59d8-53ac-ba7b-6d506e070027`) lines 164-175 [crates/gwiki/src/commands/citation_quality.rs:164-175]
  - Signature: `pub(crate) fn build_report(`
  - Purpose: `build_report` is a thin wrapper that constructs a `CitationQualityReport` for the given `vault_root` and `scope` by delegating to `build_report_with_contradiction_detector` with the `model_contradiction_findings` detector and the `ai_available` flag. [crates/gwiki/src/commands/citation_quality.rs:164-175]
- `build_report_with_contradiction_detector` (function) component `build_report_with_contradiction_detector [function]` (`e2963772-05f1-523b-96b9-439ab519c7b0`) lines 177-222 [crates/gwiki/src/commands/citation_quality.rs:177-222]
  - Signature: `fn build_report_with_contradiction_detector<F>(`
  - Purpose: It loads the vault’s source manifest, provenance graph, and health state, computes credibility, coverage-gap, contradiction, stale-source, and confidence sections (using the injected contradiction detector when AI is available), renders the citation-quality markdown report, and returns a populated `CitationQualityReport` with fixed metadata and output path. [crates/gwiki/src/commands/citation_quality.rs:177-222]
- `credibility_section` (function) component `credibility_section [function]` (`f912fc0f-8c03-52ff-a29e-778b1cb3cf3c`) lines 224-264 [crates/gwiki/src/commands/citation_quality.rs:224-264]
  - Signature: `fn credibility_section(`
  - Purpose: `credibility_section` returns a `CredibilitySection` that is marked unavailable with a note when `sources` is empty, otherwise maps each `SourceRecord` through `CredibilityScore::evaluate` using source type, age, publisher/title, and corroboration from `ProvenanceGraph`, and collects the resulting per-source credibility scores and formatted signals. [crates/gwiki/src/commands/citation_quality.rs:224-264]
- `credibility_source_type` (function) component `credibility_source_type [function]` (`27af47be-5e91-51a0-8e29-b47a9725a4fb`) lines 266-276 [crates/gwiki/src/commands/citation_quality.rs:266-276]
  - Signature: `fn credibility_source_type(kind: &SourceKind) -> CredibilitySourceType {`
  - Purpose: It maps a `SourceKind` to a `CredibilitySourceType` by returning `Academic` for `ResearchNote`, `Community` for `MediaWiki`/`Markdown`, `News` for `Url`/`Html`, `Official` for `Pdf`/`Office`/`GitRepository`, and `Unknown` for all other variants. [crates/gwiki/src/commands/citation_quality.rs:266-276]
- `source_age_days` (function) component `source_age_days [function]` (`cb21ed28-d217-573a-9cdf-fdf6faf71c7f`) lines 278-285 [crates/gwiki/src/commands/citation_quality.rs:278-285]
  - Signature: `fn source_age_days(source: &SourceRecord) -> Option<u16> {`
  - Purpose: Parses `source.fetched_at` as an RFC 3339 timestamp and returns the elapsed whole days since then in UTC, clamped to `0..=u16::MAX`, or `None` if parsing fails. [crates/gwiki/src/commands/citation_quality.rs:278-285]
- `corroborating_sources` (function) component `corroborating_sources [function]` (`b5d40b7a-5463-517c-a63f-0c7b249703ac`) lines 287-302 [crates/gwiki/src/commands/citation_quality.rs:287-302]
  - Signature: `fn corroborating_sources(source: &SourceRecord, provenance: &ProvenanceGraph) -> Vec<String> {`
  - Purpose: Returns the deduplicated, lexicographically sorted list of `source_id`s for all other sources that are linked to at least one of the same `section_id`s as `source`, based on the provenance graph. [crates/gwiki/src/commands/citation_quality.rs:287-302]
- `coverage_gap_section` (function) component `coverage_gap_section [function]` (`7a2af10b-aa2e-5810-865f-8e71f719f466`) lines 304-335 [crates/gwiki/src/commands/citation_quality.rs:304-335]
  - Signature: `fn coverage_gap_section(`
  - Purpose: It scans all pages under `vault_root` that fall within `scope`, and for each heading whose derived section ID has no provenance links in `provenance`, it records a `CoverageGap` for that `page#slugified-heading` before returning `CoverageGapSection { available: true, gaps }`. [crates/gwiki/src/commands/citation_quality.rs:304-335]
- `stale_source_section` (function) component `stale_source_section [function]` (`95d87f46-7972-5fd3-b723-b5159cd9ab05`) lines 337-349 [crates/gwiki/src/commands/citation_quality.rs:337-349]
  - Signature: `fn stale_source_section(report: &health::HealthReport) -> StaleSourceSection {`
  - Purpose: Builds a `StaleSourceSection` marked `available: true` and populates its `warnings` by cloning each `stale_citations` entry’s `source_id` and `location` from the given `health::HealthReport`. [crates/gwiki/src/commands/citation_quality.rs:337-349]
- `confidence_section` (function) component `confidence_section [function]` (`02bf7786-fd03-506c-8d59-8c3659f22bfd`) lines 351-383 [crates/gwiki/src/commands/citation_quality.rs:351-383]
  - Signature: `fn confidence_section(`
  - Purpose: It constructs a `ConfidenceSection` with `available: true` and four `OutputConfidence` entries, deriving confidence values and explanations for credibility, coverage gaps, contradictions, and stale sources from the input sections’ availability and contents. [crates/gwiki/src/commands/citation_quality.rs:351-383]
- `average_credibility` (function) component `average_credibility [function]` (`fd90408b-86db-56c9-a640-5fb4931af0f6`) lines 385-395 [crates/gwiki/src/commands/citation_quality.rs:385-395]
  - Signature: `fn average_credibility(section: &CredibilitySection) -> Option<f32> {`
  - Purpose: Returns `None` unless `section.available` is `true` and `section.sources` is non-empty; otherwise it normalizes each source `score` from `0..=100` to `0.0..=1.0` and returns the arithmetic mean as `Some(f32)`. [crates/gwiki/src/commands/citation_quality.rs:385-395]
- `confidence_explanation` (function) component `confidence_explanation [function]` (`63709a04-a849-5343-ac1e-44212fa67613`) lines 397-403 [crates/gwiki/src/commands/citation_quality.rs:397-403]
  - Signature: `fn confidence_explanation(available: bool) -> String {`
  - Purpose: `confidence_explanation` returns a `String` describing output confidence state, using a nominal “signals available” message when `available` is `true` and a degraded-output message when `false`. [crates/gwiki/src/commands/citation_quality.rs:397-403]
- `section_id_for` (function) component `section_id_for [function]` (`b8e26556-2147-59be-861b-13daa5c2b5fd`) lines 405-416 [crates/gwiki/src/commands/citation_quality.rs:405-416]
  - Signature: `fn section_id_for(page_path: &Path, heading: &str) -> String {`
  - Purpose: Returns the slugified page stem for the special `Overview` heading (falling back to `"overview"` if the stem is unavailable) and otherwise returns the slugified heading text. [crates/gwiki/src/commands/citation_quality.rs:405-416]
- `page_slugify` (function) component `page_slugify [function]` (`db74ba73-8cc4-5f03-8e59-39fbb2cbe5ee`) lines 418-428 [crates/gwiki/src/commands/citation_quality.rs:418-428]
  - Signature: `fn page_slugify(value: &str) -> String {`
  - Purpose: `page_slugify` lowercases the input, converts every non-ASCII-alphanumeric run into a single `-`, preserves only ASCII letters and digits, and trims any leading or trailing hyphens before returning the slug. [crates/gwiki/src/commands/citation_quality.rs:418-428]
- `render_markdown` (function) component `render_markdown [function]` (`280a6922-d472-5f76-aef0-bfb0bed71797`) lines 430-454 [crates/gwiki/src/commands/citation_quality.rs:430-454]
  - Signature: `fn render_markdown(`
  - Purpose: Constructs and returns a markdown `Citation Quality Report` string containing the scope, dependency classifications (`hard`, `optional`, `multimodal`), and the rendered credibility, coverage, contradiction, stale-source, and confidence sections. [crates/gwiki/src/commands/citation_quality.rs:430-454]
- `render_credibility` (function) component `render_credibility [function]` (`4b488d69-3eaa-5346-b901-dc8d746428d0`) lines 456-470 [crates/gwiki/src/commands/citation_quality.rs:456-470]
  - Signature: `fn render_credibility(markdown: &mut String, section: &CredibilitySection) {`
  - Purpose: Appends a `## Credibility` section to the markdown buffer, including the section’s `available` flag, optional `note`, and each source rendered as a bullet with `source_id`, `score`, and `location`. [crates/gwiki/src/commands/citation_quality.rs:456-470]
- `render_coverage` (function) component `render_coverage [function]` (`bb544b4b-e2cf-5f9b-a4c5-f210e3a7b997`) lines 472-483 [crates/gwiki/src/commands/citation_quality.rs:472-483]
  - Signature: `fn render_coverage(markdown: &mut String, section: &CoverageGapSection) {`
  - Purpose: It appends a `## Coverage Gaps` markdown section to the given buffer, including the `available` count and either a no-gaps message or one bullet per gap with its `section` and `reason`. [crates/gwiki/src/commands/citation_quality.rs:472-483]
- `render_contradictions` (function) component `render_contradictions [function]` (`0a7ff010-0292-5eca-80f5-be2948f56406`) lines 485-504 [crates/gwiki/src/commands/citation_quality.rs:485-504]
  - Signature: `fn render_contradictions(markdown: &mut String, section: &ContradictionSection) {`
  - Purpose: Appends a `## Contradictions` markdown section to `markdown`, including the section’s availability, optional note, either a “No contradictions reported.” placeholder when `findings` is empty or one bullet per finding listing the claim and comma-joined conflicting `source_ids`. [crates/gwiki/src/commands/citation_quality.rs:485-504]
- `render_stale_sources` (function) component `render_stale_sources [function]` (`9aae3683-0eaa-553e-8de0-ab0e1331892c`) lines 506-517 [crates/gwiki/src/commands/citation_quality.rs:506-517]
  - Signature: `fn render_stale_sources(markdown: &mut String, section: &StaleSourceSection) {`
  - Purpose: Appends a `## Stale Source Warnings` Markdown section to `markdown`, includes the section’s `available` flag, and either emits `No stale sources detected.` or one bullet per warning in `source_id: location` format. [crates/gwiki/src/commands/citation_quality.rs:506-517]
- `render_confidence` (function) component `render_confidence [function]` (`80f36ad8-4e25-5c4c-8706-f7d4409620d2`) lines 519-532 [crates/gwiki/src/commands/citation_quality.rs:519-532]
  - Signature: `fn render_confidence(markdown: &mut String, section: &ConfidenceSection) {`
  - Purpose: `render_confidence` appends a Markdown “Confidence per output” section to `markdown`, writing the section’s `available` flag and one bullet per output containing the output name, its confidence formatted to two decimals or `n/a` if absent, and the associated explanation. [crates/gwiki/src/commands/citation_quality.rs:519-532]
- `write_artifact` (function) component `write_artifact [function]` (`7dce2f2c-b96b-523c-b35b-ab98dffe9084`) lines 534-548 [crates/gwiki/src/commands/citation_quality.rs:534-548]
  - Signature: `fn write_artifact(root: &Path, relative_path: &Path, markdown: &str) -> Result<(), WikiError> {`
  - Purpose: Joins `relative_path` to `root`, creates the target directory tree if needed, and writes `markdown` to the resulting file, converting any filesystem failure into a `WikiError::Io` with context-specific action and path. [crates/gwiki/src/commands/citation_quality.rs:534-548]
- `citation_quality_execute_requires_postgresql_index` (function) component `citation_quality_execute_requires_postgresql_index [function]` (`714c7e53-14b6-5945-a346-09b0811f3292`) lines 562-572 [crates/gwiki/src/commands/citation_quality.rs:562-572]
  - Signature: `fn citation_quality_execute_requires_postgresql_index() {`
  - Purpose: Verifies that `execute(ScopeSelection::Detect)` returns a `WikiError::Config` mentioning “PostgreSQL index is required” when both `GWIKI_DATABASE_URL` and `GOBBY_POSTGRES_DSN` are unset in an isolated temporary `GOBBY_HOME`. [crates/gwiki/src/commands/citation_quality.rs:562-572]
- `citation_quality_report_covers_sections_and_degradation` (function) component `citation_quality_report_covers_sections_and_degradation [function]` (`5bb885c9-6387-5384-ab14-2310aaad8983`) lines 575-639 [crates/gwiki/src/commands/citation_quality.rs:575-639]
  - Signature: `fn citation_quality_report_covers_sections_and_degradation() {`
  - Purpose: I’m locating the test in the repo so I can summarize exactly what it asserts rather than infer from the truncated snippet.The exact symbol isn’t in the checked-out tree, so I’m summarizing from the snippet itself and the test name, which is enough to capture intent here.This test builds a temporary wiki with one sourced section and two unsourced sections across two pages, saves a provenance graph for the cited claim, and verifies that `build_report` produces markdown with a `Coverage Gaps` section listing the missing page/section anchors and a degradation-related summary. [crates/gwiki/src/commands/citation_quality.rs:575-639]
- `citation_quality_report_detects_ai_contradictions_when_available` (function) component `citation_quality_report_detects_ai_contradictions_when_available [function]` (`d2869ddf-13be-5172-86ac-faf15c720d31`) lines 642-716 [crates/gwiki/src/commands/citation_quality.rs:642-716]
  - Signature: `fn citation_quality_report_detects_ai_contradictions_when_available() {`
  - Purpose: This test seeds a page with two provenance links that assert conflicting launch dates, then verifies that `build_report_with_contradiction_detector` invokes the contradiction detector for that section and incorporates the returned AI contradiction report when available. [crates/gwiki/src/commands/citation_quality.rs:642-716]
- `citation_quality_report_ignores_repeated_support_when_ai_available` (function) component `citation_quality_report_ignores_repeated_support_when_ai_available [function]` (`c85950a2-34ac-54a7-8641-f95bbf894bde`) lines 719-769 [crates/gwiki/src/commands/citation_quality.rs:719-769]
  - Signature: `fn citation_quality_report_ignores_repeated_support_when_ai_available() {`
  - Purpose: It sets up a provenance graph where two sources support the same claim and asserts that the citation quality report marks AI as available, omits repeated-support details from the markdown, and does not invoke the AI contradiction detector. [crates/gwiki/src/commands/citation_quality.rs:719-769]
- `citation_quality_parses_fenced_contradiction_json` (function) component `citation_quality_parses_fenced_contradiction_json [function]` (`283896ab-ead9-551e-a988-4a7553050b68`) lines 772-786 [crates/gwiki/src/commands/citation_quality.rs:772-786]
  - Signature: `fn citation_quality_parses_fenced_contradiction_json() {`
  - Purpose: Verifies that `parse_contradiction_findings` can parse a JSON object wrapped in a fenced ```json code block and return a `ContradictionFinding` with the expected `claim` and `source_ids` values. [crates/gwiki/src/commands/citation_quality.rs:772-786]
- `citation_quality_coverage_gaps_apply_selected_scope` (function) component `citation_quality_coverage_gaps_apply_selected_scope [function]` (`7571597e-4c01-506a-a985-1cb39aac41d4`) lines 789-818 [crates/gwiki/src/commands/citation_quality.rs:789-818]
  - Signature: `fn citation_quality_coverage_gaps_apply_selected_scope() {`
  - Purpose: This test creates a temporary corpus with one topic page and one concept page, builds a report for the `ScopeIdentity::topic("rust")` scope, and verifies that the markdown includes only the topic page’s `#missing` citation gap while excluding the concept page’s gap. [crates/gwiki/src/commands/citation_quality.rs:789-818]
- `citation_quality_requires_configured_postgres_index` (function) component `citation_quality_requires_configured_postgres_index [function]` (`1b37caaa-a95a-530c-97d2-57370d80d0e2`) lines 822-841 [crates/gwiki/src/commands/citation_quality.rs:822-841]
  - Signature: `fn citation_quality_requires_configured_postgres_index() {`
  - Purpose: This test creates a temporary Gobby project, sets `GWIKI_DATABASE_URL` to an unreachable PostgreSQL endpoint, calls `execute(ScopeSelection::project(...))`, and asserts that citation-quality processing fails with a PostgreSQL connection error. [crates/gwiki/src/commands/citation_quality.rs:822-841]
- `write_page` (function) component `write_page [function]` (`3ce73178-c265-52a6-ba20-2981b22a6d46`) lines 843-847 [crates/gwiki/src/commands/citation_quality.rs:843-847]
  - Signature: `fn write_page(root: &std::path::Path, relative: &str, markdown: &str) {`
  - Purpose: It resolves `relative` against `root`, creates the target file’s parent directory tree if needed, and writes `markdown` to that path, panicking on any I/O error via `expect`. [crates/gwiki/src/commands/citation_quality.rs:843-847]
- `source_record` (function) component `source_record [function]` (`e104c9da-f522-51d8-b75d-0b0455d4473f`) lines 849-864 [crates/gwiki/src/commands/citation_quality.rs:849-864]
  - Signature: `fn source_record(id: &str, location: &str, fetched_at: &str) -> SourceRecord {`
  - Purpose: Constructs a `SourceRecord` by copying `id`, `location`, and `fetched_at` into strings and populating all other fields with fixed defaults, including `canonical_location = location`, `kind = SourceKind::Url`, `content_hash = "hash"`, `ingestion_method = IngestionMethod::Research`, and `compile_status = CompileStatus::Compiled`. [crates/gwiki/src/commands/citation_quality.rs:849-864]

