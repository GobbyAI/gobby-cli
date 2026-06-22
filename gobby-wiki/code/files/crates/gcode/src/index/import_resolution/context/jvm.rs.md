---
title: crates/gcode/src/index/import_resolution/context/jvm.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/jvm.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/jvm.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/context/jvm.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/jvm.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `JavaClassIndex` | class | 'JavaClassIndex' is a project-local lookup table that tracks declared Java class names and maps fully qualified class names to their declaring project-relative file paths for resolving imports and determining whether a class is external. [crates/gcode/src/index/import_resolution/context/jvm.rs:10-17] |
| `build_java_class_index` | function | Builds a 'JavaClassIndex' by scanning candidate '.java' files in parallel, extracting package declarations and declared types, collecting all local and fully qualified class names into a set, and mapping each fully qualified class name to the file’s repository-relative path. [crates/gcode/src/index/import_resolution/context/jvm.rs:19-79] |
| `build_kotlin_package_files` | function | Builds a 'HashMap' that groups relative Kotlin source file paths by their declared package (or the empty root package if no 'package' header is found), scanning only '.kt' and '.kts' files in parallel and normalizing paths to '/' separators. [crates/gcode/src/index/import_resolution/context/jvm.rs:87-145] |
| `build_scala_package_files` | function | Builds a 'HashMap' from Scala package names to relative source file paths by filtering '.scala'/'.sc' files, reading leading 'package' declarations from each file until non-package code begins, and grouping each file under the joined package string. [crates/gcode/src/index/import_resolution/context/jvm.rs:152-218] |

