---
title: crates/gcode/src/index/import_resolution/parser
type: code_module
provenance:
- file: crates/gcode/src/index/import_resolution/parser/go_rust.rs
  ranges:
  - 12-40
  - 42-96
  - 98-125
  - 127-162
  - 164-229
  - 236-247
  - 250-260
- file: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
  ranges:
  - 9-91
  - 93-169
  - 171-173
  - 175-188
- file: crates/gcode/src/index/import_resolution/parser/lua.rs
  ranges:
  - 6-44
  - 46-68
  - 70-85
  - 87-111
  - 113-128
  - 130-137
- file: crates/gcode/src/index/import_resolution/parser/mod.rs
  ranges:
  - 40-69
  - 71-89
  - 91-141
  - 143-218
  - 220-233
  - 235-254
  - 265-291
  - 302-323
  - 334-351
  - 360-384
  - 402-439
  - 441-453
  - 469-507
- file: crates/gcode/src/index/import_resolution/parser/objc.rs
  ranges:
  - 8-69
  - 71-85
  - 87-95
- file: crates/gcode/src/index/import_resolution/parser/php_kotlin.rs
  ranges:
  - 9-16
  - 18-61
  - 64-68
  - 70-136
  - 138-189
  - 199-226
  - 228-247
  - 249-262
  - 264-270
  - 272-292
- file: crates/gcode/src/index/import_resolution/parser/python_js.rs
  ranges:
  - 14-123
  - 125-155
  - 157-252
  - 254-319
- file: crates/gcode/src/index/import_resolution/parser/rest.rs
  ranges:
  - 10-54
  - 56-92
  - 94-152
  - 154-233
- file: crates/gcode/src/index/import_resolution/parser/scala.rs
  ranges:
  - 6-23
  - 25-57
  - 59-103
  - 105-112
  - 114-131
  - 133-145
  - 147-155
