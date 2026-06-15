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

This file defines the shared frontmatter contract for codewiki-generated gwiki pages, keeping the key names, marker values, and a golden page fixture in one place so gcode and gwiki can verify they stay in sync. The constants enumerate the exact YAML fields and marker strings codewiki emits and reads back, while `GOLDEN_PAGE` captures a canonical degraded file page that tests use to pin the emitter/parser behavior and prevent drift between the two crates. [crates/gcore/src/codewiki_contract.rs:64-86]

## API Symbols

- `golden_page_carries_every_contract_key_and_marker_value` (function) component `golden_page_carries_every_contract_key_and_marker_value [function]` (`572e29ca-57c6-5191-a6cf-038fbe0b7b1d`) lines 64-86 [crates/gcore/src/codewiki_contract.rs:64-86]
  - Signature: `fn golden_page_carries_every_contract_key_and_marker_value() {`
  - Purpose: Verifies that 'GOLDEN_PAGE' contains every required contract key marker, plus the expected generated-by, trust, freshness, and source file reference strings. [crates/gcore/src/codewiki_contract.rs:64-86]

