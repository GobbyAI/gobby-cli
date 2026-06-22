---
title: Call Extraction
type: code_concept
provenance:
- file: crates/gcode/src/index/parser/calls.rs
- file: crates/gcode/src/index/parser/calls/ast.rs
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
- file: crates/gcode/src/index/parser/calls/resolution.rs
- file: crates/gcode/src/index/parser/calls/shadowing.rs
- file: crates/gcode/src/index/parser/calls/text.rs
- file: crates/gcode/src/index/parser/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls.rs](crates/gcode/src/index/parser/calls.rs)
- [crates/gcode/src/index/parser/calls/ast.rs](crates/gcode/src/index/parser/calls/ast.rs)
- [crates/gcode/src/index/parser/calls/dart_textual.rs](crates/gcode/src/index/parser/calls/dart_textual.rs)
- [crates/gcode/src/index/parser/calls/objc_ast.rs](crates/gcode/src/index/parser/calls/objc_ast.rs)
- [crates/gcode/src/index/parser/calls/resolution.rs](crates/gcode/src/index/parser/calls/resolution.rs)
- [crates/gcode/src/index/parser/calls/shadowing.rs](crates/gcode/src/index/parser/calls/shadowing.rs)
- [crates/gcode/src/index/parser/calls/text.rs](crates/gcode/src/index/parser/calls/text.rs)
- [crates/gcode/src/index/parser/tests.rs](crates/gcode/src/index/parser/tests.rs)

</details>

# Call Extraction

## Purpose

Call Extraction is the part of the indexer that discovers *where one piece of code invokes another* and turns those discoveries into concrete call relations the rest of the system can query. It solves the problem of building a cross-reference graph of calls — knowing that a given call site refers to a particular callable — across a codebase that may span many languages. To do this reliably it combines AST-guided discovery (walking parsed syntax trees) with textual fallbacks, classifies each call site by its syntax kind, and accounts for local-binding shadowing so that a name introduced in an inner scope is not mistakenly resolved to a same-named definition elsewhere. The result is a materialized set of call edges produced by the parser layer in `crates/gcode/src/index/parser/calls` [crates/gcode/src/index/parser/calls/ast.rs:17-103].

## Covers / Does not cover

This concept covers the call-site side of indexing: finding candidate call sites both through the AST and through textual scanning, classifying them by syntax kind, applying local-binding shadowing checks during resolution, and emitting the resulting call relations across the supported languages. The driving logic lives in the `calls` module and its `ast` submodule [crates/gcode/src/index/parser/calls.rs:26-35] [crates/gcode/src/index/parser/calls/ast.rs:17-103].

It does not cover how source is initially parsed into an AST, how definitions (the targets of calls) are discovered and stored, or how downstream consumers query the materialized relations. Those concerns belong to other parts of the surrounding `parser` and index modules and are out of scope here [crates/gcode/src/index/parser/calls.rs:26-35].

## Architecture

The architecture is organized as a small module hierarchy. The top-level `calls` module acts as the entry and coordination point for call extraction, while the `calls/ast` submodule provides the AST-guided discovery and classification logic [crates/gcode/src/index/parser/calls.rs:26-35] [crates/gcode/src/index/parser/calls/ast.rs:17-103]. This split exists so that the syntax-tree-aware work — which is the most structurally precise path — is isolated from the broader coordination, leaving room for the textual discovery path to serve as a complement when the AST does not yield a usable call site.

The reason for this arrangement is that different languages, and different fragments within a single file, offer different levels of structure. When a parsed AST is available, walking it gives reliable, syntax-kind-classified call sites; the `ast` submodule concentrates that responsibility [crates/gcode/src/index/parser/calls/ast.rs:17-103]. The `calls` module above it ties together AST results with textual scanning and the shadowing checks that keep local bindings from polluting resolution, then materializes the final call relations [crates/gcode/src/index/parser/calls.rs:26-35]. Keeping these layers separate lets the multi-language behavior be expressed once at the coordination level while language-shaped AST handling stays in the submodule.

## Data flow

The runtime flow of call extraction proceeds roughly as follows:

1. Call extraction is invoked for a source unit through the `calls` module, which coordinates the overall discovery [crates/gcode/src/index/parser/calls.rs:26-35].
2. When a parsed syntax tree is available, the `ast` submodule walks it to find candidate call sites in a structure-aware way [crates/gcode/src/index/parser/calls/ast.rs:17-103].
3. Each discovered call site is classified by its syntax kind so that the relation reflects the form of the invocation [crates/gcode/src/index/parser/calls/ast.rs:17-103].
4. Where AST-guided discovery is not available or sufficient, the coordination layer falls back to textual call-site discovery to capture candidates the syntax tree did not surface [crates/gcode/src/index/parser/calls.rs:26-35].
5. Candidate call sites are checked against local bindings so that a shadowed name is not resolved to an unrelated same-named target [crates/gcode/src/index/parser/calls.rs:26-35].
6. The surviving, resolved call sites are materialized into call relations across the supported languages [crates/gcode/src/index/parser/calls/ast.rs:17-103].

## Key components

The two modules below are the core of call extraction; the table is intentionally small and lists only the most important pieces.

| Symbol | Role |
| --- | --- |
| `crates/gcode/src/index/parser/calls` | Coordinates call extraction: ties together AST and textual discovery, applies local-binding shadowing checks, and materializes call relations [crates/gcode/src/index/parser/calls.rs:26-35] |
| `crates/gcode/src/index/parser/calls/ast` | AST-guided call-site discovery and syntax-kind classification [crates/gcode/src/index/parser/calls/ast.rs:17-103] |

## Where to start

Start by reading the top-level `calls` module, since it is the coordination point that frames the whole flow — discovery, shadowing checks, and materialization — and shows where the AST path fits in [crates/gcode/src/index/parser/calls.rs:26-35]. Once that overall shape is clear, move into the `calls/ast` submodule to see how syntax-tree walking and syntax-kind classification produce the precise call sites [crates/gcode/src/index/parser/calls/ast.rs:17-103].

## Explore

- [[code/modules/crates/gcode/src/index/parser|crates/gcode/src/index/parser]]
- [[code/modules/crates/gcode/src/index/parser/calls|crates/gcode/src/index/parser/calls]]

