---
title: crates/gcode/src/index/parser/calls
type: code_module
provenance:
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
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/parser/calls/ast.rs:17-103](crates/gcode/src/index/parser/calls/ast.rs#L17-L103), [crates/gcode/src/index/parser/calls/ast.rs:105-135](crates/gcode/src/index/parser/calls/ast.rs#L105-L135), [crates/gcode/src/index/parser/calls/ast.rs:148-179](crates/gcode/src/index/parser/calls/ast.rs#L148-L179), [crates/gcode/src/index/parser/calls/ast.rs:181-193](crates/gcode/src/index/parser/calls/ast.rs#L181-L193), [crates/gcode/src/index/parser/calls/ast.rs:196-205](crates/gcode/src/index/parser/calls/ast.rs#L196-L205), [crates/gcode/src/index/parser/calls/ast.rs:208-217](crates/gcode/src/index/parser/calls/ast.rs#L208-L217), [crates/gcode/src/index/parser/calls/ast.rs:220-235](crates/gcode/src/index/parser/calls/ast.rs#L220-L235), [crates/gcode/src/index/parser/calls/ast.rs:238-252](crates/gcode/src/index/parser/calls/ast.rs#L238-L252)
- [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55](crates/gcode/src/index/parser/calls/dart_textual.rs#L8-L55), [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77](crates/gcode/src/index/parser/calls/dart_textual.rs#L57-L77), [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168](crates/gcode/src/index/parser/calls/dart_textual.rs#L79-L168), [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172](crates/gcode/src/index/parser/calls/dart_textual.rs#L170-L172), [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189](crates/gcode/src/index/parser/calls/dart_textual.rs#L174-L189), [crates/gcode/src/index/parser/calls/dart_textual.rs:191-216](crates/gcode/src/index/parser/calls/dart_textual.rs#L191-L216), [crates/gcode/src/index/parser/calls/dart_textual.rs:218-223](crates/gcode/src/index/parser/calls/dart_textual.rs#L218-L223), [crates/gcode/src/index/parser/calls/dart_textual.rs:226-232](crates/gcode/src/index/parser/calls/dart_textual.rs#L226-L232), [crates/gcode/src/index/parser/calls/dart_textual.rs:235-237](crates/gcode/src/index/parser/calls/dart_textual.rs#L235-L237), [crates/gcode/src/index/parser/calls/dart_textual.rs:239-243](crates/gcode/src/index/parser/calls/dart_textual.rs#L239-L243), [crates/gcode/src/index/parser/calls/dart_textual.rs:247-252](crates/gcode/src/index/parser/calls/dart_textual.rs#L247-L252), [crates/gcode/src/index/parser/calls/dart_textual.rs:255-259](crates/gcode/src/index/parser/calls/dart_textual.rs#L255-L259), [crates/gcode/src/index/parser/calls/dart_textual.rs:262-362](crates/gcode/src/index/parser/calls/dart_textual.rs#L262-L362), [crates/gcode/src/index/parser/calls/dart_textual.rs:364-366](crates/gcode/src/index/parser/calls/dart_textual.rs#L364-L366), [crates/gcode/src/index/parser/calls/dart_textual.rs:368-370](crates/gcode/src/index/parser/calls/dart_textual.rs#L368-L370), [crates/gcode/src/index/parser/calls/dart_textual.rs:373-375](crates/gcode/src/index/parser/calls/dart_textual.rs#L373-L375), [crates/gcode/src/index/parser/calls/dart_textual.rs:377-379](crates/gcode/src/index/parser/calls/dart_textual.rs#L377-L379), [crates/gcode/src/index/parser/calls/dart_textual.rs:381-391](crates/gcode/src/index/parser/calls/dart_textual.rs#L381-L391), [crates/gcode/src/index/parser/calls/dart_textual.rs:393-417](crates/gcode/src/index/parser/calls/dart_textual.rs#L393-L417), [crates/gcode/src/index/parser/calls/dart_textual.rs:419-441](crates/gcode/src/index/parser/calls/dart_textual.rs#L419-L441), [crates/gcode/src/index/parser/calls/dart_textual.rs:443-492](crates/gcode/src/index/parser/calls/dart_textual.rs#L443-L492)
- [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119](crates/gcode/src/index/parser/calls/objc_ast.rs#L16-L119), [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140](crates/gcode/src/index/parser/calls/objc_ast.rs#L121-L140), [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150](crates/gcode/src/index/parser/calls/objc_ast.rs#L142-L150), [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169](crates/gcode/src/index/parser/calls/objc_ast.rs#L152-L169), [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181](crates/gcode/src/index/parser/calls/objc_ast.rs#L171-L181), [crates/gcode/src/index/parser/calls/objc_ast.rs:183-189](crates/gcode/src/index/parser/calls/objc_ast.rs#L183-L189), [crates/gcode/src/index/parser/calls/objc_ast.rs:191-197](crates/gcode/src/index/parser/calls/objc_ast.rs#L191-L197)
- [crates/gcode/src/index/parser/calls/resolution.rs:6-10](crates/gcode/src/index/parser/calls/resolution.rs#L6-L10), [crates/gcode/src/index/parser/calls/resolution.rs:17-21](crates/gcode/src/index/parser/calls/resolution.rs#L17-L21), [crates/gcode/src/index/parser/calls/resolution.rs:23-46](crates/gcode/src/index/parser/calls/resolution.rs#L23-L46), [crates/gcode/src/index/parser/calls/resolution.rs:48-62](crates/gcode/src/index/parser/calls/resolution.rs#L48-L62), [crates/gcode/src/index/parser/calls/resolution.rs:64-66](crates/gcode/src/index/parser/calls/resolution.rs#L64-L66), [crates/gcode/src/index/parser/calls/resolution.rs:68-96](crates/gcode/src/index/parser/calls/resolution.rs#L68-L96), [crates/gcode/src/index/parser/calls/resolution.rs:98-112](crates/gcode/src/index/parser/calls/resolution.rs#L98-L112), [crates/gcode/src/index/parser/calls/resolution.rs:114-122](crates/gcode/src/index/parser/calls/resolution.rs#L114-L122), [crates/gcode/src/index/parser/calls/resolution.rs:124-145](crates/gcode/src/index/parser/calls/resolution.rs#L124-L145), [crates/gcode/src/index/parser/calls/resolution.rs:147-202](crates/gcode/src/index/parser/calls/resolution.rs#L147-L202), [crates/gcode/src/index/parser/calls/resolution.rs:204-209](crates/gcode/src/index/parser/calls/resolution.rs#L204-L209), [crates/gcode/src/index/parser/calls/resolution.rs:211-222](crates/gcode/src/index/parser/calls/resolution.rs#L211-L222), [crates/gcode/src/index/parser/calls/resolution.rs:224-229](crates/gcode/src/index/parser/calls/resolution.rs#L224-L229), [crates/gcode/src/index/parser/calls/resolution.rs:239-285](crates/gcode/src/index/parser/calls/resolution.rs#L239-L285)
- [crates/gcode/src/index/parser/calls/shadowing.rs:6-23](crates/gcode/src/index/parser/calls/shadowing.rs#L6-L23), [crates/gcode/src/index/parser/calls/shadowing.rs:25-43](crates/gcode/src/index/parser/calls/shadowing.rs#L25-L43), [crates/gcode/src/index/parser/calls/shadowing.rs:45-84](crates/gcode/src/index/parser/calls/shadowing.rs#L45-L84), [crates/gcode/src/index/parser/calls/shadowing.rs:86-96](crates/gcode/src/index/parser/calls/shadowing.rs#L86-L96), [crates/gcode/src/index/parser/calls/shadowing.rs:98-113](crates/gcode/src/index/parser/calls/shadowing.rs#L98-L113), [crates/gcode/src/index/parser/calls/shadowing.rs:115-129](crates/gcode/src/index/parser/calls/shadowing.rs#L115-L129), [crates/gcode/src/index/parser/calls/shadowing.rs:131-153](crates/gcode/src/index/parser/calls/shadowing.rs#L131-L153), [crates/gcode/src/index/parser/calls/shadowing.rs:155-218](crates/gcode/src/index/parser/calls/shadowing.rs#L155-L218), [crates/gcode/src/index/parser/calls/shadowing.rs:220-224](crates/gcode/src/index/parser/calls/shadowing.rs#L220-L224), [crates/gcode/src/index/parser/calls/shadowing.rs:226-235](crates/gcode/src/index/parser/calls/shadowing.rs#L226-L235), [crates/gcode/src/index/parser/calls/shadowing.rs:237-260](crates/gcode/src/index/parser/calls/shadowing.rs#L237-L260), [crates/gcode/src/index/parser/calls/shadowing.rs:262-273](crates/gcode/src/index/parser/calls/shadowing.rs#L262-L273), [crates/gcode/src/index/parser/calls/shadowing.rs:283-299](crates/gcode/src/index/parser/calls/shadowing.rs#L283-L299), [crates/gcode/src/index/parser/calls/shadowing.rs:302-315](crates/gcode/src/index/parser/calls/shadowing.rs#L302-L315), [crates/gcode/src/index/parser/calls/shadowing.rs:318-327](crates/gcode/src/index/parser/calls/shadowing.rs#L318-L327), [crates/gcode/src/index/parser/calls/shadowing.rs:330-339](crates/gcode/src/index/parser/calls/shadowing.rs#L330-L339), [crates/gcode/src/index/parser/calls/shadowing.rs:342-351](crates/gcode/src/index/parser/calls/shadowing.rs#L342-L351), [crates/gcode/src/index/parser/calls/shadowing.rs:354-363](crates/gcode/src/index/parser/calls/shadowing.rs#L354-L363)
- [crates/gcode/src/index/parser/calls/text.rs:4-20](crates/gcode/src/index/parser/calls/text.rs#L4-L20), [crates/gcode/src/index/parser/calls/text.rs:22-30](crates/gcode/src/index/parser/calls/text.rs#L22-L30), [crates/gcode/src/index/parser/calls/text.rs:32-49](crates/gcode/src/index/parser/calls/text.rs#L32-L49), [crates/gcode/src/index/parser/calls/text.rs:51-53](crates/gcode/src/index/parser/calls/text.rs#L51-L53), [crates/gcode/src/index/parser/calls/text.rs:55-57](crates/gcode/src/index/parser/calls/text.rs#L55-L57), [crates/gcode/src/index/parser/calls/text.rs:59-61](crates/gcode/src/index/parser/calls/text.rs#L59-L61), [crates/gcode/src/index/parser/calls/text.rs:63-65](crates/gcode/src/index/parser/calls/text.rs#L63-L65), [crates/gcode/src/index/parser/calls/text.rs:67-153](crates/gcode/src/index/parser/calls/text.rs#L67-L153), [crates/gcode/src/index/parser/calls/text.rs:160-165](crates/gcode/src/index/parser/calls/text.rs#L160-L165), [crates/gcode/src/index/parser/calls/text.rs:168-174](crates/gcode/src/index/parser/calls/text.rs#L168-L174)

</details>

# crates/gcode/src/index/parser/calls

Parent: [[code/modules/crates/gcode/src/index/parser|crates/gcode/src/index/parser]]

## Overview

The crates/gcode/src/index/parser/calls module parses and extracts call relations from source files to construct CallRelation records. For AST-based languages like JavaScript, Elixir, and Objective-C, the module runs Tree-sitter queries to capture caller-callee pairings, handling language-specific cases such as Elixir definition heads and Objective-C receiver qualifiers [crates/gcode/src/index/parser/calls/ast.rs:17-103, crates/gcode/src/index/parser/calls/objc_ast.rs:16-119]. For Dart, it employs a textual line scanner that maintains lightweight state for code, strings, and comments to filter out class or module declarations and identify call-like candidates . This extraction workflow collaborates directly with semantic resolvers like SemanticCallResolver to translate syntactic candidates into fully materialized call entries .

To resolve call targets, the module identifies enclosing symbols and classifies call syntax into Bare, Member, or Other syntax kinds [crates/gcode/src/index/parser/calls/resolution.rs:6-10, crates/gcode/src/index/parser/calls/resolution.rs:17-21, crates/gcode/src/index/parser/calls/resolution.rs:23-46]. Same-file callee resolution matches bare calls against callable symbols and splits qualified calls for namespace-based lookup [crates/gcode/src/index/parser/calls/resolution.rs:48-62]. Correctness is reinforced by a shadowing detection pipeline that inspects the caller's surrounding scope to prevent local bindings or parameters from being mistaken for external calls [crates/gcode/src/index/parser/calls/shadowing.rs:6-23, crates/gcode/src/index/parser/calls/shadowing.rs:25-43, crates/gcode/src/index/parser/calls/shadowing.rs:45-84]. Unicode-aware utilities support this processing by converting offsets, trimming identifiers, and filtering language-specific keywords [crates/gcode/src/index/parser/calls/text.rs:22-30, crates/gcode/src/index/parser/calls/text.rs:32-49, crates/gcode/src/index/parser/calls/text.rs:55-57].

Key Module Symbols:
| Symbol | Kind | Description | Citation |
| --- | --- | --- | --- |
| `extract_ast_calls` | Function | Compiles AST call queries, walks matches, and materializes call records for AST-supported languages. | [crates/gcode/src/index/parser/calls/ast.rs:17-103] |
| `extract_textual_dart_calls` | Function | Scans Dart source line by line using scanner states to filter declarations and extract candidate call relations. |  |
| `CallSyntaxKind` | Enum | Categorizes call syntax into Bare, Member, or Other for resolution classification. | [crates/gcode/src/index/parser/calls/resolution.rs:6-10] |
| `enclosing_symbol` | Function | Identifies the deepest enclosing symbol in the file containing a given byte offset. | [crates/gcode/src/index/parser/calls/resolution.rs:17-21] |
| `call_syntax_kind` | Function | Assesses tree-sitter nodes to classify the call's syntax structure. | [crates/gcode/src/index/parser/calls/resolution.rs:23-46] |
| `resolve_same_file_callee` | Function | Maps a callee and qualifier path to a same-file symbol based on call syntax kind. | [crates/gcode/src/index/parser/calls/resolution.rs:48-62] |
| `external_call_is_shadowed` | Function | Determines if an external call target is shadowed by local parameter names or bindings. | [crates/gcode/src/index/parser/calls/shadowing.rs:6-23] |
| `utf16_column_at_byte` | Function | Calculates the UTF-16 column index at a given byte offset in the source. | [crates/gcode/src/index/parser/calls/text.rs:22-30] |
| `should_ignore_call_name` | Function | Determines if a parsed name should be skipped based on language keywords. | [crates/gcode/src/index/parser/calls/text.rs:55-57] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/parser/calls/ast.rs\|crates/gcode/src/index/parser/calls/ast.rs]] | This file extracts call relations from Tree-sitter AST queries for multiple languages and turns matched call sites into `CallRelation` records. `extract_ast_calls` is the main entry point: it compiles the language’s call query, walks query matches, finds the `name` and optional `call` captures, filters ignored names, handles language-specific special cases like Elixir definition heads, and then materializes each call with qualifier-path and semantic-resolution helpers; the JS-specific helpers and the small test cases exercise capture handling, qualifier splitting, and when bare or qualified names should be treated as member calls. [crates/gcode/src/index/parser/calls/ast.rs:17-103] [crates/gcode/src/index/parser/calls/ast.rs:105-135] [crates/gcode/src/index/parser/calls/ast.rs:148-179] [crates/gcode/src/index/parser/calls/ast.rs:181-193] [crates/gcode/src/index/parser/calls/ast.rs:196-205] |
| [[code/files/crates/gcode/src/index/parser/calls/dart_textual.rs\|crates/gcode/src/index/parser/calls/dart_textual.rs]] | Implements a textual Dart call extractor for the call indexer. It walks the source line by line, maintains lightweight scan state for code, strings, comments, and class-member context, and uses that state to find call-like candidates, filter out declarations and other ignored contexts, and materialize `CallRelation` entries with optional semantic resolution. The helper functions and small state structs work together to support the heuristics: line-span splitting, candidate detection, qualifier and angle-bracket checks, declaration and string-start detection, and per-line scan bookkeeping that suppresses false positives before a call is recorded. [crates/gcode/src/index/parser/calls/dart_textual.rs:8-55] [crates/gcode/src/index/parser/calls/dart_textual.rs:57-77] [crates/gcode/src/index/parser/calls/dart_textual.rs:79-168] [crates/gcode/src/index/parser/calls/dart_textual.rs:170-172] [crates/gcode/src/index/parser/calls/dart_textual.rs:174-189] |
| [[code/files/crates/gcode/src/index/parser/calls/objc_ast.rs\|crates/gcode/src/index/parser/calls/objc_ast.rs]] | Extracts Objective-C call relations from a parsed tree-sitter AST by running the language’s call query, collecting `name`/`call`/`receiver` captures, and turning matched call sites into `CallRelation` records, optionally using a semantic resolver. The helper functions support that extraction by determining message receiver qualifiers, inferring a variable’s Objective-C type from surrounding text or lines, and checking identifier and type-identifier boundaries so call names and receivers are recognized correctly. [crates/gcode/src/index/parser/calls/objc_ast.rs:16-119] [crates/gcode/src/index/parser/calls/objc_ast.rs:121-140] [crates/gcode/src/index/parser/calls/objc_ast.rs:142-150] [crates/gcode/src/index/parser/calls/objc_ast.rs:152-169] [crates/gcode/src/index/parser/calls/objc_ast.rs:171-181] |
| [[code/files/crates/gcode/src/index/parser/calls/resolution.rs\|crates/gcode/src/index/parser/calls/resolution.rs]] | This file resolves call targets within the current file by combining tree-sitter syntax inspection with the file’s indexed symbols. It first classifies a call as `Bare`, `Member`, or `Other` via `CallSyntaxKind`, using `enclosing_symbol` to find the innermost symbol at a byte offset and `call_syntax_kind` plus syntax-kind predicates to detect whether the callee sits in a member-like expression. The resolution helpers then map a callee name and optional qualifier path to a same-file symbol ID: bare calls search for callable symbols by name, member calls try associated/member resolution, and qualified calls are split into root alias and path pieces before lookup. The remaining helpers support this pipeline by identifying unique symbols, extracting qualifier paths, and handling Lua-specific quoted `require` member qualifiers. [crates/gcode/src/index/parser/calls/resolution.rs:6-10] [crates/gcode/src/index/parser/calls/resolution.rs:17-21] [crates/gcode/src/index/parser/calls/resolution.rs:23-46] [crates/gcode/src/index/parser/calls/resolution.rs:48-62] [crates/gcode/src/index/parser/calls/resolution.rs:64-66] |
| [[code/files/crates/gcode/src/index/parser/calls/shadowing.rs\|crates/gcode/src/index/parser/calls/shadowing.rs]] | This file provides shadowing detection for call resolution. `external_call_is_shadowed` chooses the candidate name to test based on call syntax and then delegates to `local_name_in_scope_before_call`, which inspects the caller’s source span before the call site, strips block comments, and checks for either parameter names or local bindings that would shadow the external call. The rest of the helpers break that parsing into small pieces: they remove nested block comments, extract names from parameter and binding forms, split assignments and declarations, and avoid false positives from comments, typed bindings, and compound operators. [crates/gcode/src/index/parser/calls/shadowing.rs:6-23] [crates/gcode/src/index/parser/calls/shadowing.rs:25-43] [crates/gcode/src/index/parser/calls/shadowing.rs:45-84] [crates/gcode/src/index/parser/calls/shadowing.rs:86-96] [crates/gcode/src/index/parser/calls/shadowing.rs:98-113] |
| [[code/files/crates/gcode/src/index/parser/calls/text.rs\|crates/gcode/src/index/parser/calls/text.rs]] | This file provides text and identifier utilities for the call-indexing parser. It converts byte offsets to UTF-16 columns while tolerating invalid UTF-8, measures line terminator length for test support, trims likely identifier tokens, and defines Unicode-aware start/continue checks plus a fast byte-level check for textual call names. The main `should_ignore_call_name` logic ties these helpers together by deciding when a parsed name should be skipped, and the tests confirm it ignores language keywords that resemble calls and accepts Unicode XID identifier characters. [crates/gcode/src/index/parser/calls/text.rs:4-20] [crates/gcode/src/index/parser/calls/text.rs:22-30] [crates/gcode/src/index/parser/calls/text.rs:32-49] [crates/gcode/src/index/parser/calls/text.rs:51-53] [crates/gcode/src/index/parser/calls/text.rs:55-57] |

## Components

| Component ID |
| --- |
| `bcaf8341-d7e2-526b-af67-326be6b04220` |
| `586efd45-7dd8-5f7d-ade3-f785c9d9d9c8` |
| `425ba4ef-1a13-5762-bac0-07e57d1d2709` |
| `4560361a-df66-5092-969a-7592746703a4` |
| `9e398a6c-c654-5983-a963-06daa7a9169c` |
| `2146e6ac-ac69-5c87-8f97-04c4fb67ed5c` |
| `79b25384-0aab-5efe-b355-3dd11e8de21a` |
| `aa7ddaad-72e7-5d12-a15e-7b8996db3fe8` |
| `e61b2a21-72d5-5d34-8e75-b367e3ad76ba` |
| `2738a422-f288-534e-a366-5e9e46974efe` |
| `3159fb65-0a43-5df8-b392-1bc39ff422a6` |
| `044945e8-53b2-5a84-abe4-a18304877a11` |
| `75250a72-74e8-5862-ad9b-51b8a6da1a65` |
| `647ac655-f5a8-5f0d-a60f-33c8ea2c9ce2` |
| `18b2b0c1-9d75-540c-945d-d4927534fe86` |
| `a0546f1a-f17f-57c6-b2ff-422ba208d0c1` |
| `1f8978c2-802f-5f74-bade-eb9b8c282f14` |
| `c1a66187-3bcc-5091-b205-1883d9e3935b` |
| `c94c5b27-366d-50be-b9e8-f8f2e7af1dc8` |
| `826e8df3-be70-5ac4-ada1-55a31359f6ff` |
| `f3fb79da-43d4-545c-b031-131b84dca8a2` |
| `ddf1d64c-873e-530c-8e50-7993d3724101` |
| `8a1a9ca2-9049-55c1-b8f6-bc61d1c51cab` |
| `c3e16433-934e-5dfc-a56a-f42893a6a5b1` |
| `dcc92820-a198-56bc-bbad-0abad5c21c36` |
| `3efdcaae-3db8-5670-b839-7d379eb7a396` |
| `c99e04de-c6b8-5a5a-90af-0d60d1bc23f3` |
| `0467e7e4-5fdd-570e-9d33-c53d9783c68f` |
| `9ed7304a-528a-586b-adb5-856d6b59e102` |
| `bfd38d24-7867-52b9-9937-c35acd474a4d` |
| `67ee4404-02e3-5c9a-aa55-0afb3133d10e` |
| `85b0a29d-b63e-50f4-ab41-458f8661945e` |
| `48c54247-5677-5c3d-9359-2637cc182fd9` |
| `1f92b56e-539a-53bb-8cbc-db53d0bc474a` |
| `a61fb040-84db-50dc-93b0-0f2c69b8a936` |
| `d302155e-627e-5b31-bf5d-2751242abbd2` |
| `05532d20-0797-5f98-b19e-15a7f431a888` |
| `9c30b856-c855-5c26-aa73-bdd164c437a1` |
| `53222c78-5e39-5e45-a035-c9b48740a4d6` |
| `6eca919c-11ec-5425-a720-90a47399bf04` |
| `2aa8732c-83b8-518b-b0a5-843da210d4b7` |
| `f596569d-20cc-55b0-94fc-08854f353fac` |
| `46568845-3c46-5115-ae60-d4d46c3a1e10` |
| `1c703af1-47ef-5303-88a2-e47e55a8cb8b` |
| `fdba7de9-f10d-58be-96c6-0d80689eecbf` |
| `ab9858ab-0b86-5a51-ab49-596b31f73e44` |
| `b2822686-5f91-5b6f-bd1c-5864535c80e3` |
| `1e7faef2-7c39-5488-a964-e922ebf42bdb` |
| `2d7d0f18-dae7-5ea0-9ba1-98eb48cfb3c3` |
| `e962f81d-c93c-5637-9fa7-a95893a9f737` |
| `f711cf40-36c2-52cf-a202-bec5a2006631` |
| `b0d1f2d1-32c5-5ede-87e1-ac1a74ee89e9` |
| `91f1f774-696c-59ea-a440-ebfe9a240361` |
| `27126f44-582f-5846-bbb3-35f882af0451` |
| `9a912ba2-7c9e-56b2-8ec3-a010eabb16c0` |
| `d2baba53-3b1c-5882-ac45-347bb590c86c` |
| `f415fafa-d665-539d-a4b7-afc5cc430827` |
| `cf48944d-8b8e-5118-af00-bdfbe3bcfd31` |
| `c4cf63f5-441f-58dc-bb8d-ce325f3b1102` |
| `5c036c95-a10b-5266-bb92-093fffd8426f` |
| `1918300f-65c6-5a07-afb9-d4f94583c372` |
| `e2847a7f-7c36-5a77-a2e2-4ba041ba4fd9` |
| `ec04f0a0-efd8-52c8-a5c3-599458fe9acf` |
| `b17f0d6c-1293-5411-b64d-0d647a9e93db` |
| `a4ea9e5c-1e62-5126-8f32-c7c46b895e78` |
| `06cdea89-74a0-5cb1-b281-6ff2abd3ab95` |
| `5cb38be7-7a0b-55f3-a86e-19cfbc4a490b` |
| `80f0837f-99ac-5448-8675-89e6bf304849` |
| `fdf5bec9-0f92-580b-ad2e-d55c1b4ab60c` |
| `3b863457-e36d-5dad-a9b0-be2a70dadf05` |
| `e8df33ef-7361-5e81-9601-63ebdf33a38f` |
| `c03b08bd-256c-5124-9ad7-47206d4ca21c` |
| `761af537-d29e-5635-af22-70470219838a` |
| `d84b1f89-9474-5ae0-b6eb-11f06485d78b` |
| `73d66dcf-5b03-5775-be09-6972894fa9a9` |
| `7c1d719b-94ea-51f9-a0d0-a3e8634e8930` |
| `1f52b771-0c46-5d29-b23d-58bc710bc9ff` |
| `b5b569d3-26b9-53fc-980a-b47765407913` |
