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

`crates/gcode/src/index/import_resolution/context/jvm.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `JavaClassIndex` | class | Indexed class `JavaClassIndex` in `crates/gcode/src/index/import_resolution/context/jvm.rs`. [crates/gcode/src/index/import_resolution/context/jvm.rs:10-17] |
| `build_java_class_index` | function | Builds a 'JavaClassIndex' by scanning candidate '.java' files in parallel, extracting package declarations and declared types, collecting all local and fully qualified class names into a set, and mapping each fully qualified class name to the file’s repository-relative path. [crates/gcode/src/index/import_resolution/context/jvm.rs:19-79] |
| `build_kotlin_package_files` | function | Indexed function `build_kotlin_package_files` in `crates/gcode/src/index/import_resolution/context/jvm.rs`. [crates/gcode/src/index/import_resolution/context/jvm.rs:87-145] |
| `build_scala_package_files` | function | Indexed function `build_scala_package_files` in `crates/gcode/src/index/import_resolution/context/jvm.rs`. [crates/gcode/src/index/import_resolution/context/jvm.rs:152-218] |

