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
[crates/gwiki/src/falkor_graph.rs:51-54]
[crates/gwiki/src/falkor_graph.rs:56-60]
[crates/gwiki/src/falkor_graph.rs:62-78]
[crates/gwiki/src/falkor_graph.rs:80-104]
[crates/gwiki/src/falkor_graph.rs:106-197]
[crates/gwiki/src/falkor_graph.rs:199-240]
[crates/gwiki/src/falkor_graph.rs:242-250]
[crates/gwiki/src/falkor_graph.rs:252-288]
[crates/gwiki/src/falkor_graph.rs:290-296]
[crates/gwiki/src/falkor_graph.rs:298-314]
[crates/gwiki/src/falkor_graph.rs:316-320]
[crates/gwiki/src/falkor_graph.rs:322-328]
[crates/gwiki/src/falkor_graph.rs:330-332]
[crates/gwiki/src/falkor_graph.rs:334-346]
[crates/gwiki/src/falkor_graph.rs:348-350]
[crates/gwiki/src/falkor_graph.rs:352-365]
[crates/gwiki/src/falkor_graph.rs:367-370]
[crates/gwiki/src/falkor_graph.rs:372-402]
[crates/gwiki/src/falkor_graph.rs:404-439]
[crates/gwiki/src/falkor_graph.rs:441-444]
[crates/gwiki/src/falkor_graph.rs:446-473]
[crates/gwiki/src/falkor_graph.rs:475-486]
[crates/gwiki/src/falkor_graph.rs:488-573]
[crates/gwiki/src/falkor_graph.rs:575-607]
[crates/gwiki/src/falkor_graph.rs:609-617]
[crates/gwiki/src/falkor_graph.rs:619-632]
[crates/gwiki/src/falkor_graph.rs:634-636]
[crates/gwiki/src/falkor_graph.rs:638-651]
[crates/gwiki/src/falkor_graph.rs:653-658]
[crates/gwiki/src/falkor_graph.rs:660-666]
[crates/gwiki/src/falkor_graph.rs:668-670]
[crates/gwiki/src/falkor_graph.rs:672-680]
[crates/gwiki/src/falkor_graph.rs:682-697]
[crates/gwiki/src/falkor_graph.rs:699-702]
[crates/gwiki/src/falkor_graph.rs:704-708]
[crates/gwiki/src/falkor_graph.rs:710-714]
[crates/gwiki/src/falkor_graph.rs:717-719]
[crates/gwiki/src/falkor_graph.rs:722-739]
[crates/gwiki/src/falkor_graph.rs:741-745]
[crates/gwiki/src/falkor_graph.rs:756-759]
[crates/gwiki/src/falkor_graph.rs:762-805]
[crates/gwiki/src/falkor_graph.rs:808-819]
[crates/gwiki/src/falkor_graph.rs:822-824]
[crates/gwiki/src/falkor_graph.rs:827-833]
[crates/gwiki/src/falkor_graph.rs:836-841]
[crates/gwiki/src/falkor_graph.rs:844-855]
[crates/gwiki/src/falkor_graph.rs:858-874]
[crates/gwiki/src/falkor_graph.rs:877-886]
[crates/gwiki/src/falkor_graph.rs:889-908]
[crates/gwiki/src/falkor_graph.rs:911-923]
[crates/gwiki/src/falkor_graph.rs:926-978]

## API Symbols

- `SharedCodeGraphTruncation` (class) component `SharedCodeGraphTruncation [class]` (`69a3ab04-5d4a-5d74-a6ca-f87fea95ac73`) lines 29-31 [crates/gwiki/src/falkor_graph.rs:29-31]
  - Signature: `pub(crate) struct SharedCodeGraphTruncation {`
  - Purpose: A crate-private struct that encapsulates a truncated code graph as a vector of string-identified components. [crates/gwiki/src/falkor_graph.rs:29-31]
- `SharedCodeGraphTruncation` (class) component `SharedCodeGraphTruncation [class]` (`cf143add-c9ff-5468-acc8-9d2fff479423`) lines 33-43 [crates/gwiki/src/falkor_graph.rs:33-43]
  - Signature: `impl SharedCodeGraphTruncation {`
  - Purpose: `SharedCodeGraphTruncation` is a struct that tracks whether a shared code graph has been truncated by maintaining a collection of truncated components and exposing a predicate method that returns true when the collection is non-empty. [crates/gwiki/src/falkor_graph.rs:33-43]
