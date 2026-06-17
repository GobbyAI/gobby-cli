---
title: crates/gwiki/src/librarian.rs
type: code_file
provenance:
- file: crates/gwiki/src/librarian.rs
  ranges:
  - 15-20
  - 23-30
  - 34-39
  - 43-50
  - 54-59
  - 63-69
  - 72-76
  - 79-85
  - 88-93
  - 96-100
  - 102-198
  - 200-230
  - 232-239
  - 241-253
  - 255-264
  - 266-272
  - 274-283
  - 285-291
  - 293-303
  - 305-355
  - 357-371
  - 373-390
  - 392-394
  - 396-403
  - 405-434
  - 436-452
  - 454-461
  - 475-562
  - 565-591
  - 594-617
  - 620-639
  - 642-656
  - 660-679
  - 681-685
  - 687-701
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/librarian.rs:15-20](crates/gwiki/src/librarian.rs#L15-L20), [crates/gwiki/src/librarian.rs:23-30](crates/gwiki/src/librarian.rs#L23-L30), [crates/gwiki/src/librarian.rs:34-39](crates/gwiki/src/librarian.rs#L34-L39), [crates/gwiki/src/librarian.rs:43-50](crates/gwiki/src/librarian.rs#L43-L50), [crates/gwiki/src/librarian.rs:54-59](crates/gwiki/src/librarian.rs#L54-L59), [crates/gwiki/src/librarian.rs:63-69](crates/gwiki/src/librarian.rs#L63-L69), [crates/gwiki/src/librarian.rs:72-76](crates/gwiki/src/librarian.rs#L72-L76), [crates/gwiki/src/librarian.rs:79-85](crates/gwiki/src/librarian.rs#L79-L85), [crates/gwiki/src/librarian.rs:88-93](crates/gwiki/src/librarian.rs#L88-L93), [crates/gwiki/src/librarian.rs:96-100](crates/gwiki/src/librarian.rs#L96-L100), [crates/gwiki/src/librarian.rs:102-198](crates/gwiki/src/librarian.rs#L102-L198), [crates/gwiki/src/librarian.rs:200-230](crates/gwiki/src/librarian.rs#L200-L230), [crates/gwiki/src/librarian.rs:232-239](crates/gwiki/src/librarian.rs#L232-L239), [crates/gwiki/src/librarian.rs:241-253](crates/gwiki/src/librarian.rs#L241-L253), [crates/gwiki/src/librarian.rs:255-264](crates/gwiki/src/librarian.rs#L255-L264), [crates/gwiki/src/librarian.rs:266-272](crates/gwiki/src/librarian.rs#L266-L272), [crates/gwiki/src/librarian.rs:274-283](crates/gwiki/src/librarian.rs#L274-L283), [crates/gwiki/src/librarian.rs:285-291](crates/gwiki/src/librarian.rs#L285-L291), [crates/gwiki/src/librarian.rs:293-303](crates/gwiki/src/librarian.rs#L293-L303), [crates/gwiki/src/librarian.rs:305-355](crates/gwiki/src/librarian.rs#L305-L355), [crates/gwiki/src/librarian.rs:357-371](crates/gwiki/src/librarian.rs#L357-L371), [crates/gwiki/src/librarian.rs:373-390](crates/gwiki/src/librarian.rs#L373-L390), [crates/gwiki/src/librarian.rs:392-394](crates/gwiki/src/librarian.rs#L392-L394), [crates/gwiki/src/librarian.rs:396-403](crates/gwiki/src/librarian.rs#L396-L403), [crates/gwiki/src/librarian.rs:405-434](crates/gwiki/src/librarian.rs#L405-L434), [crates/gwiki/src/librarian.rs:436-452](crates/gwiki/src/librarian.rs#L436-L452), [crates/gwiki/src/librarian.rs:454-461](crates/gwiki/src/librarian.rs#L454-L461), [crates/gwiki/src/librarian.rs:475-562](crates/gwiki/src/librarian.rs#L475-L562), [crates/gwiki/src/librarian.rs:565-591](crates/gwiki/src/librarian.rs#L565-L591), [crates/gwiki/src/librarian.rs:594-617](crates/gwiki/src/librarian.rs#L594-L617), [crates/gwiki/src/librarian.rs:620-639](crates/gwiki/src/librarian.rs#L620-L639), [crates/gwiki/src/librarian.rs:642-656](crates/gwiki/src/librarian.rs#L642-L656), [crates/gwiki/src/librarian.rs:660-679](crates/gwiki/src/librarian.rs#L660-L679), [crates/gwiki/src/librarian.rs:681-685](crates/gwiki/src/librarian.rs#L681-L685), [crates/gwiki/src/librarian.rs:687-701](crates/gwiki/src/librarian.rs#L687-L701)

</details>

# crates/gwiki/src/librarian.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the “librarian” pipeline for a wiki/codewiki scope: it configures what checks are allowed, runs the available and optional audits over the selected scope, and assembles the resulting proposal report. It also defines the report/data types and helper routines for turning checks into suggested tasks, patch diffs, artifact paths, and persisted JSON/text outputs, with tests covering scope filtering, optional-check degradation, ordering, and offline/index availability behavior.
[crates/gwiki/src/librarian.rs:15-20]
[crates/gwiki/src/librarian.rs:23-30]
[crates/gwiki/src/librarian.rs:34-39]
[crates/gwiki/src/librarian.rs:43-50]
[crates/gwiki/src/librarian.rs:54-59]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Options` | class | `pub struct Options {` | `Options [class]` | `470c03cf-0128-5697-8ff8-e84d2b915c41` | 15-20 [crates/gwiki/src/librarian.rs:15-20] | Indexed class `Options` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:15-20] |
| `Options::offline` | method | `pub fn offline() -> Self {` | `Options::offline [method]` | `64077f00-50a8-5001-883f-1cf3c7a4a00c` | 23-30 [crates/gwiki/src/librarian.rs:23-30] | Indexed method `Options::offline` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:23-30] |
| `Options::default` | method | `fn default() -> Self {` | `Options::default [method]` | `f6952d0f-2f66-5501-998a-be8697d7cfff` | 34-39 [crates/gwiki/src/librarian.rs:34-39] | Indexed method `Options::default` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:34-39] |
| `ProposalsReport` | class | `pub struct ProposalsReport {` | `ProposalsReport [class]` | `b175e249-d3f2-5232-87d6-ade0e8e3f238` | 43-50 [crates/gwiki/src/librarian.rs:43-50] | Indexed class `ProposalsReport` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:43-50] |
| `ProposalsReport::check` | method | `fn check(&self, name: &str) -> &CheckReport {` | `ProposalsReport::check [method]` | `93249c15-072e-5f05-a726-3ffeb88a2e9b` | 54-59 [crates/gwiki/src/librarian.rs:54-59] | Indexed method `ProposalsReport::check` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:54-59] |
| `CheckReport` | class | `pub struct CheckReport {` | `CheckReport [class]` | `9743d59c-9062-55be-8616-e2430fee16ad` | 63-69 [crates/gwiki/src/librarian.rs:63-69] | Indexed class `CheckReport` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:63-69] |
| `SuggestedTask` | class | `pub struct SuggestedTask {` | `SuggestedTask [class]` | `627081f8-f82a-54aa-b840-805c7c501565` | 72-76 [crates/gwiki/src/librarian.rs:72-76] | Indexed class `SuggestedTask` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:72-76] |
| `SuggestedPatchDiff` | class | `pub struct SuggestedPatchDiff {` | `SuggestedPatchDiff [class]` | `f028b8a9-fffa-57ba-9e90-f13d9df576df` | 79-85 [crates/gwiki/src/librarian.rs:79-85] | Indexed class `SuggestedPatchDiff` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:79-85] |
| `LibrarianArtifacts` | class | `pub struct LibrarianArtifacts {` | `LibrarianArtifacts [class]` | `17160810-14af-5337-9749-be22f25f6d6d` | 88-93 [crates/gwiki/src/librarian.rs:88-93] | Indexed class `LibrarianArtifacts` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:88-93] |
| `DependencyClassification` | class | `pub struct DependencyClassification {` | `DependencyClassification [class]` | `2e9e2fa8-d6fc-53cd-91c3-6a9f490d6a47` | 96-100 [crates/gwiki/src/librarian.rs:96-100] | Indexed class `DependencyClassification` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:96-100] |
| `run` | function | `pub fn run(` | `run [function]` | `91a0c8d5-ffd7-52b9-8726-8a9f00b63a8c` | 102-198 [crates/gwiki/src/librarian.rs:102-198] | Indexed function `run` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:102-198] |
| `render_text` | function | `pub fn render_text(report: &ProposalsReport) -> String {` | `render_text [function]` | `1ea3bae6-ab48-5cff-9d65-a438767f7994` | 200-230 [crates/gwiki/src/librarian.rs:200-230] | Indexed function `render_text` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:200-230] |
| `available_check` | function | `fn available_check(name: &'static str, items: Vec<PathBuf>) -> CheckReport {` | `available_check [function]` | `45cc9913-6d2c-5a3b-94dc-9dcaeee0b72c` | 232-239 [crates/gwiki/src/librarian.rs:232-239] | Indexed function `available_check` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:232-239] |
| `optional_check` | function | `fn optional_check(` | `optional_check [function]` | `4e5774c9-978f-56be-ae27-acc9521a0003` | 241-253 [crates/gwiki/src/librarian.rs:241-253] | Indexed function `optional_check` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:241-253] |
| `weak_provenance_pages` | function | `fn weak_provenance_pages(pages: &[lint::WikiPage], provenance: &ProvenanceGraph) -> Vec<PathBuf> {` | `weak_provenance_pages [function]` | `dda378e7-4cc9-559c-b0fc-979e3bf48398` | 255-264 [crates/gwiki/src/librarian.rs:255-264] | Indexed function `weak_provenance_pages` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:255-264] |
| `provenance_mentions_page` | function | `fn provenance_mentions_page(provenance: &ProvenanceGraph, path: &Path) -> bool {` | `provenance_mentions_page [function]` | `b42aa384-5348-5aab-b1cc-b955979da417` | 266-272 [crates/gwiki/src/librarian.rs:266-272] | Indexed function `provenance_mentions_page` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:266-272] |
| `outdated_codewiki_pages` | function | `fn outdated_codewiki_pages(pages: &[lint::WikiPage]) -> Vec<PathBuf> {` | `outdated_codewiki_pages [function]` | `6a86a166-55bc-5632-87b1-1d65298fc33c` | 274-283 [crates/gwiki/src/librarian.rs:274-283] | Indexed function `outdated_codewiki_pages` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:274-283] |
| `page_is_codewiki` | function | `fn page_is_codewiki(page: &lint::WikiPage) -> bool {` | `page_is_codewiki [function]` | `c146d506-0c60-59c1-96fd-ffd2bfc7889c` | 285-291 [crates/gwiki/src/librarian.rs:285-291] | Indexed function `page_is_codewiki` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:285-291] |
| `frontmatter_flag` | function | `fn frontmatter_flag(markdown: &str, key: &str, expected: &str) -> bool {` | `frontmatter_flag [function]` | `b0c37dc8-383d-5342-9962-7814f6ee1440` | 293-303 [crates/gwiki/src/librarian.rs:293-303] | Indexed function `frontmatter_flag` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:293-303] |
| `suggested_tasks` | function | `fn suggested_tasks(` | `suggested_tasks [function]` | `3dd4e688-a4ec-547b-bc78-f71e64f2981d` | 305-355 [crates/gwiki/src/librarian.rs:305-355] | Indexed function `suggested_tasks` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:305-355] |
| `push_task` | function | `fn push_task(` | `push_task [function]` | `3b4c3e5a-722e-5c44-84d6-38b8a550306a` | 357-371 [crates/gwiki/src/librarian.rs:357-371] | Indexed function `push_task` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:357-371] |
| `suggested_patch_diffs` | function | `fn suggested_patch_diffs(` | `suggested_patch_diffs [function]` | `12819a51-7af5-5a14-bb48-dce2eb62827f` | 373-390 [crates/gwiki/src/librarian.rs:373-390] | Indexed function `suggested_patch_diffs` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:373-390] |
| `unique_paths` | function | `fn unique_paths(paths: impl Iterator<Item = PathBuf>) -> Vec<PathBuf> {` | `unique_paths [function]` | `da33eb1c-4a9a-59b3-b076-e5c3e3955a2d` | 392-394 [crates/gwiki/src/librarian.rs:392-394] | Indexed function `unique_paths` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:392-394] |
| `artifacts` | function | `fn artifacts() -> LibrarianArtifacts {` | `artifacts [function]` | `752679d1-fdaa-53b7-8a7f-88ac30c507b9` | 396-403 [crates/gwiki/src/librarian.rs:396-403] | Indexed function `artifacts` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:396-403] |
| `persist_report` | function | `fn persist_report(vault_root: &Path, report: &ProposalsReport) -> Result<(), WikiError> {` | `persist_report [function]` | `7484246e-b4ee-51b4-99e5-9c002f9c1095` | 405-434 [crates/gwiki/src/librarian.rs:405-434] | Indexed function `persist_report` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:405-434] |
| `write_json` | function | `fn write_json<T: Serialize>(` | `write_json [function]` | `47e3ce88-0c68-52ad-8994-1798aae06e0b` | 436-452 [crates/gwiki/src/librarian.rs:436-452] | Indexed function `write_json` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:436-452] |
| `write_text` | function | `fn write_text(vault_root: &Path, relative: &Path, text: &str) -> Result<(), WikiError> {` | `write_text [function]` | `522f78b0-5017-5425-beb4-9fc2bd38575f` | 454-461 [crates/gwiki/src/librarian.rs:454-461] | Indexed function `write_text` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:454-461] |
| `librarian_detects_and_proposes_without_rewriting_pages` | function | `fn librarian_detects_and_proposes_without_rewriting_pages() {` | `librarian_detects_and_proposes_without_rewriting_pages [function]` | `c90b5439-c094-5784-9bf2-e29a397a9d27` | 475-562 [crates/gwiki/src/librarian.rs:475-562] | Indexed function `librarian_detects_and_proposes_without_rewriting_pages` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:475-562] |
| `librarian_filters_codewiki_checks_to_selected_scope` | function | `fn librarian_filters_codewiki_checks_to_selected_scope() {` | `librarian_filters_codewiki_checks_to_selected_scope [function]` | `19864fe4-a833-5723-b1b5-e373a69d02d4` | 565-591 [crates/gwiki/src/librarian.rs:565-591] | Indexed function `librarian_filters_codewiki_checks_to_selected_scope` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:565-591] |
| `librarian_degrades_each_optional_check_independently` | function | `fn librarian_degrades_each_optional_check_independently() {` | `librarian_degrades_each_optional_check_independently [function]` | `3393e5f2-8b80-54d6-822e-5ae55c66f2f3` | 594-617 [crates/gwiki/src/librarian.rs:594-617] | Indexed function `librarian_degrades_each_optional_check_independently` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:594-617] |
| `librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale` | function | `fn librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale() {` | `librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale [function]` | `13a9c968-ebe4-544b-857f-93cc0f41ac75` | 620-639 [crates/gwiki/src/librarian.rs:620-639] | Indexed function `librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:620-639] |
| `librarian_codewiki_path_checks_are_sorted` | function | `fn librarian_codewiki_path_checks_are_sorted() {` | `librarian_codewiki_path_checks_are_sorted [function]` | `f5dbf43d-d493-5b76-987a-75f0000f43e5` | 642-656 [crates/gwiki/src/librarian.rs:642-656] | Indexed function `librarian_codewiki_path_checks_are_sorted` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:642-656] |
| `librarian_requires_configured_postgres_index` | function | `fn librarian_requires_configured_postgres_index() {` | `librarian_requires_configured_postgres_index [function]` | `a52ae97f-39bd-562e-b00d-779e1cc0624c` | 660-679 [crates/gwiki/src/librarian.rs:660-679] | Indexed function `librarian_requires_configured_postgres_index` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:660-679] |
| `write_page` | function | `fn write_page(root: &Path, relative: &str, markdown: &str) {` | `write_page [function]` | `0a6de2ff-8122-53d3-8b28-8eb8f0d27e1d` | 681-685 [crates/gwiki/src/librarian.rs:681-685] | Indexed function `write_page` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:681-685] |
| `codewiki_page` | function | `fn codewiki_page(relative: &str, stale: bool) -> lint::WikiPage {` | `codewiki_page [function]` | `0baec6d0-d7e0-5231-b166-a070518ed4bb` | 687-701 [crates/gwiki/src/librarian.rs:687-701] | Indexed function `codewiki_page` in `crates/gwiki/src/librarian.rs`. [crates/gwiki/src/librarian.rs:687-701] |
