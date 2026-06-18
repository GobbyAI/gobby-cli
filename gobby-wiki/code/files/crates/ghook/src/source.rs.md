---
title: crates/ghook/src/source.rs
type: code_file
provenance:
- file: crates/ghook/src/source.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/source.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/source.rs` exposes 7 indexed API symbols.

## How it fits

`crates/ghook/src/source.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `detect_source` | function | Returns 'cfg.source' unless it is '"claude"', in which case it prefers the non-empty 'GOBBY_SOURCE' environment variable and otherwise falls back to '"claude"'. [crates/ghook/src/source.rs:3-14] |
| `clear_source_env` | function | Removes the process environment variables 'GOBBY_SOURCE' and 'CLAUDE_CODE_ENTRYPOINT' to clear source-detection state for tests. [crates/ghook/src/source.rs:20-27] |
| `set_source_env` | function | Sets the process environment variable identified by 'key' to 'value' using 'std::env::set_var' inside an 'unsafe' block, with the safety assumption that this test module is the only code mutating these process-wide source-detection variables. [crates/ghook/src/source.rs:29-35] |
| `SourceEnvGuard` | class | 'SourceEnvGuard' is an opaque forward-declared 'struct' name with no visible members or behavior, so its semantics cannot be determined from the provided definition alone. [crates/ghook/src/source.rs:37] |
| `SourceEnvGuard::new` | method | Constructs a new 'Self' instance after calling 'clear_source_env()' to reset the source environment. [crates/ghook/src/source.rs:40-43] |
| `SourceEnvGuard::drop` | method | Invokes 'clear_source_env()' to clear the source environment when the value is dropped. [crates/ghook/src/source.rs:47-49] |
| `detect_source_respects_override_only_for_claude` | function | Verifies that 'detect_source' only honors 'GOBBY_SOURCE' as a compatibility override for Claude dispatches, ignores 'CLAUDE_CODE_ENTRYPOINT' by itself, preserves canonical sources for non-Claude CLIs, and ignores empty overrides. [crates/ghook/src/source.rs:53-87] |

