---
title: crates/gcode/src/index/walker.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker.rs
  ranges:
  - 35-38
  - 41-43
  - 45-51
  - 55-60
  - 62-107
  - 110-134
  - 138-148
  - 151-160
  - 163-175
  - 177-195
  - 197-213
  - 215-219
  - 222-224
  - 226-273
  - 275-289
  - 291-303
  - 305-311
  - 313-316
  - 318-326
  - 328-358
  - 360-385
  - 387-395
  - 397-422
  - 424-444
  - 446-451
  - 453-463
  - 465-471
  - 473-498
  - 504-510
  - 512-524
  - 527-566
  - 569-590
  - 593-604
  - 607-617
  - 620-629
  - 632-652
  - 655-674
  - 677-698
  - 701-716
  - 719-752
  - 755-777
  - 780-791
  - 794-812
  - 815-829
  - 832-845
  - 848-861
  - 864-877
  - 880-894
  - 897-907
  - 910-917
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file implements git-aware file discovery and classification for the gcode indexer. It discovers files eligible for indexing under a root directory while respecting .gitignore patterns, then classifies each file as either Ast (for syntactic analysis) or ContentOnly (for text search).

The core discovery flow uses `discover_files_with_options` to walk the filesystem with configurable gitignore respect, yielding two result lists of file candidates. Each discovered file is classified via `classify_file`, which applies a layered set of heuristics: it checks for hidden paths against an allowlist (managed by `HiddenPathAllowlist`), detects auto-generated markers in JavaScript files, identifies minified bundles by file size and line characteristics, recognizes generated metadata patterns (wiki, build artifacts), and validates file extension and content safety.

Helper predicates like `is_hidden_metadata_content_only`, `is_generated_js_bundle`, `looks_minified_js_bundle`, and `is_safe_text_file` work together to exclude generated or non-indexable content while preserving legitimate source code. The `HiddenPathAllowlist` class loads default allowlist patterns and project-specific overrides from `.gobby/gcode.json`, using glob pattern matching to determine which hidden files to include. Auxiliary utilities handle language detection, file prefix reading for marker scanning, and path visibility logic. The file also contains comprehensive test cases validating that discovery respects gitignore, classification handles various file types correctly, and special cases like generated wiki metadata and minified JS bundles are properly filtered.
[crates/gcode/src/index/walker.rs:35-38]
[crates/gcode/src/index/walker.rs:41-43]
[crates/gcode/src/index/walker.rs:45-51]
[crates/gcode/src/index/walker.rs:46-50]
[crates/gcode/src/index/walker.rs:55-60]

## API Symbols

- `FileClassification` (type) component `FileClassification [type]` (`69cfe4a5-80d2-57f4-aa68-395d80cebfd4`) lines 35-38 [crates/gcode/src/index/walker.rs:35-38]
  - Signature: `pub enum FileClassification {`
  - Purpose: Indexed type `FileClassification` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:35-38]
- `DiscoveryOptions` (class) component `DiscoveryOptions [class]` (`4748de9d-5491-57eb-b326-b6ad2d11ba46`) lines 41-43 [crates/gcode/src/index/walker.rs:41-43]
  - Signature: `pub struct DiscoveryOptions {`
  - Purpose: Indexed class `DiscoveryOptions` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:41-43]
- `DiscoveryOptions` (class) component `DiscoveryOptions [class]` (`da85b727-fa31-5519-8801-4f06e3d24f3b`) lines 45-51 [crates/gcode/src/index/walker.rs:45-51]
  - Signature: `impl Default for DiscoveryOptions {`
  - Purpose: Indexed class `DiscoveryOptions` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:45-51]
- `DiscoveryOptions.default` (method) component `DiscoveryOptions.default [method]` (`3b285eea-d96e-5f35-9248-e17ad2f737bf`) lines 46-50 [crates/gcode/src/index/walker.rs:46-50]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `DiscoveryOptions.default` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:46-50]
- `discover_files` (function) component `discover_files [function]` (`47390851-742b-5eb0-b55e-5ef0abf1ed42`) lines 55-60 [crates/gcode/src/index/walker.rs:55-60]
  - Signature: `pub fn discover_files<S: AsRef<str>>(`
  - Purpose: Indexed function `discover_files` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:55-60]
