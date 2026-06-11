---
title: crates/gcode/src/index/walker.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker.rs
  ranges:
  - 36-39
  - 42-44
  - 46-52
  - 47-51
  - 56-61
  - 63-108
  - 111-135
  - 139-149
  - 152-161
  - 164-176
  - 178-196
  - 198-214
  - 216-220
  - 223-225
  - 227-274
  - 228-235
  - 237-245
  - 247-263
  - 265-273
  - 276-290
  - 292-304
  - 306-312
  - 314-317
  - 319-327
  - 329-359
  - 361-386
  - 388-396
  - 398-423
  - 425-445
  - 447-452
  - 454-464
  - 466-472
  - 474-499
  - 505-511
  - 513-525
  - 528-567
  - 570-591
  - 594-605
  - 608-618
  - 621-630
  - 633-653
  - 656-675
  - 678-699
  - 702-717
  - 720-753
  - 756-778
  - 781-792
  - 795-813
  - 816-830
  - 833-846
  - 849-862
  - 865-878
  - 881-895
  - 898-908
  - 911-918
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

`crates/gcode/src/index/walker.rs` exposes 55 indexed API symbols.
[crates/gcode/src/index/walker.rs:36-39]
[crates/gcode/src/index/walker.rs:42-44]
[crates/gcode/src/index/walker.rs:46-52]
[crates/gcode/src/index/walker.rs:47-51]
[crates/gcode/src/index/walker.rs:56-61]

## API Symbols

- `FileClassification` (type) component `FileClassification [type]` (`b25813a1-8fbf-5784-81e4-2c07bb58f697`) lines 36-39 [crates/gcode/src/index/walker.rs:36-39]
  - Signature: `pub enum FileClassification {`
  - Purpose: Indexed type `FileClassification` in `crates/gcode/src/index/walker.rs`. [crates/gcode/src/index/walker.rs:36-39]
- `DiscoveryOptions` (class) component `DiscoveryOptions [class]` (`7e8d19bd-8f08-5a8d-b354-4cabed849962`) lines 42-44 [crates/gcode/src/index/walker.rs:42-44]
  - Signature: `pub struct DiscoveryOptions {`
  - Purpose: `DiscoveryOptions` is a configuration struct containing a boolean flag to control whether `.gitignore` files are honored during file system discovery operations. [crates/gcode/src/index/walker.rs:42-44]
- `DiscoveryOptions` (class) component `DiscoveryOptions [class]` (`58ff72f6-7714-5570-9850-6a4c62d480c3`) lines 46-52 [crates/gcode/src/index/walker.rs:46-52]
  - Signature: `impl Default for DiscoveryOptions {`
  - Purpose: `DiscoveryOptions::default()` initializes an instance with `respect_gitignore` set to `true`. [crates/gcode/src/index/walker.rs:46-52]
- `DiscoveryOptions.default` (method) component `DiscoveryOptions.default [method]` (`6fe17d6e-d8cc-5013-a83b-c65f70ee0f52`) lines 47-51 [crates/gcode/src/index/walker.rs:47-51]
  - Signature: `fn default() -> Self {`
  - Purpose: The `default()` method implements the Default trait by returning a new instance of Self with the `respect_gitignore` field set to `true`. [crates/gcode/src/index/walker.rs:47-51]
- `discover_files` (function) component `discover_files [function]` (`833b0edd-08fc-52b1-9aae-10e6e604d6f4`) lines 56-61 [crates/gcode/src/index/walker.rs:56-61]
  - Signature: `pub fn discover_files<S: AsRef<str>>(`
  - Purpose: This function discovers files under a specified root directory with pattern-based exclusions, returning a tuple of PathBuf vectors via default discovery options. [crates/gcode/src/index/walker.rs:56-61]
