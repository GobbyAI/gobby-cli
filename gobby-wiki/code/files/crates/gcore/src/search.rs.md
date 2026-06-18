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

`crates/gcore/src/search.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `TrustedRowId` | class | Indexed class `TrustedRowId` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:20] |
| `TrustedRowId::new_unchecked` | method | Indexed method `TrustedRowId::new_unchecked` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:29-31] |
| `TrustedRowId::as_str` | method | Indexed method `TrustedRowId::as_str` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:33-35] |
| `bm25_score_expr` | function | Indexed function `bm25_score_expr` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:39-41] |
| `SearchResult` | class | Indexed class `SearchResult` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:45-55] |
| `SourceExplanation` | class | Indexed class `SourceExplanation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:59-63] |
| `SearchDegradation` | class | Indexed class `SearchDegradation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:67-70] |
| `rrf_merge` | function | Indexed function `rrf_merge` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:76-130] |
| `sanitize_pg_search_query` | function | Indexed function `sanitize_pg_search_query` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:133-156] |
| `rrf_preserves_explanations_and_degradation` | function | Indexed function `rrf_preserves_explanations_and_degradation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:163-183] |
| `sanitize_pg_search_query_matches_gobby_rules` | function | Indexed function `sanitize_pg_search_query_matches_gobby_rules` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:186-201] |
| `search_result_is_cli_independent` | function | Indexed function `search_result_is_cli_independent` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:204-223] |
| `bm25_score_expression_uses_pdb_score` | function | Indexed function `bm25_score_expression_uses_pdb_score` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:226-230] |
| `bm25_score_regprocedure_matches_runtime_schema_contract` | function | Indexed function `bm25_score_regprocedure_matches_runtime_schema_contract` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:233-235] |
| `search_core_has_no_domain_queries` | function | Indexed function `search_core_has_no_domain_queries` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:238-246] |
| `forbidden_domain_fragments` | function | Indexed function `forbidden_domain_fragments` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:248-268] |
| `rrf_deduplicates_within_source` | function | Indexed function `rrf_deduplicates_within_source` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:271-280] |
| `rrf_sorts_sources_deterministically` | function | Indexed function `rrf_sorts_sources_deterministically` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:283-296] |

