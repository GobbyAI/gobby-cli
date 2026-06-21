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

## crates/gcode/assets

The `crates/gcode/assets` module acts as a static registry of well-known external library identifiers that the broader `gcode` crate draws upon for dependency recognition and analysis. It contains no direct source files of its own; its substance is entirely delegated to the `import_roots` child module, which presumably defines the canonical root import paths for each catalogued library. This separation keeps asset data cleanly partitioned from parsing and analysis logic higher in the crate.

The component catalogue spans two major language ecosystems. The Elixir/BEAM set covers HTTP clients and adapters (jason, httpoison, tesla, req, finch, mint), web and job-processing frameworks (phoenix, plug, ecto, oban, broadway), parsing and options utilities (nimble_parsec, nimble_options), and tooling libraries (telemetry, benchee, ex_doc). The Ruby set covers JSON handling (json), HTTP networking (net/http, net/https, faraday), HTML parsing (nokogiri), filesystem utilities (fileutils), and the RSpec testing stack (rspec, rspec/core, rspec/expectations, rspec/mocks). Taken together, these entries suggest the gcode crate performs polyglot import analysis across at least Elixir and Ruby source trees.

Because no source excerpts or cross-file relationships were supplied, the precise mechanism by which `import_roots` exposes these identifiers — whether as static string slices, enum variants, or structured metadata records — cannot be confirmed from available evidence. Downstream consumers within `crates/gcode` are expected to query this registry to classify import statements encountered during parsing, matching raw import strings against the catalogued roots.

### Catalogued Library Properties

| Library | Ecosystem | Stable Component ID |
|---|---|---|
| jason | Elixir | b24bad7f-7de6-5799-8fab-48802968cdba |
| httpoison | Elixir | 241d382a-2357-5a44-933b-057afcd30803 |
| tesla | Elixir | 057ed04f-1cba-56d6-87a0-75f665d776dd |
| req | Elixir | f50b2fec-6f99-5bbf-adf7-826c2a9fb4a5 |
| finch | Elixir | 79a996a2-20ac-5d65-a77c-b6a4201bdaa2 |
| mint | Elixir | e72a92b0-ba0b-50dd-b3ad-e4f0043a4ae7 |
| ecto | Elixir | b3f40f3b-afb3-5924-aa66-3718f08c29ab |
| phoenix | Elixir | 6f2d6c5d-1252-5f05-bdd5-2028fcf2af59 |
| plug | Elixir | 427b2434-f39e-59ed-89da-0758c3e82c29 |
| oban | Elixir | 997f03cd-3687-5e68-a7d2-34ae7bcf1145 |
| broadway | Elixir | c37dd26b-40c1-59a2-b1c5-818b1591d915 |
| nimble_options | Elixir | e9166c00-7594-519d-b9bd-1728d0c3d018 |
| nimble_parsec | Elixir | 53940561-1a9b-569b-a077-e1fd87ef3597 |
| telemetry | Elixir | 9cb7c1e6-04cd-5ac8-b5bb-5f3c3a5f1371 |
| benchee | Elixir | 4a83b7a5-a4e7-53fa-86d9-05cc2ca96f62 |
| ex_doc | Elixir | 9a902fa3-e0ad-5b11-80d8-02ea63ff47b4 |
| json | Ruby | bdc8856d-d4b1-52ee-a082-ed81f13f717d |
| fileutils | Ruby stdlib | 84b42fcf-4ca5-5748-b78f-6723ab9e91ae |
| net/http | Ruby stdlib | 658f8db7-f161-5950-95fc-ecd688dfdec4 |
| net/https | Ruby stdlib | dd3a025d-c3fc-5013-a67f-4721ab8e3726 |
| faraday | Ruby | 11d68f16-a6ba-5ccc-91f1-80fcd2c5658c |
| nokogiri | Ruby | 80e78745-b3af-53a4-a1e7-695c8cb6c7d2 |
| rspec | Ruby | c80959f2-726a-59a6-b48c-7b171ec61834 |
| rspec/expectations | Ruby | efc06569-088b-585c-b3d2-d0549c70df18 |
| rspec/core | Ruby | ae3687ca-8a35-5f3b-acde-d7bea5cc8f3c |
| rspec/mocks | Ruby | d4b2817f-6713-5120-83ee-952ec20c765b |
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]
[crates/gcode/assets/import_roots/ruby_require_roots.json:2]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:4]
[crates/gcode/assets/import_roots/elixir_dependency_roots.json:5]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/assets/import_roots\|crates/gcode/assets/import_roots]] | ## crates/gcode/assets/import_roots |

