---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/text.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `span` | function | Constructs and returns a 'SourceSpan' by converting 'file' into a 'String' and populating its 'file', 'line_start', and 'line_end' fields with the provided arguments. [crates/gcode/src/commands/codewiki/text.rs:51-57] |
| `frontmatter_coalesces_contiguous_provenance_ranges` | function | Verifies that 'frontmatter' merges contiguous provenance spans on the same file into compact line ranges in the generated document, preserving non-contiguous single-line entries separately. [crates/gcode/src/commands/codewiki/text.rs:60-79] |
| `citation_list_emits_one_fallback_range_per_line` | function | Verifies that 'citation_list(&spans, "")' emits exactly one citation line per input span, with each line matching 'span.citation()' for the corresponding span. [crates/gcode/src/commands/codewiki/text.rs:82-102] |
| `citation_list_caps_oversized_span_sets` | function | Verifies that 'citation_list' truncates an oversized set of 200 spans to exactly 'MAX_FALLBACK_CITATIONS' output lines when given an empty query string. [crates/gcode/src/commands/codewiki/text.rs:105-117] |
| `fallback_spans_prefer_distinct_files_over_one_files_span_run` | function | Verifies that 'fallback_spans' caps the result at 'MAX_FALLBACK_CITATIONS' and, when given many spans from one file plus a span from another file, includes at least one span from the distinct file ('src/other.rs'). [crates/gcode/src/commands/codewiki/text.rs:120-133] |
| `citation_markers_are_capped_and_keep_reference_numbering` | function | Verifies that 'citation_markers' truncates an oversized span list to 'MAX_FALLBACK_CITATIONS' markers while preserving the original numbering sequence starting at '[1]'. [crates/gcode/src/commands/codewiki/text.rs:136-149] |
| `fallback_citations_rank_lexically_relevant_files_first` | function | It verifies that 'fallback_spans' ranks candidate citation spans by lexical relevance to the query text, selecting 'src/parser.rs' first over unrelated files. [crates/gcode/src/commands/codewiki/text.rs:152-162] |
| `asset_data_files_rank_behind_source_unless_sole_provenance` | function | Verifies that 'fallback_spans' prefers source-file spans over 'assets/data.json' spans when both are present, but returns the asset span when it is the only available provenance. [crates/gcode/src/commands/codewiki/text.rs:165-176] |
| `frontmatter_caps_provenance_and_records_truncation` | function | Verifies that 'frontmatter' enforces the provenance-file cap by truncating excess source files while preserving the busiest file’s spans, emits the correct 'provenance_truncated: 8' marker for the overflow, and does not add truncation metadata when all provenance records fit within a single file. [crates/gcode/src/commands/codewiki/text.rs:179-211] |
| `references_resolve_only_markers_present_in_doc` | function | Verifies that 'write_references' appends only the reference entries for citation markers actually present in the document text, preserving their numeric order ('[2]' then '[17]') and ignoring unused spans. [crates/gcode/src/commands/codewiki/text.rs:214-229] |
| `wrap_citation_items_bounds_line_width` | function | It verifies that 'wrap_citation_items' wraps a sequence of citation strings into multiple lines when constrained to width 40, and that every resulting line is at most 40 characters long. [crates/gcode/src/commands/codewiki/text.rs:232-239] |
| `prompt_echo_is_rejected_as_failed_generation` | function | Verifies that 'maybe_generate' treats a model output that exactly echoes the prompt as a failed generation, while accepting a non-echoed response as 'Generation::Generated'. [crates/gcode/src/commands/codewiki/text.rs:242-275] |
| `short_prompts_never_trigger_echo_rejection` | function | Verifies that 'is_prompt_echo' returns 'false' when given the exact short prompt string '"Short prompt."'. [crates/gcode/src/commands/codewiki/text.rs:278-281] |
| `transport_failure` | function | Constructs and returns an 'AiError::TransportFailure' with 'status' and 'body' set to 'None' and 'source' set to '"connection reset"'. [crates/gcode/src/commands/codewiki/text.rs:283-289] |
| `bounded_retry_recovers_from_transient_transport_failure` | function | Verifies that 'generate_with_bounded_retry' retries once after an initial transient transport failure and then returns the successful '"generated"' result on the second call. [crates/gcode/src/commands/codewiki/text.rs:292-305] |
| `bounded_retry_gives_up_after_bounded_attempts` | function | Verifies that 'generate_with_bounded_retry' stops after the configured number of retry attempts, returns an 'Err', and invokes the closure exactly '1 + GENERATION_RETRY_BACKOFF.len()' times. [crates/gcode/src/commands/codewiki/text.rs:308-317] |
| `bounded_retry_fails_fast_on_non_transient_errors` | function | Verifies that 'generate_with_bounded_retry' returns the first 'AiError::NotConfigured' immediately without retrying, leaving the closure invoked exactly once. [crates/gcode/src/commands/codewiki/text.rs:320-332] |