- `SharedCodeGraphTruncation.from_components` (method) component `SharedCodeGraphTruncation.from_components [method]` (`621d8578-6ef8-513c-bfcf-5b6bb10a39d3`) lines 34-38 [crates/gwiki/src/falkor_graph.rs:34-38]
  - Signature: `fn from_components(components: BTreeSet<String>) -> Self {`
  - Purpose: Constructs a Self instance by consuming a BTreeSet<String>, converting it to an iterator, and collecting the elements into the components field. [crates/gwiki/src/falkor_graph.rs:34-38]
- `SharedCodeGraphTruncation.is_truncated` (method) component `SharedCodeGraphTruncation.is_truncated [method]` (`206766fb-8c1a-572a-904d-7b9b49795825`) lines 40-42 [crates/gwiki/src/falkor_graph.rs:40-42]
  - Signature: `pub(crate) fn is_truncated(&self) -> bool {`
  - Purpose: This method returns `true` if the `components` collection is not empty, indicating the presence of components. [crates/gwiki/src/falkor_graph.rs:40-42]
- `SharedCodeGraphEdges` (class) component `SharedCodeGraphEdges [class]` (`ce92d77c-65a3-505b-96be-f3f078a39158`) lines 46-49 [crates/gwiki/src/falkor_graph.rs:46-49]
  - Signature: `pub(crate) struct SharedCodeGraphEdges {`
  - Purpose: `SharedCodeGraphEdges` is a crate-private struct that encapsulates a vector of `WikiGraphCodeEdge` items alongside `SharedCodeGraphTruncation` metadata to represent a collection of code graph edges with potential truncation state. [crates/gwiki/src/falkor_graph.rs:46-49]
- `LimitedCodeGraphEdges` (class) component `LimitedCodeGraphEdges [class]` (`e563cd50-b372-5093-a5b3-1e55277135b7`) lines 51-54 [crates/gwiki/src/falkor_graph.rs:51-54]
  - Signature: `struct LimitedCodeGraphEdges {`
  - Purpose: `LimitedCodeGraphEdges` is a struct that wraps a vector of `WikiGraphCodeEdge` objects with a boolean flag indicating whether the result set was truncated. [crates/gwiki/src/falkor_graph.rs:51-54]
- `GraphBoostData` (class) component `GraphBoostData [class]` (`de8a1f8c-e141-5fff-a7f7-32559e404007`) lines 56-60 [crates/gwiki/src/falkor_graph.rs:56-60]
  - Signature: `pub(crate) struct GraphBoostData {`
  - Purpose: `GraphBoostData` is a crate-private struct that encapsulates documents, their interconnecting links, and an optional degradation mode for graph-based search ranking. [crates/gwiki/src/falkor_graph.rs:56-60]
- `sync_scope_from_postgres` (function) component `sync_scope_from_postgres [function]` (`c21f11b5-8376-5e3a-be3d-b82dbfe434d8`) lines 62-78 [crates/gwiki/src/falkor_graph.rs:62-78]
  - Signature: `pub(crate) fn sync_scope_from_postgres(`
  - Purpose: Synchronizes wiki graph facts from PostgreSQL to FalkorDB by clearing the target scope and executing graph write statements for the loaded facts. [crates/gwiki/src/falkor_graph.rs:62-78]
- `load_graph_boost_data` (function) component `load_graph_boost_data [function]` (`c7baf74a-98e2-5284-9203-0e4c8659f8fb`) lines 80-104 [crates/gwiki/src/falkor_graph.rs:80-104]
  - Signature: `pub(crate) fn load_graph_boost_data(`
  - Purpose: Queries documents and links from a graph database within specified limits, detects result truncation on either dataset, and returns the items with optional degradation metadata if capping occurred. [crates/gwiki/src/falkor_graph.rs:80-104]
- `load_code_graph_edges` (function) component `load_code_graph_edges [function]` (`8e5ef180-3f2c-5637-867c-53a04f2ce546`) lines 106-197 [crates/gwiki/src/falkor_graph.rs:106-197]
  - Signature: `pub(crate) fn load_code_graph_edges(`
  - Purpose: Loads code call edges from a graph database for filtered code documents, enforcing configurable per-component and total edge limits while tracking truncation metadata. [crates/gwiki/src/falkor_graph.rs:106-197]
