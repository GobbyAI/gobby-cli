---
title: crates/gwiki/src/librarian.rs
type: code_file
provenance:
- file: crates/gwiki/src/librarian.rs
  ranges:
  - 15-20
  - 22-31
  - 23-30
  - 33-40
  - 34-39
  - 43-50
  - 52-60
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

# crates/gwiki/src/librarian.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/librarian.rs` exposes 38 indexed API symbols.
[crates/gwiki/src/librarian.rs:15-20]
[crates/gwiki/src/librarian.rs:22-31]
[crates/gwiki/src/librarian.rs:23-30]
[crates/gwiki/src/librarian.rs:33-40]
[crates/gwiki/src/librarian.rs:34-39]
[crates/gwiki/src/librarian.rs:43-50]
[crates/gwiki/src/librarian.rs:52-60]
[crates/gwiki/src/librarian.rs:54-59]
[crates/gwiki/src/librarian.rs:63-69]
[crates/gwiki/src/librarian.rs:72-76]
[crates/gwiki/src/librarian.rs:79-85]
[crates/gwiki/src/librarian.rs:88-93]
[crates/gwiki/src/librarian.rs:96-100]
[crates/gwiki/src/librarian.rs:102-198]
[crates/gwiki/src/librarian.rs:200-230]
[crates/gwiki/src/librarian.rs:232-239]
[crates/gwiki/src/librarian.rs:241-253]
[crates/gwiki/src/librarian.rs:255-264]
[crates/gwiki/src/librarian.rs:266-272]
[crates/gwiki/src/librarian.rs:274-283]
[crates/gwiki/src/librarian.rs:285-291]
[crates/gwiki/src/librarian.rs:293-303]
[crates/gwiki/src/librarian.rs:305-355]
[crates/gwiki/src/librarian.rs:357-371]
[crates/gwiki/src/librarian.rs:373-390]
[crates/gwiki/src/librarian.rs:392-394]
[crates/gwiki/src/librarian.rs:396-403]
[crates/gwiki/src/librarian.rs:405-434]
[crates/gwiki/src/librarian.rs:436-452]
[crates/gwiki/src/librarian.rs:454-461]
[crates/gwiki/src/librarian.rs:475-562]
[crates/gwiki/src/librarian.rs:565-591]
[crates/gwiki/src/librarian.rs:594-617]
[crates/gwiki/src/librarian.rs:620-639]
[crates/gwiki/src/librarian.rs:642-656]
[crates/gwiki/src/librarian.rs:660-679]
[crates/gwiki/src/librarian.rs:681-685]
[crates/gwiki/src/librarian.rs:687-701]

## API Symbols

- `Options` (class) component `Options [class]` (`470c03cf-0128-5697-8ff8-e84d2b915c41`) lines 15-20 [crates/gwiki/src/librarian.rs:15-20]
  - Signature: `pub struct Options {`
  - Purpose: `Options` is a Rust struct containing four public boolean fields that represent feature availability and configuration flags for PostgreSQL indexing requirements, shared code graph, semantic analysis, and model capabilities. [crates/gwiki/src/librarian.rs:15-20]
- `Options` (class) component `Options [class]` (`bfbe48fd-3674-5ef6-b3ba-9f08a99bd5b2`) lines 22-31 [crates/gwiki/src/librarian.rs:22-31]
  - Signature: `impl Options {`
  - Purpose: The `offline()` method is a constructor that returns an Options instance with all availability flags (postgres_index requirement, shared_code_graph, semantic analysis, and model inference) disabled for offline-only operation. [crates/gwiki/src/librarian.rs:22-31]
- `Options.offline` (method) component `Options.offline [method]` (`64077f00-50a8-5001-883f-1cf3c7a4a00c`) lines 23-30 [crates/gwiki/src/librarian.rs:23-30]
  - Signature: `pub fn offline() -> Self {`
  - Purpose: Creates and returns an instance of `Self` with all four boolean configuration flags (`require_postgres_index`, `shared_code_graph_available`, `semantic_available`, `model_available`) initialized to `false`, representing an offline state with no external dependencies available. [crates/gwiki/src/librarian.rs:23-30]
- `Options` (class) component `Options [class]` (`ac710dd5-c8e2-5fda-9dd4-30ed5dd3e155`) lines 33-40 [crates/gwiki/src/librarian.rs:33-40]
  - Signature: `impl Default for Options {`
  - Purpose: The Default implementation for Options sets `require_postgres_index` to `true` while initializing all remaining fields through the `offline()` constructor method. [crates/gwiki/src/librarian.rs:33-40]
