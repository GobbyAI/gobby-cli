---
title: crates/gwiki/src/commands/read.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/read.rs
  ranges:
  - 17-28
  - 30-57
  - 59-85
  - 87-114
  - 116-122
  - 124-152
  - 154-181
  - 183-197
  - 199-211
  - 213-219
  - 221-235
  - 237-241
  - 243-312
  - 314-320
  - 322-329
  - 331-340
  - 342-361
  - 364-378
  - 380-385
  - 387-487
  - 490-493
  - 495-509
  - 512-515
  - 518-522
  - 524-557
  - 566-592
  - 595-608
  - 611-622
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/read.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

Implements the `read` command for gwiki. `execute` resolves the selected command scope, dispatches to either path-based or title-based lookup, and renders the result as a `CommandOutcome` or `WikiError`. The path flow normalizes and validates vault-relative paths, rejects unreadable locations, checks file existence, then reads markdown content with a byte cap, extracting the first heading and truncation metadata. The title flow searches the scoped wiki tree for matching first headings with bounded depth and scan limits, returning either the unique document, a not-found result, or an ambiguous result with candidates. Supporting types model the requested target, candidate documents, read output, and structured degradation/error messages used to report invalid input, missing documents, and ambiguity.
[crates/gwiki/src/commands/read.rs:17-28]
[crates/gwiki/src/commands/read.rs:30-57]
[crates/gwiki/src/commands/read.rs:59-85]
[crates/gwiki/src/commands/read.rs:87-114]
[crates/gwiki/src/commands/read.rs:116-122]

## API Symbols

- `execute` (function) component `execute [function]` (`8ef9ebe1-e821-5d37-a487-ea104e22da2f`) lines 17-28 [crates/gwiki/src/commands/read.rs:17-28]
  - Signature: `pub(crate) fn execute(`
  - Purpose: Resolves a command scope from the provided selection, reads either a path or title from that scope, and returns the rendered result as a CommandOutcome or WikiError. [crates/gwiki/src/commands/read.rs:17-28]
- `read_path` (function) component `read_path [function]` (`8b19ef2b-ddc2-58cf-ba52-edf8ce04d3a0`) lines 30-57 [crates/gwiki/src/commands/read.rs:30-57]
  - Signature: `fn read_path(`
  - Purpose: `read_path` validates and normalizes a requested file path within a scoped root directory, returning error responses for invalid or non-existent files, or delegates to read the existing file. [crates/gwiki/src/commands/read.rs:30-57]
- `read_title` (function) component `read_title [function]` (`bc93b476-82e4-5872-a117-229688f09085`) lines 59-85 [crates/gwiki/src/commands/read.rs:59-85]
  - Signature: `fn read_title(root: &Path, scope: ScopeIdentity, title: String) -> Result<ReadOutput, WikiError> {`
  - Purpose: Searches for a wiki document by title and returns the matching document if unambiguous, or a degraded result indicating invalid input, document not found, or ambiguity when multiple candidates exist. [crates/gwiki/src/commands/read.rs:59-85]
- `read_existing_path` (function) component `read_existing_path [function]` (`618f961f-ece7-547c-9ef2-32dd21fcba44`) lines 87-114 [crates/gwiki/src/commands/read.rs:87-114]
  - Signature: `fn read_existing_path(`
  - Purpose: Reads a wiki markdown file up to a configured byte limit and returns the content with extracted first-heading title, total file size, and truncation metadata. [crates/gwiki/src/commands/read.rs:87-114]
- `configured_read_max_bytes` (function) component `configured_read_max_bytes [function]` (`8db5548b-39f6-510b-afaf-eb7c903af6e0`) lines 116-122 [crates/gwiki/src/commands/read.rs:116-122]
  - Signature: `fn configured_read_max_bytes() -> usize {`
  - Purpose: Returns the configured maximum read size in bytes from an environment variable, or a default constant if the variable is missing, unparseable, or non-positive. [crates/gwiki/src/commands/read.rs:116-122]
- `read_markdown_prefix` (function) component `read_markdown_prefix [function]` (`4752581d-a145-5cad-8492-936cf8aea52f`) lines 124-152 [crates/gwiki/src/commands/read.rs:124-152]
  - Signature: `fn read_markdown_prefix(path: &Path, max_bytes: usize) -> Result<(String, bool), WikiError> {`
  - Purpose: Reads a file prefix up to a specified byte limit, truncating at valid UTF-8 boundaries if the file exceeds the limit, and returns the string content paired with a boolean indicating whether truncation occurred. [crates/gwiki/src/commands/read.rs:124-152]
