---
title: crates/gcode/src/search
type: code_module
provenance:
- file: crates/gcode/src/search/fts.rs
  ranges:
  - 1-32
- file: crates/gcode/src/search/fts/common.rs
  ranges:
  - '16'
  - 19-22
  - 25-29
  - 32-36
  - 38-54
  - 56-59
  - 63-69
  - 71-76
  - 78-86
  - 88-123
  - 126-135
  - 138-148
  - 150-152
  - 154-175
  - 177-184
  - 186-196
  - 198-200
  - 202-233
  - 235-250
  - 252-272
  - 274-291
  - 293-341
  - 348-354
  - 357-362
- file: crates/gcode/src/search/fts/content.rs
  ranges:
  - 13-21
  - 24-81
  - 83-138
  - 140-178
  - 180-196
  - 199-202
  - 204-210
  - 212-227
  - 229-244
  - 250-253
  - 256-261
  - 264-269
- file: crates/gcode/src/search/fts/counts.rs
  ranges:
  - 10-66
  - 69-113
  - 115-146
  - 148-164
  - 166-191
  - 193-243
  - 245-259
  - 261-273
  - 275-294
  - 296-307
  - 309-333
  - 335-359
  - 366-385
- file: crates/gcode/src/search/fts/graph.rs
  ranges:
  - 16-50
  - 52-55
  - 57-62
  - 64-69
  - 71-78
  - 80-96
  - 98-103
  - 108-147
- file: crates/gcode/src/search/fts/symbols.rs
  ranges:
  - 15-18
  - 21-26
  - 28-33
  - 36-73
  - 76-112
  - 114-190
  - 192-225
  - 227-260
  - 262-337
  - 339-371
  - 374-386
  - 388-401
- file: crates/gcode/src/search/fts/tests.rs
  ranges:
  - 17-26
  - 29-34
  - 37-43
  - 46-49
  - 52-57
  - 60-72
  - 75-81
  - 84-99
  - 102-133
  - 136-142
  - 145-151
  - 154-166
  - 177-209
  - 217-243
  - 251-264
  - 272-279
  - 287-295
  - 298-305
  - 307-311
  - 313-322
  - 324-328
  - 330-339
  - 341-345
  - 347-350
  - 352-358
  - 360-363
  - 365-367
  - 369-383
  - 385-473
  - 475-483
  - 485-502
  - 504-517
  - 519-536
  - 538-557
- file: crates/gcode/src/search/graph_boost.rs
  ranges:
  - 21-47
  - 55-86
  - 88-106
  - 113-127
  - 129-153
  - 156-160
  - 163-167
  - 170-174
  - 177-223
- file: crates/gcode/src/search/mod.rs
  ranges:
  - 1-11
- file: crates/gcode/src/search/rrf.rs
  ranges:
  - '7'
  - 15-20
  - 27-34
  - 37-49
  - 52-64
  - 67-75
  - 78-81
  - 84-87
  - 90-113
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The search module is the top-level coordination point for Gobby search, combining PostgreSQL keyword search, semantic vectors, and graph-derived boosts through Reciprocal Rank Fusion while allowing hybrid callers to degrade when optional services are unavailable (crates/gcode/src/search/mod.rs:1-11). Its `fts` entry point keeps command wiring stable while routing pg_search BM25 query sanitization and execution across common helpers, content search, counts, graph symbol resolution, and symbol/text search APIs, re-exporting the public functions and shared types used by callers (crates/gcode/src/search/fts.rs:1-32).

The main lexical flow starts in `fts`, where shared infrastructure handles safe parameter binding, visibility and path filters, BM25 ordering, query sanitation, and reusable result/filter types before dispatching to content, symbol, text, count, or graph-resolution helpers. Graph boosting then augments search by resolving a query to the best visible symbol with `search_symbols_exact_first_visible`, scoping graph lookup to the symbol’s project, collecting caller and usage IDs from FalkorDB, and deduplicating non-empty IDs; if FalkorDB, PostgreSQL connection, resolution, or graph neighbors are unavailable, it returns an empty list so lexical results can continue (crates/gcode/src/search/graph_boost.rs:1-47).

For broader hybrid search, `graph_expand` takes seed IDs from FTS or semantic search, groups work by project, and expands through callees and callers for use as another ranked source, again falling back to an empty result when there are no seeds or graph infrastructure is missing (crates/gcode/src/search/graph_boost.rs:55-86). The `rrf` submodule is the final merge layer: it defines merged results as `(symbol_id, combined_score, source_names)` and delegates fusion to `gobby_core::search::rrf_merge`, returning results sorted by combined reciprocal-rank score with deterministic source attribution (crates/gcode/src/search/rrf.rs:1-20).
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/content.rs:13-21]
[crates/gcode/src/search/fts/counts.rs:10-66]
[crates/gcode/src/search/fts/graph.rs:16-50]
[crates/gcode/src/search/fts/symbols.rs:15-18]

