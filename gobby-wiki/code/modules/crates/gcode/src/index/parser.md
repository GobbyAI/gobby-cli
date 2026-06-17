---
title: crates/gcode/src/index/parser
type: code_module
provenance:
- file: crates/gcode/src/index/parser/calls.rs
  ranges:
  - 26-35
  - 38-45
  - 47-61
  - 63-443
  - 445-464
- file: crates/gcode/src/index/parser/calls/ast.rs
  ranges:
  - 17-103
  - 105-135
  - 148-179
  - 181-193
  - 196-205
  - 208-217
  - 220-235
  - 238-252
- file: crates/gcode/src/index/parser/calls/dart_textual.rs
  ranges:
  - 8-55
  - 57-77
  - 79-168
  - 170-172
  - 174-189
  - 191-216
  - 218-223
  - 226-232
  - 235-237
  - 239-243
  - 247-252
  - 255-259
  - 262-362
  - 364-366
  - 368-370
  - 373-375
  - 377-379
  - 381-391
  - 393-417
  - 419-441
  - 443-492
- file: crates/gcode/src/index/parser/calls/objc_ast.rs
  ranges:
  - 16-119
  - 121-140
  - 142-150
  - 152-169
  - 171-181
  - 183-189
  - 191-197
- file: crates/gcode/src/index/parser/calls/resolution.rs
  ranges:
  - 6-10
  - 17-21
  - 23-46
  - 48-62
  - 64-66
  - 68-96
  - 98-112
  - 114-122
  - 124-145
  - 147-202
  - 204-209
  - 211-222
  - 224-229
  - 239-285
- file: crates/gcode/src/index/parser/calls/shadowing.rs
  ranges:
  - 6-23
  - 25-43
  - 45-84
  - 86-96
  - 98-113
  - 115-129
  - 131-153
  - 155-218
  - 220-224
  - 226-235
  - 237-260
  - 262-273
  - 283-299
  - 302-315
  - 318-327
  - 330-339
  - 342-351
  - 354-363
- file: crates/gcode/src/index/parser/calls/text.rs
  ranges:
  - 4-20
  - 22-30
  - 32-49
  - 51-53
  - 55-57
  - 59-61
  - 63-65
  - 67-153
  - 160-165
  - 168-174
