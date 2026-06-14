---
title: crates/gcore/src/codewiki_contract.rs
type: code_file
provenance:
- file: crates/gcore/src/codewiki_contract.rs
  ranges:
  - 64-86
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/codewiki_contract.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines the shared frontmatter contract for `codewiki`-generated wiki vault pages: the canonical keys and marker values that gcode writes and gwiki reads, plus a golden page fixture that freezes the expected degraded-page output. The test ties the fixture to the contract by asserting the golden page includes every required key and marker value, preventing producer/consumer drift. [crates/gcore/src/codewiki_contract.rs:64-86]

## API Symbols

- `golden_page_carries_every_contract_key_and_marker_value` (function) component `golden_page_carries_every_contract_key_and_marker_value [function]` (`572e29ca-57c6-5191-a6cf-038fbe0b7b1d`) lines 64-86 [crates/gcore/src/codewiki_contract.rs:64-86]
  - Signature: `fn golden_page_carries_every_contract_key_and_marker_value() {`
  - Purpose: Indexed function `golden_page_carries_every_contract_key_and_marker_value` in `crates/gcore/src/codewiki_contract.rs`. [crates/gcore/src/codewiki_contract.rs:64-86]

