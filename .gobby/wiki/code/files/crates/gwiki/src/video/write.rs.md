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

# crates/gwiki/src/video/write.rs

Module: [[code/modules/crates/gwiki/src/video|crates/gwiki/src/video]]

## Purpose

Provides atomic writing for video-derived markdown files: it stages bytes in a unique hidden temp file beside the target, flushes and syncs the temp file, then renames it into place with overwrite handling and cleanup on any I/O failure. The helper `temp_sibling_path` builds the sibling temp filename from the target’s basename plus process/time entropy, and `sync_parent_dir` persists the containing directory on Unix after the rename while remaining a no-op on other platforms.
[crates/gwiki/src/video/write.rs:9-65]
[crates/gwiki/src/video/write.rs:67-77]
[crates/gwiki/src/video/write.rs:79-98]

## API Symbols

- `write_video_markdown_atomic` (function) component `write_video_markdown_atomic [function]` (`eeefc41f-ce3c-5f36-8395-c52b9dce3854`) lines 9-65 [crates/gwiki/src/video/write.rs:9-65]
  - Signature: `pub(super) fn write_video_markdown_atomic(path: &Path, bytes: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Atomically writes 'bytes' to 'path' by creating a unique sibling temp file, fully flushing and syncing it, renaming it into place with overwrite handling, and cleaning up temp artifacts on any I/O error. [crates/gwiki/src/video/write.rs:9-65]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`82f22277-4b79-50ad-bddd-1aa65100561f`) lines 67-77 [crates/gwiki/src/video/write.rs:67-77]
  - Signature: `fn temp_sibling_path(path: &Path) -> PathBuf {`
  - Purpose: Constructs a temporary sibling 'PathBuf' by replacing the input path’s filename with a hidden name of the form '.{original_name}.{process_id}.{unix_nanos}.tmp', defaulting 'original_name' to 'video.md' if the path has no valid UTF-8 filename. [crates/gwiki/src/video/write.rs:67-77]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`20d24412-1afe-5535-952f-2b26a5764613`) lines 79-98 [crates/gwiki/src/video/write.rs:79-98]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: On Unix, this function attempts to open 'path'’s parent directory and 'sync_all' it, returning a 'WikiError::Io' on failure, while on non-Unix platforms it is a no-op that always returns 'Ok(())'. [crates/gwiki/src/video/write.rs:79-98]

