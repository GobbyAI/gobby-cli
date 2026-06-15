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
  - 60-69
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

# crates/gwiki/src/media.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Utilities for media processing built around `ffmpeg` and `ffprobe`: this file probes durations, extracts audio, samples video frames, and splits audio into fixed or overlapping chunks, storing outputs in temporary files. The public functions are thin wrappers that discover the required tools on `PATH` and delegate to shared helpers that run commands, format time arguments, and convert durations between milliseconds and public second-based values. `Chunk` represents one extracted audio segment with its millisecond range and temp-file payload, while the tests verify time formatting, duration parsing, frame-sampling limits, and temp-file cleanup behavior.
[crates/gwiki/src/media.rs:13-17]
[crates/gwiki/src/media.rs:19-22]
[crates/gwiki/src/media.rs:24-27]
[crates/gwiki/src/media.rs:29-35]
[crates/gwiki/src/media.rs:37-43]

## API Symbols

- `Chunk` (class) component `Chunk [class]` (`270f4749-0009-5b23-aa9e-53056e214fb9`) lines 13-17 [crates/gwiki/src/media.rs:13-17]
  - Signature: `pub struct Chunk {`
  - Purpose: `Chunk` is a struct that associates a time interval (delimited by `start_ms` and `end_ms` in milliseconds) with a `NamedTempFile` resource. [crates/gwiki/src/media.rs:13-17]
- `probe_duration` (function) component `probe_duration [function]` (`17089eb0-15d1-5678-9b5d-7c5f5b9aef15`) lines 19-22 [crates/gwiki/src/media.rs:19-22]
  - Signature: `pub fn probe_duration(path: impl AsRef<Path>) -> Option<u32> {`
  - Purpose: Locates the ffprobe executable on the system PATH and probes the duration of a media file at the specified path, returning an `Option<u32>`. [crates/gwiki/src/media.rs:19-22]
