---
title: Deprecations
type: code_deprecations
provenance: []
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# Deprecations

This page is derived deterministically from a source scan of the documented files — no LLM. A symbol is listed when a `#[deprecated]` attribute or a `DEPRECATED` doc-comment sits directly above its definition (or in its docstring). Each row is the symbol that carries the marker, where it lives, and the recorded reason.

## [[code/files/crates/gcode/src/commands/codewiki/build_parts/audit.rs|crates/gcode/src/commands/codewiki/build_parts/audit.rs]]

| Symbol | Kind | Location | Reason |
| --- | --- | --- | --- |
| `looks_like_attribute_continuation` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:202` | ... |
| `deprecated_attribute_reason` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:213` | ... |
| `doc_comment_deprecation` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:244` | Detect a `///` / `//!` doc-comment line mentioning the word `DEPRECATED` |
| `build_deprecations_doc` | function | `crates/gcode/src/commands/codewiki/build_parts/audit.rs:277` | deprecated symbol grouped by file (the renderer groups). Never degrades. |

## [[code/files/crates/gcode/src/commands/codewiki/render/audit.rs|crates/gcode/src/commands/codewiki/render/audit.rs]]

| Symbol | Kind | Location | Reason |
| --- | --- | --- | --- |
| `render_deprecations_doc` | function | `crates/gcode/src/commands/codewiki/render/audit.rs:8` | deprecated symbol grouped by file; renders a clear "none found" line when |

## [[code/files/crates/gcode/src/commands/codewiki/types.rs|crates/gcode/src/commands/codewiki/types.rs]]

| Symbol | Kind | Location | Reason |
| --- | --- | --- | --- |
| `DeprecationIndex` | type | `crates/gcode/src/commands/codewiki/types.rs:289` | when nothing is deprecated; the scan never panics and never degrades. |
| `DeprecatedSymbol` | class | `crates/gcode/src/commands/codewiki/types.rs:301` | One deprecated symbol on the deterministic `code/deprecations.md` page |
| `DeprecationsDoc` | class | `crates/gcode/src/commands/codewiki/types.rs:314` | The deterministic deprecations aggregate page (#889), every deprecated |

