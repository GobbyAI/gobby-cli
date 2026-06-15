---
title: crates/gwiki/src/ingest/git.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/git.rs
  ranges:
  - 15-18
  - 22-27
  - 30-55
  - 58-74
  - 77-109
  - 112-127
  - 130-142
  - 145-154
  - 157-172
  - 181-236
  - 239-247
  - 250-261
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/git.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

Defines ingestion support for Git repository snapshots in `gwiki`. The two snapshot types model a repository commit plus selected files, and `ingest_repository` turns that snapshot into a registered source by validating that files exist, serializing provenance/content for the source draft, rendering a markdown document, and writing/indexing it in the vault store. The helper functions build the serialized byte payload, generate frontmatter and markdown with safe code fences and file-type info, and the tests verify that commit provenance is preserved and fence generation stays bounded under hostile content.
[crates/gwiki/src/ingest/git.rs:15-18]
[crates/gwiki/src/ingest/git.rs:22-27]
[crates/gwiki/src/ingest/git.rs:30-55]
[crates/gwiki/src/ingest/git.rs:58-74]
[crates/gwiki/src/ingest/git.rs:77-109]

## API Symbols

- `GitFileSnapshot` (class) component `GitFileSnapshot [class]` (`31d7da91-e52c-56e2-b2b6-195f555ba05a`) lines 15-18 [crates/gwiki/src/ingest/git.rs:15-18]
  - Signature: `pub struct GitFileSnapshot {`
  - Purpose: 'GitFileSnapshot' is a simple data container holding a file path ('String') and the file contents as raw bytes ('Vec<u8>'). [crates/gwiki/src/ingest/git.rs:15-18]
- `GitRepositorySnapshot` (class) component `GitRepositorySnapshot [class]` (`87a82eb0-d930-5b8b-a202-53e8d4c5184a`) lines 22-27 [crates/gwiki/src/ingest/git.rs:22-27]
  - Signature: `pub struct GitRepositorySnapshot {`
  - Purpose: 'GitRepositorySnapshot' is a snapshot record of a Git repository’s state at a specific commit and time, containing the remote URL, commit SHA, fetch timestamp, and a collection of file snapshots. [crates/gwiki/src/ingest/git.rs:22-27]
- `ingest_repository` (function) component `ingest_repository [function]` (`b9293672-6ee0-5c09-b00b-f4a5a520a3ff`) lines 30-55 [crates/gwiki/src/ingest/git.rs:30-55]
  - Signature: `pub fn ingest_repository(`
  - Purpose: Validates that the snapshot contains at least one file, constructs a 'SourceDraft' for the Git repository snapshot using the remote URL, commit SHA, fetched timestamp, and content bytes, registers it in the manifest, renders markdown for the snapshot, and writes/indexes that content in the vault store. [crates/gwiki/src/ingest/git.rs:30-55]
- `snapshot_content_bytes` (function) component `snapshot_content_bytes [function]` (`8b196191-5c2c-5c16-8000-b7d923606856`) lines 58-74 [crates/gwiki/src/ingest/git.rs:58-74]
  - Signature: `fn snapshot_content_bytes(snapshot: &GitRepositorySnapshot) -> Vec<u8> {`
  - Purpose: Serializes a 'GitRepositorySnapshot' into a byte buffer by writing the remote URL and commit SHA as newline-separated headers, then appending each file as a '\n-- {path} --\n' delimiter followed by its raw bytes and a trailing newline if the file content does not already end with one. [crates/gwiki/src/ingest/git.rs:58-74]
- `render_git_markdown` (function) component `render_git_markdown [function]` (`3d83ef72-5f62-57f4-97a9-cc715df5bcd0`) lines 77-109 [crates/gwiki/src/ingest/git.rs:77-109]
  - Signature: `fn render_git_markdown(snapshot: &GitRepositorySnapshot, title: &str, source_hash: &str) -> String {`
  - Purpose: Builds a markdown document for a git repository snapshot by prepending source metadata, emitting a top-level title, and then rendering each file as a section with its path and UTF-8-lossy content inside a safely chosen code fence. [crates/gwiki/src/ingest/git.rs:77-109]
