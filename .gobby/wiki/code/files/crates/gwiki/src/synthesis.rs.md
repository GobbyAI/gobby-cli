---
title: crates/gwiki/src/synthesis.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis.rs
  ranges:
  - 15-19
  - 21-37
  - 40-44
  - 47-56
  - 59-65
  - 68-74
  - 77-80
  - 84-87
  - 90-93
  - 95-182
  - 188-230
  - 232-272
  - 279-293
  - 295-366
  - 368-396
  - 398-421
  - 423-438
  - 440-445
  - 447-453
  - 455-478
  - 480-494
  - 496-501
  - 503-525
  - 527-537
  - 539-573
  - 575-593
  - 595-609
  - 611-616
  - 618-636
  - 638-662
  - 664-698
  - 700-719
  - 721-731
  - 738-765
  - 768-791
  - 794-799
  - 802-815
  - 818-854
  - 857-886
  - 890-917
  - 920-930
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the wiki synthesis pipeline for turning an explainer and accepted source material into compiled Markdown pages inside a vault. `ArticleKind` maps article types to their target directories and source-kind tags, while `SynthesisSource`, `SynthesisInput`, `SynthesisPrompt`, `SynthesizedPage`, `WritePolicy`, `PageWriteKind`, and `PageWriteOutcome` carry the data flowing through synthesis and writeback. The main entry points, `synthesize_article` and `ground_article_explainer`, build a grounded article from citations and accepted sources, generate companion source pages, and attach explainer/report metadata when available. Supporting helpers handle unique slug generation, vault-relative wiki links, frontmatter and excerpt rendering, YAML escaping, and strict path validation so synthesized pages stay inside the vault and are written atomically with create/overwrite behavior controlled by policy.
[crates/gwiki/src/synthesis.rs:15-19]
[crates/gwiki/src/synthesis.rs:21-37]
[crates/gwiki/src/synthesis.rs:22-28]
[crates/gwiki/src/synthesis.rs:30-36]
[crates/gwiki/src/synthesis.rs:40-44]

## API Symbols

- `ArticleKind` (type) component `ArticleKind [type]` (`19201efc-f03a-5593-8a20-25edc3910e5f`) lines 15-19 [crates/gwiki/src/synthesis.rs:15-19]
  - Signature: `pub enum ArticleKind {`
  - Purpose: Indexed type `ArticleKind` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:15-19]
- `ArticleKind` (class) component `ArticleKind [class]` (`a11d7589-14d2-595c-8072-2bbde3593e86`) lines 21-37 [crates/gwiki/src/synthesis.rs:21-37]
  - Signature: `impl ArticleKind {`
  - Purpose: This impl block provides methods that map 'ArticleKind' enum variants to their corresponding filesystem directory paths and source type identifiers via exhaustive pattern matching. [crates/gwiki/src/synthesis.rs:21-37]
- `ArticleKind.directory` (method) component `ArticleKind.directory [method]` (`73f5f698-fae1-5315-a7b9-5b0721f28420`) lines 22-28 [crates/gwiki/src/synthesis.rs:22-28]
  - Signature: `pub fn directory(self) -> &'static str {`
  - Purpose: # Summary This method maps an enum variant to its corresponding static directory path string by pattern matching. [crates/gwiki/src/synthesis.rs:22-28]
- `ArticleKind.source_kind` (method) component `ArticleKind.source_kind [method]` (`98e8ad4a-343a-5577-8662-7e821d736003`) lines 30-36 [crates/gwiki/src/synthesis.rs:30-36]
  - Signature: `pub fn source_kind(self) -> &'static str {`
  - Purpose: This method returns a static string identifier corresponding to each enum variant through pattern matching on 'self'. [crates/gwiki/src/synthesis.rs:30-36]
- `SynthesisSource` (class) component `SynthesisSource [class]` (`9a31ede1-3f03-567e-91b6-6b557bfc76c2`) lines 40-44 [crates/gwiki/src/synthesis.rs:40-44]
  - Signature: `pub struct SynthesisSource {`
  - Purpose: 'SynthesisSource' is a struct that encapsulates a titled source document with its file path and fragmented content represented as a vector of string chunks for synthesis processing. [crates/gwiki/src/synthesis.rs:40-44]
