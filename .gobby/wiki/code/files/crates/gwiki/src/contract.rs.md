---
title: crates/gwiki/src/contract.rs
type: code_file
provenance:
- file: crates/gwiki/src/contract.rs
  ranges:
  - 6-499
  - 501-503
  - 505-515
  - 517-520
  - 522-528
  - 530-534
  - 536-546
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/contract.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/contract.rs` exposes 7 indexed API symbols.
[crates/gwiki/src/contract.rs:6-499]
[crates/gwiki/src/contract.rs:501-503]
[crates/gwiki/src/contract.rs:505-515]
[crates/gwiki/src/contract.rs:517-520]
[crates/gwiki/src/contract.rs:522-528]

## API Symbols

- `contract` (function) component `contract [function]` (`ae8a750d-02f6-54a2-9816-7bc541ecc75a`) lines 6-499 [crates/gwiki/src/contract.rs:6-499]
  - Signature: `pub fn contract() -> CliContract {`
  - Purpose: Indexed function `contract` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:6-499]
- `format_flag` (function) component `format_flag [function]` (`f56bd686-cb17-5841-9665-99466a17eaef`) lines 501-503 [crates/gwiki/src/contract.rs:501-503]
  - Signature: `fn format_flag() -> FlagContract {`
  - Purpose: Indexed function `format_flag` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:501-503]
- `ingest_file_flags` (function) component `ingest_file_flags [function]` (`2855f17d-42a6-5398-9927-28b0a57772fc`) lines 505-515 [crates/gwiki/src/contract.rs:505-515]
  - Signature: `fn ingest_file_flags() -> Vec<FlagContract> {`
  - Purpose: Indexed function `ingest_file_flags` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:505-515]
- `ai_flag` (function) component `ai_flag [function]` (`da5e05b6-a973-503b-a491-0f3d7b7b2180`) lines 517-520 [crates/gwiki/src/contract.rs:517-520]
  - Signature: `fn ai_flag(name: &'static str) -> FlagContract {`
  - Purpose: Indexed function `ai_flag` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:517-520]
- `optional_positional` (function) component `optional_positional [function]` (`1724455c-6355-5b1b-940e-feca736814d4`) lines 522-528 [crates/gwiki/src/contract.rs:522-528]
  - Signature: `fn optional_positional(name: &'static str, repeatable: bool) -> PositionalContract {`
  - Purpose: Indexed function `optional_positional` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:522-528]
- `scoped_keys` (function) component `scoped_keys [function]` (`12703e16-4e72-58ce-b482-718c7c08e84c`) lines 530-534 [crates/gwiki/src/contract.rs:530-534]
  - Signature: `fn scoped_keys(mut keys: Vec<&'static str>) -> Vec<&'static str> {`
  - Purpose: Indexed function `scoped_keys` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:530-534]
- `contract_keys` (function) component `contract_keys [function]` (`2fc05117-1d37-5b22-9484-0541eea03014`) lines 536-546 [crates/gwiki/src/contract.rs:536-546]
  - Signature: `fn contract_keys() -> Vec<&'static str> {`
  - Purpose: Indexed function `contract_keys` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:536-546]

