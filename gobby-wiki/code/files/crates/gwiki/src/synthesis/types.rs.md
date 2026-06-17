---
title: crates/gwiki/src/synthesis/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/types.rs
  ranges:
  - 9-13
  - 16-22
  - 24-30
  - 34-38
  - 41-50
  - 53-59
  - 62-68
  - 71-74
  - 78-81
  - 84-87
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/synthesis/types.rs:9-13](crates/gwiki/src/synthesis/types.rs#L9-L13), [crates/gwiki/src/synthesis/types.rs:16-22](crates/gwiki/src/synthesis/types.rs#L16-L22), [crates/gwiki/src/synthesis/types.rs:24-30](crates/gwiki/src/synthesis/types.rs#L24-L30), [crates/gwiki/src/synthesis/types.rs:34-38](crates/gwiki/src/synthesis/types.rs#L34-L38), [crates/gwiki/src/synthesis/types.rs:41-50](crates/gwiki/src/synthesis/types.rs#L41-L50), [crates/gwiki/src/synthesis/types.rs:53-59](crates/gwiki/src/synthesis/types.rs#L53-L59), [crates/gwiki/src/synthesis/types.rs:62-68](crates/gwiki/src/synthesis/types.rs#L62-L68), [crates/gwiki/src/synthesis/types.rs:71-74](crates/gwiki/src/synthesis/types.rs#L71-L74), [crates/gwiki/src/synthesis/types.rs:78-81](crates/gwiki/src/synthesis/types.rs#L78-L81), [crates/gwiki/src/synthesis/types.rs:84-87](crates/gwiki/src/synthesis/types.rs#L84-L87)

</details>

# crates/gwiki/src/synthesis/types.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Purpose

Defines the core data types for the wiki synthesis and page-write pipeline. `ArticleKind` identifies whether the output is a source, concept, or topic article and maps that choice to both its target directory and source-kind label; the surrounding structs carry synthesis inputs (`SynthesisSource`, `SynthesisInput`), generated prompt text (`SynthesisPrompt`), and the resulting page payload (`SynthesizedPage`, with an optional explainer report for compiled articles). `WritePolicy`, `PageWriteKind`, and `PageWriteOutcome` describe how a synthesized page may be written and whether that write created or overwrote a file.
[crates/gwiki/src/synthesis/types.rs:9-13]
[crates/gwiki/src/synthesis/types.rs:16-22]
[crates/gwiki/src/synthesis/types.rs:24-30]
[crates/gwiki/src/synthesis/types.rs:34-38]
[crates/gwiki/src/synthesis/types.rs:41-50]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ArticleKind` | type | `pub enum ArticleKind {` | `ArticleKind [type]` | `fb40bf25-69b2-5b00-aa18-746404bc7734` | 9-13 [crates/gwiki/src/synthesis/types.rs:9-13] | Indexed type `ArticleKind` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:9-13] |
| `ArticleKind::directory` | method | `pub fn directory(self) -> &'static str {` | `ArticleKind::directory [method]` | `21431119-194d-53a6-af44-8d9e9c405b2f` | 16-22 [crates/gwiki/src/synthesis/types.rs:16-22] | Indexed method `ArticleKind::directory` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:16-22] |
| `ArticleKind::source_kind` | method | `pub fn source_kind(self) -> &'static str {` | `ArticleKind::source_kind [method]` | `5d897595-73a4-576d-9f4e-4b9faf3be1f2` | 24-30 [crates/gwiki/src/synthesis/types.rs:24-30] | Indexed method `ArticleKind::source_kind` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:24-30] |
| `SynthesisSource` | class | `pub struct SynthesisSource {` | `SynthesisSource [class]` | `a5a52ff8-a19a-5061-ae79-0a17546d8b76` | 34-38 [crates/gwiki/src/synthesis/types.rs:34-38] | Indexed class `SynthesisSource` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:34-38] |
| `SynthesisInput` | class | `pub struct SynthesisInput {` | `SynthesisInput [class]` | `eccae649-6221-5eae-8d58-f57f8d51c46a` | 41-50 [crates/gwiki/src/synthesis/types.rs:41-50] | Indexed class `SynthesisInput` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:41-50] |
| `SynthesisPrompt` | class | `pub struct SynthesisPrompt {` | `SynthesisPrompt [class]` | `8946dc82-f2b7-559f-8631-8855772610a0` | 53-59 [crates/gwiki/src/synthesis/types.rs:53-59] | Indexed class `SynthesisPrompt` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:53-59] |
| `SynthesizedPage` | class | `pub struct SynthesizedPage {` | `SynthesizedPage [class]` | `534c3f96-98ef-546b-8ba7-bea9c94e8934` | 62-68 [crates/gwiki/src/synthesis/types.rs:62-68] | Indexed class `SynthesizedPage` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:62-68] |
| `WritePolicy` | type | `pub enum WritePolicy {` | `WritePolicy [type]` | `3127013d-7e2e-51e0-9884-4d3c26a55e8c` | 71-74 [crates/gwiki/src/synthesis/types.rs:71-74] | Indexed type `WritePolicy` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:71-74] |
| `PageWriteKind` | type | `pub enum PageWriteKind {` | `PageWriteKind [type]` | `a9cd13e0-2661-5365-9319-1f219574b051` | 78-81 [crates/gwiki/src/synthesis/types.rs:78-81] | Indexed type `PageWriteKind` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:78-81] |
| `PageWriteOutcome` | class | `pub struct PageWriteOutcome {` | `PageWriteOutcome [class]` | `cdf885f0-1cf7-5471-aafe-61189d8ac8ea` | 84-87 [crates/gwiki/src/synthesis/types.rs:84-87] | Indexed class `PageWriteOutcome` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:84-87] |
