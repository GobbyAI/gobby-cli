---
title: crates/gcode/src/contract.rs
type: code_file
provenance:
- file: crates/gcode/src/contract.rs
  ranges:
  - 5-288
  - 290-292
  - 294-297
  - 299-306
  - 308-320
  - 322-328
  - 330-348
  - 350-373
  - 375-391
  - 393-403
  - 405-407
  - 409-421
  - 423-431
  - 433-445
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/contract.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Defines the `gcode` CLI’s versioned `CliContract`, including its tool metadata, global flags, project-scope detection, and the daemon-consumed `contract` and `index` commands with their positionals, flags, and JSON output keys. The helper functions factor out reusable flag contracts and fixed key lists for search, grep, graph read, cleanup, vector cleanup, and contract payloads so the command schema stays consistent across the CLI and daemon output.
[crates/gcode/src/contract.rs:5-288]
[crates/gcode/src/contract.rs:290-292]
[crates/gcode/src/contract.rs:294-297]
[crates/gcode/src/contract.rs:299-306]
[crates/gcode/src/contract.rs:308-320]

## API Symbols

- `contract` (function) component `contract [function]` (`41472832-6151-5685-ba9f-58ae5a756e29`) lines 5-288 [crates/gcode/src/contract.rs:5-288]
  - Signature: `pub fn contract() -> CliContract {`
  - Purpose: Constructs and returns a 'CliContract' for the 'gcode' CLI, defining its versioned interface, global flags and project scope resolution, and the supported 'contract' and 'index' daemon-consumed commands with their flags, positionals, and JSON output keys. [crates/gcode/src/contract.rs:5-288]
- `format_flag` (function) component `format_flag [function]` (`9c09617f-99ea-5bc6-9b4a-990a5e6543cb`) lines 290-292 [crates/gcode/src/contract.rs:290-292]
  - Signature: `fn format_flag() -> FlagContract {`
  - Purpose: Returns a 'FlagContract' for the '--format' CLI flag with value hint 'json|text' and an अनुमति list restricted to 'json' and 'text'. [crates/gcode/src/contract.rs:290-292]
- `ai_flag` (function) component `ai_flag [function]` (`e2e911f2-b973-505d-b6c0-912b8c3eec97`) lines 294-297 [crates/gcode/src/contract.rs:294-297]
  - Signature: `fn ai_flag() -> FlagContract {`
  - Purpose: Returns a 'FlagContract' for the '--ai' option with the value spec 'auto|daemon|direct|off' and restricts it to those four allowed strings. [crates/gcode/src/contract.rs:294-297]
- `search_flags` (function) component `search_flags [function]` (`5665327b-baf5-5091-9cd5-e0cde9849f1c`) lines 299-306 [crates/gcode/src/contract.rs:299-306]
  - Signature: `fn search_flags() -> Vec<FlagContract> {`
  - Purpose: Returns a 'Vec<FlagContract>' describing four CLI value flags: '--limit N', '--offset N', '--kind KIND', and '--language LANG'. [crates/gcode/src/contract.rs:299-306]
- `grep_flags` (function) component `grep_flags [function]` (`0410e10b-aab3-5683-96f1-e51d78450fa0`) lines 308-320 [crates/gcode/src/contract.rs:308-320]
  - Signature: `fn grep_flags() -> Vec<FlagContract> {`
  - Purpose: Returns a vector of 'FlagContract's describing supported 'grep'-style options: fixed strings, ignore case, whole-word matching, before/after/context counts, repeatable glob filters, max count, and a formatting flag. [crates/gcode/src/contract.rs:308-320]
- `graph_read_flags` (function) component `graph_read_flags [function]` (`5de7b45a-0ea3-5196-ae1e-65cb92342ad9`) lines 322-328 [crates/gcode/src/contract.rs:322-328]
  - Signature: `fn graph_read_flags() -> Vec<FlagContract> {`
  - Purpose: Returns a 'Vec<FlagContract>' containing the '--limit N' and '--offset N' value flags plus the standard 'format_flag()' entry. [crates/gcode/src/contract.rs:322-328]
