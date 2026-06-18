---
title: crates/gcode/src/commands/codewiki/text/verify.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/verify.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/verify.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

`crates/gcode/src/commands/codewiki/text/verify.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/verify.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VerifyOutcome` | type | Indexed type `VerifyOutcome` in `crates/gcode/src/commands/codewiki/text/verify.rs`. [crates/gcode/src/commands/codewiki/text/verify.rs:16-28] |
| `verify_and_strip` | function | Attempts to verify block-level text against source excerpts via an optional 'TextVerifier', returning 'Skipped' when verification is unavailable or no blocks exist, 'Unusable' on malformed verifier output or when all blocks are stripped, and otherwise 'Verified' with the original or survivor text plus a 'degraded' flag indicating whether unsupported blocks were removed. [crates/gcode/src/commands/codewiki/text/verify.rs:36-71] |
| `split_blocks` | function | Splits the input string on double-newline paragraph boundaries, trims each resulting block, filters out empty blocks, and returns the remaining blocks as owned 'String's. [crates/gcode/src/commands/codewiki/text/verify.rs:76-82] |
| `parse_unsupported_ids` | function | Extracts the first bracketed JSON array from 'response', parses it as 'Vec<i64>', keeps only values that convert to 'usize' and fall within '1..=block_count', then returns the sorted deduplicated IDs or 'None' on any parse/format failure. [crates/gcode/src/commands/codewiki/text/verify.rs:88-100] |
| `strip_blocks` | function | Returns a single string formed by concatenating all 'blocks' whose 1-based positions are not listed in 'unsupported', joining the retained block strings with double newlines. [crates/gcode/src/commands/codewiki/text/verify.rs:104-112] |
| `sources` | function | Returns a 'Vec<SourceExcerpt>' containing a single excerpt entry for 'src/lib.rs' lines '1..=4' with the excerpt text 'pub fn run() {}'. [crates/gcode/src/commands/codewiki/text/verify.rs:119-126] |
| `split_blocks_separates_on_blank_lines` | function | Verifies that 'split_blocks' splits a string into separate blocks at blank lines, returning each non-empty paragraph as an element. [crates/gcode/src/commands/codewiki/text/verify.rs:129-132] |
| `parse_unsupported_ids_reads_json_array` | function | Tests that 'parse_unsupported_ids' extracts a JSON array of unsupported IDs from surrounding text, returns it as 'Some(Vec<u32>)', and discards out-of-range or duplicate entries. [crates/gcode/src/commands/codewiki/text/verify.rs:135-142] |
| `parse_unsupported_ids_rejects_garbage` | function | Verifies that 'parse_unsupported_ids' returns 'None' for non-parseable input, including arbitrary text, an empty string, and a malformed list literal. [crates/gcode/src/commands/codewiki/text/verify.rs:145-149] |
| `strip_blocks_drops_only_listed_ids` | function | Verifies that 'strip_blocks' removes only the block IDs explicitly listed, preserving all other blocks and returning the original text unchanged when the ID list is empty. [crates/gcode/src/commands/codewiki/text/verify.rs:152-156] |
| `verify_strips_planted_unsupported_block` | function | Tests that 'verify_and_strip' removes a verifier-flagged unsupported text block from the page output, returns 'Verified', and marks the result as degraded while preserving grounded content. [crates/gcode/src/commands/codewiki/text/verify.rs:159-172] |
| `verify_keeps_fully_supported_page_undegraded` | function | Verifies that 'verify_and_strip' returns 'VerifyOutcome::Verified' without marking degradation and preserves the input text unchanged when the page is fully supported and the verifier returns no stripped spans. [crates/gcode/src/commands/codewiki/text/verify.rs:175-189] |
| `verify_skips_when_verifier_unavailable` | function | Asserts that 'verify_and_strip' yields 'VerifyOutcome::Skipped' when the optional verifier is present but its model call returns 'None', indicating the verifier is unavailable. [crates/gcode/src/commands/codewiki/text/verify.rs:192-201] |
| `verify_skips_when_no_verifier_configured` | function | Asserts that 'verify_and_strip' returns 'VerifyOutcome::Skipped' when no 'TextVerifier' is configured, even if the input text contains a grounded claim. [crates/gcode/src/commands/codewiki/text/verify.rs:204-211] |
| `verify_reports_garbage_verdict_as_unusable` | function | Asserts that 'verify_and_strip' returns 'VerifyOutcome::Unusable' when a text verifier produces a non-supporting “looks fine” verdict for grounded-claim content. [crates/gcode/src/commands/codewiki/text/verify.rs:214-222] |
| `verify_reports_total_strip_as_unusable` | function | Tests that 'verify_and_strip' returns 'VerifyOutcome::Unusable' when the verifier marks every text block as claimed, leaving no surviving content. [crates/gcode/src/commands/codewiki/text/verify.rs:225-234] |

