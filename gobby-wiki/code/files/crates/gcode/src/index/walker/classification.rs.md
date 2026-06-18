---
title: crates/gcode/src/index/walker/classification.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/classification.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/classification.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Overview

`crates/gcode/src/index/walker/classification.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gcode/src/index/walker/classification.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `classify_file` | function | Returns 'None' for unsafe, generated, or bundled files, otherwise classifies hidden metadata as 'ContentOnly' and detected source/data-language files as 'Ast' except oversized data-language files and undetected text, which are downgraded to 'ContentOnly'. [crates/gcode/src/index/walker/classification.rs:15-52] |
| `classify_explicit_file_with_options` | function | Returns 'None' if 'options.respect_gitignore' is enabled and the explicit 'path' is not visible under 'root', otherwise delegates to 'classify_file(root, path, exclude_patterns)' and returns its 'Option<FileClassification>' result. [crates/gcode/src/index/walker/classification.rs:56-66] |
| `is_content_indexable` | function | Returns 'true' when 'classify_file(root, path, exclude_patterns)' yields 'Some(FileClassification::ContentOnly)', and 'false' otherwise. [crates/gcode/src/index/walker/classification.rs:69-78] |
| `content_language` | function | Returns the lowercase file extension from 'path' as the content language, defaulting to '"text"' when no extension exists and normalizing 'md'/'markdown' to '"markdown"' and 'yml'/'yaml' to '"yaml"'. [crates/gcode/src/index/walker/classification.rs:81-93] |
| `explicit_path_visible` | function | Returns 'false' for hidden paths not matched by the root allowlist, otherwise checks whether the exact 'path' exists as a file by walking its parent directory with the configured gitignore and size limits at depth 1 and comparing entries via 'same_existing_path'. [crates/gcode/src/index/walker/classification.rs:95-111] |
| `same_existing_path` | function | Returns 'true' if 'left' and 'right' resolve to the same canonical filesystem path when possible, otherwise comparing their original path values as 'PathBuf's. [crates/gcode/src/index/walker/classification.rs:113-117] |
| `is_safe_text_file` | function | Returns 'true' only for regular files under 'root' that pass path and symlink safety checks, are not excluded or secret-bearing, have readable metadata with nonzero size no larger than 'MAX_FILE_SIZE', and are not detected as binary. [crates/gcode/src/index/walker/classification.rs:119-144] |

