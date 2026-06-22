---
title: crates/gcode/src/index/import_resolution/context/elixir.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/elixir.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/elixir.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/context/elixir.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/elixir.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_elixir_local_module_roots` | function | Scans the given candidate '.ex'/'.exs' files in parallel, extracts the first dot-separated module alias from each 'defmodule' declaration whose root passes 'is_elixir_alias', and returns the deduplicated set of those root names as 'HashSet<String>'. [crates/gcode/src/index/import_resolution/context/elixir.rs:13-49] |
| `build_elixir_local_module_files` | function | Builds a 'HashMap<String, Vec<String>>' from Elixir module names to relative file paths by scanning candidate '.ex'/'.exs' files in parallel, parsing 'defmodule' declarations whose names look like Elixir alias paths, and grouping each discovered module under the files that define it. [crates/gcode/src/index/import_resolution/context/elixir.rs:55-111] |
| `load_elixir_external_roots` | function | Loads Elixir dependency names from 'root_path', gathers any dependency root paths returned for each dependency, and returns a 'HashMap<String, String>' containing those roots as both keys and values. [crates/gcode/src/index/import_resolution/context/elixir.rs:113-124] |
| `load_elixir_dependency_names` | function | Loads Elixir dependency names by heuristically scanning 'mix.exs' and 'mix.lock' under 'root_path' with regexes, collecting matched dependency keys into a 'HashSet<String>' and returning the union. [crates/gcode/src/index/import_resolution/context/elixir.rs:126-149] |
| `elixir_mix_dependency_regex` | function | Returns a lazily initialized static 'Regex' that matches the start of an Elixir Mix dependency tuple, capturing an atom-style dependency name after '{ :' with optional whitespace. [crates/gcode/src/index/import_resolution/context/elixir.rs:151-156] |
| `elixir_lock_dependency_regex` | function | Returns a lazily initialized '&'static Regex' that matches an Elixir lockfile dependency key of the form '"name":', where 'name' starts with a letter or underscore and continues with alphanumerics or underscores. [crates/gcode/src/index/import_resolution/context/elixir.rs:158-164] |

