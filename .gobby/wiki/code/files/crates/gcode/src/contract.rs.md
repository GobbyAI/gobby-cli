---
title: crates/gcode/src/contract.rs
type: code_file
provenance:
- file: crates/gcode/src/contract.rs
  ranges:
  - 5-259
  - 261-263
  - 265-268
  - 270-277
  - 279-291
  - 293-299
  - 301-319
  - 321-344
  - 346-362
  - 364-374
  - 376-378
  - 380-392
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/contract.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Defines the CLI contract for the `gcode` tool, describing its global flags, project scoping, and the full command surface that the daemon consumes. `contract()` assembles the top-level `CliContract` and wires each command to shared helpers for flags and JSON output keys, while the smaller helper functions group reusable contract pieces for formatting, AI/search/grep options, graph read options, and key lists for search, grep, graph read, lifecycle, and overall contract payloads.
[crates/gcode/src/contract.rs:5-259]
[crates/gcode/src/contract.rs:261-263]
[crates/gcode/src/contract.rs:265-268]
[crates/gcode/src/contract.rs:270-277]
[crates/gcode/src/contract.rs:279-291]

## API Symbols

- `contract` (function) component `contract [function]` (`41472832-6151-5685-ba9f-58ae5a756e29`) lines 5-259 [crates/gcode/src/contract.rs:5-259]
  - Signature: `pub fn contract() -> CliContract {`
  - Purpose: Indexed function `contract` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:5-259]
- `format_flag` (function) component `format_flag [function]` (`53720267-007d-59bc-b200-1e0700065598`) lines 261-263 [crates/gcode/src/contract.rs:261-263]
  - Signature: `fn format_flag() -> FlagContract {`
  - Purpose: Indexed function `format_flag` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:261-263]
- `ai_flag` (function) component `ai_flag [function]` (`be5a6e0b-7096-5719-9822-56c2dfe50381`) lines 265-268 [crates/gcode/src/contract.rs:265-268]
  - Signature: `fn ai_flag() -> FlagContract {`
  - Purpose: Indexed function `ai_flag` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:265-268]
- `search_flags` (function) component `search_flags [function]` (`fbaf9a3c-1a8f-51fc-9dee-0ee6bd4e66ac`) lines 270-277 [crates/gcode/src/contract.rs:270-277]
  - Signature: `fn search_flags() -> Vec<FlagContract> {`
  - Purpose: Indexed function `search_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:270-277]
- `grep_flags` (function) component `grep_flags [function]` (`5147e4b6-fd8c-5993-a383-859f8696b499`) lines 279-291 [crates/gcode/src/contract.rs:279-291]
  - Signature: `fn grep_flags() -> Vec<FlagContract> {`
  - Purpose: Indexed function `grep_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:279-291]
- `graph_read_flags` (function) component `graph_read_flags [function]` (`69de647b-d000-5874-b1a7-76fb11b0141f`) lines 293-299 [crates/gcode/src/contract.rs:293-299]
  - Signature: `fn graph_read_flags() -> Vec<FlagContract> {`
  - Purpose: Indexed function `graph_read_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:293-299]
- `search_keys` (function) component `search_keys [function]` (`df93c2ec-3ca5-53fc-88cf-8a0a6536c8db`) lines 301-319 [crates/gcode/src/contract.rs:301-319]
  - Signature: `fn search_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `search_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:301-319]
- `grep_keys` (function) component `grep_keys [function]` (`6c9c6458-4970-515b-b154-c03258eab42e`) lines 321-344 [crates/gcode/src/contract.rs:321-344]
  - Signature: `fn grep_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `grep_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:321-344]
- `graph_read_keys` (function) component `graph_read_keys [function]` (`b9fdace3-d26c-5883-8eb6-c01a6c769dbe`) lines 346-362 [crates/gcode/src/contract.rs:346-362]
  - Signature: `fn graph_read_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `graph_read_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:346-362]
- `contract_keys` (function) component `contract_keys [function]` (`e0a2ffd1-7a2e-5f10-9c60-5e55fa8cf79e`) lines 364-374 [crates/gcode/src/contract.rs:364-374]
  - Signature: `fn contract_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `contract_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:364-374]
- `graph_payload_keys` (function) component `graph_payload_keys [function]` (`3fe99dec-cf08-57dc-989b-2bcc192f684e`) lines 376-378 [crates/gcode/src/contract.rs:376-378]
  - Signature: `fn graph_payload_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `graph_payload_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:376-378]
- `graph_lifecycle_keys` (function) component `graph_lifecycle_keys [function]` (`b606dde8-ef83-567d-944b-4f0c98da1de0`) lines 380-392 [crates/gcode/src/contract.rs:380-392]
  - Signature: `fn graph_lifecycle_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `graph_lifecycle_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:380-392]

