---
title: crates/gwiki/src/compile/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/compile/render.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/compile/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_bundle` | function | Formats a 'CompileBundle' into a Markdown string containing the bundle topic, topic outline, accepted sources with nested chunks, citations, conflicting claims, and missing evidence. [crates/gwiki/src/compile/render.rs:11-47] |
| `render_list_section` | function | Appends a markdown section header and either a '- None recorded.' placeholder for empty input or a bulleted list of the provided strings, followed by a trailing blank line, to 'rendered'. [crates/gwiki/src/compile/render.rs:49-63] |
| `write_target_page` | function | Creates a new target page file inside the vault after validating and creating its parent directory, and writes the rendered content to it, returning a 'WikiError' if the path is invalid, the file already exists, or any I/O operation fails. [crates/gwiki/src/compile/render.rs:65-105] |
| `ensure_compile_target_parent_inside_vault` | function | Validates that the canonicalized parent directory of a compile target is inside the canonicalized vault root by walking up through nonexistent ancestors until an existing path is found, returning 'InvalidInput' if it escapes the vault and 'Io' on resolution errors. [crates/gwiki/src/compile/render.rs:107-144] |
| `normalize_target_page` | function | Converts an optional vault-relative 'target_page' path into an absolute 'vault_root.join(...)' 'PathBuf' after rejecting absolute paths, '..'/root/prefix escapes, and empty normalized paths, otherwise returning 'None' unchanged. [crates/gwiki/src/compile/render.rs:146-182] |
| `slugify` | function | Returns a slug string for 'topic' by delegating to 'slugify_with_options(topic, Some("handoff"), None)', using '"handoff"' as the default option. [crates/gwiki/src/compile/render.rs:184-186] |
| `unix_timestamp_ms` | function | Returns the current Unix timestamp in milliseconds by delegating to 'time::unix_timestamp_ms()', propagating any 'WikiError' from that call. [crates/gwiki/src/compile/render.rs:188-190] |

