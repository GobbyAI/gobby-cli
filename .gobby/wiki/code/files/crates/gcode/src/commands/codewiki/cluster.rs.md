---
title: crates/gcode/src/commands/codewiki/cluster.rs
type: code_file
source:
- file: crates/gcode/src/commands/codewiki/cluster.rs
  ranges:
  - 3-54
  - 56-80
  - 89-130
  - 132-156
  - 158-168
  - 170-178
  - 180-196
  - 198-206
  - 208-226
  - 228-233
provenance:
- file: crates/gcode/src/commands/codewiki/cluster.rs
  ranges:
  - 3-54
  - 56-80
  - 89-130
  - 132-156
  - 158-168
  - 170-178
  - 180-196
  - 198-206
  - 208-226
  - 228-233
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/cluster.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/cluster.rs` exposes 10 indexed API symbols.
[crates/gcode/src/commands/codewiki/cluster.rs:3-54] [crates/gcode/src/commands/codewiki/cluster.rs:56-80] [crates/gcode/src/commands/codewiki/cluster.rs:89-130] [crates/gcode/src/commands/codewiki/cluster.rs:132-156]
[crates/gcode/src/commands/codewiki/cluster.rs:158-168] [crates/gcode/src/commands/codewiki/cluster.rs:170-178] [crates/gcode/src/commands/codewiki/cluster.rs:180-196] [crates/gcode/src/commands/codewiki/cluster.rs:198-206]
[crates/gcode/src/commands/codewiki/cluster.rs:208-226] [crates/gcode/src/commands/codewiki/cluster.rs:228-233]

## API Symbols

- `cluster_file_modules` (function) component `cluster_file_modules [function]` (`b5f7a087-cd7f-5e27-823b-79664f1a5646`) lines 3-54 [crates/gcode/src/commands/codewiki/cluster.rs:3-54]
  - Signature: `pub(crate) fn cluster_file_modules(`
  - Purpose: Clusters files into connected components using union-find over call-graph edges, then assigns each file a module name derived from its connected component. [crates/gcode/src/commands/codewiki/cluster.rs:3-54]
- `union_files` (function) component `union_files [function]` (`2cf219a4-ccdc-5833-af4a-e0b6a1985105`) lines 56-80 [crates/gcode/src/commands/codewiki/cluster.rs:56-80]
  - Signature: `pub(crate) fn union_files(`
  - Purpose: Performs a union-by-rank merge in a union-find data structure, attaching the lower-ranked root to the higher-ranked root (with lexicographic tie-breaking) and incrementing the parent's rank on equal-rank unions. [crates/gcode/src/commands/codewiki/cluster.rs:56-80]
- `find_file_root` (function) component `find_file_root [function]` (`731f2c21-b8ef-5b43-a961-72daf4bf1d5a`) lines 89-130 [crates/gcode/src/commands/codewiki/cluster.rs:89-130]
  - Signature: `pub(crate) fn find_file_root(parents: &mut HashMap<String, String>, file: &str) -> String {`
  - Purpose: Locates the root file in a union-find parent mapping using path compression, and resolves any cycles by selecting the lexicographically smallest node in the cycle. [crates/gcode/src/commands/codewiki/cluster.rs:89-130]
- `common_module_for_files` (function) component `common_module_for_files [function]` (`375c30f2-681b-56a1-bb8c-3a87f1b45bb1`) lines 132-156 [crates/gcode/src/commands/codewiki/cluster.rs:132-156]
  - Signature: `pub(crate) fn common_module_for_files(files: &[String]) -> String {`
  - Purpose: Computes the longest common prefix of the module paths for all input files. [crates/gcode/src/commands/codewiki/cluster.rs:132-156]
- `symbols_by_file_component` (function) component `symbols_by_file_component [function]` (`f49c3c64-b3e7-5a95-8f0f-4848c16324dc`) lines 158-168 [crates/gcode/src/commands/codewiki/cluster.rs:158-168]
  - Signature: `pub(crate) fn symbols_by_file_component(symbols: &[Symbol]) -> BTreeMap<String, Vec<String>> {`
  - Purpose: Organizes symbol IDs by their file path into a lexicographically sorted map, including only symbols located in core files. [crates/gcode/src/commands/codewiki/cluster.rs:158-168]
- `first_component_for_file` (function) component `first_component_for_file [function]` (`4a29bdf1-f7ab-5254-a2cf-cddacc17f47c`) lines 170-178 [crates/gcode/src/commands/codewiki/cluster.rs:170-178]
  - Signature: `pub(crate) fn first_component_for_file(`
  - Purpose: Retrieves and returns the cloned first symbol from the vector associated with a given file key in a BTreeMap, or None if the file is not found or the vector is empty. [crates/gcode/src/commands/codewiki/cluster.rs:170-178]
- `files_for_import_target` (function) component `files_for_import_target [function]` (`f24c62ab-dfa9-57f2-aede-7b84478262c7`) lines 180-196 [crates/gcode/src/commands/codewiki/cluster.rs:180-196]
  - Signature: `pub(crate) fn files_for_import_target<'a>(`
  - Purpose: Returns references to files whose filesystem path or derived module components contain the target module's component sequence. [crates/gcode/src/commands/codewiki/cluster.rs:180-196]
- `module_components` (function) component `module_components [function]` (`5b87f590-cc00-51f2-a9b3-705b4fdb4048`) lines 198-206 [crates/gcode/src/commands/codewiki/cluster.rs:198-206]
  - Signature: `fn module_components(value: &str) -> Vec<String> {`
  - Purpose: Splits a module path string into components by normalizing all separators (`::`, `.`, and `\`) to forward slashes and filtering out empty parts. [crates/gcode/src/commands/codewiki/cluster.rs:198-206]
- `path_components` (function) component `path_components [function]` (`0c6bff98-f535-535b-b04c-5bc1873f8bfb`) lines 208-226 [crates/gcode/src/commands/codewiki/cluster.rs:208-226]
  - Signature: `fn path_components(file: &str) -> Vec<String> {`
  - Purpose: Returns all normalized path components as strings, removing file extensions from any component that contains one. [crates/gcode/src/commands/codewiki/cluster.rs:208-226]
- `contains_component_sequence` (function) component `contains_component_sequence [function]` (`a2788420-9cd4-55d3-925d-8765093224a7`) lines 228-233 [crates/gcode/src/commands/codewiki/cluster.rs:228-233]
  - Signature: `fn contains_component_sequence(components: &[String], target: &[String]) -> bool {`
  - Purpose: This function returns `true` if the `target` sequence appears as a contiguous subsequence within the `components` slice, determined by sliding window iteration and element-wise comparison. [crates/gcode/src/commands/codewiki/cluster.rs:228-233]