## Call Diagram

```mermaid
sequenceDiagram
    participant m_03a59319_cb90_5da0_b6da_513367ba0b40 as glob_to_like_prefix &#91;function&#93;
    participant m_06820a48_7d6c_549b_a9e6_b1b1c68426de as query_count &#91;function&#93;
    participant m_0b688623_4f21_5b00_a280_a1d2cbb2d5fb as search_symbols_exact_first &#91;function&#93;
    participant m_0c94647d_0190_534c_ab66_e0696b6a8385 as bm25_score_expression_uses_pdb_score &#91;function&#93;
    participant m_0d0fec52_b764_59a1_8b21_62c58911c683 as count_visible_symbols_by_conditions &#91;function&#93;
    participant m_1622d5fc_3a81_565d_8cfe_6ffabcb12f1f as unique_test_id &#91;function&#93;
    participant m_179dd1c5_b87f_53fc_a90c_763bdd51a20b as search_content &#91;function&#93;
    participant m_1ef9fbbf_bd96_512c_a476_ec5aafe30e6c as OverlayFixtureIds.new &#91;method&#93;
    participant m_20a648c9_6128_5fe2_b489_05e1171388f2 as cleanup_single_project &#91;function&#93;
    participant m_217b7e05_09d4_5acc_b8b3_459b8dcbde29 as cleanup_overlay_visibility_fixture &#91;function&#93;
    participant m_22a35146_0b3d_5a8b_a030_3da3a66883cd as test_merge_single_source &#91;function&#93;
    participant m_23475bad_2efa_5961_a13d_5721256c2451 as count_text_visible &#91;function&#93;
    participant m_239158ff_3daf_584d_b001_791e25c54319 as merge_delegates_to_gobby_core_rrf &#91;function&#93;
    participant m_24e75ff8_ffee_5114_97b1_60fbc8300eea as push_path_filter &#91;function&#93;
    participant m_2b93fd1b_cb44_5f9c_80ff_ccaf43295cba as connect_overlay_visibility_test_db &#91;function&#93;
    participant m_2cd40db1_4e53_5de4_be24_7b59e0b83a43 as graph_expand &#91;function&#93;
    participant m_30d84ae4_7c0c_5f47_a008_8f41fb85f29c as resolve_graph_symbol_by_id_returns_none_for_empty_id &#91;function&#93;
    participant m_3167635d_631c_5707_8b2d_6aa46bf46019 as trusted_row_id &#91;function&#93;
    participant m_33186fc9_8d87_555c_89d0_58c4b6c54b97 as push_param &#91;function&#93;
    participant m_3468182c_fb0e_5b7c_b068_8f2eb57ea954 as content_bm25_order_by_sql &#91;function&#93;
    participant m_36b6335a_ba3c_5adf_bbdd_5cce7c9bf895 as count_content_bm25_visible &#91;function&#93;
    participant m_3d1bee9a_3709_57f9_a28d_e88b9c8785a7 as resolve_graph_symbol_by_id &#91;function&#93;
    participant m_41bebba3_96fa_5b65_bc0c_3f65881e72cf as cleanup_overlay_visibility_projects &#91;function&#93;
    participant m_72fa13bb_eabb_5eb1_b8fe_d7db332ec1b3 as content_hits_from_rows &#91;function&#93;
    participant m_7f8858f7_6495_512a_a587_95d455f4fbbe as search_symbols_by_name &#91;function&#93;
    participant m_842c67f7_b4e2_5d99_8a88_32cad789aa2c as exact_symbol_matches_result &#91;function&#93;
    participant m_8e85ae6a_f520_5f17_afd9_754b8de3432f as count_symbol_file_path_rows &#91;function&#93;
    participant m_930b5993_fb3e_5fb7_8d6c_f60518226697 as path_like_prefixes &#91;function&#93;
    participant m_95df4599_dd9f_564b_83ca_459b096613b2 as param_refs &#91;function&#93;
    participant m_bc13a11f_4797_55ab_96a8_f7c8e4eb57e2 as count_visible_content_by_conditions &#91;function&#93;
    participant m_cdbdd7fb_61d4_5e31_b2bb_b1e42758c75a as graph_expand_grouped &#91;function&#93;
    participant m_d3ee1ca5_ab0b_56bc_931e_148ce45b4a3e as count_symbols_fts_visible &#91;function&#93;
    participant m_ded7d11d_b336_5edf_b8f3_1fbf422eb146 as search_symbols_fts &#91;function&#93;
    participant m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5 as merge &#91;function&#93;
    m_06820a48_7d6c_549b_a9e6_b1b1c68426de->>m_95df4599_dd9f_564b_83ca_459b096613b2: calls
    m_0b688623_4f21_5b00_a280_a1d2cbb2d5fb->>m_7f8858f7_6495_512a_a587_95d455f4fbbe: calls
    m_0b688623_4f21_5b00_a280_a1d2cbb2d5fb->>m_ded7d11d_b336_5edf_b8f3_1fbf422eb146: calls
    m_0c94647d_0190_534c_ab66_e0696b6a8385->>m_3167635d_631c_5707_8b2d_6aa46bf46019: calls
    m_0d0fec52_b764_59a1_8b21_62c58911c683->>m_8e85ae6a_f520_5f17_afd9_754b8de3432f: calls
    m_179dd1c5_b87f_53fc_a90c_763bdd51a20b->>m_3468182c_fb0e_5b7c_b068_8f2eb57ea954: calls
    m_179dd1c5_b87f_53fc_a90c_763bdd51a20b->>m_72fa13bb_eabb_5eb1_b8fe_d7db332ec1b3: calls
    m_1ef9fbbf_bd96_512c_a476_ec5aafe30e6c->>m_1622d5fc_3a81_565d_8cfe_6ffabcb12f1f: calls
    m_20a648c9_6128_5fe2_b489_05e1171388f2->>m_41bebba3_96fa_5b65_bc0c_3f65881e72cf: calls
    m_217b7e05_09d4_5acc_b8b3_459b8dcbde29->>m_41bebba3_96fa_5b65_bc0c_3f65881e72cf: calls
    m_22a35146_0b3d_5a8b_a030_3da3a66883cd->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_23475bad_2efa_5961_a13d_5721256c2451->>m_d3ee1ca5_ab0b_56bc_931e_148ce45b4a3e: calls
    m_239158ff_3daf_584d_b001_791e25c54319->>m_ee7eabc0_8008_50d8_9fde_f2a283bc7fe5: calls
    m_24e75ff8_ffee_5114_97b1_60fbc8300eea->>m_03a59319_cb90_5da0_b6da_513367ba0b40: calls
    m_24e75ff8_ffee_5114_97b1_60fbc8300eea->>m_33186fc9_8d87_555c_89d0_58c4b6c54b97: calls
    m_24e75ff8_ffee_5114_97b1_60fbc8300eea->>m_930b5993_fb3e_5fb7_8d6c_f60518226697: calls
    m_2cd40db1_4e53_5de4_be24_7b59e0b83a43->>m_cdbdd7fb_61d4_5e31_b2bb_b1e42758c75a: calls
    m_30d84ae4_7c0c_5f47_a008_8f41fb85f29c->>m_2b93fd1b_cb44_5f9c_80ff_ccaf43295cba: calls
    m_36b6335a_ba3c_5adf_bbdd_5cce7c9bf895->>m_bc13a11f_4797_55ab_96a8_f7c8e4eb57e2: calls
    m_3d1bee9a_3709_57f9_a28d_e88b9c8785a7->>m_842c67f7_b4e2_5d99_8a88_32cad789aa2c: calls
```