- `Options.default` (method) component `Options.default [method]` (`f6952d0f-2f66-5501-998a-be8697d7cfff`) lines 34-39 [crates/gwiki/src/librarian.rs:34-39]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a default instance with `require_postgres_index` set to `true` while inheriting all remaining fields from `Self::offline()` via struct update syntax. [crates/gwiki/src/librarian.rs:34-39]
- `ProposalsReport` (class) component `ProposalsReport [class]` (`b175e249-d3f2-5232-87d6-ade0e8e3f238`) lines 43-50 [crates/gwiki/src/librarian.rs:43-50]
  - Signature: `pub struct ProposalsReport {`
  - Purpose: ProposalsReport encapsulates scope-specific analysis results aggregating validation checks, suggested tasks and patches, generated artifacts, and dependency classifications. [crates/gwiki/src/librarian.rs:43-50]
- `ProposalsReport` (class) component `ProposalsReport [class]` (`9ca6c1e6-d336-52a9-b866-2d5bbcd7b29c`) lines 52-60 [crates/gwiki/src/librarian.rs:52-60]
  - Signature: `impl ProposalsReport {`
  - Purpose: ProposalsReport implements a test-only accessor method that retrieves a CheckReport from its internal checks collection by name, panicking if not found. [crates/gwiki/src/librarian.rs:52-60]
- `ProposalsReport.check` (method) component `ProposalsReport.check [method]` (`93249c15-072e-5f05-a726-3ffeb88a2e9b`) lines 54-59 [crates/gwiki/src/librarian.rs:54-59]
  - Signature: `fn check(&self, name: &str) -> &CheckReport {`
  - Purpose: Returns an immutable reference to a `CheckReport` from the internal collection by matching the given name, panicking if the check is not found. [crates/gwiki/src/librarian.rs:54-59]
- `CheckReport` (class) component `CheckReport [class]` (`9743d59c-9062-55be-8616-e2430fee16ad`) lines 63-69 [crates/gwiki/src/librarian.rs:63-69]
  - Signature: `pub struct CheckReport {`
  - Purpose: CheckReport is a serializable struct that aggregates the results of an availability check, containing a static name identifier, boolean availability status, optional note, and vector of associated file paths. [crates/gwiki/src/librarian.rs:63-69]
- `SuggestedTask` (class) component `SuggestedTask [class]` (`627081f8-f82a-54aa-b840-805c7c501565`) lines 72-76 [crates/gwiki/src/librarian.rs:72-76]
  - Signature: `pub struct SuggestedTask {`
  - Purpose: `SuggestedTask` is a public struct that encapsulates a suggested task with a title, description, and a vector of associated filesystem paths. [crates/gwiki/src/librarian.rs:72-76]
- `SuggestedPatchDiff` (class) component `SuggestedPatchDiff [class]` (`f028b8a9-fffa-57ba-9e90-f13d9df576df`) lines 79-85 [crates/gwiki/src/librarian.rs:79-85]
  - Signature: `pub struct SuggestedPatchDiff {`
  - Purpose: `SuggestedPatchDiff` is a struct that encapsulates a proposed file patch with its target path, textual summary, unified diff content, and flags indicating whether it applies to canonical content and requires user acceptance. [crates/gwiki/src/librarian.rs:79-85]
- `LibrarianArtifacts` (class) component `LibrarianArtifacts [class]` (`17160810-14af-5337-9749-be22f25f6d6d`) lines 88-93 [crates/gwiki/src/librarian.rs:88-93]
  - Signature: `pub struct LibrarianArtifacts {`
  - Purpose: `LibrarianArtifacts` is a struct that aggregates file system paths to four JSON and Markdown output artifacts: proposals, audit annotations, and stale pages metadata. [crates/gwiki/src/librarian.rs:88-93]
- `DependencyClassification` (class) component `DependencyClassification [class]` (`2e9e2fa8-d6fc-53cd-91c3-6a9f490d6a47`) lines 96-100 [crates/gwiki/src/librarian.rs:96-100]
  - Signature: `pub struct DependencyClassification {`
  - Purpose: `DependencyClassification` is a struct that categorizes dependencies using static string references partitioned into hard-required, optional, and multimodal classifications. [crates/gwiki/src/librarian.rs:96-100]
