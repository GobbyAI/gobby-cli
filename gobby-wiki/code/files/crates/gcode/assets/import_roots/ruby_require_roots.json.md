---
title: crates/gcode/assets/import_roots/ruby_require_roots.json
type: code_file
provenance:
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
  ranges:
  - 2-11
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/assets/import_roots/ruby_require_roots.json:2-11](crates/gcode/assets/import_roots/ruby_require_roots.json#L2-L11)

</details>

# crates/gcode/assets/import_roots/ruby_require_roots.json

Module: [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]

## Purpose

This JSON file provides a lookup table from Ruby `require` roots to their canonical top-level module names, so the importer can resolve common libraries consistently. Each property maps a require path like `json`, `fileutils`, `net/http`, or `rspec/mocks` to the module root it should associate with, with shared roots such as `Net` and `RSpec` covering multiple related entries.
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:3]
[crates/gcode/assets/import_roots/ruby_require_roots.json:4]
[crates/gcode/assets/import_roots/ruby_require_roots.json:5]
[crates/gcode/assets/import_roots/ruby_require_roots.json:6]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `json` | property | `"json": "JSON",` | `json [property]` | `bdc8856d-d4b1-52ee-a082-ed81f13f717d` | 2-2 [crates/gcode/assets/import_roots/ruby_require_roots.json:2] | Indexed property `json` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:2] |
| `fileutils` | property | `"fileutils": "FileUtils",` | `fileutils [property]` | `84b42fcf-4ca5-5748-b78f-6723ab9e91ae` | 3-3 [crates/gcode/assets/import_roots/ruby_require_roots.json:3] | Indexed property `fileutils` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:3] |
| `net/http` | property | `"net/http": "Net",` | `net/http [property]` | `658f8db7-f161-5950-95fc-ecd688dfdec4` | 4-4 [crates/gcode/assets/import_roots/ruby_require_roots.json:4] | Indexed property `net/http` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:4] |
| `net/https` | property | `"net/https": "Net",` | `net/https [property]` | `dd3a025d-c3fc-5013-a67f-4721ab8e3726` | 5-5 [crates/gcode/assets/import_roots/ruby_require_roots.json:5] | Indexed property `net/https` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:5] |
| `faraday` | property | `"faraday": "Faraday",` | `faraday [property]` | `11d68f16-a6ba-5ccc-91f1-80fcd2c5658c` | 6-6 [crates/gcode/assets/import_roots/ruby_require_roots.json:6] | Indexed property `faraday` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:6] |
| `nokogiri` | property | `"nokogiri": "Nokogiri",` | `nokogiri [property]` | `80e78745-b3af-53a4-a1e7-695c8cb6c7d2` | 7-7 [crates/gcode/assets/import_roots/ruby_require_roots.json:7] | Indexed property `nokogiri` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:7] |
| `rspec` | property | `"rspec": "RSpec",` | `rspec [property]` | `c80959f2-726a-59a6-b48c-7b171ec61834` | 8-8 [crates/gcode/assets/import_roots/ruby_require_roots.json:8] | Indexed property `rspec` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:8] |
| `rspec/expectations` | property | `"rspec/expectations": "RSpec",` | `rspec/expectations [property]` | `efc06569-088b-585c-b3d2-d0549c70df18` | 9-9 [crates/gcode/assets/import_roots/ruby_require_roots.json:9] | Indexed property `rspec/expectations` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:9] |
| `rspec/core` | property | `"rspec/core": "RSpec",` | `rspec/core [property]` | `ae3687ca-8a35-5f3b-acde-d7bea5cc8f3c` | 10-10 [crates/gcode/assets/import_roots/ruby_require_roots.json:10] | Indexed property `rspec/core` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:10] |
| `rspec/mocks` | property | `"rspec/mocks": "RSpec"` | `rspec/mocks [property]` | `d4b2817f-6713-5120-83ee-952ec20c765b` | 11-11 [crates/gcode/assets/import_roots/ruby_require_roots.json:11] | Indexed property `rspec/mocks` in `crates/gcode/assets/import_roots/ruby_require_roots.json`. [crates/gcode/assets/import_roots/ruby_require_roots.json:11] |