- `normalize_requested_path` (function) component `normalize_requested_path [function]` (`c1d97539-ecb6-595f-9937-1ccf733333db`) lines 154-181 [crates/gwiki/src/commands/read.rs:154-181]
  - Signature: `fn normalize_requested_path(path: &Path) -> Result<PathBuf, ReadDegradation> {`
  - Purpose: Normalizes a vault-relative file path by accepting only normal path components and rejecting absolute paths, parent-directory traversals, and empty paths. [crates/gwiki/src/commands/read.rs:154-181]
- `readable_path_degradation` (function) component `readable_path_degradation [function]` (`6dcd34d6-793b-5efe-b85a-6beaef1bc5f6`) lines 183-197 [crates/gwiki/src/commands/read.rs:183-197]
  - Signature: `fn readable_path_degradation(path: &Path) -> Option<ReadDegradation> {`
  - Purpose: This function validates that a file path targets a `.md` file within designated wiki locations (raw/INDEX.md, _index.md, log.md, knowledge/, or code/), returning `None` if valid or a `ReadDegradation` error if the path is non-Markdown or outside permitted directories. [crates/gwiki/src/commands/read.rs:183-197]
- `is_readable_wiki_path` (function) component `is_readable_wiki_path [function]` (`ecf9bb0b-e2ed-5a88-89d0-7e1f5071c190`) lines 199-211 [crates/gwiki/src/commands/read.rs:199-211]
  - Signature: `fn is_readable_wiki_path(path: &Path) -> bool {`
  - Purpose: Returns `true` if the path matches one of three hardcoded wiki files (`raw/INDEX.md`, `_index.md`, `log.md`) or has normalized components starting with `knowledge/sources`, `knowledge/concepts`, `knowledge/topics`, or `code`. [crates/gwiki/src/commands/read.rs:199-211]
- `title_candidates` (function) component `title_candidates [function]` (`a3742e2b-25aa-58db-9922-9d586430e030`) lines 213-219 [crates/gwiki/src/commands/read.rs:213-219]
  - Signature: `fn title_candidates(`
  - Purpose: Retrieves up to `max_results` `ReadCandidate` entries matching a given title from a root directory path, delegating to `title_candidates_with_scan_budget` with a fixed `MAX_TITLE_SCAN_ENTRIES` scan budget constant. [crates/gwiki/src/commands/read.rs:213-219]
- `title_candidates_with_scan_budget` (function) component `title_candidates_with_scan_budget [function]` (`cc4905c4-a855-5f7a-9e8b-4a3da9ce20aa`) lines 221-235 [crates/gwiki/src/commands/read.rs:221-235]
  - Signature: `fn title_candidates_with_scan_budget(`
  - Purpose: Collects ReadCandidates matching a given title from a directory tree, constrained by limits on both result count and scanned entries. [crates/gwiki/src/commands/read.rs:221-235]
- `TitleCandidateSearch` (class) component `TitleCandidateSearch [class]` (`1a69fb0f-2831-5354-924f-1325af61f872`) lines 237-241 [crates/gwiki/src/commands/read.rs:237-241]
  - Signature: `struct TitleCandidateSearch {`
  - Purpose: `TitleCandidateSearch` is a struct that constrains and tracks a bounded search operation by limiting maximum results and scanned entries while maintaining a scan progress counter. [crates/gwiki/src/commands/read.rs:237-241]
- `collect_title_candidates` (function) component `collect_title_candidates [function]` (`c69b92d5-d3fc-5490-a8f5-b05936460d1c`) lines 243-312 [crates/gwiki/src/commands/read.rs:243-312]
  - Signature: `fn collect_title_candidates(`
  - Purpose: Recursively scans a wiki directory tree to collect documents whose first heading matches a given title, respecting configurable depth and result count limits. [crates/gwiki/src/commands/read.rs:243-312]
