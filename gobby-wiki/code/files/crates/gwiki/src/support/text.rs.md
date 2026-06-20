---
title: crates/gwiki/src/support/text.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/text.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/text.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support/text.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gwiki/src/support/text.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `query_tokens` | function | Splits the input query on non-alphanumeric characters, discards empty segments, lowercases each remaining token, and returns them as a 'Vec<String>'. [crates/gwiki/src/support/text.rs:7-13] |
| `keyword_score` | function | Returns the total count of case-insensitive occurrences of all normalized 'tokens' in 'text' by lowercasing the input and summing 'haystack.matches(token).count()' for each token. [crates/gwiki/src/support/text.rs:15-22] |
| `sanitize_code_path` | function | Trims the input path, rejects empty or absolute paths and any path containing '..', root, or platform prefix components, then returns a normalized slash-joined relative path built only from normal components, or 'None' if invalid. [crates/gwiki/src/support/text.rs:26-46] |
| `snippet_from_text` | function | Returns the first non-empty trimmed line of 'text' as a 'String', truncating it to 237 characters and appending '...' if the line exceeds 240 characters. [crates/gwiki/src/support/text.rs:48-59] |
| `degradation_label` | function | Returns a canonical 'String' label for a 'DegradationKind', formatting 'ServiceUnavailable' variants as '"{service}_{available\|not_configured\|unreachable}"' based on 'ServiceState' and mapping all other degradation variants to fixed snake_case labels. [crates/gwiki/src/support/text.rs:61-73] |
| `document_kind_name` | function | Maps each 'store::WikiDocumentKind' variant to its corresponding static lowercase snake_case document kind string. [crates/gwiki/src/support/text.rs:75-83] |
| `postgres_object_kind` | function | Maps a 'setup::GwikiPostgresObjectKind' variant to its corresponding lowercase static string identifier: '"preflight"', '"table"', or '"index"'. [crates/gwiki/src/support/text.rs:85-91] |
| `display_path` | function | Returns a lossy UTF-8 string representation of 'path' with all backslashes normalized to forward slashes. [crates/gwiki/src/support/text.rs:93-95] |
| `slugify` | function | 'slugify' delegates to 'slugify_with_options(value, None, None)' and returns the resulting 'String' using default options. [crates/gwiki/src/support/text.rs:97-99] |
| `slugify_with_options` | function | Lowercases 'value', retains only ASCII alphanumerics separated by single '-' characters, truncates to 'max_len' by byte length if provided, trims any trailing dash, and returns 'fallback' or an empty string when the result is empty. [crates/gwiki/src/support/text.rs:101-126] |

_Verified by 3 in-file unit tests._