- `SynthesisInput` (class) component `SynthesisInput [class]` (`17a9a841-ab48-535c-94e2-a4ab0e25eaed`) lines 47-56 [crates/gwiki/src/synthesis.rs:47-56]
  - Signature: `pub struct SynthesisInput {`
  - Purpose: 'SynthesisInput' aggregates article synthesis parameters including topic definition, structural outline, output format specification, validated source references, citations, and analytical constraints (conflicts and evidence gaps). [crates/gwiki/src/synthesis.rs:47-56]
- `SynthesisPrompt` (class) component `SynthesisPrompt [class]` (`f672ee3b-c1d5-54ce-ad84-936272f8a510`) lines 59-65 [crates/gwiki/src/synthesis.rs:59-65]
  - Signature: `pub struct SynthesisPrompt {`
  - Purpose: 'SynthesisPrompt' is a struct that encapsulates system and user prompt strings alongside synthesis metadata including daemon availability, estimated token count, and the number of truncated sources. [crates/gwiki/src/synthesis.rs:59-65]
- `SynthesizedPage` (class) component `SynthesizedPage [class]` (`79bd60df-d583-50e6-823a-dc4c51748ade`) lines 68-74 [crates/gwiki/src/synthesis.rs:68-74]
  - Signature: `pub struct SynthesizedPage {`
  - Purpose: 'SynthesizedPage' is a struct that encapsulates a compiled page's metadata and content, comprising a filesystem path, title, markdown source, and an optional explainer report documenting the synthesis/compilation process. [crates/gwiki/src/synthesis.rs:68-74]
- `WritePolicy` (type) component `WritePolicy [type]` (`a7e8e5c9-b18d-541b-9b7e-f7f10b858b10`) lines 77-80 [crates/gwiki/src/synthesis.rs:77-80]
  - Signature: `pub enum WritePolicy {`
  - Purpose: Indexed type `WritePolicy` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:77-80]
- `PageWriteKind` (type) component `PageWriteKind [type]` (`5d58f29f-9ec1-5426-b2f7-af425204f876`) lines 84-87 [crates/gwiki/src/synthesis.rs:84-87]
  - Signature: `pub enum PageWriteKind {`
  - Purpose: Indexed type `PageWriteKind` in `crates/gwiki/src/synthesis.rs`. [crates/gwiki/src/synthesis.rs:84-87]
- `PageWriteOutcome` (class) component `PageWriteOutcome [class]` (`522b7da9-75ae-52e7-b78f-64de1e4c01dd`) lines 90-93 [crates/gwiki/src/synthesis.rs:90-93]
  - Signature: `pub struct PageWriteOutcome {`
  - Purpose: 'PageWriteOutcome' is a struct that encapsulates the result of a page write operation, containing the destination filesystem path and the kind of write that was performed. [crates/gwiki/src/synthesis.rs:90-93]
- `synthesize_article` (function) component `synthesize_article [function]` (`70b1b8fa-9dfc-5b46-8a13-4864deb734c9`) lines 95-182 [crates/gwiki/src/synthesis.rs:95-182]
  - Signature: `pub fn synthesize_article(`
  - Purpose: Synthesizes a markdown article by grounding an explainer against accepted sources and rendering it with frontmatter metadata and source citations to a validated vault location. [crates/gwiki/src/synthesis.rs:95-182]
- `ground_article_explainer` (function) component `ground_article_explainer [function]` (`a5dfc249-b85d-50ad-9d76-e7e17cc089ea`) lines 188-230 [crates/gwiki/src/synthesis.rs:188-230]
  - Signature: `fn ground_article_explainer(`
  - Purpose: 'ground_article_explainer' converts a generated explainer into a citation-grounded body and report by matching accepted sources to citation targets, or returns 'None' with a failure/skipped 'ExplainerReport' when generation did not succeed. [crates/gwiki/src/synthesis.rs:188-230]
- `synthesize_source_pages` (function) component `synthesize_source_pages [function]` (`b2787b84-0357-5d47-ae4d-b042e4a936f2`) lines 232-272 [crates/gwiki/src/synthesis.rs:232-272]
  - Signature: `pub fn synthesize_source_pages(`
  - Purpose: Builds a 'Vec<SynthesizedPage>' for each accepted source by validating the synthesized output path, generating source-markdown with frontmatter, title, relative source path, extracts, and a “Used by” link back to the article, and returns it as 'Ok(...)'. [crates/gwiki/src/synthesis.rs:232-272]