- `first_heading` (function) component `first_heading [function]` (`3049abc2-c0f7-52de-ae38-e11f4371afbe`) lines 314-320 [crates/gwiki/src/commands/read.rs:314-320]
  - Signature: `fn first_heading(content: &str) -> Option<String> {`
  - Purpose: This function returns the first non-empty ATX-style Markdown heading from the input string, or `None` if no such heading exists. [crates/gwiki/src/commands/read.rs:314-320]
- `normal_components` (function) component `normal_components [function]` (`8e71259b-5b72-5508-bb44-9e19f4adef6e`) lines 322-329 [crates/gwiki/src/commands/read.rs:322-329]
  - Signature: `fn normal_components(path: &Path) -> Vec<&str> {`
  - Purpose: Filters a Path to extract only normal components (excluding root and parent references) and returns them as a vector of string slices. [crates/gwiki/src/commands/read.rs:322-329]
- `render` (function) component `render [function]` (`6d876fd2-62f4-5ba5-95b3-37fce8f8dcd5`) lines 331-340 [crates/gwiki/src/commands/read.rs:331-340]
  - Signature: `fn render(output: ReadOutput) -> Result<CommandOutcome, WikiError> {`
  - Purpose: Transforms a `ReadOutput` into a scoped `CommandOutcome` by rendering its text representation and serializing the structure to JSON, returning a `WikiError` on serialization failure. [crates/gwiki/src/commands/read.rs:331-340]
- `render_text` (function) component `render_text [function]` (`fb431efe-60c4-5b5a-aa3d-ffab11d21221`) lines 342-361 [crates/gwiki/src/commands/read.rs:342-361]
  - Signature: `fn render_text(output: &ReadOutput) -> String {`
  - Purpose: Converts a `ReadOutput` into a formatted string by either returning cached content or constructing a report containing the wiki read status, scope, requested item details, and degradation messages with guidance. [crates/gwiki/src/commands/read.rs:342-361]
- `ReadOutput` (class) component `ReadOutput [class]` (`2a815644-c1f4-59b4-ba6c-f020352a3fdb`) lines 364-378 [crates/gwiki/src/commands/read.rs:364-378]
  - Signature: `struct ReadOutput {`
  - Purpose: ReadOutput is a response struct that aggregates the metadata, resolved file paths, content with format specification, and diagnostic information (candidates and degradations) resulting from a read operation. [crates/gwiki/src/commands/read.rs:364-378]
- `ReadFoundContent` (class) component `ReadFoundContent [class]` (`c868272f-3cd9-510b-b46c-204036a1672f`) lines 380-385 [crates/gwiki/src/commands/read.rs:380-385]
  - Signature: `struct ReadFoundContent {`
  - Purpose: `ReadFoundContent` is a struct that encapsulates retrieved content with an optional title, byte length, and a flag indicating whether the content was truncated. [crates/gwiki/src/commands/read.rs:380-385]
- `ReadOutput` (class) component `ReadOutput [class]` (`72595c5f-c964-543d-84c0-7334c07284e3`) lines 387-487 [crates/gwiki/src/commands/read.rs:387-487]
  - Signature: `impl ReadOutput {`
  - Purpose: `ReadOutput` impl provides factory constructors that instantiate result objects with different status conditions (found, not_found, invalid_request, ambiguous) for scoped wiki document read operations. [crates/gwiki/src/commands/read.rs:387-487]
- `ReadOutput.found` (method) component `ReadOutput.found [method]` (`b3275715-2e50-5156-98a7-2648588d4ca5`) lines 388-410 [crates/gwiki/src/commands/read.rs:388-410]
  - Signature: `fn found(`
  - Purpose: Constructs a read command response struct with 'found' status, encapsulating the scope, request context, file paths, and retrieved content metadata with an empty candidates list. [crates/gwiki/src/commands/read.rs:388-410]
- `ReadOutput.not_found` (method) component `ReadOutput.not_found [method]` (`63b15e49-ea04-5bc2-95a5-b3560b04c82c`) lines 412-427 [crates/gwiki/src/commands/read.rs:412-427]
  - Signature: `fn not_found(`
  - Purpose: Creates a not-found read response instance by delegating to `Self::empty` with the provided degradation wrapped in a single-element vector. [crates/gwiki/src/commands/read.rs:412-427]