- `discover_files_with_options` (function) component `discover_files_with_options [function]` (`ea8b8b11-3552-51c8-8938-c3cee3be607f`) lines 62-107 [crates/gcode/src/index/walker.rs:62-107]
  - Signature: `pub fn discover_files_with_options<S: AsRef<str>>(`
  - Purpose: Indexed function `discover_files_with_options` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:62-107]
- `classify_file` (function) component `classify_file [function]` (`26923437-8608-5cf9-bb59-cbfb4d927ddc`) lines 110-134 [crates/gcode/src/index/walker.rs:110-134]
  - Signature: `pub fn classify_file(`
  - Purpose: Indexed function `classify_file` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:110-134]
- `classify_explicit_file_with_options` (function) component `classify_explicit_file_with_options [function]` (`a0063a2e-95ea-59c5-8f16-8356d37e46e2`) lines 138-148 [crates/gcode/src/index/walker.rs:138-148]
  - Signature: `pub fn classify_explicit_file_with_options(`
  - Purpose: Indexed function `classify_explicit_file_with_options` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:138-148]
- `is_content_indexable` (function) component `is_content_indexable [function]` (`0b88cb41-07fd-5a0a-a543-22790912c897`) lines 151-160 [crates/gcode/src/index/walker.rs:151-160]
  - Signature: `pub fn is_content_indexable(`
  - Purpose: Indexed function `is_content_indexable` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:151-160]
- `content_language` (function) component `content_language [function]` (`3557648e-a019-57c9-a9e0-8b5bc7980d5e`) lines 163-175 [crates/gcode/src/index/walker.rs:163-175]
  - Signature: `pub fn content_language(path: &Path) -> String {`
  - Purpose: Indexed function `content_language` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:163-175]
- `push_classified_file` (function) component `push_classified_file [function]` (`dc03a8f4-8f27-5898-a5d2-c99163111a4a`) lines 177-195 [crates/gcode/src/index/walker.rs:177-195]
  - Signature: `fn push_classified_file(`
  - Purpose: Indexed function `push_classified_file` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:177-195]
- `explicit_path_visible` (function) component `explicit_path_visible [function]` (`5ce009c8-0464-51ba-8c3f-a1e103137069`) lines 197-213 [crates/gcode/src/index/walker.rs:197-213]
  - Signature: `fn explicit_path_visible(root: &Path, path: &Path, options: DiscoveryOptions) -> bool {`
  - Purpose: Indexed function `explicit_path_visible` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:197-213]
- `same_existing_path` (function) component `same_existing_path [function]` (`1c829310-9ad1-5ff4-999a-144f4c068f94`) lines 215-219 [crates/gcode/src/index/walker.rs:215-219]
  - Signature: `fn same_existing_path(left: &Path, right: &Path) -> bool {`
  - Purpose: Indexed function `same_existing_path` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:215-219]
- `HiddenPathAllowlist` (class) component `HiddenPathAllowlist [class]` (`90bdece1-60bc-595d-939c-ed3b5adc18c6`) lines 222-224 [crates/gcode/src/index/walker.rs:222-224]
  - Signature: `struct HiddenPathAllowlist {`
  - Purpose: Indexed class `HiddenPathAllowlist` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:222-224]
- `HiddenPathAllowlist` (class) component `HiddenPathAllowlist [class]` (`a314e373-a29a-59a7-8a31-fd36d0ee77f5`) lines 226-273 [crates/gcode/src/index/walker.rs:226-273]
  - Signature: `impl HiddenPathAllowlist {`
  - Purpose: Indexed class `HiddenPathAllowlist` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:226-273]
- `HiddenPathAllowlist.load` (method) component `HiddenPathAllowlist.load [method]` (`ddb1b68e-e813-5aae-8846-7dffd00a5dcf`) lines 227-234 [crates/gcode/src/index/walker.rs:227-234]
  - Signature: `fn load(root: &Path) -> Self {`
  - Purpose: Indexed method `HiddenPathAllowlist.load` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:227-234]
