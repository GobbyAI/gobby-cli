---
title: crates/gcode/assets/import_roots
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

# crates/gcode/assets/import_roots

Parent: [[code/modules/crates/gcode/assets|crates/gcode/assets]]

## Overview

This module provides static import-root lookup assets for gcode’s language analysis. The Elixir asset maps dependency package names to the top-level modules they provide, covering packages such as jason, httpoison, phoenix, telemetry, and ex_doc with PascalCase module roots like Jason, HTTPoison, Phoenix, Telemetry, and ExDoc . The Ruby asset performs the same role for require paths, mapping standard library and gem requires such as json, fileutils, net/http, faraday, nokogiri, and rspec subpaths to their root constants .

The key flow is data-driven: when gcode encounters a dependency or require path, these JSON files let the import-root analysis resolve that external name to the namespace that should appear in code. Elixir uses package-to-array mappings because a dependency can conceptually provide one or more module roots, while the current table assigns each listed dependency a single root module . Ruby uses require-path-to-constant mappings, including aliases where multiple require paths resolve to the same namespace, such as net/http and net/https both resolving to Net, and rspec plus its submodules resolving to RSpec  .

There are no child modules here; collaboration is simply between two parallel language-specific configuration files. Together they give the broader gcode asset system a compact, stable vocabulary for recognizing external import roots across Elixir and Ruby projects without embedding those package-specific conventions directly in analyzer code.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

## Files

- [[code/files/crates/gcode/assets/import_roots/elixir_dependency_roots.json|crates/gcode/assets/import_roots/elixir_dependency_roots.json]] - This JSON configuration file defines a mapping of Elixir package dependency names to their corresponding module root names. It contains sixteen entries, each pairing a snake_case package name (jason, httpoison, tesla, req, finch, mint, ecto, phoenix, plug, oban, broadway, nimble_options, nimble_parsec, telemetry, benchee, ex_doc) with an array containing the PascalCase module name for that package. This mapping serves as a lookup table to resolve which top-level modules are provided by each Elixir dependency, supporting import root analysis and code generation tooling in the gcode asset system.
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:6]
- [[code/files/crates/gcode/assets/import_roots/ruby_require_roots.json|crates/gcode/assets/import_roots/ruby_require_roots.json]] - This file is a JSON configuration that maps Ruby require paths to their root module namespaces. It contains entries for common Ruby standard library modules (json, fileutils, net/http, net/https) and third-party gems (faraday, nokogiri, rspec and its submodules), each paired with their corresponding top-level constant names. The mapping enables gcode to resolve which root module a given Ruby require statement belongs to, supporting code analysis and import tracking for Ruby projects.
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:3]
[crates/gcode/assets/import_roots/ruby_require_roots.json:4]
[crates/gcode/assets/import_roots/ruby_require_roots.json:5]
[crates/gcode/assets/import_roots/ruby_require_roots.json:6]

## Components

- `b24bad7f-7de6-5799-8fab-48802968cdba`
- `241d382a-2357-5a44-933b-057afcd30803`
- `057ed04f-1cba-56d6-87a0-75f665d776dd`
- `f50b2fec-6f99-5bbf-adf7-826c2a9fb4a5`
- `79a996a2-20ac-5d65-a77c-b6a4201bdaa2`
- `e72a92b0-ba0b-50dd-b3ad-e4f0043a4ae7`
- `b3f40f3b-afb3-5924-aa66-3718f08c29ab`
- `6f2d6c5d-1252-5f05-bdd5-2028fcf2af59`
- `427b2434-f39e-59ed-89da-0758c3e82c29`
- `997f03cd-3687-5e68-a7d2-34ae7bcf1145`
- `c37dd26b-40c1-59a2-b1c5-818b1591d915`
- `e9166c00-7594-519d-b9bd-1728d0c3d018`
- `53940561-1a9b-569b-a077-e1fd87ef3597`
- `9cb7c1e6-04cd-5ac8-b5bb-5f3c3a5f1371`
- `4a83b7a5-a4e7-53fa-86d9-05cc2ca96f62`
- `9a902fa3-e0ad-5b11-80d8-02ea63ff47b4`
- `bdc8856d-d4b1-52ee-a082-ed81f13f717d`
- `84b42fcf-4ca5-5748-b78f-6723ab9e91ae`
- `658f8db7-f161-5950-95fc-ecd688dfdec4`
- `dd3a025d-c3fc-5013-a67f-4721ab8e3726`
- `11d68f16-a6ba-5ccc-91f1-80fcd2c5658c`
- `80e78745-b3af-53a4-a1e7-695c8cb6c7d2`
- `c80959f2-726a-59a6-b48c-7b171ec61834`
- `efc06569-088b-585c-b3d2-d0549c70df18`
- `ae3687ca-8a35-5f3b-acde-d7bea5cc8f3c`
- `d4b2817f-6713-5120-83ee-952ec20c765b`