- `ReadOutput.invalid_request` (method) component `ReadOutput.invalid_request [method]` (`cc7aba31-b51c-5b99-b4d4-b3e3adc46694`) lines 429-442 [crates/gwiki/src/commands/read.rs:429-442]
  - Signature: `fn invalid_request(`
  - Purpose: Constructs an empty instance tagged as "invalid_request" with the provided scope, requested parameters, and degradation, while passing `None` for two intermediate fields. [crates/gwiki/src/commands/read.rs:429-442]
- `ReadOutput.ambiguous` (method) component `ReadOutput.ambiguous [method]` (`2c545177-9e04-59de-9af9-17290f47995f`) lines 444-461 [crates/gwiki/src/commands/read.rs:444-461]
  - Signature: `fn ambiguous(`
  - Purpose: Factory method that creates a read result indicating ambiguous resolution when multiple scoped wiki documents match the requested title, storing the scope, request metadata, and candidate list. [crates/gwiki/src/commands/read.rs:444-461]
- `ReadOutput.empty` (method) component `ReadOutput.empty [method]` (`d9117254-d2a7-557d-b482-7a4863ca8cad`) lines 463-486 [crates/gwiki/src/commands/read.rs:463-486]
  - Signature: `fn empty(`
  - Purpose: Constructs a read response struct with provided scope, status, paths, and degradations while initializing all content-bearing fields to None or empty values. [crates/gwiki/src/commands/read.rs:463-486]
- `ReadRequested` (class) component `ReadRequested [class]` (`29316e64-2e34-5da2-828b-475ad7d11711`) lines 490-493 [crates/gwiki/src/commands/read.rs:490-493]
  - Signature: `struct ReadRequested {`
  - Purpose: `ReadRequested` is a struct that pairs a static string kind discriminator with an owned `String` value to represent a typed read operation request. [crates/gwiki/src/commands/read.rs:490-493]
- `ReadRequested` (class) component `ReadRequested [class]` (`f9584bc1-1b29-5607-8bb4-4ca286adcf7f`) lines 495-509 [crates/gwiki/src/commands/read.rs:495-509]
  - Signature: `impl ReadRequested {`
  - Purpose: `ReadRequested`'s impl block provides two factory methods (`path` and `title`) that construct instances with their respective `kind` variant and a `String` value. [crates/gwiki/src/commands/read.rs:495-509]
- `ReadRequested.path` (method) component `ReadRequested.path [method]` (`9cb98ce0-d9b4-52c5-a5ac-4209f757cf3e`) lines 496-501 [crates/gwiki/src/commands/read.rs:496-501]
  - Signature: `fn path(value: String) -> Self {`
  - Purpose: This constructor creates a new `Self` instance with the `kind` field set to the string literal `"path"` and the `value` field assigned to the provided `String` parameter. [crates/gwiki/src/commands/read.rs:496-501]
- `ReadRequested.title` (method) component `ReadRequested.title [method]` (`12391654-7d30-530c-b678-89cbc2076241`) lines 503-508 [crates/gwiki/src/commands/read.rs:503-508]
  - Signature: `fn title(value: String) -> Self {`
  - Purpose: Constructs a `Self` instance with the `kind` field set to the literal string `"title"` and the `value` field assigned the input `String` parameter. [crates/gwiki/src/commands/read.rs:503-508]
- `ReadCandidate` (class) component `ReadCandidate [class]` (`664c5e6e-cad1-52af-8437-be1a041bf562`) lines 512-515 [crates/gwiki/src/commands/read.rs:512-515]
  - Signature: `struct ReadCandidate {`
  - Purpose: `ReadCandidate` is a struct that pairs a filesystem path with an optional string title, representing a candidate wiki document to be read. [crates/gwiki/src/commands/read.rs:512-515]
- `ReadDegradation` (class) component `ReadDegradation [class]` (`f0e5b7e0-fb48-57da-a459-45dcae530e83`) lines 518-522 [crates/gwiki/src/commands/read.rs:518-522]
  - Signature: `struct ReadDegradation {`
  - Purpose: `ReadDegradation` is a struct that pairs two static string references (`reason` and `guidance`) with a heap-allocated `String` (`message`) to communicate diagnostic information about read operation degradation. [crates/gwiki/src/commands/read.rs:518-522]
