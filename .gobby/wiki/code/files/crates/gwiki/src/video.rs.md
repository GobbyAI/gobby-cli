---
title: crates/gwiki/src/video.rs
type: code_file
provenance:
- file: crates/gwiki/src/video.rs
  ranges:
  - 18-21
  - 24-29
  - 32-36
  - 39-43
  - 46-49
  - 52-55
  - 58-61
  - 64-68
  - 70-94
  - 96-103
  - 105-163
  - 165-168
  - 170-178
  - 180-195
  - 197-222
  - 224-280
  - 282-292
  - 294-313
  - 315-326
  - 328-586
  - 588-603
  - 605-612
  - 614-619
  - 621-627
  - 636-663
  - 666-676
  - 679-714
  - 717-752
  - 755-848
  - 851-893
  - 895-911
  - 913-927
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/video.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/video.rs` exposes 32 indexed API symbols.
[crates/gwiki/src/video.rs:18-21]
[crates/gwiki/src/video.rs:24-29]
[crates/gwiki/src/video.rs:32-36]
[crates/gwiki/src/video.rs:39-43]
[crates/gwiki/src/video.rs:46-49]
[crates/gwiki/src/video.rs:52-55]
[crates/gwiki/src/video.rs:58-61]
[crates/gwiki/src/video.rs:64-68]
[crates/gwiki/src/video.rs:70-94]
[crates/gwiki/src/video.rs:96-103]
[crates/gwiki/src/video.rs:105-163]
[crates/gwiki/src/video.rs:165-168]
[crates/gwiki/src/video.rs:170-178]
[crates/gwiki/src/video.rs:180-195]
[crates/gwiki/src/video.rs:197-222]
[crates/gwiki/src/video.rs:224-280]
[crates/gwiki/src/video.rs:282-292]
[crates/gwiki/src/video.rs:294-313]
[crates/gwiki/src/video.rs:315-326]
[crates/gwiki/src/video.rs:328-586]
[crates/gwiki/src/video.rs:588-603]
[crates/gwiki/src/video.rs:605-612]
[crates/gwiki/src/video.rs:614-619]
[crates/gwiki/src/video.rs:621-627]
[crates/gwiki/src/video.rs:636-663]
[crates/gwiki/src/video.rs:666-676]
[crates/gwiki/src/video.rs:679-714]
[crates/gwiki/src/video.rs:717-752]
[crates/gwiki/src/video.rs:755-848]
[crates/gwiki/src/video.rs:851-893]
[crates/gwiki/src/video.rs:895-911]
[crates/gwiki/src/video.rs:913-927]

## API Symbols

- `FrameSamplingPlan` (class) component `FrameSamplingPlan [class]` (`d0f2d47c-2e6f-5706-b30c-ac596664547f`) lines 18-21 [crates/gwiki/src/video.rs:18-21]
  - Signature: `pub struct FrameSamplingPlan {`
  - Purpose: Indexed class `FrameSamplingPlan` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:18-21]
- `VideoFrameSample` (class) component `VideoFrameSample [class]` (`2a88a901-9d79-5811-b8a6-6c3e87baed44`) lines 24-29 [crates/gwiki/src/video.rs:24-29]
  - Signature: `pub struct VideoFrameSample {`
  - Purpose: Indexed class `VideoFrameSample` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:24-29]
- `VideoFrameDescription` (class) component `VideoFrameDescription [class]` (`149a6fb8-3ffb-59bd-bbb0-2d51344f70fd`) lines 32-36 [crates/gwiki/src/video.rs:32-36]
  - Signature: `pub struct VideoFrameDescription {`
  - Purpose: Indexed class `VideoFrameDescription` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:32-36]
- `AlignedVideoSegment` (class) component `AlignedVideoSegment [class]` (`1b16f91c-f47f-5cd2-9bff-7949fa2728e9`) lines 39-43 [crates/gwiki/src/video.rs:39-43]
  - Signature: `pub struct AlignedVideoSegment {`
  - Purpose: Indexed class `AlignedVideoSegment` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:39-43]
- `VideoAudioReference` (class) component `VideoAudioReference [class]` (`0efa446c-3614-5459-932c-f9b00ec6c809`) lines 46-49 [crates/gwiki/src/video.rs:46-49]
  - Signature: `pub struct VideoAudioReference {`
  - Purpose: Indexed class `VideoAudioReference` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:46-49]
- `VideoMarkdownResult` (class) component `VideoMarkdownResult [class]` (`4f92ff6a-8d3c-5f09-9eeb-f138e4286704`) lines 52-55 [crates/gwiki/src/video.rs:52-55]
  - Signature: `pub struct VideoMarkdownResult {`
  - Purpose: Indexed class `VideoMarkdownResult` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:52-55]
- `VideoMediaMetadata` (class) component `VideoMediaMetadata [class]` (`cf9f500a-4c93-534e-b363-7ee467d2f0bd`) lines 58-61 [crates/gwiki/src/video.rs:58-61]
  - Signature: `pub struct VideoMediaMetadata {`
  - Purpose: Indexed class `VideoMediaMetadata` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:58-61]
- `VideoMediaDegradation` (class) component `VideoMediaDegradation [class]` (`c40ae7e0-1054-5cca-8b7f-6a0c2749e59b`) lines 64-68 [crates/gwiki/src/video.rs:64-68]
  - Signature: `pub struct VideoMediaDegradation {`
  - Purpose: Indexed class `VideoMediaDegradation` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:64-68]
- `sample_frames` (function) component `sample_frames [function]` (`eeda002c-4818-5091-8a0a-5d594d14ed3d`) lines 70-94 [crates/gwiki/src/video.rs:70-94]
  - Signature: `pub fn sample_frames(asset_path: &Path, plan: FrameSamplingPlan) -> Vec<VideoFrameSample> {`
  - Purpose: Indexed function `sample_frames` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:70-94]
- `audio_reference_for_video` (function) component `audio_reference_for_video [function]` (`c9090ac8-7375-5727-9da6-b4c3a029e231`) lines 96-103 [crates/gwiki/src/video.rs:96-103]
  - Signature: `pub fn audio_reference_for_video(asset_path: &Path) -> VideoAudioReference {`
  - Purpose: Indexed function `audio_reference_for_video` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:96-103]
- `align_transcript_and_frames` (function) component `align_transcript_and_frames [function]` (`d9d9324e-7d2a-58da-aab3-043f02a67dcb`) lines 105-163 [crates/gwiki/src/video.rs:105-163]
  - Signature: `pub fn align_transcript_and_frames(`
  - Purpose: Indexed function `align_transcript_and_frames` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:105-163]
- `transcript_start_seconds` (function) component `transcript_start_seconds [function]` (`b081830f-1b4e-57ac-8972-4cb069a76990`) lines 165-168 [crates/gwiki/src/video.rs:165-168]
  - Signature: `fn transcript_start_seconds(segment: &TranscriptSegment) -> u32 {`
  - Purpose: Indexed function `transcript_start_seconds` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:165-168]
- `timestamp_seconds_or_zero` (function) component `timestamp_seconds_or_zero [function]` (`4258d3fc-bf86-555b-80e6-20d340157adb`) lines 170-178 [crates/gwiki/src/video.rs:170-178]
  - Signature: `fn timestamp_seconds_or_zero(value: &str, label: &str) -> u32 {`
  - Purpose: Indexed function `timestamp_seconds_or_zero` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:170-178]
- `VideoMarkdownRequest` (class) component `VideoMarkdownRequest [class]` (`afe4dc74-f6fd-5fe6-8be2-fa2723794124`) lines 180-195 [crates/gwiki/src/video.rs:180-195]
  - Signature: `pub struct VideoMarkdownRequest<'a> {`
  - Purpose: Indexed class `VideoMarkdownRequest` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:180-195]
- `write_video_derived_markdown` (function) component `write_video_derived_markdown [function]` (`8c81b61f-d00f-5108-bede-57a48beaf518`) lines 197-222 [crates/gwiki/src/video.rs:197-222]
  - Signature: `pub fn write_video_derived_markdown(`
  - Purpose: Indexed function `write_video_derived_markdown` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:197-222]
- `write_video_markdown_atomic` (function) component `write_video_markdown_atomic [function]` (`a391ee85-e936-5ecc-a4fb-19d42cd8f17a`) lines 224-280 [crates/gwiki/src/video.rs:224-280]
  - Signature: `fn write_video_markdown_atomic(path: &Path, bytes: &[u8]) -> Result<(), WikiError> {`
  - Purpose: Indexed function `write_video_markdown_atomic` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:224-280]
- `temp_sibling_path` (function) component `temp_sibling_path [function]` (`0180c287-f318-541e-b5b8-418691f8fd8c`) lines 282-292 [crates/gwiki/src/video.rs:282-292]
  - Signature: `fn temp_sibling_path(path: &Path) -> PathBuf {`
  - Purpose: Indexed function `temp_sibling_path` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:282-292]
- `sync_parent_dir` (function) component `sync_parent_dir [function]` (`dd9b2a2c-6eb5-5e8a-a3ae-5d9926dd73b5`) lines 294-313 [crates/gwiki/src/video.rs:294-313]
  - Signature: `fn sync_parent_dir(path: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `sync_parent_dir` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:294-313]
- `frame_sample` (function) component `frame_sample [function]` (`06daa396-97fe-5de7-b5ab-3b11625878ba`) lines 315-326 [crates/gwiki/src/video.rs:315-326]
  - Signature: `fn frame_sample(asset_path: &Path, timestamp_seconds: u32) -> VideoFrameSample {`
  - Purpose: Indexed function `frame_sample` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:315-326]
- `render_video_derived_markdown` (function) component `render_video_derived_markdown [function]` (`cd796e9c-3b86-53c4-aec1-cd8170bab155`) lines 328-586 [crates/gwiki/src/video.rs:328-586]
  - Signature: `fn render_video_derived_markdown(`
  - Purpose: Indexed function `render_video_derived_markdown` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:328-586]
- `parse_timestamp_seconds` (function) component `parse_timestamp_seconds [function]` (`ec447cec-83a7-54a3-a137-f65b38915bd1`) lines 588-603 [crates/gwiki/src/video.rs:588-603]
  - Signature: `fn parse_timestamp_seconds(value: &str) -> Option<u32> {`
  - Purpose: Indexed function `parse_timestamp_seconds` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:588-603]
- `parse_timestamp_part` (function) component `parse_timestamp_part [function]` (`a10c2083-6744-5651-a34a-1b41da269aa5`) lines 605-612 [crates/gwiki/src/video.rs:605-612]
  - Signature: `fn parse_timestamp_part(value: &str) -> Option<u32> {`
  - Purpose: Indexed function `parse_timestamp_part` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:605-612]
- `format_timestamp` (function) component `format_timestamp [function]` (`0fcc7bbb-02ce-5ff1-84d9-905f770c34e8`) lines 614-619 [crates/gwiki/src/video.rs:614-619]
  - Signature: `fn format_timestamp(seconds: u32) -> String {`
  - Purpose: Indexed function `format_timestamp` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:614-619]
- `format_ranges_ms` (function) component `format_ranges_ms [function]` (`ae2ffe11-f4b8-5942-b31f-937dbe7d4092`) lines 621-627 [crates/gwiki/src/video.rs:621-627]
  - Signature: `fn format_ranges_ms(ranges: &[TranscriptionRange]) -> String {`
  - Purpose: Indexed function `format_ranges_ms` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:621-627]
- `frame_sampling_records_timestamps` (function) component `frame_sampling_records_timestamps [function]` (`29988ba8-f8fc-54aa-839d-c25ec120ee93`) lines 636-663 [crates/gwiki/src/video.rs:636-663]
  - Signature: `fn frame_sampling_records_timestamps() {`
  - Purpose: Indexed function `frame_sampling_records_timestamps` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:636-663]
- `zero_frame_interval_disables_sampling` (function) component `zero_frame_interval_disables_sampling [function]` (`62c623f0-b8b1-5e9b-81a7-c373f20053cc`) lines 666-676 [crates/gwiki/src/video.rs:666-676]
  - Signature: `fn zero_frame_interval_disables_sampling() {`
  - Purpose: Indexed function `zero_frame_interval_disables_sampling` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:666-676]
- `aligns_transcript_and_frames` (function) component `aligns_transcript_and_frames [function]` (`01cc3e3c-7988-530d-8687-b5eae6ef1534`) lines 679-714 [crates/gwiki/src/video.rs:679-714]
  - Signature: `fn aligns_transcript_and_frames() {`
  - Purpose: Indexed function `aligns_transcript_and_frames` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:679-714]
- `aligns_on_numeric_start_ms` (function) component `aligns_on_numeric_start_ms [function]` (`4590065c-0476-5e6a-b5a5-6258fefdc9d1`) lines 717-752 [crates/gwiki/src/video.rs:717-752]
  - Signature: `fn aligns_on_numeric_start_ms() {`
  - Purpose: Indexed function `aligns_on_numeric_start_ms` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:717-752]
- `partial_failure_matrix` (function) component `partial_failure_matrix [function]` (`bd51bab3-7247-5b3d-9f1c-41c4b75d7bbd`) lines 755-848 [crates/gwiki/src/video.rs:755-848]
  - Signature: `fn partial_failure_matrix() {`
  - Purpose: Indexed function `partial_failure_matrix` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:755-848]
- `degradation_metadata_has_size_and_duration` (function) component `degradation_metadata_has_size_and_duration [function]` (`2e7052bf-a177-533f-8b8a-d312e2137d73`) lines 851-893 [crates/gwiki/src/video.rs:851-893]
  - Signature: `fn degradation_metadata_has_size_and_duration() {`
  - Purpose: Indexed function `degradation_metadata_has_size_and_duration` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:851-893]
- `record_for` (function) component `record_for [function]` (`7368b83a-b658-5375-ba05-abd614dc46a6`) lines 895-911 [crates/gwiki/src/video.rs:895-911]
  - Signature: `fn record_for(temp: &Path) -> SourceRecord {`
  - Purpose: Indexed function `record_for` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:895-911]
- `transcription_output` (function) component `transcription_output [function]` (`c4319b34-3552-51ce-ab42-75f2ee16a434`) lines 913-927 [crates/gwiki/src/video.rs:913-927]
  - Signature: `fn transcription_output(segments: &[TranscriptSegment]) -> TranscriptionOutput {`
  - Purpose: Indexed function `transcription_output` in `crates/gwiki/src/video.rs`. [crates/gwiki/src/video.rs:913-927]