- file: crates/gcode/src/index/parser/tests.rs
  ranges:
  - 1-12
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls.rs:26-35](crates/gcode/src/index/parser/calls.rs#L26-L35), [crates/gcode/src/index/parser/calls.rs:38-45](crates/gcode/src/index/parser/calls.rs#L38-L45), [crates/gcode/src/index/parser/calls.rs:47-61](crates/gcode/src/index/parser/calls.rs#L47-L61), [crates/gcode/src/index/parser/calls.rs:63-443](crates/gcode/src/index/parser/calls.rs#L63-L443), [crates/gcode/src/index/parser/calls.rs:445-464](crates/gcode/src/index/parser/calls.rs#L445-L464)
- [crates/gcode/src/index/parser/calls/ast.rs:17-103](crates/gcode/src/index/parser/calls/ast.rs#L17-L103), [crates/gcode/src/index/parser/calls/ast.rs:105-135](crates/gcode/src/index/parser/calls/ast.rs#L105-L135), [crates/gcode/src/index/parser/calls/ast.rs:148-179](crates/gcode/src/index/parser/calls/ast.rs#L148-L179), [crates/gcode/src/index/parser/calls/ast.rs:181-193](crates/gcode/src/index/parser/calls/ast.rs#L181-L193), [crates/gcode/src/index/parser/calls/ast.rs:196-205](crates/gcode/src/index/parser/calls/ast.rs#L196-L205), [crates/gcode/src/index/parser/calls/ast.rs:208-217](crates/gcode/src/index/parser/calls/ast.rs#L208-L217), [crates/gcode/src/index/parser/calls/ast.rs:220-235](crates/gcode/src/index/parser/calls/ast.rs#L220-L235), [crates/gcode/src/index/parser/calls/ast.rs:238-252](crates/gcode/src/index/parser/calls/ast.rs#L238-L252)
- [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55](crates/gcode/src/index/parser/calls/dart_textual.rs#L8-L55), [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77](crates/gcode/src/index/parser/calls/dart_textual.rs#L57-L77), [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168](crates/gcode/src/index/parser/calls/dart_textual.rs#L79-L168), [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172](crates/gcode/src/index/parser/calls/dart_textual.rs#L170-L172), [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189](crates/gcode/src/index/parser/calls/dart_textual.rs#L174-L189), [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216](crates/gcode/src/index/parser/calls/dart_textual.rs#L191-L216), [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223](crates/gcode/src/index/parser/calls/dart_textual.rs#L218-L223), [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232](crates/gcode/src/index/parser/calls/dart_textual.rs#L226-L232), [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237](crates/gcode/src/index/parser/calls/dart_textual.rs#L235-L237), [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243](crates/gcode/src/index/parser/calls/dart_textual.rs#L239-L243), [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252](crates/gcode/src/index/parser/calls/dart_textual.rs#L247-L252), [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259](crates/gcode/src/index/parser/calls/dart_textual.rs#L255-L259), [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362](crates/gcode/src/index/parser/calls/dart_textual.rs#L262-L362), [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366](crates/gcode/src/index/parser/calls/dart_textual.rs#L364-L366), [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370](crates/gcode/src/index/parser/calls/dart_textual.rs#L368-L370), [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375](crates/gcode/src/index/parser/calls/dart_textual.rs#L373-L375), [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379](crates/gcode/src/index/parser/calls/dart_textual.rs#L377-L379), [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391](crates/gcode/src/index/parser/calls/dart_textual.rs#L381-L391), [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417](crates/gcode/src/index/parser/calls/dart_textual.rs#L393-L417), [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441](crates/gcode/src/index/parser/calls/dart_textual.rs#L419-L441), [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492](crates/gcode/src/index/parser/calls/dart_textual.rs#L443-L492)
- [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119](crates/gcode/src/index/parser/calls/objc_ast.rs#L16-L119), [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140](crates/gcode/src/index/parser/calls/objc_ast.rs#L121-L140), [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150](crates/gcode/src/index/parser/calls/objc_ast.rs#L142-L150), [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169](crates/gcode/src/index/parser/calls/objc_ast.rs#L152-L169), [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181](crates/gcode/src/index/parser/calls/objc_ast.rs#L171-L181), [crates/gcode/src/index/parser/calls/objc_ast.rs:183-189](crates/gcode/src/index/parser/calls/objc_ast.rs#L183-L189), [crates/gcode/src/index/parser/calls/objc_ast.rs:191-197](crates/gcode/src/index/parser/calls/objc_ast.rs#L191-L197)
- [crates/gcode/src/index/parser/calls/resolution.rs:6-10](crates/gcode/src/index/parser/calls/resolution.rs#L6-L10), [crates/gcode/src/index/parser/calls/resolution.rs:17-21](crates/gcode/src/index/parser/calls/resolution.rs#L17-L21), [crates/gcode/src/index/parser/calls/resolution.rs:23-46](crates/gcode/src/index/parser/calls/resolution.rs#L23-L46), [crates/gcode/src/index/parser/calls/resolution.rs:48-62](crates/gcode/src/index/parser/calls/resolution.rs#L48-L62), [crates/gcode/src/index/parser/calls/resolution.rs:64-66](crates/gcode/src/index/parser/calls/resolution.rs#L64-L66), [crates/gcode/src/index/parser/calls/resolution.rs:68-96](crates/gcode/src/index/parser/calls/resolution.rs#L68-L96), [crates/gcode/src/index/parser/calls/resolution.rs:98-112](crates/gcode/src/index/parser/calls/resolution.rs#L98-L112), [crates/gcode/src/index/parser/calls/resolution.rs:114-122](crates/gcode/src/index/parser/calls/resolution.rs#L114-L122), [crates/gcode/src/index/parser/calls/resolution.rs:124-145](crates/gcode/src/index/parser/calls/resolution.rs#L124-L145), [crates/gcode/src/index/parser/calls/resolution.rs:147-202](crates/gcode/src/index/parser/calls/resolution.rs#L147-L202), [crates/gcode/src/index/parser/calls/resolution.rs:204-209](crates/gcode/src/index/parser/calls/resolution.rs#L204-L209), [crates/gcode/src/index/parser/calls/resolution.rs:211-222](crates/gcode/src/index/parser/calls/resolution.rs#L211-L222), [crates/gcode/src/index/parser/calls/resolution.rs:224-229](crates/gcode/src/index/parser/calls/resolution.rs#L224-L229), [crates/gcode/src/index/parser/calls/resolution.rs:239-285](crates/gcode/src/index/parser/calls/resolution.rs#L239-L285)
- [crates/gcode/src/index/parser/calls/shadowing.rs:6-23](crates/gcode/src/index/parser/calls/shadowing.rs#L6-L23), [crates/gcode/src/index/parser/calls/shadowing.rs:25-43](crates/gcode/src/index/parser/calls/shadowing.rs#L25-L43), [crates/gcode/src/index/parser/calls/shadowing.rs:45-84](crates/gcode/src/index/parser/calls/shadowing.rs#L45-L84), [crates/gcode/src/index/parser/calls/shadowing.rs:86-96](crates/gcode/src/index/parser/calls/shadowing.rs#L86-L96), [crates/gcode/src/index/parser/calls/shadowing.rs:98-113](crates/gcode/src/index/parser/calls/shadowing.rs#L98-L113), [crates/gcode/src/index/parser/calls/shadowing.rs:115-129](crates/gcode/src/index/parser/calls/shadowing.rs#L115-L129), [crates/gcode/src/index/parser/calls/shadowing.rs:131-153](crates/gcode/src/index/parser/calls/shadowing.rs#L131-L153), [crates/gcode/src/index/parser/calls/shadowing.rs:155-218](crates/gcode/src/index/parser/calls/shadowing.rs#L155-L218), [crates/gcode/src/index/parser/calls/shadowing.rs:220-224](crates/gcode/src/index/parser/calls/shadowing.rs#L220-L224), [crates/gcode/src/index/parser/calls/shadowing.rs:226-235](crates/gcode/src/index/parser/calls/shadowing.rs#L226-L235), [crates/gcode/src/index/parser/calls/shadowing.rs:237-260](crates/gcode/src/index/parser/calls/shadowing.rs#L237-L260), [crates/gcode/src/index/parser/calls/shadowing.rs:262-273](crates/gcode/src/index/parser/calls/shadowing.rs#L262-L273), [crates/gcode/src/index/parser/calls/shadowing.rs:283-299](crates/gcode/src/index/parser/calls/shadowing.rs#L283-L299), [crates/gcode/src/index/parser/calls/shadowing.rs:302-315](crates/gcode/src/index/parser/calls/shadowing.rs#L302-L315), [crates/gcode/src/index/parser/calls/shadowing.rs:318-327](crates/gcode/src/index/parser/calls/shadowing.rs#L318-L327), [crates/gcode/src/index/parser/calls/shadowing.rs:330-339](crates/gcode/src/index/parser/calls/shadowing.rs#L330-L339), [crates/gcode/src/index/parser/calls/shadowing.rs:342-351](crates/gcode/src/index/parser/calls/shadowing.rs#L342-L351), [crates/gcode/src/index/parser/calls/shadowing.rs:354-363](crates/gcode/src/index/parser/calls/shadowing.rs#L354-L363)
- [crates/gcode/src/index/parser/calls/text.rs:4-20](crates/gcode/src/index/parser/calls/text.rs#L4-L20), [crates/gcode/src/index/parser/calls/text.rs:22-30](crates/gcode/src/index/parser/calls/text.rs#L22-L30), [crates/gcode/src/index/parser/calls/text.rs:32-49](crates/gcode/src/index/parser/calls/text.rs#L32-L49), [crates/gcode/src/index/parser/calls/text.rs:51-53](crates/gcode/src/index/parser/calls/text.rs#L51-L53), [crates/gcode/src/index/parser/calls/text.rs:55-57](crates/gcode/src/index/parser/calls/text.rs#L55-L57), [crates/gcode/src/index/parser/calls/text.rs:59-61](crates/gcode/src/index/parser/calls/text.rs#L59-L61), [crates/gcode/src/index/parser/calls/text.rs:63-65](crates/gcode/src/index/parser/calls/text.rs#L63-L65), [crates/gcode/src/index/parser/calls/text.rs:67-153](crates/gcode/src/index/parser/calls/text.rs#L67-L153), [crates/gcode/src/index/parser/calls/text.rs:160-165](crates/gcode/src/index/parser/calls/text.rs#L160-L165), [crates/gcode/src/index/parser/calls/text.rs:168-174](crates/gcode/src/index/parser/calls/text.rs#L168-L174)
- [crates/gcode/src/index/parser/tests.rs:1-12](crates/gcode/src/index/parser/tests.rs#L1-L12)

</details>

# crates/gcode/src/index/parser

Parent: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

The `crates/gcode/src/index/parser` module manages the parsing and extraction of call relations from indexed source files to construct structured `CallRelation` records. The central workflow is coordinated by `extract_calls`, which routes source tree and content representations to targeted language-specific extraction strategies [crates/gcode/src/index/parser/calls.rs:47-61]. It dispatches to AST-based query handlers (such as Tree-sitter matching for JavaScript, Elixir, and Objective-C) or specialized textual line scanners (such as for Dart) to discover raw call-like targets [crates/gcode/src/index/parser/calls.rs:47-61, crates/gcode/src/index/parser/calls/ast.rs:17-103, crates/gcode/src/index/parser/calls/objc_ast.rs:16-119].

To support this extraction, the module leverages `CallExtractionContext` to bundle critical parser, path, symbol, and import binding configurations during analysis [crates/gcode/src/index/parser/calls.rs:26-35]. Discovered syntactic candidates are packaged as `CallSite` instances [crates/gcode/src/index/parser/calls.rs:38-45] and resolved into final relations using `materialize_call`. This resolution maps candidates to enclosing caller symbols, handles language-specific qualifiers like Lua `require` blocks, and collaborates with semantic engines like `SemanticCallResolver` to yield fully materialized call relations [crates/gcode/src/index/parser/calls.rs:63-443, crates/gcode/src/index/parser/calls/ast.rs:17-103].

| Symbol | Type | Description | Citation |
| --- | --- | --- | --- |
| `CallExtractionContext` | Struct | Holds language, AST parser state, file paths, symbols, and import binding context. | [crates/gcode/src/index/parser/calls.rs:26-35] |
| `CallSite` | Struct | Represents an internally parsed, raw syntactic call candidate prior to resolution. | [crates/gcode/src/index/parser/calls.rs:38-45] |
| `extract_calls` | Function | Dispatches parsing and call extraction to AST-based or textual language-specific strategies. | [crates/gcode/src/index/parser/calls.rs:47-61] |
| `materialize_call` | Function | Resolves a syntactic `CallSite` into a concrete `CallRelation` using enclosing symbols and qualifiers. | [crates/gcode/src/index/parser/calls.rs:63-443] |
| `lua_require_qualifier_before_name` | Function | Recovering Lua-specific `require` call qualifiers from the underlying source file. | [crates/gcode/src/index/parser/calls.rs:445-464] |

## Dependency Diagram

`degraded: graph-truncated`

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/index/parser/calls\|crates/gcode/src/index/parser/calls]] | The crates/gcode/src/index/parser/calls module parses and extracts call relations from source files to construct CallRelation records. For AST-based languages like JavaScript, Elixir, and Objective-C, the module runs Tree-sitter queries to capture caller-callee pairings, handling language-specific cases such as Elixir definition heads and Objective-C receiver qualifiers [crates/gcode/src/index/parser/calls/ast.rs:17-103, crates/gcode/src/index/parser/calls/objc_ast.rs:16-119]. For Dart, it employs a textual line scanner that maintains lightweight state for code, strings, and comments to filter out class or module declarations and identify call-like candidates . This extraction workflow collaborates directly with semantic resolvers like SemanticCallResolver to translate syntactic candidates into fully materialized call entries . To resolve call targets, the module identifies enclosing symbols and classifies call syntax into Bare, Member, or Other syntax kinds [crates/gcode/src/index/parser/calls/resolution.rs:6-10, crates/gcode/src/index/parser/calls/resolution.rs:17-21, crates/gcode/src/index/parser/calls/resolution.rs:23-46]. Same-file callee resolution matches bare calls against callable symbols and splits qualified calls for namespace-based lookup [crates/gcode/src/index/parser/calls/resolution.rs:48-62]. Correctness is reinforced by a shadowing detection pipeline that inspects the caller's surrounding scope to prevent local bindings or parameters from being mistaken for external calls [crates/gcode/src/index/parser/calls/shadowing.rs:6-23, crates/gcode/src/index/parser/calls/shadowing.rs:25-43, crates/gcode/src/index/parser/calls/shadowing.rs:45-84]. Unicode-aware utilities support this processing by converting offsets, trimming identifiers, and filtering language-specific keywords [crates/gcode/src/index/parser/calls/text.rs:22-30, crates/gcode/src/index/parser/calls/text.rs:32-49, crates/gcode/src/index/parser/calls/text.rs:55-57]. Key Module Symbols: \| Symbol \| Kind \| Description \| Citation \| \| --- \| --- \| --- \| --- \| \| `extract_ast_calls` \| Function \| Compiles AST call queries, walks matches, and materializes call records for AST-supported languages. \| [crates/gcode/src/index/parser/calls/ast.rs:17-103] \| \| `extract_textual_dart_calls` \| Function \| Scans Dart source line by line using scanner states to filter declarations and extract candidate call relations. \| \| \| `CallSyntaxKind` \| Enum \| Categorizes call syntax into Bare, Member, or Other for resolution classification. \| [crates/gcode/src/index/parser/calls/resolution.rs:6-10] \| \| `enclosing_symbol` \| Function \| Identifies the deepest enclosing symbol in the file containing a given byte offset. \| [crates/gcode/src/index/parser/calls/resolution.rs:17-21] \| \| `call_syntax_kind` \| Function \| Assesses tree-sitter nodes to classify the call's syntax structure. \| [crates/gcode/src/index/parser/calls/resolution.rs:23-46] \| \| `resolve_same_file_callee` \| Function \| Maps a callee and qualifier path to a same-file symbol based on call syntax kind. \| [crates/gcode/src/index/parser/calls/resolution.rs:48-62] \| \| `external_call_is_shadowed` \| Function \| Determines if an external call target is shadowed by local parameter names or bindings. \| [crates/gcode/src/index/parser/calls/shadowing.rs:6-23] \| \| `utf16_column_at_byte` \| Function \| Calculates the UTF-16 column index at a given byte offset in the source. \| [crates/gcode/src/index/parser/calls/text.rs:22-30] \| \| `should_ignore_call_name` \| Function \| Determines if a parsed name should be skipped based on language keywords. \| [crates/gcode/src/index/parser/calls/text.rs:55-57] \| |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/parser/calls.rs\|crates/gcode/src/index/parser/calls.rs]] | This file builds call-relation extraction for indexed source files. `extract_calls` dispatches by language to language-specific strategies: textual Dart handling, Objective-C AST handling, or the general AST path. `CallExtractionContext` carries the file, symbol, import, and language state needed during extraction, while `CallSite` is the internal representation of a discovered call before it is turned into a `CallRelation`. `materialize_call` resolves a `CallSite` into a concrete relation by finding the enclosing caller symbol, adjusting qualifiers when needed, and optionally using semantic resolution. `lua_require_qualifier_before_name` is a Lua-specific helper for recovering `require` qualifiers from source text. [crates/gcode/src/index/parser/calls.rs:26-35] [crates/gcode/src/index/parser/calls.rs:38-45] [crates/gcode/src/index/parser/calls.rs:47-61] [crates/gcode/src/index/parser/calls.rs:63-443] [crates/gcode/src/index/parser/calls.rs:445-464] |
| [[code/files/crates/gcode/src/index/parser/tests.rs\|crates/gcode/src/index/parser/tests.rs]] | Test module entry point for the gcode index parser, declaring the parser test suites and shared test helpers for different language-specific and semantic/resolution cases. [crates/gcode/src/index/parser/tests.rs:1-12] |

## Components

| Component ID |
| --- |
| `d6a9337c-e91f-51f2-ab7a-3e09d9c76d54` |
| `bb7b96bd-5bc7-596e-bcdf-e71a138157c6` |
| `4fbb11be-6ade-5beb-8319-d251fa699b44` |
| `33296882-0bdf-5b08-889a-5c6ed6eef29a` |
| `134c9149-8205-5fa4-9544-0f9f1f3f3881` |
