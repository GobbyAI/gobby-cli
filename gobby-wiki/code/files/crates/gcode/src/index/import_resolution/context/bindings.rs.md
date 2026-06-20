---
title: crates/gcode/src/index/import_resolution/context/bindings.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/bindings.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]

## Overview

`crates/gcode/src/index/import_resolution/context/bindings.rs` exposes 10 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/bindings.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ExternalImportBinding` | class | 'ExternalImportBinding' is an internal struct that stores the target module path and the imported callee name for an external import binding. [crates/gcode/src/index/import_resolution/context/bindings.rs:6-9] |
| `LocalCallResolution` | type | Indexed type `LocalCallResolution` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:12-15] |
| `LocalCallBinding` | class | 'LocalCallBinding' represents a locally resolved call target, storing path-derived candidate files, the original imported callee name, and the final 'LocalCallResolution' used to identify the binding. [crates/gcode/src/index/import_resolution/context/bindings.rs:22-29] |
| `LocalCallBinding::named` | method | Constructs and returns a 'Self' value initialized with the provided 'candidate_files' and 'callee_name', while setting 'resolution' to 'LocalCallResolution::Named'. [crates/gcode/src/index/import_resolution/context/bindings.rs:32-38] |
| `LocalCallBinding::default_export` | method | Constructs a 'Self' instance for a local call resolved as 'LocalCallResolution::DefaultExport', storing the provided 'candidate_files' and mapping 'local_alias' into 'callee_name'. [crates/gcode/src/index/import_resolution/context/bindings.rs:40-46] |
| `LocalCallBinding::is_default_export` | method | Returns 'true' when 'self.resolution' is 'LocalCallResolution::DefaultExport', and 'false' otherwise. [crates/gcode/src/index/import_resolution/context/bindings.rs:48-50] |
| `ImportBindings` | class | 'ImportBindings' is a per-file import-resolution index that tracks bare, local, member, wildcard, and language-specific namespace bindings so identifiers and member calls can be resolved to imported external roots, local files, or scoped declarations. [crates/gcode/src/index/import_resolution/context/bindings.rs:54-90] |
| `ExternalRootBinding` | class | 'ExternalRootBinding' is an internal struct that stores the external root module name as a 'String' along with a 'bool' flag indicating whether that module name was derived from a qualifier. [crates/gcode/src/index/import_resolution/context/bindings.rs:93-96] |
| `ExtractedImports` | class | 'ExtractedImports' is a crate-visible struct that groups a list of 'ImportRelation' values with their associated 'ImportBindings' for an extraction result. [crates/gcode/src/index/import_resolution/context/bindings.rs:99-102] |
| `ExternalCallTarget` | class | 'ExternalCallTarget' is a crate-visible struct that identifies an external call by storing the target 'module' and the 'callee_name' as 'String' values. [crates/gcode/src/index/import_resolution/context/bindings.rs:105-108] |

