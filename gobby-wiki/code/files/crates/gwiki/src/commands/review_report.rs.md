---
title: crates/gwiki/src/commands/review_report.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/review_report.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/review_report.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/review_report.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/review_report.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `execute` | function | Resolves the review-report scope and change-set options, opens a read-only PostgreSQL-backed wiki index, loads graph/provenance data, computes affected pages and local neighborhoods, inspects repository health, and conditionally constructs an analytics graph before assembling the report outcome. [crates/gwiki/src/commands/review_report.rs:28-105] |
| `ChangeSetInput` | class | 'ChangeSetInput' is a data-only struct that carries a list of file paths, a list of symbol names, an optional diff file path, and an output string for configuring a change-set operation. [crates/gwiki/src/commands/review_report.rs:108-113] |
| `ChangeSetInput::from_options` | method | Constructs a 'ReviewReport' from 'ReviewReportOptions' by merging any files extracted from 'diff_path', deduplicating and filtering empty file/symbol lists, rejecting empty input unless at least one file, symbol, or diff change is provided, and then preserving 'diff_path' and 'output' in the result. [crates/gwiki/src/commands/review_report.rs:116-135] |
| `ChangeSetInput::as_code_change_set` | method | Returns a new 'CodeChangeSet' by cloning and transferring the receiver’s 'files' and 'symbols' collections into the result. [crates/gwiki/src/commands/review_report.rs:137-142] |
| `ReportParts` | class | 'ReportParts' is a data-transfer struct that aggregates a scope identity, change set input, affected and stale pages, code-graph neighborhoods, an optional analytics graph, and a list of degraded source identifiers for report generation or analysis. [crates/gwiki/src/commands/review_report.rs:146-154] |
| `ReviewReport` | class | 'ReviewReport' is a review-result aggregate struct that records the command and scope evaluated, whether the review was degraded and why, the proposed changes, affected pages, stale documentation, graph-neighborhood changes, and risky dependency shifts. [crates/gwiki/src/commands/review_report.rs:157-167] |
| `ReviewAffectedPage` | class | 'ReviewAffectedPage' is a data structure representing a page identified by 'page_path' along with the review source identifiers and source file paths associated with that page. [crates/gwiki/src/commands/review_report.rs:170-174] |
| `RiskyDependencyShift` | class | 'RiskyDependencyShift' is a data structure that records a node reference, its dependency degree, a floating-point risk score, whether it acts as a bridge, and a list of explanatory reasons. [crates/gwiki/src/commands/review_report.rs:177-183] |
| `build_report_from_parts` | function | Constructs a 'ReviewReport' from 'ReportParts' by deduplicating non-empty degraded sources, deriving risky dependency shifts from the optional analytics graph and changes, mapping affected pages and stale page paths into report-friendly forms, and copying the remaining fields into the output. [crates/gwiki/src/commands/review_report.rs:185-211] |
| `render_markdown` | function | Builds and returns a Markdown review report string with YAML front matter from 'ReviewReport' metadata, a '# Review report' heading, and rendered sections for changes, affected pages, stale docs, graph neighborhoods, and risky shifts. [crates/gwiki/src/commands/review_report.rs:213-229] |
| `render_changes` | function | Appends a “## Change set” section to the provided markdown buffer, listing the change set’s files and symbols via 'render_string_list' and optionally adding a quoted diff path when 'changes.diff_path' is present. [crates/gwiki/src/commands/review_report.rs:231-241] |
| `render_affected_pages` | function | Appends an “Affected wiki pages” Markdown section to 'markdown', writing '- none' when 'pages' is empty and otherwise emitting one bullet per 'ReviewAffectedPage' with the page path and optional comma-separated source paths. [crates/gwiki/src/commands/review_report.rs:243-260] |
| `render_stale_docs` | function | Appends a '## Stale docs' section to the provided Markdown buffer, renders the 'stale_docs' list under the label 'Docs' via 'render_string_list', and terminates the section with a trailing newline. [crates/gwiki/src/commands/review_report.rs:262-266] |
| `render_neighborhoods` | function | Appends a “Changed graph neighborhoods” markdown section to 'markdown', emitting '- none' when the slice is empty, otherwise listing each 'CodeGraphEdge' as 'edge: 'source' -> 'target'' with an optional '(file_path[:line])' suffix. [crates/gwiki/src/commands/review_report.rs:268-294] |
| `render_risky_shifts` | function | Appends a “Risky dependency shifts” Markdown section to 'markdown', short-circuiting with an unavailable/omitted message if any degraded source blocks graph analysis, otherwise emitting '- none' when there are no risky shifts or one bullet per shift with node id, degree, score to three decimals, and joined reasons. [crates/gwiki/src/commands/review_report.rs:296-321] |
| `graph_neighborhoods` | function | 'graph_neighborhoods' returns the unique 'CodeGraphEdge's for all changed files and symbols in a project by querying the Falkor-backed code graph, while recording degradation reasons and falling back to an empty result when the scope is not a project or Falkor is unavailable. [crates/gwiki/src/commands/review_report.rs:323-362] |
| `analytics_graph_from_edges` | function | Builds an 'AnalyticsGraph' by marking changed node IDs as 'kind = "changed"' with weight '3.0', adding any edge endpoints not already changed as 'kind = "neighbor"' with weight '1.0', and converting each 'CodeGraphEdge' into an 'AnalyticsEdge' with a kind-specific weight. [crates/gwiki/src/commands/review_report.rs:364-399] |
| `risky_dependency_shifts` | function | Computes graph analytics, filters centrality scores to nodes changed by the input 'ChangeSetInput', converts qualifying scores into 'RiskyDependencyShift' values for bridge nodes, and returns them sorted by descending risk score with node ID as a tie-breaker. [crates/gwiki/src/commands/review_report.rs:401-430] |
| `risk_from_score` | function | Returns 'None' unless the scored node is either a bridge or high-centrality ('degree >= 2' or tied for 'max_score'), otherwise constructs a 'RiskyDependencyShift' for that node with its degree, score, bridge flag, and explanatory reasons. [crates/gwiki/src/commands/review_report.rs:432-456] |
| `changed_node_ids` | function | Returns the set of changed node IDs by starting with all symbols in 'changes.symbols' and then adding both endpoints of any 'edges' whose 'file_path' matches a path in 'changes.files'. [crates/gwiki/src/commands/review_report.rs:458-471] |
| `changed_node_ids_from_graph` | function | Returns a 'BTreeSet<String>' containing all symbol IDs from 'changes.symbols' plus the IDs of every node in 'graph.nodes' whose 'kind' equals '"changed"'. [crates/gwiki/src/commands/review_report.rs:473-484] |
| `changed_files_from_diff` | function | Reads the diff file at 'path' into a string, mapping any I/O failure to 'WikiError::Io' with action '"read review-report diff"', and returns the list of changed file paths parsed from the unified diff contents. [crates/gwiki/src/commands/review_report.rs:486-493] |
| `parse_unified_diff_files` | function | Parses unified diff text to collect unique, sanitized file paths from '+++ b/', '--- a/', and 'diff --git a/... b/...' headers, preferring the new/right-side path when present and excluding '/dev/null', then returns them in sorted order. [crates/gwiki/src/commands/review_report.rs:495-530] |
| `trim_diff_path` | function | Returns the input string with leading and trailing whitespace removed and any leading or trailing double-quote characters stripped. [crates/gwiki/src/commands/review_report.rs:532-534] |

_7 more symbol(s) not shown — run `gcode outline crates/gwiki/src/commands/review_report.rs` for the full list._

_Verified by 5 in-file unit tests._