- `run` (function) component `run [function]` (`91a0c8d5-ffd7-52b9-8726-8a9f00b63a8c`) lines 102-198 [crates/gwiki/src/librarian.rs:102-198]
  - Signature: `pub fn run(`
  - Purpose: Orchestrates health inspection, audit validation, and linting analysis on a scoped documentation vault to aggregate detected quality issues (stale pages, missing citations, broken links, weak provenance, outdated codewiki references) into a ProposalsReport. [crates/gwiki/src/librarian.rs:102-198]
- `render_text` (function) component `render_text [function]` (`1ea3bae6-ab48-5cff-9d65-a438767f7994`) lines 200-230 [crates/gwiki/src/librarian.rs:200-230]
  - Signature: `pub fn render_text(report: &ProposalsReport) -> String {`
  - Purpose: Converts a `ProposalsReport` into a formatted text string containing a scope header, availability status with item listings for each check, and a list of suggested tasks. [crates/gwiki/src/librarian.rs:200-230]
- `available_check` (function) component `available_check [function]` (`45cc9913-6d2c-5a3b-94dc-9dcaeee0b72c`) lines 232-239 [crates/gwiki/src/librarian.rs:232-239]
  - Signature: `fn available_check(name: &'static str, items: Vec<PathBuf>) -> CheckReport {`
  - Purpose: Constructs a `CheckReport` struct indicating availability is true with the provided static name and path buffer items. [crates/gwiki/src/librarian.rs:232-239]
- `optional_check` (function) component `optional_check [function]` (`4e5774c9-978f-56be-ae27-acc9521a0003`) lines 241-253 [crates/gwiki/src/librarian.rs:241-253]
  - Signature: `fn optional_check(`
  - Purpose: Constructs a CheckReport struct that conditionally includes items if available or populates an unavailability note if not. [crates/gwiki/src/librarian.rs:241-253]
- `weak_provenance_pages` (function) component `weak_provenance_pages [function]` (`dda378e7-4cc9-559c-b0fc-979e3bf48398`) lines 255-264 [crates/gwiki/src/librarian.rs:255-264]
  - Signature: `fn weak_provenance_pages(pages: &[lint::WikiPage], provenance: &ProvenanceGraph) -> Vec<PathBuf> {`
  - Purpose: Collects and returns lexicographically sorted relative paths of codewiki pages not referenced in the provenance graph. [crates/gwiki/src/librarian.rs:255-264]
- `provenance_mentions_page` (function) component `provenance_mentions_page [function]` (`b42aa384-5348-5aab-b1cc-b955979da417`) lines 266-272 [crates/gwiki/src/librarian.rs:266-272]
  - Signature: `fn provenance_mentions_page(provenance: &ProvenanceGraph, path: &Path) -> bool {`
  - Purpose: Returns `true` if the provenance graph contains any link whose section's page path matches the provided file path. [crates/gwiki/src/librarian.rs:266-272]
- `outdated_codewiki_pages` (function) component `outdated_codewiki_pages [function]` (`6a86a166-55bc-5632-87b1-1d65298fc33c`) lines 274-283 [crates/gwiki/src/librarian.rs:274-283]
  - Signature: `fn outdated_codewiki_pages(pages: &[lint::WikiPage]) -> Vec<PathBuf> {`
  - Purpose: This function filters wiki pages marked as codewiki with 'stale' frontmatter status, extracts their relative paths, and returns them sorted. [crates/gwiki/src/librarian.rs:274-283]
- `page_is_codewiki` (function) component `page_is_codewiki [function]` (`c146d506-0c60-59c1-96fd-ffd2bfc7889c`) lines 285-291 [crates/gwiki/src/librarian.rs:285-291]
  - Signature: `fn page_is_codewiki(page: &lint::WikiPage) -> bool {`
  - Purpose: This function returns `true` if the WikiPage's frontmatter `generated_by` field contains the substring "codewiki", `false` otherwise. [crates/gwiki/src/librarian.rs:285-291]
- `frontmatter_flag` (function) component `frontmatter_flag [function]` (`b0c37dc8-383d-5342-9962-7814f6ee1440`) lines 293-303 [crates/gwiki/src/librarian.rs:293-303]
  - Signature: `fn frontmatter_flag(markdown: &str, key: &str, expected: &str) -> bool {`
  - Purpose: Extracts and validates a frontmatter metadata field against an expected value, returning true for string equality or boolean true when expected is "true", otherwise false. [crates/gwiki/src/librarian.rs:293-303]