- `git_markdown_metadata` (function) component `git_markdown_metadata [function]` (`72e77782-501f-58ca-9e7b-387f3cdb2519`) lines 112-127 [crates/gwiki/src/ingest/git.rs:112-127]
  - Signature: `fn git_markdown_metadata(fields: &[(&str, String)]) -> String {`
  - Purpose: Builds a Git-style YAML frontmatter string from key/value pairs by single-line sanitizing each value, serializing the resulting mapping with 'serde_yaml', and wrapping it between '---' delimiters. [crates/gwiki/src/ingest/git.rs:112-127]
- `code_fence_info` (function) component `code_fence_info [function]` (`f185869d-e87e-54cf-b941-12ba58660fa8`) lines 130-142 [crates/gwiki/src/ingest/git.rs:130-142]
  - Signature: `fn code_fence_info(path: &str) -> String {`
  - Purpose: Returns the sanitized file extension from 'path' using only ASCII alphanumerics, '_', and '-' for a code-fence info string, or '"text"' if no valid non-empty extension exists. [crates/gwiki/src/ingest/git.rs:130-142]
- `markdown_code_fence` (function) component `markdown_code_fence [function]` (`3a8a5912-7ca0-5aac-baad-0ad8ba6f79bb`) lines 145-154 [crates/gwiki/src/ingest/git.rs:145-154]
  - Signature: `fn markdown_code_fence(text: &str) -> String {`
  - Purpose: Returns a Markdown code-fence string made of either backticks or tildes, choosing the delimiter with the shorter maximum run in 'text' and repeating it 'max_run + 1' times with a minimum length of 3. [crates/gwiki/src/ingest/git.rs:145-154]
- `bounded_max_run` (function) component `bounded_max_run [function]` (`c90da6b4-0423-5aea-b127-6df728cf8025`) lines 157-172 [crates/gwiki/src/ingest/git.rs:157-172]
  - Signature: `fn bounded_max_run(text: &str, delimiter: char) -> usize {`
  - Purpose: Counts the longest contiguous run of 'delimiter' characters in 'text', but clamps early to 'MAX_CODE_FENCE_LEN - 1' once the run length would make 'max_run + 1 >= MAX_CODE_FENCE_LEN'. [crates/gwiki/src/ingest/git.rs:157-172]
- `git_ingest_records_commit_provenance` (function) component `git_ingest_records_commit_provenance [function]` (`1ee2f603-9dcb-56da-b029-109200745032`) lines 181-236 [crates/gwiki/src/ingest/git.rs:181-236]
  - Signature: `fn git_ingest_records_commit_provenance() {`
  - Purpose: Verifies that 'ingest_repository' records Git repository provenance in the generated markdown by writing 'source_kind', remote URL, and commit SHA into frontmatter and including each snapshot file’s path and content. [crates/gwiki/src/ingest/git.rs:181-236]
- `code_fence_length_is_bounded_by_switching_delimiters` (function) component `code_fence_length_is_bounded_by_switching_delimiters [function]` (`5685732f-8c29-5557-a59d-04658106033d`) lines 239-247 [crates/gwiki/src/ingest/git.rs:239-247]
  - Signature: `fn code_fence_length_is_bounded_by_switching_delimiters() {`
  - Purpose: Verifies that 'markdown_code_fence' bounds the generated fence length at three characters by switching to '~~~' when needed, even for inputs consisting of very long runs of apostrophes or tildes. [crates/gwiki/src/ingest/git.rs:239-247]
- `code_fence_length_is_clamped_when_both_delimiters_are_saturated` (function) component `code_fence_length_is_clamped_when_both_delimiters_are_saturated [function]` (`e9d92190-3075-51ce-94d2-aed5c9e5e93c`) lines 250-261 [crates/gwiki/src/ingest/git.rs:250-261]
  - Signature: `fn code_fence_length_is_clamped_when_both_delimiters_are_saturated() {`
  - Purpose: Verifies that 'markdown_code_fence' clamps the generated fence to 'MAX_CODE_FENCE_LEN' and uses only apostrophes when both candidate delimiters are fully saturated by the input. [crates/gwiki/src/ingest/git.rs:250-261]

