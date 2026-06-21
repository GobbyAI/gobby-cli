---
title: Import Resolution
type: code_concept
provenance:
- file: crates/gcode/src/index/import_resolution/context.rs
- file: crates/gcode/src/index/import_resolution/context/apple.rs
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
- file: crates/gcode/src/index/import_resolution/context/dotnet.rs
- file: crates/gcode/src/index/import_resolution/context/elixir.rs
- file: crates/gcode/src/index/import_resolution/context/jvm.rs
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
- file: crates/gcode/src/index/import_resolution/context/python.rs
- file: crates/gcode/src/index/import_resolution/context/scripting.rs
- file: crates/gcode/src/index/import_resolution/helpers.rs
- file: crates/gcode/src/index/import_resolution/js_local.rs
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
- file: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
- file: crates/gcode/src/index/import_resolution/parser/lua.rs
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
- file: crates/gcode/src/index/import_resolution/parser/objc.rs
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
- file: crates/gcode/src/index/import_resolution/parser/python_js.rs
- file: crates/gcode/src/index/import_resolution/parser/rest.rs
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
- file: crates/gcode/src/index/import_resolution/parser/shell.rs
- file: crates/gcode/src/index/import_resolution/predicates.rs
- file: crates/gcode/src/index/import_resolution/rust_local.rs
- file: crates/gcode/src/index/import_resolution/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context.rs](crates/gcode/src/index/import_resolution/context.rs)
- [crates/gcode/src/index/import_resolution/context/apple.rs](crates/gcode/src/index/import_resolution/context/apple.rs)
- [crates/gcode/src/index/import_resolution/context/bindings.rs](crates/gcode/src/index/import_resolution/context/bindings.rs)
- [crates/gcode/src/index/import_resolution/context/dotnet.rs](crates/gcode/src/index/import_resolution/context/dotnet.rs)
- [crates/gcode/src/index/import_resolution/context/elixir.rs](crates/gcode/src/index/import_resolution/context/elixir.rs)
- [crates/gcode/src/index/import_resolution/context/jvm.rs](crates/gcode/src/index/import_resolution/context/jvm.rs)
- [crates/gcode/src/index/import_resolution/context/package_metadata.rs](crates/gcode/src/index/import_resolution/context/package_metadata.rs)
- [crates/gcode/src/index/import_resolution/context/python.rs](crates/gcode/src/index/import_resolution/context/python.rs)
- [crates/gcode/src/index/import_resolution/context/scripting.rs](crates/gcode/src/index/import_resolution/context/scripting.rs)
- [crates/gcode/src/index/import_resolution/helpers.rs](crates/gcode/src/index/import_resolution/helpers.rs)
- [crates/gcode/src/index/import_resolution/js_local.rs](crates/gcode/src/index/import_resolution/js_local.rs)
- [crates/gcode/src/index/import_resolution/parser/go_rust.rs](crates/gcode/src/index/import_resolution/parser/go_rust.rs)

_12 more source files omitted._

</details>

# Import Resolution

## Purpose

Import Resolution is the cross-language engine that turns raw import statements — the `import`, `use`, `require`, `#import`, and equivalent directives found in source files — into concrete candidate files on disk. Its core job is *classification*: given a written dependency, decide whether it refers to another file inside the same project (a local dependency) or to something pulled in from outside the codebase (an external dependency), and do so consistently across more than a dozen language ecosystems.

This solves a problem that every code-indexing or cross-reference tool eventually hits: import syntax and resolution rules differ wildly between languages, yet downstream consumers want a single, uniform notion of "this symbol came from that file." By centralizing the parsing and the per-ecosystem resolution context in one module, the rest of the system can reason about dependencies without re-implementing each language's lookup semantics. The module lives under `crates/gcode/src/index/import_resolution` [crates/gcode/src/index/import_resolution/context.rs:41-138].

## Covers / Does not cover

This page covers the import resolution module as it is exposed by its two main submodules: the `parser` layer that reads import directives out of source [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40], and the `context` layer that supplies per-ecosystem resolution rules and turns parsed imports into candidate files [crates/gcode/src/index/import_resolution/context.rs:41-138]. It also covers the local-versus-external classification that is the module's central responsibility, and the fact that resolution is organized per ecosystem (for example, Apple/Objective-C-family contexts [crates/gcode/src/index/import_resolution/context/apple.rs:8-12], and combined Go/Rust parsing [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]).