## Child Modules

- [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]] - The `crates/gcode/src/search/fts` module owns PostgreSQL-backed full-text search for gcode symbols and content, with shared infrastructure in `common.rs` for safe parameter binding, BM25 score ordering, visibility and path filters, and the shared result/filter types used by the rest of the module. It centralizes pg_search query sanitation through `gobby_core`, exposes helper types such as `ResolvedGraphSymbol`, `SymbolFilters`, `SymbolOrder`, and `PgParam`, and uses helpers like `push_param`, `param_refs`, and `query_count` so the search and count implementations compose SQL without hand-numbering parameters or duplicating common predicates. 

The main search flows split by domain. `content.rs` searches `code_content_chunks`, rejecting empty queries and empty sanitized BM25 terms, then builds a parameterized query scoped by project, optional language, path filters, and BM25 ordering via `pdb.score` before mapping rows into `ContentSearchHit` snippets.  `symbols.rs` provides matching symbol search flows, including BM25 search, name-based fallback, exact-first matching, and visibility-aware variants that can mark results as degraded when filtering must be relaxed.  `counts.rs` mirrors those flows for result counts, applying the same sanitation, language, project, visibility, and path constraints, with regex or post-filter fallback support for path glob cases. [crates/gcode/src/search/fts/counts.rs:10-66] 

