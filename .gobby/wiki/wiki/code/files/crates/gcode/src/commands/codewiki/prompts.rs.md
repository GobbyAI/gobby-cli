---
title: crates/gcode/src/commands/codewiki/prompts.rs
type: code_file
source_files:
- file: crates/gcode/src/commands/codewiki/prompts.rs
  ranges:
  - 10-32
  - 34-55
  - 57-90
  - 92-112
  - 115-123
  - 126-129
---

# crates/gcode/src/commands/codewiki/prompts.rs

Module: [[modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/prompts.rs` exposes 6 indexed API symbols. [crates/gcode/src/commands/codewiki/prompts.rs:10-32] [crates/gcode/src/commands/codewiki/prompts.rs:34-55] [crates/gcode/src/commands/codewiki/prompts.rs:57-90] [crates/gcode/src/commands/codewiki/prompts.rs:92-112] [crates/gcode/src/commands/codewiki/prompts.rs:115-123] [crates/gcode/src/commands/codewiki/prompts.rs:126-129]

## API Symbols

- `symbol_prompt` (function) component `symbol_prompt [function]` (`a8c20e75-e599-5d43-b5e7-baa63a832eb0`) lines 10-32 [crates/gcode/src/commands/codewiki/prompts.rs:10-32]
  - Signature: `pub fn symbol_prompt(symbol: &Symbol) -> String {`
  - Purpose: Formats a string prompt containing a Symbol's file path, qualified name, kind, line range, and optional signature and docstring. [crates/gcode/src/commands/codewiki/prompts.rs:10-32]
- `file_prompt` (function) component `file_prompt [function]` (`1b93934f-9750-5dda-b735-1d47567704d4`) lines 34-55 [crates/gcode/src/commands/codewiki/prompts.rs:34-55]
  - Signature: `pub fn file_prompt(file: &str, symbols: &[SymbolSummary]) -> String {`
  - Purpose: Constructs a formatted prompt string that aggregates a filename with its AST symbol metadata (name, kind, component identifier, line ranges, and purpose) for file summarization. [crates/gcode/src/commands/codewiki/prompts.rs:34-55]
- `module_prompt` (function) component `module_prompt [function]` (`d85ff83a-6038-5053-85fb-591a9b83c59d`) lines 57-90 [crates/gcode/src/commands/codewiki/prompts.rs:57-90]
  - Signature: `pub fn module_prompt(`
  - Purpose: Generates a structured prompt string that aggregates hierarchical summaries of files, child modules, and component IDs for a specified module to enable multi-level code summarization. [crates/gcode/src/commands/codewiki/prompts.rs:57-90]
- `repo_prompt` (function) component `repo_prompt [function]` (`b625d6cc-4160-5259-8cf9-f7f84a705165`) lines 92-112 [crates/gcode/src/commands/codewiki/prompts.rs:92-112]
  - Signature: `pub fn repo_prompt(modules: &[ChildSummary], files: &[ChildSummary]) -> String {`
  - Purpose: Constructs a prompt string that aggregates module and root-file summaries from `ChildSummary` slices, with fallback text for empty collections. [crates/gcode/src/commands/codewiki/prompts.rs:92-112]
- `SymbolSummary` (class) component `SymbolSummary [class]` (`e8058451-3af3-577b-ae65-63878ae8e6cc`) lines 115-123 [crates/gcode/src/commands/codewiki/prompts.rs:115-123]
  - Signature: `pub struct SymbolSummary {`
  - Purpose: `SymbolSummary` is a struct that aggregates metadata for a source code symbol, including its identifier, syntactic kind, component association, line range, and semantic purpose. [crates/gcode/src/commands/codewiki/prompts.rs:115-123]
- `ChildSummary` (class) component `ChildSummary [class]` (`02754726-8ede-5feb-befc-8ff822c0b6f0`) lines 126-129 [crates/gcode/src/commands/codewiki/prompts.rs:126-129]
  - Signature: `pub struct ChildSummary {`
  - Purpose: `ChildSummary` is a public struct that holds two String fields: a child entity's name and its summary description. [crates/gcode/src/commands/codewiki/prompts.rs:126-129]