- `HiddenPathAllowlist.from_patterns` (method) component `HiddenPathAllowlist.from_patterns [method]` (`c52093f3-c1cb-52d8-9a45-387fe3e92fcc`) lines 236-244 [crates/gcode/src/index/walker.rs:236-244]
  - Signature: `fn from_patterns(patterns: Vec<String>) -> Self {`
  - Purpose: Indexed method `HiddenPathAllowlist.from_patterns` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:236-244]
- `HiddenPathAllowlist.discover` (method) component `HiddenPathAllowlist.discover [method]` (`80b69712-5867-5225-9a42-ac488f266cc5`) lines 246-262 [crates/gcode/src/index/walker.rs:246-262]
  - Signature: `fn discover(&self, root: &Path) -> Vec<PathBuf> {`
  - Purpose: Indexed method `HiddenPathAllowlist.discover` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:246-262]
- `HiddenPathAllowlist.matches` (method) component `HiddenPathAllowlist.matches [method]` (`2bbcbe91-2491-594a-8b36-8f902927df29`) lines 264-272 [crates/gcode/src/index/walker.rs:264-272]
  - Signature: `fn matches(&self, root: &Path, path: &Path) -> bool {`
  - Purpose: Indexed method `HiddenPathAllowlist.matches` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:264-272]
- `read_project_hidden_allowlist` (function) component `read_project_hidden_allowlist [function]` (`69260939-f520-573f-8754-e62e11bc4d25`) lines 275-289 [crates/gcode/src/index/walker.rs:275-289]
  - Signature: `fn read_project_hidden_allowlist(root: &Path) -> Vec<String> {`
  - Purpose: Indexed function `read_project_hidden_allowlist` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:275-289]
- `is_valid_allowlist_pattern` (function) component `is_valid_allowlist_pattern [function]` (`48a5999b-b3a6-564c-9f79-f619aad46f00`) lines 291-303 [crates/gcode/src/index/walker.rs:291-303]
  - Signature: `fn is_valid_allowlist_pattern(pattern: &str) -> bool {`
  - Purpose: Indexed function `is_valid_allowlist_pattern` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:291-303]
- `expand_zero_depth_globstar` (function) component `expand_zero_depth_globstar [function]` (`72ce852a-cd0b-58b3-a6a3-120e7b5ca487`) lines 305-311 [crates/gcode/src/index/walker.rs:305-311]
  - Signature: `fn expand_zero_depth_globstar(pattern: &str) -> Vec<String> {`
  - Purpose: Indexed function `expand_zero_depth_globstar` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:305-311]
- `absolute_glob_pattern` (function) component `absolute_glob_pattern [function]` (`8318bbb3-6948-5a2e-8bf2-77fa5a9106eb`) lines 313-316 [crates/gcode/src/index/walker.rs:313-316]
  - Signature: `fn absolute_glob_pattern(root: &Path, pattern: &str) -> Option<String> {`
  - Purpose: Indexed function `absolute_glob_pattern` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:313-316]
- `is_hidden_path` (function) component `is_hidden_path [function]` (`6ffb19bb-2dd5-5e60-bc21-0ef673affe0d`) lines 318-326 [crates/gcode/src/index/walker.rs:318-326]
  - Signature: `fn is_hidden_path(root: &Path, path: &Path) -> bool {`
  - Purpose: Indexed function `is_hidden_path` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:318-326]
- `is_hidden_metadata_content_only` (function) component `is_hidden_metadata_content_only [function]` (`c48c8d73-4a4e-53ec-a431-0c4ab551fb08`) lines 328-358 [crates/gcode/src/index/walker.rs:328-358]
  - Signature: `fn is_hidden_metadata_content_only(root: &Path, path: &Path) -> bool {`
  - Purpose: Indexed function `is_hidden_metadata_content_only` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:328-358]
- `is_generated_wiki_metadata` (function) component `is_generated_wiki_metadata [function]` (`6cfb259e-88fe-5cd5-8f07-9d1d937beafc`) lines 360-385 [crates/gcode/src/index/walker.rs:360-385]
  - Signature: `fn is_generated_wiki_metadata(root: &Path, path: &Path) -> bool {`
  - Purpose: Indexed function `is_generated_wiki_metadata` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:360-385]
