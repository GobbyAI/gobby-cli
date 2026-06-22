---
title: Dependency Root Catalog
type: code_concept
provenance:
- file: crates/gcode/assets/import_roots/elixir_dependency_roots.json
- file: crates/gcode/assets/import_roots/ruby_require_roots.json
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/assets/import_roots/elixir_dependency_roots.json](crates/gcode/assets/import_roots/elixir_dependency_roots.json)
- [crates/gcode/assets/import_roots/ruby_require_roots.json](crates/gcode/assets/import_roots/ruby_require_roots.json)

</details>

# Dependency Root Catalog

## Purpose

The Dependency Root Catalog is a set of static, language-specific lookup tables that map a package name or `require` path back to the canonical root module(s) that name introduces. When analyzing source code across multiple languages (polyglot import analysis), a dependency declared in a manifest (for example the Elixir package `httpoison`) does not literally match the symbol used in code (the `HTTPoison` module). The catalog bridges that gap by recording, per ecosystem, which top-level module names a given dependency or require path resolves to.

Concretely, the Elixir table maps a Mix dependency atom such as `jason` to its module list `["Jason"]` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2], and the Ruby table maps a require path such as `net/http` to its root constant `Net` [crates/gcode/assets/import_roots/ruby_require_roots.json:4]. This solves the problem of correlating declared dependencies with the symbols actually imported in code, which is necessary for accurate cross-language import resolution.

## Covers / Does not cover

This concept covers the data assets themselves: the JSON lookup tables that ship under `crates/gcode/assets/import_roots/`. It covers two ecosystems today:

- Elixir dependency roots, with 16 indexed entries [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2].
- Ruby require roots, with 10 indexed entries [crates/gcode/assets/import_roots/ruby_require_roots.json:2].

It does not cover the Rust code in the `gcode` crate that loads or consumes these tables — that loader logic is not present in the supplied input. It also does not cover other languages: only Elixir and Ruby tables exist here, and there is no general registry of every package in either ecosystem. The tables are curated, finite catalogs of common libraries, not exhaustive mirrors of Hex or RubyGems.

## Architecture

The catalog is structured as one JSON file per language, grouped under the `import_roots` module directory inside the crate's `assets` folder [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]. Splitting by language is deliberate: each ecosystem has different naming conventions and a different shape of mapping, so encoding each in its own file keeps the data simple and the per-language semantics explicit.

The two files differ in value shape, reflecting how each language resolves names. The Elixir table maps each key to an *array* of module names — for example `"jason": ["Jason"]` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] — because a single Mix dependency can introduce more than one root module. The Ruby table maps each key to a *single string* constant — for example `"json": "JSON"` [crates/gcode/assets/import_roots/ruby_require_roots.json:2] — matching Ruby's convention that a require path yields one primary constant root.

The Ruby table also demonstrates that multiple keys may share one root. The require paths `net/http` and `net/https` both resolve to `Net` [crates/gcode/assets/import_roots/ruby_require_roots.json:4], and the several `rspec/*` paths all resolve to `RSpec`. This many-to-one arrangement lets a sub-path require still be attributed to the correct top-level constant. Because these are plain static assets keyed by name, lookups are direct key access with no computation, which is why the data lives as JSON rather than code.

## Data flow

The following traces how the catalog participates at runtime. (The consuming loader code is outside the supplied input; steps that reference it describe the catalog's role in that flow.)

1. An import analyzer encounters a dependency or require reference in source — for example the Elixir atom `httpoison` or the Ruby require `"net/http"`.
2. The analyzer selects the language-appropriate table: the Elixir file for Elixir sources [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3], the Ruby file for Ruby sources [crates/gcode/assets/import_roots/ruby_require_roots.json:4].
3. The reference name is looked up as a key. For Elixir, `httpoison` resolves to the module list `["HTTPoison"]` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]; for Ruby, `net/http` resolves to the single constant `Net` [crates/gcode/assets/import_roots/ruby_require_roots.json:4].
4. The resolved root module(s) are returned to the analyzer, which can then correlate them with symbols actually used in code.
5. When a key is not present in the table — that is, the dependency or require path is not catalogued here — there is no mapping to return. The catalog is a finite curated set, so any uncatalogued name has no canonical root and the analyzer must fall back to its own default handling; the table itself contributes nothing for that name.

## Key components

The most important elements are the two table files and representative entries showing each table's value shape.

| Symbol | File | Role |
| --- | --- | --- |
| Elixir dependency roots table | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] | Maps Mix dependency names to arrays of canonical root modules |
| Ruby require roots table | [crates/gcode/assets/import_roots/ruby_require_roots.json:2] | Maps require paths to a single canonical root constant |
| `jason` → `["Jason"]` | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2] | Example Elixir entry; value is a module array |
| `httpoison` → `["HTTPoison"]` | [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3] | Shows package name differing from module name |
| `net/http` → `Net` | [crates/gcode/assets/import_roots/ruby_require_roots.json:4] | Example Ruby entry; sub-path mapped to top-level constant |

## Where to start

Start by reading `crates/gcode/assets/import_roots/elixir_dependency_roots.json` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:2]. It is the larger of the two tables and clearly demonstrates the core idea — a package key resolving to its canonical module — including cases where the names diverge, such as `httpoison` → `HTTPoison` [crates/gcode/assets/import_roots/elixir_dependency_roots.json:3]. Then read `ruby_require_roots.json` [crates/gcode/assets/import_roots/ruby_require_roots.json:2] to see the alternate single-string value shape and the many-to-one pattern where `net/http` and `net/https` both map to `Net` [crates/gcode/assets/import_roots/ruby_require_roots.json:4].

## Explore

- [[code/modules/crates/gcode/assets|crates/gcode/assets]]
- [[code/modules/crates/gcode/assets/import_roots|crates/gcode/assets/import_roots]]