- `ensure_page_write_allowed` (function) component `ensure_page_write_allowed [function]` (`b1e5441c-7815-5af1-b3b2-d47abad81902`) lines 279-293 [crates/gwiki/src/synthesis.rs:279-293]
  - Signature: `pub fn ensure_page_write_allowed(`
  - Purpose: Returns 'Ok(())' unless the target page already exists and the policy is 'WritePolicy::RequireMergeIntent', in which case it rejects the write with 'WikiError::InvalidInput' on 'write_intent' indicating the existing page must be handled via merge/diff before overwrite. [crates/gwiki/src/synthesis.rs:279-293]
- `write_synthesized_page` (function) component `write_synthesized_page [function]` (`671b2930-7ccd-5cfc-9ad9-35ecd9d05d67`) lines 295-366 [crates/gwiki/src/synthesis.rs:295-366]
  - Signature: `pub fn write_synthesized_page(`
  - Purpose: Writes a synthesized wiki page to a vault path after enforcing vault-bound path safety and parent-directory constraints, then applies policy-dependent create/overwrite semantics and returns a 'PageWriteOutcome' or structured 'WikiError'. [crates/gwiki/src/synthesis.rs:295-366]
- `ensure_synthesized_path_inside_vault` (function) component `ensure_synthesized_path_inside_vault [function]` (`66672f5f-0307-5809-a7e8-1ee0a86573f2`) lines 368-396 [crates/gwiki/src/synthesis.rs:368-396]
  - Signature: `pub fn ensure_synthesized_path_inside_vault(`
  - Purpose: Resolves the vault root and candidate path, canonicalizes the existing prefix, and returns an error unless the resulting path is strictly contained within the vault root with no parent, root, or prefix components. [crates/gwiki/src/synthesis.rs:368-396]
- `canonicalize_existing_prefix` (function) component `canonicalize_existing_prefix [function]` (`1a72ed39-22f7-50c9-9143-511b254c2059`) lines 398-421 [crates/gwiki/src/synthesis.rs:398-421]
  - Signature: `fn canonicalize_existing_prefix(path: &Path, action: &'static str) -> Result<PathBuf, WikiError> {`
  - Purpose: Resolves 'path' by walking up to the nearest existing ancestor, canonicalizing that existing prefix, and then appending the missing suffix components back onto the resolved 'PathBuf', returning an 'Io'-wrapped 'WikiError' if canonicalization of the existing prefix fails. [crates/gwiki/src/synthesis.rs:398-421]
- `ensure_existing_parent_inside_vault` (function) component `ensure_existing_parent_inside_vault [function]` (`430d12c7-0bb9-5df9-930d-ebe6a0265d66`) lines 423-438 [crates/gwiki/src/synthesis.rs:423-438]
  - Signature: `fn ensure_existing_parent_inside_vault(`
  - Purpose: It canonicalizes the vault root and an existing parent path, then returns 'Ok(())' only if the parent path is inside the canonical vault root, otherwise it raises a synthesized-path-outside-vault error after mapping any vault-root resolution failure to 'WikiError::Io'. [crates/gwiki/src/synthesis.rs:423-438]
- `synthesized_path_outside_vault` (function) component `synthesized_path_outside_vault [function]` (`31369524-6b67-55af-addc-5dce8b8d3bd8`) lines 440-445 [crates/gwiki/src/synthesis.rs:440-445]
  - Signature: `fn synthesized_path_outside_vault(field: &'static str) -> WikiError {`
  - Purpose: Constructs a 'WikiError::InvalidInput' for the given field, indicating that a synthesized wiki page path must remain inside the vault. [crates/gwiki/src/synthesis.rs:440-445]
- `wiki_link` (function) component `wiki_link [function]` (`d2301d12-66b5-5b05-978e-1d65437afd9c`) lines 447-453 [crates/gwiki/src/synthesis.rs:447-453]
  - Signature: `pub fn wiki_link(vault_root: &Path, path: &Path, title: &str) -> String {`
  - Purpose: Constructs an Obsidian-style wiki link string by converting 'path' to a vault-relative path with any Markdown extension removed and formatting it as '[[relative_path|title]]'. [crates/gwiki/src/synthesis.rs:447-453]
