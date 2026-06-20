---
title: crates/gwiki/src/commands/read.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/read.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/read.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/read.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/read.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the command scope, derives its identity for output, reads either a path or title from the scope root based on 'target', and renders the resulting content into a 'CommandOutcome' or returns a 'WikiError'. [crates/gwiki/src/commands/read.rs:17-28] |
| `read_path` | function | 'read_path' normalizes and validates a requested wiki-relative path, returns an invalid-request or not-found 'ReadOutput' on failure, and otherwise delegates to 'read_existing_path' for an existing file under 'root'. [crates/gwiki/src/commands/read.rs:30-57] |
| `read_title` | function | Validates that 'title' is non-empty, resolves matching wiki documents under 'root' for the given 'scope', and returns an invalid-request, not-found, ambiguous, or single-document 'ReadOutput' depending on how many sorted candidates are found. [crates/gwiki/src/commands/read.rs:59-85] |
| `read_existing_path` | function | Resolves 'wiki_path' under 'root', stats the file to obtain its byte length, reads at most the configured markdown prefix, derives the first heading as the title, and returns a 'ReadOutput::found' with the content and truncation metadata or a wrapped I/O error if stat fails. [crates/gwiki/src/commands/read.rs:87-114] |
| `configured_read_max_bytes` | function | Returns the positive 'usize' value from the 'READ_MAX_BYTES_ENV' environment variable if it is set and parses successfully, otherwise falls back to 'DEFAULT_READ_MAX_BYTES'. [crates/gwiki/src/commands/read.rs:116-122] |
| `read_markdown_prefix` | function | Opens the file at 'path', reads up to 'max_bytes' plus one extra byte into memory, truncates back to a valid UTF-8 prefix if the read exceeded 'max_bytes', and returns the resulting 'String' with a 'bool' indicating whether truncation occurred, mapping all I/O and decoding failures to 'WikiError::Io'. [crates/gwiki/src/commands/read.rs:124-152] |
| `normalize_requested_path` | function | Validates and canonicalizes a requested path by rejecting absolute paths and any '..', root, or prefix components, stripping '.' segments, and returning a non-empty vault-relative 'PathBuf' or an 'invalid_request' degradation error. [crates/gwiki/src/commands/read.rs:154-181] |
| `readable_path_degradation` | function | Returns 'None' only for canonical readable wiki paths ending in '.md' that satisfy 'is_readable_wiki_path', otherwise returns 'Some(ReadDegradation::invalid_request(...))' indicating either a non-Markdown path or a non-canonical wiki document. [crates/gwiki/src/commands/read.rs:183-197] |
| `is_readable_wiki_path` | function | Returns 'true' only for the exact paths 'raw/INDEX.md', '_index.md', or 'log.md', or for normalized paths whose components start with 'knowledge/sources', 'knowledge/concepts', 'knowledge/topics', or 'code'; otherwise returns 'false'. [crates/gwiki/src/commands/read.rs:199-211] |
| `title_candidates` | function | Returns the result of 'title_candidates_with_scan_budget(root, title, max_results, MAX_TITLE_SCAN_ENTRIES)', i.e. a 'Result<Vec<ReadCandidate>, WikiError>' containing up to 'max_results' title-based read candidates scanned from 'root'. [crates/gwiki/src/commands/read.rs:213-219] |
| `title_candidates_with_scan_budget` | function | Initializes a bounded title-candidate search over 'root' by configuring scan and result limits, recursively collecting matching 'ReadCandidate's via 'collect_title_candidates', and returning the accumulated vector or a 'WikiError'. [crates/gwiki/src/commands/read.rs:221-235] |
| `TitleCandidateSearch` | class | 'TitleCandidateSearch' is a search-state struct that tracks a configurable result limit ('max_results'), a cap on how many entries may be scanned ('max_scanned_entries'), and the current scan count ('scanned_entries'). [crates/gwiki/src/commands/read.rs:237-241] |
| `collect_title_candidates` | function | Recursively scans 'dir' for readable wiki documents under 'root', stopping at configured result and scan limits, and collects 'ReadCandidate's for files whose first heading exactly matches 'title'. [crates/gwiki/src/commands/read.rs:243-312] |
| `first_heading` | function | Returns the first non-empty ATX heading found in 'content' by scanning lines in order and extracting the heading text, or 'None' if no such heading exists. [crates/gwiki/src/commands/read.rs:314-320] |
| `normal_components` | function | Returns a 'Vec<&str>' containing the UTF-8 string slices of only the 'Component::Normal' components from 'path', discarding all other path component տեսակs. [crates/gwiki/src/commands/read.rs:322-329] |
| `render` | function | Clones the input scope, renders a textual representation and JSON payload from 'ReadOutput', converts serialization failures into 'WikiError::Json', and returns a scoped '"read"' 'CommandOutcome' via 'super::scoped_outcome'. [crates/gwiki/src/commands/read.rs:331-340] |
| `render_text` | function | 'render_text' returns 'output.content' cloned when present, otherwise formats a fallback multiline status report containing the read status, scope, requested kind/value, and each degradation’s label, message, and guidance. [crates/gwiki/src/commands/read.rs:342-361] |
| `ReadOutput` | class | 'ReadOutput' is a read-operation result record that captures the executed command, scope, request parameters, status, resolved paths and title, content format and optional body, byte length, truncation flag, candidate matches, and any degradations. [crates/gwiki/src/commands/read.rs:364-378] |
| `ReadFoundContent` | class | 'ReadFoundContent' is a data container holding an optional title, the content text, the original byte length, and a truncation flag for found source data. [crates/gwiki/src/commands/read.rs:380-385] |
| `ReadOutput::found` | method | Constructs a 'Self' value representing a successful 'read' result by populating metadata ('scope', 'requested', wiki and absolute paths) and content fields from 'ReadFoundContent', setting 'status' to '"found"' and initializing 'candidates' and 'degradations' as empty. [crates/gwiki/src/commands/read.rs:388-410] |
| `ReadOutput::not_found` | method | Constructs a new 'Self' by delegating to 'Self::empty' with the provided 'scope' and 'requested', the fixed identifier '"not_found"', the optional 'wiki_path' and 'absolute_path', and a single-element degradation list containing 'degradation'. [crates/gwiki/src/commands/read.rs:412-427] |
| `ReadOutput::invalid_request` | method | Constructs an empty instance for the given 'scope' and 'requested' values, tagging it with the '"invalid_request"' kind and attaching the supplied 'degradation' as the sole degradation entry. [crates/gwiki/src/commands/read.rs:429-442] |
| `ReadOutput::ambiguous` | method | Constructs an empty read result for the given 'scope' and 'requested' state marked with an '"ambiguous"' degradation explaining that multiple scoped wiki documents share the title, then stores the provided 'candidates' in the result. [crates/gwiki/src/commands/read.rs:444-461] |
| `ReadOutput::empty` | method | Constructs and returns a 'Self' value for a 'read' result with the given scope, request, status, optional wiki and absolute paths, and degradations, while initializing 'title'/'content'/'byte_len' to 'None', 'content_format' to '"markdown"', 'truncated' to 'false', and 'candidates' to an empty vector. [crates/gwiki/src/commands/read.rs:463-486] |

_9 more symbol(s) not shown — run `gcode outline crates/gwiki/src/commands/read.rs` for the full list._

_Verified by 3 in-file unit tests._

