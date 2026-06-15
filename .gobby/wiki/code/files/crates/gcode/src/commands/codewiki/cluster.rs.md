---
title: crates/gcode/src/commands/codewiki/cluster.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/cluster.rs
  ranges:
  - 8-43
  - 46-55
  - 57-61
  - 63-123
  - 125-149
  - 158-199
  - 201-225
  - 227-237
  - 239-247
  - 249-265
  - 267-275
  - 277-295
  - 297-302
  - 308-310
  - 313-329
  - 332-336
  - 339-350
  - 353-413
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/cluster.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file groups repository files into subsystem-aware clusters for codewiki decomposition. It first derives subsystem roots from file paths, treating container directories as expandable to meaningful child roots when they have no direct files, then uses those roots to keep clustering local to each subsystem. The main clustering logic unions files connected by `Call` edges within the same root, resolves disjoint-set representatives with deterministic union/find behavior, and assigns each resulting cluster a module path from its common module or lone file. Supporting helpers split and compare module/path components, map symbols to files, and select the files relevant to an import target.
[crates/gcode/src/commands/codewiki/cluster.rs:8-43]
[crates/gcode/src/commands/codewiki/cluster.rs:46-55]
[crates/gcode/src/commands/codewiki/cluster.rs:57-61]
[crates/gcode/src/commands/codewiki/cluster.rs:63-123]
[crates/gcode/src/commands/codewiki/cluster.rs:125-149]

## API Symbols

- `subsystem_roots` (function) component `subsystem_roots [function]` (`1162d4f9-5626-571f-89ec-a1251b313bd7`) lines 8-43 [crates/gcode/src/commands/codewiki/cluster.rs:8-43]
  - Signature: `pub(crate) fn subsystem_roots(files: &[String]) -> BTreeSet<String> {`
  - Purpose: Returns the set of subsystem root identifiers derived from file paths by grouping modules by their top-level segment, preferring immediate child namespaces like 'top/child' when a top-level package has no direct files and has children, otherwise emitting the top-level name itself. [crates/gcode/src/commands/codewiki/cluster.rs:8-43]
- `subsystem_root_for_file` (function) component `subsystem_root_for_file [function]` (`cd08cbab-e272-5dfb-a306-6728aeacea18`) lines 46-55 [crates/gcode/src/commands/codewiki/cluster.rs:46-55]
  - Signature: `pub(crate) fn subsystem_root_for_file<'a>(`
  - Purpose: Returns the first root in 'roots' whose path/module prefix contains the module derived from 'file', or 'None' if no such root exists. [crates/gcode/src/commands/codewiki/cluster.rs:46-55]
- `module_is_within` (function) component `module_is_within [function]` (`b5d6567b-87b1-59a7-8894-5a2df2ce8d6f`) lines 57-61 [crates/gcode/src/commands/codewiki/cluster.rs:57-61]
  - Signature: `fn module_is_within(module: &str, root: &str) -> bool {`
  - Purpose: Returns 'true' when 'module' has 'root' as a prefix and the remaining suffix is either empty or begins with '/', ensuring 'module' is within 'root' as a path-like namespace boundary. [crates/gcode/src/commands/codewiki/cluster.rs:57-61]
- `cluster_file_modules` (function) component `cluster_file_modules [function]` (`d05bc055-1ab7-54e0-880f-8ae763200521`) lines 63-123 [crates/gcode/src/commands/codewiki/cluster.rs:63-123]
  - Signature: `pub(crate) fn cluster_file_modules(`
  - Purpose: 'cluster_file_modules' groups files into connected clusters by unioning files that have 'Call' edges between symbols in the same subsystem root, then assigns each cluster a module path derived from the cluster’s common module or the lone file’s module. [crates/gcode/src/commands/codewiki/cluster.rs:63-123]
