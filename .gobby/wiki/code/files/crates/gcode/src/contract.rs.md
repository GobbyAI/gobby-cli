---
title: crates/gcode/src/contract.rs
type: code_file
provenance:
- file: crates/gcode/src/contract.rs
  ranges:
  - 5-254
  - 256-258
  - 260-263
  - 265-272
  - 274-286
  - 288-294
  - 296-314
  - 316-339
  - 341-357
  - 359-369
  - 371-373
  - 375-387
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/contract.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/contract.rs` exposes 12 indexed API symbols.
[crates/gcode/src/contract.rs:5-254]
[crates/gcode/src/contract.rs:256-258]
[crates/gcode/src/contract.rs:260-263]
[crates/gcode/src/contract.rs:265-272]
[crates/gcode/src/contract.rs:274-286]
[crates/gcode/src/contract.rs:288-294]
[crates/gcode/src/contract.rs:296-314]
[crates/gcode/src/contract.rs:316-339]
[crates/gcode/src/contract.rs:341-357]
[crates/gcode/src/contract.rs:359-369]
[crates/gcode/src/contract.rs:371-373]
[crates/gcode/src/contract.rs:375-387]

## API Symbols

- `contract` (function) component `contract [function]` (`41472832-6151-5685-ba9f-58ae5a756e29`) lines 5-254 [crates/gcode/src/contract.rs:5-254]
  - Signature: `pub fn contract() -> CliContract {`
  - Purpose: Indexed function `contract` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:5-254]
- `format_flag` (function) component `format_flag [function]` (`27bc2e46-e13e-5e85-b7c0-29c052ce93fa`) lines 256-258 [crates/gcode/src/contract.rs:256-258]
  - Signature: `fn format_flag() -> FlagContract {`
  - Purpose: Indexed function `format_flag` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:256-258]
- `ai_flag` (function) component `ai_flag [function]` (`43644977-5212-5ee1-8935-db0b7710a94f`) lines 260-263 [crates/gcode/src/contract.rs:260-263]
  - Signature: `fn ai_flag() -> FlagContract {`
  - Purpose: Indexed function `ai_flag` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:260-263]
- `search_flags` (function) component `search_flags [function]` (`34f209bf-7e8a-5a1f-90c4-60f3c3e40149`) lines 265-272 [crates/gcode/src/contract.rs:265-272]
  - Signature: `fn search_flags() -> Vec<FlagContract> {`
  - Purpose: Indexed function `search_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:265-272]
- `grep_flags` (function) component `grep_flags [function]` (`b0ac629e-152e-597f-be08-4a1d03fa3ba8`) lines 274-286 [crates/gcode/src/contract.rs:274-286]
  - Signature: `fn grep_flags() -> Vec<FlagContract> {`
  - Purpose: Indexed function `grep_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:274-286]
- `graph_read_flags` (function) component `graph_read_flags [function]` (`04c2ccfe-3138-59e4-b778-39d1872d6206`) lines 288-294 [crates/gcode/src/contract.rs:288-294]
  - Signature: `fn graph_read_flags() -> Vec<FlagContract> {`
  - Purpose: Indexed function `graph_read_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:288-294]
- `search_keys` (function) component `search_keys [function]` (`4e74cfc1-65fd-55ca-9fd3-c581dfc5bd07`) lines 296-314 [crates/gcode/src/contract.rs:296-314]
  - Signature: `fn search_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `search_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:296-314]
- `grep_keys` (function) component `grep_keys [function]` (`979eacd0-660b-51cb-9b8e-686e55bacacb`) lines 316-339 [crates/gcode/src/contract.rs:316-339]
  - Signature: `fn grep_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `grep_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:316-339]
- `graph_read_keys` (function) component `graph_read_keys [function]` (`86e51545-9ede-587f-990d-ce15e5b604b0`) lines 341-357 [crates/gcode/src/contract.rs:341-357]
  - Signature: `fn graph_read_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `graph_read_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:341-357]
- `contract_keys` (function) component `contract_keys [function]` (`5deaa977-b39a-5bff-88cf-4a121c664c32`) lines 359-369 [crates/gcode/src/contract.rs:359-369]
  - Signature: `fn contract_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `contract_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:359-369]
- `graph_payload_keys` (function) component `graph_payload_keys [function]` (`7f715bf6-c3b0-5dd5-814f-44493c36fa65`) lines 371-373 [crates/gcode/src/contract.rs:371-373]
  - Signature: `fn graph_payload_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `graph_payload_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:371-373]
- `graph_lifecycle_keys` (function) component `graph_lifecycle_keys [function]` (`4c6fe517-7a38-568a-8d51-53fb7ba2b755`) lines 375-387 [crates/gcode/src/contract.rs:375-387]
  - Signature: `fn graph_lifecycle_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `graph_lifecycle_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:375-387]