- `suggested_tasks` (function) component `suggested_tasks [function]` (`3dd4e688-a4ec-547b-bc78-f71e64f2981d`) lines 305-355 [crates/gwiki/src/librarian.rs:305-355]
  - Signature: `fn suggested_tasks(`
  - Purpose: Aggregates wiki documentation quality defects (stale pages, missing citations, broken links, weak provenance, outdated codewiki) into a vector of suggested remediation tasks. [crates/gwiki/src/librarian.rs:305-355]
- `push_task` (function) component `push_task [function]` (`3b4c3e5a-722e-5c44-84d6-38b8a550306a`) lines 357-371 [crates/gwiki/src/librarian.rs:357-371]
  - Signature: `fn push_task(`
  - Purpose: Conditionally appends a new `SuggestedTask` containing the provided title, description, and paths to the tasks vector if the `include` flag is true. [crates/gwiki/src/librarian.rs:357-371]
- `suggested_patch_diffs` (function) component `suggested_patch_diffs [function]` (`12819a51-7af5-5a14-bb48-dce2eb62827f`) lines 373-390 [crates/gwiki/src/librarian.rs:373-390]
  - Signature: `fn suggested_patch_diffs(`
  - Purpose: Generates suggested patch diffs that insert citation refresh reminder comments into de-duplicated file paths with stale or missing citations, marked for canonical content application with mandatory user acceptance. [crates/gwiki/src/librarian.rs:373-390]
- `unique_paths` (function) component `unique_paths [function]` (`da33eb1c-4a9a-59b3-b076-e5c3e3955a2d`) lines 392-394 [crates/gwiki/src/librarian.rs:392-394]
  - Signature: `fn unique_paths(paths: impl Iterator<Item = PathBuf>) -> Vec<PathBuf> {`
  - Purpose: Deduplicates and lexicographically sorts an iterator of PathBuf values into a vector by using a BTreeSet as an intermediate collection. [crates/gwiki/src/librarian.rs:392-394]
- `artifacts` (function) component `artifacts [function]` (`752679d1-fdaa-53b7-8a7f-88ac30c507b9`) lines 396-403 [crates/gwiki/src/librarian.rs:396-403]
  - Signature: `fn artifacts() -> LibrarianArtifacts {`
  - Purpose: Returns a `LibrarianArtifacts` struct initialized with `PathBuf` instances for four librarian metadata files (proposals in JSON and Markdown formats, audit annotations, and stale pages). [crates/gwiki/src/librarian.rs:396-403]
- `persist_report` (function) component `persist_report [function]` (`7484246e-b4ee-51b4-99e5-9c002f9c1095`) lines 405-434 [crates/gwiki/src/librarian.rs:405-434]
  - Signature: `fn persist_report(vault_root: &Path, report: &ProposalsReport) -> Result<(), WikiError> {`
  - Purpose: Persists a ProposalsReport by serializing its proposals and audit check results (missing_citations, weak_provenance, stale_pages, outdated_codewiki) to JSON and markdown artifacts in a librarian metadata directory. [crates/gwiki/src/librarian.rs:405-434]
- `write_json` (function) component `write_json [function]` (`47e3ce88-0c68-52ad-8994-1798aae06e0b`) lines 436-452 [crates/gwiki/src/librarian.rs:436-452]
  - Signature: `fn write_json<T: Serialize>(`
  - Purpose: Serializes a Serialize-implementing value to a pretty-printed JSON file at the specified vault path, mapping serialization and I/O errors to WikiError variants. [crates/gwiki/src/librarian.rs:436-452]
- `write_text` (function) component `write_text [function]` (`522f78b0-5017-5425-beb4-9fc2bd38575f`) lines 454-461 [crates/gwiki/src/librarian.rs:454-461]
  - Signature: `fn write_text(vault_root: &Path, relative: &Path, text: &str) -> Result<(), WikiError> {`
  - Purpose: Writes a text string to a file at the path formed by joining `vault_root` and `relative`, mapping IO errors to `WikiError`. [crates/gwiki/src/librarian.rs:454-461]
