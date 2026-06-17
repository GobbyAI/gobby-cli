---
title: crates/gwiki/src/health.rs
type: code_file
provenance:
- file: crates/gwiki/src/health.rs
  ranges:
  - 22-34
  - 37-41
  - 44-47
  - 49-53
  - 55-95
  - 97-106
  - 108-132
  - 134-142
  - 144-169
  - 171-188
  - 190-192
  - 194-197
  - 199-211
  - 213-226
  - 228-236
  - 238-240
  - 242-247
  - 249-253
  - 255-262
  - 265-276
  - 279-281
  - 284-286
  - 289-327
  - 329-339
  - 341-350
  - 353-360
  - 362-381
  - 384-386
  - 389-391
  - 393-398
  - 400-403
  - 406-435
  - 439-441
  - 445-450
  - 452-458
  - 461-467
  - 469-489
  - 491-504
  - 506-521
  - 523-538
  - 540-560
  - 568-611
  - 614-638
  - 641-654
  - 657-695
  - 698-700
  - 703-712
  - 715-726
  - 729-735
  - 738-745
  - 748-753
  - 756-769
  - 772-807
  - 809-813
  - 815-830
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/health.rs:22-34](crates/gwiki/src/health.rs#L22-L34), [crates/gwiki/src/health.rs:37-41](crates/gwiki/src/health.rs#L37-L41), [crates/gwiki/src/health.rs:44-47](crates/gwiki/src/health.rs#L44-L47), [crates/gwiki/src/health.rs:49-53](crates/gwiki/src/health.rs#L49-L53), [crates/gwiki/src/health.rs:55-95](crates/gwiki/src/health.rs#L55-L95), [crates/gwiki/src/health.rs:97-106](crates/gwiki/src/health.rs#L97-L106), [crates/gwiki/src/health.rs:108-132](crates/gwiki/src/health.rs#L108-L132), [crates/gwiki/src/health.rs:134-142](crates/gwiki/src/health.rs#L134-L142), [crates/gwiki/src/health.rs:144-169](crates/gwiki/src/health.rs#L144-L169), [crates/gwiki/src/health.rs:171-188](crates/gwiki/src/health.rs#L171-L188), [crates/gwiki/src/health.rs:190-192](crates/gwiki/src/health.rs#L190-L192), [crates/gwiki/src/health.rs:194-197](crates/gwiki/src/health.rs#L194-L197), [crates/gwiki/src/health.rs:199-211](crates/gwiki/src/health.rs#L199-L211), [crates/gwiki/src/health.rs:213-226](crates/gwiki/src/health.rs#L213-L226), [crates/gwiki/src/health.rs:228-236](crates/gwiki/src/health.rs#L228-L236), [crates/gwiki/src/health.rs:238-240](crates/gwiki/src/health.rs#L238-L240), [crates/gwiki/src/health.rs:242-247](crates/gwiki/src/health.rs#L242-L247), [crates/gwiki/src/health.rs:249-253](crates/gwiki/src/health.rs#L249-L253), [crates/gwiki/src/health.rs:255-262](crates/gwiki/src/health.rs#L255-L262), [crates/gwiki/src/health.rs:265-276](crates/gwiki/src/health.rs#L265-L276), [crates/gwiki/src/health.rs:279-281](crates/gwiki/src/health.rs#L279-L281), [crates/gwiki/src/health.rs:284-286](crates/gwiki/src/health.rs#L284-L286), [crates/gwiki/src/health.rs:289-327](crates/gwiki/src/health.rs#L289-L327), [crates/gwiki/src/health.rs:329-339](crates/gwiki/src/health.rs#L329-L339), [crates/gwiki/src/health.rs:341-350](crates/gwiki/src/health.rs#L341-L350), [crates/gwiki/src/health.rs:353-360](crates/gwiki/src/health.rs#L353-L360), [crates/gwiki/src/health.rs:362-381](crates/gwiki/src/health.rs#L362-L381), [crates/gwiki/src/health.rs:384-386](crates/gwiki/src/health.rs#L384-L386), [crates/gwiki/src/health.rs:389-391](crates/gwiki/src/health.rs#L389-L391), [crates/gwiki/src/health.rs:393-398](crates/gwiki/src/health.rs#L393-L398), [crates/gwiki/src/health.rs:400-403](crates/gwiki/src/health.rs#L400-L403), [crates/gwiki/src/health.rs:406-435](crates/gwiki/src/health.rs#L406-L435), [crates/gwiki/src/health.rs:439-441](crates/gwiki/src/health.rs#L439-L441), [crates/gwiki/src/health.rs:445-450](crates/gwiki/src/health.rs#L445-L450), [crates/gwiki/src/health.rs:452-458](crates/gwiki/src/health.rs#L452-L458), [crates/gwiki/src/health.rs:461-467](crates/gwiki/src/health.rs#L461-L467), [crates/gwiki/src/health.rs:469-489](crates/gwiki/src/health.rs#L469-L489), [crates/gwiki/src/health.rs:491-504](crates/gwiki/src/health.rs#L491-L504), [crates/gwiki/src/health.rs:506-521](crates/gwiki/src/health.rs#L506-L521), [crates/gwiki/src/health.rs:523-538](crates/gwiki/src/health.rs#L523-L538), [crates/gwiki/src/health.rs:540-560](crates/gwiki/src/health.rs#L540-L560), [crates/gwiki/src/health.rs:568-611](crates/gwiki/src/health.rs#L568-L611), [crates/gwiki/src/health.rs:614-638](crates/gwiki/src/health.rs#L614-L638), [crates/gwiki/src/health.rs:641-654](crates/gwiki/src/health.rs#L641-L654), [crates/gwiki/src/health.rs:657-695](crates/gwiki/src/health.rs#L657-L695), [crates/gwiki/src/health.rs:698-700](crates/gwiki/src/health.rs#L698-L700), [crates/gwiki/src/health.rs:703-712](crates/gwiki/src/health.rs#L703-L712), [crates/gwiki/src/health.rs:715-726](crates/gwiki/src/health.rs#L715-L726), [crates/gwiki/src/health.rs:729-735](crates/gwiki/src/health.rs#L729-L735), [crates/gwiki/src/health.rs:738-745](crates/gwiki/src/health.rs#L738-L745), [crates/gwiki/src/health.rs:748-753](crates/gwiki/src/health.rs#L748-L753), [crates/gwiki/src/health.rs:756-769](crates/gwiki/src/health.rs#L756-L769), [crates/gwiki/src/health.rs:772-807](crates/gwiki/src/health.rs#L772-L807), [crates/gwiki/src/health.rs:809-813](crates/gwiki/src/health.rs#L809-L813), [crates/gwiki/src/health.rs:815-830](crates/gwiki/src/health.rs#L815-L830)

</details>

# crates/gwiki/src/health.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides the gwiki “health” workflow: it inspects a vault, aggregates repository health issues into a `HealthReport`, renders that report to text, and persists JSON/text snapshots. `run` is the entry point that calls `inspect` and then `persist_report`; `inspect` gathers lint results, page listings, source manifests, and provenance, then computes stale pages, stale citations, uncited sources, broken links, duplicate concepts, and uncompiled sources. The rest of the file is support code for determining staleness, parsing fetched timestamps, building a citation index with cached regex matching, detecting source references and duplicate concepts, and formatting or writing the final report.
[crates/gwiki/src/health.rs:22-34]
[crates/gwiki/src/health.rs:37-41]
[crates/gwiki/src/health.rs:44-47]
[crates/gwiki/src/health.rs:49-53]
[crates/gwiki/src/health.rs:55-95]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `HealthReport` | class | `pub struct HealthReport {` | `HealthReport [class]` | `8e8faed1-9caa-5488-837a-6ca7884bacc4` | 22-34 [crates/gwiki/src/health.rs:22-34] | Indexed class `HealthReport` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:22-34] |
| `HealthSourceIssue` | class | `pub struct HealthSourceIssue {` | `HealthSourceIssue [class]` | `521805b7-f9e9-5b99-b35b-023d10795e8c` | 37-41 [crates/gwiki/src/health.rs:37-41] | Indexed class `HealthSourceIssue` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:37-41] |
| `DuplicateConcept` | class | `pub struct DuplicateConcept {` | `DuplicateConcept [class]` | `c05ab9f9-742c-5cc4-bfc0-a61d45186b5c` | 44-47 [crates/gwiki/src/health.rs:44-47] | Indexed class `DuplicateConcept` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:44-47] |
| `run` | function | `pub fn run(vault_root: &Path, scope: ScopeIdentity) -> Result<HealthReport, WikiError> {` | `run [function]` | `80be6334-5f52-54f8-9c94-b13ad405a784` | 49-53 [crates/gwiki/src/health.rs:49-53] | Indexed function `run` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:49-53] |
| `inspect` | function | `pub fn inspect(vault_root: &Path, scope: ScopeIdentity) -> Result<HealthReport, WikiError> {` | `inspect [function]` | `05f06473-a4aa-53a4-8b35-6a24d2450262` | 55-95 [crates/gwiki/src/health.rs:55-95] | Indexed function `inspect` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:55-95] |
| `render_text` | function | `pub fn render_text(report: &HealthReport) -> String {` | `render_text [function]` | `18d0d482-352f-519d-8eb2-aed6698ec986` | 97-106 [crates/gwiki/src/health.rs:97-106] | Indexed function `render_text` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:97-106] |
| `persist_report` | function | `fn persist_report(vault_root: &Path, report: &HealthReport) -> Result<(), WikiError> {` | `persist_report [function]` | `bcdbef5c-719e-514a-b2cc-4674f57c2d16` | 108-132 [crates/gwiki/src/health.rs:108-132] | Indexed function `persist_report` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:108-132] |
| `stale_pages` | function | `fn stale_pages(pages: &[crate::lint::WikiPage]) -> Vec<PathBuf> {` | `stale_pages [function]` | `5552f9eb-d607-5db4-8349-955789907b4e` | 134-142 [crates/gwiki/src/health.rs:134-142] | Indexed function `stale_pages` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:134-142] |
| `page_is_stale` | function | `fn page_is_stale(page: &crate::lint::WikiPage) -> bool {` | `page_is_stale [function]` | `4218ea4d-7759-59d8-be53-1f82315ce4bd` | 144-169 [crates/gwiki/src/health.rs:144-169] | Indexed function `page_is_stale` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:144-169] |
| `stale_after_is_due` | function | `fn stale_after_is_due(value: &str, now: DateTime<Utc>) -> bool {` | `stale_after_is_due [function]` | `cac94c7c-7675-50dd-89e2-40d6999db5b7` | 171-188 [crates/gwiki/src/health.rs:171-188] | Indexed function `stale_after_is_due` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:171-188] |
| `source_citation_is_stale` | function | `fn source_citation_is_stale(source: &SourceRecord) -> bool {` | `source_citation_is_stale [function]` | `72c4c995-cc4a-52c2-8633-e9aabe865b5b` | 190-192 [crates/gwiki/src/health.rs:190-192] | Indexed function `source_citation_is_stale` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:190-192] |
| `source_citation_is_stale_at` | function | `fn source_citation_is_stale_at(source: &SourceRecord, now: DateTime<Utc>) -> bool {` | `source_citation_is_stale_at [function]` | `15b50b69-1a32-5d63-952a-20abeed3b7e7` | 194-197 [crates/gwiki/src/health.rs:194-197] | Indexed function `source_citation_is_stale_at` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:194-197] |
| `fetched_at_is_stale` | function | `fn fetched_at_is_stale(value: &str, stale_years: u64, now: DateTime<Utc>) -> bool {` | `fetched_at_is_stale [function]` | `7e131d91-760c-5c54-8655-8fd1af49e7b1` | 199-211 [crates/gwiki/src/health.rs:199-211] | Indexed function `fetched_at_is_stale` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:199-211] |
| `parse_fetched_at` | function | `fn parse_fetched_at(value: &str) -> Option<DateTime<Utc>> {` | `parse_fetched_at [function]` | `62cd60df-837c-5e85-b5fb-da636385e40d` | 213-226 [crates/gwiki/src/health.rs:213-226] | Indexed function `parse_fetched_at` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:213-226] |
| `stale_citation_years` | function | `fn stale_citation_years() -> u64 {` | `stale_citation_years [function]` | `93a1b2ea-8094-53e8-9508-c8135c3b9f5b` | 228-236 [crates/gwiki/src/health.rs:228-236] | Indexed function `stale_citation_years` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:228-236] |
| `stale_citation_years_from_env` | function | `fn stale_citation_years_from_env(raw: &str) -> Option<u64> {` | `stale_citation_years_from_env [function]` | `851ac77a-561f-5a2e-80d2-62baf8dc0145` | 238-240 [crates/gwiki/src/health.rs:238-240] | Indexed function `stale_citation_years_from_env` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:238-240] |
| `fetched_year` | function | `fn fetched_year(value: &str) -> Option<u64> {` | `fetched_year [function]` | `b33e6056-14ae-59c8-b906-4b9705bdaf9f` | 242-247 [crates/gwiki/src/health.rs:242-247] | Indexed function `fetched_year` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:242-247] |
| `approximate_current_year_at` | function | `fn approximate_current_year_at(now: DateTime<Utc>) -> u64 {` | `approximate_current_year_at [function]` | `e7d0fb1a-c7a7-5a58-b51c-08e736cd7db1` | 249-253 [crates/gwiki/src/health.rs:249-253] | Indexed function `approximate_current_year_at` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:249-253] |
| `load_provenance` | function | `fn load_provenance(vault_root: &Path) -> Result<ProvenanceGraph, WikiError> {` | `load_provenance [function]` | `569e0759-f646-5d73-9b34-482e3047743c` | 255-262 [crates/gwiki/src/health.rs:255-262] | Indexed function `load_provenance` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:255-262] |
| `change_triggered_affected_pages` | function | `pub fn change_triggered_affected_pages(` | `change_triggered_affected_pages [function]` | `7674b329-2142-55d4-b76b-2b3b55de8840` | 265-276 [crates/gwiki/src/health.rs:265-276] | Indexed function `change_triggered_affected_pages` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:265-276] |
| `SourceCitationIndex` | class | `struct SourceCitationIndex {` | `SourceCitationIndex [class]` | `98cfcc88-e62b-5af2-838f-c51e316b32b1` | 279-281 [crates/gwiki/src/health.rs:279-281] | Indexed class `SourceCitationIndex` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:279-281] |
| `SourceCitationIndex::cites` | method | `fn cites(&self, source_id: &str) -> bool {` | `SourceCitationIndex::cites [method]` | `6d63b24b-db45-5793-a06f-4cced9996466` | 284-286 [crates/gwiki/src/health.rs:284-286] | Indexed method `SourceCitationIndex::cites` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:284-286] |
| `build_citation_index` | function | `fn build_citation_index(` | `build_citation_index [function]` | `79b0445e-0ea3-5b18-9c04-290fe572affe` | 289-327 [crates/gwiki/src/health.rs:289-327] | Indexed function `build_citation_index` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:289-327] |
| `source_reference_needles` | function | `fn source_reference_needles(source: &SourceRecord) -> Vec<&str> {` | `source_reference_needles [function]` | `5e89f9d0-847f-54c1-b6b8-13f29dffc77b` | 329-339 [crates/gwiki/src/health.rs:329-339] | Indexed function `source_reference_needles` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:329-339] |
| `source_reference_patterns` | function | `fn source_reference_patterns(needle: &str) -> Vec<String> {` | `source_reference_patterns [function]` | `1d380cc7-1f43-5178-8698-4ed8a5e2feeb` | 341-350 [crates/gwiki/src/health.rs:341-350] | Indexed function `source_reference_patterns` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:341-350] |
| `source_reference_is_present` | function | `fn source_reference_is_present(markdown: &str, needle: &str) -> bool {` | `source_reference_is_present [function]` | `bbe38d21-00ab-59b1-b4d3-08f2b0314783` | 353-360 [crates/gwiki/src/health.rs:353-360] | Indexed function `source_reference_is_present` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:353-360] |
| `markdown_without_fenced_code` | function | `fn markdown_without_fenced_code(markdown: &str) -> String {` | `markdown_without_fenced_code [function]` | `8319fc90-d8cc-5663-a9e1-0dd0fceb0dbf` | 362-381 [crates/gwiki/src/health.rs:362-381] | Indexed function `markdown_without_fenced_code` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:362-381] |
| `markdown_link_target_matches` | function | `fn markdown_link_target_matches(markdown: &str, needle: &str) -> bool {` | `markdown_link_target_matches [function]` | `79d4a86e-2724-5d68-a73b-7c5b0e229c37` | 384-386 [crates/gwiki/src/health.rs:384-386] | Indexed function `markdown_link_target_matches` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:384-386] |
| `bounded_text_matches` | function | `fn bounded_text_matches(markdown: &str, needle: &str) -> bool {` | `bounded_text_matches [function]` | `a14a9973-a1b8-5fc6-a1a8-453efb24e13e` | 389-391 [crates/gwiki/src/health.rs:389-391] | Indexed function `bounded_text_matches` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:389-391] |
| `markdown_link_target_pattern` | function | `fn markdown_link_target_pattern(needle: &str) -> String {` | `markdown_link_target_pattern [function]` | `95a1c367-800b-5fe9-8ee2-e21aee0fda96` | 393-398 [crates/gwiki/src/health.rs:393-398] | Indexed function `markdown_link_target_pattern` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:393-398] |
| `bounded_text_pattern` | function | `fn bounded_text_pattern(needle: &str) -> String {` | `bounded_text_pattern [function]` | `d5b02fda-779e-549a-96bd-76b506af94fb` | 400-403 [crates/gwiki/src/health.rs:400-403] | Indexed function `bounded_text_pattern` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:400-403] |
| `cached_regex_is_match` | function | `fn cached_regex_is_match(pattern: String, haystack: &str) -> bool {` | `cached_regex_is_match [function]` | `1940fe23-c47e-56c1-a6b6-d03171d115fe` | 406-435 [crates/gwiki/src/health.rs:406-435] | Indexed function `cached_regex_is_match` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:406-435] |
| `RegexCache` | class | `struct RegexCache {` | `RegexCache [class]` | `3347362a-3f1a-5abc-bf67-d5c0100bd0be` | 439-441 [crates/gwiki/src/health.rs:439-441] | Indexed class `RegexCache` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:439-441] |
| `RegexCache::get` | method | `fn get(&mut self, pattern: &str) -> Option<regex::Regex> {` | `RegexCache::get [method]` | `a8d355a4-3204-557f-86c2-30fe85745901` | 445-450 [crates/gwiki/src/health.rs:445-450] | Indexed method `RegexCache::get` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:445-450] |
| `RegexCache::insert` | method | `fn insert(&mut self, pattern: String, regex: regex::Regex) {` | `RegexCache::insert [method]` | `72862afc-613d-51e1-9d39-87c77709fca4` | 452-458 [crates/gwiki/src/health.rs:452-458] | Indexed method `RegexCache::insert` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:452-458] |
| `source_issue` | function | `fn source_issue(source: &SourceRecord) -> HealthSourceIssue {` | `source_issue [function]` | `addd0e03-5908-5e29-adae-11b87ea753be` | 461-467 [crates/gwiki/src/health.rs:461-467] | Indexed function `source_issue` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:461-467] |
| `duplicate_concepts` | function | `fn duplicate_concepts(pages: &[crate::lint::WikiPage]) -> Vec<DuplicateConcept> {` | `duplicate_concepts [function]` | `aa127f22-26d8-5151-9b8e-1b53f96cedb6` | 469-489 [crates/gwiki/src/health.rs:469-489] | Indexed function `duplicate_concepts` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:469-489] |
| `render_paths` | function | `fn render_paths(text: &mut String, heading: &str, paths: &[PathBuf]) {` | `render_paths [function]` | `3915ed8d-cf6c-5da0-a73f-b118efa3f581` | 491-504 [crates/gwiki/src/health.rs:491-504] | Indexed function `render_paths` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:491-504] |
| `render_sources` | function | `fn render_sources(text: &mut String, heading: &str, sources: &[HealthSourceIssue]) {` | `render_sources [function]` | `0f343c25-8234-5046-a27e-72e786e0271f` | 506-521 [crates/gwiki/src/health.rs:506-521] | Indexed function `render_sources` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:506-521] |
| `render_broken_links` | function | `fn render_broken_links(text: &mut String, issues: &[crate::lint::LinkIssue]) {` | `render_broken_links [function]` | `52a1766a-685d-533d-8c9d-36959e015f9c` | 523-538 [crates/gwiki/src/health.rs:523-538] | Indexed function `render_broken_links` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:523-538] |
| `render_duplicate_concepts` | function | `fn render_duplicate_concepts(text: &mut String, duplicates: &[DuplicateConcept]) {` | `render_duplicate_concepts [function]` | `cb18da0f-5e4e-5b7d-8d13-ee44f5da9f5e` | 540-560 [crates/gwiki/src/health.rs:540-560] | Indexed function `render_duplicate_concepts` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:540-560] |
| `health_checks_required_cases` | function | `fn health_checks_required_cases() {` | `health_checks_required_cases [function]` | `7269f5b3-ec4a-573f-89f0-783909bec53f` | 568-611 [crates/gwiki/src/health.rs:568-611] | Indexed function `health_checks_required_cases` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:568-611] |
| `inspect_does_not_persist_health_snapshots` | function | `fn inspect_does_not_persist_health_snapshots() {` | `inspect_does_not_persist_health_snapshots [function]` | `ad2b78fd-4fa1-5265-a4a3-bcb804064ac3` | 614-638 [crates/gwiki/src/health.rs:614-638] | Indexed function `inspect_does_not_persist_health_snapshots` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:614-638] |
| `source_reference_matching_skips_code_fences_and_partial_words` | function | `fn source_reference_matching_skips_code_fences_and_partial_words() {` | `source_reference_matching_skips_code_fences_and_partial_words [function]` | `87a1399c-6487-5d9f-9e60-c3616113e8aa` | 641-654 [crates/gwiki/src/health.rs:641-654] | Indexed function `source_reference_matching_skips_code_fences_and_partial_words` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:641-654] |
| `citation_index_marks_cited_sources_once_per_page` | function | `fn citation_index_marks_cited_sources_once_per_page() {` | `citation_index_marks_cited_sources_once_per_page [function]` | `4689ee6f-ee25-58c0-a45c-0c00adbb4ca2` | 657-695 [crates/gwiki/src/health.rs:657-695] | Indexed function `citation_index_marks_cited_sources_once_per_page` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:657-695] |
| `cached_regex_returns_false_for_malformed_patterns` | function | `fn cached_regex_returns_false_for_malformed_patterns() {` | `cached_regex_returns_false_for_malformed_patterns [function]` | `3c438f63-463b-5304-b523-315a9332e936` | 698-700 [crates/gwiki/src/health.rs:698-700] | Indexed function `cached_regex_returns_false_for_malformed_patterns` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:698-700] |
| `stale_after_compares_dates_and_times_to_now` | function | `fn stale_after_compares_dates_and_times_to_now() {` | `stale_after_compares_dates_and_times_to_now [function]` | `c57b8b6a-a231-5476-bee2-eee435da290e` | 703-712 [crates/gwiki/src/health.rs:703-712] | Indexed function `stale_after_compares_dates_and_times_to_now` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:703-712] |
| `regex_cache_touch_updates_lru_order` | function | `fn regex_cache_touch_updates_lru_order() {` | `regex_cache_touch_updates_lru_order [function]` | `7b8015d9-cf15-5a10-977f-d67cac60898f` | 715-726 [crates/gwiki/src/health.rs:715-726] | Indexed function `regex_cache_touch_updates_lru_order` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:715-726] |
| `fenced_code_closes_only_on_matching_delimiter` | function | `fn fenced_code_closes_only_on_matching_delimiter() {` | `fenced_code_closes_only_on_matching_delimiter [function]` | `de2bf799-c120-503f-ba2a-a610d0277e49` | 729-735 [crates/gwiki/src/health.rs:729-735] | Indexed function `fenced_code_closes_only_on_matching_delimiter` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:729-735] |
| `fenced_code_requires_matching_marker_length` | function | `fn fenced_code_requires_matching_marker_length() {` | `fenced_code_requires_matching_marker_length [function]` | `a1f83db7-a365-55c1-93a7-1892e919847e` | 738-745 [crates/gwiki/src/health.rs:738-745] | Indexed function `fenced_code_requires_matching_marker_length` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:738-745] |
| `stale_citation_env_rejects_invalid_values` | function | `fn stale_citation_env_rejects_invalid_values() {` | `stale_citation_env_rejects_invalid_values [function]` | `5abb0747-9e2f-5286-838a-f84ce15607c8` | 748-753 [crates/gwiki/src/health.rs:748-753] | Indexed function `stale_citation_env_rejects_invalid_values` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:748-753] |
| `stale_citation_uses_full_fetched_timestamp` | function | `fn stale_citation_uses_full_fetched_timestamp() {` | `stale_citation_uses_full_fetched_timestamp [function]` | `9db51653-7d4d-5c51-9716-2397299f42e6` | 756-769 [crates/gwiki/src/health.rs:756-769] | Indexed function `stale_citation_uses_full_fetched_timestamp` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:756-769] |
| `change_triggered_refresh_health_degrades_to_provenance_only_mapping` | function | `fn change_triggered_refresh_health_degrades_to_provenance_only_mapping() {` | `change_triggered_refresh_health_degrades_to_provenance_only_mapping [function]` | `ffb0c270-15d1-5f51-951c-a858b98e55b3` | 772-807 [crates/gwiki/src/health.rs:772-807] | Indexed function `change_triggered_refresh_health_degrades_to_provenance_only_mapping` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:772-807] |
| `write_page` | function | `fn write_page(root: &Path, relative: &str, markdown: &str) {` | `write_page [function]` | `928a548c-07e6-59b8-addd-73f3f27be823` | 809-813 [crates/gwiki/src/health.rs:809-813] | Indexed function `write_page` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:809-813] |
| `source_record` | function | `fn source_record(fetched_at: &str) -> SourceRecord {` | `source_record [function]` | `a0aec9fa-bb33-5cba-9543-5facdbbc2c67` | 815-830 [crates/gwiki/src/health.rs:815-830] | Indexed function `source_record` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:815-830] |
