---
title: crates/gwiki/src/falkor_graph/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/tests.rs
  ranges:
  - 27-30
  - 33-76
  - 79-90
  - 93-95
  - 98-104
  - 107-112
  - 115-126
  - 129-147
  - 150-159
  - 162-181
  - 184-196
  - 199-251
  - 253-255
  - 257-274
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/tests.rs

Module: [[code/modules/crates/gwiki/src/falkor_graph|crates/gwiki/src/falkor_graph]]

## Purpose

This file is a test suite for the Falkor/wiki graph layer. It verifies that the graph is wired to the wiki namespace, that wiki link targets resolve correctly while unresolved and external targets are handled safely, that scope and Cypher string helpers produce the expected literals and escaping, and that code-edge truncation logic respects limits and sentinel handling. It also checks partial degradation reporting and that wiki graph write statements emit the right labels and relationships without leaking code-graph data.
[crates/gwiki/src/falkor_graph/tests.rs:27-30]
[crates/gwiki/src/falkor_graph/tests.rs:33-76]
[crates/gwiki/src/falkor_graph/tests.rs:79-90]
[crates/gwiki/src/falkor_graph/tests.rs:93-95]
[crates/gwiki/src/falkor_graph/tests.rs:98-104]

## API Symbols

- `falkordb_graph_name_is_wiki_owned` (function) component `falkordb_graph_name_is_wiki_owned [function]` (`dda75dcf-bed7-502e-8fa9-95594f0457ac`) lines 27-30 [crates/gwiki/src/falkor_graph/tests.rs:27-30]
  - Signature: `fn falkordb_graph_name_is_wiki_owned() {`
  - Purpose: Verifies that 'FALKORDB_GRAPH_NAME' is exactly '"gobby_wiki"' and not '"gobby_code"' via two assertions. [crates/gwiki/src/falkor_graph/tests.rs:27-30]
- `graph_resolution_keeps_unresolved_targets_and_skips_external` (function) component `graph_resolution_keeps_unresolved_targets_and_skips_external [function]` (`8af826ff-4be3-5ac3-b322-1136a96c7fd5`) lines 33-76 [crates/gwiki/src/falkor_graph/tests.rs:33-76]
  - Signature: `fn graph_resolution_keeps_unresolved_targets_and_skips_external() {`
  - Purpose: Verifies that 'resolve_graph_target' resolves an internal document title to a path, preserves missing targets as 'Unresolved', and returns 'None' for external URLs. [crates/gwiki/src/falkor_graph/tests.rs:33-76]
- `graph_scope_params_are_cypher_string_literals` (function) component `graph_scope_params_are_cypher_string_literals [function]` (`a482585a-9872-5fc7-a17f-798c33cac30b`) lines 79-90 [crates/gwiki/src/falkor_graph/tests.rs:79-90]
  - Signature: `fn graph_scope_params_are_cypher_string_literals() {`
  - Purpose: Verifies that 'scope_params' encodes graph-scope values as Cypher string literals, including escaping embedded single quotes in the scope ID. [crates/gwiki/src/falkor_graph/tests.rs:79-90]
- `graph_scope_params_omit_global_scope_filters` (function) component `graph_scope_params_omit_global_scope_filters [function]` (`69cefdd7-1f80-51a8-b82a-4ae177569bc6`) lines 93-95 [crates/gwiki/src/falkor_graph/tests.rs:93-95]
  - Signature: `fn graph_scope_params_omit_global_scope_filters() {`
  - Purpose: Verifies that 'scope_params' returns 'None' for 'SearchScope::global()', meaning global scopes omit scope parameters and global-scope filters. [crates/gwiki/src/falkor_graph/tests.rs:93-95]
- `ask_unified_graph_code_doc_source_path_maps_to_code_file` (function) component `ask_unified_graph_code_doc_source_path_maps_to_code_file [function]` (`698360e3-f57f-5e20-9552-fe589bbbdbcd`) lines 98-104 [crates/gwiki/src/falkor_graph/tests.rs:98-104]
  - Signature: `fn ask_unified_graph_code_doc_source_path_maps_to_code_file() {`
  - Purpose: Verifies that 'code_doc_source_path' converts 'code/files/crates/gwiki/src/lib.rs.md' to 'Some("crates/gwiki/src/lib.rs")' and returns 'None' for non-code-doc paths like 'wiki/notes.md'. [crates/gwiki/src/falkor_graph/tests.rs:98-104]
- `cypher_string_literal_escapes_like_gcode` (function) component `cypher_string_literal_escapes_like_gcode [function]` (`932a5137-6dbb-5ce7-98bf-9801e22b85c2`) lines 107-112 [crates/gwiki/src/falkor_graph/tests.rs:107-112]
  - Signature: `fn cypher_string_literal_escapes_like_gcode() {`
  - Purpose: Verifies that 'cypher_string_literal' escapes quotes, backslashes, control characters, and other special characters in a Cypher string the same way as G-code style escaping, producing the exact expected quoted literal. [crates/gwiki/src/falkor_graph/tests.rs:107-112]