- `librarian_detects_and_proposes_without_rewriting_pages` (function) component `librarian_detects_and_proposes_without_rewriting_pages [function]` (`c90b5439-c094-5784-9bf2-e29a397a9d27`) lines 475-562 [crates/gwiki/src/librarian.rs:475-562]
  - Signature: `fn librarian_detects_and_proposes_without_rewriting_pages() {`
  - Purpose: This test verifies that the librarian detects documentation defects (stale pages, missing citations, broken links, and weak provenance) and generates a diagnostic report without modifying the source files. [crates/gwiki/src/librarian.rs:475-562]
- `librarian_filters_codewiki_checks_to_selected_scope` (function) component `librarian_filters_codewiki_checks_to_selected_scope [function]` (`19864fe4-a833-5723-b1b5-e373a69d02d4`) lines 565-591 [crates/gwiki/src/librarian.rs:565-591]
  - Signature: `fn librarian_filters_codewiki_checks_to_selected_scope() {`
  - Purpose: Validates that the librarian restricts codewiki checks (weak_provenance and outdated_codewiki) to the selected scope identity, filtering out items outside the specified topic scope. [crates/gwiki/src/librarian.rs:565-591]
- `librarian_degrades_each_optional_check_independently` (function) component `librarian_degrades_each_optional_check_independently [function]` (`3393e5f2-8b80-54d6-822e-5ae55c66f2f3`) lines 594-617 [crates/gwiki/src/librarian.rs:594-617]
  - Signature: `fn librarian_degrades_each_optional_check_independently() {`
  - Purpose: This test verifies that the librarian tool independently disables optional quality checks based on resource availability, enabling four dependency-free checks (stale pages, citations, links, provenance) while gracefully degrading those requiring unavailable external resources (shared code graph) in offline mode. [crates/gwiki/src/librarian.rs:594-617]
- `librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale` (function) component `librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale [function]` (`13a9c968-ebe4-544b-857f-93cc0f41ac75`) lines 620-639 [crates/gwiki/src/librarian.rs:620-639]
  - Signature: `fn librarian_outdated_codewiki_unavailable_without_shared_graph_even_when_stale() {`
  - Purpose: Tests that the librarian's outdated_codewiki check is unavailable and skipped when running in offline mode due to inaccessible shared code graph. [crates/gwiki/src/librarian.rs:620-639]
- `librarian_codewiki_path_checks_are_sorted` (function) component `librarian_codewiki_path_checks_are_sorted [function]` (`f5dbf43d-d493-5b76-987a-75f0000f43e5`) lines 642-656 [crates/gwiki/src/librarian.rs:642-656]
  - Signature: `fn librarian_codewiki_path_checks_are_sorted() {`
  - Purpose: Tests that `weak_provenance_pages` and `outdated_codewiki_pages` functions return codewiki page paths in lexicographically sorted order regardless of input ordering. [crates/gwiki/src/librarian.rs:642-656]
- `librarian_requires_configured_postgres_index` (function) component `librarian_requires_configured_postgres_index [function]` (`a52ae97f-39bd-562e-b00d-779e1cc0624c`) lines 660-679 [crates/gwiki/src/librarian.rs:660-679]
  - Signature: `fn librarian_requires_configured_postgres_index() {`
  - Purpose: This test verifies that the librarian fails with a specific PostgreSQL connection error when attempting to run with an unreachable database URL. [crates/gwiki/src/librarian.rs:660-679]
- `write_page` (function) component `write_page [function]` (`0a6de2ff-8122-53d3-8b28-8eb8f0d27e1d`) lines 681-685 [crates/gwiki/src/librarian.rs:681-685]
  - Signature: `fn write_page(root: &Path, relative: &str, markdown: &str) {`
  - Purpose: Writes markdown content to a file at the path formed by joining `root` and `relative`, creating all intermediate parent directories as needed. [crates/gwiki/src/librarian.rs:681-685]
- `codewiki_page` (function) component `codewiki_page [function]` (`0baec6d0-d7e0-5231-b166-a070518ed4bb`) lines 687-701 [crates/gwiki/src/librarian.rs:687-701]
  - Signature: `fn codewiki_page(relative: &str, stale: bool) -> lint::WikiPage {`
  - Purpose: Constructs a `lint::WikiPage` from a relative path with YAML frontmatter metadata indicating code documentation staleness status (stale/fresh). [crates/gwiki/src/librarian.rs:687-701]

