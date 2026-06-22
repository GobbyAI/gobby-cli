---
title: crates/gwiki/src/synthesis/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/synthesis/types.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Overview

`crates/gwiki/src/synthesis/types.rs` exposes 10 indexed API symbols.

## How it fits

`crates/gwiki/src/synthesis/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ArticleKind` | type | Indexed type `ArticleKind` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:9-13] |
| `ArticleKind::directory` | method | Returns the static directory path string corresponding to the enum variant, mapping 'Source' to 'knowledge/sources', 'Concept' to 'knowledge/concepts', and 'Topic' to 'knowledge/topics'. [crates/gwiki/src/synthesis/types.rs:16-22] |
| `ArticleKind::source_kind` | method | Returns a static string label identifying the enum variant as '"source_note"', '"concept"', or '"topic"'. [crates/gwiki/src/synthesis/types.rs:24-30] |
| `SynthesisSource` | class | 'SynthesisSource' is a Rust data container holding a source title, a filesystem path, and an ordered list of text chunks. [crates/gwiki/src/synthesis/types.rs:34-38] |
| `SynthesisInput` | class | 'SynthesisInput' is a Rust data struct that packages a synthesis job’s handoff ID, topic, outline, target article kind, accepted sources, citations, and lists of conflicting claims and missing evidence for downstream generation or review. [crates/gwiki/src/synthesis/types.rs:41-50] |
| `SynthesisPrompt` | class | 'SynthesisPrompt' is a data structure that bundles the system and user prompt strings with synthesis metadata indicating daemon availability, estimated token count, and the number of truncated sources. [crates/gwiki/src/synthesis/types.rs:53-59] |
| `SynthesizedPage` | class | 'SynthesizedPage' is a struct representing a compiled page with a filesystem path, title, markdown content, and an optional 'ExplainerReport' used only for synthesized articles. [crates/gwiki/src/synthesis/types.rs:62-68] |
| `WritePolicy` | type | Indexed type `WritePolicy` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:71-74] |
| `PageWriteKind` | type | Indexed type `PageWriteKind` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:78-81] |
| `PageWriteOutcome` | class | 'PageWriteOutcome' is a struct that records the destination 'PathBuf' and 'PageWriteKind' resulting from a page write operation. [crates/gwiki/src/synthesis/types.rs:84-87] |

