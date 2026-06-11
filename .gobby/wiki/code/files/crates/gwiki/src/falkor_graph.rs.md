---
title: crates/gwiki/src/falkor_graph.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph.rs
  ranges:
  - 29-31
  - 33-43
  - 34-38
  - 40-42
  - 46-49
  - 51-54
  - 56-60
  - 62-78
  - 80-104
  - 106-197
  - 199-240
  - 242-250
  - 252-288
  - 290-296
  - 298-314
  - 316-320
  - 322-328
  - 330-332
  - 334-346
  - 348-350
  - 352-365
  - 367-370
  - 372-402
  - 404-439
  - 441-444
  - 446-473
  - 475-486
  - 488-573
  - 575-607
  - 609-617
  - 619-632
  - 634-636
  - 638-651
  - 653-658
  - 660-666
  - 668-670
  - 672-680
  - 682-697
  - 699-702
  - 704-708
  - 710-714
  - 717-719
  - 722-739
  - 741-745
  - 756-759
  - 762-805
  - 808-819
  - 822-824
  - 827-833
  - 836-841
  - 844-855
  - 858-874
  - 877-886
  - 889-908
  - 911-923
  - 926-978
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/falkor_graph.rs` exposes 56 indexed API symbols.
[crates/gwiki/src/falkor_graph.rs:29-31]
[crates/gwiki/src/falkor_graph.rs:33-43]
[crates/gwiki/src/falkor_graph.rs:34-38]
[crates/gwiki/src/falkor_graph.rs:40-42]
[crates/gwiki/src/falkor_graph.rs:46-49]

## API Symbols

- `SharedCodeGraphTruncation` (class) component `SharedCodeGraphTruncation [class]` (`69a3ab04-5d4a-5d74-a6ca-f87fea95ac73`) lines 29-31 [crates/gwiki/src/falkor_graph.rs:29-31]
  - Signature: `pub(crate) struct SharedCodeGraphTruncation {`
  - Purpose: `SharedCodeGraphTruncation` is a crate-private struct that wraps a vector of strings representing components of a truncated code graph. [crates/gwiki/src/falkor_graph.rs:29-31]
- `SharedCodeGraphTruncation` (class) component `SharedCodeGraphTruncation [class]` (`cf143add-c9ff-5468-acc8-9d2fff479423`) lines 33-43 [crates/gwiki/src/falkor_graph.rs:33-43]
  - Signature: `impl SharedCodeGraphTruncation {`
  - Purpose: This implementation provides factory and state-checking methods for a truncation tracker that records which components were excluded from a shared code graph, with truncation indicated by the presence of stored components. [crates/gwiki/src/falkor_graph.rs:33-43]
- `SharedCodeGraphTruncation.from_components` (method) component `SharedCodeGraphTruncation.from_components [method]` (`621d8578-6ef8-513c-bfcf-5b6bb10a39d3`) lines 34-38 [crates/gwiki/src/falkor_graph.rs:34-38]
  - Signature: `fn from_components(components: BTreeSet<String>) -> Self {`
  - Purpose: Creates a new instance by consuming a `BTreeSet<String>` and collecting its elements into the `components` field. [crates/gwiki/src/falkor_graph.rs:34-38]
- `SharedCodeGraphTruncation.is_truncated` (method) component `SharedCodeGraphTruncation.is_truncated [method]` (`206766fb-8c1a-572a-904d-7b9b49795825`) lines 40-42 [crates/gwiki/src/falkor_graph.rs:40-42]
  - Signature: `pub(crate) fn is_truncated(&self) -> bool {`
  - Purpose: Returns `true` if the `components` field contains any elements, `false` otherwise. [crates/gwiki/src/falkor_graph.rs:40-42]
- `SharedCodeGraphEdges` (class) component `SharedCodeGraphEdges [class]` (`ce92d77c-65a3-505b-96be-f3f078a39158`) lines 46-49 [crates/gwiki/src/falkor_graph.rs:46-49]
  - Signature: `pub(crate) struct SharedCodeGraphEdges {`
  - Purpose: `SharedCodeGraphEdges` is a crate-private struct that holds a vector of `WikiGraphCodeEdge` items alongside `SharedCodeGraphTruncation` metadata indicating whether the edge collection was truncated. [crates/gwiki/src/falkor_graph.rs:46-49]
- `LimitedCodeGraphEdges` (class) component `LimitedCodeGraphEdges [class]` (`e563cd50-b372-5093-a5b3-1e55277135b7`) lines 51-54 [crates/gwiki/src/falkor_graph.rs:51-54]
  - Signature: `struct LimitedCodeGraphEdges {`
  - Purpose: `LimitedCodeGraphEdges` is a struct that encapsulates a vector of `WikiGraphCodeEdge` items along with a boolean flag indicating whether the edge collection was truncated due to size constraints. [crates/gwiki/src/falkor_graph.rs:51-54]
- `GraphBoostData` (class) component `GraphBoostData [class]` (`de8a1f8c-e141-5fff-a7f7-32559e404007`) lines 56-60 [crates/gwiki/src/falkor_graph.rs:56-60]
  - Signature: `pub(crate) struct GraphBoostData {`
  - Purpose: GraphBoostData is a crate-private struct containing vectors of documents and their interconnecting links for graph-based search boosting, along with optional degradation metadata. [crates/gwiki/src/falkor_graph.rs:56-60]
- `sync_scope_from_postgres` (function) component `sync_scope_from_postgres [function]` (`c21f11b5-8376-5e3a-be3d-b82dbfe434d8`) lines 62-78 [crates/gwiki/src/falkor_graph.rs:62-78]
  - Signature: `pub(crate) fn sync_scope_from_postgres(`
  - Purpose: Synchronizes wiki graph facts from PostgreSQL to a FalkorDB graph instance for a specified scope by loading facts, clearing existing data, and executing write statements. [crates/gwiki/src/falkor_graph.rs:62-78]
- `load_graph_boost_data` (function) component `load_graph_boost_data [function]` (`c7baf74a-98e2-5284-9203-0e4c8659f8fb`) lines 80-104 [crates/gwiki/src/falkor_graph.rs:80-104]
  - Signature: `pub(crate) fn load_graph_boost_data(`
  - Purpose: Loads documents and links from a GraphClient within specified limits and returns GraphBoostData with degradation metadata indicating whether either query result was capped. [crates/gwiki/src/falkor_graph.rs:80-104]
- `load_code_graph_edges` (function) component `load_code_graph_edges [function]` (`8e5ef180-3f2c-5637-867c-53a04f2ce546`) lines 106-197 [crates/gwiki/src/falkor_graph.rs:106-197]
  - Signature: `pub(crate) fn load_code_graph_edges(`
  - Purpose: Loads code graph call and import edges from a graph database for indexed code documents, enforcing per-component and aggregate edge limits while tracking truncation events. [crates/gwiki/src/falkor_graph.rs:106-197]
- `code_call_edges` (function) component `code_call_edges [function]` (`cc910344-3638-5610-9542-35621556eee5`) lines 199-240 [crates/gwiki/src/falkor_graph.rs:199-240]
  - Signature: `fn code_call_edges(`
  - Purpose: Fetches and transforms code call graph edges for a specified file from a GraphClient, classifying each edge as either an incoming caller or outgoing call, returning the results with truncation metadata. [crates/gwiki/src/falkor_graph.rs:199-240]
- `code_call_edges_query` (function) component `code_call_edges_query [function]` (`7531ab0d-8c04-5d4c-a2d7-d7497abe1d2f`) lines 242-250 [crates/gwiki/src/falkor_graph.rs:242-250]
  - Signature: `fn code_call_edges_query() -> &'static str {`
  - Purpose: This function returns a static Cypher query string that retrieves directed call edges (CALLS relationships) between code symbols within a project, filtered by source or target file path and ordered by location. [crates/gwiki/src/falkor_graph.rs:242-250]
- `code_import_edges` (function) component `code_import_edges [function]` (`37c8b381-055b-50da-8e60-1bce3861752a`) lines 252-288 [crates/gwiki/src/falkor_graph.rs:252-288]
  - Signature: `fn code_import_edges(`
  - Purpose: Queries a code graph for outgoing import edges from a specified file, transforms the results into `WikiGraphCodeEdge` objects with scope and document context, and returns them with truncation status. [crates/gwiki/src/falkor_graph.rs:252-288]
- `code_import_edges_query` (function) component `code_import_edges_query [function]` (`fbe9714e-66a0-576b-b329-b881451641e3`) lines 290-296 [crates/gwiki/src/falkor_graph.rs:290-296]
  - Signature: `fn code_import_edges_query() -> &'static str {`
  - Purpose: Returns a parameterized Cypher query that retrieves all CodeModule imports reachable from a specified CodeFile, projecting source file path and target module name pairs in ordered fashion with a configurable limit. [crates/gwiki/src/falkor_graph.rs:290-296]
- `code_edge_query_params` (function) component `code_edge_query_params [function]` (`5949c735-f368-552a-9179-0f89a140d327`) lines 298-314 [crates/gwiki/src/falkor_graph.rs:298-314]
  - Signature: `fn code_edge_query_params(`
  - Purpose: Constructs a HashMap of query parameters by escaping the project ID and file path strings and converting a validated limit value to a string. [crates/gwiki/src/falkor_graph.rs:298-314]
- `sentinel_limit` (function) component `sentinel_limit [function]` (`c803ed80-3d42-5e5b-a563-93204e1a04ed`) lines 316-320 [crates/gwiki/src/falkor_graph.rs:316-320]
  - Signature: `fn sentinel_limit(limit: usize) -> anyhow::Result<usize> {`
  - Purpose: Attempts to increment the input limit by one, returning the result or an anyhow error if the addition would overflow. [crates/gwiki/src/falkor_graph.rs:316-320]
- `truncate_to_limit` (function) component `truncate_to_limit [function]` (`7b01def8-5288-56cc-a301-d15e5de5a62b`) lines 322-328 [crates/gwiki/src/falkor_graph.rs:322-328]
  - Signature: `fn truncate_to_limit<T>(rows: &mut Vec<T>, limit: usize) -> bool {`
  - Purpose: This function truncates a mutable vector to a specified limit and returns a boolean indicating whether truncation occurred. [crates/gwiki/src/falkor_graph.rs:322-328]
- `remaining_code_edge_limit` (function) component `remaining_code_edge_limit [function]` (`124b1407-f7a4-58c3-970a-71fd4f7363a6`) lines 330-332 [crates/gwiki/src/falkor_graph.rs:330-332]
  - Signature: `fn remaining_code_edge_limit(configured_limit: usize, remaining_edges: usize) -> Option<usize> {`
  - Purpose: Returns `Some` containing the minimum of `configured_limit` and `remaining_edges` if `remaining_edges` is positive, otherwise returns `None`. [crates/gwiki/src/falkor_graph.rs:330-332]
- `record_code_edge_truncation` (function) component `record_code_edge_truncation [function]` (`99474ed0-9f15-5798-a7d9-935bd802409a`) lines 334-346 [crates/gwiki/src/falkor_graph.rs:334-346]
  - Signature: `fn record_code_edge_truncation(`
  - Purpose: Inserts a truncation component into a set, selecting either a default component (CODE_TOTAL_EDGE_TRUNCATION_COMPONENT) or the provided component based on whether query_limit is less than configured_limit. [crates/gwiki/src/falkor_graph.rs:334-346]
- `truncation_component` (function) component `truncation_component [function]` (`73986137-22f1-5eb0-9b44-bdcf3fb01416`) lines 348-350 [crates/gwiki/src/falkor_graph.rs:348-350]
  - Signature: `fn truncation_component(component: &str, limit: usize) -> String {`
  - Purpose: Formats a string by concatenating a component identifier, a '>' delimiter, and a numeric limit value. [crates/gwiki/src/falkor_graph.rs:348-350]
- `clear_scope` (function) component `clear_scope [function]` (`876468d0-6666-5ecd-bc9e-152fb394f62e`) lines 352-365 [crates/gwiki/src/falkor_graph.rs:352-365]
  - Signature: `fn clear_scope(client: &mut GraphClient, scope: &SearchScope) -> anyhow::Result<()> {`
  - Purpose: Executes a parameterized Cypher query to DETACH DELETE all WikiDoc, WikiSource, and WikiTarget nodes matching a specified scope from the graph database, or errors if the scope cannot be parameterized as a scoped projection. [crates/gwiki/src/falkor_graph.rs:352-365]
- `execute_statement` (function) component `execute_statement [function]` (`a135d49e-1ee8-5e61-a7f6-88454e434184`) lines 367-370 [crates/gwiki/src/falkor_graph.rs:367-370]
  - Signature: `fn execute_statement(client: &mut GraphClient, statement: GraphStatement) -> anyhow::Result<()> {`
  - Purpose: # execute_statement

Executes a Cypher query string from a GraphStatement against a GraphClient, returning a Result that propagates any query execution errors. [crates/gwiki/src/falkor_graph.rs:367-370]
- `query_documents` (function) component `query_documents [function]` (`b49bc1b0-eb12-549b-ae29-f3ec54db3f98`) lines 372-402 [crates/gwiki/src/falkor_graph.rs:372-402]
  - Signature: `fn query_documents(`
  - Purpose: Executes a Cypher query against a GraphClient to retrieve WikiDoc nodes filtered by SearchScope, mapping the results into a LimitedQuery of GraphBoostDocument structs containing file paths and optional titles. [crates/gwiki/src/falkor_graph.rs:372-402]
- `query_links` (function) component `query_links [function]` (`e154fc8c-c0f3-57e6-81bd-1ac738be31a5`) lines 404-439 [crates/gwiki/src/falkor_graph.rs:404-439]
  - Signature: `fn query_links(`
  - Purpose: Executes a Neo4j Cypher query to retrieve wiki document inter-document links (either globally or within a specified scope) up to a limit, returning the results as GraphBoostLink objects mapping source to target paths. [crates/gwiki/src/falkor_graph.rs:404-439]
- `LimitedQuery` (class) component `LimitedQuery [class]` (`047e5fad-9a50-5f8f-ba46-27b6ada0b762`) lines 441-444 [crates/gwiki/src/falkor_graph.rs:441-444]
  - Signature: `struct LimitedQuery<T> {`
  - Purpose: `LimitedQuery<T>` is a generic struct that holds a vector of items and a boolean flag indicating whether the results were capped at a query limit. [crates/gwiki/src/falkor_graph.rs:441-444]
- `query_limited` (function) component `query_limited [function]` (`b24b8c59-e0a6-54b4-a62a-ced84bebb8c5`) lines 446-473 [crates/gwiki/src/falkor_graph.rs:446-473]
  - Signature: `fn query_limited(`
  - Purpose: Executes a FalkorDB query with a LIMIT clause, detects whether results were truncated by fetching an extra sentinel row, and returns the results capped at the specified limit along with a flag indicating overflow. [crates/gwiki/src/falkor_graph.rs:446-473]
- `partial_graph_degradation` (function) component `partial_graph_degradation [function]` (`a884a7f2-a962-5f02-bda3-c868392b389f`) lines 475-486 [crates/gwiki/src/falkor_graph.rs:475-486]
  - Signature: `fn partial_graph_degradation(capped: &[String]) -> Option<DegradationKind> {`
  - Purpose: Constructs a `DegradationKind::PartialData` variant documenting that gwiki_graph exceeded configured capacity limits if the input is non-empty, otherwise returns `None`. [crates/gwiki/src/falkor_graph.rs:475-486]
- `load_wiki_graph_facts` (function) component `load_wiki_graph_facts [function]` (`391d7b3f-7e8a-58cb-80b9-c02c331c99d0`) lines 488-573 [crates/gwiki/src/falkor_graph.rs:488-573]
  - Signature: `pub(crate) fn load_wiki_graph_facts(`
  - Purpose: Loads wiki documents and links filtered by `SearchScope` from a database client, resolves link target references, and returns the aggregated `WikiGraphFacts` structure. [crates/gwiki/src/falkor_graph.rs:488-573]
- `resolve_graph_target` (function) component `resolve_graph_target [function]` (`72f0064f-d5bf-5e6e-a03e-4245dbd56609`) lines 575-607 [crates/gwiki/src/falkor_graph.rs:575-607]
  - Signature: `fn resolve_graph_target(`
  - Purpose: Resolves a wiki link target by normalizing it, attempting direct path matching against available documents, and falling back to slug-based lookup, returning either a resolved path or an unresolved target string. [crates/gwiki/src/falkor_graph.rs:575-607]
- `slug_target_map` (function) component `slug_target_map [function]` (`7b7ba0ac-0c26-5730-911c-9830ff1fff39`) lines 609-617 [crates/gwiki/src/falkor_graph.rs:609-617]
  - Signature: `fn slug_target_map(documents: &[WikiGraphDocument]) -> BTreeMap<String, PathBuf> {`
  - Purpose: Produces a BTreeMap mapping slugified document titles to their corresponding file paths, excluding documents without titles. [crates/gwiki/src/falkor_graph.rs:609-617]
- `resolve_relative_graph_path` (function) component `resolve_relative_graph_path [function]` (`69fe9a26-e786-51dd-be61-5c7ccd05d188`) lines 619-632 [crates/gwiki/src/falkor_graph.rs:619-632]
  - Signature: `fn resolve_relative_graph_path(raw_target: &str, source_path: &Path) -> String {`
  - Purpose: Resolves relative path targets against the parent directory of a source path, while preserving absolute paths and non-path-like targets unchanged. [crates/gwiki/src/falkor_graph.rs:619-632]
- `is_path_like_target` (function) component `is_path_like_target [function]` (`9e22ee27-856d-5636-82b6-e44e8d989c4f`) lines 634-636 [crates/gwiki/src/falkor_graph.rs:634-636]
  - Signature: `fn is_path_like_target(target: &str) -> bool {`
  - Purpose: Returns true if the target string contains a forward slash, starts with a dot, or ends with ".md", indicating a file path. [crates/gwiki/src/falkor_graph.rs:634-636]
- `normalize_path` (function) component `normalize_path [function]` (`d4a38969-fe7d-5829-b62d-55da64b6f49f`) lines 638-651 [crates/gwiki/src/falkor_graph.rs:638-651]
  - Signature: `fn normalize_path(path: PathBuf) -> PathBuf {`
  - Purpose: Normalizes a path by resolving `..` components while discarding `.`, root, and prefix components, yielding a relative path. [crates/gwiki/src/falkor_graph.rs:638-651]
- `code_doc_source_path` (function) component `code_doc_source_path [function]` (`a2fb716d-c983-53b0-8c79-4f0d19c4d825`) lines 653-658 [crates/gwiki/src/falkor_graph.rs:653-658]
  - Signature: `fn code_doc_source_path(path: &Path) -> Option<String> {`
  - Purpose: Converts a normalized file path to a code source identifier by removing the 'code/files/' directory prefix and '.md' file extension. [crates/gwiki/src/falkor_graph.rs:653-658]
- `code_endpoint` (function) component `code_endpoint [function]` (`922f15fd-1267-589f-a066-76db372f589d`) lines 660-666 [crates/gwiki/src/falkor_graph.rs:660-666]
  - Signature: `fn code_endpoint(file_path: &str, symbol: &str) -> String {`
  - Purpose: This function constructs a code reference string by concatenating a file path with an optional symbol using colon notation, returning only the file path if the symbol is empty. [crates/gwiki/src/falkor_graph.rs:660-666]
- `normalize_graph_path` (function) component `normalize_graph_path [function]` (`576e25d8-cf55-5bc5-8ae8-6ef7cd391b57`) lines 668-670 [crates/gwiki/src/falkor_graph.rs:668-670]
  - Signature: `fn normalize_graph_path(path: &Path) -> String {`
  - Purpose: Converts a filesystem Path to a String representation with all backslashes normalized to forward slashes, enabling cross-platform path consistency. [crates/gwiki/src/falkor_graph.rs:668-670]
- `is_external_target` (function) component `is_external_target [function]` (`4c19e976-3a5a-51d6-9e66-bd049b75cdea`) lines 672-680 [crates/gwiki/src/falkor_graph.rs:672-680]
  - Signature: `fn is_external_target(target: &str) -> bool {`
  - Purpose: Determines whether a target string represents an external resource by checking for protocol schemes (http, https, mailto), network paths (//), UNC paths (\\), or arbitrary protocol delimiters (://). [crates/gwiki/src/falkor_graph.rs:672-680]
- `scope_params` (function) component `scope_params [function]` (`a60b910d-6a37-5ead-99c0-41c76ddf38bd`) lines 682-697 [crates/gwiki/src/falkor_graph.rs:682-697]
  - Signature: `fn scope_params(scope: &SearchScope) -> Option<HashMap<String, String>> {`
  - Purpose: Maps a SearchScope's filter tuple to a HashMap of Cypher-escaped string parameters for 'scope_kind' and 'scope_id', returning None if no filter is present. [crates/gwiki/src/falkor_graph.rs:682-697]
- `row_string` (function) component `row_string [function]` (`51ab7fad-ad2f-58ec-a36e-14338f20e119`) lines 699-702 [crates/gwiki/src/falkor_graph.rs:699-702]
  - Signature: `fn row_string(row: &Row, key: &'static str) -> Result<String, SearchError> {`
  - Purpose: Extracts a string value from a Row by key, converting the optional result to a Result type that returns a SearchError::Backend if the key is missing. [crates/gwiki/src/falkor_graph.rs:699-702]
- `optional_row_string` (function) component `optional_row_string [function]` (`24089d0c-03f3-552a-b116-1e992cb3260b`) lines 704-708 [crates/gwiki/src/falkor_graph.rs:704-708]
  - Signature: `fn optional_row_string(row: &Row, key: &'static str) -> Option<String> {`
  - Purpose: Retrieves a value from a row by key and returns an `Option<String>` containing the value as an owned string if it exists and is convertible to a string type, otherwise `None`. [crates/gwiki/src/falkor_graph.rs:704-708]
- `optional_row_usize` (function) component `optional_row_usize [function]` (`1ce14acf-427e-51f8-b12f-4f3fad2fe9f6`) lines 710-714 [crates/gwiki/src/falkor_graph.rs:710-714]
  - Signature: `fn optional_row_usize(row: &Row, key: &'static str) -> Option<usize> {`
  - Purpose: Retrieves a value from a Row by key and returns it as an Option<usize> after converting through u64 with fallible conversions at each step. [crates/gwiki/src/falkor_graph.rs:710-714]
- `cypher_string_literal` (function) component `cypher_string_literal [function]` (`8b4a9cac-352b-590b-9742-34c9e50dcf85`) lines 717-719 [crates/gwiki/src/falkor_graph.rs:717-719]
  - Signature: `fn cypher_string_literal(value: &str) -> String {`
  - Purpose: Converts a string into a Cypher-formatted string literal by escaping its contents and wrapping it in single quotes. [crates/gwiki/src/falkor_graph.rs:717-719]
- `escape_string_contents` (function) component `escape_string_contents [function]` (`1ea7fde2-76b0-59b8-8ea6-faa3075d1b03`) lines 722-739 [crates/gwiki/src/falkor_graph.rs:722-739]
  - Signature: `fn escape_string_contents(value: &str) -> String {`
  - Purpose: Escapes special characters and control characters in a string by replacing them with their corresponding backslash escape sequences or `\uXXXX` Unicode notation. [crates/gwiki/src/falkor_graph.rs:722-739]
- `graph_sync_error` (function) component `graph_sync_error [function]` (`183433d6-60e6-5508-b0a4-d5784158831f`) lines 741-745 [crates/gwiki/src/falkor_graph.rs:741-745]
  - Signature: `fn graph_sync_error(error: anyhow::Error) -> WikiError {`
  - Purpose: Converts an `anyhow::Error` into a `WikiError::Config` variant with a formatted error message describing the failure to synchronize a gwiki graph to FalkorDB. [crates/gwiki/src/falkor_graph.rs:741-745]
- `falkordb_graph_name_is_wiki_owned` (function) component `falkordb_graph_name_is_wiki_owned [function]` (`3c3c5114-7cea-5537-8479-efa867d5256b`) lines 756-759 [crates/gwiki/src/falkor_graph.rs:756-759]
  - Signature: `fn falkordb_graph_name_is_wiki_owned() {`
  - Purpose: This test function asserts that the `FALKORDB_GRAPH_NAME` constant is set to `"gobby_wiki"` and does not equal `"gobby_code"`. [crates/gwiki/src/falkor_graph.rs:756-759]
- `graph_resolution_keeps_unresolved_targets_and_skips_external` (function) component `graph_resolution_keeps_unresolved_targets_and_skips_external [function]` (`30b708f3-2338-5a44-94fb-5fb80193f3ef`) lines 762-805 [crates/gwiki/src/falkor_graph.rs:762-805]
  - Signature: `fn graph_resolution_keeps_unresolved_targets_and_skips_external() {`
  - Purpose: This test verifies that `resolve_graph_target` resolves valid internal targets to their file paths, preserves invalid internal references as unresolved targets, and skips external URLs by returning `None`. [crates/gwiki/src/falkor_graph.rs:762-805]
- `graph_scope_params_are_cypher_string_literals` (function) component `graph_scope_params_are_cypher_string_literals [function]` (`e381b8ed-cbaa-5266-858c-81d20215a7af`) lines 808-819 [crates/gwiki/src/falkor_graph.rs:808-819]
  - Signature: `fn graph_scope_params_are_cypher_string_literals() {`
  - Purpose: # Summary

This function verifies that `scope_params()` correctly formats scope parameters as escaped Cypher string literals with single-quoted values, properly escaping internal quotes using backslash notation. [crates/gwiki/src/falkor_graph.rs:808-819]
- `graph_scope_params_omit_global_scope_filters` (function) component `graph_scope_params_omit_global_scope_filters [function]` (`5d974222-e6fe-5bfb-8e99-b71ceb0f0114`) lines 822-824 [crates/gwiki/src/falkor_graph.rs:822-824]
  - Signature: `fn graph_scope_params_omit_global_scope_filters() {`
  - Purpose: Asserts that `scope_params()` returns `None` when passed a global search scope, verifying that global scope parameters are omitted for unrestricted searches. [crates/gwiki/src/falkor_graph.rs:822-824]
- `ask_unified_graph_code_doc_source_path_maps_to_code_file` (function) component `ask_unified_graph_code_doc_source_path_maps_to_code_file [function]` (`a4361bcc-55b6-5c76-b719-9c291a3c833d`) lines 827-833 [crates/gwiki/src/falkor_graph.rs:827-833]
  - Signature: `fn ask_unified_graph_code_doc_source_path_maps_to_code_file() {`
  - Purpose: Tests that `code_doc_source_path()` correctly extracts source code file paths from documentation markdown files within the 'code/files/' directory structure and returns `None` for non-matching paths. [crates/gwiki/src/falkor_graph.rs:827-833]
- `cypher_string_literal_escapes_like_gcode` (function) component `cypher_string_literal_escapes_like_gcode [function]` (`2f877716-2825-59bb-82f5-33b897035530`) lines 836-841 [crates/gwiki/src/falkor_graph.rs:836-841]
  - Signature: `fn cypher_string_literal_escapes_like_gcode() {`
  - Purpose: This test verifies that `cypher_string_literal()` correctly escapes special characters (quotes, backslashes, and control characters) in a Cypher string literal, encoding them with gcode-compatible escape sequences and wrapping the result in single quotes. [crates/gwiki/src/falkor_graph.rs:836-841]
- `partial_graph_degradation_reports_capped_components` (function) component `partial_graph_degradation_reports_capped_components [function]` (`07d8082a-b9f2-5b67-a6c4-dcb496472f9d`) lines 844-855 [crates/gwiki/src/falkor_graph.rs:844-855]
  - Signature: `fn partial_graph_degradation_reports_capped_components() {`
  - Purpose: Tests that `partial_graph_degradation` with capped component constraints (documents>10, links>20) produces a `PartialData` degradation for the gwiki_graph component with those constraints reflected in the error message. [crates/gwiki/src/falkor_graph.rs:844-855]
- `code_edge_query_params_use_sentinel_limit_and_parameterized_queries` (function) component `code_edge_query_params_use_sentinel_limit_and_parameterized_queries [function]` (`c3a2d43a-83ba-59fa-82e0-3ce6b20e5f21`) lines 858-874 [crates/gwiki/src/falkor_graph.rs:858-874]
  - Signature: `fn code_edge_query_params_use_sentinel_limit_and_parameterized_queries() {`
  - Purpose: This test verifies that code edge queries use parameterized `LIMIT $limit` placeholders instead of hardcoded limits, and validates that the query parameter builder correctly generates sentinel limit values. [crates/gwiki/src/falkor_graph.rs:858-874]
- `truncation_components_name_capped_call_and_import_queries` (function) component `truncation_components_name_capped_call_and_import_queries [function]` (`00263a8c-4fba-5775-8ac6-5285148853a5`) lines 877-886 [crates/gwiki/src/falkor_graph.rs:877-886]
  - Signature: `fn truncation_components_name_capped_call_and_import_queries() {`
  - Purpose: This test function verifies that `truncation_component` correctly formats call and import edge truncation component names with their respective numeric thresholds. [crates/gwiki/src/falkor_graph.rs:877-886]
- `code_edge_query_limit_respects_total_remaining_cap` (function) component `code_edge_query_limit_respects_total_remaining_cap [function]` (`255e1e3b-14b6-550a-826a-cc1bf49a1e89`) lines 889-908 [crates/gwiki/src/falkor_graph.rs:889-908]
  - Signature: `fn code_edge_query_limit_respects_total_remaining_cap() {`
  - Purpose: This test validates that the code edge query limit respects the global capacity constraint by enforcing the minimum of the requested limit and total remaining capacity (or None if exhausted), and properly records truncation events when limits are exceeded. [crates/gwiki/src/falkor_graph.rs:889-908]
- `truncate_to_limit_handles_sentinel_rows_and_zero_limit` (function) component `truncate_to_limit_handles_sentinel_rows_and_zero_limit [function]` (`2abbd0b3-22d8-55df-a006-665245a40d7e`) lines 911-923 [crates/gwiki/src/falkor_graph.rs:911-923]
  - Signature: `fn truncate_to_limit_handles_sentinel_rows_and_zero_limit() {`
  - Purpose: Tests that `truncate_to_limit` truncates a mutable vector to a specified limit and returns true when truncation occurs, false when the vector is already at or below the limit. [crates/gwiki/src/falkor_graph.rs:911-923]
- `graph_write_uses_wiki_labels_and_relationships` (function) component `graph_write_uses_wiki_labels_and_relationships [function]` (`bb1a8622-bcd5-59c0-aebb-8d9e84e9ac2f`) lines 926-978 [crates/gwiki/src/falkor_graph.rs:926-978]
  - Signature: `fn graph_write_uses_wiki_labels_and_relationships() {`
  - Purpose: This function tests that `graph_write_statements()` generates Cypher statements containing all required wiki graph labels and relationship types (documents, sources, targets, links_to, mentions_target, and supports relationships). [crates/gwiki/src/falkor_graph.rs:926-978]

