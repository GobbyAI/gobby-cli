---
title: crates/gwiki/src/compile/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/mod.rs
  ranges:
  - 30-35
  - 38-41
  - 44-47
  - 49-56
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

# crates/gwiki/src/compile/mod.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

This module defines the data types and orchestration entry points for compiling a research session into a wiki-ready handoff and, when requested, synthesized article output. `CompileRequest`, `CompileBundle`, `CompileOutcome`, and the accepted-source structs carry the topic, outline, citations, source chunks, target page, and write intent through the pipeline, while `WikiCompileOptions` and `WikiCompileOutcome` configure and report the wiki-specific compilation run. The public `compile_to_wiki` wrapper uses default options, and `compile_to_wiki_with_options` and `prepare_handoff` normalize the target page, gather and render sources, write the handoff bundle, optionally write the target page, and assemble the resulting compile state and synthesis inputs; `index_lock_timeout` provides the timeout used for index locking from an environment override or default.
[crates/gwiki/src/compile/mod.rs:30-35]
[crates/gwiki/src/compile/mod.rs:38-41]
[crates/gwiki/src/compile/mod.rs:44-47]
[crates/gwiki/src/compile/mod.rs:49-56]
[crates/gwiki/src/compile/mod.rs:50-55]

## API Symbols

- `CompileRequest` (class) component `CompileRequest [class]` (`b23540e3-d38d-56c1-90c9-14963213139f`) lines 30-35 [crates/gwiki/src/compile/mod.rs:30-35]
  - Signature: `pub struct CompileRequest {`
  - Purpose: 'CompileRequest' is a Rust request payload that carries a 'topic', an 'outline' of string sections, an optional 'target_page' path, and a 'write_intent' flag indicating whether the compile operation is intended to persist output. [crates/gwiki/src/compile/mod.rs:30-35]
- `CompileOutcome` (class) component `CompileOutcome [class]` (`b6734559-97c0-5e96-a3e5-8caf50e357d2`) lines 38-41 [crates/gwiki/src/compile/mod.rs:38-41]
  - Signature: `pub struct CompileOutcome {`
  - Purpose: 'CompileOutcome' is a Rust struct that pairs a 'CompileBundle' with the resulting 'CompileState'. [crates/gwiki/src/compile/mod.rs:38-41]
- `WikiCompileOptions` (class) component `WikiCompileOptions [class]` (`192531a0-7c72-5348-bec2-7886adba8b49`) lines 44-47 [crates/gwiki/src/compile/mod.rs:44-47]
  - Signature: `pub struct WikiCompileOptions {`
  - Purpose: 'WikiCompileOptions' is a configuration struct that specifies the target 'ArticleKind' to compile for and whether daemon synthesis is available during compilation. [crates/gwiki/src/compile/mod.rs:44-47]
- `WikiCompileOptions` (class) component `WikiCompileOptions [class]` (`e81f90b8-c658-5938-b818-ed7d561f298f`) lines 49-56 [crates/gwiki/src/compile/mod.rs:49-56]
  - Signature: `impl Default for WikiCompileOptions {`
  - Purpose: 'WikiCompileOptions' defines the default wiki compilation settings, initializing 'target_kind' to 'ArticleKind::Topic' and 'daemon_synthesis_available' to 'false'. [crates/gwiki/src/compile/mod.rs:49-56]
- `WikiCompileOptions.default` (method) component `WikiCompileOptions.default [method]` (`d8ef38af-aeb1-5853-b421-1de93e7d1323`) lines 50-55 [crates/gwiki/src/compile/mod.rs:50-55]
  - Signature: `fn default() -> Self {`
  - Purpose: Constructs a 'Self' instance with 'target_kind' initialized to 'ArticleKind::Topic' and 'daemon_synthesis_available' set to 'false'. [crates/gwiki/src/compile/mod.rs:50-55]
- `WikiCompileOutcome` (class) component `WikiCompileOutcome [class]` (`20be72c2-19de-56bf-b907-af8f59f9cad5`) lines 59-67 [crates/gwiki/src/compile/mod.rs:59-67]
  - Signature: `pub struct WikiCompileOutcome {`
  - Purpose: 'WikiCompileOutcome' is a result record for a wiki compilation run, capturing the handoff ID, generated article and index paths, contributing source paths, per-page write outcomes, the synthesis prompt used, and an optional explainer report. [crates/gwiki/src/compile/mod.rs:59-67]
