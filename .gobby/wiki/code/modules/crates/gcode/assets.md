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

The crates/gcode/assets module is an asset container rather than an implementation module: it has no direct files of its own, and its responsibilities are carried by the import_roots child module. That child module supplies static lookup tables used by gcode’s language analysis to connect dependency names or require paths to the top-level symbols they introduce.

The key flow is language-specific import-root resolution. For Elixir, package names such as jason, httpoison, phoenix, telemetry, and ex_doc map to PascalCase module roots such as Jason, HTTPoison, Phoenix, Telemetry, and ExDoc. For Ruby, require paths such as json, fileutils, net/http, faraday, nokogiri, and rspec subpaths map to their corresponding root constants. The stable component IDs show these mappings are tracked as individual properties, including Elixir entries like phoenix and telemetry and Ruby entries like net/http, rspec/core, and rspec/mocks.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

## Child Modules

- [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]] - This module provides static import-root lookup assets for gcode’s language analysis. The Elixir asset maps dependency package names to the top-level modules they provide, covering packages such as jason, httpoison, phoenix, telemetry, and ex_doc with PascalCase module roots like Jason, HTTPoison, Phoenix, Telemetry, and ExDoc . The Ruby asset performs the same role for require paths, mapping standard library and gem requires such as json, fileutils, net/http, faraday, nokogiri, and rspec subpaths to their root constants .

The key flow is data-driven: when gcode encounters a dependency or require path, these JSON files let the import-root analysis resolve that external name to the namespace that should appear in code. Elixir uses package-to-array mappings because a dependency can conceptually provide one or more module roots, while the current table assigns each listed dependency a single root module . Ruby uses require-path-to-constant mappings, including aliases where multiple require paths resolve to the same namespace, such as net/http and net/https both resolving to Net, and rspec plus its submodules resolving to RSpec  .

There are no child modules here; collaboration is simply between two parallel language-specific configuration files. Together they give the broader gcode asset system a compact, stable vocabulary for recognizing external import roots across Elixir and Ruby projects without embedding those package-specific conventions directly in analyzer code.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

