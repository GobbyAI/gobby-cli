---
title: crates/gwiki/src/video/write.rs
type: code_file
provenance:
- file: crates/gwiki/src/video/write.rs
  ranges:
  - 9-65
  - 67-77
  - 79-98
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/video/write.rs:9-65](crates/gwiki/src/video/write.rs#L9-L65), [crates/gwiki/src/video/write.rs:67-77](crates/gwiki/src/video/write.rs#L67-L77), [crates/gwiki/src/video/write.rs:79-98](crates/gwiki/src/video/write.rs#L79-L98)

</details>

# crates/gwiki/src/video/write.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Provides an atomic write path for video-derived markdown files: it creates a temporary sibling file, writes and fsyncs the bytes, then renames it into place so the target is replaced safely. The helper functions choose a temporary filename next to the destination and sync the parent directory afterward to make the rename durable, with special handling for existing targets and cleanup on failure.
[crates/gwiki/src/video/write.rs:9-65]
[crates/gwiki/src/video/write.rs:67-77]
[crates/gwiki/src/video/write.rs:79-98]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `write_video_markdown_atomic` | function | `pub(super) fn write_video_markdown_atomic(path: &Path, bytes: &[u8]) -> Result<(), WikiError> {` | `write_video_markdown_atomic [function]` | `eeefc41f-ce3c-5f36-8395-c52b9dce3854` | 9-65 [crates/gwiki/src/video/write.rs:9-65] | Indexed function `write_video_markdown_atomic` in `crates/gwiki/src/video/write.rs`. [crates/gwiki/src/video/write.rs:9-65] |
| `temp_sibling_path` | function | `fn temp_sibling_path(path: &Path) -> PathBuf {` | `temp_sibling_path [function]` | `82f22277-4b79-50ad-bddd-1aa65100561f` | 67-77 [crates/gwiki/src/video/write.rs:67-77] | Indexed function `temp_sibling_path` in `crates/gwiki/src/video/write.rs`. [crates/gwiki/src/video/write.rs:67-77] |
| `sync_parent_dir` | function | `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {` | `sync_parent_dir [function]` | `20d24412-1afe-5535-952f-2b26a5764613` | 79-98 [crates/gwiki/src/video/write.rs:79-98] | Indexed function `sync_parent_dir` in `crates/gwiki/src/video/write.rs`. [crates/gwiki/src/video/write.rs:79-98] |
