---
title: crates/gwiki/src/synthesis.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis.rs
  ranges:
  - 14-18
  - 20-36
  - 21-27
  - 29-35
  - 39-43
  - 46-56
  - 59-63
  - 66-70
  - 73-76
  - 80-83
  - 86-89
  - 91-124
  - 126-192
  - 194-232
  - 239-253
  - 255-326
  - 328-356
  - 358-381
  - 383-398
  - 400-405
  - 407-413
  - 415-438
  - 440-454
  - 456-461
  - 463-485
  - 487-497
  - 499-522
  - 524-542
  - 544-558
  - 560-565
  - 567-585
  - 587-611
  - 613-647
  - 649-668
  - 670-680
  - 687-713
  - 716-738
  - 741-746
  - 749-762
  - 765-797
  - 800-828
  - 832-858
  - 861-871
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/synthesis.rs` exposes 43 indexed API symbols.
[crates/gwiki/src/synthesis.rs:14-18]
[crates/gwiki/src/synthesis.rs:20-36]
[crates/gwiki/src/synthesis.rs:21-27]
[crates/gwiki/src/synthesis.rs:29-35]
[crates/gwiki/src/synthesis.rs:39-43]

## API Symbols

- `ArticleKind` (type) component `ArticleKind [type]` (`b7b4f4cd-b215-5cdb-9a1c-e5d7441bfcb1`) lines 14-18 [crates/gwiki/src/synthesis.rs:14-18]
  - Signature: `pub enum ArticleKind {`
  - Purpose: Indexed type `ArticleKind` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:14-18]
- `ArticleKind` (class) component `ArticleKind [class]` (`35b1df1f-a810-5077-b250-12353b845102`) lines 20-36 [crates/gwiki/src/synthesis.rs:20-36]
  - Signature: `impl ArticleKind {`
  - Purpose: Indexed class `ArticleKind` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:20-36]
- `ArticleKind.directory` (method) component `ArticleKind.directory [method]` (`81f74d77-fa86-5b44-9c4e-8156e83ae789`) lines 21-27 [crates/gwiki/src/synthesis.rs:21-27]
  - Signature: `pub fn directory(self) -> &'static str {`
  - Purpose: Indexed method `ArticleKind.directory` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:21-27]
- `ArticleKind.source_kind` (method) component `ArticleKind.source_kind [method]` (`4854c1ec-b718-52cd-addf-c874e08d51d1`) lines 29-35 [crates/gwiki/src/synthesis.rs:29-35]
  - Signature: `pub fn source_kind(self) -> &'static str {`
  - Purpose: Indexed method `ArticleKind.source_kind` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:29-35]
- `SynthesisSource` (class) component `SynthesisSource [class]` (`6581ef90-f867-57f4-be48-cadc6f8c4cb9`) lines 39-43 [crates/gwiki/src/synthesis.rs:39-43]
  - Signature: `pub struct SynthesisSource {`
  - Purpose: Indexed class `SynthesisSource` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:39-43]
- `SynthesisInput` (class) component `SynthesisInput [class]` (`482acd2a-2ef2-5db1-b7a9-ec3ba5381d98`) lines 46-56 [crates/gwiki/src/synthesis.rs:46-56]
  - Signature: `pub struct SynthesisInput {`
  - Purpose: Indexed class `SynthesisInput` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:46-56]
- `SynthesisPrompt` (class) component `SynthesisPrompt [class]` (`7ccf298b-fa4b-5ef0-a02c-7ed3792553d0`) lines 59-63 [crates/gwiki/src/synthesis.rs:59-63]
  - Signature: `pub struct SynthesisPrompt {`
  - Purpose: Indexed class `SynthesisPrompt` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:59-63]
- `SynthesizedPage` (class) component `SynthesizedPage [class]` (`84aa1732-0e32-543a-854b-c607ccf941b6`) lines 66-70 [crates/gwiki/src/synthesis.rs:66-70]
  - Signature: `pub struct SynthesizedPage {`
  - Purpose: Indexed class `SynthesizedPage` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:66-70]
- `WritePolicy` (type) component `WritePolicy [type]` (`8a3b491a-6d54-576d-9ed8-4a9e6b4cb535`) lines 73-76 [crates/gwiki/src/synthesis.rs:73-76]
  - Signature: `pub enum WritePolicy {`
  - Purpose: Indexed type `WritePolicy` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:73-76]