- `union_files` (function) component `union_files [function]` (`69836486-d6f1-5a42-9d07-abfd020e0cb2`) lines 125-149 [crates/gcode/src/commands/codewiki/cluster.rs:125-149]
  - Signature: `pub(crate) fn union_files(`
  - Purpose: Performs a union-by-rank merge of two file-set representatives in the 'parents' disjoint-set map, choosing the parent deterministically on equal rank by lexicographic root order and incrementing the chosen root’s rank when needed. [crates/gcode/src/commands/codewiki/cluster.rs:125-149]
- `find_file_root` (function) component `find_file_root [function]` (`9e38315c-b59c-5c60-9533-218af1e5e89f`) lines 158-199 [crates/gcode/src/commands/codewiki/cluster.rs:158-199]
  - Signature: `pub(crate) fn find_file_root(parents: &mut HashMap<String, String>, file: &str) -> String {`
  - Purpose: Performs path-compression lookup in a parent map to resolve a file’s representative root, detecting cycles by choosing the lexicographically smallest node in the cycle and updating all traversed nodes to point to that root. [crates/gcode/src/commands/codewiki/cluster.rs:158-199]
- `common_module_for_files` (function) component `common_module_for_files [function]` (`921214d7-ccfc-5fad-9c90-f94f966ffb06`) lines 201-225 [crates/gcode/src/commands/codewiki/cluster.rs:201-225]
  - Signature: `pub(crate) fn common_module_for_files(files: &[String]) -> String {`
  - Purpose: Returns the longest shared slash-delimited module path prefix across all input files, after mapping each file through 'module_for_file', filtering out empty path segments, and returning an empty string for an empty input slice. [crates/gcode/src/commands/codewiki/cluster.rs:201-225]
- `symbols_by_file_component` (function) component `symbols_by_file_component [function]` (`15b839b6-5065-5891-af35-45ed8ba699c4`) lines 227-237 [crates/gcode/src/commands/codewiki/cluster.rs:227-237]
  - Signature: `pub(crate) fn symbols_by_file_component(symbols: &[Symbol]) -> BTreeMap<String, Vec<String>> {`
  - Purpose: Returns a 'BTreeMap' grouping the 'id's of symbols whose 'file_path' satisfies 'is_core_file' by their exact 'file_path', preserving keys in sorted order. [crates/gcode/src/commands/codewiki/cluster.rs:227-237]
- `first_component_for_file` (function) component `first_component_for_file [function]` (`6926a399-46b2-5fc0-86de-ccd09751f171`) lines 239-247 [crates/gcode/src/commands/codewiki/cluster.rs:239-247]
  - Signature: `pub(crate) fn first_component_for_file(`
  - Purpose: Returns the first symbol/component associated with 'file' from 'symbols_by_file' by looking up the file key in the 'BTreeMap', taking the first 'Vec<String>' element if present, and cloning it into an 'Option<String>'. [crates/gcode/src/commands/codewiki/cluster.rs:239-247]
- `files_for_import_target` (function) component `files_for_import_target [function]` (`b5b4658b-fe51-54b2-94ab-c763bbd85b77`) lines 249-265 [crates/gcode/src/commands/codewiki/cluster.rs:249-265]
  - Signature: `pub(crate) fn files_for_import_target<'a>(`
  - Purpose: Returns the subset of input file paths whose path components or derived module-name components contain the target module’s component sequence, or an empty vector if the target module has no components. [crates/gcode/src/commands/codewiki/cluster.rs:249-265]
- `module_components` (function) component `module_components [function]` (`07e3fb63-606b-5d7d-926b-0080b561c941`) lines 267-275 [crates/gcode/src/commands/codewiki/cluster.rs:267-275]
  - Signature: `fn module_components(value: &str) -> Vec<String> {`
  - Purpose: Splits a module path string into non-empty components by normalizing '::', '.' and '\' separators to '/' and returning each segment as a 'Vec<String>'. [crates/gcode/src/commands/codewiki/cluster.rs:267-275]
