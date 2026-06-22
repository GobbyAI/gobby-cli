---
title: crates/gwiki/src/health.rs
type: code_file
provenance:
- file: crates/gwiki/src/health.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/health.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/health.rs` exposes 55 indexed API symbols.

## How it fits

`crates/gwiki/src/health.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HealthReport` | class | A struct that aggregates multiple categories of documentation health diagnostics (stale pages, citation issues, broken links, duplicate concepts, and compilation errors) along with execution context and output serialization paths. [crates/gwiki/src/health.rs:22-34] |
| `HealthSourceIssue` | class | 'HealthSourceIssue' is a Rust struct that represents an issue associated with a health data source, containing a source identifier, an optional file system path, and a location string. [crates/gwiki/src/health.rs:37-41] |
| `DuplicateConcept` | class | 'DuplicateConcept' is a public struct that associates a textual title with a vector of file system paths, representing multiple occurrences of a semantically equivalent item across different locations. [crates/gwiki/src/health.rs:44-47] |
| `run` | function | Inspects a vault at the specified path for a given scope, persists the resulting health report, and returns the report or propagates a WikiError. [crates/gwiki/src/health.rs:49-53] |
| `inspect` | function | # Summary Conducts a comprehensive health audit of a wiki vault by analyzing citations, linting, and source metadata to report stale pages, uncited sources, broken links, duplicate concepts, and uncompiled sources within a specified scope. [crates/gwiki/src/health.rs:55-95] |
| `render_text` | function | Generates a markdown-formatted text report String from a HealthReport struct by rendering its diagnostic components (stale pages, citations, broken links, duplicates, and uncompiled sources). [crates/gwiki/src/health.rs:97-106] |
| `persist_report` | function | Persists a HealthReport to disk by serializing it to JSON and writing both JSON and rendered text formats to the vault's meta/health directory, with error handling for directory creation, serialization, and file I/O operations. [crates/gwiki/src/health.rs:108-132] |
| `stale_pages` | function | This function filters a slice of wiki pages to identify stale entries, extracts their relative file paths, sorts them, and returns the sorted vector of paths. [crates/gwiki/src/health.rs:134-142] |
| `page_is_stale` | function | # Summary Returns true if a WikiPage's frontmatter contains an explicit 'stale' boolean flag, a 'status' or 'review_status' field valued as "stale" (case-insensitive), or an overdue 'stale_after' date relative to the current UTC time. [crates/gwiki/src/health.rs:144-169] |
| `stale_after_is_due` | function | # Summary Attempts to parse a string as a datetime using RFC3339, naive datetime, or date formats and returns true if the parsed temporal value is less than or equal to the provided current UTC time. [crates/gwiki/src/health.rs:171-188] |
| `source_citation_is_stale` | function | Checks whether a source citation is stale by delegating to 'source_citation_is_stale_at' with the provided source and the current UTC timestamp. [crates/gwiki/src/health.rs:190-192] |
| `source_citation_is_stale_at` | function | This function returns true if a source contains a citation and its fetch timestamp exceeds the configured stale citation age threshold as of the specified time. [crates/gwiki/src/health.rs:194-197] |
| `fetched_at_is_stale` | function | Returns true if a fetched timestamp parsed from the input string is older than the specified stale threshold in years relative to the provided current UTC time. [crates/gwiki/src/health.rs:199-211] |
| `parse_fetched_at` | function | Parses a string into a 'DateTime<Utc>' by sequentially attempting RFC3339, YYYY-MM-DD, and two ISO-like datetime formats (with space or 'T' separators), returning 'None' if all attempts fail. [crates/gwiki/src/health.rs:213-226] |
| `stale_citation_years` | function | Returns a u64 value parsed from the STALE_CITATION_YEARS_ENV environment variable, defaulting to 1 if the variable is unset or parsing fails. [crates/gwiki/src/health.rs:228-236] |
| `stale_citation_years_from_env` | function | Parses a trimmed string as a u64 and returns 'Some' only if parsing succeeds and the value is greater than zero. [crates/gwiki/src/health.rs:238-240] |
| `fetched_year` | function | Attempts to parse the first four characters of the input string as a u64, returning None if the string is shorter than four characters or contains non-ASCII-digit characters. [crates/gwiki/src/health.rs:242-247] |
| `approximate_current_year_at` | function | Approximates the current year by adding 1970 to the quotient of the input UTC datetime's Unix timestamp (in seconds) and the average Gregorian year duration. [crates/gwiki/src/health.rs:249-253] |
| `load_provenance` | function | Loads a 'ProvenanceGraph' from the vault's 'meta/provenance.json' file if it exists, otherwise returns a default 'ProvenanceGraph' instance, with errors wrapped in a 'Result<ProvenanceGraph, WikiError>'. [crates/gwiki/src/health.rs:255-262] |
| `change_triggered_affected_pages` | function | Loads provenance metadata and queries the code graph to identify which wiki pages are affected by a given set of code changes within a specified project configuration. [crates/gwiki/src/health.rs:265-276] |
| `SourceCitationIndex` | class | SourceCitationIndex is a struct that maintains a sorted set of unique source identifiers as strings through a BTreeSet field. [crates/gwiki/src/health.rs:279-281] |
| `SourceCitationIndex::cites` | method | This method returns 'true' if the provided 'source_id' exists within the object's 'cited_source_ids' collection, otherwise 'false'. [crates/gwiki/src/health.rs:284-286] |
| `build_citation_index` | function | Constructs a 'SourceCitationIndex' by combining provenance-tracked source citations with regex-based pattern matching of source reference patterns against wiki page markdown (excluding fenced code blocks). [crates/gwiki/src/health.rs:289-327] |
| `source_reference_needles` | function | Extracts and returns a vector of string references containing a SourceRecord's id, location, canonical_location, and optional citation field. [crates/gwiki/src/health.rs:329-339] |

_18 more symbol(s) not shown — run `gcode outline crates/gwiki/src/health.rs` for the full list._

_Verified by 13 in-file unit tests._