- `slugify` (function) component `slugify [function]` (`021b8958-d6c8-50b4-9afd-0b4c3c03eec4`) lines 455-478 [crates/gwiki/src/synthesis.rs:455-478]
  - Signature: `pub fn slugify(title: &str) -> String {`
  - Purpose: Converts 'title' to a lowercase ASCII slug by keeping alphanumeric characters, collapsing any run of non-alphanumerics into single hyphens between segments, trimming trailing hyphens, and returning '"wiki-page"' if no slugable content remains. [crates/gwiki/src/synthesis.rs:455-478]
- `slugify_unique` (function) component `slugify_unique [function]` (`50c8937f-1ac5-5510-965b-6d4aa141c995`) lines 480-494 [crates/gwiki/src/synthesis.rs:480-494]
  - Signature: `pub fn slugify_unique(title: &str, mut exists: impl FnMut(&str) -> bool) -> String {`
  - Purpose: Returns a slugified version of 'title', appending '-2' through '-MAX_SLUG_TRIES' until 'exists' reports a free value, and if all candidates are taken, falls back to a slug plus a fresh UUID suffix. [crates/gwiki/src/synthesis.rs:480-494]
- `relative_path` (function) component `relative_path [function]` (`84552683-159a-52a9-a61c-7aca44b2b576`) lines 496-501 [crates/gwiki/src/synthesis.rs:496-501]
  - Signature: `pub fn relative_path(root: &Path, path: &Path) -> String {`
  - Purpose: Returns 'path' relative to 'root' when possible, otherwise the original path, and normalizes the result to a UTF-8 lossy string with backslashes replaced by forward slashes. [crates/gwiki/src/synthesis.rs:496-501]
- `source_page_paths` (function) component `source_page_paths [function]` (`15fa2277-0a1d-5b11-a194-7b92f031f7a6`) lines 503-525 [crates/gwiki/src/synthesis.rs:503-525]
  - Signature: `fn source_page_paths(`
  - Purpose: Builds unique markdown source file paths under the vault’s source directory by reserving the current article slug when applicable, slugifying each source title, avoiding collisions with already reserved names or existing files, and returning the resulting 'PathBuf's. [crates/gwiki/src/synthesis.rs:503-525]
- `source_links` (function) component `source_links [function]` (`ac4840df-b980-5700-b615-28a660c7be23`) lines 527-537 [crates/gwiki/src/synthesis.rs:527-537]
  - Signature: `fn source_links(`
  - Purpose: Builds a 'Vec<String>' of wiki links by zipping 'sources' with 'source_paths' and formatting each pair via 'wiki_link(vault_root, path, &source.title)'. [crates/gwiki/src/synthesis.rs:527-537]
- `render_frontmatter` (function) component `render_frontmatter [function]` (`bebd3eef-5b44-5232-9f55-4f778b0043a5`) lines 539-573 [crates/gwiki/src/synthesis.rs:539-573]
  - Signature: `fn render_frontmatter(`
  - Purpose: 'render_frontmatter' appends a YAML frontmatter block to the provided Markdown buffer, setting the title, source kind, fixed 'gwiki' and 'compiled' tags, compile handoff ID, synthesis mode, and optional degraded-source metadata when any degraded sources are present. [crates/gwiki/src/synthesis.rs:539-573]
- `render_source_excerpts` (function) component `render_source_excerpts [function]` (`423c60ca-4042-5587-97ac-0fe173da8f01`) lines 575-593 [crates/gwiki/src/synthesis.rs:575-593]
  - Signature: `fn render_source_excerpts(markdown: &mut String, sources: &[SynthesisSource]) {`
  - Purpose: Appends a bulleted excerpt list of accepted sources to the markdown buffer, using each source’s title and first chunk when available, or emitting a fallback message when no text was extracted, and writing a “No accepted sources were recorded.” notice if the slice is empty. [crates/gwiki/src/synthesis.rs:575-593]
