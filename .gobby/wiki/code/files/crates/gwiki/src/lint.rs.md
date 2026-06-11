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

# crates/gwiki/src/lint.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/lint.rs` exposes 33 indexed API symbols.
[crates/gwiki/src/lint.rs:13-22]
[crates/gwiki/src/lint.rs:25-30]
[crates/gwiki/src/lint.rs:33-36]
[crates/gwiki/src/lint.rs:38-103]
[crates/gwiki/src/lint.rs:105-126]

## API Symbols

- `LintReport` (class) component `LintReport [class]` (`fabd96aa-0ccd-5f9d-857c-74c101a15b1e`) lines 13-22 [crates/gwiki/src/lint.rs:13-22]
  - Signature: `pub struct LintReport {`
  - Purpose: Indexed class `LintReport` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:13-22]
- `LinkIssue` (class) component `LinkIssue [class]` (`38e9052c-2455-5794-93cc-4c812451565b`) lines 25-30 [crates/gwiki/src/lint.rs:25-30]
  - Signature: `pub struct LinkIssue {`
  - Purpose: Indexed class `LinkIssue` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:25-30]
- `DuplicateAlias` (class) component `DuplicateAlias [class]` (`e6f6f987-8d12-50b3-8b53-e51adfae13ac`) lines 33-36 [crates/gwiki/src/lint.rs:33-36]
  - Signature: `pub struct DuplicateAlias {`
  - Purpose: Indexed class `DuplicateAlias` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:33-36]
- `run` (function) component `run [function]` (`ef465155-fa1a-51ff-9897-980c4184011c`) lines 38-103 [crates/gwiki/src/lint.rs:38-103]
  - Signature: `pub fn run(vault_root: &Path, scope: ScopeIdentity) -> Result<LintReport, WikiError> {`
  - Purpose: Indexed function `run` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:38-103]
- `render_text` (function) component `render_text [function]` (`c0dfda7d-c6eb-57da-9019-ab65cbf64f5f`) lines 105-126 [crates/gwiki/src/lint.rs:105-126]
  - Signature: `pub fn render_text(report: &LintReport) -> String {`
  - Purpose: Indexed function `render_text` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:105-126]
- `WikiPage` (class) component `WikiPage [class]` (`5e1302a3-5982-521b-bf7a-e1e6245339ef`) lines 129-135 [crates/gwiki/src/lint.rs:129-135]
  - Signature: `pub(crate) struct WikiPage {`
  - Purpose: Indexed class `WikiPage` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:129-135]
- `collect_pages` (function) component `collect_pages [function]` (`19127504-a8f8-5b7a-9293-b9bd5b2eb0c7`) lines 137-169 [crates/gwiki/src/lint.rs:137-169]
  - Signature: `pub(crate) fn collect_pages(vault_root: &Path) -> Result<Vec<WikiPage>, WikiError> {`
  - Purpose: Indexed function `collect_pages` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:137-169]
- `relative_path` (function) component `relative_path [function]` (`e72186f3-48f4-52f4-8927-60f61a8d89d1`) lines 171-173 [crates/gwiki/src/lint.rs:171-173]
  - Signature: `pub(crate) fn relative_path(root: &Path, path: &Path) -> PathBuf {`
  - Purpose: Indexed function `relative_path` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:171-173]
- `line_number` (function) component `line_number [function]` (`a9b1a0ad-5d4c-5ec8-875b-cbdedca2476b`) lines 175-181 [crates/gwiki/src/lint.rs:175-181]
  - Signature: `pub(crate) fn line_number(markdown: &str, byte_start: usize) -> usize {`
  - Purpose: Indexed function `line_number` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:175-181]
- `title_for_page` (function) component `title_for_page [function]` (`00a42b27-b27d-5d92-bcb3-10217a252f9c`) lines 183-195 [crates/gwiki/src/lint.rs:183-195]
  - Signature: `pub(crate) fn title_for_page(page: &WikiPage) -> String {`
  - Purpose: Indexed function `title_for_page` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:183-195]
- `collect_markdown_files` (function) component `collect_markdown_files [function]` (`3804c0f5-d347-571c-a356-873635f0c326`) lines 197-254 [crates/gwiki/src/lint.rs:197-254]
  - Signature: `fn collect_markdown_files(`
  - Purpose: Indexed function `collect_markdown_files` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:197-254]