- `PageWriteKind` (type) component `PageWriteKind [type]` (`fed40e2c-945f-510c-815d-bf8554293b5c`) lines 80-83 [crates/gwiki/src/synthesis.rs:80-83]
  - Signature: `pub enum PageWriteKind {`
  - Purpose: Indexed type `PageWriteKind` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:80-83]
- `PageWriteOutcome` (class) component `PageWriteOutcome [class]` (`4be61a36-f7a9-5408-a0e2-914b4a6091e0`) lines 86-89 [crates/gwiki/src/synthesis.rs:86-89]
  - Signature: `pub struct PageWriteOutcome {`
  - Purpose: Indexed class `PageWriteOutcome` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:86-89]
- `build_synthesis_prompt` (function) component `build_synthesis_prompt [function]` (`e7f1d613-10da-5d8f-b1b8-7b8138c4bebd`) lines 91-124 [crates/gwiki/src/synthesis.rs:91-124]
  - Signature: `pub fn build_synthesis_prompt(input: &SynthesisInput) -> SynthesisPrompt {`
  - Purpose: Indexed function `build_synthesis_prompt` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:91-124]
- `synthesize_article` (function) component `synthesize_article [function]` (`4954a624-f353-585b-9a42-cf8a31d7a5c9`) lines 126-192 [crates/gwiki/src/synthesis.rs:126-192]
  - Signature: `pub fn synthesize_article(`
  - Purpose: Indexed function `synthesize_article` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:126-192]
- `synthesize_source_pages` (function) component `synthesize_source_pages [function]` (`71b3b30d-d8cb-5d84-9632-9273109f1206`) lines 194-232 [crates/gwiki/src/synthesis.rs:194-232]
  - Signature: `pub fn synthesize_source_pages(`
  - Purpose: Indexed function `synthesize_source_pages` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:194-232]
- `ensure_page_write_allowed` (function) component `ensure_page_write_allowed [function]` (`047e61ab-c94e-5b46-9389-11ae677c9d77`) lines 239-253 [crates/gwiki/src/synthesis.rs:239-253]
  - Signature: `pub fn ensure_page_write_allowed(`
  - Purpose: Indexed function `ensure_page_write_allowed` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:239-253]
- `write_synthesized_page` (function) component `write_synthesized_page [function]` (`cfb5bd1c-78c7-5612-aaef-4576e01c2a89`) lines 255-326 [crates/gwiki/src/synthesis.rs:255-326]
  - Signature: `pub fn write_synthesized_page(`
  - Purpose: Indexed function `write_synthesized_page` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:255-326]
- `ensure_synthesized_path_inside_vault` (function) component `ensure_synthesized_path_inside_vault [function]` (`e37881b0-f242-54f7-b3ed-9ec2f2038e69`) lines 328-356 [crates/gwiki/src/synthesis.rs:328-356]
  - Signature: `pub fn ensure_synthesized_path_inside_vault(`
  - Purpose: Indexed function `ensure_synthesized_path_inside_vault` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:328-356]
- `canonicalize_existing_prefix` (function) component `canonicalize_existing_prefix [function]` (`9896196a-7c08-5375-9fa6-ddba63ba5074`) lines 358-381 [crates/gwiki/src/synthesis.rs:358-381]
  - Signature: `fn canonicalize_existing_prefix(path: &Path, action: &'static str) -> Result<PathBuf, WikiError> {`
  - Purpose: Indexed function `canonicalize_existing_prefix` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:358-381]
- `ensure_existing_parent_inside_vault` (function) component `ensure_existing_parent_inside_vault [function]` (`0f8bdebe-1275-5485-8f49-b2051459fc9f`) lines 383-398 [crates/gwiki/src/synthesis.rs:383-398]
  - Signature: `fn ensure_existing_parent_inside_vault(`
  - Purpose: Indexed function `ensure_existing_parent_inside_vault` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:383-398]
- `synthesized_path_outside_vault` (function) component `synthesized_path_outside_vault [function]` (`b31f8dc4-ecb6-5f5f-af35-a6e886c97581`) lines 400-405 [crates/gwiki/src/synthesis.rs:400-405]
  - Signature: `fn synthesized_path_outside_vault(field: &'static str) -> WikiError {`
  - Purpose: Indexed function `synthesized_path_outside_vault` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:400-405]