It does not cover the broader indexing pipeline that invokes this module, the on-disk index format, or how candidate files are later consumed for cross-references — those live outside `import_resolution`. Because the supplied input exposes no indexed symbols and no source excerpts, this page does not enumerate individual functions, struct names, or signatures; it describes structure and intent only at the granularity the evidence supports.

## Architecture

The module is split into two cooperating layers, and the split is deliberate. The `parser` layer is responsible purely for *reading*: it extracts import directives from a source file's text and normalizes them into a parsed form independent of how they will eventually be resolved [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40]. The `context` layer is responsible for *resolving*: it holds the per-ecosystem knowledge needed to map a parsed import to candidate files and to decide whether that import is local or external [crates/gcode/src/index/import_resolution/context.rs:41-138].

Parsing and resolution are kept separate so that each can be specialized per ecosystem without coupling. On the parser side, languages with similar import grammars can share an implementation — Go and Rust are handled together in `parser/go_rust.rs` [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] — while the context side carries dedicated modules for ecosystems whose resolution rules differ, such as the Apple-family context in `context/apple.rs` [crates/gcode/src/index/import_resolution/context/apple.rs:8-12]. The top-level `context.rs` ties these per-ecosystem contexts together into the engine's shared resolution surface [crates/gcode/src/index/import_resolution/context.rs:41-138].

This arrangement is what makes the "cross-language" claim tractable: adding a new ecosystem means adding (or reusing) a parser for its import syntax and a context for its resolution rules, rather than threading new special cases through a single monolithic resolver.

## Data flow

The following traces the runtime flow from a raw source file to classified candidate files:

1. A source file is handed to the `parser` layer, which extracts its import directives and produces a normalized, parsed representation of each import [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40].
2. Each parsed import is paired with the appropriate per-ecosystem resolution context drawn from the `context` layer [crates/gcode/src/index/import_resolution/context.rs:41-138].
3. The context applies its ecosystem-specific rules — for example, the Apple-family rules in `context/apple.rs` for that family of imports [crates/gcode/src/index/import_resolution/context/apple.rs:8-12] — to attempt to map the import to one or more candidate files.
4. Based on whether that mapping lands inside the project, the import is classified as a local dependency (resolved to candidate files within the codebase) or an external dependency (originating outside it) [crates/gcode/src/index/import_resolution/context.rs:41-138].
5. The resulting candidate files and their local/external classification are returned to the caller for downstream indexing.

The supplied excerpts do not show explicit fallback behavior for the case where a step's dependency is unavailable, so this flow does not assert specific degraded-mode handling beyond the local-versus-external classification itself.

## Key components

The most important pieces are the two layers and the per-ecosystem specializations that hang off them.

| Component | Anchor | Role |
| --- | --- | --- |
| `import_resolution` (module root) | [crates/gcode/src/index/import_resolution/context.rs:41-138] | Top-level engine surface that ties parsing and per-ecosystem contexts into one resolver |
| `context` | [crates/gcode/src/index/import_resolution/context.rs:41-138] | Holds per-ecosystem resolution rules and drives local-vs-external classification |
| `context/apple` | [crates/gcode/src/index/import_resolution/context/apple.rs:8-12] | Apple-family ecosystem resolution context |
| `parser/go_rust` | [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] | Extracts and normalizes import directives for Go and Rust |

## Where to start

Begin with the top-level `context.rs` [crates/gcode/src/index/import_resolution/context.rs:41-138], since it defines the engine's shared resolution surface and shows how the per-ecosystem contexts are assembled and how local-versus-external classification is expressed. Once that overall shape is clear, read one parser to see the input side — `parser/go_rust.rs` is a good first choice because it covers two ecosystems at once [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] — and then a single specialized context such as `context/apple.rs` [crates/gcode/src/index/import_resolution/context/apple.rs:8-12] to see how one ecosystem plugs its resolution rules into the engine.

## Explore

- [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]
- [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]
- [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]