- `discover_files_with_options` (function) component `discover_files_with_options [function]` (`45d67eac-bdd7-5bad-8387-4608ca1ab802`) lines 63-108 [crates/gcode/src/index/walker.rs:63-108]
  - Signature: `pub fn discover_files_with_options<S: AsRef<str>>(`
  - Purpose: Recursively discovers and classifies files from a root directory into two vectors (candidates and content_only) while applying gitignore rules, file size constraints, exclusion patterns, and hidden file allowlists. [crates/gcode/src/index/walker.rs:63-108]
- `classify_file` (function) component `classify_file [function]` (`8b586fbb-de6e-5c8c-8d40-6bef1f774618`) lines 111-135 [crates/gcode/src/index/walker.rs:111-135]
  - Signature: `pub fn classify_file(`
  - Purpose: Classifies safe text files into AST-parseable source code (if language-detected) or content-only variants, while filtering out generated and excluded files. [crates/gcode/src/index/walker.rs:111-135]
- `classify_explicit_file_with_options` (function) component `classify_explicit_file_with_options [function]` (`05678993-c7b0-5ad7-9576-cef7df8433a7`) lines 139-149 [crates/gcode/src/index/walker.rs:139-149]
  - Signature: `pub fn classify_explicit_file_with_options(`
  - Purpose: Classifies a file after optionally validating its visibility against gitignore rules when the `respect_gitignore` option is enabled. [crates/gcode/src/index/walker.rs:139-149]
- `is_content_indexable` (function) component `is_content_indexable [function]` (`7acd22ea-c903-5c6a-b4dc-bbe6b33ccb86`) lines 152-161 [crates/gcode/src/index/walker.rs:152-161]
  - Signature: `pub fn is_content_indexable(`
  - Purpose: Returns true if the file at the given path is classified as `ContentOnly`, indicating it is eligible for content indexing after accounting for the root directory and exclusion patterns. [crates/gcode/src/index/walker.rs:152-161]
- `content_language` (function) component `content_language [function]` (`6e62c8bd-cd0d-5992-92d0-ee332c792248`) lines 164-176 [crates/gcode/src/index/walker.rs:164-176]
  - Signature: `pub fn content_language(path: &Path) -> String {`
  - Purpose: Maps file extensions to normalized language identifiers, with special handling for Markdown and YAML variants, defaulting to 'text' for extensionless files. [crates/gcode/src/index/walker.rs:164-176]
- `push_classified_file` (function) component `push_classified_file [function]` (`cebab3bb-c7e4-56c0-9ed2-38288be37978`) lines 178-196 [crates/gcode/src/index/walker.rs:178-196]
  - Signature: `fn push_classified_file(`
  - Purpose: Deduplicates and classifies a canonicalized file path, routing it to either an AST-candidates or content-only vector based on its classification result. [crates/gcode/src/index/walker.rs:178-196]
- `explicit_path_visible` (function) component `explicit_path_visible [function]` (`8eb440e8-dd33-5696-9d86-814e991fa556`) lines 198-214 [crates/gcode/src/index/walker.rs:198-214]
  - Signature: `fn explicit_path_visible(root: &Path, path: &Path, options: DiscoveryOptions) -> bool {`
  - Purpose: Determines whether a path is visible by checking that it is not hidden (or is allowlisted) and exists as a file discoverable in a shallow walk of its parent directory respecting gitignore rules. [crates/gcode/src/index/walker.rs:198-214]
- `same_existing_path` (function) component `same_existing_path [function]` (`4055b0af-e2e4-5b87-aef3-84fbc4e951ae`) lines 216-220 [crates/gcode/src/index/walker.rs:216-220]
  - Signature: `fn same_existing_path(left: &Path, right: &Path) -> bool {`
  - Purpose: Determines if two paths refer to the same location by comparing their canonicalized forms, with a fallback to raw path comparison if canonicalization fails. [crates/gcode/src/index/walker.rs:216-220]
