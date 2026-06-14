---
title: crates/gwiki/src/commands/librarian.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/librarian.rs
  ranges:
  - 3-11
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/librarian.rs

Module: [[code/modules/crates/gwiki/src/commands|crates/gwiki/src/commands]]

## Purpose

This file defines the `librarian` command entry point. Its `execute` function delegates to the shared `run_analysis_command` helper, passing the command name, a description, the selected scope, the librarian analysis runner with default options, and the text renderer so the command produces a serialized proposals report as text. [crates/gwiki/src/commands/librarian.rs:3-11]

## API Symbols

- `execute` (function) component `execute [function]` (`ce00f6fd-84c3-5e9b-940b-9e677acbac9c`) lines 3-11 [crates/gwiki/src/commands/librarian.rs:3-11]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: # Summary

Executes a librarian analysis command that serializes proposals report data for the specified scope selection and renders the output as text. [crates/gwiki/src/commands/librarian.rs:3-11]

