---
title: Start Here
type: code_onboarding
provenance:
- file: crates/gcode/src/commands/codewiki/io.rs
  ranges:
  - 3-9
  - 11-17
- file: crates/gcode/src/commands/codewiki/mod.rs
  ranges:
  - 81-86
  - 89-93
  - 96-105
  - 107-116
  - 120-123
  - 155-159
  - 281-293
  - '333'
  - 357-472
  - 500-505
- file: crates/gcode/src/commands/codewiki/prompts.rs
  ranges:
  - 11-33
  - 35-56
  - 58-72
  - 74-94
  - 96-110
  - 157-165
  - 168-171
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Start Here

## Entry Points

- [[code/files/crates/gcode/src/commands/codewiki/io.rs|crates/gcode/src/commands/codewiki/io.rs]] - write_doc_set public API `pub fn write_doc_set(out_dir: &Path, docs: &[(String, String)]) -> anyhow::Result<()> {`
- [[code/files/crates/gcode/src/commands/codewiki/io.rs|crates/gcode/src/commands/codewiki/io.rs]] - write_incremental_doc_set public API `pub fn write_incremental_doc_set(`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - CodewikiInput public API `pub struct CodewikiInput {`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - CodewikiGraphEdge public API `pub struct CodewikiGraphEdge {`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - CodewikiGraphEdge.call public API `pub fn call(`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - CodewikiGraphEdge.import public API `pub fn import(`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - CodewikiGraphEdgeKind public API `pub enum CodewikiGraphEdgeKind {`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - CodewikiGraphAvailability public API `pub enum CodewikiGraphAvailability {`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - CodewikiRunSummary public API `pub struct CodewikiRunSummary {`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - TextGenerator public API `pub type TextGenerator<'a> = dyn FnMut(&str, &str) -> Option<String> + 'a;`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - run public API `pub fn run(`
- [[code/files/crates/gcode/src/commands/codewiki/mod.rs|crates/gcode/src/commands/codewiki/mod.rs]] - generate_hierarchical_docs public API `pub fn generate_hierarchical_docs(`
- [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]] - symbol_prompt public API `pub fn symbol_prompt(symbol: &Symbol) -> String {`
- [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]] - file_prompt public API `pub fn file_prompt(file: &str, symbols: &[SymbolSummary]) -> String {`
- [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]] - module_prompt public API `pub fn module_prompt(`
- [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]] - repo_prompt public API `pub fn repo_prompt(modules: &[ChildSummary], files: &[ChildSummary]) -> String {`
- [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]] - architecture_prompt public API `pub fn architecture_prompt(`
- [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]] - SymbolSummary public API `pub struct SymbolSummary {`
- [[code/files/crates/gcode/src/commands/codewiki/prompts.rs|crates/gcode/src/commands/codewiki/prompts.rs]] - ChildSummary public API `pub struct ChildSummary {`