- `HiddenPathAllowlist` (class) component `HiddenPathAllowlist [class]` (`1c4278dd-826f-5993-be69-e6bdf3e40264`) lines 223-225 [crates/gcode/src/index/walker.rs:223-225]
  - Signature: `struct HiddenPathAllowlist {`
  - Purpose: `HiddenPathAllowlist` is a struct that encapsulates a vector of string patterns for matching and allowlisting hidden file paths. [crates/gcode/src/index/walker.rs:223-225]
- `HiddenPathAllowlist` (class) component `HiddenPathAllowlist [class]` (`cbe63296-4596-50c8-9c39-aa2efe4be9f5`) lines 227-274 [crates/gcode/src/index/walker.rs:227-274]
  - Signature: `impl HiddenPathAllowlist {`
  - Purpose: A glob pattern allowlist that discovers and matches hidden files by combining default and project-specific patterns relative to a project root. [crates/gcode/src/index/walker.rs:227-274]
- `HiddenPathAllowlist.load` (method) component `HiddenPathAllowlist.load [method]` (`daa2cd55-0874-5ff8-9158-53c5914c7988`) lines 228-235 [crates/gcode/src/index/walker.rs:228-235]
  - Signature: `fn load(root: &Path) -> Self {`
  - Purpose: Constructs an instance by merging default hidden allowlist patterns with project-specific patterns read from the filesystem at the given root path. [crates/gcode/src/index/walker.rs:228-235]
- `HiddenPathAllowlist.from_patterns` (method) component `HiddenPathAllowlist.from_patterns [method]` (`ab8d47e5-b813-5b0b-be52-a503d31cd91b`) lines 237-245 [crates/gcode/src/index/walker.rs:237-245]
  - Signature: `fn from_patterns(patterns: Vec<String>) -> Self {`
  - Purpose: Constructs `Self` from patterns by normalizing whitespace and path separators, filtering against an allowlist pattern validator, and expanding zero-depth globstar patterns. [crates/gcode/src/index/walker.rs:237-245]
- `HiddenPathAllowlist.discover` (method) component `HiddenPathAllowlist.discover [method]` (`7823b7f5-a678-5230-8fa3-6b29b6bc795c`) lines 247-263 [crates/gcode/src/index/walker.rs:247-263]
  - Signature: `fn discover(&self, root: &Path) -> Vec<PathBuf> {`
  - Purpose: Discovers and returns a vector of hidden file paths matching the configured glob patterns under a specified root directory. [crates/gcode/src/index/walker.rs:247-263]
- `HiddenPathAllowlist.matches` (method) component `HiddenPathAllowlist.matches [method]` (`bdabd5a2-7d9b-5df5-af51-90257e7b6b5c`) lines 265-273 [crates/gcode/src/index/walker.rs:265-273]
  - Signature: `fn matches(&self, root: &Path, path: &Path) -> bool {`
  - Purpose: Tests whether a path matches any glob pattern in the collection by comparing against the relative path (with normalized forward slashes). [crates/gcode/src/index/walker.rs:265-273]
- `read_project_hidden_allowlist` (function) component `read_project_hidden_allowlist [function]` (`c8f902ab-d83d-5516-ad7f-7503824778d0`) lines 276-290 [crates/gcode/src/index/walker.rs:276-290]
  - Signature: `fn read_project_hidden_allowlist(root: &Path) -> Vec<String> {`
  - Purpose: Parses the gcode configuration file from a project root directory and returns the `index.hidden_allowlist` JSON array as a Vec<String>, defaulting to an empty vector on I/O or parse errors. [crates/gcode/src/index/walker.rs:276-290]
- `is_valid_allowlist_pattern` (function) component `is_valid_allowlist_pattern [function]` (`6ef5a3db-ac42-5128-906c-c525ff89b584`) lines 292-304 [crates/gcode/src/index/walker.rs:292-304]
  - Signature: `fn is_valid_allowlist_pattern(pattern: &str) -> bool {`
  - Purpose: Validates that a pattern is a non-empty relative path without parent directory traversal (`..`), root, or absolute path components. [crates/gcode/src/index/walker.rs:292-304]
