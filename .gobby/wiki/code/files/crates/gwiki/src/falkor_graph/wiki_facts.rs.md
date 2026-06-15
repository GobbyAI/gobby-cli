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

# crates/gwiki/src/falkor_graph/wiki_facts.rs

Module: [[code/modules/crates/gwiki/src/falkor_graph|crates/gwiki/src/falkor_graph]]

## Purpose

This file loads wiki graph data from FalkorDB for a given `SearchScope` and turns it into `WikiGraphFacts`. It queries `gwiki_documents` to build `WikiGraphDocument` records, derives lookup structures from their paths and slugified titles, then queries `gwiki_links` and resolves each raw link target into either a concrete internal destination or an unresolved target. The helper functions handle target classification and normalization: they reject external or empty links, normalize relative path-like targets against the source page, map title slugs to document paths, and compare candidates against known document paths to decide whether a link can be resolved.
[crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161]

## API Symbols

- `load_wiki_graph_facts` (function) component `load_wiki_graph_facts [function]` (`4d60aa47-5986-548d-9cae-f94257e97305`) lines 13-98 [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
  - Signature: `pub(crate) fn load_wiki_graph_facts(`
  - Purpose: Loads all 'gwiki_documents' and 'gwiki_links' rows for the given 'SearchScope', converts them into 'WikiGraphDocument' and resolved 'WikiGraphLink' values, and returns them as 'WikiGraphFacts' or a configuration error if either query fails. [crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
- `resolve_graph_target` (function) component `resolve_graph_target [function]` (`0f96a6b2-3f9f-54e1-8a93-55d3dacff49b`) lines 100-132 [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132]
  - Signature: `pub(super) fn resolve_graph_target(`
  - Purpose: Resolves an internal graph-link target by trimming, rejecting external or empty targets, stripping fragments and normalizing separators, resolving the path relative to 'source_path', returning a 'Resolved' path if it matches 'document_paths' or a slug lookup in 'slug_targets', and otherwise returning 'Unresolved(lookup)'. [crates/gwiki/src/falkor_graph/wiki_facts.rs:100-132]
- `slug_target_map` (function) component `slug_target_map [function]` (`0db8eae8-81ba-5f42-a87b-1811ef91f66e`) lines 134-142 [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142]
  - Signature: `pub(super) fn slug_target_map(documents: &[WikiGraphDocument]) -> BTreeMap<String, PathBuf> {`
  - Purpose: Builds a 'BTreeMap' from each document’s slugified title to its cloned 'PathBuf', skipping any 'WikiGraphDocument' without a title. [crates/gwiki/src/falkor_graph/wiki_facts.rs:134-142]
- `resolve_relative_graph_path` (function) component `resolve_relative_graph_path [function]` (`d6ff3e27-e967-5741-bce2-edc03a5634ae`) lines 144-157 [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157]
  - Signature: `fn resolve_relative_graph_path(raw_target: &str, source_path: &Path) -> String {`
  - Purpose: Returns an absolute, normalized, forward-slash path for a relative graph target by resolving it against 'source_path'’s parent directory, while leaving already-absolute or non-path-like targets unchanged except for stripping a leading '/'. [crates/gwiki/src/falkor_graph/wiki_facts.rs:144-157]
- `is_path_like_target` (function) component `is_path_like_target [function]` (`663ec667-9918-525d-a4dc-74935a3d965b`) lines 159-161 [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161]
  - Signature: `fn is_path_like_target(target: &str) -> bool {`
  - Purpose: Returns 'true' if 'target' contains a '/', starts with '.', or ends with '.md', and 'false' otherwise. [crates/gwiki/src/falkor_graph/wiki_facts.rs:159-161]
- `normalize_path` (function) component `normalize_path [function]` (`b07ea7cf-e4ea-5736-a222-440a89520e01`) lines 163-176 [crates/gwiki/src/falkor_graph/wiki_facts.rs:163-176]
  - Signature: `fn normalize_path(path: PathBuf) -> PathBuf {`
  - Purpose: Constructs a new 'PathBuf' by iterating the input path’s components, discarding '.' and root/prefix segments, resolving '..' by popping the last normalized segment, and pushing all normal path segments in order. [crates/gwiki/src/falkor_graph/wiki_facts.rs:163-176]
- `is_external_target` (function) component `is_external_target [function]` (`a0c822d1-8b52-5757-8738-840ac6a1b723`) lines 178-186 [crates/gwiki/src/falkor_graph/wiki_facts.rs:178-186]
  - Signature: `fn is_external_target(target: &str) -> bool {`
  - Purpose: Returns 'true' if 'target' looks like an external URL or network reference by checking for 'http://', 'https://', 'mailto:', protocol-relative '//', a Windows UNC path prefix '\\', or any substring '://' (case-insensitive for the scheme prefixes). [crates/gwiki/src/falkor_graph/wiki_facts.rs:178-186]

