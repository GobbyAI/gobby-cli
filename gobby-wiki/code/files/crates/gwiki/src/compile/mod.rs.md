---
title: crates/gwiki/src/compile/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/mod.rs
  ranges:
  - 30-35
  - 38-41
  - 44-47
  - 50-55
  - 59-67
  - 70-81
  - 84-89
  - 92-95
  - 98-103
  - 105-204
  - 206-280
  - 283-288
  - 290-303
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/compile/mod.rs:30-35](crates/gwiki/src/compile/mod.rs#L30-L35), [crates/gwiki/src/compile/mod.rs:38-41](crates/gwiki/src/compile/mod.rs#L38-L41), [crates/gwiki/src/compile/mod.rs:44-47](crates/gwiki/src/compile/mod.rs#L44-L47), [crates/gwiki/src/compile/mod.rs:50-55](crates/gwiki/src/compile/mod.rs#L50-L55), [crates/gwiki/src/compile/mod.rs:59-67](crates/gwiki/src/compile/mod.rs#L59-L67), [crates/gwiki/src/compile/mod.rs:70-81](crates/gwiki/src/compile/mod.rs#L70-L81), [crates/gwiki/src/compile/mod.rs:84-89](crates/gwiki/src/compile/mod.rs#L84-L89), [crates/gwiki/src/compile/mod.rs:92-95](crates/gwiki/src/compile/mod.rs#L92-L95), [crates/gwiki/src/compile/mod.rs:98-103](crates/gwiki/src/compile/mod.rs#L98-L103), [crates/gwiki/src/compile/mod.rs:105-204](crates/gwiki/src/compile/mod.rs#L105-L204), [crates/gwiki/src/compile/mod.rs:206-280](crates/gwiki/src/compile/mod.rs#L206-L280), [crates/gwiki/src/compile/mod.rs:283-288](crates/gwiki/src/compile/mod.rs#L283-L288), [crates/gwiki/src/compile/mod.rs:290-303](crates/gwiki/src/compile/mod.rs#L290-L303)

</details>

# crates/gwiki/src/compile/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This module defines the data model and orchestration for compiling a wiki article from a research session. `CompileRequest` and `CompileOutcome` represent the top-level input/output for a compile, while `WikiCompileOptions` configures the target article kind and whether daemon synthesis is available, with a default of topic articles and no daemon support. `WikiCompileOutcome` packages the final article path, source and index paths, generated page writes, synthesis prompt, and optional explainer report. `CompileBundle` and the accepted-source/chunk structs capture the vetted evidence, citations, conflicts, and missing support that feed the compile. The main flow is split across `compile_to_wiki` and `compile_to_wiki_with_options`, which drive collection, synthesis, rendering, and handoff preparation through the helper modules, with `prepare_handoff` assembling the final bundle and `index_lock_timeout` controlling index locking via an environment-backed timeout.
[crates/gwiki/src/compile/mod.rs:30-35]
[crates/gwiki/src/compile/mod.rs:38-41]
[crates/gwiki/src/compile/mod.rs:44-47]
[crates/gwiki/src/compile/mod.rs:50-55]
[crates/gwiki/src/compile/mod.rs:59-67]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CompileRequest` | class | `pub struct CompileRequest {` | `CompileRequest [class]` | `b23540e3-d38d-56c1-90c9-14963213139f` | 30-35 [crates/gwiki/src/compile/mod.rs:30-35] | Indexed class `CompileRequest` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:30-35] |
| `CompileOutcome` | class | `pub struct CompileOutcome {` | `CompileOutcome [class]` | `b6734559-97c0-5e96-a3e5-8caf50e357d2` | 38-41 [crates/gwiki/src/compile/mod.rs:38-41] | Indexed class `CompileOutcome` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:38-41] |
| `WikiCompileOptions` | class | `pub struct WikiCompileOptions {` | `WikiCompileOptions [class]` | `192531a0-7c72-5348-bec2-7886adba8b49` | 44-47 [crates/gwiki/src/compile/mod.rs:44-47] | Indexed class `WikiCompileOptions` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:44-47] |
| `WikiCompileOptions::default` | method | `fn default() -> Self {` | `WikiCompileOptions::default [method]` | `d8ef38af-aeb1-5853-b421-1de93e7d1323` | 50-55 [crates/gwiki/src/compile/mod.rs:50-55] | Indexed method `WikiCompileOptions::default` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:50-55] |
| `WikiCompileOutcome` | class | `pub struct WikiCompileOutcome {` | `WikiCompileOutcome [class]` | `20be72c2-19de-56bf-b907-af8f59f9cad5` | 59-67 [crates/gwiki/src/compile/mod.rs:59-67] | Indexed class `WikiCompileOutcome` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:59-67] |
| `CompileBundle` | class | `pub struct CompileBundle {` | `CompileBundle [class]` | `088250f4-33b1-546d-8bf0-b1e977fdab7b` | 70-81 [crates/gwiki/src/compile/mod.rs:70-81] | Indexed class `CompileBundle` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:70-81] |
| `AcceptedCompileSource` | class | `pub struct AcceptedCompileSource {` | `AcceptedCompileSource [class]` | `81e495a8-9423-5f49-895b-a6b785c011f5` | 84-89 [crates/gwiki/src/compile/mod.rs:84-89] | Indexed class `AcceptedCompileSource` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:84-89] |
| `AcceptedCompileChunkOffset` | class | `pub struct AcceptedCompileChunkOffset {` | `AcceptedCompileChunkOffset [class]` | `3f17d229-f900-5fe6-b1ca-8bc44882b1b1` | 92-95 [crates/gwiki/src/compile/mod.rs:92-95] | Indexed class `AcceptedCompileChunkOffset` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:92-95] |
| `compile_to_wiki` | function | `pub fn compile_to_wiki(` | `compile_to_wiki [function]` | `0659dfce-1c2b-5d6b-a343-0ec556862cf5` | 98-103 [crates/gwiki/src/compile/mod.rs:98-103] | Indexed function `compile_to_wiki` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:98-103] |
| `compile_to_wiki_with_options` | function | `pub fn compile_to_wiki_with_options(` | `compile_to_wiki_with_options [function]` | `49c1e484-b88c-58a1-a53e-d6f7be9353a2` | 105-204 [crates/gwiki/src/compile/mod.rs:105-204] | Indexed function `compile_to_wiki_with_options` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:105-204] |
| `prepare_handoff` | function | `pub fn prepare_handoff(` | `prepare_handoff [function]` | `05b8ac7e-6c62-5efc-9c94-e6f52519e4bd` | 206-280 [crates/gwiki/src/compile/mod.rs:206-280] | Indexed function `prepare_handoff` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:206-280] |
| `CollectedSources` | class | `pub(crate) struct CollectedSources {` | `CollectedSources [class]` | `b05172c1-0012-5265-b08e-1fc88b7c1c04` | 283-288 [crates/gwiki/src/compile/mod.rs:283-288] | Indexed class `CollectedSources` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:283-288] |
| `index_lock_timeout` | function | `pub(crate) fn index_lock_timeout() -> Duration {` | `index_lock_timeout [function]` | `37c3c1e1-1596-570c-8950-3d451ecff6b5` | 290-303 [crates/gwiki/src/compile/mod.rs:290-303] | Indexed function `index_lock_timeout` in `crates/gwiki/src/compile/mod.rs`. [crates/gwiki/src/compile/mod.rs:290-303] |
