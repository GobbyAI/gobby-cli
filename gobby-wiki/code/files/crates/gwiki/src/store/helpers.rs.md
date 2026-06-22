---
title: crates/gwiki/src/store/helpers.rs
type: code_file
provenance:
- file: crates/gwiki/src/store/helpers.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/store/helpers.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/store/helpers.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gwiki/src/store/helpers.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `display_path` | function | Returns a lossy UTF-8 string representation of 'path' with all backslashes normalized to forward slashes. [crates/gwiki/src/store/helpers.rs:12-14] |
| `validate_chunk_paths` | function | Validates that every 'WikiChunk' in 'chunks' has a 'path' matching the supplied 'path', returning the first 'StoreError' from 'validate_matching_path' if any mismatch occurs. [crates/gwiki/src/store/helpers.rs:16-21] |
| `validate_link_paths` | function | Iterates over 'links' and validates that each 'link.path' matches the provided 'path' via 'validate_matching_path', returning the first 'StoreError' encountered or 'Ok(())' if all match. [crates/gwiki/src/store/helpers.rs:23-28] |
| `validate_matching_path` | function | Returns 'Ok(())' when 'expected' and 'found' refer to the same display path, otherwise returns 'StoreError::InvalidData' for 'field' with a message reporting the expected and found paths. [crates/gwiki/src/store/helpers.rs:30-46] |
| `equivalent_display_path` | function | Returns 'true' when 'left' and 'right' produce the same 'display_path' representation, and 'false' otherwise. [crates/gwiki/src/store/helpers.rs:48-50] |
| `platform_path_from_display` | function | Converts a display-form path string into a platform 'PathBuf', returning it unchanged on Unix-like systems and replacing '/' with the OS main separator on non-'/' platforms. [crates/gwiki/src/store/helpers.rs:52-58] |
| `scoped_id` | function | Builds a scoped text identifier by delegating to 'scoped_text_id' with the given 'prefix', 'scope', and 'path', appending a single 'suffix' value when present or no extra components otherwise. [crates/gwiki/src/store/helpers.rs:60-70] |
| `scoped_text_id` | function | Constructs a scoped identifier string as 'prefix:scope_kind:scope_id:display_path(path)' with each 'suffix' appended as additional ':'-separated segments, then passes the result through 'cap_scoped_id' and returns it. [crates/gwiki/src/store/helpers.rs:72-89] |
| `cap_scoped_id` | function | Computes a content hash of the input string’s bytes and delegates to 'cap_scoped_id_with_hash' with the original 'id' and the resulting hash. [crates/gwiki/src/store/helpers.rs:91-94] |
| `cap_scoped_id_with_hash` | function | Returns 'id' unchanged when its byte length is at most 'MAX_ID_LEN', otherwise truncates 'id' at a UTF-8 character boundary so that '"{prefix}-{suffix}"' fits within 'MAX_ID_LEN', where 'suffix' is the first 'HASH_SUFFIX_LEN' bytes of 'hash' if available or the full 'hash' otherwise. [crates/gwiki/src/store/helpers.rs:96-115] |
| `document_kind_name` | function | Returns the canonical static string label for a 'WikiDocumentKind' variant by matching each kind to its corresponding snake_case name. [crates/gwiki/src/store/helpers.rs:117-125] |
| `ingestion_status` | function | Returns the lowercase static status string corresponding to a 'WikiIngestionEvent' variant: 'added', 'changed', 'deleted', 'unchanged', or 'skipped'. [crates/gwiki/src/store/helpers.rs:127-135] |
| `link_kind` | function | Returns '"markdown"' for targets that are network-path references or have a URI scheme after trimming whitespace, and '"wiki"' otherwise. [crates/gwiki/src/store/helpers.rs:137-144] |
| `has_uri_scheme` | function | Returns 'true' if 'target' contains a ':' and the substring before it is a valid URI scheme name starting with an ASCII letter followed only by ASCII alphanumerics, '+', '.', or '-'; otherwise returns 'false'. [crates/gwiki/src/store/helpers.rs:146-153] |
| `rollback_link_replacement` | function | Attempts to roll back the given transaction for a gwiki link replacement at 'path', and logs an error with the path if the rollback fails. [crates/gwiki/src/store/helpers.rs:155-159] |
| `rollback_chunk_replacement` | function | Attempts to roll back the given transaction for a gwiki chunk replacement and logs an error including the path if the rollback fails. [crates/gwiki/src/store/helpers.rs:161-165] |
| `configured_memory_index_limit_bytes` | function | Returns the positive 'u64' value of the 'MAX_MEMORY_INDEX_BYTES_ENV' environment variable if it is set and parses successfully, otherwise emits a warning for invalid values and returns 'None'. [crates/gwiki/src/store/helpers.rs:167-180] |

