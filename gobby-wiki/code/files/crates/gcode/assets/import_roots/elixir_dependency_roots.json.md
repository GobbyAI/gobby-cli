---
title: crates/gcode/assets/import_roots/elixir_dependency_roots.json
type: code_file
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/assets/import_roots/elixir_dependency_roots.json

Module: [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]

## Overview
This asset file defines a static lookup map of popular Elixir dependency package names to their canonical top-level module names. It provides a structured dictionary where each key represents a lowercase Elixir package name, and the value is an array containing the capitalized module namespaces associated with that library.

The file serves as a reference directory for resolve and import analysis tools within the gcode toolchain. By providing these standard mappings, it enables tools to identify external modules imported or used in Elixir projects and map them back to their originating packages.

## How it fits
This configuration file is placed under the asset directories of the gcode workspace. It defines the mapping schema for standard libraries such as `jason` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:2, `httpoison` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:3, `tesla` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:4, `req` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:5, and `finch` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:6.

It also contains mappings for `mint` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:7, `ecto` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:8, `phoenix` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:9, `plug` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:10, and `oban` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:11.

Furthermore, it maps `broadway` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:12, `nimble_options` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:13, `nimble_parsec` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:14, `telemetry` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:15, `benchee` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:16, and `ex_doc` on crates/gcode/assets/import_roots/elixir_dependency_roots.json:17.

No external calling files or direct module relationships are supplied in the current context, indicating that this resource is loaded dynamically or compiled in by the surrounding module resolution systems of the crate.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:6]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `jason` | property | Indexed property `jason` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] |
| `httpoison` | property | Indexed property `httpoison` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3] |
| `tesla` | property | Indexed property `tesla` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:4] |
| `req` | property | Indexed property `req` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:5] |
| `finch` | property | Indexed property `finch` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:6] |
| `mint` | property | Indexed property `mint` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:7] |
| `ecto` | property | Indexed property `ecto` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:8] |
| `phoenix` | property | Indexed property `phoenix` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:9] |
| `plug` | property | Indexed property `plug` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:10] |
| `oban` | property | Indexed property `oban` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:11] |
| `broadway` | property | Indexed property `broadway` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:12] |
| `nimble_options` | property | Indexed property `nimble_options` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:13] |
| `nimble_parsec` | property | Indexed property `nimble_parsec` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:14] |
| `telemetry` | property | Indexed property `telemetry` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:15] |
| `benchee` | property | Indexed property `benchee` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:16] |
| `ex_doc` | property | Indexed property `ex_doc` in `crates/gcode/assets/import_roots/elixir_dependency_roots.json`. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:17] |

