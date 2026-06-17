---
title: crates/gcode/src/index/import_resolution/context/jvm.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/jvm.rs
  ranges:
  - 10-17
  - 19-79
  - 87-145
  - 152-218
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/jvm.rs:10-17](crates/gcode/src/index/import_resolution/context/jvm.rs#L10-L17), [crates/gcode/src/index/import_resolution/context/jvm.rs:19-79](crates/gcode/src/index/import_resolution/context/jvm.rs#L19-L79), [crates/gcode/src/index/import_resolution/context/jvm.rs:87-145](crates/gcode/src/index/import_resolution/context/jvm.rs#L87-L145), [crates/gcode/src/index/import_resolution/context/jvm.rs:152-218](crates/gcode/src/index/import_resolution/context/jvm.rs#L152-L218)

</details>

# crates/gcode/src/index/import_resolution/context/jvm.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Builds import-resolution indexes for JVM source files. `JavaClassIndex` tracks locally declared Java class names and maps fully qualified Java class names to the project-relative files that declare them, so the resolver can tell whether an import refers to a local Java type and where to find it. The three builder functions scan candidate files for Java, Kotlin, and Scala sources, extract package/type information, and assemble the per-language file mappings used by the import-resolution context.
[crates/gcode/src/index/import_resolution/context/jvm.rs:10-17]
[crates/gcode/src/index/import_resolution/context/jvm.rs:19-79]
[crates/gcode/src/index/import_resolution/context/jvm.rs:87-145]
[crates/gcode/src/index/import_resolution/context/jvm.rs:152-218]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `JavaClassIndex` | class | `pub(super) struct JavaClassIndex {` | `JavaClassIndex [class]` | `eb455653-0926-5398-b568-c0f5ab585c4a` | 10-17 [crates/gcode/src/index/import_resolution/context/jvm.rs:10-17] | Indexed class `JavaClassIndex` in `crates/gcode/src/index/import_resolution/context/jvm.rs`. [crates/gcode/src/index/import_resolution/context/jvm.rs:10-17] |
| `build_java_class_index` | function | `pub(super) fn build_java_class_index(` | `build_java_class_index [function]` | `efe49f6d-694c-5de3-bb37-ef952a3a4624` | 19-79 [crates/gcode/src/index/import_resolution/context/jvm.rs:19-79] | Indexed function `build_java_class_index` in `crates/gcode/src/index/import_resolution/context/jvm.rs`. [crates/gcode/src/index/import_resolution/context/jvm.rs:19-79] |
| `build_kotlin_package_files` | function | `pub(super) fn build_kotlin_package_files(` | `build_kotlin_package_files [function]` | `afc72c0f-1b80-5056-b8ae-e13aae8500d9` | 87-145 [crates/gcode/src/index/import_resolution/context/jvm.rs:87-145] | Indexed function `build_kotlin_package_files` in `crates/gcode/src/index/import_resolution/context/jvm.rs`. [crates/gcode/src/index/import_resolution/context/jvm.rs:87-145] |
| `build_scala_package_files` | function | `pub(super) fn build_scala_package_files(` | `build_scala_package_files [function]` | `56a984dd-ac94-5599-a643-ac0de0e77ad2` | 152-218 [crates/gcode/src/index/import_resolution/context/jvm.rs:152-218] | Indexed function `build_scala_package_files` in `crates/gcode/src/index/import_resolution/context/jvm.rs`. [crates/gcode/src/index/import_resolution/context/jvm.rs:152-218] |