- `expand_zero_depth_globstar` (function) component `expand_zero_depth_globstar [function]` (`eac99db7-9bf2-5834-8a6b-a3463a4fb782`) lines 306-312 [crates/gcode/src/index/walker.rs:306-312]
  - Signature: `fn expand_zero_depth_globstar(pattern: &str) -> Vec<String> {`
  - Purpose: Expands a glob pattern containing the globstar operator `/**/` into two variants: the original pattern and a simplified form with `/**/` collapsed to `/`, enabling zero-depth directory matches. [crates/gcode/src/index/walker.rs:306-312]
- `absolute_glob_pattern` (function) component `absolute_glob_pattern [function]` (`535beedd-f8d2-5d93-ae7b-5c6d62be73e4`) lines 314-317 [crates/gcode/src/index/walker.rs:314-317]
  - Signature: `fn absolute_glob_pattern(root: &Path, pattern: &str) -> Option<String> {`
  - Purpose: Constructs an absolute glob pattern by concatenating an escaped root path with a glob pattern, returning `None` if the root path cannot be converted to UTF-8. [crates/gcode/src/index/walker.rs:314-317]
- `is_hidden_path` (function) component `is_hidden_path [function]` (`9231f3a0-0ba7-5ae2-9390-cf93f660779f`) lines 319-327 [crates/gcode/src/index/walker.rs:319-327]
  - Signature: `fn is_hidden_path(root: &Path, path: &Path) -> bool {`
  - Purpose: Returns true if the path contains any hidden components by checking whether any path segment starts with '.' while excluding the current ('.') and parent ('..') directory references. [crates/gcode/src/index/walker.rs:319-327]
- `is_hidden_metadata_content_only` (function) component `is_hidden_metadata_content_only [function]` (`b64ecf51-c842-5048-858e-76a93ca600b6`) lines 329-359 [crates/gcode/src/index/walker.rs:329-359]
  - Signature: `fn is_hidden_metadata_content_only(root: &Path, path: &Path) -> bool {`
  - Purpose: Determines whether a file is hidden metadata content by checking if it's a markdown file within `.gobby/plans/` or `.gobby/wiki/` directories, or a YAML file within `.github/workflows/`. [crates/gcode/src/index/walker.rs:329-359]
- `is_generated_wiki_metadata` (function) component `is_generated_wiki_metadata [function]` (`53b36550-60a4-5c78-9b79-2f200c16c5d6`) lines 361-386 [crates/gcode/src/index/walker.rs:361-386]
  - Signature: `fn is_generated_wiki_metadata(root: &Path, path: &Path) -> bool {`
  - Purpose: Determines whether a path represents generated wiki metadata by checking if it resides in the `.gobby/wiki/_meta/` directory or is a `.json.lock` file within `.gobby/wiki/`. [crates/gcode/src/index/walker.rs:361-386]
- `path_has_extension` (function) component `path_has_extension [function]` (`1d5d3b0e-0f25-5d72-94a9-15f87db850a0`) lines 388-396 [crates/gcode/src/index/walker.rs:388-396]
  - Signature: `fn path_has_extension(path: &Path, extensions: &[&str]) -> bool {`
  - Purpose: Returns whether a file path's case-insensitive extension is present in the provided slice of valid extensions, defaulting to false if the path lacks an extension or its extension cannot be decoded as valid UTF-8. [crates/gcode/src/index/walker.rs:388-396]
- `is_safe_text_file` (function) component `is_safe_text_file [function]` (`d92f9ce4-5f41-596a-9b1c-19c4b9d13fdc`) lines 398-423 [crates/gcode/src/index/walker.rs:398-423]
  - Signature: `fn is_safe_text_file(root: &Path, path: &Path, exclude_patterns: &[impl AsRef<str>]) -> bool {`
  - Purpose: Returns true if a file is a safe, non-binary text file that passes path validation, symlink security checks, size constraints (non-zero and ≤ MAX_FILE_SIZE), exclusion pattern matching, and secret extension filtering. [crates/gcode/src/index/walker.rs:398-423]