- file: crates/gcode/src/index/import_resolution/parser/shell.rs
  ranges:
  - 8-40
  - 42-57
  - 59-78
  - 80-96
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L12-L40), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L42-L96), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L98-L125), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L127-L162), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L164-L229), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:236-247](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L236-L247), [crates/gcode/src/index/import_resolution/parser/go_rust.rs:250-260](crates/gcode/src/index/import_resolution/parser/go_rust.rs#L250-L260)
- [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L9-L91), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L93-L169), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L171-L173), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L175-L188)
- [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44](crates/gcode/src/index/import_resolution/parser/lua.rs#L6-L44), [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68](crates/gcode/src/index/import_resolution/parser/lua.rs#L46-L68), [crates/gcode/src/index/import_resolution/parser/lua.rs:70-85](crates/gcode/src/index/import_resolution/parser/lua.rs#L70-L85), [crates/gcode/src/index/import_resolution/parser/lua.rs:87-111](crates/gcode/src/index/import_resolution/parser/lua.rs#L87-L111), [crates/gcode/src/index/import_resolution/parser/lua.rs:113-128](crates/gcode/src/index/import_resolution/parser/lua.rs#L113-L128), [crates/gcode/src/index/import_resolution/parser/lua.rs:130-137](crates/gcode/src/index/import_resolution/parser/lua.rs#L130-L137)
- [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69](crates/gcode/src/index/import_resolution/parser/mod.rs#L40-L69), [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89](crates/gcode/src/index/import_resolution/parser/mod.rs#L71-L89), [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141](crates/gcode/src/index/import_resolution/parser/mod.rs#L91-L141), [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218](crates/gcode/src/index/import_resolution/parser/mod.rs#L143-L218), [crates/gcode/src/index/import_resolution/parser/mod.rs:220-233](crates/gcode/src/index/import_resolution/parser/mod.rs#L220-L233), [crates/gcode/src/index/import_resolution/parser/mod.rs:235-254](crates/gcode/src/index/import_resolution/parser/mod.rs#L235-L254), [crates/gcode/src/index/import_resolution/parser/mod.rs:265-291](crates/gcode/src/index/import_resolution/parser/mod.rs#L265-L291), [crates/gcode/src/index/import_resolution/parser/mod.rs:302-323](crates/gcode/src/index/import_resolution/parser/mod.rs#L302-L323), [crates/gcode/src/index/import_resolution/parser/mod.rs:334-351](crates/gcode/src/index/import_resolution/parser/mod.rs#L334-L351), [crates/gcode/src/index/import_resolution/parser/mod.rs:360-384](crates/gcode/src/index/import_resolution/parser/mod.rs#L360-L384), [crates/gcode/src/index/import_resolution/parser/mod.rs:402-439](crates/gcode/src/index/import_resolution/parser/mod.rs#L402-L439), [crates/gcode/src/index/import_resolution/parser/mod.rs:441-453](crates/gcode/src/index/import_resolution/parser/mod.rs#L441-L453), [crates/gcode/src/index/import_resolution/parser/mod.rs:469-507](crates/gcode/src/index/import_resolution/parser/mod.rs#L469-L507)
- [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69](crates/gcode/src/index/import_resolution/parser/objc.rs#L8-L69), [crates/gcode/src/index/import_resolution/parser/objc.rs:71-85](crates/gcode/src/index/import_resolution/parser/objc.rs#L71-L85), [crates/gcode/src/index/import_resolution/parser/objc.rs:87-95](crates/gcode/src/index/import_resolution/parser/objc.rs#L87-L95)
- [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L9-L16), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L18-L61), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L64-L68), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L70-L136), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L138-L189), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:199-226](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L199-L226), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:228-247](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L228-L247), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:249-262](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L249-L262), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:264-270](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L264-L270), [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:272-292](crates/gcode/src/index/import_resolution/parser/php_kotlin.rs#L272-L292)
- [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123](crates/gcode/src/index/import_resolution/parser/python_js.rs#L14-L123), [crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155](crates/gcode/src/index/import_resolution/parser/python_js.rs#L125-L155), [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252](crates/gcode/src/index/import_resolution/parser/python_js.rs#L157-L252), [crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319](crates/gcode/src/index/import_resolution/parser/python_js.rs#L254-L319)
- [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54](crates/gcode/src/index/import_resolution/parser/rest.rs#L10-L54), [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92](crates/gcode/src/index/import_resolution/parser/rest.rs#L56-L92), [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152](crates/gcode/src/index/import_resolution/parser/rest.rs#L94-L152), [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233](crates/gcode/src/index/import_resolution/parser/rest.rs#L154-L233)
- [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23](crates/gcode/src/index/import_resolution/parser/scala.rs#L6-L23), [crates/gcode/src/index/import_resolution/parser/scala.rs:25-57](crates/gcode/src/index/import_resolution/parser/scala.rs#L25-L57), [crates/gcode/src/index/import_resolution/parser/scala.rs:59-103](crates/gcode/src/index/import_resolution/parser/scala.rs#L59-L103), [crates/gcode/src/index/import_resolution/parser/scala.rs:105-112](crates/gcode/src/index/import_resolution/parser/scala.rs#L105-L112), [crates/gcode/src/index/import_resolution/parser/scala.rs:114-131](crates/gcode/src/index/import_resolution/parser/scala.rs#L114-L131), [crates/gcode/src/index/import_resolution/parser/scala.rs:133-145](crates/gcode/src/index/import_resolution/parser/scala.rs#L133-L145), [crates/gcode/src/index/import_resolution/parser/scala.rs:147-155](crates/gcode/src/index/import_resolution/parser/scala.rs#L147-L155)
- [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40](crates/gcode/src/index/import_resolution/parser/shell.rs#L8-L40), [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57](crates/gcode/src/index/import_resolution/parser/shell.rs#L42-L57), [crates/gcode/src/index/import_resolution/parser/shell.rs:59-78](crates/gcode/src/index/import_resolution/parser/shell.rs#L59-L78), [crates/gcode/src/index/import_resolution/parser/shell.rs:80-96](crates/gcode/src/index/import_resolution/parser/shell.rs#L80-L96)

</details>

# crates/gcode/src/index/import_resolution/parser

Parent: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

The `crates/gcode/src/index/import_resolution/parser` module is responsible for parsing language-specific import statements, mapping import paths to raw import relations, and establishing symbol bindings for downstream call resolution [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69]. The primary entry point, `parse_import_statement`, acts as a dispatcher that routes indexed source files to their respective language parser [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69]. Language-specific sub-parsers normalize imports and register aliases, wildcards, and external/local bindings into `ExtractedImports` across Python, JavaScript, Go, Rust, Java, C#, PHP, Kotlin, Scala, Lua, Objective-C, Shell, Swift, Ruby, Dart, and Elixir [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40, crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91, crates/gcode/src/index/import_resolution/parser/scala.rs:6-23].

To perform resolution, the parser collaborates with the `ImportResolutionContext` to inspect package topologies, query local declarations, and filter out system or external bindings [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69, crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16]. Initial state is compiled by `seed_import_bindings`, which bridges raw import relations and context-derived metadata [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141]. These bindings are then consumed by language-specific callee-resolution helpers—such as those for Lua, Objective-C, and Shell—to map call sites and member accesses back to their imported target files or local namespace symbols [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218, crates/gcode/src/index/import_resolution/parser/lua.rs:46-68, crates/gcode/src/index/import_resolution/parser/shell.rs:42-57].

### Key API Symbols

| Symbol | Responsibility | Target Language / Context | Reference |
| --- | --- | --- | --- |
| parse_import_statement | Main dispatcher that routes source lines to language sub-parsers | Multi-language router | [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69] |
| seed_import_bindings | Populates initial binding map from extracted imports and context | General resolution binder | [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141] |
| push_unparsed_import | Records import statements that could not be fully interpreted | General parser fallback | [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89] |
| parse_go_import_statement | Parses Go quoted module paths, block imports, and local package aliases | Go | [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] |
| parse_rust_import_statement | Parses Rust grouped and nested `use` statements | Rust | [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125] |
| parse_java_import_statement | Extracts Java static, wildcard, and standard class imports | Java | [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91] |
| parse_csharp_import_statement | Parses C# `using` directives, including global alias normalization | C# | [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169] |
| parse_python_import_statement | Extracts Python standard and `from ... import ...` clauses | Python | [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123] |
| parse_js_import_statement | Parses JS/TS named, default, and namespace imports | JavaScript / TypeScript | [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252] |
| parse_php_import_statement | Parses PHP standard, grouped, and comma-separated `use` forms | PHP | [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61] |
| parse_kotlin_import_statement | Extracts Kotlin imports, including custom aliases and wildcards | Kotlin | [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136] |
| parse_scala_import_statement | Extracts Scala imports, expanding selectors and wildcards | Scala | [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23] |
| parse_lua_import_statement | Parses Lua `require` statements and local module bindings | Lua | [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44] |
| parse_objc_import_statement | Identifies Objective-C `#import` and `#include` system/local paths | Objective-C | [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69] |
| parse_shell_import_statement | Resolves relative file targets in shell `source` and `.` lines | Shell | [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40] |
| parse_swift_import_statement | Normalizes and extracts Swift module imports | Swift | [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54] |
| parse_ruby_import_statement | Extracts Ruby require and load targets | Ruby | [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92] |
| parse_dart_import_statement | Parses Dart module and file imports | Dart | [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152] |
| parse_elixir_import_statement | Parses Elixir import and alias directives | Elixir | [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233] |
| resolve_lua_require_member_callee | Maps member-style call targets back to resolved modules | Lua | [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68] |
| resolve_objc_local_callee | Decides whether a bare call maps to an imported local declaration | Objective-C | [crates/gcode/src/index/import_resolution/parser/objc.rs:71-85] |
| resolve_shell_local_callee | Resolves bare functions to sourced script files | Shell | [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/import_resolution/parser/go_rust.rs\|crates/gcode/src/index/import_resolution/parser/go_rust.rs]] | Parses Go and Rust import syntax for the import-resolution indexer. `parse_go_import_statement` and `parse_go_import_spec` extract quoted module paths from single or grouped Go imports, record each import relation, and, when applicable, register local aliases or external bindings while skipping blank and dot imports. `parse_rust_import_statement`, `register_rust_group_imports`, and `register_rust_path_import` do the same for Rust `use` statements, handling grouped imports, path imports, and external-root binding resolution. The two tests confirm that ordinary Go or Rust statements that are not imports do not create raw import records. [crates/gcode/src/index/import_resolution/parser/go_rust.rs:12-40] [crates/gcode/src/index/import_resolution/parser/go_rust.rs:42-96] [crates/gcode/src/index/import_resolution/parser/go_rust.rs:98-125] [crates/gcode/src/index/import_resolution/parser/go_rust.rs:127-162] [crates/gcode/src/index/import_resolution/parser/go_rust.rs:164-229] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/java_csharp.rs\|crates/gcode/src/index/import_resolution/parser/java_csharp.rs]] | Parses Java and C# import statements into the import-resolution index, recording each import relation and building the bindings used later to resolve bare calls, member access, and namespace aliases. The Java parser handles static imports, wildcard imports, external-class detection, and local class/file candidates; the C# parser does the same for `using` directives, including global alias normalization and splitting qualified names so external and local imports are bound consistently. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91] [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169] [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173] [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/lua.rs\|crates/gcode/src/index/import_resolution/parser/lua.rs]] | This file extracts Lua import relationships and callable bindings from source text. `parse_lua_import_statement` normalizes a statement, finds `require` and its quoted module path, records the import, and, when it sees a valid `local` assignment, binds either the whole required module or a specific member to matching module files; `resolve_lua_require_member_callee` performs the same module lookup for member-style calls on `require(...)`, while the helper functions parse assignment structure, locate text after the first quoted string, detect member access after `require`, and validate Lua identifiers. [crates/gcode/src/index/import_resolution/parser/lua.rs:6-44] [crates/gcode/src/index/import_resolution/parser/lua.rs:46-68] [crates/gcode/src/index/import_resolution/parser/lua.rs:70-85] [crates/gcode/src/index/import_resolution/parser/lua.rs:87-111] [crates/gcode/src/index/import_resolution/parser/lua.rs:113-128] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/mod.rs\|crates/gcode/src/index/import_resolution/parser/mod.rs]] | This module is the import-resolution parser for indexed source files. `parse_import_statement` dispatches by language to the appropriate language-specific import parser, while `push_unparsed_import` records imports that could not be fully interpreted. `seed_import_bindings` builds the initial binding state from extracted imports and context, and the various `resolve_*_callee` helpers then map call sites to imported targets or local symbols across languages like Ruby, PHP, Swift, Dart, Elixir, Rust, and C#. [crates/gcode/src/index/import_resolution/parser/mod.rs:40-69] [crates/gcode/src/index/import_resolution/parser/mod.rs:71-89] [crates/gcode/src/index/import_resolution/parser/mod.rs:91-141] [crates/gcode/src/index/import_resolution/parser/mod.rs:143-218] [crates/gcode/src/index/import_resolution/parser/mod.rs:220-233] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/objc.rs\|crates/gcode/src/index/import_resolution/parser/objc.rs]] | This file parses Objective-C `#import` and `#include` statements for import resolution. `parse_objc_import_statement` identifies import lines, extracts the import path and whether it is a system import, records the import relation, and for non-system imports asks the import context for candidate files so it can populate Objective-C import-file bindings plus function and type lookup bindings, then deduplicates them. `resolve_objc_local_callee` uses those bindings together with the current symbol set to decide whether a bare call should be resolved to an imported local Objective-C declaration. `objc_import_path` is the small parser that extracts the path and import kind from the directive text. [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69] [crates/gcode/src/index/import_resolution/parser/objc.rs:71-85] [crates/gcode/src/index/import_resolution/parser/objc.rs:87-95] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/php_kotlin.rs\|crates/gcode/src/index/import_resolution/parser/php_kotlin.rs]] | Parses PHP and Kotlin import statements for import resolution, normalizing each statement and turning it into `ExtractedImports` entries in the current `ImportResolutionContext`. The PHP side handles local-symbol checks, import kind detection, grouped and comma-separated `use` forms, wildcard/module derivation, and registration of class, function, and const imports; the Kotlin side does the same for `import` syntax, including alias and wildcard handling. Helper functions split and join PHP `use` paths, seed local PHP imports, and register either specific imports or wildcard/module bindings so downstream resolution can match local and external symbols consistently. [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:9-16] [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:18-61] [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:64-68] [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:70-136] [crates/gcode/src/index/import_resolution/parser/php_kotlin.rs:138-189] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/python_js.rs\|crates/gcode/src/index/import_resolution/parser/python_js.rs]] | This file parses import statements for both Python and JavaScript and records them as `ImportRelation`s plus any derived bindings in `ExtractedImports`. `parse_python_import_statement` handles Python `import ...` and `from ... import ...` forms, splitting multiple entries, filtering malformed cases, and using `python_local_module_lookup` to decide when a Python import should resolve to a local module versus an external one. `parse_js_import_statement` does the same for JavaScript imports, delegating clause-specific work to `parse_js_local_import_clause` to extract local bindings from named, default, and namespace-style import clauses. Together, these helpers normalize import syntax into the index’s import graph and binding map, while falling back to unparsed handling for statements that do not match the expected patterns. [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123] [crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155] [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252] [crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/rest.rs\|crates/gcode/src/index/import_resolution/parser/rest.rs]] | Parses import-like statements for several languages and records them as `ImportRelation` entries, while also resolving external root bindings when the import can be mapped to a non-local module. The four parsers handle language-specific syntax for Swift, Ruby, Dart, and Elixir, but share the same pattern: normalize the line, extract the module or quoted target, push the import into `ExtractedImports`, and consult `ImportResolutionContext` plus helper predicates/functions to decide whether to register an external root or alias information. [crates/gcode/src/index/import_resolution/parser/rest.rs:10-54] [crates/gcode/src/index/import_resolution/parser/rest.rs:56-92] [crates/gcode/src/index/import_resolution/parser/rest.rs:94-152] [crates/gcode/src/index/import_resolution/parser/rest.rs:154-233] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/scala.rs\|crates/gcode/src/index/import_resolution/parser/scala.rs]] | This file parses Scala `import` statements and records the resolved import relations. `parse_scala_import_statement` normalizes a statement, strips the `import` keyword, splits comma-separated top-level items, and forwards each one for handling. `register_scala_import_or_group` recursively expands grouped imports like brace selections, handles wildcard module imports, or delegates to `register_scala_import_item` for ordinary imports. `register_scala_import_item` splits aliases, stores the target import, and uses the import context to resolve package-qualified names and local bindings for aliasing. The remaining helpers support that flow by splitting grouped selectors, joining nested import paths, recognizing wildcard modules, and separating aliases from targets. [crates/gcode/src/index/import_resolution/parser/scala.rs:6-23] [crates/gcode/src/index/import_resolution/parser/scala.rs:25-57] [crates/gcode/src/index/import_resolution/parser/scala.rs:59-103] [crates/gcode/src/index/import_resolution/parser/scala.rs:105-112] [crates/gcode/src/index/import_resolution/parser/scala.rs:114-131] |
| [[code/files/crates/gcode/src/index/import_resolution/parser/shell.rs\|crates/gcode/src/index/import_resolution/parser/shell.rs]] | This file handles shell import detection and shell-local call resolution for import indexing. `parse_shell_import_statement` normalizes a line of shell text, recognizes `source` and `.` statements, extracts the referenced path, records an `ImportRelation`, and, when the target is a safe relative path, adds the resolved file to `shell_source_files`. `resolve_shell_local_callee` then uses those sourced files to build a `LocalCallBinding` for bare calls only when no existing symbol in the file already matches the callee name. The helper `shell_source_target` filters out absolute, interpolated, or otherwise dynamic paths and resolves safe relative paths against the importing file, while `normalize_project_path` canonicalizes the resulting project path form. [crates/gcode/src/index/import_resolution/parser/shell.rs:8-40] [crates/gcode/src/index/import_resolution/parser/shell.rs:42-57] [crates/gcode/src/index/import_resolution/parser/shell.rs:59-78] [crates/gcode/src/index/import_resolution/parser/shell.rs:80-96] |

## Components

| Component ID |
| --- |
| `09b2efc9-1277-55d5-bcd5-177f6318698b` |
| `4f70d13c-23e0-5f16-a6c6-69ce69537432` |
| `9c57e3f5-8a2a-5fa3-a1a7-baf71c849708` |
| `b9f7233b-7a03-51ab-887d-6c70c7d6c327` |
| `4f47792a-3f24-5996-ad3e-8f5e2fd5e681` |
| `c131ab9b-ef95-501b-b4a9-618083b0fd0e` |
| `09c34044-9a13-5a41-acce-165cca2751eb` |
| `d77e8007-6ca0-51db-9118-2850c570d7e6` |
| `69b9be96-05ec-5a63-924a-b6d650a9e909` |
| `0887984d-837e-5b06-ad36-0a8ec474f36a` |
| `18f18117-8092-562d-867d-6d56874eb1a8` |
| `3e1957e4-ed67-566b-bcbe-eaa6451a06c8` |
| `38a34874-ccac-532b-ad3a-d5197d39f2e5` |
| `1bcda28c-5e7e-58ca-b1da-ea2f099d0795` |
| `33339e4a-3cb4-55b1-968a-c5528dcc91e6` |
| `1ee7d248-f3a4-52e5-b0bc-40bd5e06ca75` |
| `64ed031c-38d0-5f4c-92aa-4c877fb6cf37` |
| `9d0855cb-3d92-571d-83b9-a1ad069e87e6` |
| `11ca3348-1d6a-5111-8f72-a5aeaa606614` |
| `82839e7b-dca9-57a5-a62b-6014b02782d8` |
| `830a7161-e44c-5286-9282-4efe3ec9137a` |
| `fa6161a5-bd8c-5e90-83c9-f3ec61f9ba92` |
| `4288d21a-f368-5308-9fc5-3cd40b8bf5b9` |
| `afb86bf9-eac2-5548-ad9f-b7e686b9fe64` |
| `2253dff6-aefd-5b3c-8e1b-8af0871c1a1a` |
| `5b715a52-6ec5-5290-9277-c9c020e34f3f` |
| `2bff1cb0-961b-54f2-bf2f-986941f45406` |
| `07bf3cce-3e07-5d73-9a9a-06455b9fc8a2` |
| `d36a5bac-400a-508f-9beb-30b2304de6c2` |
| `292df235-702b-5f7a-98ee-e3702e20a962` |
| `14dccfb5-4820-5c32-9ea6-8059e9fe8b97` |
| `457f1187-702e-5f4e-8474-9b55fd09533a` |
| `a42e632d-2288-5577-b4a9-99897008b77b` |
| `7bcb73e7-eaed-59fb-8374-236c08833d88` |
| `0225aeb4-7bb6-5b85-b952-55e351e25a18` |
| `ebe68bb0-90a5-5c94-8f98-745d79c0a81c` |
| `54027118-15a2-5aa6-9613-0fc66b68c61b` |
| `39ad1c9e-b8b5-587e-8581-92eee1187170` |
| `fbb0efc4-f84e-5b91-b868-80d1c252d06a` |
| `4f4a5f16-d7ff-50ec-bf39-e1229f684afd` |
| `15993d02-9907-5488-b5c0-b52c31fd986f` |
| `5a9aa418-d366-5ca3-b7fb-f170aad815e8` |
| `f5470716-fd61-586e-9f39-adeecc5033a5` |
| `83e93bc0-a2e3-5842-a6c3-96a01264515d` |
| `6f46dc14-ac5c-594b-a514-9869a5835a6f` |
| `4fb31e49-91a9-5bac-967a-1e535de427b6` |
| `52ab03a3-ed8c-562a-b77e-bec3aa0aa4f8` |
| `e43548a5-2a3b-51ca-a297-cf5686b2dc57` |
| `bdf2899e-c0cb-53d5-9e06-78efe985bb44` |
| `b7b78884-8762-5fa4-87ba-b83d91ca6c80` |
| `50be796b-ea81-528d-8c6c-9654adee1305` |
| `7d3ce58b-953a-55ef-a126-e90d034de42d` |
| `d7996606-16e0-51a9-a896-dce9a2dbd8c0` |
| `397541f1-a3d9-5684-be7e-9530a0d25b80` |
| `e0a8bab6-ca9e-5581-9afb-9657861db1e2` |
| `82cf3f94-1763-5110-9395-2c7ecf3c48f5` |
| `b6c03a59-0604-55b5-b214-1f438fd0ae27` |
| `30661c80-e80c-55e5-9670-3eb7956be103` |
| `00447dc2-bfc5-5aa9-bc0e-11a47087513d` |
| `2fc09547-bb5d-5ce6-b830-e6262a5eb599` |
| `f3d5fddd-d9a7-5917-9fd0-c7b03fdc3961` |
| `66aaedd2-8099-54da-b607-d9c86b9928ee` |
