---
title: crates/gwiki/src/audit/claims.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit/claims.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit/claims.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/audit/claims.rs` exposes 23 indexed API symbols.

## How it fits

`crates/gwiki/src/audit/claims.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `unsupported_claims` | function | Returns a 'Vec<UnsupportedClaim>' for each claim line in a 'WikiPage' that lacks provenance support, page-level source-span support for structural claims, or inline citation support, populating each result with the page path, line, heading, claim text, a fixed reason, and cloned source context. [crates/gwiki/src/audit/claims.rs:15-44] |
| `claim_source_context` | function | Returns an empty 'Arc<Vec<AuditSourceContext>>' for generated CodeWiki pages, otherwise clones and returns the provided 'source_context'. [crates/gwiki/src/audit/claims.rs:46-55] |
| `is_generated_codewiki_page` | function | Returns 'true' only when the page’s normalized relative path begins with 'code/' and its frontmatter 'trust' field is exactly 'gobby_core::codewiki_contract::TRUST_GENERATED'; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:57-62] |
| `has_codewiki_frontmatter_source_spans` | function | Returns 'true' if the page’s normalized relative path starts with 'code/' and its frontmatter provenance contains at least one value whose source span is classified as code, otherwise 'false'. [crates/gwiki/src/audit/claims.rs:64-73] |
| `frontmatter_value_has_code_source_span` | function | Returns 'true' only when 'value' is a 'Value::Array' containing at least one element for which 'frontmatter_source_has_code_span' returns 'true'; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:75-80] |
| `frontmatter_source_has_code_span` | function | Returns 'true' only when 'value' is a JSON object containing a provenance file string that satisfies 'is_code_source_path' and a provenance ranges array with at least one range for which 'frontmatter_range_is_valid' returns 'true'; otherwise it returns 'false'. [crates/gwiki/src/audit/claims.rs:82-98] |
| `frontmatter_range_is_valid` | function | Returns 'true' if the 'Value' is either a string that satisfies 'is_line_span' or an unsigned integer greater than zero, and 'false' otherwise. [crates/gwiki/src/audit/claims.rs:100-106] |
| `supported_claim_lines` | function | Returns the set of claim line numbers whose optional heading matches a provenance-backed heading on the current page, after normalizing the page path and accepting only headings that either match the page slug or an existing parsed page heading. [crates/gwiki/src/audit/claims.rs:108-145] |
| `ClaimLine` | class | 'ClaimLine' is a package-visible struct that stores a line number, an optional heading, claim text, and an internal 'ClaimKind' discriminator. [crates/gwiki/src/audit/claims.rs:148-153] |
| `ClaimKind` | type | Indexed type `ClaimKind` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:156-159] |
| `claim_lines` | function | It scans a wiki page’s Markdown line by line while tracking byte offsets and suppressing frontmatter, fenced code blocks, HTML comments, headings, thematic breaks, and ignored sections/lines, then emits 'ClaimLine' records for the remaining content after normalizing list-item prefixes. [crates/gwiki/src/audit/claims.rs:166-243] |
| `claim_kind` | function | Returns 'ClaimKind::Structural' when 'is_structural_codewiki_claim(text)' is true, otherwise returns 'ClaimKind::Prose'. [crates/gwiki/src/audit/claims.rs:245-251] |
| `is_structural_codewiki_claim` | function | Returns 'true' if the input, case-insensitively, begins with one of the structural CodeWiki markers 'module:', 'parent:', 'signature:', 'source path:', 'component:', 'components:', or '[[code/'; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:253-262] |
| `heading_title` | function | Returns the non-empty ATX heading text from 'line' by extracting the parsed heading content and returning it as 'Some(String)', or 'None' if the line is not an ATX heading or the heading text is empty. [crates/gwiki/src/audit/claims.rs:264-268] |
| `ignored_claim_section` | function | Returns 'true' only when 'heading' is 'Some' and 'options.ignores_section(heading)' is true; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:270-272] |
| `ignored_claim_line` | function | Returns 'true' when the input line, case-insensitively, begins with 'sources:', 'source path:', 'citation:', or 'citations:', or is exactly '- none recorded.' after ASCII lowercasing. [crates/gwiki/src/audit/claims.rs:274-281] |
| `is_thematic_break` | function | Returns 'true' if 'line', after removing all whitespace, is at least three characters long and consists entirely of one repeated marker character chosen from '-', '*', or '_'; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:283-295] |
| `has_inline_source_support` | function | Returns 'true' if the line, case-insensitively, contains an inline source marker such as '[[knowledge/sources/', '(knowledge/sources/', a code source span, a 'citation:' or 'source:' link-like token, or 'gwiki-source:'. [crates/gwiki/src/audit/claims.rs:297-305] |
| `has_code_source_span` | function | Returns 'true' if 'line' contains any bracketed substring ('[...]') that 'is_code_source_span' accepts, otherwise 'false' after scanning all '['-delimited candidates. [crates/gwiki/src/audit/claims.rs:307-320] |
| `is_code_source_span` | function | Returns 'true' only when 'candidate' splits at the last ':' into a valid code source path and a valid line span, otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:322-327] |
| `is_code_source_path` | function | Returns 'true' only for non-empty, whitespace-free paths that contain either a '/' or '.', and do not contain '://', effectively filtering for likely code source paths rather than URLs or blank/invalid strings. [crates/gwiki/src/audit/claims.rs:329-334] |
| `is_line_span` | function | Returns 'true' if 'span' is either a positive 1-based line number ('usize > 0') or a hyphenated inclusive line range of two parseable 'usize' values with 'start > 0' and 'end >= start', otherwise 'false'. [crates/gwiki/src/audit/claims.rs:336-347] |
| `has_link_like_source_token` | function | Returns 'true' if 'token' appears in 'line' with a non-identifier boundary before it and is immediately followed by a link-like source prefix such as 'http://', 'https://', '[[knowledge/sources/', '[', '(knowledge/sources/', 'knowledge/sources/', or 'gwiki-source:', otherwise 'false'. [crates/gwiki/src/audit/claims.rs:349-371] |

