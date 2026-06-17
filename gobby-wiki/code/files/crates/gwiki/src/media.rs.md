---
title: crates/gwiki/src/media.rs
type: code_file
provenance:
- file: crates/gwiki/src/media.rs
  ranges:
  - 13-17
  - 19-22
  - 24-27
  - 29-35
  - 37-43
  - 45-52
  - 55-58
  - 61-68
  - 71-93
  - 95-125
  - 127-139
  - 141-200
  - 202-209
  - 211-213
  - 215-230
  - 232-245
  - 247-250
  - 252-267
  - 269-271
  - 273-283
  - 285-300
  - 302-311
  - 313-340
  - 342-346
  - 355-359
  - 362-366
  - 369-375
  - 379-436
  - 439-449
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/media.rs:13-17](crates/gwiki/src/media.rs#L13-L17), [crates/gwiki/src/media.rs:19-22](crates/gwiki/src/media.rs#L19-L22), [crates/gwiki/src/media.rs:24-27](crates/gwiki/src/media.rs#L24-L27), [crates/gwiki/src/media.rs:29-35](crates/gwiki/src/media.rs#L29-L35), [crates/gwiki/src/media.rs:37-43](crates/gwiki/src/media.rs#L37-L43), [crates/gwiki/src/media.rs:45-52](crates/gwiki/src/media.rs#L45-L52), [crates/gwiki/src/media.rs:55-58](crates/gwiki/src/media.rs#L55-L58), [crates/gwiki/src/media.rs:61-68](crates/gwiki/src/media.rs#L61-L68), [crates/gwiki/src/media.rs:71-93](crates/gwiki/src/media.rs#L71-L93), [crates/gwiki/src/media.rs:95-125](crates/gwiki/src/media.rs#L95-L125), [crates/gwiki/src/media.rs:127-139](crates/gwiki/src/media.rs#L127-L139), [crates/gwiki/src/media.rs:141-200](crates/gwiki/src/media.rs#L141-L200), [crates/gwiki/src/media.rs:202-209](crates/gwiki/src/media.rs#L202-L209), [crates/gwiki/src/media.rs:211-213](crates/gwiki/src/media.rs#L211-L213), [crates/gwiki/src/media.rs:215-230](crates/gwiki/src/media.rs#L215-L230), [crates/gwiki/src/media.rs:232-245](crates/gwiki/src/media.rs#L232-L245), [crates/gwiki/src/media.rs:247-250](crates/gwiki/src/media.rs#L247-L250), [crates/gwiki/src/media.rs:252-267](crates/gwiki/src/media.rs#L252-L267), [crates/gwiki/src/media.rs:269-271](crates/gwiki/src/media.rs#L269-L271), [crates/gwiki/src/media.rs:273-283](crates/gwiki/src/media.rs#L273-L283), [crates/gwiki/src/media.rs:285-300](crates/gwiki/src/media.rs#L285-L300), [crates/gwiki/src/media.rs:302-311](crates/gwiki/src/media.rs#L302-L311), [crates/gwiki/src/media.rs:313-340](crates/gwiki/src/media.rs#L313-L340), [crates/gwiki/src/media.rs:342-346](crates/gwiki/src/media.rs#L342-L346), [crates/gwiki/src/media.rs:355-359](crates/gwiki/src/media.rs#L355-L359), [crates/gwiki/src/media.rs:362-366](crates/gwiki/src/media.rs#L362-L366), [crates/gwiki/src/media.rs:369-375](crates/gwiki/src/media.rs#L369-L375), [crates/gwiki/src/media.rs:379-436](crates/gwiki/src/media.rs#L379-L436), [crates/gwiki/src/media.rs:439-449](crates/gwiki/src/media.rs#L439-L449)

</details>

# crates/gwiki/src/media.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file provides media-processing utilities built around `ffmpeg` and `ffprobe`: probing media duration, extracting audio from video, sampling video frames, and splitting audio into timed chunks, including overlap-aware splitting. The public entry points delegate to shared internal helpers that discover the required tools, build and run the media commands, convert between duration formats, and manage temporary output files, with tests covering duration parsing, sampling bounds, temp-file cleanup, and executable handling.
[crates/gwiki/src/media.rs:13-17]
[crates/gwiki/src/media.rs:19-22]
[crates/gwiki/src/media.rs:24-27]
[crates/gwiki/src/media.rs:29-35]
[crates/gwiki/src/media.rs:37-43]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Chunk` | class | `pub struct Chunk {` | `Chunk [class]` | `270f4749-0009-5b23-aa9e-53056e214fb9` | 13-17 [crates/gwiki/src/media.rs:13-17] | Indexed class `Chunk` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:13-17] |
| `probe_duration` | function | `pub fn probe_duration(path: impl AsRef<Path>) -> Option<u32> {` | `probe_duration [function]` | `17089eb0-15d1-5678-9b5d-7c5f5b9aef15` | 19-22 [crates/gwiki/src/media.rs:19-22] | Indexed function `probe_duration` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:19-22] |
| `extract_audio_file` | function | `pub fn extract_audio_file(video: impl AsRef<Path>) -> Result<NamedTempFile, WikiError> {` | `extract_audio_file [function]` | `8203a4f6-ccb7-501c-83bd-f89543493214` | 24-27 [crates/gwiki/src/media.rs:24-27] | Indexed function `extract_audio_file` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:24-27] |
| `sample_frame_images` | function | `pub fn sample_frame_images(` | `sample_frame_images [function]` | `f9f85e53-4a51-5c90-8d16-5798327364c0` | 29-35 [crates/gwiki/src/media.rs:29-35] | Indexed function `sample_frame_images` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:29-35] |
| `split_audio_file` | function | `pub fn split_audio_file(` | `split_audio_file [function]` | `1354e3cc-c390-58cd-8684-dd02542de09e` | 37-43 [crates/gwiki/src/media.rs:37-43] | Indexed function `split_audio_file` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:37-43] |
| `split_audio_file_with_overlap` | function | `pub fn split_audio_file_with_overlap(` | `split_audio_file_with_overlap [function]` | `10fcd962-2485-528e-912d-bdf345500127` | 45-52 [crates/gwiki/src/media.rs:45-52] | Indexed function `split_audio_file_with_overlap` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:45-52] |
| `MediaTools` | class | `struct MediaTools {` | `MediaTools [class]` | `3d660f56-5329-51e0-92a6-b90742bc7ea6` | 55-58 [crates/gwiki/src/media.rs:55-58] | Indexed class `MediaTools` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:55-58] |
| `MediaTools::discover` | method | `fn discover() -> Result<Self, WikiError> {` | `MediaTools::discover [method]` | `46397133-b3d9-55a6-8405-7de4085005ea` | 61-68 [crates/gwiki/src/media.rs:61-68] | Indexed method `MediaTools::discover` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:61-68] |
| `extract_audio_file_with_ffmpeg` | function | `fn extract_audio_file_with_ffmpeg(video: &Path, ffmpeg: &Path) -> Result<NamedTempFile, WikiError> {` | `extract_audio_file_with_ffmpeg [function]` | `95074d05-1f21-517e-9091-20424fe59c25` | 71-93 [crates/gwiki/src/media.rs:71-93] | Indexed function `extract_audio_file_with_ffmpeg` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:71-93] |
| `sample_frame_images_with_tools` | function | `fn sample_frame_images_with_tools(` | `sample_frame_images_with_tools [function]` | `16d94929-0d68-5d60-b5c8-33d505671806` | 95-125 [crates/gwiki/src/media.rs:95-125] | Indexed function `sample_frame_images_with_tools` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:95-125] |
| `frame_sample_offsets` | function | `fn frame_sample_offsets(duration_ms: u64, interval: Duration) -> Result<Vec<u64>, WikiError> {` | `frame_sample_offsets [function]` | `1c211151-a726-5dd8-850b-26ce87d82434` | 127-139 [crates/gwiki/src/media.rs:127-139] | Indexed function `frame_sample_offsets` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:127-139] |
| `split_audio_file_with_tools` | function | `fn split_audio_file_with_tools(` | `split_audio_file_with_tools [function]` | `4da4c18e-ddea-568e-9d0a-395da540b2ff` | 141-200 [crates/gwiki/src/media.rs:141-200] | Indexed function `split_audio_file_with_tools` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:141-200] |
| `media_duration_ms` | function | `fn media_duration_ms(path: &Path, tools: &MediaTools) -> Result<u64, WikiError> {` | `media_duration_ms [function]` | `eb112e19-e93d-5535-8c47-33f0b079548f` | 202-209 [crates/gwiki/src/media.rs:202-209] | Indexed function `media_duration_ms` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:202-209] |
| `probe_duration_with_tool` | function | `fn probe_duration_with_tool(path: &Path, ffprobe: &Path) -> Option<u32> {` | `probe_duration_with_tool [function]` | `2e1d1857-23ff-555f-9024-f75bdc451eea` | 211-213 [crates/gwiki/src/media.rs:211-213] | Indexed function `probe_duration_with_tool` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:211-213] |
| `probe_duration_ms_with_tool` | function | `fn probe_duration_ms_with_tool(path: &Path, ffprobe: &Path) -> Option<u64> {` | `probe_duration_ms_with_tool [function]` | `9efe7bc3-a2a4-5885-a7f8-8d9b62a28d82` | 215-230 [crates/gwiki/src/media.rs:215-230] | Indexed function `probe_duration_ms_with_tool` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:215-230] |
| `parse_duration_ms` | function | `fn parse_duration_ms(raw: &str) -> Option<u64> {` | `parse_duration_ms [function]` | `a7cbad16-ee8a-5217-bd17-5fe75c9afec6` | 232-245 [crates/gwiki/src/media.rs:232-245] | Indexed function `parse_duration_ms` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:232-245] |
| `duration_ms_to_public_seconds` | function | `fn duration_ms_to_public_seconds(milliseconds: u64) -> Option<u32> {` | `duration_ms_to_public_seconds [function]` | `a38bef6c-7dd8-5b54-bf13-fe291d387cc9` | 247-250 [crates/gwiki/src/media.rs:247-250] | Indexed function `duration_ms_to_public_seconds` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:247-250] |
| `duration_to_ms` | function | `fn duration_to_ms(duration: Duration, field: &'static str) -> Result<u64, WikiError> {` | `duration_to_ms [function]` | `9debed46-293c-5782-a96d-a09160073c3c` | 252-267 [crates/gwiki/src/media.rs:252-267] | Indexed function `duration_to_ms` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:252-267] |
| `seconds_arg` | function | `fn seconds_arg(milliseconds: u64) -> String {` | `seconds_arg [function]` | `5f002eec-9485-5f71-b973-60e91823a02f` | 269-271 [crates/gwiki/src/media.rs:269-271] | Indexed function `seconds_arg` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:269-271] |
| `media_temp_file` | function | `fn media_temp_file(suffix: &str, action: &'static str) -> Result<NamedTempFile, WikiError> {` | `media_temp_file [function]` | `f48deaa1-d6c2-5aad-a756-452b291cb598` | 273-283 [crates/gwiki/src/media.rs:273-283] | Indexed function `media_temp_file` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:273-283] |
| `run_media_command` | function | `fn run_media_command(` | `run_media_command [function]` | `f8e1852d-f67b-5398-838d-3cebfe5caa8d` | 285-300 [crates/gwiki/src/media.rs:285-300] | Indexed function `run_media_command` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:285-300] |
| `media_command_failed` | function | `fn media_command_failed(tool: &str, output: Output) -> WikiError {` | `media_command_failed [function]` | `ba07876c-0a6d-5142-a55f-378fd8253057` | 302-311 [crates/gwiki/src/media.rs:302-311] | Indexed function `media_command_failed` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:302-311] |
| `find_executable_on_path` | function | `fn find_executable_on_path(name: &str) -> Option<PathBuf> {` | `find_executable_on_path [function]` | `092ad0ee-f2eb-5c83-bd6b-017c41a9c0a2` | 313-340 [crates/gwiki/src/media.rs:313-340] | Indexed function `find_executable_on_path` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:313-340] |
| `missing_media_tool` | function | `fn missing_media_tool(tool: &str) -> WikiError {` | `missing_media_tool [function]` | `7c59bc6a-4e54-5dd2-88ff-8e141d588d87` | 342-346 [crates/gwiki/src/media.rs:342-346] | Indexed function `missing_media_tool` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:342-346] |
| `seconds_args_use_integer_milliseconds` | function | `fn seconds_args_use_integer_milliseconds() {` | `seconds_args_use_integer_milliseconds [function]` | `735e556f-142e-57d1-b7e2-7eb565066191` | 355-359 [crates/gwiki/src/media.rs:355-359] | Indexed function `seconds_args_use_integer_milliseconds` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:355-359] |
| `duration_parser_preserves_milliseconds_internally` | function | `fn duration_parser_preserves_milliseconds_internally() {` | `duration_parser_preserves_milliseconds_internally [function]` | `5d706fda-1ecf-50c3-8494-77b98c9aa231` | 362-366 [crates/gwiki/src/media.rs:362-366] | Indexed function `duration_parser_preserves_milliseconds_internally` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:362-366] |
| `frame_sampling_offsets_are_capped_and_clamped` | function | `fn frame_sampling_offsets_are_capped_and_clamped() {` | `frame_sampling_offsets_are_capped_and_clamped [function]` | `d0e1f1ba-3477-529c-a06f-c1b39bf5abcf` | 369-375 [crates/gwiki/src/media.rs:369-375] | Indexed function `frame_sampling_offsets_are_capped_and_clamped` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:369-375] |
| `temp_files_cleaned_asset_survives` | function | `fn temp_files_cleaned_asset_survives() {` | `temp_files_cleaned_asset_survives [function]` | `75f55493-cb17-5f5b-8f66-63529b659462` | 379-436 [crates/gwiki/src/media.rs:379-436] | Indexed function `temp_files_cleaned_asset_survives` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:379-436] |
| `write_executable` | function | `fn write_executable(path: &Path, contents: &str) {` | `write_executable [function]` | `51f9d35b-6372-5ae0-8173-f1f75480aedb` | 439-449 [crates/gwiki/src/media.rs:439-449] | Indexed function `write_executable` in `crates/gwiki/src/media.rs`. [crates/gwiki/src/media.rs:439-449] |