- `path_components` (function) component `path_components [function]` (`984bc8c7-5466-54dc-a75f-6d345529eb0d`) lines 277-295 [crates/gcode/src/commands/codewiki/cluster.rs:277-295]
  - Signature: `fn path_components(file: &str) -> Vec<String> {`
  - Purpose: Returns a 'Vec<String>' of the non-empty normal path segments from 'file', stripping file extensions from any segment that has one and discarding all non-'Normal' path components. [crates/gcode/src/commands/codewiki/cluster.rs:277-295]
- `contains_component_sequence` (function) component `contains_component_sequence [function]` (`8ee1a096-f2bb-5fa2-8c7c-9d52c5a1b472`) lines 297-302 [crates/gcode/src/commands/codewiki/cluster.rs:297-302]
  - Signature: `fn contains_component_sequence(components: &[String], target: &[String]) -> bool {`
  - Purpose: Returns 'true' if 'target' appears as a contiguous, order-preserving subsequence within 'components', and 'false' otherwise. [crates/gcode/src/commands/codewiki/cluster.rs:297-302]
- `paths` (function) component `paths [function]` (`b80a607d-786c-5c72-a0f6-b9bceb73d0e7`) lines 308-310 [crates/gcode/src/commands/codewiki/cluster.rs:308-310]
  - Signature: `fn paths(values: &[&str]) -> Vec<String> {`
  - Purpose: Converts a slice of '&str' values into a 'Vec<String>' by cloning each string slice into an owned 'String'. [crates/gcode/src/commands/codewiki/cluster.rs:308-310]
- `subsystem_roots_expand_container_directories_one_level` (function) component `subsystem_roots_expand_container_directories_one_level [function]` (`eba3f9fc-4edb-508b-9d88-599114e469ed`) lines 313-329 [crates/gcode/src/commands/codewiki/cluster.rs:313-329]
  - Signature: `fn subsystem_roots_expand_container_directories_one_level() {`
  - Purpose: Verifies that 'subsystem_roots' expands a container directory one level deep for file paths, returning leaf subsystem roots like 'crates/gcode', 'crates/gcore', 'docs/guides', and 'scripts' while excluding the broader container root 'crates'. [crates/gcode/src/commands/codewiki/cluster.rs:313-329]
- `subsystem_roots_keep_top_level_directories_with_direct_files` (function) component `subsystem_roots_keep_top_level_directories_with_direct_files [function]` (`5e0da510-1ba6-5e2f-ab68-a592e2284a91`) lines 332-336 [crates/gcode/src/commands/codewiki/cluster.rs:332-336]
  - Signature: `fn subsystem_roots_keep_top_level_directories_with_direct_files() {`
  - Purpose: Verifies that 'subsystem_roots' returns the top-level directory 'docs' when given files directly under that directory, even if they are nested in subdirectories. [crates/gcode/src/commands/codewiki/cluster.rs:332-336]
- `subsystem_root_for_file_matches_whole_components_only` (function) component `subsystem_root_for_file_matches_whole_components_only [function]` (`8d84bd95-4e0d-5bb0-98f8-b22ff265a5b7`) lines 339-350 [crates/gcode/src/commands/codewiki/cluster.rs:339-350]
  - Signature: `fn subsystem_root_for_file_matches_whole_components_only() {`
  - Purpose: Verifies that 'subsystem_root_for_file' returns a match only when the file path starts with an exact subsystem root path component ('crates/gcode'), and does not match partial prefixes like 'crates/gcodex' or non-rooted files like 'README.md'. [crates/gcode/src/commands/codewiki/cluster.rs:339-350]
- `call_edges_never_merge_clusters_across_subsystem_roots` (function) component `call_edges_never_merge_clusters_across_subsystem_roots [function]` (`c7422994-ec4b-5acb-a19d-1bfb95d95df8`) lines 353-413 [crates/gcode/src/commands/codewiki/cluster.rs:353-413]
  - Signature: `fn call_edges_never_merge_clusters_across_subsystem_roots() {`
  - Purpose: Verifies that a call edge between symbols in different subsystem roots does not cause 'cluster_file_modules' to merge their file modules upward to a shared parent like 'crates', preserving each root-specific module path. [crates/gcode/src/commands/codewiki/cluster.rs:353-413]

