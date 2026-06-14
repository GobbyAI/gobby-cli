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

This file implements the `run` function for the init command, which bootstraps a gcode project. It orchestrates three main steps: first, it resolves the project's identity and optionally generates a gcode.json configuration file; second, it installs AI CLI skills for all supported targets unless the project is Gobby-managed; and third, it prepares the database context needed for code indexing. The function aggregates configuration from multiple modules (config, project, skill, and db) to establish a fully initialized project environment. [crates/gcode/src/commands/init.rs:11-148]

## API Symbols

- `run` (function) component `run [function]` (`fe31a853-1683-5729-9359-f9f539491450`) lines 11-148 [crates/gcode/src/commands/init.rs:11-148]
  - Signature: `pub fn run(project_root: &Path, format: Format, quiet: bool) -> anyhow::Result<()> {`
  - Purpose: # Summary

Initializes a project by resolving its identity, installing AI CLI skills for supported targets (unless Gobby-managed), and configuring database prerequisites for code indexing. [crates/gcode/src/commands/init.rs:11-148]