- `is_generated_js_bundle` (function) component `is_generated_js_bundle [function]` (`72540ac2-b7f7-5282-8e35-c7965ecc874a`) lines 425-445 [crates/gcode/src/index/walker.rs:425-445]
  - Signature: `fn is_generated_js_bundle(path: &Path) -> bool {`
  - Purpose: Detects whether a file path is a generated JavaScript bundle by checking for explicit generated markers or inferring minification characteristics from file size and content patterns. [crates/gcode/src/index/walker.rs:425-445]
- `read_file_prefix` (function) component `read_file_prefix [function]` (`d58fce29-aef1-57c9-ba70-30352c59c60e`) lines 447-452 [crates/gcode/src/index/walker.rs:447-452]
  - Signature: `fn read_file_prefix(path: &Path, max_bytes: u64) -> std::io::Result<Vec<u8>> {`
  - Purpose: Reads at most `max_bytes` from the beginning of a file into a `Vec<u8>`, returning the byte vector or an IO error. [crates/gcode/src/index/walker.rs:447-452]
- `is_js_family_file` (function) component `is_js_family_file [function]` (`53a45d19-c957-5ba2-ad91-fc365f6ce4eb`) lines 454-464 [crates/gcode/src/index/walker.rs:454-464]
  - Signature: `fn is_js_family_file(path: &Path) -> bool {`
  - Purpose: Checks whether a file path's extension matches a JavaScript-family format (js, jsx, cjs, or mjs) using case-insensitive comparison. [crates/gcode/src/index/walker.rs:454-464]
- `contains_generated_js_marker` (function) component `contains_generated_js_marker [function]` (`09628716-17fd-51e0-a2b0-2e44a8d0ce48`) lines 466-472 [crates/gcode/src/index/walker.rs:466-472]
  - Signature: `fn contains_generated_js_marker(bytes: &[u8]) -> bool {`
  - Purpose: This function returns true if any case-insensitive match of predefined generated JavaScript markers is found within the first N bytes of the input byte slice. [crates/gcode/src/index/walker.rs:466-472]
- `looks_minified_js_bundle` (function) component `looks_minified_js_bundle [function]` (`d2f5d5a9-efe0-5450-9b55-d5aa35666b5e`) lines 474-499 [crates/gcode/src/index/walker.rs:474-499]
  - Signature: `fn looks_minified_js_bundle(bytes: &[u8]) -> bool {`
  - Purpose: Detects minified JavaScript bundles by checking minimum size and verifying either the presence of abnormally long lines or high average line length relative to total line count. [crates/gcode/src/index/walker.rs:474-499]
- `write_file` (function) component `write_file [function]` (`9ae7a20b-739c-5e21-bb65-6196ca850285`) lines 505-511 [crates/gcode/src/index/walker.rs:505-511]
  - Signature: `fn write_file(root: &Path, rel: &str, contents: &[u8]) {`
  - Purpose: Writes byte contents to a file at a specified root-relative path, creating all missing parent directories if necessary. [crates/gcode/src/index/walker.rs:505-511]
- `rels` (function) component `rels [function]` (`6ddea6f7-14d1-541d-b587-6937a3fb5f4c`) lines 513-525 [crates/gcode/src/index/walker.rs:513-525]
  - Signature: `fn rels(root: &Path, paths: Vec<PathBuf>) -> Vec<String> {`
  - Purpose: Converts absolute paths to relative path strings by stripping a common root prefix, returning them sorted. [crates/gcode/src/index/walker.rs:513-525]
