---
title: crates/gwiki/src/error.rs
type: code_file
provenance:
- file: crates/gwiki/src/error.rs
  ranges:
  - 10-66
  - 68-100
  - 69-86
  - 88-99
  - 102-159
  - 103-158
  - 161-176
  - 178-190
  - 179-189
  - 192-196
  - 193-195
  - 198-202
  - 199-201
  - 204-208
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

# crates/gwiki/src/error.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/error.rs` exposes 20 indexed API symbols.
[crates/gwiki/src/error.rs:10-66]
[crates/gwiki/src/error.rs:68-100]
[crates/gwiki/src/error.rs:69-86]
[crates/gwiki/src/error.rs:88-99]
[crates/gwiki/src/error.rs:102-159]
[crates/gwiki/src/error.rs:103-158]
[crates/gwiki/src/error.rs:161-176]
[crates/gwiki/src/error.rs:178-190]
[crates/gwiki/src/error.rs:179-189]
[crates/gwiki/src/error.rs:192-196]
[crates/gwiki/src/error.rs:193-195]
[crates/gwiki/src/error.rs:198-202]
[crates/gwiki/src/error.rs:199-201]
[crates/gwiki/src/error.rs:204-208]
[crates/gwiki/src/error.rs:205-207]
[crates/gwiki/src/error.rs:216-227]
[crates/gwiki/src/error.rs:230-240]
[crates/gwiki/src/error.rs:243-254]
[crates/gwiki/src/error.rs:257-275]
[crates/gwiki/src/error.rs:278-287]

## API Symbols

- `WikiError` (type) component `WikiError [type]` (`112c956a-2044-535b-aa5d-1b7fbc26685e`) lines 10-66 [crates/gwiki/src/error.rs:10-66]
  - Signature: `pub enum WikiError {`
  - Purpose: Indexed type `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:10-66]
- `WikiError` (class) component `WikiError [class]` (`c7a305c7-a79b-5a92-9d17-50d7d50d6574`) lines 68-100 [crates/gwiki/src/error.rs:68-100]
  - Signature: `impl WikiError {`
  - Purpose: Indexed class `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:68-100]
- `WikiError.code` (method) component `WikiError.code [method]` (`11d4afc8-edd8-5799-8252-62ffa09b2fab`) lines 69-86 [crates/gwiki/src/error.rs:69-86]
  - Signature: `pub fn code(&self) -> &'static str {`
  - Purpose: Indexed method `WikiError.code` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:69-86]
- `WikiError.is_ffmpeg_unavailable` (method) component `WikiError.is_ffmpeg_unavailable [method]` (`4b4b7188-29cd-5935-b1eb-edffdc4defa9`) lines 88-99 [crates/gwiki/src/error.rs:88-99]
  - Signature: `pub(crate) fn is_ffmpeg_unavailable(&self) -> bool {`
  - Purpose: Indexed method `WikiError.is_ffmpeg_unavailable` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:88-99]
