---
title: Codewiki
type: code_concept
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/changes.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
- file: crates/gcode/src/commands/codewiki/build_parts/curated_content.rs
- file: crates/gcode/src/commands/codewiki/build_parts/onboarding.rs
- file: crates/gcode/src/commands/codewiki/cluster.rs
- file: crates/gcode/src/commands/codewiki/generation.rs
- file: crates/gcode/src/commands/codewiki/io.rs
- file: crates/gcode/src/commands/codewiki/ownership.rs
- file: crates/gcode/src/commands/codewiki/ownership/analysis.rs
- file: crates/gcode/src/commands/codewiki/ownership/codeowners.rs
- file: crates/gcode/src/commands/codewiki/ownership/render.rs
- file: crates/gcode/src/commands/codewiki/ownership/tests.rs
- file: crates/gcode/src/commands/codewiki/paths.rs
- file: crates/gcode/src/commands/codewiki/progress.rs
- file: crates/gcode/src/commands/codewiki/prompts.rs
- file: crates/gcode/src/commands/codewiki/render/diagrams.rs
- file: crates/gcode/src/commands/codewiki/repair.rs
- file: crates/gcode/src/commands/codewiki/reuse.rs
- file: crates/gcode/src/commands/codewiki/run.rs
- file: crates/gcode/src/commands/codewiki/text.rs
- file: crates/gcode/src/commands/codewiki/text/citations.rs
- file: crates/gcode/src/commands/codewiki/text/frontmatter.rs
- file: crates/gcode/src/commands/codewiki/text/generation.rs
- file: crates/gcode/src/commands/codewiki/text/sanitize.rs
- file: crates/gcode/src/commands/codewiki/text/structural.rs
- file: crates/gcode/src/commands/codewiki/text/verify.rs
- file: crates/gcode/src/commands/codewiki/types.rs
provenance_truncated: 16
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/changes.rs](crates/gcode/src/commands/codewiki/build_parts/changes.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts.rs](crates/gcode/src/commands/codewiki/build_parts/concepts.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/plan.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/render.rs)
- [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs](crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs)
- [crates/gcode/src/commands/codewiki/build_parts/curated_content.rs](crates/gcode/src/commands/codewiki/build_parts/curated_content.rs)
- [crates/gcode/src/commands/codewiki/build_parts/onboarding.rs](crates/gcode/src/commands/codewiki/build_parts/onboarding.rs)
- [crates/gcode/src/commands/codewiki/cluster.rs](crates/gcode/src/commands/codewiki/cluster.rs)
- [crates/gcode/src/commands/codewiki/generation.rs](crates/gcode/src/commands/codewiki/generation.rs)
- [crates/gcode/src/commands/codewiki/io.rs](crates/gcode/src/commands/codewiki/io.rs)
- [crates/gcode/src/commands/codewiki/ownership.rs](crates/gcode/src/commands/codewiki/ownership.rs)
- [crates/gcode/src/commands/codewiki/ownership/analysis.rs](crates/gcode/src/commands/codewiki/ownership/analysis.rs)

_34 more source files omitted._

</details>

# Codewiki

## Purpose

Codewiki groups the related modules and files listed below; read the key components for the grounded detail.

## Key components

