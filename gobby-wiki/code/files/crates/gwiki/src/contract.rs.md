---
title: crates/gwiki/src/contract.rs
type: code_file
provenance:
- file: crates/gwiki/src/contract.rs
  ranges:
  - 6-494
  - 496-498
  - 500-510
  - 512-515
  - 517-523
  - 525-529
  - 531-541
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/contract.rs:6-494](crates/gwiki/src/contract.rs#L6-L494), [crates/gwiki/src/contract.rs:496-498](crates/gwiki/src/contract.rs#L496-L498), [crates/gwiki/src/contract.rs:500-510](crates/gwiki/src/contract.rs#L500-L510), [crates/gwiki/src/contract.rs:512-515](crates/gwiki/src/contract.rs#L512-L515), [crates/gwiki/src/contract.rs:517-523](crates/gwiki/src/contract.rs#L517-L523), [crates/gwiki/src/contract.rs:525-529](crates/gwiki/src/contract.rs#L525-L529), [crates/gwiki/src/contract.rs:531-541](crates/gwiki/src/contract.rs#L531-L541)

</details>

# crates/gwiki/src/contract.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the `gwiki` CLI contract for the local-first wiki tool. `contract()` builds the top-level `CliContract` with shared global flags, scope selection, and a set of daemon-backed commands such as `contract`, `index`, and `search`, each declaring its positional args, flags, and JSON output shape. The helper functions `format_flag`, `ingest_file_flags`, `ai_flag`, `optional_positional`, `scoped_keys`, and `contract_keys` centralize reusable flag and key definitions so the command specs stay consistent.
[crates/gwiki/src/contract.rs:6-494]
[crates/gwiki/src/contract.rs:496-498]
[crates/gwiki/src/contract.rs:500-510]
[crates/gwiki/src/contract.rs:512-515]
[crates/gwiki/src/contract.rs:517-523]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `contract` | function | `pub fn contract() -> CliContract {` | `contract [function]` | `ae8a750d-02f6-54a2-9816-7bc541ecc75a` | 6-494 [crates/gwiki/src/contract.rs:6-494] | Indexed function `contract` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:6-494] |
| `format_flag` | function | `fn format_flag() -> FlagContract {` | `format_flag [function]` | `23eeae13-b48a-5187-a358-b27fbd453a57` | 496-498 [crates/gwiki/src/contract.rs:496-498] | Indexed function `format_flag` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:496-498] |
| `ingest_file_flags` | function | `fn ingest_file_flags() -> Vec<FlagContract> {` | `ingest_file_flags [function]` | `1b07b153-5717-5d7d-b04f-cdcfc83581ed` | 500-510 [crates/gwiki/src/contract.rs:500-510] | Indexed function `ingest_file_flags` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:500-510] |
| `ai_flag` | function | `fn ai_flag(name: &'static str) -> FlagContract {` | `ai_flag [function]` | `98d39735-6c25-545c-a755-df77c5b0e6e8` | 512-515 [crates/gwiki/src/contract.rs:512-515] | Indexed function `ai_flag` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:512-515] |
| `optional_positional` | function | `fn optional_positional(name: &'static str, repeatable: bool) -> PositionalContract {` | `optional_positional [function]` | `ab974554-db86-591a-b4ed-9b5287ff5239` | 517-523 [crates/gwiki/src/contract.rs:517-523] | Indexed function `optional_positional` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:517-523] |
| `scoped_keys` | function | `fn scoped_keys(mut keys: Vec<&'static str>) -> Vec<&'static str> {` | `scoped_keys [function]` | `193a6915-4b42-5f54-902f-2f639587107c` | 525-529 [crates/gwiki/src/contract.rs:525-529] | Indexed function `scoped_keys` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:525-529] |
| `contract_keys` | function | `fn contract_keys() -> Vec<&'static str> {` | `contract_keys [function]` | `857bb262-75b8-5783-ba02-4b125b9d5b39` | 531-541 [crates/gwiki/src/contract.rs:531-541] | Indexed function `contract_keys` in `crates/gwiki/src/contract.rs`. [crates/gwiki/src/contract.rs:531-541] |
