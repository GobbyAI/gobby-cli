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

This file defines the `librarian` command entry point. `execute` delegates to the shared analysis-command runner with the command name, selected scope, a fixed report description, the default `librarian` analysis options, and `librarian::render_text` to turn the serialized proposals report into text output. [crates/gwiki/src/commands/librarian.rs:3-11]

## API Symbols

- `execute` (function) component `execute [function]` (`ce00f6fd-84c3-5e9b-940b-9e677acbac9c`) lines 3-11 [crates/gwiki/src/commands/librarian.rs:3-11]
  - Signature: `pub(crate) fn execute(selection: ScopeSelection) -> Result<CommandOutcome, WikiError> {`
  - Purpose: # Summary

Executes a librarian analysis command that serializes proposals report data for the specified scope selection and renders the output as text. [crates/gwiki/src/commands/librarian.rs:3-11]

