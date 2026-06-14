---
title: crates/gwiki/src/contract.rs
type: code_file
provenance:
- file: crates/gwiki/src/contract.rs
  ranges:
  - 6-469
  - 471-473
  - 475-485
  - 487-490
  - 492-498
  - 500-504
  - 506-516
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/contract.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the `gwiki` CLI contract and its reusable contract-building helpers. `contract()` assembles the top-level `CliContract` with version, summary, global and scope flags, and the daemon-backed commands, each paired with its positional/flag requirements and JSON output keys. The helper functions factor out common pieces: `format_flag()` and `ai_flag()` constrain repeated flag values, `ingest_file_flags()` bundles ingestion-related switches and routing flags, `optional_positional()` builds non-required positionals, and `scoped_keys()`/`contract_keys()` generate the shared JSON field lists used by command schemas.
[crates/gwiki/src/contract.rs:6-469]
[crates/gwiki/src/contract.rs:471-473]
[crates/gwiki/src/contract.rs:475-485]
[crates/gwiki/src/contract.rs:487-490]
[crates/gwiki/src/contract.rs:492-498]

## API Symbols

- `contract` (function) component `contract [function]` (`ae8a750d-02f6-54a2-9816-7bc541ecc75a`) lines 6-469 [crates/gwiki/src/contract.rs:6-469]
  - Signature: `pub fn contract() -> CliContract {`
  - Purpose: Constructs and returns a 'CliContract' for the 'gwiki' CLI, defining its version, summary, global and scope flags, and the available daemon-backed commands with their JSON output schemas. [crates/gwiki/src/contract.rs:6-469]
- `format_flag` (function) component `format_flag [function]` (`abdf6692-4a93-5b35-a191-e38f93c6726d`) lines 471-473 [crates/gwiki/src/contract.rs:471-473]
  - Signature: `fn format_flag() -> FlagContract {`
  - Purpose: Returns a 'FlagContract' for the '--format' CLI flag, constraining its value to the allowed string set '{"json", "text"}'. [crates/gwiki/src/contract.rs:471-473]
- `ingest_file_flags` (function) component `ingest_file_flags [function]` (`d295b3b7-a976-5eb8-83df-3d5e9a190538`) lines 475-485 [crates/gwiki/src/contract.rs:475-485]
  - Signature: `fn ingest_file_flags() -> Vec<FlagContract> {`
  - Purpose: Returns a 'Vec<FlagContract>' defining CLI ingestion flags, including two switches ('--no-ai', '--translate'), two value flags ('--target-lang', '--video-frame-interval'), and three AI-backed routing flags ('--transcription-routing', '--vision-routing', '--text-routing'). [crates/gwiki/src/contract.rs:475-485]
- `ai_flag` (function) component `ai_flag [function]` (`5987f6ae-1fb5-55da-baa8-5b9a8a49b696`) lines 487-490 [crates/gwiki/src/contract.rs:487-490]
  - Signature: `fn ai_flag(name: &'static str) -> FlagContract {`
  - Purpose: Creates a 'FlagContract' for the given flag name whose value is restricted to one of 'auto', 'daemon', 'direct', or 'off'. [crates/gwiki/src/contract.rs:487-490]
- `optional_positional` (function) component `optional_positional [function]` (`fcd368a2-ecd3-5797-bde6-2af7e6294c42`) lines 492-498 [crates/gwiki/src/contract.rs:492-498]
  - Signature: `fn optional_positional(name: &'static str, repeatable: bool) -> PositionalContract {`
  - Purpose: Constructs and returns a 'PositionalContract' for the given 'name' with 'required' fixed to 'false' and 'repeatable' set from the argument. [crates/gwiki/src/contract.rs:492-498]
- `scoped_keys` (function) component `scoped_keys [function]` (`5454c1e4-e30d-5f6a-aa0c-2a066a92f83f`) lines 500-504 [crates/gwiki/src/contract.rs:500-504]
  - Signature: `fn scoped_keys(mut keys: Vec<&'static str>) -> Vec<&'static str> {`
  - Purpose: Returns a new 'Vec<&'static str>' containing '"command"' and '"scope"' prepended to the input 'keys' vector, consuming and appending the original keys in place. [crates/gwiki/src/contract.rs:500-504]
- `contract_keys` (function) component `contract_keys [function]` (`1a63ad46-6c27-5ab7-ae2f-72d6cef416c3`) lines 506-516 [crates/gwiki/src/contract.rs:506-516]
  - Signature: `fn contract_keys() -> Vec<&'static str> {`
  - Purpose: Returns a vector of the seven static contract field names: 'tool', 'contract_version', 'summary', 'global_flags', 'scope', 'commands', and 'error_codes'. [crates/gwiki/src/contract.rs:506-516]

