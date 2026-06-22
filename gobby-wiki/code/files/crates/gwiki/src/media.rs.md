---
title: crates/gwiki/src/media.rs
type: code_file
provenance:
- file: crates/gwiki/src/media.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/media.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/media.rs` exposes 29 indexed API symbols.

## How it fits

`crates/gwiki/src/media.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Chunk` | class | 'Chunk' is a Rust struct that represents a time-bounded temporary file segment, storing its start and end timestamps in milliseconds along with a 'NamedTempFile' path. [crates/gwiki/src/media.rs:13-17] |
| `probe_duration` | function | Returns the media duration in seconds as a 'u32' by locating 'ffprobe' on 'PATH' and delegating to 'probe_duration_with_tool', or 'None' if 'ffprobe' is unavailable or probing fails. [crates/gwiki/src/media.rs:19-22] |
| `extract_audio_file` | function | Resolves 'ffmpeg' on 'PATH' and delegates to 'extract_audio_file_with_ffmpeg' to extract the given video’s audio into a 'NamedTempFile', returning a 'WikiError' if 'ffmpeg' is unavailable. [crates/gwiki/src/media.rs:24-27] |
| `sample_frame_images` | function | Discovers media tools and delegates to 'sample_frame_images_with_tools' to sample a video at the given 'interval', returning a 'Result' containing a 'Vec' of '(u64, NamedTempFile)' frame-image pairs or a 'WikiError'. [crates/gwiki/src/media.rs:29-35] |
| `split_audio_file` | function | Discovers available media tools and delegates to 'split_audio_file_with_tools' to split the input audio path into 'Chunk' segments of the specified 'window' duration starting at 'Duration::ZERO', returning the resulting chunks or a 'WikiError'. [crates/gwiki/src/media.rs:37-43] |
| `split_audio_file_with_overlap` | function | Discovers available media tools and delegates to 'split_audio_file_with_tools' to split the given audio file into overlapping 'Chunk's using the specified 'window' and 'overlap', returning a 'Result<Vec<Chunk>, WikiError>'. [crates/gwiki/src/media.rs:45-52] |
| `MediaTools` | class | 'MediaTools' is a struct that stores filesystem paths to the 'ffmpeg' and 'ffprobe' executables as 'PathBuf' values. [crates/gwiki/src/media.rs:55-58] |
| `MediaTools::discover` | method | Constructs 'Self' by locating 'ffmpeg' and 'ffprobe' on the system 'PATH', returning a 'WikiError' via 'missing_media_tool(...)' if either executable is absent. [crates/gwiki/src/media.rs:61-68] |
| `extract_audio_file_with_ffmpeg` | function | Runs 'ffmpeg' to extract the input video's audio into a temporary 16 kHz mono WAV file encoded as signed 16-bit PCM and returns the 'NamedTempFile'. [crates/gwiki/src/media.rs:71-93] |
| `sample_frame_images_with_tools` | function | Creates a series of temporary JPEG still images by invoking 'ffmpeg' at sampled millisecond offsets across a video’s duration and returns them as '(timestamp_ms, NamedTempFile)' pairs. [crates/gwiki/src/media.rs:95-125] |
| `frame_sample_offsets` | function | Generates monotonically increasing frame-sample offsets in milliseconds from '0' up to but excluding 'duration_ms', spaced by at least 'MIN_FRAME_SAMPLE_INTERVAL', capped at 'MAX_SAMPLED_FRAMES', and protected against 'u64' overflow via saturating addition. [crates/gwiki/src/media.rs:127-139] |
| `split_audio_file_with_tools` | function | Splits the input audio file into a sequence of temporary mono 16 kHz WAV chunks of at most 'window' duration, advancing by 'window - overlap', validating that 'overlap < window', and returning each chunk with its start and end timestamps. [crates/gwiki/src/media.rs:141-200] |
| `media_duration_ms` | function | Returns the media duration in milliseconds by delegating to 'probe_duration_ms_with_tool' using 'tools.ffprobe', and converts a missing result into a 'WikiError::Config' that reports 'ffprobe' could not determine the duration for the given path. [crates/gwiki/src/media.rs:202-209] |
| `probe_duration_with_tool` | function | Calls 'probe_duration_ms_with_tool(path, ffprobe)' and converts the resulting duration in milliseconds to public seconds, returning 'None' if either step fails. [crates/gwiki/src/media.rs:211-213] |
| `probe_duration_ms_with_tool` | function | Runs 'ffprobe' on 'path' to read the container’s 'format=duration' in a quiet, keyless format, returns 'None' if the process fails or exits unsuccessfully, and otherwise parses stdout into an 'Option<u64>' duration in milliseconds. [crates/gwiki/src/media.rs:215-230] |
| `parse_duration_ms` | function | Parses the first line in 'raw' that can be read as a nonnegative finite 'f64' number of seconds, converts it to milliseconds by multiplying by 1000 and rounding up, and returns 'None' if parsing fails, the value is negative/non-finite, or the result exceeds 'u64::MAX'. [crates/gwiki/src/media.rs:232-245] |
| `duration_ms_to_public_seconds` | function | Converts a millisecond duration to a public 'u32' second count by rounding up with ceiling division by 1000 and returning 'None' if the result does not fit in 'u32'. [crates/gwiki/src/media.rs:247-250] |
| `duration_to_ms` | function | Converts a 'Duration' to 'u64' milliseconds, returning 'WikiError::InvalidInput' if the duration is zero or exceeds 'u64::MAX' milliseconds. [crates/gwiki/src/media.rs:252-267] |
| `seconds_arg` | function | Formats a 'u64' millisecond count as a seconds string with exactly three fractional digits by dividing by 1000 for the whole seconds and zero-padding the remaining milliseconds. [crates/gwiki/src/media.rs:269-271] |
| `media_temp_file` | function | Creates a named temporary file with the 'gwiki-media-' prefix and the provided suffix, converting any I/O failure from 'tempfile()' into a 'WikiError::Io' that records the supplied 'action' and no path. [crates/gwiki/src/media.rs:273-283] |
| `run_media_command` | function | Runs the supplied media 'Command', returning 'Ok(())' on a successful exit status and otherwise converting I/O failures or nonzero exits into a 'WikiError' via 'media_command_failed' with the provided tool, action, and source path. [crates/gwiki/src/media.rs:285-300] |
| `media_command_failed` | function | Constructs a 'WikiError::Config' whose detail reports that 'tool' exited with the given 'Output' status, appending trimmed UTF-8-lossy stderr text when non-empty. [crates/gwiki/src/media.rs:302-311] |
| `find_executable_on_path` | function | Returns the first existing file path for 'name', treating multi-component inputs as explicit paths and otherwise searching each directory in 'PATH' (and 'PATHEXT'-suffixed variants on Windows), or 'None' if no matching executable file is found. [crates/gwiki/src/media.rs:313-340] |
| `missing_media_tool` | function | Constructs and returns a 'WikiError::Config' whose 'detail' states that the specified tool executable was not found on 'PATH'. [crates/gwiki/src/media.rs:342-346] |

_1 more symbol(s) not shown — run `gcode outline crates/gwiki/src/media.rs` for the full list._

_Verified by 4 in-file unit tests._

