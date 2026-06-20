---
title: crates/gcode/assets/import_roots
type: code_module
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/assets/import_roots

Parent: [[code/modules/crates/gcode/assets|crates/gcode/assets]]

## Overview

This module is a data-only import-root registry for dependency resolution. It maps language package or require identifiers to the top-level API symbol that downstream indexing code can associate with source imports: Elixir dependency names resolve to module roots such as `jason` -> `Jason`, while Ruby require strings resolve to constants or namespaces such as `net/http` -> `Net` and `rspec/core` -> `RSpec` (elixir_dependency_roots.json, ruby_require_roots.json).

The key flow is lookup-oriented: callers load the relevant JSON asset, use the dependency or require root as the key, and receive the canonical public symbol used for indexing or symbol linking. No cross-file caller/callee relationships were supplied, so the collaboration point exposed here is the asset contract itself: these files import nothing, call out to nothing, and are consumed by external code as static maps.

| Asset | Entries | Key Form | Value Form |
| --- | ---: | --- | --- |
| `elixir_dependency_roots.json` | 16 | Hex dependency name | Array of Elixir module roots |
| `ruby_require_roots.json` | 10 | Ruby `require` path | Ruby constant or namespace |

| Elixir Roots | Symbols | Source |
| --- | --- | --- |
| `jason`, `httpoison`, `tesla`, `req`, `finch`, `mint` | `Jason`, `HTTPoison`, `Tesla`, `Req`, `Finch`, `Mint` | (/private/var/folders/5w/9cmg71vd2m108t5r_fb77l0h0000gn/T/gobby-textgen-vlaleh7c/crates/gcode/assets/import_roots/elixir_dependency_roots.json:2) |
| `ecto`, `phoenix`, `plug`, `oban`, `broadway` | `Ecto`, `Phoenix`, `Plug`, `Oban`, `Broadway` | (/private/var/folders/5w/9cmg71vd2m108t5r_fb77l0h0000gn/T/gobby-textgen-vlaleh7c/crates/gcode/assets/import_roots/elixir_dependency_roots.json:8) |
| `nimble_options`, `nimble_parsec`, `telemetry`, `benchee`, `ex_doc` | `NimbleOptions`, `NimbleParsec`, `Telemetry`, `Benchee`, `ExDoc` | (/private/var/folders/5w/9cmg71vd2m108t5r_fb77l0h0000gn/T/gobby-textgen-vlaleh7c/crates/gcode/assets/import_roots/elixir_dependency_roots.json:13) |

| Ruby Requires | Symbols | Source |
| --- | --- | --- |
| `json`, `fileutils` | `JSON`, `FileUtils` | (/private/var/folders/5w/9cmg71vd2m108t5r_fb77l0h0000gn/T/gobby-textgen-vlaleh7c/crates/gcode/assets/import_roots/ruby_require_roots.json:2) |
| `net/http`, `net/https`, `faraday`, `nokogiri` | `Net`, `Net`, `Faraday`, `Nokogiri` | (/private/var/folders/5w/9cmg71vd2m108t5r_fb77l0h0000gn/T/gobby-textgen-vlaleh7c/crates/gcode/assets/import_roots/ruby_require_roots.json:4) |
| `rspec`, `rspec/expectations`, `rspec/core`, `rspec/mocks` | `RSpec` | (/private/var/folders/5w/9cmg71vd2m108t5r_fb77l0h0000gn/T/gobby-textgen-vlaleh7c/crates/gcode/assets/import_roots/ruby_require_roots.json:8) |
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/assets/import_roots/elixir_dependency_roots.json\|crates/gcode/assets/import_roots/elixir_dependency_roots.json]] | `crates/gcode/assets/import_roots/elixir_dependency_roots.json` exposes 16 indexed API symbols. |
| [[code/files/crates/gcode/assets/import_roots/ruby_require_roots.json\|crates/gcode/assets/import_roots/ruby_require_roots.json]] | `crates/gcode/assets/import_roots/ruby_require_roots.json` exposes 10 indexed API symbols. |

