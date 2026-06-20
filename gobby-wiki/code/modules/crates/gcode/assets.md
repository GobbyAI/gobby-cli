---
title: crates/gcode/assets
type: code_module
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/assets

Parent: [[code/modules/crates/gcode|crates/gcode]]

## Overview

`crates/gcode/assets` is a data-only asset area for GCode’s dependency/import resolution. Its child module, `assets/import_roots`, provides registry JSON files that map package or require identifiers to top-level API roots used by downstream indexing code.

The key flow is lookup-based: Elixir dependency names such as `jason` resolve to module roots such as `Jason`, while Ruby require strings such as `net/http` and `rspec/core` resolve to constants or namespaces such as `Net` and `RSpec`. No direct module source files, excerpts, or cross-file call relationships were supplied, so this brief only describes the asset responsibilities visible from the summaries.

| Asset | Language | Identifier Type | Example Mapping |
| --- | --- | --- | --- |
| `elixir_dependency_roots.json` | Elixir | Dependency name | `jason` -> `Jason` |
| `ruby_require_roots.json` | Ruby | `require` string | `net/http` -> `Net` |
| `ruby_require_roots.json` | Ruby | `require` string | `rspec/core` -> `RSpec` |

| Registry Entries |
| --- |
| `jason`, `httpoison`, `tesla`, `req`, `finch`, `mint`, `ecto`, `phoenix`, `plug`, `oban`, `broadway`, `nimble_options`, `nimble_parsec`, `telemetry`, `benchee`, `ex_doc`, `json`, `fileutils`, `net/http`, `net/https`, `faraday`, `nokogiri`, `rspec`, `rspec/expectations`, `rspec/core`, `rspec/mocks` |
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/assets/import_roots\|crates/gcode/assets/import_roots]] | This module is a data-only import-root registry for dependency resolution. It maps language package or require identifiers to the top-level API symbol that downstream indexing code can associate with source imports: Elixir dependency names resolve to module roots such as `jason` -> `Jason`, while Ruby require strings resolve to constants or namespaces such as `net/http` -> `Net` and `rspec/core` -> `RSpec` (elixir_dependency_roots.json, ruby_require_roots.json). |

