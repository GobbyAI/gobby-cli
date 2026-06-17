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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/ingest/git.rs:15-18](crates/gwiki/src/ingest/git.rs#L15-L18), [crates/gwiki/src/ingest/git.rs:22-27](crates/gwiki/src/ingest/git.rs#L22-L27), [crates/gwiki/src/ingest/git.rs:30-55](crates/gwiki/src/ingest/git.rs#L30-L55), [crates/gwiki/src/ingest/git.rs:58-74](crates/gwiki/src/ingest/git.rs#L58-L74), [crates/gwiki/src/ingest/git.rs:77-109](crates/gwiki/src/ingest/git.rs#L77-L109), [crates/gwiki/src/ingest/git.rs:112-127](crates/gwiki/src/ingest/git.rs#L112-L127), [crates/gwiki/src/ingest/git.rs:130-142](crates/gwiki/src/ingest/git.rs#L130-L142), [crates/gwiki/src/ingest/git.rs:145-154](crates/gwiki/src/ingest/git.rs#L145-L154), [crates/gwiki/src/ingest/git.rs:157-172](crates/gwiki/src/ingest/git.rs#L157-L172), [crates/gwiki/src/ingest/git.rs:181-236](crates/gwiki/src/ingest/git.rs#L181-L236), [crates/gwiki/src/ingest/git.rs:239-247](crates/gwiki/src/ingest/git.rs#L239-L247), [crates/gwiki/src/ingest/git.rs:250-261](crates/gwiki/src/ingest/git.rs#L250-L261)

</details>

# crates/gwiki/src/ingest/git.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file turns a selected Git repository snapshot into a wiki ingest record and markdown document. `GitFileSnapshot` and `GitRepositorySnapshot` model the input snapshot, `ingest_repository` validates that at least one file is present, registers the snapshot as a `SourceDraft`/`SourceManifest`, renders markdown, and writes it into the index store. The helper functions build stable snapshot bytes for content hashing, format the markdown and its metadata, and choose a bounded code-fence delimiter so embedded file content stays renderable even when backticks appear in the source.
[crates/gwiki/src/ingest/git.rs:15-18]
[crates/gwiki/src/ingest/git.rs:22-27]
[crates/gwiki/src/ingest/git.rs:30-55]
[crates/gwiki/src/ingest/git.rs:58-74]
[crates/gwiki/src/ingest/git.rs:77-109]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GitFileSnapshot` | class | `pub struct GitFileSnapshot {` | `GitFileSnapshot [class]` | `31d7da91-e52c-56e2-b2b6-195f555ba05a` | 15-18 [crates/gwiki/src/ingest/git.rs:15-18] | Indexed class `GitFileSnapshot` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:15-18] |
| `GitRepositorySnapshot` | class | `pub struct GitRepositorySnapshot {` | `GitRepositorySnapshot [class]` | `87a82eb0-d930-5b8b-a202-53e8d4c5184a` | 22-27 [crates/gwiki/src/ingest/git.rs:22-27] | Indexed class `GitRepositorySnapshot` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:22-27] |
| `ingest_repository` | function | `pub fn ingest_repository(` | `ingest_repository [function]` | `b9293672-6ee0-5c09-b00b-f4a5a520a3ff` | 30-55 [crates/gwiki/src/ingest/git.rs:30-55] | Indexed function `ingest_repository` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:30-55] |
| `snapshot_content_bytes` | function | `fn snapshot_content_bytes(snapshot: &GitRepositorySnapshot) -> Vec<u8> {` | `snapshot_content_bytes [function]` | `8b196191-5c2c-5c16-8000-b7d923606856` | 58-74 [crates/gwiki/src/ingest/git.rs:58-74] | Indexed function `snapshot_content_bytes` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:58-74] |
| `render_git_markdown` | function | `fn render_git_markdown(snapshot: &GitRepositorySnapshot, title: &str, source_hash: &str) -> String {` | `render_git_markdown [function]` | `3d83ef72-5f62-57f4-97a9-cc715df5bcd0` | 77-109 [crates/gwiki/src/ingest/git.rs:77-109] | Indexed function `render_git_markdown` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:77-109] |
| `git_markdown_metadata` | function | `fn git_markdown_metadata(fields: &[(&str, String)]) -> String {` | `git_markdown_metadata [function]` | `72e77782-501f-58ca-9e7b-387f3cdb2519` | 112-127 [crates/gwiki/src/ingest/git.rs:112-127] | Indexed function `git_markdown_metadata` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:112-127] |
| `code_fence_info` | function | `fn code_fence_info(path: &str) -> String {` | `code_fence_info [function]` | `f185869d-e87e-54cf-b941-12ba58660fa8` | 130-142 [crates/gwiki/src/ingest/git.rs:130-142] | Indexed function `code_fence_info` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:130-142] |
| `markdown_code_fence` | function | `fn markdown_code_fence(text: &str) -> String {` | `markdown_code_fence [function]` | `3a8a5912-7ca0-5aac-baad-0ad8ba6f79bb` | 145-154 [crates/gwiki/src/ingest/git.rs:145-154] | Indexed function `markdown_code_fence` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:145-154] |
| `bounded_max_run` | function | `fn bounded_max_run(text: &str, delimiter: char) -> usize {` | `bounded_max_run [function]` | `c90da6b4-0423-5aea-b127-6df728cf8025` | 157-172 [crates/gwiki/src/ingest/git.rs:157-172] | Indexed function `bounded_max_run` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:157-172] |
| `git_ingest_records_commit_provenance` | function | `fn git_ingest_records_commit_provenance() {` | `git_ingest_records_commit_provenance [function]` | `1ee2f603-9dcb-56da-b029-109200745032` | 181-236 [crates/gwiki/src/ingest/git.rs:181-236] | Indexed function `git_ingest_records_commit_provenance` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:181-236] |
| `code_fence_length_is_bounded_by_switching_delimiters` | function | `fn code_fence_length_is_bounded_by_switching_delimiters() {` | `code_fence_length_is_bounded_by_switching_delimiters [function]` | `5685732f-8c29-5557-a59d-04658106033d` | 239-247 [crates/gwiki/src/ingest/git.rs:239-247] | Indexed function `code_fence_length_is_bounded_by_switching_delimiters` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:239-247] |
| `code_fence_length_is_clamped_when_both_delimiters_are_saturated` | function | `fn code_fence_length_is_clamped_when_both_delimiters_are_saturated() {` | `code_fence_length_is_clamped_when_both_delimiters_are_saturated [function]` | `e9d92190-3075-51ce-94d2-aed5c9e5e93c` | 250-261 [crates/gwiki/src/ingest/git.rs:250-261] | Indexed function `code_fence_length_is_clamped_when_both_delimiters_are_saturated` in `crates/gwiki/src/ingest/git.rs`. [crates/gwiki/src/ingest/git.rs:250-261] |
