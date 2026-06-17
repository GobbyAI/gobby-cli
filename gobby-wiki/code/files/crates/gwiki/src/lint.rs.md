---
title: crates/gwiki/src/lint.rs
type: code_file
provenance:
- file: crates/gwiki/src/lint.rs
  ranges:
  - 13-22
  - 25-30
  - 33-36
  - 38-103
  - 105-126
  - 129-135
  - 137-169
  - 171-173
  - 175-181
  - 183-195
  - 197-254
  - 256-262
  - 264-270
  - 272-282
  - 284-290
  - 292-306
  - 308-316
  - 318-347
  - 349-365
  - 367-376
  - 378-397
  - 399-433
  - 435-440
  - 442-461
  - 463-476
  - 478-484
  - 487-493
  - 500-532
  - 535-552
  - 555-560
  - 563-568
  - 571-587
  - 589-593
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/lint.rs:13-22](crates/gwiki/src/lint.rs#L13-L22), [crates/gwiki/src/lint.rs:25-30](crates/gwiki/src/lint.rs#L25-L30), [crates/gwiki/src/lint.rs:33-36](crates/gwiki/src/lint.rs#L33-L36), [crates/gwiki/src/lint.rs:38-103](crates/gwiki/src/lint.rs#L38-L103), [crates/gwiki/src/lint.rs:105-126](crates/gwiki/src/lint.rs#L105-L126), [crates/gwiki/src/lint.rs:129-135](crates/gwiki/src/lint.rs#L129-L135), [crates/gwiki/src/lint.rs:137-169](crates/gwiki/src/lint.rs#L137-L169), [crates/gwiki/src/lint.rs:171-173](crates/gwiki/src/lint.rs#L171-L173), [crates/gwiki/src/lint.rs:175-181](crates/gwiki/src/lint.rs#L175-L181), [crates/gwiki/src/lint.rs:183-195](crates/gwiki/src/lint.rs#L183-L195), [crates/gwiki/src/lint.rs:197-254](crates/gwiki/src/lint.rs#L197-L254), [crates/gwiki/src/lint.rs:256-262](crates/gwiki/src/lint.rs#L256-L262), [crates/gwiki/src/lint.rs:264-270](crates/gwiki/src/lint.rs#L264-L270), [crates/gwiki/src/lint.rs:272-282](crates/gwiki/src/lint.rs#L272-L282), [crates/gwiki/src/lint.rs:284-290](crates/gwiki/src/lint.rs#L284-L290), [crates/gwiki/src/lint.rs:292-306](crates/gwiki/src/lint.rs#L292-L306), [crates/gwiki/src/lint.rs:308-316](crates/gwiki/src/lint.rs#L308-L316), [crates/gwiki/src/lint.rs:318-347](crates/gwiki/src/lint.rs#L318-L347), [crates/gwiki/src/lint.rs:349-365](crates/gwiki/src/lint.rs#L349-L365), [crates/gwiki/src/lint.rs:367-376](crates/gwiki/src/lint.rs#L367-L376), [crates/gwiki/src/lint.rs:378-397](crates/gwiki/src/lint.rs#L378-L397), [crates/gwiki/src/lint.rs:399-433](crates/gwiki/src/lint.rs#L399-L433), [crates/gwiki/src/lint.rs:435-440](crates/gwiki/src/lint.rs#L435-L440), [crates/gwiki/src/lint.rs:442-461](crates/gwiki/src/lint.rs#L442-L461), [crates/gwiki/src/lint.rs:463-476](crates/gwiki/src/lint.rs#L463-L476), [crates/gwiki/src/lint.rs:478-484](crates/gwiki/src/lint.rs#L478-L484), [crates/gwiki/src/lint.rs:487-493](crates/gwiki/src/lint.rs#L487-L493), [crates/gwiki/src/lint.rs:500-532](crates/gwiki/src/lint.rs#L500-L532), [crates/gwiki/src/lint.rs:535-552](crates/gwiki/src/lint.rs#L535-L552), [crates/gwiki/src/lint.rs:555-560](crates/gwiki/src/lint.rs#L555-L560), [crates/gwiki/src/lint.rs:563-568](crates/gwiki/src/lint.rs#L563-L568), [crates/gwiki/src/lint.rs:571-587](crates/gwiki/src/lint.rs#L571-L587), [crates/gwiki/src/lint.rs:589-593](crates/gwiki/src/lint.rs#L589-L593)

</details>

# crates/gwiki/src/lint.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements a read-only wiki linter that scans a vault, parses each page’s frontmatter and markdown, resolves wiki and markdown links, and assembles a `LintReport` describing broken links, orphan pages, missing frontmatter, duplicate aliases, and missing backlinks. The main `run` flow builds page and target maps, tracks inbound/outgoing links, and uses helper functions to normalize paths, classify link targets, filter ignored or exempt cases, and render human-readable summaries for issues and paths.
[crates/gwiki/src/lint.rs:13-22]
[crates/gwiki/src/lint.rs:25-30]
[crates/gwiki/src/lint.rs:33-36]
[crates/gwiki/src/lint.rs:38-103]
[crates/gwiki/src/lint.rs:105-126]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `LintReport` | class | `pub struct LintReport {` | `LintReport [class]` | `fabd96aa-0ccd-5f9d-857c-74c101a15b1e` | 13-22 [crates/gwiki/src/lint.rs:13-22] | Indexed class `LintReport` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:13-22] |
| `LinkIssue` | class | `pub struct LinkIssue {` | `LinkIssue [class]` | `38e9052c-2455-5794-93cc-4c812451565b` | 25-30 [crates/gwiki/src/lint.rs:25-30] | Indexed class `LinkIssue` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:25-30] |
| `DuplicateAlias` | class | `pub struct DuplicateAlias {` | `DuplicateAlias [class]` | `e6f6f987-8d12-50b3-8b53-e51adfae13ac` | 33-36 [crates/gwiki/src/lint.rs:33-36] | Indexed class `DuplicateAlias` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:33-36] |
| `run` | function | `pub fn run(vault_root: &Path, scope: ScopeIdentity) -> Result<LintReport, WikiError> {` | `run [function]` | `ef465155-fa1a-51ff-9897-980c4184011c` | 38-103 [crates/gwiki/src/lint.rs:38-103] | Indexed function `run` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:38-103] |
| `render_text` | function | `pub fn render_text(report: &LintReport) -> String {` | `render_text [function]` | `c0dfda7d-c6eb-57da-9019-ab65cbf64f5f` | 105-126 [crates/gwiki/src/lint.rs:105-126] | Indexed function `render_text` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:105-126] |
| `WikiPage` | class | `pub(crate) struct WikiPage {` | `WikiPage [class]` | `5e1302a3-5982-521b-bf7a-e1e6245339ef` | 129-135 [crates/gwiki/src/lint.rs:129-135] | Indexed class `WikiPage` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:129-135] |
| `collect_pages` | function | `pub(crate) fn collect_pages(vault_root: &Path) -> Result<Vec<WikiPage>, WikiError> {` | `collect_pages [function]` | `19127504-a8f8-5b7a-9293-b9bd5b2eb0c7` | 137-169 [crates/gwiki/src/lint.rs:137-169] | Indexed function `collect_pages` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:137-169] |
| `relative_path` | function | `pub(crate) fn relative_path(root: &Path, path: &Path) -> PathBuf {` | `relative_path [function]` | `e72186f3-48f4-52f4-8927-60f61a8d89d1` | 171-173 [crates/gwiki/src/lint.rs:171-173] | Indexed function `relative_path` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:171-173] |
| `line_number` | function | `pub(crate) fn line_number(markdown: &str, byte_start: usize) -> usize {` | `line_number [function]` | `a9b1a0ad-5d4c-5ec8-875b-cbdedca2476b` | 175-181 [crates/gwiki/src/lint.rs:175-181] | Indexed function `line_number` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:175-181] |
| `title_for_page` | function | `pub(crate) fn title_for_page(page: &WikiPage) -> String {` | `title_for_page [function]` | `00a42b27-b27d-5d92-bcb3-10217a252f9c` | 183-195 [crates/gwiki/src/lint.rs:183-195] | Indexed function `title_for_page` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:183-195] |
| `collect_markdown_files` | function | `fn collect_markdown_files(` | `collect_markdown_files [function]` | `3804c0f5-d347-571c-a356-873635f0c326` | 197-254 [crates/gwiki/src/lint.rs:197-254] | Indexed function `collect_markdown_files` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:197-254] |
| `is_markdown_path` | function | `fn is_markdown_path(path: &Path) -> bool {` | `is_markdown_path [function]` | `5b272c42-2078-593e-9e54-fe7b9b492e43` | 256-262 [crates/gwiki/src/lint.rs:256-262] | Indexed function `is_markdown_path` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:256-262] |
| `known_targets` | function | `fn known_targets(raw_pages: &[RawWikiPage]) -> BTreeSet<String> {` | `known_targets [function]` | `7afad565-6b6d-5711-adc5-973d4976b786` | 264-270 [crates/gwiki/src/lint.rs:264-270] | Indexed function `known_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:264-270] |
| `target_map` | function | `fn target_map(pages: &[WikiPage]) -> BTreeMap<String, PathBuf> {` | `target_map [function]` | `08fc4ede-258b-5357-8655-592eb3fc7c97` | 272-282 [crates/gwiki/src/lint.rs:272-282] | Indexed function `target_map` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:272-282] |
| `insert_page_targets` | function | `fn insert_page_targets(` | `insert_page_targets [function]` | `51d2b7a3-efdd-5b81-8e10-c42456d34ff1` | 284-290 [crates/gwiki/src/lint.rs:284-290] | Indexed function `insert_page_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:284-290] |
| `page_targets` | function | `fn page_targets(relative_path: &Path, frontmatter: &WikiFrontmatter) -> Vec<String> {` | `page_targets [function]` | `52619537-64d0-521e-8dfc-758fa37c9f97` | 292-306 [crates/gwiki/src/lint.rs:292-306] | Indexed function `page_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:292-306] |
| `ignored_target` | function | `fn ignored_target(target: &str) -> bool {` | `ignored_target [function]` | `f138cc7a-27a2-5084-9235-82cea54d345d` | 308-316 [crates/gwiki/src/lint.rs:308-316] | Indexed function `ignored_target` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:308-316] |
| `link_lookup_targets` | function | `fn link_lookup_targets(page: &WikiPage, link: &WikiLink) -> Vec<String> {` | `link_lookup_targets [function]` | `5311575e-1b64-50ac-bb76-689f172a098c` | 318-347 [crates/gwiki/src/lint.rs:318-347] | Indexed function `link_lookup_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:318-347] |
| `normalize_path_components` | function | `fn normalize_path_components(parent: &str, target: &str) -> String {` | `normalize_path_components [function]` | `11223fd4-7714-59a5-99f0-7a11741c4d40` | 349-365 [crates/gwiki/src/lint.rs:349-365] | Indexed function `normalize_path_components` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:349-365] |
| `is_orphan_exempt` | function | `fn is_orphan_exempt(path: &Path) -> bool {` | `is_orphan_exempt [function]` | `a19d0f16-deda-56ed-b071-b2bfa940ecdf` | 367-376 [crates/gwiki/src/lint.rs:367-376] | Indexed function `is_orphan_exempt` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:367-376] |
| `duplicate_aliases` | function | `fn duplicate_aliases(pages: &[WikiPage]) -> Vec<DuplicateAlias> {` | `duplicate_aliases [function]` | `3ac55f97-05f9-5535-876b-91fa1257fcdd` | 378-397 [crates/gwiki/src/lint.rs:378-397] | Indexed function `duplicate_aliases` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:378-397] |
| `missing_backlinks` | function | `fn missing_backlinks(` | `missing_backlinks [function]` | `fd7158fa-2ad6-52ac-b76e-ca84896770b6` | 399-433 [crates/gwiki/src/lint.rs:399-433] | Indexed function `missing_backlinks` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:399-433] |
| `link_kind` | function | `fn link_kind(kind: LinkKind) -> &'static str {` | `link_kind [function]` | `7391078e-a867-5e2b-a530-fe7d675156ba` | 435-440 [crates/gwiki/src/lint.rs:435-440] | Indexed function `link_kind` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:435-440] |
| `render_link_issues` | function | `fn render_link_issues(text: &mut String, heading: &str, issues: &[LinkIssue]) {` | `render_link_issues [function]` | `b055cdeb-9044-5a7f-9b51-5b8c75fb01af` | 442-461 [crates/gwiki/src/lint.rs:442-461] | Indexed function `render_link_issues` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:442-461] |
| `render_paths` | function | `fn render_paths(text: &mut String, heading: &str, paths: &[PathBuf]) {` | `render_paths [function]` | `7ac78ddf-dac5-5516-ba72-5618af878f90` | 463-476 [crates/gwiki/src/lint.rs:463-476] | Indexed function `render_paths` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:463-476] |
| `join_paths` | function | `fn join_paths(paths: &[PathBuf]) -> String {` | `join_paths [function]` | `4ec8c346-aad4-5087-9bad-847ea545eb73` | 478-484 [crates/gwiki/src/lint.rs:478-484] | Indexed function `join_paths` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:478-484] |
| `RawWikiPage` | class | `struct RawWikiPage {` | `RawWikiPage [class]` | `ba76b4f5-8b0f-5cfe-aa96-7bb1372c0712` | 487-493 [crates/gwiki/src/lint.rs:487-493] | Indexed class `RawWikiPage` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:487-493] |
| `detects_broken_links_and_orphans` | function | `fn detects_broken_links_and_orphans() {` | `detects_broken_links_and_orphans [function]` | `b6293c7b-7275-50b9-8d89-9ee1d5eec6c2` | 500-532 [crates/gwiki/src/lint.rs:500-532] | Indexed function `detects_broken_links_and_orphans` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:500-532] |
| `nested_wikilinks_resolve_relative_to_current_subtree` | function | `fn nested_wikilinks_resolve_relative_to_current_subtree() {` | `nested_wikilinks_resolve_relative_to_current_subtree [function]` | `ac4f6ea5-95af-5eb1-9d35-347049e1be38` | 535-552 [crates/gwiki/src/lint.rs:535-552] | Indexed function `nested_wikilinks_resolve_relative_to_current_subtree` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:535-552] |
| `relative_markdown_links_clamp_traversal_at_vault_root` | function | `fn relative_markdown_links_clamp_traversal_at_vault_root() {` | `relative_markdown_links_clamp_traversal_at_vault_root [function]` | `209ddca7-d222-5906-96ed-538115984c58` | 555-560 [crates/gwiki/src/lint.rs:555-560] | Indexed function `relative_markdown_links_clamp_traversal_at_vault_root` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:555-560] |
| `ignored_target_skips_external_network_references` | function | `fn ignored_target_skips_external_network_references() {` | `ignored_target_skips_external_network_references [function]` | `b64c6775-747c-5816-be20-254269dcade8` | 563-568 [crates/gwiki/src/lint.rs:563-568] | Indexed function `ignored_target_skips_external_network_references` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:563-568] |
| `lint_is_read_only` | function | `fn lint_is_read_only() {` | `lint_is_read_only [function]` | `ce6678ce-74c1-5487-9992-59cb3062f14d` | 571-587 [crates/gwiki/src/lint.rs:571-587] | Indexed function `lint_is_read_only` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:571-587] |
| `write_page` | function | `fn write_page(root: &Path, relative: &str, markdown: &str) {` | `write_page [function]` | `ebdc8297-4898-5d5f-a45b-4fbb22d41bf6` | 589-593 [crates/gwiki/src/lint.rs:589-593] | Indexed function `write_page` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:589-593] |
