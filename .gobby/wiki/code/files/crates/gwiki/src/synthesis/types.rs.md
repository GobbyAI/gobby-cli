---
title: crates/gwiki/src/synthesis/types.rs
type: code_file
provenance:
- file: crates/gwiki/src/synthesis/types.rs
  ranges:
  - 9-13
  - 15-31
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

# crates/gwiki/src/synthesis/types.rs

Module: [[code/modules/crates/gwiki/src/synthesis|crates/gwiki/src/synthesis]]

## Purpose

This file defines the core data types for the synthesis pipeline: `ArticleKind` classifies generated content as source, concept, or topic and provides the matching knowledge directory and source-kind label; `SynthesisSource`, `SynthesisInput`, `SynthesisPrompt`, and `SynthesizedPage` carry the source material, job metadata, prompt text, and generated page artifact through synthesis; and `WritePolicy`, `PageWriteKind`, and `PageWriteOutcome` describe how page writes are allowed and what result was produced.
[crates/gwiki/src/synthesis/types.rs:9-13]
[crates/gwiki/src/synthesis/types.rs:15-31]
[crates/gwiki/src/synthesis/types.rs:16-22]
[crates/gwiki/src/synthesis/types.rs:24-30]
[crates/gwiki/src/synthesis/types.rs:34-38]

## API Symbols

- `ArticleKind` (type) component `ArticleKind [type]` (`fb40bf25-69b2-5b00-aa18-746404bc7734`) lines 9-13 [crates/gwiki/src/synthesis/types.rs:9-13]
  - Signature: `pub enum ArticleKind {`
  - Purpose: Indexed type `ArticleKind` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:9-13]
- `ArticleKind` (class) component `ArticleKind [class]` (`97652b28-47ed-5814-8c4e-1e8f45a4a043`) lines 15-31 [crates/gwiki/src/synthesis/types.rs:15-31]
  - Signature: `impl ArticleKind {`
  - Purpose: 'ArticleKind' is an enum helper that maps each variant ('Source', 'Concept', 'Topic') to its corresponding knowledge-base directory path and source kind string. [crates/gwiki/src/synthesis/types.rs:15-31]
- `ArticleKind.directory` (method) component `ArticleKind.directory [method]` (`21431119-194d-53a6-af44-8d9e9c405b2f`) lines 16-22 [crates/gwiki/src/synthesis/types.rs:16-22]
  - Signature: `pub fn directory(self) -> &'static str {`
  - Purpose: Returns the static directory path string corresponding to the enum variant, mapping 'Source' to 'knowledge/sources', 'Concept' to 'knowledge/concepts', and 'Topic' to 'knowledge/topics'. [crates/gwiki/src/synthesis/types.rs:16-22]
- `ArticleKind.source_kind` (method) component `ArticleKind.source_kind [method]` (`5d897595-73a4-576d-9f4e-4b9faf3be1f2`) lines 24-30 [crates/gwiki/src/synthesis/types.rs:24-30]
  - Signature: `pub fn source_kind(self) -> &'static str {`
  - Purpose: Returns a static string discriminator for the enum variant, mapping 'Source' to '"source_note"', 'Concept' to '"concept"', and 'Topic' to '"topic"'. [crates/gwiki/src/synthesis/types.rs:24-30]
- `SynthesisSource` (class) component `SynthesisSource [class]` (`a5a52ff8-a19a-5061-ae79-0a17546d8b76`) lines 34-38 [crates/gwiki/src/synthesis/types.rs:34-38]
  - Signature: `pub struct SynthesisSource {`
  - Purpose: 'SynthesisSource' is a Rust struct that stores a source title, its filesystem path, and an ordered collection of text chunks as 'String' values. [crates/gwiki/src/synthesis/types.rs:34-38]
- `SynthesisInput` (class) component `SynthesisInput [class]` (`eccae649-6221-5eae-8d58-f57f8d51c46a`) lines 41-50 [crates/gwiki/src/synthesis/types.rs:41-50]
  - Signature: `pub struct SynthesisInput {`
  - Purpose: 'SynthesisInput' is a Rust data struct that packages a synthesis job’s identifiers, topic, outline, target article kind, accepted sources, citations, and tracked evidence gaps or conflicts for downstream content generation. [crates/gwiki/src/synthesis/types.rs:41-50]
- `SynthesisPrompt` (class) component `SynthesisPrompt [class]` (`8946dc82-f2b7-559f-8631-8855772610a0`) lines 53-59 [crates/gwiki/src/synthesis/types.rs:53-59]
  - Signature: `pub struct SynthesisPrompt {`
  - Purpose: 'SynthesisPrompt' is a data container for a synthesized prompt, holding separate 'system' and 'user' strings plus metadata indicating daemon synthesis availability, estimated token count, and how many source inputs were truncated. [crates/gwiki/src/synthesis/types.rs:53-59]
- `SynthesizedPage` (class) component `SynthesizedPage [class]` (`534c3f96-98ef-546b-8ba7-bea9c94e8934`) lines 62-68 [crates/gwiki/src/synthesis/types.rs:62-68]
  - Signature: `pub struct SynthesizedPage {`
  - Purpose: 'SynthesizedPage' is a struct representing a generated page artifact, containing its filesystem 'path', 'title', rendered 'markdown' content, and an optional 'ExplainerReport' used only for compiled articles. [crates/gwiki/src/synthesis/types.rs:62-68]
- `WritePolicy` (type) component `WritePolicy [type]` (`3127013d-7e2e-51e0-9884-4d3c26a55e8c`) lines 71-74 [crates/gwiki/src/synthesis/types.rs:71-74]
  - Signature: `pub enum WritePolicy {`
  - Purpose: Indexed type `WritePolicy` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:71-74]
- `PageWriteKind` (type) component `PageWriteKind [type]` (`a9cd13e0-2661-5365-9319-1f219574b051`) lines 78-81 [crates/gwiki/src/synthesis/types.rs:78-81]
  - Signature: `pub enum PageWriteKind {`
  - Purpose: Indexed type `PageWriteKind` in `crates/gwiki/src/synthesis/types.rs`. [crates/gwiki/src/synthesis/types.rs:78-81]
- `PageWriteOutcome` (class) component `PageWriteOutcome [class]` (`cdf885f0-1cf7-5471-aafe-61189d8ac8ea`) lines 84-87 [crates/gwiki/src/synthesis/types.rs:84-87]
  - Signature: `pub struct PageWriteOutcome {`
  - Purpose: 'PageWriteOutcome' is a result record containing the destination 'PathBuf' and the 'PageWriteKind' classification for a page write operation. [crates/gwiki/src/synthesis/types.rs:84-87]