Graph-symbol resolution is handled separately in `graph.rs`: it queries `code_symbols`, maps database rows into lightweight `ResolvedGraphSymbol` values, tries exact matches first, then falls back to candidate-based resolution and suggestion labels when a single decisive symbol cannot be found.  The test suite ties the pieces together against PostgreSQL fixtures, covering query sanitation, path and glob normalization, snippet behavior, overlay visibility predicates, and graph-symbol lookup; it also defines helpers for unique IDs, database connections, fixture seeding, cleanup, and overlay-scoped contexts. 

## Files

- [[code/files/crates/gcode/src/search/fts.rs|crates/gcode/src/search/fts.rs]] - Module entry point for Gobby’s PostgreSQL-backed keyword search, including BM25 query sanitization, search/count helpers for content, symbols, text, and graph symbol resolution. It also re-exports the main search APIs and shared filtering utilities used by the `fts` command wiring. [crates/gcode/src/search/fts.rs:1-32]
- [[code/files/crates/gcode/src/search/graph_boost.rs|crates/gcode/src/search/graph_boost.rs]] - Provides FalkorDB-backed graph boosting for search. `graph_boost` resolves a query to the best visible symbol with FTS, then collects and deduplicates related caller and usage IDs from the symbol’s project so hybrid search can boost graph-connected results. `graph_expand` and `graph_expand_grouped` take seed symbol IDs and expand them through visible callees and callers, batching by project and deduplicating the combined neighborhood. The helper constructors build test `Context` values with and without FalkorDB, and the tests verify the empty-fallback behavior and grouped expansion/deduping logic.
[crates/gcode/src/search/graph_boost.rs:21-47]
[crates/gcode/src/search/graph_boost.rs:55-86]
[crates/gcode/src/search/graph_boost.rs:88-106]
[crates/gcode/src/search/graph_boost.rs:113-127]
[crates/gcode/src/search/graph_boost.rs:129-153]
- [[code/files/crates/gcode/src/search/mod.rs|crates/gcode/src/search/mod.rs]] - Top-level search module that wires together full-text search, semantic vector search, and graph boosting, with reciprocal rank fusion for ranking. It exposes the `fts`, `graph_boost`, and `rrf` submodules and is designed to degrade gracefully when some configured search services are unavailable. [crates/gcode/src/search/mod.rs:1-11]
- [[code/files/crates/gcode/src/search/rrf.rs|crates/gcode/src/search/rrf.rs]] - This file provides a thin Reciprocal Rank Fusion wrapper for search results. It defines `MergedResult` as `(symbol_id, combined_score, source_names)` and exposes `merge`, which delegates to `gobby_core::search::rrf_merge` and converts the returned fused items into that tuple form; the tests exercise single-source ordering, duplicate and disjoint source merging, empty input handling, deterministic source ordering, and delegation behavior.
[crates/gcode/src/search/rrf.rs:7]
[crates/gcode/src/search/rrf.rs:15-20]
[crates/gcode/src/search/rrf.rs:27-34]
[crates/gcode/src/search/rrf.rs:37-49]
[crates/gcode/src/search/rrf.rs:52-64]

## Components

- `821967f5-60ed-567d-b11d-f9cfb2726a60`
- `2cd40db1-4e53-5de4-be24-7b59e0b83a43`
- `cdbdd7fb-61d4-5e31-b2bb-b1e42758c75a`
- `fce20da6-a98f-553e-bfa7-bec5b8685476`
- `8e07f24c-1345-5ff2-b99b-fa4256b92f7a`
- `d2b29a0f-7fa5-5865-a104-83fe2cdd3eef`
- `8e475747-c493-5cc6-a3e7-f86a684ba506`
- `d0070db0-0756-5591-97c0-c2b4fa4bd3f2`
- `752226a9-8b51-5e80-97ec-354312b73330`
- `4f252f0f-f18a-5b74-97a4-740bcaaa731d`
- `ee7eabc0-8008-50d8-9fde-f2a283bc7fe5`
- `22a35146-0b3d-5a8b-a030-3da3a66883cd`
- `873d4c1e-dd07-58fe-a832-e784dabd9689`
- `58647f00-fd39-5646-bad7-155c0cbd79f2`
- `84046dbc-3560-568e-a490-df5f55d17f96`
- `76109a10-3a96-55e7-bf6b-0ebfdd2fcb4a`
- `8cb6830f-e7a6-5d3f-b87c-ad56c1e35dd1`
- `239158ff-3daf-584d-b001-791e25c54319`