- `is_markdown_path` (function) component `is_markdown_path [function]` (`5b272c42-2078-593e-9e54-fe7b9b492e43`) lines 256-262 [crates/gwiki/src/lint.rs:256-262]
  - Signature: `fn is_markdown_path(path: &Path) -> bool {`
  - Purpose: Indexed function `is_markdown_path` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:256-262]
- `known_targets` (function) component `known_targets [function]` (`7afad565-6b6d-5711-adc5-973d4976b786`) lines 264-270 [crates/gwiki/src/lint.rs:264-270]
  - Signature: `fn known_targets(raw_pages: &[RawWikiPage]) -> BTreeSet<String> {`
  - Purpose: Indexed function `known_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:264-270]
- `target_map` (function) component `target_map [function]` (`08fc4ede-258b-5357-8655-592eb3fc7c97`) lines 272-282 [crates/gwiki/src/lint.rs:272-282]
  - Signature: `fn target_map(pages: &[WikiPage]) -> BTreeMap<String, PathBuf> {`
  - Purpose: Indexed function `target_map` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:272-282]
- `insert_page_targets` (function) component `insert_page_targets [function]` (`51d2b7a3-efdd-5b81-8e10-c42456d34ff1`) lines 284-290 [crates/gwiki/src/lint.rs:284-290]
  - Signature: `fn insert_page_targets(`
  - Purpose: Indexed function `insert_page_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:284-290]
- `page_targets` (function) component `page_targets [function]` (`52619537-64d0-521e-8dfc-758fa37c9f97`) lines 292-306 [crates/gwiki/src/lint.rs:292-306]
  - Signature: `fn page_targets(relative_path: &Path, frontmatter: &WikiFrontmatter) -> Vec<String> {`
  - Purpose: Indexed function `page_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:292-306]
- `ignored_target` (function) component `ignored_target [function]` (`f138cc7a-27a2-5084-9235-82cea54d345d`) lines 308-316 [crates/gwiki/src/lint.rs:308-316]
  - Signature: `fn ignored_target(target: &str) -> bool {`
  - Purpose: Indexed function `ignored_target` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:308-316]
- `link_lookup_targets` (function) component `link_lookup_targets [function]` (`5311575e-1b64-50ac-bb76-689f172a098c`) lines 318-347 [crates/gwiki/src/lint.rs:318-347]
  - Signature: `fn link_lookup_targets(page: &WikiPage, link: &WikiLink) -> Vec<String> {`
  - Purpose: Indexed function `link_lookup_targets` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:318-347]
- `normalize_path_components` (function) component `normalize_path_components [function]` (`11223fd4-7714-59a5-99f0-7a11741c4d40`) lines 349-365 [crates/gwiki/src/lint.rs:349-365]
  - Signature: `fn normalize_path_components(parent: &str, target: &str) -> String {`
  - Purpose: Indexed function `normalize_path_components` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:349-365]
- `is_orphan_exempt` (function) component `is_orphan_exempt [function]` (`a19d0f16-deda-56ed-b071-b2bfa940ecdf`) lines 367-376 [crates/gwiki/src/lint.rs:367-376]
  - Signature: `fn is_orphan_exempt(path: &Path) -> bool {`
  - Purpose: Indexed function `is_orphan_exempt` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:367-376]
- `duplicate_aliases` (function) component `duplicate_aliases [function]` (`3ac55f97-05f9-5535-876b-91fa1257fcdd`) lines 378-397 [crates/gwiki/src/lint.rs:378-397]
  - Signature: `fn duplicate_aliases(pages: &[WikiPage]) -> Vec<DuplicateAlias> {`
  - Purpose: Indexed function `duplicate_aliases` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:378-397]
- `missing_backlinks` (function) component `missing_backlinks [function]` (`fd7158fa-2ad6-52ac-b76e-ca84896770b6`) lines 399-433 [crates/gwiki/src/lint.rs:399-433]
  - Signature: `fn missing_backlinks(`
  - Purpose: Indexed function `missing_backlinks` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:399-433]
- `link_kind` (function) component `link_kind [function]` (`7391078e-a867-5e2b-a530-fe7d675156ba`) lines 435-440 [crates/gwiki/src/lint.rs:435-440]
  - Signature: `fn link_kind(kind: LinkKind) -> &'static str {`
  - Purpose: Indexed function `link_kind` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:435-440]
- `render_link_issues` (function) component `render_link_issues [function]` (`b055cdeb-9044-5a7f-9b51-5b8c75fb01af`) lines 442-461 [crates/gwiki/src/lint.rs:442-461]
  - Signature: `fn render_link_issues(text: &mut String, heading: &str, issues: &[LinkIssue]) {`
  - Purpose: Indexed function `render_link_issues` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:442-461]
- `render_paths` (function) component `render_paths [function]` (`7ac78ddf-dac5-5516-ba72-5618af878f90`) lines 463-476 [crates/gwiki/src/lint.rs:463-476]
  - Signature: `fn render_paths(text: &mut String, heading: &str, paths: &[PathBuf]) {`
  - Purpose: Indexed function `render_paths` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:463-476]
- `join_paths` (function) component `join_paths [function]` (`4ec8c346-aad4-5087-9bad-847ea545eb73`) lines 478-484 [crates/gwiki/src/lint.rs:478-484]
  - Signature: `fn join_paths(paths: &[PathBuf]) -> String {`
  - Purpose: Indexed function `join_paths` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:478-484]
- `RawWikiPage` (class) component `RawWikiPage [class]` (`ba76b4f5-8b0f-5cfe-aa96-7bb1372c0712`) lines 487-493 [crates/gwiki/src/lint.rs:487-493]
  - Signature: `struct RawWikiPage {`
  - Purpose: Indexed class `RawWikiPage` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:487-493]
- `detects_broken_links_and_orphans` (function) component `detects_broken_links_and_orphans [function]` (`b6293c7b-7275-50b9-8d89-9ee1d5eec6c2`) lines 500-532 [crates/gwiki/src/lint.rs:500-532]
  - Signature: `fn detects_broken_links_and_orphans() {`
  - Purpose: Indexed function `detects_broken_links_and_orphans` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:500-532]
- `nested_wikilinks_resolve_relative_to_current_subtree` (function) component `nested_wikilinks_resolve_relative_to_current_subtree [function]` (`ac4f6ea5-95af-5eb1-9d35-347049e1be38`) lines 535-552 [crates/gwiki/src/lint.rs:535-552]
  - Signature: `fn nested_wikilinks_resolve_relative_to_current_subtree() {`
  - Purpose: Indexed function `nested_wikilinks_resolve_relative_to_current_subtree` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:535-552]
