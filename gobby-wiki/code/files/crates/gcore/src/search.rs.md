---
title: crates/gcore/src/search.rs
type: code_file
provenance:
- file: crates/gcore/src/search.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/search.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/search.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcore/src/search.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TrustedRowId` | class | TrustedRowId is a public newtype tuple struct that wraps a String to provide type-safe representation of a validated or trusted row identifier. [crates/gcore/src/search.rs:20] |
| `TrustedRowId::new_unchecked` | method | This unsafe constructor creates a new instance by converting the provided string reference to an owned 'String' and wrapping it in 'Self' without any validation. [crates/gcore/src/search.rs:29-31] |
| `TrustedRowId::as_str` | method | # Summary The 'as_str' method returns a borrowed string slice reference to the tuple struct's first field. [crates/gcore/src/search.rs:33-35] |
| `bm25_score_expr` | function | Constructs and returns a string representation of a BM25 score function expression by formatting a BM25 score function name with the provided row ID as an argument. [crates/gcore/src/search.rs:39-41] |
| `SearchResult` | class | SearchResult is a struct representing a ranked search outcome that aggregates an opaque identifier, a fusion-combined relevance score, contributing source references, and optional source-level explanations for debugging. [crates/gcore/src/search.rs:45-55] |
| `SourceExplanation` | class | 'SourceExplanation' is a public struct that encapsulates a source identifier string, its numeric rank position, and an associated floating-point relevance or quality score. [crates/gcore/src/search.rs:59-63] |
| `SearchDegradation` | class | A public struct that tracks search source availability by maintaining two vectors of strings: one cataloging unavailable sources and one cataloging available sources. [crates/gcore/src/search.rs:67-70] |
| `rrf_merge` | function | Applies Reciprocal Rank Fusion (RRF) to aggregate multiple ranked search result lists into a single deduplicated result set ordered by summed relevance scores. [crates/gcore/src/search.rs:76-130] |
| `sanitize_pg_search_query` | function | # Summary Sanitizes PostgreSQL search queries by normalizing control characters and escaping leading hyphens to prevent negation operator interpretation. [crates/gcore/src/search.rs:133-156] |
| `forbidden_domain_fragments` | function | Returns a 'Vec<String>' of forbidden domain fragments constructed by concatenating predefined pairs of string substrings. [crates/gcore/src/search.rs:248-268] |

_Verified by 8 in-file unit tests._