- `discovers_ast_and_content_only_text_files` (function) component `discovers_ast_and_content_only_text_files [function]` (`5c1493f7-2905-5574-aace-24ae8e842cc5`) lines 528-567 [crates/gcode/src/index/walker.rs:528-567]
  - Signature: `fn discovers_ast_and_content_only_text_files() {`
  - Purpose: Tests that `discover_files` correctly partitions text files into AST-parseable source code and content-only text files while filtering out binary files, secret-pattern-matched files, and excluded directories. [crates/gcode/src/index/walker.rs:528-567]
- `discover_files_respects_gitignore_by_default_and_option` (function) component `discover_files_respects_gitignore_by_default_and_option [function]` (`e50b8164-7734-5be2-8dd1-10ccd719fe27`) lines 570-591 [crates/gcode/src/index/walker.rs:570-591]
  - Signature: `fn discover_files_respects_gitignore_by_default_and_option() {`
  - Purpose: This test verifies that `discover_files` respects `.gitignore` exclusions by default and that the `respect_gitignore` option controls whether ignored files are included in file discovery results. [crates/gcode/src/index/walker.rs:570-591]
- `classifies_extensionless_text_as_content_only` (function) component `classifies_extensionless_text_as_content_only [function]` (`acbefad2-21d2-5df7-a11d-593551ff9cab`) lines 594-605 [crates/gcode/src/index/walker.rs:594-605]
  - Signature: `fn classifies_extensionless_text_as_content_only() {`
  - Purpose: This test verifies that the `classify_file` function categorizes an extensionless Makefile as `FileClassification::ContentOnly` with a detected content language of `"text"`. [crates/gcode/src/index/walker.rs:594-605]
- `classifies_markdown_content_language_as_markdown` (function) component `classifies_markdown_content_language_as_markdown [function]` (`f55c853d-09c5-5136-b465-59f91cab8742`) lines 608-618 [crates/gcode/src/index/walker.rs:608-618]
  - Signature: `fn classifies_markdown_content_language_as_markdown() {`
  - Purpose: This unit test verifies that the `content_language()` function correctly classifies files with `.md` and `.markdown` extensions as the `"markdown"` language type. [crates/gcode/src/index/walker.rs:608-618]
- `classifies_yaml_content_language_as_yaml` (function) component `classifies_yaml_content_language_as_yaml [function]` (`0970873c-d800-5259-8bba-0f509d605add`) lines 621-630 [crates/gcode/src/index/walker.rs:621-630]
  - Signature: `fn classifies_yaml_content_language_as_yaml() {`
  - Purpose: This test function verifies that the `content_language()` function correctly classifies files with `.yml` and `.yaml` extensions as the "yaml" language. [crates/gcode/src/index/walker.rs:621-630]
- `classifies_mjs_as_ast_and_markdown_as_content_only` (function) component `classifies_mjs_as_ast_and_markdown_as_content_only [function]` (`8285f7a0-80ef-5633-88b2-f00ff985a034`) lines 633-653 [crates/gcode/src/index/walker.rs:633-653]
  - Signature: `fn classifies_mjs_as_ast_and_markdown_as_content_only() {`
  - Purpose: This test verifies that the file classification function correctly categorizes ES module files (`.mjs`) as `Ast` and markdown files (`.md`, `.markdown`) as `ContentOnly`. [crates/gcode/src/index/walker.rs:633-653]
- `classifies_github_workflow_yaml_as_content_only` (function) component `classifies_github_workflow_yaml_as_content_only [function]` (`49cf2e35-5f19-5679-bac3-7ee293f8617e`) lines 656-675 [crates/gcode/src/index/walker.rs:656-675]
  - Signature: `fn classifies_github_workflow_yaml_as_content_only() {`
  - Purpose: This unit test verifies that the `classify_file` function correctly identifies GitHub Actions workflow YAML files in `.github/workflows/` as `FileClassification::ContentOnly`. [crates/gcode/src/index/walker.rs:656-675]
