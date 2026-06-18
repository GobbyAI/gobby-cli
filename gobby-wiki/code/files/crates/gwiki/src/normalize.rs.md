---
title: crates/gwiki/src/normalize.rs
type: code_file
provenance:
- file: crates/gwiki/src/normalize.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/normalize.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/normalize.rs` exposes 14 indexed API symbols.

## How it fits

`crates/gwiki/src/normalize.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `NormalizeReport` | class | 'NormalizeReport' is a summary record for a normalization run, capturing the invoked command, target scope and root path, the number of authored Markdown files scanned, the relative paths that changed or would change under check mode, and whether the run was check-only. [crates/gwiki/src/normalize.rs:37-47] |
| `run` | function | Scans authored Markdown files under the vault root, normalizes each file’s contents, optionally writes back any differences atomically when 'check_only' is false, and returns a 'NormalizeReport' listing the scanned and changed relative paths. [crates/gwiki/src/normalize.rs:54-103] |
| `render_text` | function | Formats a 'NormalizeReport' into a plain-text summary showing the scope, number of scanned files, and either the number of files that “need normalization” or were “normalized,” followed by a '-'-prefixed list of changed file paths. [crates/gwiki/src/normalize.rs:106-125] |
| `check_exit_code` | function | Returns '1' when 'report.check_only' is true and 'report.changed' is non-empty, otherwise returns '0'. [crates/gwiki/src/normalize.rs:131-137] |
| `collect_markdown` | function | Recursively traverses 'directory', collecting paths of files whose names satisfy 'is_markdown_path' into 'files', ignoring missing directories and otherwise propagating I/O errors as 'WikiError::Io'. [crates/gwiki/src/normalize.rs:141-172] |
| `is_markdown_path` | function | Returns 'true' when the path has an extension that, after UTF-8 conversion and ASCII lowercasing, is exactly 'md' or 'markdown'; otherwise returns 'false'. [crates/gwiki/src/normalize.rs:174-180] |
| `write` | function | Joins 'relative' to 'root', creates the target file’s parent directory tree, and writes 'contents' to the resulting path, panicking on any I/O failure. [crates/gwiki/src/normalize.rs:186-190] |
| `normalizes_authored_docs_and_leaves_raw_captures_untouched` | function | Verifies that normalization rewrites authored Markdown docs in-scope ('knowledge/concepts/dirty.md' and 'code/INDEX.md') while excluding 'raw/<id>.md' captures from scanning, rewriting, and 'report.changed', preserving their bytes exactly. [crates/gwiki/src/normalize.rs:195-240] |
| `is_idempotent` | function | Creates a temporary topic tree with a dirty markdown file, runs normalization twice for 'ScopeIdentity::topic("ops")', and verifies the first pass reports one change while the second pass is idempotent and reports none. [crates/gwiki/src/normalize.rs:243-257] |
| `check_mode_reports_without_writing` | function | Verifies that running 'run' in check mode for the 'ops' topic reports 'knowledge/topics/page.md' as changed, sets 'report.check_only' to true, and leaves the dirty file unmodified on disk. [crates/gwiki/src/normalize.rs:260-277] |
| `normalizes_vault_root_stub_files` | function | Creates a temporary vault root containing '_index.md' and 'log.md' stub Markdown files with extra trailing blank lines, runs 'normalize', and verifies both files are reported as changed. [crates/gwiki/src/normalize.rs:280-290] |
| `report_with` | function | Constructs and returns a 'NormalizeReport' for the '"normalize"' command in the '"ops"' scope rooted at '/tmp/vault', recording the provided 'changed' paths, their count, and the 'check_only' flag. [crates/gwiki/src/normalize.rs:292-301] |
| `render_text_summarizes_changed_paths` | function | Verifies that 'render_text' for a report with two changed paths includes the normalization count and lists both paths as bullet items in the rendered text. [crates/gwiki/src/normalize.rs:304-315] |
| `check_exit_code_gates_only_dirty_check_runs` | function | Verifies that 'check_exit_code' returns '1' only for dirty check runs, and returns '0' for both clean check runs and dirty write runs that modify files in place. [crates/gwiki/src/normalize.rs:318-331] |

