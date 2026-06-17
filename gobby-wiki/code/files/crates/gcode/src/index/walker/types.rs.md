---
title: crates/gcode/src/index/walker/types.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/types.rs
  ranges:
  - 3-6
  - 9-11
  - 14-18
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/walker/types.rs:3-6](crates/gcode/src/index/walker/types.rs#L3-L6), [crates/gcode/src/index/walker/types.rs:9-11](crates/gcode/src/index/walker/types.rs#L9-L11), [crates/gcode/src/index/walker/types.rs:14-18](crates/gcode/src/index/walker/types.rs#L14-L18)

</details>

# crates/gcode/src/index/walker/types.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

Defines the indexing walker’s core types: `FileClassification` describes whether a file is indexed as full AST data or content only, and `DiscoveryOptions` carries discovery behavior flags, currently just whether `.gitignore` rules are respected. `DiscoveryOptions::default` enables gitignore respect by default so callers get conservative file discovery unless they opt out.
[crates/gcode/src/index/walker/types.rs:3-6]
[crates/gcode/src/index/walker/types.rs:9-11]
[crates/gcode/src/index/walker/types.rs:14-18]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `FileClassification` | type | `pub enum FileClassification {` | `FileClassification [type]` | `7c87077a-f68d-52c7-bb6f-d5901c757cd2` | 3-6 [crates/gcode/src/index/walker/types.rs:3-6] | Indexed type `FileClassification` in `crates/gcode/src/index/walker/types.rs`. [crates/gcode/src/index/walker/types.rs:3-6] |
| `DiscoveryOptions` | class | `pub struct DiscoveryOptions {` | `DiscoveryOptions [class]` | `f06ddb92-61e4-5deb-a6b5-d7cb883a2d84` | 9-11 [crates/gcode/src/index/walker/types.rs:9-11] | Indexed class `DiscoveryOptions` in `crates/gcode/src/index/walker/types.rs`. [crates/gcode/src/index/walker/types.rs:9-11] |
| `DiscoveryOptions::default` | method | `fn default() -> Self {` | `DiscoveryOptions::default [method]` | `87f2dccf-a964-5cff-b02b-10019a2721f3` | 14-18 [crates/gcode/src/index/walker/types.rs:14-18] | Indexed method `DiscoveryOptions::default` in `crates/gcode/src/index/walker/types.rs`. [crates/gcode/src/index/walker/types.rs:14-18] |
