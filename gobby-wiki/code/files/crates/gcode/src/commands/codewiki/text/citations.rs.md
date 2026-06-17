---
title: crates/gcode/src/commands/codewiki/text/citations.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/citations.rs
  ranges:
  - 26-34
  - 38-44
  - 46-51
  - 58-98
  - 100-106
  - 108-128
  - 130-142
  - 144-153
  - 155-161
  - 166-179
  - 181-197
  - 199-225
  - 227-244
  - 246-259
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/text/citations.rs:26-34](crates/gcode/src/commands/codewiki/text/citations.rs#L26-L34), [crates/gcode/src/commands/codewiki/text/citations.rs:38-44](crates/gcode/src/commands/codewiki/text/citations.rs#L38-L44), [crates/gcode/src/commands/codewiki/text/citations.rs:46-51](crates/gcode/src/commands/codewiki/text/citations.rs#L46-L51), [crates/gcode/src/commands/codewiki/text/citations.rs:58-98](crates/gcode/src/commands/codewiki/text/citations.rs#L58-L98), [crates/gcode/src/commands/codewiki/text/citations.rs:100-106](crates/gcode/src/commands/codewiki/text/citations.rs#L100-L106), [crates/gcode/src/commands/codewiki/text/citations.rs:108-128](crates/gcode/src/commands/codewiki/text/citations.rs#L108-L128), [crates/gcode/src/commands/codewiki/text/citations.rs:130-142](crates/gcode/src/commands/codewiki/text/citations.rs#L130-L142), [crates/gcode/src/commands/codewiki/text/citations.rs:144-153](crates/gcode/src/commands/codewiki/text/citations.rs#L144-L153), [crates/gcode/src/commands/codewiki/text/citations.rs:155-161](crates/gcode/src/commands/codewiki/text/citations.rs#L155-L161), [crates/gcode/src/commands/codewiki/text/citations.rs:166-179](crates/gcode/src/commands/codewiki/text/citations.rs#L166-L179), [crates/gcode/src/commands/codewiki/text/citations.rs:181-197](crates/gcode/src/commands/codewiki/text/citations.rs#L181-L197), [crates/gcode/src/commands/codewiki/text/citations.rs:199-225](crates/gcode/src/commands/codewiki/text/citations.rs#L199-L225), [crates/gcode/src/commands/codewiki/text/citations.rs:227-244](crates/gcode/src/commands/codewiki/text/citations.rs#L227-L244), [crates/gcode/src/commands/codewiki/text/citations.rs:246-259](crates/gcode/src/commands/codewiki/text/citations.rs#L246-L259)

</details>

# crates/gcode/src/commands/codewiki/text/citations.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Purpose

Implements citation handling for codewiki text generation: it scores source spans against generated prose, prefers representative fallback citations from distinct source files, and deprioritizes asset/data files unless they are the only provenance available. It also builds citation lists, wraps and replaces inline citations with markers, writes a references section, grounds text against available spans, and strips or validates malformed citations by parsing citation parts and checking whether any valid citation remains.
[crates/gcode/src/commands/codewiki/text/citations.rs:26-34]
[crates/gcode/src/commands/codewiki/text/citations.rs:38-44]
[crates/gcode/src/commands/codewiki/text/citations.rs:46-51]
[crates/gcode/src/commands/codewiki/text/citations.rs:58-98]
[crates/gcode/src/commands/codewiki/text/citations.rs:100-106]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `is_asset_or_data_file` | function | `fn is_asset_or_data_file(file: &str) -> bool {` | `is_asset_or_data_file [function]` | `fa943380-0501-5373-a714-5ab4987af8b7` | 26-34 [crates/gcode/src/commands/codewiki/text/citations.rs:26-34] | Indexed function `is_asset_or_data_file` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:26-34] |
| `lexical_tokens` | function | `fn lexical_tokens(value: &str) -> BTreeSet<String> {` | `lexical_tokens [function]` | `c02cf790-b9de-5278-9fa8-5777daa87eca` | 38-44 [crates/gcode/src/commands/codewiki/text/citations.rs:38-44] | Indexed function `lexical_tokens` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:38-44] |
| `citation_relevance` | function | `fn citation_relevance(text_tokens: &BTreeSet<String>, file: &str) -> usize {` | `citation_relevance [function]` | `a4e632c0-3e80-5fc7-90c3-616b20540091` | 46-51 [crates/gcode/src/commands/codewiki/text/citations.rs:46-51] | Indexed function `citation_relevance` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:46-51] |
| `fallback_spans` | function | `pub(super) fn fallback_spans(spans: &[SourceSpan], text: &str) -> Vec<SourceSpan> {` | `fallback_spans [function]` | `ba5263ac-e540-51e0-a016-a88d65285fb9` | 58-98 [crates/gcode/src/commands/codewiki/text/citations.rs:58-98] | Indexed function `fallback_spans` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:58-98] |
| `citation_list` | function | `pub(crate) fn citation_list(spans: &[SourceSpan], text: &str) -> String {` | `citation_list [function]` | `3259ccdb-4bbb-5ca5-8a94-1672a0888c7e` | 100-106 [crates/gcode/src/commands/codewiki/text/citations.rs:100-106] | Indexed function `citation_list` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:100-106] |
| `wrap_citation_items` | function | `pub(super) fn wrap_citation_items<I>(items: I, max_line_width: usize) -> String` | `wrap_citation_items [function]` | `d14e37d2-ce3c-533e-9bf7-ebb42cef4aa2` | 108-128 [crates/gcode/src/commands/codewiki/text/citations.rs:108-128] | Indexed function `wrap_citation_items` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:108-128] |
| `citation_markers` | function | `pub(crate) fn citation_markers(spans: &[SourceSpan], text: &str) -> String {` | `citation_markers [function]` | `1bd8f5f4-499b-5e57-b8e6-55e2a27e6bd7` | 130-142 [crates/gcode/src/commands/codewiki/text/citations.rs:130-142] | Indexed function `citation_markers` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:130-142] |
| `citation_references` | function | `fn citation_references(spans: &[SourceSpan]) -> Vec<(usize, String)> {` | `citation_references [function]` | `2da98224-d432-58ca-b667-5d59e63082e4` | 144-153 [crates/gcode/src/commands/codewiki/text/citations.rs:144-153] | Indexed function `citation_references` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:144-153] |
| `replace_citations_with_markers` | function | `pub(crate) fn replace_citations_with_markers(text: &str, spans: &[SourceSpan]) -> String {` | `replace_citations_with_markers [function]` | `88b1c0c3-5b9a-544c-8f02-85353cbd72ef` | 155-161 [crates/gcode/src/commands/codewiki/text/citations.rs:155-161] | Indexed function `replace_citations_with_markers` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:155-161] |
| `write_references` | function | `pub(crate) fn write_references(doc: &mut String, spans: &[SourceSpan]) {` | `write_references [function]` | `c2f3f5c4-e3cf-5a98-9300-273ba3e26af1` | 166-179 [crates/gcode/src/commands/codewiki/text/citations.rs:166-179] | Indexed function `write_references` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:166-179] |
| `ground_text` | function | `pub(crate) fn ground_text(` | `ground_text [function]` | `8ca67329-d972-5fbf-9ff1-927845074c11` | 181-197 [crates/gcode/src/commands/codewiki/text/citations.rs:181-197] | Indexed function `ground_text` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:181-197] |
| `strip_invalid_citations` | function | `fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {` | `strip_invalid_citations [function]` | `c52bbeb5-443f-5293-9ee1-d48ed1c4eb91` | 199-225 [crates/gcode/src/commands/codewiki/text/citations.rs:199-225] | Indexed function `strip_invalid_citations` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:199-225] |
| `contains_valid_citation` | function | `fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {` | `contains_valid_citation [function]` | `0dc90579-6e54-5bc4-964e-47624afcd042` | 227-244 [crates/gcode/src/commands/codewiki/text/citations.rs:227-244] | Indexed function `contains_valid_citation` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:227-244] |
| `citation_parts` | function | `fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {` | `citation_parts [function]` | `c26c2e95-c4af-53b5-8b8e-106e5065ccc1` | 246-259 [crates/gcode/src/commands/codewiki/text/citations.rs:246-259] | Indexed function `citation_parts` in `crates/gcode/src/commands/codewiki/text/citations.rs`. [crates/gcode/src/commands/codewiki/text/citations.rs:246-259] |