- `wiki_link` (function) component `wiki_link [function]` (`11839458-cbd7-5300-bfaf-9649522e1525`) lines 407-413 [crates/gwiki/src/synthesis.rs:407-413]
  - Signature: `pub fn wiki_link(vault_root: &Path, path: &Path, title: &str) -> String {`
  - Purpose: Indexed function `wiki_link` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:407-413]
- `slugify` (function) component `slugify [function]` (`5f40eb60-9abe-5cee-b26b-f8315d395b88`) lines 415-438 [crates/gwiki/src/synthesis.rs:415-438]
  - Signature: `pub fn slugify(title: &str) -> String {`
  - Purpose: Indexed function `slugify` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:415-438]
- `slugify_unique` (function) component `slugify_unique [function]` (`3d38bada-e2b6-549f-949d-592d4bdc4efe`) lines 440-454 [crates/gwiki/src/synthesis.rs:440-454]
  - Signature: `pub fn slugify_unique(title: &str, mut exists: impl FnMut(&str) -> bool) -> String {`
  - Purpose: Indexed function `slugify_unique` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:440-454]
- `relative_path` (function) component `relative_path [function]` (`2278c948-81d2-5d76-8c2f-4eddf5978af7`) lines 456-461 [crates/gwiki/src/synthesis.rs:456-461]
  - Signature: `pub fn relative_path(root: &Path, path: &Path) -> String {`
  - Purpose: Indexed function `relative_path` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:456-461]
- `source_page_paths` (function) component `source_page_paths [function]` (`a326099f-0797-5617-be7f-93628be2a42c`) lines 463-485 [crates/gwiki/src/synthesis.rs:463-485]
  - Signature: `fn source_page_paths(`
  - Purpose: Indexed function `source_page_paths` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:463-485]
- `source_links` (function) component `source_links [function]` (`6846cc09-83ff-5f48-9c4e-131d6823f004`) lines 487-497 [crates/gwiki/src/synthesis.rs:487-497]
  - Signature: `fn source_links(`
  - Purpose: Indexed function `source_links` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:487-497]
- `render_frontmatter` (function) component `render_frontmatter [function]` (`4872592d-7c0f-59a0-90cb-28affee5d868`) lines 499-522 [crates/gwiki/src/synthesis.rs:499-522]
  - Signature: `fn render_frontmatter(`
  - Purpose: Indexed function `render_frontmatter` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:499-522]
- `render_source_excerpts` (function) component `render_source_excerpts [function]` (`a11fc84b-28e1-53c0-bc31-3c8173313d8a`) lines 524-542 [crates/gwiki/src/synthesis.rs:524-542]
  - Signature: `fn render_source_excerpts(markdown: &mut String, sources: &[SynthesisSource]) {`
  - Purpose: Indexed function `render_source_excerpts` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:524-542]
- `render_list_section` (function) component `render_list_section [function]` (`296f6f28-6772-5e0c-b7e2-708f37249021`) lines 544-558 [crates/gwiki/src/synthesis.rs:544-558]
  - Signature: `fn render_list_section(markdown: &mut String, title: &str, values: &[String]) {`
  - Purpose: Indexed function `render_list_section` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:544-558]
- `trim_markdown_extension` (function) component `trim_markdown_extension [function]` (`435b41ab-37b7-5390-936a-445f04e7ef0e`) lines 560-565 [crates/gwiki/src/synthesis.rs:560-565]
  - Signature: `fn trim_markdown_extension(path: &str) -> String {`
  - Purpose: Indexed function `trim_markdown_extension` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:560-565]
- `yaml_scalar` (function) component `yaml_scalar [function]` (`e31aebd5-4817-5ec9-b54f-08cff95ade1f`) lines 567-585 [crates/gwiki/src/synthesis.rs:567-585]
  - Signature: `fn yaml_scalar(value: &str) -> String {`
  - Purpose: Indexed function `yaml_scalar` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:567-585]
- `write_created_synthesized_page` (function) component `write_created_synthesized_page [function]` (`0a6216d7-14bb-502a-a95d-0ee6361220e4`) lines 587-611 [crates/gwiki/src/synthesis.rs:587-611]
  - Signature: `fn write_created_synthesized_page(`
  - Purpose: Indexed function `write_created_synthesized_page` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:587-611]
