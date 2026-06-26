---
title: crates/gcode/src/index
type: code_module
provenance:
- file: crates/gcode/src/index/api.rs
- file: crates/gcode/src/index/import_resolution/context.rs
- file: crates/gcode/src/index/import_resolution/context/apple.rs
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
- file: crates/gcode/src/index/import_resolution/helpers.rs
- file: crates/gcode/src/index/import_resolution/js_local.rs
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
- file: crates/gcode/src/index/import_resolution/predicates.rs
- file: crates/gcode/src/index/import_resolution/rust_local.rs
- file: crates/gcode/src/index/indexer/file.rs
- file: crates/gcode/src/index/indexer/freshness_probe.rs
- file: crates/gcode/src/index/indexer/lifecycle.rs
- file: crates/gcode/src/index/indexer/overlay.rs
- file: crates/gcode/src/index/indexer/sink.rs
- file: crates/gcode/src/index/indexer/types.rs
- file: crates/gcode/src/index/indexer/util.rs
- file: crates/gcode/src/index/languages.rs
- file: crates/gcode/src/index/parser.rs
- file: crates/gcode/src/index/parser/calls/ast.rs
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
- file: crates/gcode/src/index/parser/calls/resolution.rs
- file: crates/gcode/src/index/parser/calls/shadowing.rs
- file: crates/gcode/src/index/parser/calls/text.rs
- file: crates/gcode/src/index/security.rs
- file: crates/gcode/src/index/semantic.rs
- file: crates/gcode/src/index/walker/hidden.rs
provenance_truncated: 29
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/index` contains 18 direct files and 4 child modules.
[crates/gcode/src/index/api.rs:16-23]
[crates/gcode/src/index/chunker.rs:19-62]
[crates/gcode/src/index/hasher.rs:7-9]
[crates/gcode/src/index/import_resolution.rs:1-26]
[crates/gcode/src/index/import_resolution/context.rs:41-138]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/import_resolution\|crates/gcode/src/index/import_resolution]] | `crates/gcode/src/index/import_resolution` contains 21 direct files and 2 child modules. [crates/gcode/src/index/import_resolution/context.rs:41-138] [crates/gcode/src/index/import_resolution/context/apple.rs:8-12] [crates/gcode/src/index/import_resolution/context/bindings.rs:6-9] [crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17] [crates/gcode/src/index/import_resolution/context/elixir.rs:13-49] |
| [[code/modules/crates/gcode/src/index/indexer\|crates/gcode/src/index/indexer]] | `crates/gcode/src/index/indexer` contains 10 direct files and 0 child modules. [crates/gcode/src/index/indexer/file.rs:15-91] [crates/gcode/src/index/indexer/freshness_probe.rs:37-81] [crates/gcode/src/index/indexer/lifecycle.rs:16-54] [crates/gcode/src/index/indexer/local_imports.rs:31-38] [crates/gcode/src/index/indexer/overlay.rs:33-36] |
| [[code/modules/crates/gcode/src/index/parser\|crates/gcode/src/index/parser]] | `crates/gcode/src/index/parser` contains 2 direct files and 1 child module. [crates/gcode/src/index/parser/calls.rs:26-35] [crates/gcode/src/index/parser/calls/ast.rs:17-103] [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55] [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119] [crates/gcode/src/index/parser/calls/resolution.rs:6-10] |
| [[code/modules/crates/gcode/src/index/walker\|crates/gcode/src/index/walker]] | `crates/gcode/src/index/walker` contains 6 direct files and 0 child modules. [crates/gcode/src/index/walker/classification.rs:15-52] [crates/gcode/src/index/walker/discovery.rs:12-17] [crates/gcode/src/index/walker/generated.rs:18-38] [crates/gcode/src/index/walker/hidden.rs:13-15] [crates/gcode/src/index/walker/tests.rs:11-17] |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/api.rs\|crates/gcode/src/index/api.rs]] | `crates/gcode/src/index/api.rs` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/src/index/chunker.rs\|crates/gcode/src/index/chunker.rs]] | `crates/gcode/src/index/chunker.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/index/hasher.rs\|crates/gcode/src/index/hasher.rs]] | `crates/gcode/src/index/hasher.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution.rs\|crates/gcode/src/index/import_resolution.rs]] | `crates/gcode/src/index/import_resolution.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/index/indexer.rs\|crates/gcode/src/index/indexer.rs]] | `crates/gcode/src/index/indexer.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/index/languages.rs\|crates/gcode/src/index/languages.rs]] | `crates/gcode/src/index/languages.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gcode/src/index/mod.rs\|crates/gcode/src/index/mod.rs]] | `crates/gcode/src/index/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser.rs\|crates/gcode/src/index/parser.rs]] | `crates/gcode/src/index/parser.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls.rs\|crates/gcode/src/index/parser/calls.rs]] | `crates/gcode/src/index/parser/calls.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/ast.rs\|crates/gcode/src/index/parser/calls/ast.rs]] | `crates/gcode/src/index/parser/calls/ast.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/dart_textual.rs\|crates/gcode/src/index/parser/calls/dart_textual.rs]] | `crates/gcode/src/index/parser/calls/dart_textual.rs` exposes 21 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/objc_ast.rs\|crates/gcode/src/index/parser/calls/objc_ast.rs]] | `crates/gcode/src/index/parser/calls/objc_ast.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/resolution.rs\|crates/gcode/src/index/parser/calls/resolution.rs]] | `crates/gcode/src/index/parser/calls/resolution.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/shadowing.rs\|crates/gcode/src/index/parser/calls/shadowing.rs]] | `crates/gcode/src/index/parser/calls/shadowing.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/index/parser/calls/text.rs\|crates/gcode/src/index/parser/calls/text.rs]] | `crates/gcode/src/index/parser/calls/text.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/index/security.rs\|crates/gcode/src/index/security.rs]] | `crates/gcode/src/index/security.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/index/semantic.rs\|crates/gcode/src/index/semantic.rs]] | `crates/gcode/src/index/semantic.rs` exposes 56 indexed API symbols. |
| [[code/files/crates/gcode/src/index/walker.rs\|crates/gcode/src/index/walker.rs]] | `crates/gcode/src/index/walker.rs` has no indexed API symbols. |