- `extract_audio_file` (function) component `extract_audio_file [function]` (`8203a4f6-ccb7-501c-83bd-f89543493214`) lines 24-27 [crates/gwiki/src/media.rs:24-27]
  - Signature: `pub fn extract_audio_file(video: impl AsRef<Path>) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Locates ffmpeg on the system PATH and uses it to extract audio from a video file into a temporary file, returning a `NamedTempFile` or a `WikiError` if ffmpeg is unavailable. [crates/gwiki/src/media.rs:24-27]
- `sample_frame_images` (function) component `sample_frame_images [function]` (`f9f85e53-4a51-5c90-8d16-5798327364c0`) lines 29-35 [crates/gwiki/src/media.rs:29-35]
  - Signature: `pub fn sample_frame_images(`
  - Purpose: Discovers available media tools and samples video frames at the specified interval, returning frame indices paired with temporary image files. [crates/gwiki/src/media.rs:29-35]
- `split_audio_file` (function) component `split_audio_file [function]` (`1354e3cc-c390-58cd-8684-dd02542de09e`) lines 37-43 [crates/gwiki/src/media.rs:37-43]
  - Signature: `pub fn split_audio_file(`
  - Purpose: Splits an audio file into chunks of a specified window duration using automatically discovered media tools. [crates/gwiki/src/media.rs:37-43]
- `split_audio_file_with_overlap` (function) component `split_audio_file_with_overlap [function]` (`10fcd962-2485-528e-912d-bdf345500127`) lines 45-52 [crates/gwiki/src/media.rs:45-52]
  - Signature: `pub fn split_audio_file_with_overlap(`
  - Purpose: Splits an audio file into overlapping chunks of specified window and overlap durations using auto-discovered MediaTools. [crates/gwiki/src/media.rs:45-52]
- `MediaTools` (class) component `MediaTools [class]` (`3d660f56-5329-51e0-92a6-b90742bc7ea6`) lines 55-58 [crates/gwiki/src/media.rs:55-58]
  - Signature: `struct MediaTools {`
  - Purpose: MediaTools is a struct that encapsulates file paths to the ffmpeg and ffprobe executables for media processing operations. [crates/gwiki/src/media.rs:55-58]
- `MediaTools` (class) component `MediaTools [class]` (`c6e26e9f-5bc2-5654-b4c1-150cca46b9ea`) lines 60-69 [crates/gwiki/src/media.rs:60-69]
  - Signature: `impl MediaTools {`
  - Purpose: MediaTools::discover() constructs a MediaTools instance by locating ffmpeg and ffprobe executables on the system PATH, returning a Result with the instance on success or WikiError if either executable is missing. [crates/gwiki/src/media.rs:60-69]
- `MediaTools.discover` (method) component `MediaTools.discover [method]` (`46397133-b3d9-55a6-8405-7de4085005ea`) lines 61-68 [crates/gwiki/src/media.rs:61-68]
  - Signature: `fn discover() -> Result<Self, WikiError> {`
  - Purpose: Discovers and constructs `Self` by locating the `ffmpeg` and `ffprobe` executables on the system PATH, returning `WikiError` if either is missing. [crates/gwiki/src/media.rs:61-68]
- `extract_audio_file_with_ffmpeg` (function) component `extract_audio_file_with_ffmpeg [function]` (`95074d05-1f21-517e-9091-20424fe59c25`) lines 71-93 [crates/gwiki/src/media.rs:71-93]
  - Signature: `fn extract_audio_file_with_ffmpeg(video: &Path, ffmpeg: &Path) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Extracts and transcodes video audio to a temporary mono, 16-bit PCM WAV file at 16 kHz sample rate using ffmpeg. [crates/gwiki/src/media.rs:71-93]
- `sample_frame_images_with_tools` (function) component `sample_frame_images_with_tools [function]` (`16d94929-0d68-5d60-b5c8-33d505671806`) lines 95-125 [crates/gwiki/src/media.rs:95-125]
  - Signature: `fn sample_frame_images_with_tools(`
  - Purpose: Samples video frames at uniform time intervals using ffmpeg and returns a vector of tuples containing each frame's timestamp offset paired with its corresponding temporary JPEG file. [crates/gwiki/src/media.rs:95-125]
- `frame_sample_offsets` (function) component `frame_sample_offsets [function]` (`1c211151-a726-5dd8-850b-26ce87d82434`) lines 127-139 [crates/gwiki/src/media.rs:127-139]
  - Signature: `fn frame_sample_offsets(duration_ms: u64, interval: Duration) -> Result<Vec<u64>, WikiError> {`
  - Purpose: Generates a vector of uniformly-spaced frame sample time offsets (in milliseconds) from 0 to `duration_ms` at intervals no shorter than `MIN_FRAME_SAMPLE_INTERVAL`, capped at `MAX_SAMPLED_FRAMES` samples. [crates/gwiki/src/media.rs:127-139]
- `split_audio_file_with_tools` (function) component `split_audio_file_with_tools [function]` (`4da4c18e-ddea-568e-9d0a-395da540b2ff`) lines 141-200 [crates/gwiki/src/media.rs:141-200]
  - Signature: `fn split_audio_file_with_tools(`
  - Purpose: Splits an audio file into overlapping fixed-window chunks with specified stride, converting each to mono 16-bit PCM WAV at 16kHz via FFmpeg. [crates/gwiki/src/media.rs:141-200]
- `media_duration_ms` (function) component `media_duration_ms [function]` (`eb112e19-e93d-5535-8c47-33f0b079548f`) lines 202-209 [crates/gwiki/src/media.rs:202-209]
  - Signature: `fn media_duration_ms(path: &Path, tools: &MediaTools) -> Result<u64, WikiError> {`
  - Purpose: Probes a media file's duration in milliseconds using ffprobe, returning a `u64` or a `WikiError` if ffprobe fails to determine the duration. [crates/gwiki/src/media.rs:202-209]
- `probe_duration_with_tool` (function) component `probe_duration_with_tool [function]` (`2e1d1857-23ff-555f-9024-f75bdc451eea`) lines 211-213 [crates/gwiki/src/media.rs:211-213]
  - Signature: `fn probe_duration_with_tool(path: &Path, ffprobe: &Path) -> Option<u32> {`
  - Purpose: Probes a media file's duration in milliseconds using ffprobe, converts the result to seconds, and returns `Option<u32>`. [crates/gwiki/src/media.rs:211-213]
- `probe_duration_ms_with_tool` (function) component `probe_duration_ms_with_tool [function]` (`9efe7bc3-a2a4-5885-a7f8-8d9b62a28d82`) lines 215-230 [crates/gwiki/src/media.rs:215-230]
  - Signature: `fn probe_duration_ms_with_tool(path: &Path, ffprobe: &Path) -> Option<u64> {`
  - Purpose: Executes ffprobe to extract a media file's duration and returns the parsed result in milliseconds as `Some(u64)`, or `None` if the process fails or parsing is unsuccessful. [crates/gwiki/src/media.rs:215-230]
- `parse_duration_ms` (function) component `parse_duration_ms [function]` (`a7cbad16-ee8a-5217-bd17-5fe75c9afec6`) lines 232-245 [crates/gwiki/src/media.rs:232-245]
  - Signature: `fn parse_duration_ms(raw: &str) -> Option<u64> {`
  - Purpose: Parses the first valid f64 from a multi-line string as seconds, validates finiteness and non-negativity, and returns the u64 ceiling of its millisecond-scaled value. [crates/gwiki/src/media.rs:232-245]
- `duration_ms_to_public_seconds` (function) component `duration_ms_to_public_seconds [function]` (`a38bef6c-7dd8-5b54-bf13-fe291d387cc9`) lines 247-250 [crates/gwiki/src/media.rs:247-250]
  - Signature: `fn duration_ms_to_public_seconds(milliseconds: u64) -> Option<u32> {`
  - Purpose: Converts milliseconds to seconds using ceiling division and attempts to cast the result to `u32`, returning `Some` on success or `None` on overflow. [crates/gwiki/src/media.rs:247-250]
- `duration_to_ms` (function) component `duration_to_ms [function]` (`9debed46-293c-5782-a96d-a09160073c3c`) lines 252-267 [crates/gwiki/src/media.rs:252-267]
  - Signature: `fn duration_to_ms(duration: Duration, field: &'static str) -> Result<u64, WikiError> {`
  - Purpose: Converts a `Duration` to milliseconds as a `u64` with validation that the result is at least 1ms and fits within `u64` bounds. [crates/gwiki/src/media.rs:252-267]
- `seconds_arg` (function) component `seconds_arg [function]` (`5f002eec-9485-5f71-b973-60e91823a02f`) lines 269-271 [crates/gwiki/src/media.rs:269-271]
  - Signature: `fn seconds_arg(milliseconds: u64) -> String {`
  - Purpose: Converts a u64 millisecond value to a decimal string representation with the format `seconds.milliseconds`, zero-padding the fractional part to three digits. [crates/gwiki/src/media.rs:269-271]
- `media_temp_file` (function) component `media_temp_file [function]` (`f48deaa1-d6c2-5aad-a756-452b291cb598`) lines 273-283 [crates/gwiki/src/media.rs:273-283]
  - Signature: `fn media_temp_file(suffix: &str, action: &'static str) -> Result<NamedTempFile, WikiError> {`
  - Purpose: Creates a NamedTempFile with the prefix "gwiki-media-" and a provided suffix, wrapping any IO errors into a WikiError::Io variant with the given action context. [crates/gwiki/src/media.rs:273-283]
- `run_media_command` (function) component `run_media_command [function]` (`f8e1852d-f67b-5398-838d-3cebfe5caa8d`) lines 285-300 [crates/gwiki/src/media.rs:285-300]
  - Signature: `fn run_media_command(`
  - Purpose: Executes a media command and returns a WikiError wrapping either I/O errors with contextual metadata (action, path) or the command's failure output. [crates/gwiki/src/media.rs:285-300]
- `media_command_failed` (function) component `media_command_failed [function]` (`ba07876c-0a6d-5142-a55f-378fd8253057`) lines 302-311 [crates/gwiki/src/media.rs:302-311]
  - Signature: `fn media_command_failed(tool: &str, output: Output) -> WikiError {`
  - Purpose: Constructs a `WikiError::Config` from a failed command's exit status and stderr output, conditionally including stderr in the error detail if non-empty. [crates/gwiki/src/media.rs:302-311]
- `find_executable_on_path` (function) component `find_executable_on_path [function]` (`092ad0ee-f2eb-5c83-bd6b-017c41a9c0a2`) lines 313-340 [crates/gwiki/src/media.rs:313-340]
  - Signature: `fn find_executable_on_path(name: &str) -> Option<PathBuf> {`
  - Purpose: Resolves an executable's full path by checking explicit paths first, then searching PATH directories with platform-specific executable extension matching on Windows. [crates/gwiki/src/media.rs:313-340]
- `missing_media_tool` (function) component `missing_media_tool [function]` (`7c59bc6a-4e54-5dd2-88ff-8e141d588d87`) lines 342-346 [crates/gwiki/src/media.rs:342-346]
  - Signature: `fn missing_media_tool(tool: &str) -> WikiError {`
  - Purpose: This function returns a `WikiError::Config` variant with a detail message indicating that a specified tool executable is not found on the system PATH. [crates/gwiki/src/media.rs:342-346]
- `seconds_args_use_integer_milliseconds` (function) component `seconds_args_use_integer_milliseconds [function]` (`735e556f-142e-57d1-b7e2-7eb565066191`) lines 355-359 [crates/gwiki/src/media.rs:355-359]
  - Signature: `fn seconds_args_use_integer_milliseconds() {`
  - Purpose: This test function verifies that `seconds_arg()` correctly converts integer millisecond values to formatted decimal strings representing seconds with three decimal places. [crates/gwiki/src/media.rs:355-359]
- `duration_parser_preserves_milliseconds_internally` (function) component `duration_parser_preserves_milliseconds_internally [function]` (`5d706fda-1ecf-50c3-8494-77b98c9aa231`) lines 362-366 [crates/gwiki/src/media.rs:362-366]
  - Signature: `fn duration_parser_preserves_milliseconds_internally() {`
  - Purpose: This test verifies that the duration parser internally preserves millisecond precision from fractional second input while the public API rounds up to whole seconds using ceiling division. [crates/gwiki/src/media.rs:362-366]
- `frame_sampling_offsets_are_capped_and_clamped` (function) component `frame_sampling_offsets_are_capped_and_clamped [function]` (`d0e1f1ba-3477-529c-a06f-c1b39bf5abcf`) lines 369-375 [crates/gwiki/src/media.rs:369-375]
  - Signature: `fn frame_sampling_offsets_are_capped_and_clamped() {`
  - Purpose: # Summary

Unit test verifying that `frame_sample_offsets()` caps the returned array to `MAX_SAMPLED_FRAMES` entries and clamps initial offset values to 0 and 1,000 milliseconds. [crates/gwiki/src/media.rs:369-375]
- `temp_files_cleaned_asset_survives` (function) component `temp_files_cleaned_asset_survives [function]` (`75f55493-cb17-5f5b-8f66-63529b659462`) lines 379-436 [crates/gwiki/src/media.rs:379-436]
  - Signature: `fn temp_files_cleaned_asset_survives() {`
  - Purpose: Tests that `sample_frame_images_with_tools()` cleans up all temporary ffmpeg output files while preserving the original asset when ffmpeg fails mid-execution. [crates/gwiki/src/media.rs:379-436]
- `write_executable` (function) component `write_executable [function]` (`51f9d35b-6372-5ae0-8173-f1f75480aedb`) lines 439-449 [crates/gwiki/src/media.rs:439-449]
  - Signature: `fn write_executable(path: &Path, contents: &str) {`
  - Purpose: Creates an executable file at the given path by writing the provided contents and setting Unix file permissions to 0o755 (rwxr-xr-x). [crates/gwiki/src/media.rs:439-449]

