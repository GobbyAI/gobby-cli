---
title: crates/gwiki/src/compile/mod.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/mod.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/mod.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/compile/mod.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gwiki/src/compile/mod.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CompileRequest` | class | 'CompileRequest' is a request struct that carries a compilation topic, an ordered outline of sections, an optional output file path, and a flag indicating whether the compile operation is intended to write output. [crates/gwiki/src/compile/mod.rs:30-35] |
| `CompileOutcome` | class | 'CompileOutcome' is a struct that encapsulates the result of compilation by pairing a 'CompileBundle' with its corresponding 'CompileState'. [crates/gwiki/src/compile/mod.rs:38-41] |
| `WikiCompileOptions` | class | 'WikiCompileOptions' is a configuration struct that specifies the target article kind and whether daemon synthesis support is available for wiki compilation. [crates/gwiki/src/compile/mod.rs:44-47] |
| `WikiCompileOptions::default` | method | Constructs a 'Self' value with 'target_kind' initialized to 'ArticleKind::Topic' and 'daemon_synthesis_available' set to 'false'. [crates/gwiki/src/compile/mod.rs:50-55] |
| `WikiCompileOutcome` | class | 'WikiCompileOutcome' is a compilation result record containing the handoff identifier, generated article and index paths, the source file paths used, per-page write outcomes, the synthesis prompt, and an optional explainer report. [crates/gwiki/src/compile/mod.rs:59-67] |
| `CompileBundle` | class | 'CompileBundle' is a data container for a compilation request, holding the handoff identifier, topic, outline, accepted sources, citations, conflict and evidence gaps, an optional target page, a write-intent flag, and the output path. [crates/gwiki/src/compile/mod.rs:70-81] |
| `AcceptedCompileSource` | class | 'AcceptedCompileSource' is a data container for a compile-accepted source file, storing its 'title', filesystem 'path', ordered text 'chunks', and corresponding 'chunk_offsets' metadata. [crates/gwiki/src/compile/mod.rs:84-89] |
| `AcceptedCompileChunkOffset` | class | 'AcceptedCompileChunkOffset' is a struct that records an accepted compile chunk’s byte-range within the source as inclusive start and exclusive end offsets, stored in 'byte_start' and 'byte_end'. [crates/gwiki/src/compile/mod.rs:92-95] |
| `compile_to_wiki` | function | 'compile_to_wiki' is a thin wrapper that invokes 'compile_to_wiki_with_options' on the given 'ResearchSession' and 'CompileRequest' using 'WikiCompileOptions::default()' and no extra context, returning a 'WikiCompileOutcome' or 'WikiError'. [crates/gwiki/src/compile/mod.rs:98-103] |
| `compile_to_wiki_with_options` | function | Compiles a research session into a wiki handoff by normalizing the target page, preparing and recording compile state, optionally rendering and writing the bundle to the target page when 'write_intent' is set, and assembling accepted sources and citations into a synthesis input for the wiki compiler. [crates/gwiki/src/compile/mod.rs:105-204] |
| `prepare_handoff` | function | Validates that 'request.topic' is non-empty, normalizes the target page, generates a unique compile handoff ID, collects accepted sources, renders and writes a compile bundle Markdown file under the session state directory, and initializes the corresponding 'CompileState'. [crates/gwiki/src/compile/mod.rs:206-280] |
| `CollectedSources` | class | 'CollectedSources' is an internal aggregate that tracks accepted compile sources alongside associated citation strings, conflicting claims, and missing evidence entries. [crates/gwiki/src/compile/mod.rs:283-288] |
| `index_lock_timeout` | function | Returns the lock timeout as a 'Duration' by reading 'INDEX_LOCK_TIMEOUT_ENV', accepting only positive 'u64' millisecond values, and falling back to 'DEFAULT_INDEX_LOCK_TIMEOUT_MS' while emitting a warning for invalid environment values. [crates/gwiki/src/compile/mod.rs:290-303] |

