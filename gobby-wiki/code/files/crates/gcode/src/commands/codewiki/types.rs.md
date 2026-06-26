---
title: crates/gcode/src/commands/codewiki/types.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/types.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/types.rs` exposes 66 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodewikiInput` | class | The 'CodewikiInput' struct aggregates file paths, dependency graph edges, graph availability, extracted code symbols, and leading file content chunks to serve as the structured input payload for generating aggregate code-wiki prompts. [crates/gcode/src/commands/codewiki/types.rs:11-21] |
| `LeadingChunk` | class | The 'LeadingChunk' struct represents a segment of text content along with its starting and ending line boundaries. [crates/gcode/src/commands/codewiki/types.rs:26-30] |
| `CodewikiTruthDigest` | class | Indexed class `CodewikiTruthDigest` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:33-43] |
| `CodewikiTruthStackEntry` | class | Indexed class `CodewikiTruthStackEntry` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:46-53] |
| `CodewikiTruthSuperseded` | class | Indexed class `CodewikiTruthSuperseded` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:56-59] |
| `source_excerpt_for_file` | function | Indexed function `source_excerpt_for_file` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:62-74] |
| `ranked_source_excerpts` | function | Indexed function `ranked_source_excerpts` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:79-91] |
| `CodewikiGraphEdge` | class | Indexed class `CodewikiGraphEdge` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:94-98] |
| `CodewikiGraphEdge::call` | method | Indexed method `CodewikiGraphEdge::call` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:101-110] |
| `CodewikiGraphEdge::import` | method | Indexed method `CodewikiGraphEdge::import` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:112-121] |
| `CodewikiGraphEdgeKind` | type | Indexed type `CodewikiGraphEdgeKind` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:125-128] |
| `CodewikiGraph` | class | Indexed class `CodewikiGraph` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:131-134] |
| `CodewikiGraph::available` | method | Indexed method `CodewikiGraph::available` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:137-142] |
| `CodewikiGraph::truncated` | method | Indexed method `CodewikiGraph::truncated` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:144-149] |
| `CodewikiGraph::unavailable` | method | Indexed method `CodewikiGraph::unavailable` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:151-156] |
| `CodewikiGraphAvailability` | type | Indexed type `CodewikiGraphAvailability` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:160-164] |
| `FileDoc` | class | Indexed class `FileDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:167-187] |
| `SymbolDoc` | class | Indexed class `SymbolDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:190-211] |
| `ModuleDoc` | class | Indexed class `ModuleDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:214-227] |
| `ArchitectureDoc` | class | Indexed class `ArchitectureDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:230-247] |
| `ArchitectureSubsystem` | class | Indexed class `ArchitectureSubsystem` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:250-255] |
| `InfraSection` | class | Indexed class `InfraSection` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:263-269] |
| `InfrastructureDoc` | class | Indexed class `InfrastructureDoc` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:276-279] |
| `FeatureEntry` | class | Indexed class `FeatureEntry` in `crates/gcode/src/commands/codewiki/types.rs`. [crates/gcode/src/commands/codewiki/types.rs:287-293] |

_42 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/codewiki/types.rs` for the full list._