- `code_call_edges` (function) component `code_call_edges [function]` (`cc910344-3638-5610-9542-35621556eee5`) lines 199-240 [crates/gwiki/src/falkor_graph.rs:199-240]
  - Signature: `fn code_call_edges(`
  - Purpose: Retrieves function call edges for a specified file from a code graph database, classifies them as incoming (callers) or outgoing (calls) based on direction, and returns them as structured `WikiGraphCodeEdge` objects with directional metadata and optional truncation. [crates/gwiki/src/falkor_graph.rs:199-240]
- `code_call_edges_query` (function) component `code_call_edges_query [function]` (`7531ab0d-8c04-5d4c-a2d7-d7497abe1d2f`) lines 242-250 [crates/gwiki/src/falkor_graph.rs:242-250]
  - Signature: `fn code_call_edges_query() -> &'static str {`
  - Purpose: Returns a Neo4j Cypher query that retrieves all function call edges between CodeSymbols in a specified project and file path, including caller/callee names and line numbers. [crates/gwiki/src/falkor_graph.rs:242-250]
- `code_import_edges` (function) component `code_import_edges [function]` (`d7c0ba60-6a15-5c75-8ea5-30393f847a02`) lines 252-288 [crates/gwiki/src/falkor_graph.rs:252-288]
  - Signature: `fn code_import_edges(`
  - Purpose: Retrieves outgoing import edges for a specified file from a code graph database, maps the query results to WikiGraphCodeEdge objects, and returns them with truncation tracking. [crates/gwiki/src/falkor_graph.rs:252-288]
- `code_import_edges_query` (function) component `code_import_edges_query [function]` (`dac2d5e9-6cf0-5128-b60e-099c92d89f86`) lines 290-296 [crates/gwiki/src/falkor_graph.rs:290-296]
  - Signature: `fn code_import_edges_query() -> &'static str {`
  - Purpose: Returns a static Cypher query string that retrieves IMPORTS relationship edges from a specified CodeFile node to its dependent CodeModule nodes, projecting source file path and target module name. [crates/gwiki/src/falkor_graph.rs:290-296]
- `code_edge_query_params` (function) component `code_edge_query_params [function]` (`a4ee429f-cef2-57d2-834a-baf7af6fd3a3`) lines 298-314 [crates/gwiki/src/falkor_graph.rs:298-314]
  - Signature: `fn code_edge_query_params(`
  - Purpose: Constructs and returns a HashMap of URL-encoded query parameters (project, path, limit) for code edge requests, with string values escaped and limit validated. [crates/gwiki/src/falkor_graph.rs:298-314]
- `sentinel_limit` (function) component `sentinel_limit [function]` (`561c608f-576b-56a5-bb27-3ad756327ed9`) lines 316-320 [crates/gwiki/src/falkor_graph.rs:316-320]
  - Signature: `fn sentinel_limit(limit: usize) -> anyhow::Result<usize> {`
  - Purpose: Adds one to a `usize` limit with overflow checking, returning the incremented value or an error if the addition would overflow. [crates/gwiki/src/falkor_graph.rs:316-320]
- `truncate_to_limit` (function) component `truncate_to_limit [function]` (`2948ec58-9396-5d23-834c-5d4e007d369b`) lines 322-328 [crates/gwiki/src/falkor_graph.rs:322-328]
  - Signature: `fn truncate_to_limit<T>(rows: &mut Vec<T>, limit: usize) -> bool {`
  - Purpose: Truncates a generic vector to a maximum length and returns a boolean indicating whether the truncation was performed. [crates/gwiki/src/falkor_graph.rs:322-328]
- `remaining_code_edge_limit` (function) component `remaining_code_edge_limit [function]` (`05e70971-8735-5cc7-b31c-121e9bf55526`) lines 330-332 [crates/gwiki/src/falkor_graph.rs:330-332]
  - Signature: `fn remaining_code_edge_limit(configured_limit: usize, remaining_edges: usize) -> Option<usize> {`
  - Purpose: Returns `Some` containing the minimum of the configured limit and remaining edges if any edges remain, otherwise `None`. [crates/gwiki/src/falkor_graph.rs:330-332]
