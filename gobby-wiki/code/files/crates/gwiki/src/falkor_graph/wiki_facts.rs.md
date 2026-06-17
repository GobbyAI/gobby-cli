---
title: crates/gwiki/src/falkor_graph/wiki_facts.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/wiki_facts.rs
  ranges:
  - 13-98
  - 100-132
  - 134-142
  - 144-157
  - 159-161
  - 163-176
  - 178-186
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98](crates/gwiki/src/falkor_graph/wiki_facts.rs#L13-L98), [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132](crates/gwiki/src/falkor_graph/wiki_facts.rs#L100-L132), [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142](crates/gwiki/src/falkor_graph/wiki_facts.rs#L134-L142), [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157](crates/gwiki/src/falkor_graph/wiki_facts.rs#L144-L157), [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161](crates/gwiki/src/falkor_graph/wiki_facts.rs#L159-L161), [crates/gwiki/src/falkor_graph/wiki_facts.rs:163-176](crates/gwiki/src/falkor_graph/wiki_facts.rs#L163-L176), [crates/gwiki/src/falkor_graph/wiki_facts.rs:178-186](crates/gwiki/src/falkor_graph/wiki_facts.rs#L178-L186)

</details>

# crates/gwiki/src/falkor_graph/wiki_facts.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds `WikiGraphFacts` for a search scope by reading wiki documents and links from Postgres, then resolving each link target into a normalized graph target. `load_wiki_graph_facts` gathers documents, derives the set of known document paths, builds a slug-to-target map for title-based references, and loads links and sources into the graph facts result. The helper functions work together to interpret targets: `resolve_graph_target` chooses between direct paths, relative paths, slug matches, and external URLs; `resolve_relative_graph_path` and `normalize_path` clean up path-like targets; `slug_target_map` indexes documents by slug; `is_path_like_target` and `is_external_target` classify raw link targets before resolution.
[crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `load_wiki_graph_facts` | function | `pub(crate) fn load_wiki_graph_facts(` | `load_wiki_graph_facts [function]` | `4d60aa47-5986-548d-9cae-f94257e97305` | 13-98 [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98] | Indexed function `load_wiki_graph_facts` in `crates/gwiki/src/falkor_graph/wiki_facts.rs`. [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98] |
| `resolve_graph_target` | function | `pub(super) fn resolve_graph_target(` | `resolve_graph_target [function]` | `0f96a6b2-3f9f-54e1-8a93-55d3dacff49b` | 100-132 [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132] | Indexed function `resolve_graph_target` in `crates/gwiki/src/falkor_graph/wiki_facts.rs`. [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132] |
| `slug_target_map` | function | `pub(super) fn slug_target_map(documents: &[WikiGraphDocument]) -> BTreeMap<String, PathBuf> {` | `slug_target_map [function]` | `0db8eae8-81ba-5f42-a87b-1811ef91f66e` | 134-142 [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142] | Indexed function `slug_target_map` in `crates/gwiki/src/falkor_graph/wiki_facts.rs`. [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142] |
| `resolve_relative_graph_path` | function | `fn resolve_relative_graph_path(raw_target: &str, source_path: &Path) -> String {` | `resolve_relative_graph_path [function]` | `d6ff3e27-e967-5741-bce2-edc03a5634ae` | 144-157 [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157] | Indexed function `resolve_relative_graph_path` in `crates/gwiki/src/falkor_graph/wiki_facts.rs`. [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157] |
| `is_path_like_target` | function | `fn is_path_like_target(target: &str) -> bool {` | `is_path_like_target [function]` | `663ec667-9918-525d-a4dc-74935a3d965b` | 159-161 [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161] | Indexed function `is_path_like_target` in `crates/gwiki/src/falkor_graph/wiki_facts.rs`. [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161] |
| `normalize_path` | function | `fn normalize_path(path: PathBuf) -> PathBuf {` | `normalize_path [function]` | `b07ea7cf-e4ea-5736-a222-440a89520e01` | 163-176 [crates/gwiki/src/falkor_graph/wiki_facts.rs:163-176] | Indexed function `normalize_path` in `crates/gwiki/src/falkor_graph/wiki_facts.rs`. [crates/gwiki/src/falkor_graph/wiki_facts.rs:163-176] |
| `is_external_target` | function | `fn is_external_target(target: &str) -> bool {` | `is_external_target [function]` | `a0c822d1-8b52-5757-8738-840ac6a1b723` | 178-186 [crates/gwiki/src/falkor_graph/wiki_facts.rs:178-186] | Indexed function `is_external_target` in `crates/gwiki/src/falkor_graph/wiki_facts.rs`. [crates/gwiki/src/falkor_graph/wiki_facts.rs:178-186] |
