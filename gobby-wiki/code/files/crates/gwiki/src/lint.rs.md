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

`crates/gwiki/src/lint.rs` exposes 36 indexed API symbols.

## How it fits

`crates/gwiki/src/lint.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `LintReport` | class | 'LintReport' is a structured linting results container that records the executed command, checked scope and root path, and collections of detected documentation issues such as broken links, orphan pages, missing frontmatter, duplicate aliases, and missing backlinks. [crates/gwiki/src/lint.rs:13-22] |
| `LinkIssue` | class | 'LinkIssue' is a struct that represents a link-related problem by storing the source 'path', the 1-based 'line' where it occurs, the link 'target', and a string 'kind' categorizing the issue. [crates/gwiki/src/lint.rs:25-30] |
| `DuplicateAlias` | class | 'DuplicateAlias' is a struct that records a duplicated alias string together with the set of filesystem paths associated with that alias. [crates/gwiki/src/lint.rs:33-36] |
| `run` | function | Scans all pages under 'vault_root' for the given 'scope', resolves and validates links against the page target map, and builds a 'LintReport' containing broken links, orphan pages, missing frontmatter, and other page-structure issues. [crates/gwiki/src/lint.rs:38-103] |
| `render_text` | function | Formats a 'LintReport' into a plain-text wiki lint report string by emitting the scope header and appending sections for broken links, orphan pages, missing frontmatter, duplicate aliases, and missing backlinks. [crates/gwiki/src/lint.rs:105-126] |
| `WikiPage` | class | 'WikiPage' is a crate-visible data container representing a wiki page’s file paths, raw Markdown content, parsed 'MarkdownDomainRecord', and a flag indicating whether frontmatter was present. [crates/gwiki/src/lint.rs:129-135] |
| `collect_pages` | function | Recursively collects markdown files under 'vault_root/knowledge' and 'vault_root/code', sorts them by relative path, parses each page against the set of known targets, and returns a 'Vec<WikiPage>' or a 'WikiError' if file collection or markdown parsing fails. [crates/gwiki/src/lint.rs:137-169] |
| `relative_path` | function | Returns 'path' with the 'root' prefix removed when 'path' starts with 'root', otherwise returns 'path' unchanged as a 'PathBuf'. [crates/gwiki/src/lint.rs:171-173] |
| `line_number` | function | Returns the 1-based line number containing 'byte_start' by counting '\n' bytes in 'markdown[..min(byte_start, markdown.len())]' and adding 1. [crates/gwiki/src/lint.rs:175-181] |
| `title_for_page` | function | Returns the page title from frontmatter 'title' if present, otherwise falls back to the file stem of 'page.path', and finally to the display string of 'page.relative_path' if no stem is available. [crates/gwiki/src/lint.rs:183-195] |
| `collect_markdown_files` | function | Recursively traverses 'directory' under 'vault_root', reads each Markdown file, parses its frontmatter, computes its relative path, and appends a 'RawWikiPage' to 'pages', returning 'Ok(())' for missing directories and wrapping I/O or frontmatter parse failures in 'WikiError'. [crates/gwiki/src/lint.rs:197-254] |
| `is_markdown_path` | function | Returns 'true' when the path has an extension that, after UTF-8 conversion and case-insensitive normalization, is exactly 'md' or 'markdown', and 'false' otherwise. [crates/gwiki/src/lint.rs:256-262] |
| `known_targets` | function | Builds and returns a 'BTreeSet<String>' of all targets extracted from each 'RawWikiPage' by calling 'insert_page_targets' with the page’s 'relative_path' and 'frontmatter'. [crates/gwiki/src/lint.rs:264-270] |
| `target_map` | function | Builds a 'BTreeMap' from each target string returned by 'page_targets' for the given pages to the first 'relative_path' that declares it, preserving the earliest page encountered for duplicate targets. [crates/gwiki/src/lint.rs:272-282] |
| `insert_page_targets` | function | 'insert_page_targets' computes the page-target strings for 'relative_path' and 'frontmatter' via 'page_targets' and inserts them into the mutable 'BTreeSet<String>' 'targets' by extending the set with the returned iterator. [crates/gwiki/src/lint.rs:284-290] |
| `page_targets` | function | 'page_targets' builds and returns a list of normalized wiki target strings derived from the page’s relative path, its file stem, the frontmatter title if present, and all frontmatter aliases. [crates/gwiki/src/lint.rs:292-306] |
| `ignored_target` | function | Returns 'true' when the trimmed 'target' string looks like an ignored link or reference, namely if it starts with '#', '//', '\\\\', 'mailto:', or 'tel:', or contains '://'; otherwise returns 'false'. [crates/gwiki/src/lint.rs:308-316] |
| `link_lookup_targets` | function | Returns a deduplicated list of candidate lookup paths for a wiki link, starting with its normalized target and, for Markdown or Wikilink targets outside reserved namespaces and not absolute, adding normalized resolutions relative to each parent directory of the current page. [crates/gwiki/src/lint.rs:318-347] |
| `normalize_path_components` | function | Returns a slash-separated path string formed by concatenating 'parent' and 'target', removing empty and '.' segments and resolving '..' by popping the previous component when possible. [crates/gwiki/src/lint.rs:349-365] |
| `is_orphan_exempt` | function | Returns 'true' when the path’s filename stem, interpreted as UTF-8 and case-folded to ASCII lowercase, is exactly '_index', 'index', 'home', or 'readme'; otherwise it returns 'false'. [crates/gwiki/src/lint.rs:367-376] |
| `is_backlink_source_exempt` | function | Returns 'true' when the normalized path, with backslashes converted to slashes and a trailing '.md' removed, exactly matches one of the exempt backlink source paths under 'code/', and 'false' otherwise. [crates/gwiki/src/lint.rs:384-395] |
| `duplicate_aliases` | function | Collects frontmatter aliases from all pages, normalizes them by trimming and case-folding to lowercase, groups the page paths for each alias, sorts each path list, and returns only aliases that appear on more than one page as 'DuplicateAlias' records. [crates/gwiki/src/lint.rs:397-416] |
| `missing_backlinks` | function | 'missing_backlinks' builds a title map for wiki pages, scans each non-exempt page’s outgoing links, and returns a sorted 'Vec<LinkIssue>' for every target that does not contain a reciprocal link back to the source, using the source page title as the issue target. [crates/gwiki/src/lint.rs:418-457] |
| `link_kind` | function | Returns the static string '"wikilink"' for 'LinkKind::Wikilink' and '"markdown"' for 'LinkKind::Markdown'. [crates/gwiki/src/lint.rs:459-464] |
| `render_link_issues` | function | Appends a headed newline-delimited report of 'LinkIssue' entries to 'text', writing '- none' when the slice is empty and otherwise formatting each issue as 'path:line -> target (kind)'. [crates/gwiki/src/lint.rs:466-485] |
| `render_paths` | function | Appends a newline, the given 'heading' followed by ':\n', and then either '- none\n' if 'paths' is empty or one '- <display path>\n' line per 'PathBuf' to 'text'. [crates/gwiki/src/lint.rs:487-500] |
| `join_paths` | function | Converts each 'PathBuf' in 'paths' to its display string, collects them into a vector, and returns the strings joined into a single comma-separated 'String'. [crates/gwiki/src/lint.rs:502-508] |
| `RawWikiPage` | class | 'RawWikiPage' is a data-only struct representing an untrusted wiki page payload with its absolute and relative paths, markdown content, parsed 'WikiFrontmatter', and a flag indicating whether frontmatter was present. [crates/gwiki/src/lint.rs:511-517] |
| `detects_broken_links_and_orphans` | function | Creates a temporary knowledge tree and verifies that 'run(..., ScopeIdentity::topic("ops"))' reports two broken links from 'knowledge/topics/home.md' ('`[[Missing]]`' and '`[gone](missing.md)`') and one orphan page ('knowledge/topics/orphan.md') with no inbound links. [crates/gwiki/src/lint.rs:524-556] |
| `nested_wikilinks_resolve_relative_to_current_subtree` | function | Creates two markdown pages with nested wikilinks and verifies that a relative link inside 'code/modules/crates.md' resolves correctly to 'code/repo.md' within the current subtree, producing no broken links in the lint report. [crates/gwiki/src/lint.rs:559-576] |
| `relative_markdown_links_clamp_traversal_at_vault_root` | function | Verifies that 'normalize_path_components' clamps '..' traversal at the vault root, so '"knowledge/topics"' combined with '"../../../outside.md"' normalizes to '"outside.md"'. [crates/gwiki/src/lint.rs:579-584] |
| `ignored_target_skips_external_network_references` | function | Verifies that 'ignored_target' returns 'true' for external network references such as '//'-prefixed CDN paths, UNC paths, and 'https://' URLs, and 'false' for a normal relative file path. [crates/gwiki/src/lint.rs:587-592] |
| `lint_is_read_only` | function | Verifies that running the linter on a topic-scoped workspace does not modify the source page and does not create 'meta/health/latest.json', i.e. the lint pass is read-only. [crates/gwiki/src/lint.rs:595-611] |
| `navigation_root_links_are_exempt_from_missing_backlinks` | function | Verifies that a navigation-root page linking to a content page that does not link back does not produce any 'missing_backlinks' lint findings. [crates/gwiki/src/lint.rs:614-638] |
| `content_page_links_still_require_reciprocity` | function | Verifies that a non-navigation content page under 'code/' is still reported for a missing reciprocal backlink when it is linked to by another page, producing one 'missing_backlink' issue for 'code/narrative/architecture.md' targeting 'Introduction'. [crates/gwiki/src/lint.rs:641-669] |
| `write_page` | function | Creates the target page path by joining 'root' with 'relative', ensures its parent directory exists with 'create_dir_all', and writes 'markdown' to the file, panicking on any I/O failure. [crates/gwiki/src/lint.rs:671-675] |