- `discovers_default_hidden_metadata_allowlist` (function) component `discovers_default_hidden_metadata_allowlist [function]` (`e7ca9103-669e-5317-a024-14e31a1960a3`) lines 678-699 [crates/gcode/src/index/walker.rs:678-699]
  - Signature: `fn discovers_default_hidden_metadata_allowlist() {`
  - Purpose: This test verifies that `discover_files()` with an empty allowlist segregates non-hidden source files into the AST result while relegating hidden dotfile directories (.gobby, .github) to the content_only result. [crates/gcode/src/index/walker.rs:678-699]
- `skips_non_allowlisted_hidden_metadata_by_default` (function) component `skips_non_allowlisted_hidden_metadata_by_default [function]` (`bc41ec85-b650-5e65-a1f4-4f37f0590c0e`) lines 702-717 [crates/gcode/src/index/walker.rs:702-717]
  - Signature: `fn skips_non_allowlisted_hidden_metadata_by_default() {`
  - Purpose: This test verifies that `discover_files` excludes non-allowlisted hidden metadata files by default, retaining only explicitly allowlisted content directories (e.g., `.gobby/wiki/`). [crates/gcode/src/index/walker.rs:702-717]
- `discovers_wiki_markdown_and_skips_generated_wiki_metadata` (function) component `discovers_wiki_markdown_and_skips_generated_wiki_metadata [function]` (`95cdd1cc-310e-5db4-a6ba-5e65e2d5d747`) lines 720-753 [crates/gcode/src/index/walker.rs:720-753]
  - Signature: `fn discovers_wiki_markdown_and_skips_generated_wiki_metadata() {`
  - Purpose: This test verifies that `discover_files()` correctly identifies wiki markdown files in `.gobby/wiki/` while filtering out generated metadata files in `_meta/` subdirectories and `.lock` files. [crates/gcode/src/index/walker.rs:720-753]
- `discovers_project_hidden_allowlist_from_gcode_json` (function) component `discovers_project_hidden_allowlist_from_gcode_json [function]` (`46aba99c-a60f-5f7b-8b9b-fb290230ba32`) lines 756-778 [crates/gcode/src/index/walker.rs:756-778]
  - Signature: `fn discovers_project_hidden_allowlist_from_gcode_json() {`
  - Purpose: This test verifies that `discover_files()` correctly parses and applies a glob pattern-based `hidden_allowlist` from `.gobby/gcode.json` to filter discovered files, returning only matches in the content-only result set while leaving the AST result set empty. [crates/gcode/src/index/walker.rs:756-778]
- `excludes_win_over_allowlisted_hidden_paths` (function) component `excludes_win_over_allowlisted_hidden_paths [function]` (`94e2a24b-49a0-5ca8-b386-c9e94644d1ed`) lines 781-792 [crates/gcode/src/index/walker.rs:781-792]
  - Signature: `fn excludes_win_over_allowlisted_hidden_paths() {`
  - Purpose: Verifies that explicit exclusion patterns prevent file discovery in hidden directories, taking precedence over any allowlist behavior. [crates/gcode/src/index/walker.rs:781-792]
- `skips_js_family_files_with_generated_markers` (function) component `skips_js_family_files_with_generated_markers [function]` (`4e6c419f-ced2-5e69-832f-60210fbaa4a9`) lines 795-813 [crates/gcode/src/index/walker.rs:795-813]
  - Signature: `fn skips_js_family_files_with_generated_markers() {`
  - Purpose: This test verifies that `classify_file()` returns `None` for JavaScript-family files (`.mjs`, `.js`, `.jsx`, `.cjs`) containing common generated-code marker comments. [crates/gcode/src/index/walker.rs:795-813]
