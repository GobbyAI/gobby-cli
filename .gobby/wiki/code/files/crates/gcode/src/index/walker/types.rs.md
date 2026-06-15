---
title: crates/gcode/src/index/walker/types.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/types.rs
  ranges:
  - 3-6
  - 9-11
  - 13-19
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/types.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Purpose

Defines the index walker’s core types: `FileClassification`, an enum for choosing whether a file is indexed as parsed AST or as content only, and `DiscoveryOptions`, a small configuration struct that controls discovery behavior via `respect_gitignore`. The pieces are tied together by `Default` for `DiscoveryOptions`, which enables `.gitignore` handling by default.
[crates/gcode/src/index/walker/types.rs:3-6]
[crates/gcode/src/index/walker/types.rs:9-11]
[crates/gcode/src/index/walker/types.rs:13-19]
[crates/gcode/src/index/walker/types.rs:14-18]

## API Symbols

- `FileClassification` (type) component `FileClassification [type]` (`7c87077a-f68d-52c7-bb6f-d5901c757cd2`) lines 3-6 [crates/gcode/src/index/walker/types.rs:3-6]
  - Signature: `pub enum FileClassification {`
  - Purpose: Indexed type `FileClassification` in `crates/gcode/src/index/walker/types.rs`. [crates/gcode/src/index/walker/types.rs:3-6]
- `DiscoveryOptions` (class) component `DiscoveryOptions [class]` (`f06ddb92-61e4-5deb-a6b5-d7cb883a2d84`) lines 9-11 [crates/gcode/src/index/walker/types.rs:9-11]
  - Signature: `pub struct DiscoveryOptions {`
  - Purpose: 'DiscoveryOptions' is a configuration struct with a single 'respect_gitignore: bool' field that controls whether discovery should honor '.gitignore' rules. [crates/gcode/src/index/walker/types.rs:9-11]
- `DiscoveryOptions` (class) component `DiscoveryOptions [class]` (`3b0f5972-0c42-5d06-baeb-0a58e7cde08c`) lines 13-19 [crates/gcode/src/index/walker/types.rs:13-19]
  - Signature: `impl Default for DiscoveryOptions {`
  - Purpose: 'DiscoveryOptions' is a configuration type whose 'Default' implementation enables 'respect_gitignore' by setting it to 'true'. [crates/gcode/src/index/walker/types.rs:13-19]
- `DiscoveryOptions.default` (method) component `DiscoveryOptions.default [method]` (`87f2dccf-a964-5cff-b02b-10019a2721f3`) lines 14-18 [crates/gcode/src/index/walker/types.rs:14-18]
  - Signature: `fn default() -> Self {`
  - Purpose: Returns a new 'Self' instance with 'respect_gitignore' initialized to 'true'. [crates/gcode/src/index/walker/types.rs:14-18]

