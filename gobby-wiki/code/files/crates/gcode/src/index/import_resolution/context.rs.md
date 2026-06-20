---
title: crates/gcode/src/index/import_resolution/context.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/context.rs` exposes 21 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ImportResolutionContext` | class | 'ImportResolutionContext' is a language-aware import/symbol resolution index that stores project-local and dependency package/class/type metadata for Python, JavaScript, Go, Rust, Java, C#, and Kotlin so imports and member references can be resolved to candidate source files. [crates/gcode/src/index/import_resolution/context.rs:41-138] |
| `ImportResolutionContext::js_candidate_files` | method | Returns the list of JavaScript candidate file paths for a given relative path and module specifier by delegating to 'js_candidate_files' with the package name from 'self.js_self_package_name' as an optional argument. [crates/gcode/src/index/import_resolution/context.rs:144-146] |
| `ImportResolutionContext::rust_import_candidate` | method | Resolves a Rust import target from 'rel_path' and 'path' using the current crate/external crate context, then returns a named 'LocalCallBinding' built from the target’s candidate files and symbol name, or 'None' if resolution fails. [crates/gcode/src/index/import_resolution/context.rs:151-166] |
| `ImportResolutionContext::rust_qualified_candidate` | method | Resolves a Rust qualified call target from the relative path, qualifier path, and symbol name using the current crate and external crate set, then returns a 'LocalCallBinding' for the target’s candidate files and resolved name if resolution succeeds. [crates/gcode/src/index/import_resolution/context.rs:170-187] |
| `ImportResolutionContext::go_candidate_files` | method | Returns the cached candidate file list for a Go module path relative to 'self.go_module_path', yielding an empty vector if the module path is unavailable, does not match the current module prefix, or has no entry for the derived directory key. [crates/gcode/src/index/import_resolution/context.rs:194-206] |
| `ImportResolutionContext::java_candidate_files` | method | Returns a cloned 'Vec<String>' of Java class-file candidates for the given fully qualified class name from 'self.java_class_files', or an empty vector if no entry exists. [crates/gcode/src/index/import_resolution/context.rs:212-214] |
| `ImportResolutionContext::csharp_type_files` | method | Returns a cloned 'Vec<String>' of file paths associated with 'type_path' from 'self.csharp_type_files', or an empty vector if the key is absent. [crates/gcode/src/index/import_resolution/context.rs:220-225] |
| `ImportResolutionContext::kotlin_package_files` | method | Returns a cloned 'Vec<String>' of Kotlin package file paths for the given 'package' key from 'self.kotlin_package_files', or an empty vector if the package is absent. [crates/gcode/src/index/import_resolution/context.rs:231-236] |
| `ImportResolutionContext::scala_package_files` | method | Returns a cloned 'Vec<String>' of Scala package files for the given 'package' key from 'self.scala_package_files', or an empty vector if the package is absent. [crates/gcode/src/index/import_resolution/context.rs:241-246] |
| `ImportResolutionContext::lua_module_files` | method | Returns a cloned 'Vec<String>' of file paths registered for the given Lua module name, or an empty vector if the module is not present. [crates/gcode/src/index/import_resolution/context.rs:248-253] |
| `ImportResolutionContext::objc_import_candidate_files` | method | Builds a deduplicated, sorted list of Objective-C import candidates by combining a relative-import resolution for 'rel_path' and 'import_path' with any configured mappings for the full import path and its basename. [crates/gcode/src/index/import_resolution/context.rs:255-277] |
| `ImportResolutionContext::objc_declared_types` | method | Returns a cloned 'Vec<String>' of Objective-C declared types for the given relative path from 'self.objc_file_types', or an empty vector if no entry exists. [crates/gcode/src/index/import_resolution/context.rs:279-284] |
| `ImportResolutionContext::objc_declared_functions` | method | Returns a cloned 'Vec<String>' of Objective-C function names associated with 'rel_path' from 'self.objc_file_functions', or an empty vector if the path is not present. [crates/gcode/src/index/import_resolution/context.rs:286-291] |
| `ImportResolutionContext::php_candidate_files` | method | Returns the vector of PHP file paths associated with the given symbol name after stripping any leading backslashes and lowercasing it for a case-insensitive lookup, or an empty vector if no entry exists. [crates/gcode/src/index/import_resolution/context.rs:297-302] |
| `ImportResolutionContext::swift_module_candidate_files` | method | Returns the sorted, deduplicated list of Swift source file paths associated with the modules inferred from 'rel_path' by looking up each module in 'self.swift_module_files'. [crates/gcode/src/index/import_resolution/context.rs:309-319] |
| `ImportResolutionContext::ruby_require_root` | method | Returns the cached override for 'required' from 'self.ruby_require_root_overrides' as '&str' if present, otherwise delegates to 'ruby_require_root(required)' and returns its 'Option<&str>' result. [crates/gcode/src/index/import_resolution/context.rs:321-326] |
| `ImportResolutionContext::ruby_constant_files` | method | Returns a cloned 'Vec<String>' of cached Ruby constant file paths for the given 'root', or an empty vector if no entry exists. [crates/gcode/src/index/import_resolution/context.rs:328-333] |
| `ImportResolutionContext::elixir_external_root_module` | method | Returns the configured external root module name for 'root', preferring 'elixir_external_root_overrides' over 'elixir_external_roots' and converting the selected 'String' to '&str', or 'None' if neither map contains the key. [crates/gcode/src/index/import_resolution/context.rs:335-340] |
| `ImportResolutionContext::elixir_module_files` | method | Returns a cloned 'Vec<String>' of file paths associated with the given module name from 'self.elixir_module_files', or an empty vector if the module is absent. [crates/gcode/src/index/import_resolution/context.rs:345-350] |
| `build_import_resolution_context` | function | Creates an 'ImportResolutionContext' by delegating to 'build_import_resolution_context_with_overrides' with the given 'root_path' and 'candidate_files', using empty dependency and override maps. [crates/gcode/src/index/import_resolution/context.rs:353-363] |
| `build_import_resolution_context_with_overrides` | function | Builds an 'ImportResolutionContext' by scanning 'candidate_files' under 'root_path' to assemble language-specific symbol/module/package indices and loading project metadata, while incorporating the provided Ruby require-root and Elixir external-root override maps. [crates/gcode/src/index/import_resolution/context.rs:365-409] |

