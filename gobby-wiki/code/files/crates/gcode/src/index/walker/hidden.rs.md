---
title: crates/gcode/src/index/walker/hidden.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/hidden.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/hidden.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Overview

`crates/gcode/src/index/walker/hidden.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/index/walker/hidden.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HiddenPathAllowlist` | class | 'HiddenPathAllowlist' is a 'pub(super)' struct that encapsulates a 'Vec<String>' of path-matching patterns used to define which hidden paths are permitted. [crates/gcode/src/index/walker/hidden.rs:13-15] |
| `HiddenPathAllowlist::load` | method | Builds a hidden-allowlist by cloning the default allowlist patterns, extending them with project-specific patterns read from 'root', and constructing 'Self' from the combined pattern list. [crates/gcode/src/index/walker/hidden.rs:18-25] |
| `HiddenPathAllowlist::from_patterns` | method | Constructs 'Self' by trimming each input pattern, normalizing path separators from '\' to '/', retaining only patterns accepted by 'is_valid_allowlist_pattern', expanding zero-depth globstars, and collecting the resulting patterns into the struct. [crates/gcode/src/index/walker/hidden.rs:27-35] |
| `HiddenPathAllowlist::discover` | method | It expands each configured glob pattern against 'root', filters matching paths to hidden files only, deduplicates them with a 'BTreeSet', and returns the sorted results as a 'Vec<PathBuf>'. [crates/gcode/src/index/walker/hidden.rs:37-53] |
| `HiddenPathAllowlist::matches` | method | It normalizes 'path' to a root-relative, forward-slash-separated string and returns 'true' if any stored glob pattern parses successfully and matches that relative path. [crates/gcode/src/index/walker/hidden.rs:55-63] |
| `read_project_hidden_allowlist` | function | Reads and parses the project config at 'root.join(GCODE_CONFIG_PATH)', returning the 'index.hidden_allowlist' string array as a 'Vec<String>' and falling back to an empty vector on any file read, JSON parse, or field-shape error. [crates/gcode/src/index/walker/hidden.rs:66-80] |
| `is_valid_allowlist_pattern` | function | Returns 'true' only for non-empty, relative path patterns that contain no absolute-path components, parent-directory segments ('..'), or platform-specific prefixes/root components. [crates/gcode/src/index/walker/hidden.rs:82-94] |
| `expand_zero_depth_globstar` | function | Returns a 'Vec<String>' containing the original glob pattern and, if it includes the substring '"/**/"', an additional variant with that segment collapsed to '"/"' to represent the zero-depth match. [crates/gcode/src/index/walker/hidden.rs:96-102] |
| `absolute_glob_pattern` | function | Returns 'None' if 'root' is not valid UTF-8, otherwise returns a glob pattern string formed by escaping the UTF-8 'root' path and concatenating '"/"' plus the provided 'pattern'. [crates/gcode/src/index/walker/hidden.rs:104-107] |
| `is_hidden_path` | function | Returns 'true' if 'path' is either relative to 'root' or used as-is and any of its path components is a UTF-8 name beginning with '.' other than '.' or '..', indicating a hidden path. [crates/gcode/src/index/walker/hidden.rs:109-117] |
| `is_hidden_metadata_content_only` | function | Returns 'true' only for markdown files under '.gobby/plans' or 'gobby-wiki', or for YAML workflow files under '.github/workflows', using 'root' to compute a relative path before checking the normalized path components and extension. [crates/gcode/src/index/walker/hidden.rs:119-145] |
| `is_generated_wiki_metadata` | function | Returns 'true' when 'path' is within the 'gobby-wiki' root and matches a generated metadata location or file pattern ('_meta', '.obsidian', top-level 'wikis.json', '_gwiki' JSON files at depth 3, or any '*.lock' file), otherwise 'false'. [crates/gcode/src/index/walker/hidden.rs:147-178] |
| `path_has_extension` | function | Returns 'true' if 'path' has a UTF-8 file extension that, case-insensitively, matches one of the provided 'extensions', and 'false' otherwise. [crates/gcode/src/index/walker/hidden.rs:180-188] |

