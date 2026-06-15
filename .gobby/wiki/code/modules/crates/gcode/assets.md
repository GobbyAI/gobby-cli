---
title: crates/gcode/assets
type: code_module
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
  ranges:
  - 2-17
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
  ranges:
  - 2-11
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/assets

Parent: [[code/modules/crates/gcode|crates/gcode]]

## Overview

crates/gcode/assets is an asset-only module with no direct source files of its own. Its responsibility is to group static lookup data used by gcode tooling, currently through the import_roots child module, so dependency-resolution logic can consume curated language-specific mappings rather than hard-coding them elsewhere.

The key flow is lookup-oriented: a dependency package name is normalized to the lowercase key used in the asset table, then resolved to one or more canonical import roots. The Elixir import-root asset maps packages such as `jason`, `httpoison`, `ecto`, and `phoenix` to roots like `Jason`, `HTTPoison`, `Ecto`, and `Phoenix`, with values stored as arrays so dependencies can expose multiple roots when needed (crates/gcode/assets/import_roots/elixir_dependency_roots.json:2-18).

The parent module acts as the bundle boundary, while crates/gcode/assets/import_roots owns the actual language tables. This keeps asset ownership separated from the resolver code that reads it, and gives the module a stable catalog of dependency-name properties spanning Elixir and Ruby-style package identifiers for downstream import inference.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

## Child Modules

- [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]] - This module is a small asset bundle that centralizes import-root lookup data for language-specific dependency resolution. Its Elixir table maps lowercase package names to canonical module roots, covering libraries such as `jason` to `Jason`, `httpoison` to `HTTPoison`, `ecto` to `Ecto`, and `phoenix` to `Phoenix` in an array-valued format suitable for dependencies that may expose one or more roots (crates/gcode/assets/import_roots/elixir_dependency_roots.json:2-18).

The Ruby table performs the parallel role for `require` paths, mapping each require root to the top-level constant it introduces. It handles both direct one-to-one roots like `json` to `JSON`, `fileutils` to `FileUtils`, `faraday` to `Faraday`, and `nokogiri` to `Nokogiri`, and grouped paths where multiple requires share a namespace, such as `net/http` and `net/https` both resolving to `Net`, plus several RSpec require paths resolving to `RSpec` (crates/gcode/assets/import_roots/ruby_require_roots.json:2-11).

There are no child modules; collaboration here is by convention across the two JSON assets. Together, they give the importer stable, language-aware dictionaries for converting dependency or require identifiers into the symbols that downstream analysis should treat as introduced import roots.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