- `path_has_extension` (function) component `path_has_extension [function]` (`35a9da7f-ccf4-55b1-8420-1b81b750e70d`) lines 387-395 [crates/gcode/src/index/walker.rs:387-395]
  - Signature: `fn path_has_extension(path: &Path, extensions: &[&str]) -> bool {`
  - Purpose: Indexed function `path_has_extension` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:387-395]
- `is_safe_text_file` (function) component `is_safe_text_file [function]` (`1290a317-e1b5-5ae1-9591-72bae183b995`) lines 397-422 [crates/gcode/src/index/walker.rs:397-422]
  - Signature: `fn is_safe_text_file(root: &Path, path: &Path, exclude_patterns: &[impl AsRef<str>]) -> bool {`
  - Purpose: Indexed function `is_safe_text_file` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:397-422]
- `is_generated_js_bundle` (function) component `is_generated_js_bundle [function]` (`9d2bd1ca-20e9-5109-8cc8-382095e793d9`) lines 424-444 [crates/gcode/src/index/walker.rs:424-444]
  - Signature: `fn is_generated_js_bundle(path: &Path) -> bool {`
  - Purpose: Indexed function `is_generated_js_bundle` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:424-444]
- `read_file_prefix` (function) component `read_file_prefix [function]` (`1dfbfb1d-e01a-5383-955c-6b8d0ee22c03`) lines 446-451 [crates/gcode/src/index/walker.rs:446-451]
  - Signature: `fn read_file_prefix(path: &Path, max_bytes: u64) -> std::io::Result<Vec<u8>> {`
  - Purpose: Indexed function `read_file_prefix` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:446-451]
- `is_js_family_file` (function) component `is_js_family_file [function]` (`05a0b07e-e66b-5235-9ef0-b08c23f899ca`) lines 453-463 [crates/gcode/src/index/walker.rs:453-463]
  - Signature: `fn is_js_family_file(path: &Path) -> bool {`
  - Purpose: Indexed function `is_js_family_file` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:453-463]
- `contains_generated_js_marker` (function) component `contains_generated_js_marker [function]` (`a5b9a7b6-31d4-5066-af8e-231447281a69`) lines 465-471 [crates/gcode/src/index/walker.rs:465-471]
  - Signature: `fn contains_generated_js_marker(bytes: &[u8]) -> bool {`
  - Purpose: Indexed function `contains_generated_js_marker` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:465-471]
- `looks_minified_js_bundle` (function) component `looks_minified_js_bundle [function]` (`04b03c7b-c55e-5fb1-8b00-ca1d09b5d824`) lines 473-498 [crates/gcode/src/index/walker.rs:473-498]
  - Signature: `fn looks_minified_js_bundle(bytes: &[u8]) -> bool {`
  - Purpose: Indexed function `looks_minified_js_bundle` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:473-498]