- `record_code_edge_truncation` (function) component `record_code_edge_truncation [function]` (`7eeea5e9-dd55-5011-a1ae-374403a187b3`) lines 334-346 [crates/gwiki/src/falkor_graph.rs:334-346]
  - Signature: `fn record_code_edge_truncation(`
  - Purpose: Inserts a code edge truncation component into a BTreeSet, using a global default truncation configuration when query_limit is less than configured_limit, otherwise using the provided component. [crates/gwiki/src/falkor_graph.rs:334-346]
- `truncation_component` (function) component `truncation_component [function]` (`bd249107-e3b0-52f2-aa69-2bdd3c410013`) lines 348-350 [crates/gwiki/src/falkor_graph.rs:348-350]
  - Signature: `fn truncation_component(component: &str, limit: usize) -> String {`
  - Purpose: Creates a formatted string by concatenating the input component string and limit value with a `>` delimiter. [crates/gwiki/src/falkor_graph.rs:348-350]
- `clear_scope` (function) component `clear_scope [function]` (`c56b5746-9214-54bd-9829-4cab5b701d3f`) lines 352-365 [crates/gwiki/src/falkor_graph.rs:352-365]
  - Signature: `fn clear_scope(client: &mut GraphClient, scope: &SearchScope) -> anyhow::Result<()> {`
  - Purpose: # Summary

Deletes all WikiDoc, WikiSource, and WikiTarget nodes from a graph database matching the provided scope via a parameterized Cypher DETACH DELETE query, or errors if the scope is global. [crates/gwiki/src/falkor_graph.rs:352-365]
- `execute_statement` (function) component `execute_statement [function]` (`6f7a4115-4be0-5ee3-8816-69a82d2404f8`) lines 367-370 [crates/gwiki/src/falkor_graph.rs:367-370]
  - Signature: `fn execute_statement(client: &mut GraphClient, statement: GraphStatement) -> anyhow::Result<()> {`
  - Purpose: Executes a Cypher query extracted from a GraphStatement against the provided GraphClient. [crates/gwiki/src/falkor_graph.rs:367-370]
- `query_documents` (function) component `query_documents [function]` (`71f12a12-2336-58bf-a02d-8df16f816f6b`) lines 372-402 [crates/gwiki/src/falkor_graph.rs:372-402]
  - Signature: `fn query_documents(`
  - Purpose: Executes a scope-filtered Cypher query to retrieve WikiDoc nodes from a graph database, returning a limited result set of documents as `GraphBoostDocument` objects with paths and optional titles. [crates/gwiki/src/falkor_graph.rs:372-402]
- `query_links` (function) component `query_links [function]` (`48fa7739-b1a1-5d6c-b73c-ec75067aa0ae`) lines 404-439 [crates/gwiki/src/falkor_graph.rs:404-439]
  - Signature: `fn query_links(`
  - Purpose: Queries a graph database to retrieve wiki document hyperlinks (WIKI_LINKS_TO relationships) within a specified scope, returning a paginated result set of source-to-target document path pairs. [crates/gwiki/src/falkor_graph.rs:404-439]
- `LimitedQuery` (class) component `LimitedQuery [class]` (`a37adf07-2cef-5ee1-bd7e-82c1ff46c475`) lines 441-444 [crates/gwiki/src/falkor_graph.rs:441-444]
  - Signature: `struct LimitedQuery<T> {`
  - Purpose: LimitedQuery<T> is a generic struct that wraps a vector of items and a boolean flag indicating whether the result set has been capped to a maximum size limit. [crates/gwiki/src/falkor_graph.rs:441-444]
- `query_limited` (function) component `query_limited [function]` (`d27d3350-3293-5a16-9ff7-88e166b862f2`) lines 446-473 [crates/gwiki/src/falkor_graph.rs:446-473]
  - Signature: `fn query_limited(`
  - Purpose: Executes a FalkorDB query with a sentinel-row (+1) limit pattern to detect truncation, returning at most the requested number of rows along with a boolean flag indicating whether more results exist. [crates/gwiki/src/falkor_graph.rs:446-473]
