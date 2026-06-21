---
title: crates/gwiki/src/falkor_graph/wiki_facts.rs
type: code_file
provenance:
- file: crates/gwiki/src/falkor_graph/wiki_facts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph/wiki_facts.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/falkor_graph/wiki_facts.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/falkor_graph/wiki_facts.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `load_wiki_graph_facts` | function | Queries a database to load wiki documents and links filtered by a search scope, resolves link targets to document paths, and returns aggregated WikiGraphFacts or a WikiError. [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98] |
| `resolve_graph_target` | function | Resolves a wiki graph link target by normalizing the input string and attempting to match it against known document paths through direct path lookup and slug-based resolution, returning either a confirmed document path or an unresolved target string. [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132] |
| `slug_target_map` | function | Constructs a lexicographically sorted 'BTreeMap' from slugified document titles to their corresponding file paths, filtering out documents lacking titles. [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142] |
| `resolve_relative_graph_path` | function | Resolves a raw target string as an absolute path (if it starts with '/' or isn't path-like) or relative to the parent directory of the source path, returning a normalized path string with forward slashes. [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157] |
| `is_path_like_target` | function | Returns 'true' if the target string contains a forward slash, starts with a dot, or ends with '.md', indicating a file path or markdown file reference. [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161] |
| `normalize_path` | function | Normalizes a path by resolving relative directory traversals ('.' and '..') and discarding root/prefix components, returning a relative path. [crates/gwiki/src/falkor_graph/wiki_facts.rs:163-176] |
| `is_external_target` | function | Determines whether a target string represents an external resource by checking if it starts with common external protocol schemes (http, https, mailto, //, \\) or contains a URI scheme marker (://). [crates/gwiki/src/falkor_graph/wiki_facts.rs:178-186] |