- `ReadDegradation` (class) component `ReadDegradation [class]` (`8499ea8a-81a8-537d-9719-4cf34616154c`) lines 524-557 [crates/gwiki/src/commands/read.rs:524-557]
  - Signature: `impl ReadDegradation {`
  - Purpose: ReadDegradation provides factory methods and a display label mapper to construct structured document read failure states with reason-specific guidance for users. [crates/gwiki/src/commands/read.rs:524-557]
- `ReadDegradation.display_label` (method) component `ReadDegradation.display_label [method]` (`bf25fb1c-cf19-55b6-9e8d-867bd1c97991`) lines 525-532 [crates/gwiki/src/commands/read.rs:525-532]
  - Signature: `fn display_label(&self) -> &'static str {`
  - Purpose: Returns a static string slice containing a human-readable display label mapped from the `reason` field via exhaustive pattern matching, with "Degraded" as the default case. [crates/gwiki/src/commands/read.rs:525-532]
- `ReadDegradation.invalid_request` (method) component `ReadDegradation.invalid_request [method]` (`a9f22573-87ef-59fa-9fc3-5186f7eccee5`) lines 534-540 [crates/gwiki/src/commands/read.rs:534-540]
  - Signature: `fn invalid_request(message: impl Into<String>) -> Self {`
  - Purpose: # Summary

This method constructs and returns an error instance with reason `"invalid_request"`, converting the provided message parameter and including usage guidance directing callers to provide either a `--path` with a vault-relative Markdown path or a `--title` with an exact first heading. [crates/gwiki/src/commands/read.rs:534-540]
- `ReadDegradation.not_found` (method) component `ReadDegradation.not_found [method]` (`bc192068-8595-5615-aa9e-abdd4bde19a0`) lines 542-548 [crates/gwiki/src/commands/read.rs:542-548]
  - Signature: `fn not_found(message: impl Into<String>) -> Self {`
  - Purpose: This factory method constructs a `not_found` error instance with a user-provided message and predefined guidance directing users to search or specify a vault-relative path. [crates/gwiki/src/commands/read.rs:542-548]
- `ReadDegradation.ambiguous` (method) component `ReadDegradation.ambiguous [method]` (`f0b6c883-863d-591c-8006-aaf9fb3cc649`) lines 550-556 [crates/gwiki/src/commands/read.rs:550-556]
  - Signature: `fn ambiguous(message: impl Into<String>) -> Self {`
  - Purpose: Constructs a Self instance with the fixed reason code "ambiguous", a generic message parameter, and static guidance text instructing the user to resolve the ambiguity by passing `--path` with a candidate wiki_path value. [crates/gwiki/src/commands/read.rs:550-556]
- `read_path_caps_content_and_marks_truncated` (function) component `read_path_caps_content_and_marks_truncated [function]` (`ced3ed5e-1c79-54b3-899d-50b780203db4`) lines 566-592 [crates/gwiki/src/commands/read.rs:566-592]
  - Signature: `fn read_path_caps_content_and_marks_truncated() {`
  - Purpose: This function tests that `read_path()` correctly truncates file content to the byte limit specified by `READ_MAX_BYTES_ENV` while preserving the full file length in metadata and setting a truncation flag. [crates/gwiki/src/commands/read.rs:566-592]
- `title_search_stops_at_max_depth` (function) component `title_search_stops_at_max_depth [function]` (`78c0f306-caf7-5a6a-b5b6-0238d9da34d8`) lines 595-608 [crates/gwiki/src/commands/read.rs:595-608]
  - Signature: `fn title_search_stops_at_max_depth() {`
  - Purpose: Verifies that `title_candidates()` enforces a search depth limit by returning empty results when the target markdown file exceeds `MAX_TITLE_SEARCH_DEPTH` nesting levels. [crates/gwiki/src/commands/read.rs:595-608]
- `title_search_stops_at_scan_budget` (function) component `title_search_stops_at_scan_budget [function]` (`971e1604-aee8-565b-b053-8e25fb6b38d2`) lines 611-622 [crates/gwiki/src/commands/read.rs:611-622]
  - Signature: `fn title_search_stops_at_scan_budget() {`
  - Purpose: This test verifies that `title_candidates_with_scan_budget` returns an empty result set when the scan budget parameter is set to zero, preventing title candidate discovery despite matching files existing in the filesystem. [crates/gwiki/src/commands/read.rs:611-622]

