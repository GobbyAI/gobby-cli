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

## crates/gcode/assets/import_roots

This module is a static asset directory inside the `gcode` crate that supplies language-specific lookup tables for resolving dependency identifiers back to their canonical root namespaces. It currently covers two ecosystems — Elixir (Mix dependencies) and Ruby (RubyGems / standard-library requires) — each encoded as a compact JSON object. The files are consumed at build time or at runtime by the `gcode` crate's import-analysis logic to determine which top-level constant or module a given `require` or `use` statement introduces into scope.

The core responsibility of each file is the same: given a package or require-path string as a key, expose the one or more root module constants that become available after the import is evaluated. For Elixir, values are arrays because a single Mix dependency may expose several root modules (elixir_dependency_roots.json:1-19). For Ruby, values are plain strings because a `require` call surfaces exactly one top-level constant, even when multiple require-paths share the same namespace (e.g. `rspec`, `rspec/core`, and `rspec/mocks` all resolve to `RSpec`) (ruby_require_roots.json:1-13).

These JSON assets are pure data with no executable code; all logic that reads and applies them lives in the parent `gcode` crate. The files act as a seam between the static, human-curated knowledge of "what does this dependency export?" and the dynamic program-analysis passes that walk source files. Adding support for a new well-known library requires only an entry in the appropriate JSON file rather than a code change.

### Elixir dependency → root module mapping

elixir_dependency_roots.json:1-19

| Mix dependency | Root module(s) |
|---|---|
| jason | Jason |
| httpoison | HTTPoison |
| tesla | Tesla |
| req | Req |
| finch | Finch |
| mint | Mint |
| ecto | Ecto |
| phoenix | Phoenix |
| plug | Plug |
| oban | Oban |
| broadway | Broadway |
| nimble_options | NimbleOptions |
| nimble_parsec | NimbleParsec |
| telemetry | Telemetry |
| benchee | Benchee |
| ex_doc | ExDoc |

### Ruby require-path → root constant mapping

ruby_require_roots.json:1-13

| require path | Root constant |
|---|---|
| json | JSON |
| fileutils | FileUtils |
| net/http | Net |
| net/https | Net |
| faraday | Faraday |
| nokogiri | Nokogiri |
| rspec | RSpec |
| rspec/expectations | RSpec |
| rspec/core | RSpec |
| rspec/mocks | RSpec |
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