- `render_list_section` (function) component `render_list_section [function]` (`157dc583-2735-5e2c-8986-ceb2dcc5687a`) lines 595-609 [crates/gwiki/src/synthesis.rs:595-609]
  - Signature: `fn render_list_section(markdown: &mut String, title: &str, values: &[String]) {`
  - Purpose: Appends a Markdown level-2 section header and either a '- None recorded.' placeholder or a bullet list of the provided values to the 'markdown' buffer, followed by blank-line separation. [crates/gwiki/src/synthesis.rs:595-609]
- `trim_markdown_extension` (function) component `trim_markdown_extension [function]` (`d062d6b6-3399-56f5-ba6a-21a75116dcd9`) lines 611-616 [crates/gwiki/src/synthesis.rs:611-616]
  - Signature: `fn trim_markdown_extension(path: &str) -> String {`
  - Purpose: Returns the input path with a trailing '.md' or '.markdown' suffix removed, if present, otherwise returns the original path unchanged as a 'String'. [crates/gwiki/src/synthesis.rs:611-616]
- `yaml_scalar` (function) component `yaml_scalar [function]` (`9bd198a2-f37c-5bc6-93e0-d44367121152`) lines 618-636 [crates/gwiki/src/synthesis.rs:618-636]
  - Signature: `fn yaml_scalar(value: &str) -> String {`
  - Purpose: Returns a double-quoted YAML scalar string with backslash, quote, newline, carriage return, tab, NUL, other control characters, and DEL escaped using YAML-compatible escape sequences. [crates/gwiki/src/synthesis.rs:618-636]
- `write_created_synthesized_page` (function) component `write_created_synthesized_page [function]` (`b4e1e7f1-e648-5852-895f-fdea9f4c5c67`) lines 638-662 [crates/gwiki/src/synthesis.rs:638-662]
  - Signature: `fn write_created_synthesized_page(`
  - Purpose: Writes synthesized page bytes to a file, fsyncs them, and on either write or sync failure closes and deletes the target path before returning a 'WikiError::Io' with the path and underlying error. [crates/gwiki/src/synthesis.rs:638-662]
