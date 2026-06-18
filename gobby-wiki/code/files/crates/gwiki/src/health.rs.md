---
title: crates/gwiki/src/health.rs
type: code_file
provenance:
- file: crates/gwiki/src/health.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/health.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/health.rs` exposes 55 indexed API symbols.

## How it fits

`crates/gwiki/src/health.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `HealthReport` | class | Indexed class `HealthReport` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:22-34] |
| `HealthSourceIssue` | class | Indexed class `HealthSourceIssue` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:37-41] |
| `DuplicateConcept` | class | Indexed class `DuplicateConcept` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:44-47] |
| `run` | function | Indexed function `run` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:49-53] |
| `inspect` | function | Indexed function `inspect` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:55-95] |
| `render_text` | function | Indexed function `render_text` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:97-106] |
| `persist_report` | function | Indexed function `persist_report` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:108-132] |
| `stale_pages` | function | Indexed function `stale_pages` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:134-142] |
| `page_is_stale` | function | Indexed function `page_is_stale` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:144-169] |
| `stale_after_is_due` | function | Indexed function `stale_after_is_due` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:171-188] |
| `source_citation_is_stale` | function | Indexed function `source_citation_is_stale` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:190-192] |
| `source_citation_is_stale_at` | function | Indexed function `source_citation_is_stale_at` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:194-197] |
| `fetched_at_is_stale` | function | Indexed function `fetched_at_is_stale` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:199-211] |
| `parse_fetched_at` | function | Indexed function `parse_fetched_at` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:213-226] |
| `stale_citation_years` | function | Indexed function `stale_citation_years` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:228-236] |
| `stale_citation_years_from_env` | function | Indexed function `stale_citation_years_from_env` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:238-240] |
| `fetched_year` | function | Indexed function `fetched_year` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:242-247] |
| `approximate_current_year_at` | function | Indexed function `approximate_current_year_at` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:249-253] |
| `load_provenance` | function | Indexed function `load_provenance` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:255-262] |
| `change_triggered_affected_pages` | function | Indexed function `change_triggered_affected_pages` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:265-276] |
| `SourceCitationIndex` | class | Indexed class `SourceCitationIndex` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:279-281] |
| `SourceCitationIndex::cites` | method | Indexed method `SourceCitationIndex::cites` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:284-286] |
| `build_citation_index` | function | Indexed function `build_citation_index` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:289-327] |
| `source_reference_needles` | function | Indexed function `source_reference_needles` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:329-339] |
| `source_reference_patterns` | function | Indexed function `source_reference_patterns` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:341-350] |
| `source_reference_is_present` | function | Indexed function `source_reference_is_present` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:353-360] |
| `markdown_without_fenced_code` | function | Indexed function `markdown_without_fenced_code` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:362-381] |
| `markdown_link_target_matches` | function | Indexed function `markdown_link_target_matches` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:384-386] |
| `bounded_text_matches` | function | Indexed function `bounded_text_matches` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:389-391] |
| `markdown_link_target_pattern` | function | Indexed function `markdown_link_target_pattern` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:393-398] |
| `bounded_text_pattern` | function | Indexed function `bounded_text_pattern` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:400-403] |
| `cached_regex_is_match` | function | Indexed function `cached_regex_is_match` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:406-435] |
| `RegexCache` | class | Indexed class `RegexCache` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:439-441] |
| `RegexCache::get` | method | Indexed method `RegexCache::get` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:445-450] |
| `RegexCache::insert` | method | Indexed method `RegexCache::insert` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:452-458] |
| `source_issue` | function | Indexed function `source_issue` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:461-467] |
| `duplicate_concepts` | function | Indexed function `duplicate_concepts` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:469-489] |
| `render_paths` | function | Indexed function `render_paths` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:491-504] |
| `render_sources` | function | Indexed function `render_sources` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:506-521] |
| `render_broken_links` | function | Indexed function `render_broken_links` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:523-538] |
| `render_duplicate_concepts` | function | Indexed function `render_duplicate_concepts` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:540-560] |
| `health_checks_required_cases` | function | Indexed function `health_checks_required_cases` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:568-611] |
| `inspect_does_not_persist_health_snapshots` | function | Indexed function `inspect_does_not_persist_health_snapshots` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:614-638] |
| `source_reference_matching_skips_code_fences_and_partial_words` | function | Indexed function `source_reference_matching_skips_code_fences_and_partial_words` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:641-654] |
| `citation_index_marks_cited_sources_once_per_page` | function | Indexed function `citation_index_marks_cited_sources_once_per_page` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:657-695] |
| `cached_regex_returns_false_for_malformed_patterns` | function | Indexed function `cached_regex_returns_false_for_malformed_patterns` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:698-700] |
| `stale_after_compares_dates_and_times_to_now` | function | Indexed function `stale_after_compares_dates_and_times_to_now` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:703-712] |
| `regex_cache_touch_updates_lru_order` | function | Indexed function `regex_cache_touch_updates_lru_order` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:715-726] |
| `fenced_code_closes_only_on_matching_delimiter` | function | Indexed function `fenced_code_closes_only_on_matching_delimiter` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:729-735] |
| `fenced_code_requires_matching_marker_length` | function | Indexed function `fenced_code_requires_matching_marker_length` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:738-745] |
| `stale_citation_env_rejects_invalid_values` | function | Indexed function `stale_citation_env_rejects_invalid_values` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:748-753] |
| `stale_citation_uses_full_fetched_timestamp` | function | Indexed function `stale_citation_uses_full_fetched_timestamp` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:756-769] |
| `change_triggered_refresh_health_degrades_to_provenance_only_mapping` | function | Indexed function `change_triggered_refresh_health_degrades_to_provenance_only_mapping` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:772-807] |
| `write_page` | function | Indexed function `write_page` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:809-813] |
| `source_record` | function | Indexed function `source_record` in `crates/gwiki/src/health.rs`. [crates/gwiki/src/health.rs:815-830] |

