---
title: crates/gwiki/src/sources/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/sources/tests.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gwiki/src/sources/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `dedupes_by_canonical_identity_and_hash` | function | Verifies that registering two URL drafts with the same canonical identity and identical content hash returns the original manifest, writes only one source record to the index, and preserves the first draft’s metadata fields. [crates/gwiki/src/sources/tests.rs:8-50] |
| `local_file_replay_metadata_round_trips_through_manifest` | function | Verifies that a 'SourceReplay::LocalFile' persisted in a 'SourceManifest' round-trips through disk intact, preserving the entry ID, file path, and serialized ingest routing settings. [crates/gwiki/src/sources/tests.rs:53-113] |
| `canonical_location_sorts_query_before_trimming_slash` | function | Verifies that 'canonicalize_location' lowercases the host, sorts query parameters alphabetically, and removes the trailing slash and fragment from 'https://Example.com/docs/?b=2&a=1#frag', yielding 'https://example.com/docs?a=1&b=2'. [crates/gwiki/src/sources/tests.rs:116-121] |
| `existing_index_strips_unmarked_manifest_until_next_heading` | function | Creates a temp index file containing an unmarked '## Source manifest' section and verifies 'existing_index_without_manifest' removes that manifest block from the returned prefix while preserving the subsequent generated heading and content in the suffix. [crates/gwiki/src/sources/tests.rs:124-140] |
| `existing_index_preserves_content_after_marked_manifest` | function | Verifies that 'existing_index_without_manifest' removes the generated source-manifest block from an existing index while preserving manual content in both the prefix and suffix. [crates/gwiki/src/sources/tests.rs:143-160] |