- `write_file` (function) component `write_file [function]` (`4f32cb32-3983-5e2e-a133-2621571d3454`) lines 504-510 [crates/gcode/src/index/walker.rs:504-510]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) {`
  - Purpose: Indexed function `write_file` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:504-510]
- `rels` (function) component `rels [function]` (`7520b232-4ec2-551e-827c-1239b0bae576`) lines 512-524 [crates/gcode/src/index/walker.rs:512-524]
  - Signature: `fn rels(root: &Path, paths: Vec<PathBuf>) -> Vec<String> {`
  - Purpose: Indexed function `rels` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:512-524]
- `discovers_ast_and_content_only_text_files` (function) component `discovers_ast_and_content_only_text_files [function]` (`e6505c73-f69d-5454-b519-3e819caaa4cf`) lines 527-566 [crates/gcode/src/index/walker.rs:527-566]
  - Signature: `fn discovers_ast_and_content_only_text_files() {`
  - Purpose: Indexed function `discovers_ast_and_content_only_text_files` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:527-566]
- `discover_files_respects_gitignore_by_default_and_option` (function) component `discover_files_respects_gitignore_by_default_and_option [function]` (`08d29d34-cb96-533b-8e47-3b058d4d4bf8`) lines 569-590 [crates/gcode/src/index/walker.rs:569-590]
  - Signature: `fn discover_files_respects_gitignore_by_default_and_option() {`
  - Purpose: Indexed function `discover_files_respects_gitignore_by_default_and_option` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:569-590]
- `classifies_extensionless_text_as_content_only` (function) component `classifies_extensionless_text_as_content_only [function]` (`4042cde5-4beb-5122-a590-7e48a43d09b5`) lines 593-604 [crates/gcode/src/index/walker.rs:593-604]
  - Signature: `fn classifies_extensionless_text_as_content_only() {`
  - Purpose: Indexed function `classifies_extensionless_text_as_content_only` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:593-604]
- `classifies_markdown_content_language_as_markdown` (function) component `classifies_markdown_content_language_as_markdown [function]` (`07a71ef5-4c54-5822-b4fb-2653002cec29`) lines 607-617 [crates/gcode/src/index/walker.rs:607-617]
  - Signature: `fn classifies_markdown_content_language_as_markdown() {`
  - Purpose: Indexed function `classifies_markdown_content_language_as_markdown` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:607-617]
- `classifies_yaml_content_language_as_yaml` (function) component `classifies_yaml_content_language_as_yaml [function]` (`6c0f08de-e6c4-5b33-a8ca-002a4b4fe53f`) lines 620-629 [crates/gcode/src/index/walker.rs:620-629]
  - Signature: `fn classifies_yaml_content_language_as_yaml() {`
  - Purpose: Indexed function `classifies_yaml_content_language_as_yaml` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:620-629]
- `classifies_mjs_as_ast_and_markdown_as_content_only` (function) component `classifies_mjs_as_ast_and_markdown_as_content_only [function]` (`365abe5e-24c8-557d-97b7-4c01f4c3463a`) lines 632-652 [crates/gcode/src/index/walker.rs:632-652]
  - Signature: `fn classifies_mjs_as_ast_and_markdown_as_content_only() {`
  - Purpose: Indexed function `classifies_mjs_as_ast_and_markdown_as_content_only` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:632-652]
- `classifies_github_workflow_yaml_as_content_only` (function) component `classifies_github_workflow_yaml_as_content_only [function]` (`ecd69d6f-b2b0-5906-92de-344f4b5beca8`) lines 655-674 [crates/gcode/src/index/walker.rs:655-674]
  - Signature: `fn classifies_github_workflow_yaml_as_content_only() {`
  - Purpose: Indexed function `classifies_github_workflow_yaml_as_content_only` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:655-674]
- `discovers_default_hidden_metadata_allowlist` (function) component `discovers_default_hidden_metadata_allowlist [function]` (`25b2fd3e-3e6e-56f4-bd19-4b088b6c15e0`) lines 677-698 [crates/gcode/src/index/walker.rs:677-698]
  - Signature: `fn discovers_default_hidden_metadata_allowlist() {`
  - Purpose: Indexed function `discovers_default_hidden_metadata_allowlist` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:677-698]
- `skips_non_allowlisted_hidden_metadata_by_default` (function) component `skips_non_allowlisted_hidden_metadata_by_default [function]` (`685ba7af-8a9b-52b9-ac48-362104f0e044`) lines 701-716 [crates/gcode/src/index/walker.rs:701-716]
  - Signature: `fn skips_non_allowlisted_hidden_metadata_by_default() {`
  - Purpose: Indexed function `skips_non_allowlisted_hidden_metadata_by_default` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:701-716]
- `discovers_wiki_markdown_and_skips_generated_wiki_metadata` (function) component `discovers_wiki_markdown_and_skips_generated_wiki_metadata [function]` (`c47755d6-e715-597e-94e8-8cdbb682a177`) lines 719-752 [crates/gcode/src/index/walker.rs:719-752]
  - Signature: `fn discovers_wiki_markdown_and_skips_generated_wiki_metadata() {`
  - Purpose: Indexed function `discovers_wiki_markdown_and_skips_generated_wiki_metadata` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:719-752]
- `discovers_project_hidden_allowlist_from_gcode_json` (function) component `discovers_project_hidden_allowlist_from_gcode_json [function]` (`f44731a2-d1c3-59f9-bd27-e7bea963361f`) lines 755-777 [crates/gcode/src/index/walker.rs:755-777]
  - Signature: `fn discovers_project_hidden_allowlist_from_gcode_json() {`
  - Purpose: Indexed function `discovers_project_hidden_allowlist_from_gcode_json` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:755-777]
- `excludes_win_over_allowlisted_hidden_paths` (function) component `excludes_win_over_allowlisted_hidden_paths [function]` (`3f5d47c8-48b1-51fa-8347-569529ec5d07`) lines 780-791 [crates/gcode/src/index/walker.rs:780-791]
  - Signature: `fn excludes_win_over_allowlisted_hidden_paths() {`
  - Purpose: Indexed function `excludes_win_over_allowlisted_hidden_paths` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:780-791]
- `skips_js_family_files_with_generated_markers` (function) component `skips_js_family_files_with_generated_markers [function]` (`ed8fecda-00f7-5621-abfa-8817d9297112`) lines 794-812 [crates/gcode/src/index/walker.rs:794-812]
  - Signature: `fn skips_js_family_files_with_generated_markers() {`
  - Purpose: Indexed function `skips_js_family_files_with_generated_markers` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:794-812]
- `keeps_ordinary_mjs_source_ast_indexable` (function) component `keeps_ordinary_mjs_source_ast_indexable [function]` (`d6c260a7-3e2b-5344-a333-f59672f1aa51`) lines 815-829 [crates/gcode/src/index/walker.rs:815-829]
  - Signature: `fn keeps_ordinary_mjs_source_ast_indexable() {`
  - Purpose: Indexed function `keeps_ordinary_mjs_source_ast_indexable` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:815-829]
- `skips_large_minified_js_bundles` (function) component `skips_large_minified_js_bundles [function]` (`5e242768-9019-5c80-a76b-727f2584ea57`) lines 832-845 [crates/gcode/src/index/walker.rs:832-845]
  - Signature: `fn skips_large_minified_js_bundles() {`
  - Purpose: Indexed function `skips_large_minified_js_bundles` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:832-845]
- `skips_single_line_minified_js_bundle_with_newline` (function) component `skips_single_line_minified_js_bundle_with_newline [function]` (`d3cbc94c-0d89-57a4-8b0a-797312c148e8`) lines 848-861 [crates/gcode/src/index/walker.rs:848-861]
  - Signature: `fn skips_single_line_minified_js_bundle_with_newline() {`
  - Purpose: Indexed function `skips_single_line_minified_js_bundle_with_newline` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:848-861]
- `skips_single_line_minified_js_bundle_without_newline` (function) component `skips_single_line_minified_js_bundle_without_newline [function]` (`79191789-6434-53ff-814b-85d04c64d7ae`) lines 864-877 [crates/gcode/src/index/walker.rs:864-877]
  - Signature: `fn skips_single_line_minified_js_bundle_without_newline() {`
  - Purpose: Indexed function `skips_single_line_minified_js_bundle_without_newline` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:864-877]
- `classifies_source_build_directory_as_ast_indexable` (function) component `classifies_source_build_directory_as_ast_indexable [function]` (`b90a4156-2aab-5583-910c-728f5cf0236c`) lines 880-894 [crates/gcode/src/index/walker.rs:880-894]
  - Signature: `fn classifies_source_build_directory_as_ast_indexable() {`
  - Purpose: Indexed function `classifies_source_build_directory_as_ast_indexable` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:880-894]
- `skips_root_build_directory` (function) component `skips_root_build_directory [function]` (`028fe4bd-db40-553e-b5a7-ac83a4266eea`) lines 897-907 [crates/gcode/src/index/walker.rs:897-907]
  - Signature: `fn skips_root_build_directory() {`
  - Purpose: Indexed function `skips_root_build_directory` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:897-907]
- `walker_consumes_gobby_core_walker_settings` (function) component `walker_consumes_gobby_core_walker_settings [function]` (`9ba94745-c010-5fd9-b1df-f5d86cf4f307`) lines 910-917 [crates/gcode/src/index/walker.rs:910-917]
  - Signature: `fn walker_consumes_gobby_core_walker_settings() {`
  - Purpose: Indexed function `walker_consumes_gobby_core_walker_settings` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:910-917]