- `relative_markdown_links_clamp_traversal_at_vault_root` (function) component `relative_markdown_links_clamp_traversal_at_vault_root [function]` (`209ddca7-d222-5906-96ed-538115984c58`) lines 555-560 [crates/gwiki/src/lint.rs:555-560]
  - Signature: `fn relative_markdown_links_clamp_traversal_at_vault_root() {`
  - Purpose: Indexed function `relative_markdown_links_clamp_traversal_at_vault_root` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:555-560]
- `ignored_target_skips_external_network_references` (function) component `ignored_target_skips_external_network_references [function]` (`b64c6775-747c-5816-be20-254269dcade8`) lines 563-568 [crates/gwiki/src/lint.rs:563-568]
  - Signature: `fn ignored_target_skips_external_network_references() {`
  - Purpose: Indexed function `ignored_target_skips_external_network_references` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:563-568]
- `lint_is_read_only` (function) component `lint_is_read_only [function]` (`ce6678ce-74c1-5487-9992-59cb3062f14d`) lines 571-587 [crates/gwiki/src/lint.rs:571-587]
  - Signature: `fn lint_is_read_only() {`
  - Purpose: Indexed function `lint_is_read_only` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:571-587]
- `write_page` (function) component `write_page [function]` (`ebdc8297-4898-5d5f-a45b-4fbb22d41bf6`) lines 589-593 [crates/gwiki/src/lint.rs:589-593]
  - Signature: `fn write_page(root: &Path, relative: &str, markdown: &str) {`
  - Purpose: Indexed function `write_page` in `crates/gwiki/src/lint.rs`. [crates/gwiki/src/lint.rs:589-593]

