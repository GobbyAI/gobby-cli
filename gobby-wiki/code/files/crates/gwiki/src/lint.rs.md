---
title: crates/gwiki/src/lint.rs
type: code_file
provenance:
- file: crates/gwiki/src/lint.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/lint.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/lint.rs` exposes 55 indexed API symbols.

## How it fits

`crates/gwiki/src/lint.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LintReport` | class | 'LintReport' is a struct that aggregates multiple categories of linting validation issues—including broken links, orphan pages, missing frontmatter, duplicate aliases, missing backlinks, and invalid diagrams—detected within a specified document scope and root directory. [crates/gwiki/src/lint.rs:13-23] |
| `LinkIssue` | class | LinkIssue is a Rust struct that records the location (file path and line number), target reference, and classification type of a detected link-related problem. [crates/gwiki/src/lint.rs:26-31] |
| `DuplicateAlias` | class | 'DuplicateAlias' is a struct that associates a single alias (String) with multiple file system paths (Vec<PathBuf>), representing a duplicate or conflicting alias mapping. [crates/gwiki/src/lint.rs:34-37] |
| `DiagramIssue` | class | 'DiagramIssue' is a public struct that represents a diagram validation error, storing the file path, line number, and reason description for the detected issue. [crates/gwiki/src/lint.rs:45-49] |
| `run` | function | The 'run' function performs static analysis on a wiki vault to identify and report broken cross-references, orphaned pages, and missing frontmatter metadata. [crates/gwiki/src/lint.rs:51-118] |
| `render_text` | function | Formats a 'LintReport' into a text string by aggregating multiple categories of wiki linting issues (broken links, orphan pages, missing frontmatter, duplicate aliases, missing backlinks, and invalid diagrams). [crates/gwiki/src/lint.rs:120-142] |
| `WikiPage` | class | WikiPage is a crate-private struct that represents a wiki document, storing both absolute and relative filesystem paths, raw markdown source, its parsed MarkdownDomainRecord representation, and a frontmatter presence indicator. [crates/gwiki/src/lint.rs:145-151] |
| `collect_pages` | function | Collects markdown files from 'knowledge' and 'code' subdirectories of a vault, parses them with resolved cross-references, sorts by relative path, and returns a vector of structured WikiPage objects or a WikiError. [crates/gwiki/src/lint.rs:153-185] |
| `relative_path` | function | # Summary This function strips a root prefix from a path and returns the resulting relative path as a 'PathBuf', or returns the original path unchanged if the prefix removal fails. [crates/gwiki/src/lint.rs:187-189] |
| `line_number` | function | This function returns the 1-indexed line number corresponding to a specified byte offset in a markdown string by counting all preceding newline characters. [crates/gwiki/src/lint.rs:191-197] |
| `title_for_page` | function | Returns a WikiPage title from its frontmatter metadata, or derives it from the filename stem or relative path as successive fallbacks. [crates/gwiki/src/lint.rs:199-211] |
| `collect_markdown_files` | function | Recursively traverses a directory tree to identify markdown files, parse their YAML frontmatter and content, and populate a mutable vector with 'RawWikiPage' structures containing the parsed metadata and relative paths. [crates/gwiki/src/lint.rs:213-270] |
| `is_markdown_path` | function | Returns 'true' if the provided path has a file extension of "md" or "markdown" (case-insensitive), otherwise returns 'false'. [crates/gwiki/src/lint.rs:272-278] |
| `known_targets` | function | "Aggregates all link targets extracted from each wiki page's relative path and frontmatter into a sorted, deduplicated set." [crates/gwiki/src/lint.rs:280-286] |
| `target_map` | function | This function builds a BTreeMap that associates target identifiers (extracted from each WikiPage's relative path and frontmatter) with the paths of the first pages that define them, using first-occurrence semantics for duplicate targets. [crates/gwiki/src/lint.rs:288-298] |
| `insert_page_targets` | function | Extends a mutable BTreeSet with string targets computed from a relative file path and wiki frontmatter metadata. [crates/gwiki/src/lint.rs:300-306] |
| `page_targets` | function | Returns a vector of normalized wiki link targets constructed from a page's relative file path, filename stem, frontmatter title, and aliases. [crates/gwiki/src/lint.rs:308-322] |
| `ignored_target` | function | This function returns 'true' if the target string represents a non-standard link reference—specifically, if it is a fragment identifier (#), protocol-relative URL (//), UNC path (\\), or contains an explicit URI scheme (mailto:, tel:, ://)—otherwise it returns 'false'. [crates/gwiki/src/lint.rs:324-332] |
| `link_lookup_targets` | function | # Summary 'link_lookup_targets' returns a vector of possible target paths for a wiki link by combining its normalized target with relative path candidates resolved against the page's directory hierarchy, applying type-specific traversal rules (immediate parent for Markdown links, all ancestors for Wikilinks). [crates/gwiki/src/lint.rs:334-363] |
| `normalize_path_components` | function | Normalizes a filesystem path by concatenating 'parent' and 'target' path components, resolving parent directory references ('..') and filtering out empty segments and current directory ('.') entries. [crates/gwiki/src/lint.rs:365-381] |
| `is_orphan_exempt` | function | Returns true if the file's stem (filename without extension) matches one of the predefined exempt filenames (_index, index, home, or readme) in a case-insensitive comparison. [crates/gwiki/src/lint.rs:383-392] |
| `is_backlink_source_exempt` | function | This function returns 'true' if the given file path, after normalizing path separators to forward slashes and stripping the '.md' extension, matches one of five predefined exempt backlink source paths. [crates/gwiki/src/lint.rs:400-411] |
| `duplicate_aliases` | function | This function identifies and returns all aliases that appear across multiple wiki pages, grouping each duplicate alias with the paths of all pages containing it using case-insensitive matching. [crates/gwiki/src/lint.rs:413-432] |
| `missing_backlinks` | function | This function identifies missing reciprocal backlinks by detecting outgoing links from non-exempt source pages that are not reciprocated by their target pages, returning a sorted vector of 'LinkIssue' records. [crates/gwiki/src/lint.rs:434-473] |

_16 more symbol(s) not shown — run `gcode outline crates/gwiki/src/lint.rs` for the full list._

_Verified by 15 in-file unit tests._

