---
title: crates/gcode/src/graph/code_graph/read/relationships.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read/relationships.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Overview

`crates/gcode/src/graph/code_graph/read/relationships.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/read/relationships.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ResolvedExternalCallTarget` | class | Indexed class `ResolvedExternalCallTarget` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:24-27] |
| `external_call_target_display_name` | function | Indexed function `external_call_target_display_name` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:29-35] |
| `select_external_call_target` | function | Indexed function `select_external_call_target` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:37-48] |
| `count_callers` | function | Indexed function `count_callers` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:50-60] |
| `count_usages` | function | Indexed function `count_usages` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:62-72] |
| `find_callers` | function | Indexed function `find_callers` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:74-85] |
| `find_usages` | function | Indexed function `find_usages` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:87-98] |
| `find_caller_ids` | function | Indexed function `find_caller_ids` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:100-113] |
| `find_usage_ids` | function | Indexed function `find_usage_ids` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:115-124] |
| `find_callers_batch` | function | Indexed function `find_callers_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:126-139] |
| `find_caller_ids_batch` | function | Indexed function `find_caller_ids_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:141-157] |
| `find_callees_batch` | function | Indexed function `find_callees_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:159-172] |
| `find_callee_ids_batch` | function | Indexed function `find_callee_ids_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:174-190] |
| `get_imports` | function | Indexed function `get_imports` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:192-198] |
| `resolve_external_call_target` | function | Indexed function `resolve_external_call_target` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:200-225] |
| `symbol_callee_edges` | function | Indexed function `symbol_callee_edges` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:227-245] |
| `reconstruct_symbol_path` | function | Indexed function `reconstruct_symbol_path` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:247-263] |
| `symbol_path_steps` | function | Indexed function `symbol_path_steps` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:265-302] |
| `shortest_symbol_path` | function | Indexed function `shortest_symbol_path` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:304-342] |
| `blast_radius` | function | Indexed function `blast_radius` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:344-355] |
| `target` | function | Indexed function `target` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:361-366] |
| `external_call_target_display_uses_module_when_present` | function | Indexed function `external_call_target_display_uses_module_when_present` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:369-375] |
| `select_external_call_target_resolves_single_candidate` | function | Indexed function `select_external_call_target_resolves_single_candidate` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:378-386] |
| `select_external_call_target_reports_ambiguous_candidates` | function | Indexed function `select_external_call_target_reports_ambiguous_candidates` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:389-397] |

