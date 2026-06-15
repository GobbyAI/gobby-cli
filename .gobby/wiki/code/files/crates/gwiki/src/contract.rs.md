---
title: crates/gwiki/src/contract.rs
type: code_file
provenance:
- file: crates/gwiki/src/contract.rs
  ranges:
  - 6-470
  - 472-474
  - 476-486
  - 488-491
  - 493-499
  - 501-505
  - 507-517
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/contract.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the `gwiki` CLI contract in one place. `contract()` builds the top-level `CliContract` for the tool, setting its version, summary, global flags, scope handling, and the full command list. The helper functions provide reusable pieces for that schema: `format_flag()` and `ai_flag()` define constrained enum flags, `ingest_file_flags()` groups ingest-related options, `optional_positional()` builds optional positional arguments, and `scoped_keys()` / `contract_keys()` assemble the JSON output key sets used by commands. Together these functions keep the command definitions consistent and make the CLI contract easy to extend.
[crates/gwiki/src/contract.rs:6-470]
[crates/gwiki/src/contract.rs:472-474]
[crates/gwiki/src/contract.rs:476-486]
[crates/gwiki/src/contract.rs:488-491]
[crates/gwiki/src/contract.rs:493-499]

## API Symbols

- `contract` (function) component `contract [function]` (`ae8a750d-02f6-54a2-9816-7bc541ecc75a`) lines 6-470 [crates/gwiki/src/contract.rs:6-470]
  - Signature: `pub fn contract() -> CliContract {`
  - Purpose: Constructs and returns a 'CliContract' struct that specifies the complete CLI interface definition for gwiki, including global flags, scope parameters, and command contracts. [crates/gwiki/src/contract.rs:6-470]
- `format_flag` (function) component `format_flag [function]` (`38f684e0-9e71-5365-8875-f347c08808db`) lines 472-474 [crates/gwiki/src/contract.rs:472-474]
  - Signature: `fn format_flag() -> FlagContract {`
  - Purpose: Creates and returns a 'FlagContract' for a '--format' command-line flag constrained to two allowed values: "json" and "text". [crates/gwiki/src/contract.rs:472-474]
- `ingest_file_flags` (function) component `ingest_file_flags [function]` (`76bd4494-1744-5755-9eff-ed080f723564`) lines 476-486 [crates/gwiki/src/contract.rs:476-486]
  - Signature: `fn ingest_file_flags() -> Vec<FlagContract> {`
  - Purpose: Returns a vector of FlagContract objects defining command-line flags for file ingestion, including toggle switches for AI control and translation, value parameters for target language and video frame interval, and AI feature routing directives. [crates/gwiki/src/contract.rs:476-486]
- `ai_flag` (function) component `ai_flag [function]` (`8655ca9e-7cff-537e-94da-501fba4a5080`) lines 488-491 [crates/gwiki/src/contract.rs:488-491]
  - Signature: `fn ai_flag(name: &'static str) -> FlagContract {`
  - Purpose: 'ai_flag' constructs a 'FlagContract' that validates a named configuration flag against a whitelist of exactly four allowed string values: 'auto', 'daemon', 'direct', and 'off'. [crates/gwiki/src/contract.rs:488-491]
- `optional_positional` (function) component `optional_positional [function]` (`074a83b8-5744-5f0a-896a-1d6a1d2dcf5c`) lines 493-499 [crates/gwiki/src/contract.rs:493-499]
  - Signature: `fn optional_positional(name: &'static str, repeatable: bool) -> PositionalContract {`
  - Purpose: Constructs a 'PositionalContract' for a non-required positional argument with the specified name and repeatability configuration. [crates/gwiki/src/contract.rs:493-499]
- `scoped_keys` (function) component `scoped_keys [function]` (`af56d771-d9ae-54e6-8f3a-b3842cc9c124`) lines 501-505 [crates/gwiki/src/contract.rs:501-505]
  - Signature: `fn scoped_keys(mut keys: Vec<&'static str>) -> Vec<&'static str> {`
  - Purpose: Prepends the static string literals '"command"' and '"scope"' to the input vector of static string references and returns the augmented vector. [crates/gwiki/src/contract.rs:501-505]
- `contract_keys` (function) component `contract_keys [function]` (`f8bdcc62-1187-50c5-ab24-0779e9c910e1`) lines 507-517 [crates/gwiki/src/contract.rs:507-517]
  - Signature: `fn contract_keys() -> Vec<&'static str> {`
  - Purpose: This function returns a vector of seven static string references representing the field keys that compose a contract definition schema. [crates/gwiki/src/contract.rs:507-517]

