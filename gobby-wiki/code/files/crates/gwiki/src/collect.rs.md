---
title: crates/gwiki/src/collect.rs
type: code_file
provenance:
- file: crates/gwiki/src/collect.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/collect.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/collect.rs` exposes 43 indexed API symbols.

## How it fits

`crates/gwiki/src/collect.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CollectReport` | class | 'CollectReport' is a Rust struct that records the outcome of a collection operation by separating 'CollectAction' values into 'accepted' and 'skipped' vectors. [crates/gwiki/src/collect.rs:18-21] |
| `CollectAction` | class | 'CollectAction' is a Rust data structure representing a collection operation, containing the target inbox path, current collection status, an optional kind label, an optional raw source path, and an optional reason string. [crates/gwiki/src/collect.rs:24-30] |
| `CollectStatus` | type | Indexed type `CollectStatus` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:34-37] |
| `InboxKind` | type | Indexed type `InboxKind` in `crates/gwiki/src/collect.rs`. [crates/gwiki/src/collect.rs:39-42] |
| `collect_inbox` | function | Forwards 'vault_root' and 'fetched_at' to 'collect_inbox_with_limit', using the inbox item byte limit from the environment, and returns its 'Result<CollectReport, WikiError>'. [crates/gwiki/src/collect.rs:44-46] |
| `collect_inbox_with_limit` | function | 'collect_inbox_with_limit' scans 'vault_root/inbox' in sorted order, skips status sidecars and unsupported or oversized entries, and attempts to collect each remaining file into a 'CollectReport' using a per-item byte limit. [crates/gwiki/src/collect.rs:48-140] |
| `collect_inbox_and_index` | function | Collects inbox items from 'vault_root' at 'fetched_at', and if any were accepted, rebuilds the wiki index via 'index_after_ingest' before returning the resulting 'CollectReport'. [crates/gwiki/src/collect.rs:142-152] |
| `read_inbox_item_limited` | function | Opens the file at 'path', reads at most 'max_item_bytes + 1' bytes into memory, and returns 'Ok(Some(bytes))' if the file size is within 'max_item_bytes' or 'Ok(None)' if it exceeds that limit, mapping any I/O failure to 'WikiError'. [crates/gwiki/src/collect.rs:154-165] |
| `ensure_collect_paths` | function | Creates the 'inbox', 'raw', and 'raw/assets' directories under 'vault_root' if missing, and initializes 'log.md' with '# Log\n\n' when it does not already exist. [crates/gwiki/src/collect.rs:167-179] |
| `classify_inbox_item` | function | 'classify_inbox_item' inspects the lowercased file extension from 'path' and, for recognized link extensions, extensionless content, or specific media/document extensions, classifies the item as 'InboxKind::Url' by extracting an HTTP(S) URL from the UTF-8-lossy bytes or as 'InboxKind::File' with a matching 'SourceKind' variant, otherwise defaulting to 'SourceKind::File' or returning a static error when a URL cannot be extracted. [crates/gwiki/src/collect.rs:181-204] |
| `accept_item` | function | 'accept_item' records an inbox item into the vault by reading the current manifest, registering a new source draft, emitting raw markdown for URL items, and rolling back any partial registration on write failure. [crates/gwiki/src/collect.rs:206-327] |
| `rollback_registered_collect_source` | function | 'rollback_registered_collect_source' cleans up any partially written raw/asset files, restores the previous source manifest in 'vault_root', and then returns the original collection error augmented with any cleanup failures, or a config error if manifest rollback itself fails. [crates/gwiki/src/collect.rs:329-352] |
| `cleanup_collect_file` | function | Attempts to delete the file at 'vault_root.join(relative_path)', ignores 'NotFound' errors, and appends any other removal error to 'cleanup_errors' as a formatted path-prefixed message. [crates/gwiki/src/collect.rs:354-361] |
| `collect_error_with_cleanup` | function | 'collect_error_with_cleanup' returns the original 'WikiError' unchanged when there are no cleanup errors, otherwise appends a formatted cleanup-detail string to the error and rewraps it as a 'WikiError' variant, preserving 'std::io::ErrorKind' for 'Io' errors. [crates/gwiki/src/collect.rs:363-390] |
| `collect_cleanup_detail` | function | Returns an empty string when 'cleanup_errors' is empty, otherwise formats the errors into a semicolon-prefixed suffix of the form '; cleanup failures: <error1>; <error2>; ...'. [crates/gwiki/src/collect.rs:392-398] |
| `skip_item` | function | Creates a 'CollectAction' marked 'Skipped' with the provided relative path and reason, writes it as a status sidecar under 'vault_root' for 'path', appends it to 'report.skipped', and returns 'Ok(())' or propagates any 'WikiError' from sidecar writing. [crates/gwiki/src/collect.rs:400-418] |
| `render_url_markdown` | function | Builds a markdown string with URL source metadata ('source_kind', 'source_url', 'fetched_at', 'source_hash') and a simple body containing an H1 title and a “Captured URL” line for the given 'url'. [crates/gwiki/src/collect.rs:420-433] |
| `render_file_markdown` | function | Builds a Markdown string with metadata front matter for the source, emits an '#' title, appends UTF-8 text content for 'Markdown'/'Text' inputs or a note about the stored original artifact for other kinds, and returns the assembled document. [crates/gwiki/src/collect.rs:435-480] |
| `write_status_sidecar` | function | Writes a pretty-printed JSON sidecar file at 'status_sidecar_path(path)' containing the action’s inbox item path, status, reason, and 'checked_at' timestamp, mapping serialization and write failures into 'WikiError'/I/O errors. [crates/gwiki/src/collect.rs:482-501] |
| `append_log` | function | Appends a Markdown-formatted entry to 'vault_root/log.md', creating the file and writing a '# Log' header if it is empty, then recording each accepted and skipped item from 'report' with the 'fetched_at' timestamp and returning any I/O error as 'WikiError'. [crates/gwiki/src/collect.rs:503-550] |
| `extract_url` | function | Scans non-empty trimmed lines of 'text' and returns the first valid HTTP URL found, accepting either a 'URL=' prefix, a line that is itself a valid HTTP URL, or the first URL extracted from embedded text. [crates/gwiki/src/collect.rs:552-572] |
| `urls_from_embedded_text` | function | Scans the input text for embedded 'http://' or 'https://' substrings, tokenizes each candidate URL up to whitespace or angle/quote delimiters, validates it with 'parse_embedded_http_url', and returns all successfully parsed URLs as a 'Vec<String>'. [crates/gwiki/src/collect.rs:574-588] |
| `is_http_url` | function | Returns 'true' if 'parse_http_url(value)' successfully parses the input as an HTTP URL, and 'false' otherwise. [crates/gwiki/src/collect.rs:590-592] |
| `parse_embedded_http_url` | function | Returns the first valid HTTP URL found in 'candidate', preferring a version with trailing URL punctuation trimmed, otherwise falling back to the original string or a minimally punctuation-trimmed suffix, and yields it as an owned 'String'. [crates/gwiki/src/collect.rs:594-604] |

_9 more symbol(s) not shown — run `gcode outline crates/gwiki/src/collect.rs` for the full list._

_Verified by 10 in-file unit tests._

