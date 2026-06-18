---
title: crates/gcode/src/index/import_resolution/predicates.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/predicates.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/predicates.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/predicates.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/predicates.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `is_external_python_module` | function | Returns 'true' for a non-relative Python module name that does not match any local module in the import context, including exact matches or either module being a dotted prefix of the other. [crates/gcode/src/index/import_resolution/predicates.rs:8-21] |
| `is_external_js_module` | function | Returns 'true' for JavaScript imports that are Node built-ins or package specifiers treated as external, and 'false' for relative/absolute/path aliases, self-package imports, or specifiers that cannot be resolved to an external package name. [crates/gcode/src/index/import_resolution/predicates.rs:23-53] |
| `is_external_go_module` | function | Returns 'false' for relative imports and for modules equal to or nested under the current Go module path from 'import_context', and 'true' otherwise, indicating the module is external. [crates/gcode/src/index/import_resolution/predicates.rs:55-68] |
| `rust_external_roots` | function | Returns the set of Rust external root crate names by cloning 'import_context.rust_external_crates', adding all standard Rust crate names, and removing the current crate name if 'rust_self_crate_name' is set. [crates/gcode/src/index/import_resolution/predicates.rs:70-77] |
| `java_declared_types` | function | Returns the list of declared type names found in the given Java source text by scanning for 'class', 'interface', 'enum', and 'record' declarations. [crates/gcode/src/index/import_resolution/predicates.rs:79-81] |
| `csharp_declared_types` | function | Returns the list of declared C# type names in 'contents' by delegating to 'declared_types' with the keywords 'class', 'interface', 'enum', 'record', and 'struct'. [crates/gcode/src/index/import_resolution/predicates.rs:83-88] |
| `declared_types` | function | Returns the identifiers immediately following any token in 'keywords' after stripping comments and string literals, by tokenizing on non-alphanumeric/underscore characters and collecting each matching second token into a 'Vec<String>'. [crates/gcode/src/index/import_resolution/predicates.rs:94-107] |
| `strip_comments_and_string_literals` | function | Returns a same-length copy of 'contents' with '//' line comments, '/* ... */' block comments, and quoted string/character literals replaced by spaces while preserving newline characters and line structure. [crates/gcode/src/index/import_resolution/predicates.rs:109-179] |
| `php_declared_symbols` | function | Returns the names of PHP classes, interfaces, traits, enums, and functions declared in the input by stripping comments and string literals, tokenizing on non-identifier characters, and collecting the token immediately following each matching declaration keyword. [crates/gcode/src/index/import_resolution/predicates.rs:185-201] |
| `is_external_java_class` | function | Returns 'true' only when every non-empty Java class-name candidate derived from 'class_path' is absent from 'import_context.java_local_classes', indicating the class is not locally defined. [crates/gcode/src/index/import_resolution/predicates.rs:203-210] |
| `java_class_name_candidates` | function | Returns an iterator over three candidate Java class names derived from 'class_path': the original string, the substring after the last '.', and the substring after the last '$' in that dotted segment. [crates/gcode/src/index/import_resolution/predicates.rs:212-220] |
| `is_external_csharp_path` | function | Returns 'true' when the path, after optionally removing a leading 'global::', has a first dotted segment that is not present in 'import_context.csharp_local_roots', indicating the C# path is external. [crates/gcode/src/index/import_resolution/predicates.rs:222-231] |
| `is_external_php_symbol` | function | Returns 'true' when the given PHP symbol path is not present in the import context’s local-symbol set, either by its full lowercased path or by its final '\'-separated name, making the lookup case-insensitive and conservative about external symbols. [crates/gcode/src/index/import_resolution/predicates.rs:233-241] |
| `is_external_rust_root` | function | Returns 'true' when 'root' names an importable external Rust crate, excluding the built-in module roots 'crate', 'self', 'super', and the current crate name from 'import_context', and otherwise checking membership in 'rust_external_crates' or 'STANDARD_RUST_CRATES'. [crates/gcode/src/index/import_resolution/predicates.rs:243-251] |
| `ruby_require_root` | function | Returns the static string slice for a bundled Ruby require root matching 'required', or 'None' if no mapping exists. [crates/gcode/src/index/import_resolution/predicates.rs:258-262] |
| `is_external_dart_uri` | function | Returns 'true' when 'uri' is a 'dart:' URI or a 'package:' URI whose package name is listed in 'import_context.dart_external_packages' and is not the current self package, otherwise returns 'false'. [crates/gcode/src/index/import_resolution/predicates.rs:264-276] |
| `elixir_dependency_roots` | function | Returns the bundled dependency-root list for the given Elixir dependency name by looking it up in a map and converting the stored 'Vec<String>' to an '&'static [String]', or 'None' if absent. [crates/gcode/src/index/import_resolution/predicates.rs:284-288] |
| `bundled_ruby_require_roots` | function | Returns a lazily initialized, process-wide 'HashMap<String, String>' by parsing the bundled 'ruby_require_roots.json' asset once with 'serde_json' and caching it in a 'OnceLock'. [crates/gcode/src/index/import_resolution/predicates.rs:290-302] |
| `bundled_elixir_dependency_roots` | function | Returns a lazily initialized global 'HashMap<String, Vec<String>>' by parsing the bundled 'elixir_dependency_roots.json' asset once and caching it in a 'OnceLock'. [crates/gcode/src/index/import_resolution/predicates.rs:304-316] |
| `js_package_name` | function | Returns the JavaScript package name prefix from a module specifier, yielding '@scope/package' for scoped imports by slicing through the second path segment and otherwise returning the first '/'-delimited segment. [crates/gcode/src/index/import_resolution/predicates.rs:318-328] |

