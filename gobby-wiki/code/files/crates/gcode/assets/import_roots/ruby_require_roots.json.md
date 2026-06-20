---
title: crates/gcode/assets/import_roots/ruby_require_roots.json
type: code_file
provenance:
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/assets/import_roots/ruby_require_roots.json

Module: [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]

## Overview

The `crates/gcode/assets/import_roots/ruby_require_roots.json` file is a static configuration asset that defines mappings between Ruby require paths and their corresponding top-level constant or module namespaces. It acts as a static registry used by the indexing and analysis system to resolve import dependencies to their correct runtime constants.

This file helps bridge the gap between file-based import paths and the actual constants defined in Ruby's global namespace. For instance, requiring the path `json` corresponds to the `JSON` namespace as mapped in crates/gcode/assets/import_roots/ruby_require_roots.json:2, while requiring `fileutils` exposes the `FileUtils` namespace as specified in crates/gcode/assets/import_roots/ruby_require_roots.json:3.

## How it fits

This JSON file provides a static dictionary for the surrounding codebase to look up standard and third-party Ruby namespaces. In static analysis, it is difficult to infer namespaces from require paths because Ruby's load paths and naming conventions can decouple file names from module names. 

The configuration maps standard library components like `net/http` at crates/gcode/assets/import_roots/ruby_require_roots.json:4 and `net/https` at crates/gcode/assets/import_roots/ruby_require_roots.json:5 to the shared `Net` namespace. It also indexes major third-party dependencies, resolving the `faraday` HTTP library to `Faraday` at crates/gcode/assets/import_roots/ruby_require_roots.json:6 and `nokogiri` to `Nokogiri` at crates/gcode/assets/import_roots/ruby_require_roots.json:7.

Additionally, testing libraries are consolidated under a single namespace definition. The core testing path `rspec` at crates/gcode/assets/import_roots/ruby_require_roots.json:8, as well as its submodules `rspec/expectations` at crates/gcode/assets/import_roots/ruby_require_roots.json:9, `rspec/core` at crates/gcode/assets/import_roots/ruby_require_roots.json:10, and `rspec/mocks` at crates/gcode/assets/import_roots/ruby_require_roots.json:11, all correctly map to the unified `RSpec` namespace. This mappings layout ensures correct symbol resolution and cross-referencing within Ruby environments.
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:3]
[crates/gcode/assets/import_roots/ruby_require_roots.json:4]
[crates/gcode/assets/import_roots/ruby_require_roots.json:5]
[crates/gcode/assets/import_roots/ruby_require_roots.json:6]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `json` | property | Indexed property `json` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:2] |
| `fileutils` | property | Indexed property `fileutils` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:3] |
| `net/http` | property | Indexed property `net/http` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:4] |
| `net/https` | property | Indexed property `net/https` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:5] |
| `faraday` | property | Indexed property `faraday` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:6] |
| `nokogiri` | property | Indexed property `nokogiri` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:7] |
| `rspec` | property | Indexed property `rspec` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:8] |
| `rspec/expectations` | property | Indexed property `rspec/expectations` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:9] |
| `rspec/core` | property | Indexed property `rspec/core` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:10] |
| `rspec/mocks` | property | Indexed property `rspec/mocks` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:11] |