- `keeps_ordinary_mjs_source_ast_indexable` (function) component `keeps_ordinary_mjs_source_ast_indexable [function]` (`0be0e413-4468-54b3-99d2-a36b61ec6467`) lines 816-830 [crates/gcode/src/index/walker.rs:816-830]
  - Signature: `fn keeps_ordinary_mjs_source_ast_indexable() {`
  - Purpose: This test verifies that `classify_file()` returns `FileClassification::Ast` for an ordinary .mjs ES module source file when no exclusion rules are applied. [crates/gcode/src/index/walker.rs:816-830]
- `skips_large_minified_js_bundles` (function) component `skips_large_minified_js_bundles [function]` (`0edaf40d-be4f-52be-a7df-83af9bc3009d`) lines 833-846 [crates/gcode/src/index/walker.rs:833-846]
  - Signature: `fn skips_large_minified_js_bundles() {`
  - Purpose: Asserts that `classify_file` returns `None` when processing a JavaScript bundle file whose minified content exceeds `MINIFIED_JS_MIN_BYTES`, verifying the exclusion of large minified JS bundles. [crates/gcode/src/index/walker.rs:833-846]
- `skips_single_line_minified_js_bundle_with_newline` (function) component `skips_single_line_minified_js_bundle_with_newline [function]` (`54e7273d-94c5-50cd-a15f-4a4824d1d887`) lines 849-862 [crates/gcode/src/index/walker.rs:849-862]
  - Signature: `fn skips_single_line_minified_js_bundle_with_newline() {`
  - Purpose: Verifies that `classify_file()` returns `None` when classifying a single-line minified JavaScript bundle with a trailing newline. [crates/gcode/src/index/walker.rs:849-862]
- `skips_single_line_minified_js_bundle_without_newline` (function) component `skips_single_line_minified_js_bundle_without_newline [function]` (`bcd6f964-e4bb-5365-b4da-03cc9a7a0593`) lines 865-878 [crates/gcode/src/index/walker.rs:865-878]
  - Signature: `fn skips_single_line_minified_js_bundle_without_newline() {`
  - Purpose: This test function verifies that a single-line minified JavaScript IIFE bundle without newlines is correctly classified as a skippable file (returns `None` from `classify_file`). [crates/gcode/src/index/walker.rs:865-878]
- `classifies_source_build_directory_as_ast_indexable` (function) component `classifies_source_build_directory_as_ast_indexable [function]` (`80ba2aad-af63-59c6-b191-8fe2d49ff2ad`) lines 881-895 [crates/gcode/src/index/walker.rs:881-895]
  - Signature: `fn classifies_source_build_directory_as_ast_indexable() {`
  - Purpose: This test verifies that `classify_file()` returns `FileClassification::Ast` for a Python source file located in src/gobby/build/workspaces.py, demonstrating that the "build" exclude pattern does not prevent AST classification of files within nested build subdirectories. [crates/gcode/src/index/walker.rs:881-895]
- `skips_root_build_directory` (function) component `skips_root_build_directory [function]` (`581a4300-81f3-5621-8f8e-57f43820b9fc`) lines 898-908 [crates/gcode/src/index/walker.rs:898-908]
  - Signature: `fn skips_root_build_directory() {`
  - Purpose: This test verifies that `classify_file()` returns `None` when classifying a file located in a directory specified within the excludes list. [crates/gcode/src/index/walker.rs:898-908]
- `walker_consumes_gobby_core_walker_settings` (function) component `walker_consumes_gobby_core_walker_settings [function]` (`05a6f71f-6a99-5879-a8f0-2d4ecb84dd33`) lines 911-918 [crates/gcode/src/index/walker.rs:911-918]
  - Signature: `fn walker_consumes_gobby_core_walker_settings() {`
  - Purpose: # Summary

This test function asserts that `walker.rs` contains references to `gobby_core::indexing::WalkerSettings` while explicitly excluding any direct instantiation of `WalkBuilder::new(root)`, enforcing proper architectural dependency compliance. [crates/gcode/src/index/walker.rs:911-918]