- `partial_graph_degradation_reports_capped_components` (function) component `partial_graph_degradation_reports_capped_components [function]` (`f34434ae-e2dd-586b-b128-b7a2c6845f5f`) lines 115-126 [crates/gwiki/src/falkor_graph/tests.rs:115-126]
  - Signature: `fn partial_graph_degradation_reports_capped_components() {`
  - Purpose: Verifies that 'partial_graph_degradation' returns a 'DegradationKind::PartialData' for 'gwiki_graph' whose message includes both 'documents>10' and 'links>20'. [crates/gwiki/src/falkor_graph/tests.rs:115-126]
- `code_edge_query_params_use_sentinel_limit_and_parameterized_queries` (function) component `code_edge_query_params_use_sentinel_limit_and_parameterized_queries [function]` (`d7a19ea1-0976-5338-9677-46448e5dbc23`) lines 129-147 [crates/gwiki/src/falkor_graph/tests.rs:129-147]
  - Signature: `fn code_edge_query_params_use_sentinel_limit_and_parameterized_queries() {`
  - Purpose: Verifies that call and import edge queries use a parameterized 'LIMIT $limit' with stable 'ORDER BY' clauses, do not hardcode 'LIMIT 200', and that 'code_edge_query_params' converts an input limit of '7' into the sentinel-adjusted parameter value '"8"'. [crates/gwiki/src/falkor_graph/tests.rs:129-147]
- `truncation_components_name_capped_call_and_import_queries` (function) component `truncation_components_name_capped_call_and_import_queries [function]` (`18c8c2e2-3e75-580b-8fc2-72ed731fa47b`) lines 150-159 [crates/gwiki/src/falkor_graph/tests.rs:150-159]
  - Signature: `fn truncation_components_name_capped_call_and_import_queries() {`
  - Purpose: Tests that 'truncation_component' formats the code call and code import edge truncation components as capped labels, expecting '"code_call_edges>7"' and '"code_import_edges>9"'. [crates/gwiki/src/falkor_graph/tests.rs:150-159]
- `code_edge_query_limit_respects_total_remaining_cap` (function) component `code_edge_query_limit_respects_total_remaining_cap [function]` (`c3d9b04b-5171-5876-b9a9-64a14adcf741`) lines 162-181 [crates/gwiki/src/falkor_graph/tests.rs:162-181]
  - Signature: `fn code_edge_query_limit_respects_total_remaining_cap() {`
  - Purpose: Verifies that 'remaining_code_edge_limit' returns the minimum of the requested and remaining total code-edge cap, yields 'None' when no budget remains, and that 'record_code_edge_truncation' records a total-edge truncation component capped at 'MAX_TOTAL_CODE_EDGES'. [crates/gwiki/src/falkor_graph/tests.rs:162-181]
- `truncate_to_limit_handles_sentinel_rows_and_zero_limit` (function) component `truncate_to_limit_handles_sentinel_rows_and_zero_limit [function]` (`a6ee0af9-71f4-5331-87f2-0166dc3bb591`) lines 184-196 [crates/gwiki/src/falkor_graph/tests.rs:184-196]
  - Signature: `fn truncate_to_limit_handles_sentinel_rows_and_zero_limit() {`
  - Purpose: Verifies that 'truncate_to_limit' truncates rows when the length exceeds the limit, empties the collection when the limit is zero, and returns 'false' without modifying the input when the length is already within the limit. [crates/gwiki/src/falkor_graph/tests.rs:184-196]
- `graph_write_uses_wiki_labels_and_relationships` (function) component `graph_write_uses_wiki_labels_and_relationships [function]` (`4c9c1f92-82e3-5e96-b008-d96e90d2b5f8`) lines 199-251 [crates/gwiki/src/falkor_graph/tests.rs:199-251]
  - Signature: `fn graph_write_uses_wiki_labels_and_relationships() {`
  - Purpose: Verifies that 'graph_write_statements' emits wiki document/source/target labels and 'LINKS_TO', 'MENTIONS_TARGET', and 'SUPPORTS' relationships for wiki facts, while excluding any code-symbol graph labels or 'gobby_code' content. [crates/gwiki/src/falkor_graph/tests.rs:199-251]
- `cypher_string_literal` (function) component `cypher_string_literal [function]` (`9dc9ad72-462d-51ff-b7e0-e90e29907994`) lines 253-255 [crates/gwiki/src/falkor_graph/tests.rs:253-255]
  - Signature: `fn cypher_string_literal(value: &str) -> String {`
  - Purpose: Returns a Cypher string literal by wrapping the escaped contents of 'value' in single quotes. [crates/gwiki/src/falkor_graph/tests.rs:253-255]
- `escape_string_contents` (function) component `escape_string_contents [function]` (`d13bd21c-ea6b-5d61-a349-13aae32a30a2`) lines 257-274 [crates/gwiki/src/falkor_graph/tests.rs:257-274]
  - Signature: `fn escape_string_contents(value: &str) -> String {`
  - Purpose: Returns a new 'String' with backslashes, quotes, common whitespace control characters, and any other ASCII control characters escaped using Rust-style backslash sequences or '\uXXXX', leaving all other characters unchanged. [crates/gwiki/src/falkor_graph/tests.rs:257-274]