- `partial_graph_degradation` (function) component `partial_graph_degradation [function]` (`f489da9a-0a73-50b1-bc6d-badf19cb5e88`) lines 475-486 [crates/gwiki/src/falkor_graph.rs:475-486]
  - Signature: `fn partial_graph_degradation(capped: &[String]) -> Option<DegradationKind> {`
  - Purpose: This function constructs a `DegradationKind::PartialData` variant indicating that the gwiki_graph component exceeded configured capacity constraints (listing the violated caps), or returns `None` if the input slice is empty. [crates/gwiki/src/falkor_graph.rs:475-486]
- `load_wiki_graph_facts` (function) component `load_wiki_graph_facts [function]` (`9f7a9c12-cdb1-5aa4-bc52-a080a96ab669`) lines 488-573 [crates/gwiki/src/falkor_graph.rs:488-573]
  - Signature: `pub(crate) fn load_wiki_graph_facts(`
  - Purpose: Queries a database to retrieve wiki documents and inter-document links for a given scope, resolves link targets to canonical document paths, and returns the aggregated WikiGraphFacts structure. [crates/gwiki/src/falkor_graph.rs:488-573]
- `resolve_graph_target` (function) component `resolve_graph_target [function]` (`d2afe17e-b7e9-5a08-b42f-02b510d9e290`) lines 575-607 [crates/gwiki/src/falkor_graph.rs:575-607]
  - Signature: `fn resolve_graph_target(`
  - Purpose: Resolves a wiki link target to an optional WikiGraphLinkTarget by normalizing the input and matching against document paths directly or via slug lookup, returning None for external or empty targets. [crates/gwiki/src/falkor_graph.rs:575-607]
- `slug_target_map` (function) component `slug_target_map [function]` (`43b51f74-a07f-5880-b686-dd64494561de`) lines 609-617 [crates/gwiki/src/falkor_graph.rs:609-617]
  - Signature: `fn slug_target_map(documents: &[WikiGraphDocument]) -> BTreeMap<String, PathBuf> {`
  - Purpose: Returns a `BTreeMap` that maps each WikiGraphDocument's slugified title to its filesystem path. [crates/gwiki/src/falkor_graph.rs:609-617]
- `resolve_relative_graph_path` (function) component `resolve_relative_graph_path [function]` (`436a1305-13b0-590f-87ff-c4319c4830e5`) lines 619-632 [crates/gwiki/src/falkor_graph.rs:619-632]
  - Signature: `fn resolve_relative_graph_path(raw_target: &str, source_path: &Path) -> String {`
  - Purpose: Resolves a relative graph path reference by joining it with the source path's parent directory if the target is path-like and non-absolute, otherwise returns the normalized target unchanged. [crates/gwiki/src/falkor_graph.rs:619-632]
- `is_path_like_target` (function) component `is_path_like_target [function]` (`28dd9a97-8d0c-59d6-8a29-df95d3265805`) lines 634-636 [crates/gwiki/src/falkor_graph.rs:634-636]
  - Signature: `fn is_path_like_target(target: &str) -> bool {`
  - Purpose: Returns `true` if the target string contains a forward slash, starts with a dot, or ends with `.md`, indicating a path-like or markdown file reference. [crates/gwiki/src/falkor_graph.rs:634-636]
- `normalize_path` (function) component `normalize_path [function]` (`49ef6a0d-a00b-519a-85fe-96ebed09cd80`) lines 638-651 [crates/gwiki/src/falkor_graph.rs:638-651]
  - Signature: `fn normalize_path(path: PathBuf) -> PathBuf {`
  - Purpose: Normalizes a path by resolving parent (`..`) and current (`.`) directory references while excluding root directory and filesystem prefix components, returning a relative path structure. [crates/gwiki/src/falkor_graph.rs:638-651]
- `code_doc_source_path` (function) component `code_doc_source_path [function]` (`aa972abe-5b67-5b84-8cd4-53c72b0357ee`) lines 653-658 [crates/gwiki/src/falkor_graph.rs:653-658]
  - Signature: `fn code_doc_source_path(path: &Path) -> Option<String> {`
  - Purpose: Normalizes a path and returns the source file path by stripping the "code/files/" prefix and ".md" suffix, or None if any operation fails. [crates/gwiki/src/falkor_graph.rs:653-658]
