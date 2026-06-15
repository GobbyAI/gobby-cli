---
title: crates/gcode/src/commands/init.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/init.rs
  ranges:
  - 11-148
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/init.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

Initializes a project for gcode by resolving or generating its project identity, optionally writing `gcode.json`, installing supported AI CLI skills unless the project is Gobby-managed, and preparing the database-backed indexing context. The `run` function ties these steps together: it derives the project status from identity source, reports or suppresses install output based on `quiet`, attempts skill installation for each supported target, then resolves the database URL and builds the indexing context needed to continue project setup. [crates/gcode/src/commands/init.rs:11-148]

## API Symbols

- `run` (function) component `run [function]` (`fe31a853-1683-5729-9359-f9f539491450`) lines 11-148 [crates/gcode/src/commands/init.rs:11-148]
  - Signature: `pub fn run(project_root: &Path, format: Format, quiet: bool) -> anyhow::Result<()> {`
  - Purpose: # Summary

Initializes a project by resolving its identity, installing AI CLI skills for supported targets (unless Gobby-managed), and configuring database prerequisites for code indexing. [crates/gcode/src/commands/init.rs:11-148]

