---
title: crates/gcode/src/search/fts/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/tests.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/search/fts/tests.rs` exposes 34 indexed API symbols.

## How it fits

`crates/gcode/src/search/fts/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `unique_test_id` | function | Indexed function `unique_test_id` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:17-26] |
| `sanitize_pg_search_query_matches_gobby_rules` | function | Indexed function `sanitize_pg_search_query_matches_gobby_rules` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:29-34] |
| `sanitize_pg_search_query_escapes_leading_minus_per_token` | function | Indexed function `sanitize_pg_search_query_escapes_leading_minus_per_token` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:37-43] |
| `sanitize_pg_search_query_preserves_dsl_punctuation` | function | Indexed function `sanitize_pg_search_query_preserves_dsl_punctuation` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:46-49] |
| `glob_to_like_prefix_escapes_like_wildcards` | function | Indexed function `glob_to_like_prefix_escapes_like_wildcards` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:52-57] |
| `expand_paths_trims_skips_empty_and_expands_bare_paths` | function | Indexed function `expand_paths_trims_skips_empty_and_expands_bare_paths` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:60-72] |
| `compile_patterns_reports_invalid_glob` | function | Indexed function `compile_patterns_reports_invalid_glob` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:75-81] |
| `path_like_prefixes_escape_and_require_all_patterns` | function | Indexed function `path_like_prefixes_escape_and_require_all_patterns` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:84-99] |
| `append_unique_symbols_respects_zero_limit` | function | Indexed function `append_unique_symbols_respects_zero_limit` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:102-133] |
| `snippet_centers_first_matching_token` | function | Indexed function `snippet_centers_first_matching_token` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:136-142] |
| `snippet_centers_earliest_matching_token_regardless_of_query_order` | function | Indexed function `snippet_centers_earliest_matching_token_regardless_of_query_order` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:145-151] |
| `snippet_handles_unicode_before_match` | function | Indexed function `snippet_handles_unicode_before_match` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:154-166] |
| `overlay_visibility_counts_and_kinds_use_database_predicates` | function | Indexed function `overlay_visibility_counts_and_kinds_use_database_predicates` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:177-209] |
| `resolve_graph_symbol_by_id_resolves_exact_symbol` | function | Indexed function `resolve_graph_symbol_by_id_resolves_exact_symbol` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:217-243] |
| `resolve_graph_symbol_by_id_returns_none_for_missing_uuid` | function | Indexed function `resolve_graph_symbol_by_id_returns_none_for_missing_uuid` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:251-264] |
| `resolve_graph_symbol_by_id_returns_none_for_empty_id` | function | Indexed function `resolve_graph_symbol_by_id_returns_none_for_empty_id` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:272-279] |
| `resolve_graph_symbol_by_id_returns_none_for_malformed_id` | function | Indexed function `resolve_graph_symbol_by_id_returns_none_for_malformed_id` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:287-295] |
| `connect_overlay_visibility_test_db` | function | Indexed function `connect_overlay_visibility_test_db` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:298-305] |
| `OverlayFixtureIds` | class | Indexed class `OverlayFixtureIds` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:307-311] |
| `OverlayFixtureIds::new` | method | Indexed method `OverlayFixtureIds::new` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:314-321] |
| `OverlayFixtureCleanup` | class | Indexed class `OverlayFixtureCleanup` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:324-328] |
| `OverlayFixtureCleanup::cleanup` | method | Indexed method `OverlayFixtureCleanup::cleanup` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:331-338] |
| `OverlayFixtureCleanup::drop` | method | Indexed method `OverlayFixtureCleanup::drop` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:342-344] |
| `SingleProjectCleanup` | class | Indexed class `SingleProjectCleanup` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:347-350] |
| `SingleProjectCleanup::drop` | method | Indexed method `SingleProjectCleanup::drop` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:353-357] |
| `cleanup_overlay_visibility_fixture` | function | Indexed function `cleanup_overlay_visibility_fixture` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:360-363] |
| `cleanup_single_project` | function | Indexed function `cleanup_single_project` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:365-367] |
| `cleanup_overlay_visibility_projects` | function | Indexed function `cleanup_overlay_visibility_projects` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:369-383] |
| `seed_overlay_visibility_fixture` | function | Indexed function `seed_overlay_visibility_fixture` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:385-473] |
| `insert_project` | function | Indexed function `insert_project` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:475-483] |
| `insert_file` | function | Indexed function `insert_file` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:485-502] |
| `insert_symbol` | function | Indexed function `insert_symbol` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:504-517] |
| `insert_chunk` | function | Indexed function `insert_chunk` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:519-536] |
| `overlay_visibility_context` | function | Indexed function `overlay_visibility_context` in `crates/gcode/src/search/fts/tests.rs`. [crates/gcode/src/search/fts/tests.rs:538-557] |

