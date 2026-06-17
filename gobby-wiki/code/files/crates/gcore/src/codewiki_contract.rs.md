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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/codewiki_contract.rs:64-86](crates/gcore/src/codewiki_contract.rs#L64-L86)

</details>

# crates/gcore/src/codewiki_contract.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines the shared frontmatter contract for codewiki-generated wiki vault pages. The constants name the YAML keys and marker values that gcode emits and gwiki parses, while `GOLDEN_PAGE` captures the canonical degraded page layout, including provenance formatting and wikilink syntax, so both crates can pin their emitter/parser behavior against the same fixture and detect drift in tests. [crates/gcore/src/codewiki_contract.rs:64-86]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `golden_page_carries_every_contract_key_and_marker_value` | function | `fn golden_page_carries_every_contract_key_and_marker_value() {` | `golden_page_carries_every_contract_key_and_marker_value [function]` | `572e29ca-57c6-5191-a6cf-038fbe0b7b1d` | 64-86 [crates/gcore/src/codewiki_contract.rs:64-86] | Indexed function `golden_page_carries_every_contract_key_and_marker_value` in `crates/gcore/src/codewiki_contract.rs`. [crates/gcore/src/codewiki_contract.rs:64-86] |