- `write_synthesized_page_atomically` (function) component `write_synthesized_page_atomically [function]` (`bf195dd0-be33-5cf4-838d-7114dac35640`) lines 613-647 [crates/gwiki/src/synthesis.rs:613-647]
  - Signature: `fn write_synthesized_page_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Indexed function `write_synthesized_page_atomically` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:613-647]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`3f38d5f0-f49c-53ad-8f11-ef0f66b758a7`) lines 649-668 [crates/gwiki/src/synthesis.rs:649-668]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `sync_parent_dir` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:649-668]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`e5344c2e-2332-58f6-b51e-bcec55da749b`) lines 670-680 [crates/gwiki/src/synthesis.rs:670-680]
  - Signature: `fn temp_sibling_path(path: &Path) -> PathBuf {`
  - Purpose: Indexed function `temp_sibling_path` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:670-680]
- `existing_page_requires_merge_intent` (function) component `existing_page_requires_merge_intent [function]` (`17b3cc2e-93fc-503f-bbc5-2cc7aed6b553`) lines 687-713 [crates/gwiki/src/synthesis.rs:687-713]
  - Signature: `fn existing_page_requires_merge_intent() {`
  - Purpose: Indexed function `existing_page_requires_merge_intent` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:687-713]
- `synthesized_page_write_classifies_create_and_overwrite_atomically` (function) component `synthesized_page_write_classifies_create_and_overwrite_atomically [function]` (`65dee847-39d0-5f25-9602-a48078270d75`) lines 716-738 [crates/gwiki/src/synthesis.rs:716-738]
  - Signature: `fn synthesized_page_write_classifies_create_and_overwrite_atomically() {`
  - Purpose: Indexed function `synthesized_page_write_classifies_create_and_overwrite_atomically` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:716-738]
- `slugify_unique_falls_back_after_bounded_suffixes` (function) component `slugify_unique_falls_back_after_bounded_suffixes [function]` (`7fbd636d-6204-5196-9059-df6dbf429cfd`) lines 741-746 [crates/gwiki/src/synthesis.rs:741-746]
  - Signature: `fn slugify_unique_falls_back_after_bounded_suffixes() {`
  - Purpose: Indexed function `slugify_unique_falls_back_after_bounded_suffixes` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:741-746]
- `source_page_paths_reserve_article_path` (function) component `source_page_paths_reserve_article_path [function]` (`f843f86e-cc93-502a-a5ea-88c7550f8da8`) lines 749-762 [crates/gwiki/src/synthesis.rs:749-762]
  - Signature: `fn source_page_paths_reserve_article_path() {`
  - Purpose: Indexed function `source_page_paths_reserve_article_path` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:749-762]
- `synthesized_article_rejects_escaping_target_path` (function) component `synthesized_article_rejects_escaping_target_path [function]` (`ed2cd4fe-cc12-5ce3-b3be-404622239c4c`) lines 765-797 [crates/gwiki/src/synthesis.rs:765-797]
  - Signature: `fn synthesized_article_rejects_escaping_target_path() {`
  - Purpose: Indexed function `synthesized_article_rejects_escaping_target_path` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:765-797]
- `synthesized_writer_rejects_escaping_page_path_before_write` (function) component `synthesized_writer_rejects_escaping_page_path_before_write [function]` (`9e625330-d71e-5dab-89fa-69f2e1dfc56e`) lines 800-828 [crates/gwiki/src/synthesis.rs:800-828]
  - Signature: `fn synthesized_writer_rejects_escaping_page_path_before_write() {`
  - Purpose: Indexed function `synthesized_writer_rejects_escaping_page_path_before_write` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:800-828]
- `synthesized_writer_rejects_symlinked_parent_before_create_dir_all` (function) component `synthesized_writer_rejects_symlinked_parent_before_create_dir_all [function]` (`df97382e-582b-5510-8751-1ffb7e15a563`) lines 832-858 [crates/gwiki/src/synthesis.rs:832-858]
  - Signature: `fn synthesized_writer_rejects_symlinked_parent_before_create_dir_all() {`
  - Purpose: Indexed function `synthesized_writer_rejects_symlinked_parent_before_create_dir_all` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:832-858]
- `yaml_scalar_escapes_quoted_control_characters` (function) component `yaml_scalar_escapes_quoted_control_characters [function]` (`e451dc10-8995-5cf9-95b6-55de46b3b82c`) lines 861-871 [crates/gwiki/src/synthesis.rs:861-871]
  - Signature: `fn yaml_scalar_escapes_quoted_control_characters() {`
  - Purpose: Indexed function `yaml_scalar_escapes_quoted_control_characters` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:861-871]

