---
title: crates/gwiki/src/ingest/git.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/git.rs
  ranges:
  - 13-16
  - 19-24
  - 26-51
  - 53-69
  - 71-103
  - 105-120
  - 122-134
  - 136-145
  - 147-162
  - 171-226
  - 229-237
  - 240-251
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/git.rs

Module: [[code/modules/crates/gwiki/src/ingest|crates/gwiki/src/ingest]]

## Purpose

`crates/gwiki/src/ingest/git.rs` exposes 12 indexed API symbols.
[crates/gwiki/src/ingest/git.rs:13-16]
[crates/gwiki/src/ingest/git.rs:19-24]
[crates/gwiki/src/ingest/git.rs:26-51]
[crates/gwiki/src/ingest/git.rs:53-69]
[crates/gwiki/src/ingest/git.rs:71-103]

## API Symbols

- `GitFileSnapshot` (class) component `GitFileSnapshot [class]` (`b14e84bf-18b3-5d2f-9d83-8e50e9e17425`) lines 13-16 [crates/gwiki/src/ingest/git.rs:13-16]
  - Signature: `pub struct GitFileSnapshot {`
  - Purpose: `GitFileSnapshot` is a struct that pairs a file path with its binary content (as a byte vector) to represent a point-in-time snapshot of a file from a Git repository. [crates/gwiki/src/ingest/git.rs:13-16]
- `GitRepositorySnapshot` (class) component `GitRepositorySnapshot [class]` (`eab30da7-60a6-5139-9332-3440c0349236`) lines 19-24 [crates/gwiki/src/ingest/git.rs:19-24]
  - Signature: `pub struct GitRepositorySnapshot {`
  - Purpose: `GitRepositorySnapshot` is a struct that captures an immutable snapshot of a remote Git repository at a specific commit, containing the remote URL, commit SHA, fetch timestamp, and its associated files. [crates/gwiki/src/ingest/git.rs:19-24]
- `ingest_repository` (function) component `ingest_repository [function]` (`7b9f7cc6-784e-5302-9820-5946293b3d73`) lines 26-51 [crates/gwiki/src/ingest/git.rs:26-51]
  - Signature: `pub fn ingest_repository(`
  - Purpose: Ingests a git repository snapshot by registering it as a versioned source manifest, rendering its contents as markdown, and indexing the result in a wiki store. [crates/gwiki/src/ingest/git.rs:26-51]
- `snapshot_content_bytes` (function) component `snapshot_content_bytes [function]` (`68e3660d-20f0-5aa9-b9c9-a3e5a9bc5971`) lines 53-69 [crates/gwiki/src/ingest/git.rs:53-69]
  - Signature: `fn snapshot_content_bytes(snapshot: &GitRepositorySnapshot) -> Vec<u8> {`
  - Purpose: Serializes a GitRepositorySnapshot to a byte vector containing the remote URL, commit SHA, and each file's path and contents separated by newlines. [crates/gwiki/src/ingest/git.rs:53-69]
- `render_git_markdown` (function) component `render_git_markdown [function]` (`189d95d2-2e72-5ab0-89b3-025cd59efe38`) lines 71-103 [crates/gwiki/src/ingest/git.rs:71-103]
  - Signature: `fn render_git_markdown(snapshot: &GitRepositorySnapshot, title: &str, source_hash: &str) -> String {`
  - Purpose: Serializes a `GitRepositorySnapshot` to a markdown document containing git repository metadata (remote, commit SHA, fetch timestamp) and all source files formatted within code fences. [crates/gwiki/src/ingest/git.rs:71-103]
- `git_markdown_metadata` (function) component `git_markdown_metadata [function]` (`0ba11fa7-0032-51b6-987f-14d4a89683a4`) lines 105-120 [crates/gwiki/src/ingest/git.rs:105-120]
  - Signature: `fn git_markdown_metadata(fields: &[(&str, String)]) -> String {`
  - Purpose: Converts a slice of key-value field tuples into YAML-formatted markdown frontmatter wrapped with triple-dash delimiters. [crates/gwiki/src/ingest/git.rs:105-120]
- `code_fence_info` (function) component `code_fence_info [function]` (`07596048-983f-5302-a271-1233b52e10e3`) lines 122-134 [crates/gwiki/src/ingest/git.rs:122-134]
  - Signature: `fn code_fence_info(path: &str) -> String {`
  - Purpose: Extracts a file extension from a path and returns it as a sanitized code fence language specifier by retaining only ASCII alphanumeric characters, hyphens, and underscores, defaulting to "text" if absent or empty. [crates/gwiki/src/ingest/git.rs:122-134]
- `markdown_code_fence` (function) component `markdown_code_fence [function]` (`de073625-b801-58d6-b5b6-a175827945d8`) lines 136-145 [crates/gwiki/src/ingest/git.rs:136-145]
  - Signature: `fn markdown_code_fence(text: &str) -> String {`
  - Purpose: Generates a markdown code fence delimiter by selecting backticks or tildes based on which has the smaller maximum consecutive run in the input text, then repeating the selected delimiter for a length exceeding that maximum run (with a minimum of 3 characters) to prevent conflicts with the fenced content. [crates/gwiki/src/ingest/git.rs:136-145]
- `bounded_max_run` (function) component `bounded_max_run [function]` (`2f7fbea6-b137-5b6b-a739-e27ed1d6ba8c`) lines 147-162 [crates/gwiki/src/ingest/git.rs:147-162]
  - Signature: `fn bounded_max_run(text: &str, delimiter: char) -> usize {`
  - Purpose: Returns the length of the longest consecutive sequence of the delimiter character in the input string, bounded by `MAX_CODE_FENCE_LEN - 1`. [crates/gwiki/src/ingest/git.rs:147-162]
- `git_ingest_records_commit_provenance` (function) component `git_ingest_records_commit_provenance [function]` (`f95d4dc4-c452-5f89-ae97-e0a91fe221a5`) lines 171-226 [crates/gwiki/src/ingest/git.rs:171-226]
  - Signature: `fn git_ingest_records_commit_provenance() {`
  - Purpose: This test function verifies that `ingest_repository()` correctly ingests a Git repository snapshot into markdown files with YAML frontmatter containing provenance metadata (source_kind, remote URL, commit SHA) and repository file contents. [crates/gwiki/src/ingest/git.rs:171-226]
- `code_fence_length_is_bounded_by_switching_delimiters` (function) component `code_fence_length_is_bounded_by_switching_delimiters [function]` (`896eb075-9c0d-56be-adae-ac766442456e`) lines 229-237 [crates/gwiki/src/ingest/git.rs:229-237]
  - Signature: `fn code_fence_length_is_bounded_by_switching_delimiters() {`
  - Purpose: Verifies that `markdown_code_fence()` bounds output fence length to 3 characters by switching delimiters (backticks ↔ tildes) when input sequences exceed MAX_CODE_FENCE_LEN. [crates/gwiki/src/ingest/git.rs:229-237]
- `code_fence_length_is_clamped_when_both_delimiters_are_saturated` (function) component `code_fence_length_is_clamped_when_both_delimiters_are_saturated [function]` (`6a9550e2-42a1-5b58-a633-68fac544fa19`) lines 240-251 [crates/gwiki/src/ingest/git.rs:240-251]
  - Signature: `fn code_fence_length_is_clamped_when_both_delimiters_are_saturated() {`
  - Purpose: This test verifies that `markdown_code_fence()` clamps the generated fence length to `MAX_CODE_FENCE_LEN` and selects backticks as the delimiter when both backtick and tilde candidates exceed the maximum allowed length. [crates/gwiki/src/ingest/git.rs:240-251]