- `write_synthesized_page_atomically` (function) component `write_synthesized_page_atomically [function]` (`7db36eef-8cb9-5d5b-9c77-d405e72b3575`) lines 664-698 [crates/gwiki/src/synthesis.rs:664-698]
  - Signature: `fn write_synthesized_page_atomically(path: &Path, contents: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Writes 'contents' to a sibling temporary file, fsyncs it, atomically renames it over 'path', and syncs the parent directory, cleaning up the temp file and mapping any I/O failure into 'WikiError::Io'. [crates/gwiki/src/synthesis.rs:664-698]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`93cf934e-d4cd-514f-8819-e39eacc3c41f`) lines 700-719 [crates/gwiki/src/synthesis.rs:700-719]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, it opens the parent directory of 'path' and calls 'sync_all()' to flush directory metadata to disk, mapping any I/O failure into 'WikiError::Io', while on non-Unix platforms it is a no-op. [crates/gwiki/src/synthesis.rs:700-719]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`537af723-d179-53cf-a55f-f0edf7ddb705`) lines 721-731 [crates/gwiki/src/synthesis.rs:721-731]
  - Signature: `fn temp_sibling_path(path: &Path) -> PathBuf {`
  - Purpose: Constructs a temporary sibling 'PathBuf' by replacing the input path’s filename with a hidden '.{original_name}.{process_id}.{unix_nanos}.tmp' name, defaulting to 'page.md' if the filename is missing or non-UTF-8. [crates/gwiki/src/synthesis.rs:721-731]
- `existing_page_requires_merge_intent` (function) component `existing_page_requires_merge_intent [function]` (`d1f0c5af-0b51-56e8-ad89-a78eab1a8d23`) lines 738-765 [crates/gwiki/src/synthesis.rs:738-765]
  - Signature: `fn existing_page_requires_merge_intent() {`
  - Purpose: Verifies that 'write_synthesized_page' refuses to overwrite an already existing page when 'WritePolicy::RequireMergeIntent' is used, returning 'WikiError::InvalidInput' for 'write_intent' and leaving the original file unchanged. [crates/gwiki/src/synthesis.rs:738-765]
- `synthesized_page_write_classifies_create_and_overwrite_atomically` (function) component `synthesized_page_write_classifies_create_and_overwrite_atomically [function]` (`1f8723b8-f79a-5cd9-998e-a4f7e8739e96`) lines 768-791 [crates/gwiki/src/synthesis.rs:768-791]
  - Signature: `fn synthesized_page_write_classifies_create_and_overwrite_atomically() {`
  - Purpose: Verifies that 'write_synthesized_page' writes a new synthesized page as 'PageWriteKind::Created' on first call and 'PageWriteKind::Overwritten' on a second call with the same content, while leaving the file contents unchanged. [crates/gwiki/src/synthesis.rs:768-791]
- `slugify_unique_falls_back_after_bounded_suffixes` (function) component `slugify_unique_falls_back_after_bounded_suffixes [function]` (`0abda041-d4ca-58fc-8200-9312615db2fb`) lines 794-799 [crates/gwiki/src/synthesis.rs:794-799]
  - Signature: `fn slugify_unique_falls_back_after_bounded_suffixes() {`
  - Purpose: Verifies that 'slugify_unique("Collision", |_| true)' returns a slug prefixed with 'collision-' and includes an additional disambiguating suffix beyond the bounded base prefix. [crates/gwiki/src/synthesis.rs:794-799]
- `source_page_paths_reserve_article_path` (function) component `source_page_paths_reserve_article_path [function]` (`fa27bdc3-f450-5486-9c34-6f633251a369`) lines 802-815 [crates/gwiki/src/synthesis.rs:802-815]
  - Signature: `fn source_page_paths_reserve_article_path() {`
  - Purpose: Verifies that 'source_page_paths' does not reuse the target article path for a source page, instead allocating a distinct path under 'knowledge/sources' within the temporary workspace. [crates/gwiki/src/synthesis.rs:802-815]
- `synthesized_article_rejects_escaping_target_path` (function) component `synthesized_article_rejects_escaping_target_path [function]` (`475f9de9-6580-5157-b639-6ac5e2501326`) lines 818-854 [crates/gwiki/src/synthesis.rs:818-854]
  - Signature: `fn synthesized_article_rejects_escaping_target_path() {`
  - Purpose: Verifies that 'synthesize_article' rejects a target path that escapes the provided temp directory by returning 'WikiError::InvalidInput' for 'article_path'. [crates/gwiki/src/synthesis.rs:818-854]
- `synthesized_writer_rejects_escaping_page_path_before_write` (function) component `synthesized_writer_rejects_escaping_page_path_before_write [function]` (`0babc2f3-ab27-5657-be81-3d8bcdcdef07`) lines 857-886 [crates/gwiki/src/synthesis.rs:857-886]
  - Signature: `fn synthesized_writer_rejects_escaping_page_path_before_write() {`
  - Purpose: Verifies that 'write_synthesized_page' rejects a synthesized page whose target path escapes the allowed base directory, returning 'WikiError::InvalidInput' for 'synthesized_page' and not creating the خارج-path file. [crates/gwiki/src/synthesis.rs:857-886]
- `synthesized_writer_rejects_symlinked_parent_before_create_dir_all` (function) component `synthesized_writer_rejects_symlinked_parent_before_create_dir_all [function]` (`5293fcdc-d725-545c-ab01-308996f4ff3c`) lines 890-917 [crates/gwiki/src/synthesis.rs:890-917]
  - Signature: `fn synthesized_writer_rejects_symlinked_parent_before_create_dir_all() {`
  - Purpose: It verifies that 'write_synthesized_page' rejects a synthesized page whose parent path is a symlink before any 'create_dir_all'-driven directory creation, returning 'WikiError::InvalidInput' and leaving the symlink target untouched. [crates/gwiki/src/synthesis.rs:890-917]
- `yaml_scalar_escapes_quoted_control_characters` (function) component `yaml_scalar_escapes_quoted_control_characters [function]` (`699c8e12-cceb-50c3-89bf-4c0414ef5139`) lines 920-930 [crates/gwiki/src/synthesis.rs:920-930]
  - Signature: `fn yaml_scalar_escapes_quoted_control_characters() {`
  - Purpose: Verifies that 'yaml_scalar' emits double-quoted YAML strings and correctly escapes backslashes, quotes, control characters, and non-ASCII control bytes using standard YAML escape sequences. [crates/gwiki/src/synthesis.rs:920-930]