- `CompileBundle` (class) component `CompileBundle [class]` (`088250f4-33b1-546d-8bf0-b1e977fdab7b`) lines 70-81 [crates/gwiki/src/compile/mod.rs:70-81]
  - Signature: `pub struct CompileBundle {`
  - Purpose: 'CompileBundle' is a data carrier for a compile/handoff operation, bundling the handoff metadata, topic outline, accepted sources, citations, conflict and evidence gaps, optional target page, write intent flag, and output path. [crates/gwiki/src/compile/mod.rs:70-81]
- `AcceptedCompileSource` (class) component `AcceptedCompileSource [class]` (`81e495a8-9423-5f49-895b-a6b785c011f5`) lines 84-89 [crates/gwiki/src/compile/mod.rs:84-89]
  - Signature: `pub struct AcceptedCompileSource {`
  - Purpose: 'AcceptedCompileSource' is a data container for an accepted compile input, holding a 'title', a filesystem 'path', the source split into 'chunks', and corresponding 'chunk_offsets' for those chunks. [crates/gwiki/src/compile/mod.rs:84-89]
- `AcceptedCompileChunkOffset` (class) component `AcceptedCompileChunkOffset [class]` (`3f17d229-f900-5fe6-b1ca-8bc44882b1b1`) lines 92-95 [crates/gwiki/src/compile/mod.rs:92-95]
  - Signature: `pub struct AcceptedCompileChunkOffset {`
  - Purpose: 'AcceptedCompileChunkOffset' is a struct that stores the accepted byte-range boundaries of a compile chunk via 'byte_start' and 'byte_end' offsets. [crates/gwiki/src/compile/mod.rs:92-95]
- `compile_to_wiki` (function) component `compile_to_wiki [function]` (`0659dfce-1c2b-5d6b-a343-0ec556862cf5`) lines 98-103 [crates/gwiki/src/compile/mod.rs:98-103]
  - Signature: `pub fn compile_to_wiki(`
  - Purpose: 'compile_to_wiki' is a thin wrapper that delegates the given 'ResearchSession' and 'CompileRequest' to 'compile_to_wiki_with_options' using 'WikiCompileOptions::default()' and no extra context, returning its 'WikiCompileOutcome' or 'WikiError'. [crates/gwiki/src/compile/mod.rs:98-103]
- `compile_to_wiki_with_options` (function) component `compile_to_wiki_with_options [function]` (`49c1e484-b88c-58a1-a53e-d6f7be9353a2`) lines 105-204 [crates/gwiki/src/compile/mod.rs:105-204]
  - Signature: `pub fn compile_to_wiki_with_options(`
  - Purpose: Normalizes the requested target page, prepares and records a wiki-compilation handoff from the research session and request, optionally renders and writes the target page when 'write_intent' is set, and assembles unique citations plus synthesis input for downstream wiki generation. [crates/gwiki/src/compile/mod.rs:105-204]
- `prepare_handoff` (function) component `prepare_handoff [function]` (`05b8ac7e-6c62-5efc-9c94-e6f52519e4bd`) lines 206-280 [crates/gwiki/src/compile/mod.rs:206-280]
  - Signature: `pub fn prepare_handoff(`
  - Purpose: 'prepare_handoff' validates that 'request.topic' is non-empty, normalizes the target page, generates a unique compile handoff ID and bundle path, collects accepted sources from the session, renders and writes a '.gwiki/compile/{handoff_id}.md' bundle, and begins constructing a 'CompileState'/'CompileOutcome' for the handoff. [crates/gwiki/src/compile/mod.rs:206-280]
- `CollectedSources` (class) component `CollectedSources [class]` (`b05172c1-0012-5265-b08e-1fc88b7c1c04`) lines 283-288 [crates/gwiki/src/compile/mod.rs:283-288]
  - Signature: `pub(crate) struct CollectedSources {`
  - Purpose: 'CollectedSources' is an internal aggregation struct that groups accepted compile sources alongside citation strings, conflicting claims, and missing-evidence records for downstream evaluation or reporting. [crates/gwiki/src/compile/mod.rs:283-288]
- `index_lock_timeout` (function) component `index_lock_timeout [function]` (`37c3c1e1-1596-570c-8950-3d451ecff6b5`) lines 290-303 [crates/gwiki/src/compile/mod.rs:290-303]
  - Signature: `pub(crate) fn index_lock_timeout() -> Duration {`
  - Purpose: Returns the index lock timeout as a 'Duration', reading 'INDEX_LOCK_TIMEOUT_ENV' as a positive 'u64' millisecond value when present and otherwise falling back to 'DEFAULT_INDEX_LOCK_TIMEOUT_MS', while emitting a warning to stderr for invalid environment values. [crates/gwiki/src/compile/mod.rs:290-303]

