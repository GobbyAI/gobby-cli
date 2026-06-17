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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2-17](crates/gcode/assets/import_roots/elixir_dependency_roots.json#L2-L17)
- [crates/gcode/assets/import_roots/ruby_require_roots.json:2-11](crates/gcode/assets/import_roots/ruby_require_roots.json#L2-L11)

</details>

# crates/gcode/assets/import_roots

Parent: [[code/modules/crates/gcode/assets|crates/gcode/assets]]

## Overview

The `crates/gcode/assets/import_roots` module acts as a static registry of configuration assets that map Elixir and Ruby external dependencies to their canonical namespaces. Its primary responsibility is to supply the codebase importer with standardized definitions, resolving third-party imports to ensure consistent indexing across varying source file conventions. The module leverages simple JSON-structured lookup tables to establish mapping rules without maintaining complex execution state.

During import and analysis workflows, the indexing engine queries these dependency databases. For Elixir targets, the package names are resolved to their canonical module roots . For Ruby source files, the system parses `require` statements and routes the import targets to unified top-level modules, consolidating clustered subsystems such as net utilities or test frameworks under a singular root .

### Elixir Dependency Root Mappings

| Dependency Key | Canonical Module Root | Citation |
| --- | --- | --- |
| jason | ["Jason"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] |
| httpoison | ["HTTPoison"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3] |
| tesla | ["Tesla"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:4] |
| req | ["Req"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:5] |
| finch | ["Finch"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:6] |
| mint | ["Mint"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:7] |
| ecto | ["Ecto"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:8] |
| phoenix | ["Phoenix"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:9] |
| plug | ["Plug"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:10] |
| oban | ["Oban"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:11] |
| broadway | ["Broadway"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:12] |
| nimble_options | ["NimbleOptions"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:13] |
| nimble_parsec | ["NimbleParsec"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:14] |
| telemetry | ["Telemetry"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:15] |
| benchee | ["Benchee"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:16] |
| ex_doc | ["ExDoc"] | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:17] |

### Ruby Require Mappings

| Require Path | Canonical Module Root | Citation |
| --- | --- | --- |
| json | JSON | [crates/gcode/assets/import_roots/ruby_require_roots.json:2] |
| fileutils | FileUtils | [crates/gcode/assets/import_roots/ruby_require_roots.json:3] |
| net/http | Net | [crates/gcode/assets/import_roots/ruby_require_roots.json:4] |
| net/https | Net | [crates/gcode/assets/import_roots/ruby_require_roots.json:5] |
| faraday | Faraday | [crates/gcode/assets/import_roots/ruby_require_roots.json:6] |
| nokogiri | Nokogiri | [crates/gcode/assets/import_roots/ruby_require_roots.json:7] |
| rspec | RSpec | [crates/gcode/assets/import_roots/ruby_require_roots.json:8] |
| rspec/expectations | RSpec | [crates/gcode/assets/import_roots/ruby_require_roots.json:9] |
| rspec/core | RSpec | [crates/gcode/assets/import_roots/ruby_require_roots.json:10] |
| rspec/mocks | RSpec | [crates/gcode/assets/import_roots/ruby_require_roots.json:11] |

## Dependency Diagram

`degraded: graph-truncated`

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/assets/import_roots/elixir_dependency_roots.json\|crates/gcode/assets/import_roots/elixir_dependency_roots.json]] | This JSON file maps common Elixir dependency root names to their canonical module/import roots, providing a lookup table for libraries like `jason`, `httpoison`, `phoenix`, and `ex_doc`. Each property supplies the normalized package key and its corresponding root identifier so the importer can recognize and index Elixir dependencies consistently. [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:4] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:5] [crates/gcode/assets/import_roots/elixir_dependency_roots.json:6] |
| [[code/files/crates/gcode/assets/import_roots/ruby_require_roots.json\|crates/gcode/assets/import_roots/ruby_require_roots.json]] | This JSON file provides a lookup table from Ruby `require` roots to their canonical top-level module names, so the importer can resolve common libraries consistently. Each property maps a require path like `json`, `fileutils`, `net/http`, or `rspec/mocks` to the module root it should associate with, with shared roots such as `Net` and `RSpec` covering multiple related entries. [crates/gcode/assets/import_roots/ruby_require_roots.json:2] [crates/gcode/assets/import_roots/ruby_require_roots.json:3] [crates/gcode/assets/import_roots/ruby_require_roots.json:4] [crates/gcode/assets/import_roots/ruby_require_roots.json:5] [crates/gcode/assets/import_roots/ruby_require_roots.json:6] |

## Components

| Component ID |
| --- |
| `b24bad7f-7de6-5799-8fab-48802968cdba` |
| `241d382a-2357-5a44-933b-057afcd30803` |
| `057ed04f-1cba-56d6-87a0-75f665d776dd` |
| `f50b2fec-6f99-5bbf-adf7-826c2a9fb4a5` |
| `79a996a2-20ac-5d65-a77c-b6a4201bdaa2` |
| `e72a92b0-ba0b-50dd-b3ad-e4f0043a4ae7` |
| `b3f40f3b-afb3-5924-aa66-3718f08c29ab` |
| `6f2d6c5d-1252-5f05-bdd5-2028fcf2af59` |
| `427b2434-f39e-59ed-89da-0758c3e82c29` |
| `997f03cd-3687-5e68-a7d2-34ae7bcf1145` |
| `c37dd26b-40c1-59a2-b1c5-818b1591d915` |
| `e9166c00-7594-519d-b9bd-1728d0c3d018` |
| `53940561-1a9b-569b-a077-e1fd87ef3597` |
| `9cb7c1e6-04cd-5ac8-b5bb-5f3c3a5f1371` |
| `4a83b7a5-a4e7-53fa-86d9-05cc2ca96f62` |
| `9a902fa3-e0ad-5b11-80d8-02ea63ff47b4` |
| `bdc8856d-d4b1-52ee-a082-ed81f13f717d` |
| `84b42fcf-4ca5-5748-b78f-6723ab9e91ae` |
| `658f8db7-f161-5950-95fc-ecd688dfdec4` |
| `dd3a025d-c3fc-5013-a67f-4721ab8e3726` |
| `11d68f16-a6ba-5ccc-91f1-80fcd2c5658c` |
| `80e78745-b3af-53a4-a1e7-695c8cb6c7d2` |
| `c80959f2-726a-59a6-b48c-7b171ec61834` |
| `efc06569-088b-585c-b3d2-d0549c70df18` |
| `ae3687ca-8a35-5f3b-acde-d7bea5cc8f3c` |
| `d4b2817f-6713-5120-83ee-952ec20c765b` |