- `search_keys` (function) component `search_keys [function]` (`755696f1-076a-5f26-9dc5-00c15bbdffc3`) lines 330-348 [crates/gcode/src/contract.rs:330-348]
  - Signature: `fn search_keys() -> Vec<&'static str> {`
  - Purpose: Returns a fixed 'Vec<&'static str>' containing the ordered list of searchable field keys: 'project_id', 'total', 'offset', 'limit', 'results', 'id', 'name', 'qualified_name', 'kind', 'language', 'file_path', 'line_start', 'line_end', 'signature', and 'score'. [crates/gcode/src/contract.rs:330-348]
- `grep_keys` (function) component `grep_keys [function]` (`3eeb8bfb-187f-526f-bc0d-b482b4a1ef34`) lines 350-373 [crates/gcode/src/contract.rs:350-373]
  - Signature: `fn grep_keys() -> Vec<&'static str> {`
  - Purpose: Returns a fixed vector of static string field names used for grep-style query, result, and match metadata serialization. [crates/gcode/src/contract.rs:350-373]
- `graph_read_keys` (function) component `graph_read_keys [function]` (`c5695556-299b-5f46-9225-11c5f51db35d`) lines 375-391 [crates/gcode/src/contract.rs:375-391]
  - Signature: `fn graph_read_keys() -> Vec<&'static str> {`
  - Purpose: Returns a vector of static string keys used by the graph reader: 'project_id', 'total', 'offset', 'limit', 'results', 'id', 'name', 'file_path', 'line', 'relation', 'distance', 'metadata', and 'hint'. [crates/gcode/src/contract.rs:375-391]
- `contract_keys` (function) component `contract_keys [function]` (`b745d5ed-1cc1-5c17-90b1-893aa1620018`) lines 393-403 [crates/gcode/src/contract.rs:393-403]
  - Signature: `fn contract_keys() -> Vec<&'static str> {`
  - Purpose: Returns a vector of the seven static contract field names: 'tool', 'contract_version', 'summary', 'global_flags', 'scope', 'commands', and 'error_codes'. [crates/gcode/src/contract.rs:393-403]
- `graph_payload_keys` (function) component `graph_payload_keys [function]` (`41bc9137-aaf2-560e-beb3-9b6efa7b2bee`) lines 405-407 [crates/gcode/src/contract.rs:405-407]
  - Signature: `fn graph_payload_keys() -> Vec<&'static str> {`
  - Purpose: Returns a static vector containing the three graph payload field names: '"nodes"', '"links"', and '"summary"'. [crates/gcode/src/contract.rs:405-407]
- `graph_lifecycle_keys` (function) component `graph_lifecycle_keys [function]` (`d3445a60-fe41-550d-9673-5454f285265d`) lines 409-421 [crates/gcode/src/contract.rs:409-421]
  - Signature: `fn graph_lifecycle_keys() -> Vec<&'static str> {`
  - Purpose: Returns a static vector of lifecycle-state field names for a graph, listing status, action, project_id, sync and deletion counters, and summary. [crates/gcode/src/contract.rs:409-421]
- `graph_cleanup_keys` (function) component `graph_cleanup_keys [function]` (`66f16e24-1c8e-5c91-b027-92c63ae1639c`) lines 423-431 [crates/gcode/src/contract.rs:423-431]
  - Signature: `fn graph_cleanup_keys() -> Vec<&'static str> {`
  - Purpose: Returns a vector of static string keys used to report graph cleanup state and counts: 'status', 'action', 'project_id', 'stale_graph_files_deleted', and 'graph_nodes_deleted'. [crates/gcode/src/contract.rs:423-431]
- `vector_cleanup_keys` (function) component `vector_cleanup_keys [function]` (`eaba3079-cfb6-5037-8986-efc20d820870`) lines 433-445 [crates/gcode/src/contract.rs:433-445]
  - Signature: `fn vector_cleanup_keys() -> Vec<&'static str> {`
  - Purpose: Returns a static vector of cleanup-related key names for vector operations: 'project_id', 'projection', 'action', 'collection', 'status', 'vector_files_scanned', 'orphan_files_deleted', 'vectors_deleted', and 'summary'. [crates/gcode/src/contract.rs:433-445]