- `WikiError` (class) component `WikiError [class]` (`3eaf52bd-7e70-5522-996b-8697d9134984`) lines 102-159 [crates/gwiki/src/error.rs:102-159]
  - Signature: `impl fmt::Display for WikiError {`
  - Purpose: Indexed class `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:102-159]
- `WikiError.fmt` (method) component `WikiError.fmt [method]` (`b0574737-29da-5369-9dec-730dff09cfe0`) lines 103-158 [crates/gwiki/src/error.rs:103-158]
  - Signature: `fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {`
  - Purpose: Indexed method `WikiError.fmt` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:103-158]
- `format_action_error` (function) component `format_action_error [function]` (`e73af4e6-78a4-59db-9fad-9001e79bd22f`) lines 161-176 [crates/gwiki/src/error.rs:161-176]
  - Signature: `fn format_action_error(`
  - Purpose: Indexed function `format_action_error` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:161-176]
- `WikiError` (class) component `WikiError [class]` (`07ea4ee5-6946-58c3-8fec-c267f06eb48b`) lines 178-190 [crates/gwiki/src/error.rs:178-190]
  - Signature: `impl std::error::Error for WikiError {`
  - Purpose: Indexed class `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:178-190]
- `WikiError.source` (method) component `WikiError.source [method]` (`2c6dd5af-a233-54a8-95a5-f3ddd63fbb80`) lines 179-189 [crates/gwiki/src/error.rs:179-189]
  - Signature: `fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {`
  - Purpose: Indexed method `WikiError.source` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:179-189]
- `WikiError` (class) component `WikiError [class]` (`3d908a1b-89ac-5c49-a251-bf744e332235`) lines 192-196 [crates/gwiki/src/error.rs:192-196]
  - Signature: `impl From<indexer::IndexError> for WikiError {`
  - Purpose: Indexed class `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:192-196]
- `WikiError.from` (method) component `WikiError.from [method]` (`070f169c-fa8b-5349-8f29-cfa44594cdb2`) lines 193-195 [crates/gwiki/src/error.rs:193-195]
  - Signature: `fn from(error: indexer::IndexError) -> Self {`
  - Purpose: Indexed method `WikiError.from` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:193-195]
- `WikiError` (class) component `WikiError [class]` (`ab18b3f9-6195-5587-a7c7-5b76ed6edbb1`) lines 198-202 [crates/gwiki/src/error.rs:198-202]
  - Signature: `impl From<search::SearchError> for WikiError {`
  - Purpose: Indexed class `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:198-202]
- `WikiError.from` (method) component `WikiError.from [method]` (`d7029b8d-b80f-55d0-951b-c8c03a6f3fa4`) lines 199-201 [crates/gwiki/src/error.rs:199-201]
  - Signature: `fn from(error: search::SearchError) -> Self {`
  - Purpose: Indexed method `WikiError.from` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:199-201]
- `WikiError` (class) component `WikiError [class]` (`81073c45-7f10-58a5-903a-d214b2be2b3d`) lines 204-208 [crates/gwiki/src/error.rs:204-208]
  - Signature: `impl From<SetupError> for WikiError {`
  - Purpose: Indexed class `WikiError` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:204-208]
- `WikiError.from` (method) component `WikiError.from [method]` (`350a5256-d247-5f71-803a-f941210bdc36`) lines 205-207 [crates/gwiki/src/error.rs:205-207]
  - Signature: `fn from(error: SetupError) -> Self {`
  - Purpose: Indexed method `WikiError.from` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:205-207]
- `typed_error_sources_are_preserved` (function) component `typed_error_sources_are_preserved [function]` (`82edcf04-a245-50e3-a1b1-cb273de38f41`) lines 216-227 [crates/gwiki/src/error.rs:216-227]
  - Signature: `fn typed_error_sources_are_preserved() {`
  - Purpose: Indexed function `typed_error_sources_are_preserved` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:216-227]
- `wrapped_error_codes_are_specific` (function) component `wrapped_error_codes_are_specific [function]` (`a81a6414-0ee7-54ae-9a12-505766315c5d`) lines 230-240 [crates/gwiki/src/error.rs:230-240]
  - Signature: `fn wrapped_error_codes_are_specific() {`
  - Purpose: Indexed function `wrapped_error_codes_are_specific` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:230-240]
- `timeout_errors_are_typed` (function) component `timeout_errors_are_typed [function]` (`4be03e26-9128-5e18-9a8b-8f2d39a1cbf6`) lines 243-254 [crates/gwiki/src/error.rs:243-254]
  - Signature: `fn timeout_errors_are_typed() {`
  - Purpose: Indexed function `timeout_errors_are_typed` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:243-254]
- `ffmpeg_unavailable_detection_matches_config_and_io_errors` (function) component `ffmpeg_unavailable_detection_matches_config_and_io_errors [function]` (`bd2b2bd2-56aa-5b4f-bd1c-22031b3baef6`) lines 257-275 [crates/gwiki/src/error.rs:257-275]
  - Signature: `fn ffmpeg_unavailable_detection_matches_config_and_io_errors() {`
  - Purpose: Indexed function `ffmpeg_unavailable_detection_matches_config_and_io_errors` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:257-275]
- `setup_error_source_is_preserved` (function) component `setup_error_source_is_preserved [function]` (`70da36ee-1d76-5985-8489-f033815340fc`) lines 278-287 [crates/gwiki/src/error.rs:278-287]
  - Signature: `fn setup_error_source_is_preserved() {`
  - Purpose: Indexed function `setup_error_source_is_preserved` in `crates/gwiki/src/error.rs`. [crates/gwiki/src/error.rs:278-287]

