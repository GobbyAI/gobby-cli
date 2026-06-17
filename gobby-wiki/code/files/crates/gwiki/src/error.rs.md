---
title: crates/gwiki/src/error.rs
type: code_file
provenance:
- file: crates/gwiki/src/error.rs
  ranges:
  - 10-66
  - 69-86
  - 88-99
  - 103-158
  - 161-176
  - 179-189
  - 193-195
  - 199-201
  - 205-207
  - 216-227
  - 230-240
  - 243-254
  - 257-275
  - 278-287
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/error.rs:10-66](crates/gwiki/src/error.rs#L10-L66), [crates/gwiki/src/error.rs:69-86](crates/gwiki/src/error.rs#L69-L86), [crates/gwiki/src/error.rs:88-99](crates/gwiki/src/error.rs#L88-L99), [crates/gwiki/src/error.rs:103-158](crates/gwiki/src/error.rs#L103-L158), [crates/gwiki/src/error.rs:161-176](crates/gwiki/src/error.rs#L161-L176), [crates/gwiki/src/error.rs:179-189](crates/gwiki/src/error.rs#L179-L189), [crates/gwiki/src/error.rs:193-195](crates/gwiki/src/error.rs#L193-L195), [crates/gwiki/src/error.rs:199-201](crates/gwiki/src/error.rs#L199-L201), [crates/gwiki/src/error.rs:205-207](crates/gwiki/src/error.rs#L205-L207), [crates/gwiki/src/error.rs:216-227](crates/gwiki/src/error.rs#L216-L227), [crates/gwiki/src/error.rs:230-240](crates/gwiki/src/error.rs#L230-L240), [crates/gwiki/src/error.rs:243-254](crates/gwiki/src/error.rs#L243-L254), [crates/gwiki/src/error.rs:257-275](crates/gwiki/src/error.rs#L257-L275), [crates/gwiki/src/error.rs:278-287](crates/gwiki/src/error.rs#L278-L287)

</details>

# crates/gwiki/src/error.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the `WikiError` enum for the wiki crate, centralizing all error cases the crate can emit, from config and I/O failures to index, search, daemon, and setup errors. Its helpers map each variant to a stable error code, detect the special “ffmpeg unavailable” case, format user-facing messages, preserve underlying sources, and provide `From` conversions from wrapped error types. The tests verify that typed sources are retained, codes stay specific, timeout errors remain structured, and ffmpeg-unavailable detection works for both config and I/O paths.
[crates/gwiki/src/error.rs:10-66]
[crates/gwiki/src/error.rs:69-86]
[crates/gwiki/src/error.rs:88-99]
[crates/gwiki/src/error.rs:103-158]
[crates/gwiki/src/error.rs:161-176]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `WikiError` | type | `pub enum WikiError {` | `WikiError [type]` | `112c956a-2044-535b-aa5d-1b7fbc26685e` | 10-66 [crates/gwiki/src/error.rs:10-66] | Indexed type `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:10-66] |
| `WikiError::code` | method | `pub fn code(&self) -> &'static str {` | `WikiError::code [method]` | `11d4afc8-edd8-5799-8252-62ffa09b2fab` | 69-86 [crates/gwiki/src/error.rs:69-86] | Indexed method `WikiError::code` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:69-86] |
| `WikiError::is_ffmpeg_unavailable` | method | `pub(crate) fn is_ffmpeg_unavailable(&self) -> bool {` | `WikiError::is_ffmpeg_unavailable [method]` | `4b4b7188-29cd-5935-b1eb-edffdc4defa9` | 88-99 [crates/gwiki/src/error.rs:88-99] | Indexed method `WikiError::is_ffmpeg_unavailable` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:88-99] |
| `WikiError::fmt` | method | `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {` | `WikiError::fmt [method]` | `b0574737-29da-5369-9dec-730dff09cfe0` | 103-158 [crates/gwiki/src/error.rs:103-158] | Indexed method `WikiError::fmt` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:103-158] |
| `format_action_error` | function | `fn format_action_error(` | `format_action_error [function]` | `e73af4e6-78a4-59db-9fad-9001e79bd22f` | 161-176 [crates/gwiki/src/error.rs:161-176] | Indexed function `format_action_error` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:161-176] |
| `WikiError::source` | method | `fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {` | `WikiError::source [method]` | `2c6dd5af-a233-54a8-95a5-f3ddd63fbb80` | 179-189 [crates/gwiki/src/error.rs:179-189] | Indexed method `WikiError::source` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:179-189] |
| `WikiError::from` | method | `fn from(error: indexer::IndexError) -> Self {` | `WikiError::from [method]` | `070f169c-fa8b-5349-8f29-cfa44594cdb2` | 193-195 [crates/gwiki/src/error.rs:193-195] | Indexed method `WikiError::from` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:193-195] |
| `WikiError::from` | method | `fn from(error: search::SearchError) -> Self {` | `WikiError::from [method]` | `d7029b8d-b80f-55d0-951b-c8c03a6f3fa4` | 199-201 [crates/gwiki/src/error.rs:199-201] | Indexed method `WikiError::from` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:199-201] |
| `WikiError::from` | method | `fn from(error: SetupError) -> Self {` | `WikiError::from [method]` | `350a5256-d247-5f71-803a-f941210bdc36` | 205-207 [crates/gwiki/src/error.rs:205-207] | Indexed method `WikiError::from` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:205-207] |
| `typed_error_sources_are_preserved` | function | `fn typed_error_sources_are_preserved() {` | `typed_error_sources_are_preserved [function]` | `82edcf04-a245-50e3-a1b1-cb273de38f41` | 216-227 [crates/gwiki/src/error.rs:216-227] | Indexed function `typed_error_sources_are_preserved` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:216-227] |
| `wrapped_error_codes_are_specific` | function | `fn wrapped_error_codes_are_specific() {` | `wrapped_error_codes_are_specific [function]` | `a81a6414-0ee7-54ae-9a12-505766315c5d` | 230-240 [crates/gwiki/src/error.rs:230-240] | Indexed function `wrapped_error_codes_are_specific` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:230-240] |
| `timeout_errors_are_typed` | function | `fn timeout_errors_are_typed() {` | `timeout_errors_are_typed [function]` | `4be03e26-9128-5e18-9a8b-8f2d39a1cbf6` | 243-254 [crates/gwiki/src/error.rs:243-254] | Indexed function `timeout_errors_are_typed` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:243-254] |
| `ffmpeg_unavailable_detection_matches_config_and_io_errors` | function | `fn ffmpeg_unavailable_detection_matches_config_and_io_errors() {` | `ffmpeg_unavailable_detection_matches_config_and_io_errors [function]` | `bd2b2bd2-56aa-5b4f-bd1c-22031b3baef6` | 257-275 [crates/gwiki/src/error.rs:257-275] | Indexed function `ffmpeg_unavailable_detection_matches_config_and_io_errors` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:257-275] |
| `setup_error_source_is_preserved` | function | `fn setup_error_source_is_preserved() {` | `setup_error_source_is_preserved [function]` | `70da36ee-1d76-5985-8489-f033815340fc` | 278-287 [crates/gwiki/src/error.rs:278-287] | Indexed function `setup_error_source_is_preserved` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:278-287] |
