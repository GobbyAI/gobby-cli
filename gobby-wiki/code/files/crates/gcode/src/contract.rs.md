---
title: crates/gcode/src/contract.rs
type: code_file
provenance:
- file: crates/gcode/src/contract.rs
  ranges:
  - 5-511
  - 513-515
  - 517-520
  - 522-524
  - 526-533
  - 535-547
  - 549-555
  - 557-575
  - 577-600
  - 602-619
  - 621-638
  - 640-650
  - 652-654
  - 656-668
  - 670-678
  - 680-682
  - 684-697
  - 699-711
  - 713-723
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/contract.rs:5-511](crates/gcode/src/contract.rs#L5-L511), [crates/gcode/src/contract.rs:513-515](crates/gcode/src/contract.rs#L513-L515), [crates/gcode/src/contract.rs:517-520](crates/gcode/src/contract.rs#L517-L520), [crates/gcode/src/contract.rs:522-524](crates/gcode/src/contract.rs#L522-L524), [crates/gcode/src/contract.rs:526-533](crates/gcode/src/contract.rs#L526-L533), [crates/gcode/src/contract.rs:535-547](crates/gcode/src/contract.rs#L535-L547), [crates/gcode/src/contract.rs:549-555](crates/gcode/src/contract.rs#L549-L555), [crates/gcode/src/contract.rs:557-575](crates/gcode/src/contract.rs#L557-L575), [crates/gcode/src/contract.rs:577-600](crates/gcode/src/contract.rs#L577-L600), [crates/gcode/src/contract.rs:602-619](crates/gcode/src/contract.rs#L602-L619), [crates/gcode/src/contract.rs:621-638](crates/gcode/src/contract.rs#L621-L638), [crates/gcode/src/contract.rs:640-650](crates/gcode/src/contract.rs#L640-L650), [crates/gcode/src/contract.rs:652-654](crates/gcode/src/contract.rs#L652-L654), [crates/gcode/src/contract.rs:656-668](crates/gcode/src/contract.rs#L656-L668), [crates/gcode/src/contract.rs:670-678](crates/gcode/src/contract.rs#L670-L678), [crates/gcode/src/contract.rs:680-682](crates/gcode/src/contract.rs#L680-L682), [crates/gcode/src/contract.rs:684-697](crates/gcode/src/contract.rs#L684-L697), [crates/gcode/src/contract.rs:699-711](crates/gcode/src/contract.rs#L699-L711), [crates/gcode/src/contract.rs:713-723](crates/gcode/src/contract.rs#L713-L723)

</details>

# crates/gcode/src/contract.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Defines the CLI contract for the `gcode` tool. `contract()` assembles the full `CliContract` for the command set, global/scope flags, and JSON output keys, while the helper functions group reusable flag definitions and output-key lists for specific command areas such as search, grep, graph read/path/lifecycle/cleanup/report, vector lifecycle/cleanup, and embeddings doctor.
[crates/gcode/src/contract.rs:5-511]
[crates/gcode/src/contract.rs:513-515]
[crates/gcode/src/contract.rs:517-520]
[crates/gcode/src/contract.rs:522-524]
[crates/gcode/src/contract.rs:526-533]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `contract` | function | `pub fn contract() -> CliContract {` | `contract [function]` | `41472832-6151-5685-ba9f-58ae5a756e29` | 5-511 [crates/gcode/src/contract.rs:5-511] | Indexed function `contract` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:5-511] |
| `format_flag` | function | `fn format_flag() -> FlagContract {` | `format_flag [function]` | `3e1cc9ab-9149-598b-b450-f09f1eb93c61` | 513-515 [crates/gcode/src/contract.rs:513-515] | Indexed function `format_flag` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:513-515] |
| `ai_flag` | function | `fn ai_flag() -> FlagContract {` | `ai_flag [function]` | `a2c1e17b-f50f-5547-aa5f-62643100d506` | 517-520 [crates/gcode/src/contract.rs:517-520] | Indexed function `ai_flag` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:517-520] |
| `token_budget_flag` | function | `fn token_budget_flag() -> FlagContract {` | `token_budget_flag [function]` | `9c56a4aa-54dc-54ae-b042-74df15dc23bb` | 522-524 [crates/gcode/src/contract.rs:522-524] | Indexed function `token_budget_flag` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:522-524] |
| `search_flags` | function | `fn search_flags() -> Vec<FlagContract> {` | `search_flags [function]` | `8dd3bcc8-873b-5536-a691-ae0bc58ffd42` | 526-533 [crates/gcode/src/contract.rs:526-533] | Indexed function `search_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:526-533] |
| `grep_flags` | function | `fn grep_flags() -> Vec<FlagContract> {` | `grep_flags [function]` | `a547e5a5-101d-525c-afc8-d670de458389` | 535-547 [crates/gcode/src/contract.rs:535-547] | Indexed function `grep_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:535-547] |
| `graph_read_flags` | function | `fn graph_read_flags() -> Vec<FlagContract> {` | `graph_read_flags [function]` | `13fcdc31-8c6b-51a9-bf53-a18a7fe0b106` | 549-555 [crates/gcode/src/contract.rs:549-555] | Indexed function `graph_read_flags` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:549-555] |
| `search_keys` | function | `fn search_keys() -> Vec<&'static str> {` | `search_keys [function]` | `f1e0d1f0-6048-538e-8f33-ec317c4cfaee` | 557-575 [crates/gcode/src/contract.rs:557-575] | Indexed function `search_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:557-575] |
| `grep_keys` | function | `fn grep_keys() -> Vec<&'static str> {` | `grep_keys [function]` | `0cca9616-0896-50ac-9e18-18764aedca3c` | 577-600 [crates/gcode/src/contract.rs:577-600] | Indexed function `grep_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:577-600] |
| `graph_read_keys` | function | `fn graph_read_keys() -> Vec<&'static str> {` | `graph_read_keys [function]` | `2a02b4ff-9e5d-58d4-a063-b310b50ae10c` | 602-619 [crates/gcode/src/contract.rs:602-619] | Indexed function `graph_read_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:602-619] |
| `graph_path_keys` | function | `fn graph_path_keys() -> Vec<&'static str> {` | `graph_path_keys [function]` | `33936443-5db3-5b23-9381-0d34dd953cfd` | 621-638 [crates/gcode/src/contract.rs:621-638] | Indexed function `graph_path_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:621-638] |
| `contract_keys` | function | `fn contract_keys() -> Vec<&'static str> {` | `contract_keys [function]` | `6080c714-8d50-5036-bcfe-9e3166bea80e` | 640-650 [crates/gcode/src/contract.rs:640-650] | Indexed function `contract_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:640-650] |
| `graph_payload_keys` | function | `fn graph_payload_keys() -> Vec<&'static str> {` | `graph_payload_keys [function]` | `0f0cefda-b242-5199-98b7-95fc3c92a8f5` | 652-654 [crates/gcode/src/contract.rs:652-654] | Indexed function `graph_payload_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:652-654] |
| `graph_lifecycle_keys` | function | `fn graph_lifecycle_keys() -> Vec<&'static str> {` | `graph_lifecycle_keys [function]` | `c6fee3bb-3690-57bf-8fc8-d99892901ed4` | 656-668 [crates/gcode/src/contract.rs:656-668] | Indexed function `graph_lifecycle_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:656-668] |
| `graph_cleanup_keys` | function | `fn graph_cleanup_keys() -> Vec<&'static str> {` | `graph_cleanup_keys [function]` | `21c550f1-40e9-5a65-85fc-4bcdc3e20c9e` | 670-678 [crates/gcode/src/contract.rs:670-678] | Indexed function `graph_cleanup_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:670-678] |
| `graph_report_keys` | function | `fn graph_report_keys() -> Vec<&'static str> {` | `graph_report_keys [function]` | `3780b278-45f0-5762-b48a-5a6087a0ca89` | 680-682 [crates/gcode/src/contract.rs:680-682] | Indexed function `graph_report_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:680-682] |
| `vector_lifecycle_keys` | function | `fn vector_lifecycle_keys() -> Vec<&'static str> {` | `vector_lifecycle_keys [function]` | `082de58a-de6b-5f90-b4ea-b538f738b0b3` | 684-697 [crates/gcode/src/contract.rs:684-697] | Indexed function `vector_lifecycle_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:684-697] |
| `vector_cleanup_keys` | function | `fn vector_cleanup_keys() -> Vec<&'static str> {` | `vector_cleanup_keys [function]` | `466dbf2a-1ef3-52bc-868d-c3eca324590f` | 699-711 [crates/gcode/src/contract.rs:699-711] | Indexed function `vector_cleanup_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:699-711] |
| `embeddings_doctor_keys` | function | `fn embeddings_doctor_keys() -> Vec<&'static str> {` | `embeddings_doctor_keys [function]` | `2e85b36a-9b4c-5bee-8045-2c92d701f3e2` | 713-723 [crates/gcode/src/contract.rs:713-723] | Indexed function `embeddings_doctor_keys` in `crates/gcode/src/contract.rs`. [crates/gcode/src/contract.rs:713-723] |