- `code_endpoint` (function) component `code_endpoint [function]` (`fc37e9ac-eaf6-5074-96eb-64debbbcddeb`) lines 660-666 [crates/gwiki/src/falkor_graph.rs:660-666]
  - Signature: `fn code_endpoint(file_path: &str, symbol: &str) -> String {`
  - Purpose: This function constructs a code endpoint reference string by concatenating `file_path` and `symbol` with a colon separator, or returns `file_path` alone if `symbol` is empty. [crates/gwiki/src/falkor_graph.rs:660-666]
- `normalize_graph_path` (function) component `normalize_graph_path [function]` (`4dbc8b06-2c0a-5321-94d1-b311cf304ba2`) lines 668-670 [crates/gwiki/src/falkor_graph.rs:668-670]
  - Signature: `fn normalize_graph_path(path: &Path) -> String {`
  - Purpose: Converts a file path to a UTF-8 string with all backslashes normalized to forward slashes. [crates/gwiki/src/falkor_graph.rs:668-670]
- `is_external_target` (function) component `is_external_target [function]` (`a6968a60-4f47-59c1-b2f7-bbaca6625e82`) lines 672-680 [crates/gwiki/src/falkor_graph.rs:672-680]
  - Signature: `fn is_external_target(target: &str) -> bool {`
  - Purpose: Returns `true` if the target string references an external resource, detected by checking for protocol schemes (http, https, mailto), network paths (//), UNC paths (\\), or any string containing `://`. [crates/gwiki/src/falkor_graph.rs:672-680]
- `scope_params` (function) component `scope_params [function]` (`99634529-f1c5-5945-89f9-d20d05504a5e`) lines 682-697 [crates/gwiki/src/falkor_graph.rs:682-697]
  - Signature: `fn scope_params(scope: &SearchScope) -> Option<HashMap<String, String>> {`
  - Purpose: Transforms a `SearchScope`'s filter components into a `HashMap` of Cypher-escaped scope_kind and scope_id key-value pairs for falkordb parameter interpolation. [crates/gwiki/src/falkor_graph.rs:682-697]
- `row_string` (function) component `row_string [function]` (`a6ead3a4-1fea-5f58-8036-e10fdfd45be4`) lines 699-702 [crates/gwiki/src/falkor_graph.rs:699-702]
  - Signature: `fn row_string(row: &Row, key: &'static str) -> Result<String, SearchError> {`
  - Purpose: Unwraps an optional string from a database row by key, converting a None value into a SearchError with a message indicating the missing FalkorDB wiki graph field. [crates/gwiki/src/falkor_graph.rs:699-702]
- `optional_row_string` (function) component `optional_row_string [function]` (`e735c901-a231-50e7-90bc-6cee3f1ffbb5`) lines 704-708 [crates/gwiki/src/falkor_graph.rs:704-708]
  - Signature: `fn optional_row_string(row: &Row, key: &'static str) -> Option<String> {`
  - Purpose: Retrieves a value from a row by key, converts it to a string reference if available, and returns an owned String wrapped in an Option. [crates/gwiki/src/falkor_graph.rs:704-708]
- `optional_row_usize` (function) component `optional_row_usize [function]` (`b59baf89-9507-58d1-9804-8b2b5cb2ef89`) lines 710-714 [crates/gwiki/src/falkor_graph.rs:710-714]
  - Signature: `fn optional_row_usize(row: &Row, key: &'static str) -> Option<usize> {`
  - Purpose: Retrieves a value from a `Row` by key and converts it to `usize` through intermediate `u64` conversion, returning `None` if any step fails. [crates/gwiki/src/falkor_graph.rs:710-714]
- `cypher_string_literal` (function) component `cypher_string_literal [function]` (`0bc3b22f-dee2-54aa-a3d6-04610311bc3e`) lines 717-719 [crates/gwiki/src/falkor_graph.rs:717-719]
  - Signature: `fn cypher_string_literal(value: &str) -> String {`
  - Purpose: Encodes a string as a Cypher string literal by escaping special characters and wrapping the result in single quotes. [crates/gwiki/src/falkor_graph.rs:717-719]
- `escape_string_contents` (function) component `escape_string_contents [function]` (`491b9d3c-c2a6-530e-a535-1ddd1b62394d`) lines 722-739 [crates/gwiki/src/falkor_graph.rs:722-739]
  - Signature: `fn escape_string_contents(value: &str) -> String {`
  - Purpose: This function escapes a string by replacing backslashes, quotes, whitespace control characters, and non-printable control characters with their corresponding backslash escape sequences or `\uXXXX` Unicode escape sequences. [crates/gwiki/src/falkor_graph.rs:722-739]
- `graph_sync_error` (function) component `graph_sync_error [function]` (`2351cf34-e277-55e4-9bdc-0cda1955aad4`) lines 741-745 [crates/gwiki/src/falkor_graph.rs:741-745]
  - Signature: `fn graph_sync_error(error: anyhow::Error) -> WikiError {`
  - Purpose: Converts an `anyhow::Error` into a `WikiError::Config` variant with a formatted error message describing a failed gwiki graph synchronization to FalkorDB. [crates/gwiki/src/falkor_graph.rs:741-745]
- `falkordb_graph_name_is_wiki_owned` (function) component `falkordb_graph_name_is_wiki_owned [function]` (`32653c7d-15fc-5edf-8c7a-e5d65bce7739`) lines 756-759 [crates/gwiki/src/falkor_graph.rs:756-759]
  - Signature: `fn falkordb_graph_name_is_wiki_owned() {`
  - Purpose: This function tests that the `FALKORDB_GRAPH_NAME` constant is set to `"gobby_wiki"` and does not equal `"gobby_code"`. [crates/gwiki/src/falkor_graph.rs:756-759]
- `graph_resolution_keeps_unresolved_targets_and_skips_external` (function) component `graph_resolution_keeps_unresolved_targets_and_skips_external [function]` (`927ce41a-7d19-5ceb-84b6-0f7be00c23ea`) lines 762-805 [crates/gwiki/src/falkor_graph.rs:762-805]
  - Signature: `fn graph_resolution_keeps_unresolved_targets_and_skips_external() {`
  - Purpose: This unit test verifies that `resolve_graph_target` correctly resolves document slugs to their file paths, preserves unresolved internal link targets, and filters out external URLs by returning `None`. [crates/gwiki/src/falkor_graph.rs:762-805]
- `graph_scope_params_are_cypher_string_literals` (function) component `graph_scope_params_are_cypher_string_literals [function]` (`8e2bad04-6782-545a-809e-f18af9e0bd8b`) lines 808-819 [crates/gwiki/src/falkor_graph.rs:808-819]
  - Signature: `fn graph_scope_params_are_cypher_string_literals() {`
  - Purpose: This test asserts that `scope_params()` correctly formats `SearchScope` parameters as Cypher string literals with proper single-quote escaping for both the scope kind and scope ID. [crates/gwiki/src/falkor_graph.rs:808-819]
- `graph_scope_params_omit_global_scope_filters` (function) component `graph_scope_params_omit_global_scope_filters [function]` (`0f624a1e-7a01-5aa9-8bf2-e1739fd6cb5b`) lines 822-824 [crates/gwiki/src/falkor_graph.rs:822-824]
  - Signature: `fn graph_scope_params_omit_global_scope_filters() {`
  - Purpose: This test function asserts that `scope_params()` returns `None` when passed a global search scope, verifying that scope parameters are not generated for global scopes. [crates/gwiki/src/falkor_graph.rs:822-824]
- `ask_unified_graph_code_doc_source_path_maps_to_code_file` (function) component `ask_unified_graph_code_doc_source_path_maps_to_code_file [function]` (`532dad87-4248-5008-b3e6-371a9f0adccf`) lines 827-833 [crates/gwiki/src/falkor_graph.rs:827-833]
  - Signature: `fn ask_unified_graph_code_doc_source_path_maps_to_code_file() {`
  - Purpose: This test function verifies that `code_doc_source_path` correctly extracts the underlying source code file path from documentation file paths (removing `.md` extension and `code/files/` prefix) while returning `None` for non-code-associated documentation. [crates/gwiki/src/falkor_graph.rs:827-833]
- `cypher_string_literal_escapes_like_gcode` (function) component `cypher_string_literal_escapes_like_gcode [function]` (`b3373679-8575-5a38-bd43-b69a41738810`) lines 836-841 [crates/gwiki/src/falkor_graph.rs:836-841]
  - Signature: `fn cypher_string_literal_escapes_like_gcode() {`
  - Purpose: Verifies that `cypher_string_literal` correctly escapes quotes, backslashes, and control characters according to Cypher string literal escape sequence syntax. [crates/gwiki/src/falkor_graph.rs:836-841]
- `partial_graph_degradation_reports_capped_components` (function) component `partial_graph_degradation_reports_capped_components [function]` (`cca0d811-012f-580f-9f0d-2329a7a47da0`) lines 844-855 [crates/gwiki/src/falkor_graph.rs:844-855]
  - Signature: `fn partial_graph_degradation_reports_capped_components() {`
  - Purpose: Tests that `partial_graph_degradation()` with capped component thresholds (`documents>10`, `links>20`) returns a `DegradationKind::PartialData` variant for the `gwiki_graph` component with both threshold constraints reflected in the error message. [crates/gwiki/src/falkor_graph.rs:844-855]
- `code_edge_query_params_use_sentinel_limit_and_parameterized_queries` (function) component `code_edge_query_params_use_sentinel_limit_and_parameterized_queries [function]` (`8cfb0b01-6f42-5562-98cb-2e88f8b87903`) lines 858-874 [crates/gwiki/src/falkor_graph.rs:858-874]
  - Signature: `fn code_edge_query_params_use_sentinel_limit_and_parameterized_queries() {`
  - Purpose: Verifies that code edge query functions use parameterized sentinel limits via `LIMIT toInteger($limit)` instead of hardcoded constants, and validates the generated query parameters contain the correct limit value. [crates/gwiki/src/falkor_graph.rs:858-874]
- `truncation_components_name_capped_call_and_import_queries` (function) component `truncation_components_name_capped_call_and_import_queries [function]` (`b6611b48-2c70-5cd6-982e-d8f6e14223f0`) lines 877-886 [crates/gwiki/src/falkor_graph.rs:877-886]
  - Signature: `fn truncation_components_name_capped_call_and_import_queries() {`
  - Purpose: Tests that `truncation_component` generates correctly formatted truncation query strings for code call and import edge components with specified threshold values. [crates/gwiki/src/falkor_graph.rs:877-886]
- `code_edge_query_limit_respects_total_remaining_cap` (function) component `code_edge_query_limit_respects_total_remaining_cap [function]` (`127eacff-e184-5896-b6d6-7e4528801f7b`) lines 889-908 [crates/gwiki/src/falkor_graph.rs:889-908]
  - Signature: `fn code_edge_query_limit_respects_total_remaining_cap() {`
  - Purpose: This test validates that the remaining code edge query limit respects a total capacity cap by returning the minimum between the requested limit and remaining total, and records truncation metadata when the cap becomes the binding constraint. [crates/gwiki/src/falkor_graph.rs:889-908]
- `truncate_to_limit_handles_sentinel_rows_and_zero_limit` (function) component `truncate_to_limit_handles_sentinel_rows_and_zero_limit [function]` (`4d355e8e-9ca0-57c6-9f44-6c27f7528302`) lines 911-923 [crates/gwiki/src/falkor_graph.rs:911-923]
  - Signature: `fn truncate_to_limit_handles_sentinel_rows_and_zero_limit() {`
  - Purpose: Verifies that `truncate_to_limit` truncates a mutable row vector to the requested maximum length, empties it when the limit is `0`, and returns `false` without modifying the vector when it is already at the limit. [crates/gwiki/src/falkor_graph.rs:911-923]
- `graph_write_uses_wiki_labels_and_relationships` (function) component `graph_write_uses_wiki_labels_and_relationships [function]` (`ada32c91-f508-561d-89c7-a24b6836dd58`) lines 926-978 [crates/gwiki/src/falkor_graph.rs:926-978]
  - Signature: `fn graph_write_uses_wiki_labels_and_relationships() {`
  - Purpose: It builds a `WikiGraphFacts` fixture with two documents, one resolved and one unresolved wiki link, and one source edge, then verifies that `graph_write_statements(&facts)` emits Cypher containing the wiki document/source/target labels and the `LINKS_TO`, `MENTIONS_TARGET`, and `SUPPORTS` relationship types. [crates/gwiki/src/falkor_graph.rs:926-978]