| Symbol | Kind | Source | Role |
| --- | --- | --- | --- |
| DocPruneScope | class | [crates/gcode/src/commands/codewiki/io.rs:46-48] | 'DocPruneScope' is a crate-private Rust struct that stores a 'Vec<String>' of scope identifiers used to define the pruning scope for documentation processing. [crates/gcode/src/commands/codewiki/io.rs:46-48] |
| DocSink | class | [crates/gcode/src/commands/codewiki/io.rs:99-109] | 'DocSink<'a>' is a stateful document-generation/pruning accumulator that tracks project and output paths, AI mode, prior and next documentation metadata, visited and generated document IDs, an optional index snapshot, and the active prune scope. [crates/gcode/src/commands/codewiki/io.rs:99-109] |
| call_edges_never_merge_clusters_across_subsystem_roots | function | [crates/gcode/src/commands/codewiki/cluster.rs:353-413] | Verifies that a call edge between symbols in different subsystem roots does not cause 'cluster_file_modules' to collapse the file modules to a shared higher-level directory like 'crates', preserving each root’s separate module path. [crates/gcode/src/commands/codewiki/cluster.rs:353-413] |
| cluster_file_modules | function | [crates/gcode/src/commands/codewiki/cluster.rs:63-123] | Clusters files into module groups by mapping symbols to their owning files, unioning files connected by 'Call' edges that stay within the same subsystem root, and then assigning each connected set either a shared common module name or a per-file module path. [crates/gcode/src/commands/codewiki/cluster.rs:63-123] |
| codewiki_call_edges_query | function | [crates/gcode/src/commands/codewiki/graph.rs:149-164] | Builds and returns a Cypher query plus parameter map that selects intra-project 'CALLS' edges between 'CodeSymbol' nodes, returning source and target IDs and applying the provided 'edge_limit'. [crates/gcode/src/commands/codewiki/graph.rs:149-164] |
| codewiki_import_edges_query | function | [crates/gcode/src/commands/codewiki/graph.rs:166-181] | Builds and returns a Cypher 'MATCH' query that selects 'CodeFile' nodes importing 'CodeModule' nodes within the given 'project_id', limits results to 'edge_limit', and supplies a parameter map containing the quoted 'project' value. [crates/gcode/src/commands/codewiki/graph.rs:166-181] |
| common_module_for_files | function | [crates/gcode/src/commands/codewiki/cluster.rs:201-225] | Returns the deepest shared slash-separated module path among all input files by computing each file’s module path via 'module_for_file', intersecting path components from the front, and joining the common prefix, or an empty string for no files. [crates/gcode/src/commands/codewiki/cluster.rs:201-225] |
| contains_component_sequence | function | [crates/gcode/src/commands/codewiki/cluster.rs:297-302] | Returns 'true' if 'target' appears as a contiguous subsequence within 'components', and 'false' otherwise. [crates/gcode/src/commands/codewiki/cluster.rs:297-302] |
| decode_hex_escape | function | [crates/gcode/src/commands/codewiki/io.rs:442-449] | Parses exactly 'digits' hexadecimal characters from 'chars', accumulating them into a 'u32' with checked arithmetic and returning the corresponding 'char' via 'char::from_u32', or 'None' if input is insufficient, contains a non-hex digit, overflows, or yields an invalid Unicode scalar value. [crates/gcode/src/commands/codewiki/io.rs:442-449] |
| fetch_codewiki_graph_edges | function | [crates/gcode/src/commands/codewiki/graph.rs:5-110] | Fetches Codewiki graph edges for core-file symbols from FalkorDB, returning an unavailable graph on missing config, connection/query failure, or no core symbols, and conservatively marking the result truncated when the edge query returns 'edge_limit' rows. [crates/gcode/src/commands/codewiki/graph.rs:5-110] |
| files_for_import_target | function | [crates/gcode/src/commands/codewiki/cluster.rs:249-265] | Returns the subset of 'files' whose path components or derived module-name components contain the component sequence for 'target_module', or an empty vector if the target module has no components. [crates/gcode/src/commands/codewiki/cluster.rs:249-265] |
| find_file_root | function | [crates/gcode/src/commands/codewiki/cluster.rs:158-199] | Performs union-find root resolution for a file key in 'parents', with path compression back into the discovered root and cycle detection that collapses a detected parent loop to the lexicographically smallest node in the cycle. [crates/gcode/src/commands/codewiki/cluster.rs:158-199] |

## Members

- `crates/gcode/src/commands/codewiki` (module) [crates/gcode/src/commands/codewiki/build.rs:1-30]
- `crates/gcode/src/commands/codewiki/build.rs` (file) [crates/gcode/src/commands/codewiki/build.rs:1-30]
- `crates/gcode/src/commands/codewiki/cluster.rs` (file) [crates/gcode/src/commands/codewiki/cluster.rs:8-43]
- `crates/gcode/src/commands/codewiki/generation.rs` (file) [crates/gcode/src/commands/codewiki/generation.rs:16-24]
- `crates/gcode/src/commands/codewiki/graph.rs` (file) [crates/gcode/src/commands/codewiki/graph.rs:5-110]
- `crates/gcode/src/commands/codewiki/io.rs` (file) [crates/gcode/src/commands/codewiki/io.rs:3-9]
- `crates/gcode/src/commands/codewiki/mod.rs` (file) [crates/gcode/src/commands/codewiki/mod.rs:1-100]


## Explore

- [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

