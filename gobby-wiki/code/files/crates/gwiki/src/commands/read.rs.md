---
title: crates/gwiki/src/commands/read.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/read.rs
  ranges:
  - 17-28
  - 30-57
  - 59-85
  - 87-114
  - 116-122
  - 124-152
  - 154-181
  - 183-197
  - 199-211
  - 213-219
  - 221-235
  - 237-241
  - 243-312
  - 314-320
  - 322-329
  - 331-340
  - 342-361
  - 364-378
  - 380-385
  - 388-410
  - 412-427
  - 429-442
  - 444-461
  - 463-486
  - 490-493
  - 496-501
  - 503-508
  - 512-515
  - 518-522
  - 525-532
  - 534-540
  - 542-548
  - 550-556
  - 566-592
  - 595-608
  - 611-622
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/commands/read.rs:17-28](crates/gwiki/src/commands/read.rs#L17-L28), [crates/gwiki/src/commands/read.rs:30-57](crates/gwiki/src/commands/read.rs#L30-L57), [crates/gwiki/src/commands/read.rs:59-85](crates/gwiki/src/commands/read.rs#L59-L85), [crates/gwiki/src/commands/read.rs:87-114](crates/gwiki/src/commands/read.rs#L87-L114), [crates/gwiki/src/commands/read.rs:116-122](crates/gwiki/src/commands/read.rs#L116-L122), [crates/gwiki/src/commands/read.rs:124-152](crates/gwiki/src/commands/read.rs#L124-L152), [crates/gwiki/src/commands/read.rs:154-181](crates/gwiki/src/commands/read.rs#L154-L181), [crates/gwiki/src/commands/read.rs:183-197](crates/gwiki/src/commands/read.rs#L183-L197), [crates/gwiki/src/commands/read.rs:199-211](crates/gwiki/src/commands/read.rs#L199-L211), [crates/gwiki/src/commands/read.rs:213-219](crates/gwiki/src/commands/read.rs#L213-L219), [crates/gwiki/src/commands/read.rs:221-235](crates/gwiki/src/commands/read.rs#L221-L235), [crates/gwiki/src/commands/read.rs:237-241](crates/gwiki/src/commands/read.rs#L237-L241), [crates/gwiki/src/commands/read.rs:243-312](crates/gwiki/src/commands/read.rs#L243-L312), [crates/gwiki/src/commands/read.rs:314-320](crates/gwiki/src/commands/read.rs#L314-L320), [crates/gwiki/src/commands/read.rs:322-329](crates/gwiki/src/commands/read.rs#L322-L329), [crates/gwiki/src/commands/read.rs:331-340](crates/gwiki/src/commands/read.rs#L331-L340), [crates/gwiki/src/commands/read.rs:342-361](crates/gwiki/src/commands/read.rs#L342-L361), [crates/gwiki/src/commands/read.rs:364-378](crates/gwiki/src/commands/read.rs#L364-L378), [crates/gwiki/src/commands/read.rs:380-385](crates/gwiki/src/commands/read.rs#L380-L385), [crates/gwiki/src/commands/read.rs:388-410](crates/gwiki/src/commands/read.rs#L388-L410), [crates/gwiki/src/commands/read.rs:412-427](crates/gwiki/src/commands/read.rs#L412-L427), [crates/gwiki/src/commands/read.rs:429-442](crates/gwiki/src/commands/read.rs#L429-L442), [crates/gwiki/src/commands/read.rs:444-461](crates/gwiki/src/commands/read.rs#L444-L461), [crates/gwiki/src/commands/read.rs:463-486](crates/gwiki/src/commands/read.rs#L463-L486), [crates/gwiki/src/commands/read.rs:490-493](crates/gwiki/src/commands/read.rs#L490-L493), [crates/gwiki/src/commands/read.rs:496-501](crates/gwiki/src/commands/read.rs#L496-L501), [crates/gwiki/src/commands/read.rs:503-508](crates/gwiki/src/commands/read.rs#L503-L508), [crates/gwiki/src/commands/read.rs:512-515](crates/gwiki/src/commands/read.rs#L512-L515), [crates/gwiki/src/commands/read.rs:518-522](crates/gwiki/src/commands/read.rs#L518-L522), [crates/gwiki/src/commands/read.rs:525-532](crates/gwiki/src/commands/read.rs#L525-L532), [crates/gwiki/src/commands/read.rs:534-540](crates/gwiki/src/commands/read.rs#L534-L540), [crates/gwiki/src/commands/read.rs:542-548](crates/gwiki/src/commands/read.rs#L542-L548), [crates/gwiki/src/commands/read.rs:550-556](crates/gwiki/src/commands/read.rs#L550-L556), [crates/gwiki/src/commands/read.rs:566-592](crates/gwiki/src/commands/read.rs#L566-L592), [crates/gwiki/src/commands/read.rs:595-608](crates/gwiki/src/commands/read.rs#L595-L608), [crates/gwiki/src/commands/read.rs:611-622](crates/gwiki/src/commands/read.rs#L611-L622)

</details>

# crates/gwiki/src/commands/read.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Implements the `read` command for scoped wiki content: `execute` resolves the command scope, dispatches to `read_path` or `read_title`, and then `render`s the result into a `CommandOutcome`. The path flow normalizes and validates the requested path, rejects unreadable or missing targets, and reads an existing file with byte limits and truncation handling. The title flow rejects empty titles, gathers title candidates with bounded depth and scan budget, and returns structured outcomes for found, not found, invalid, ambiguous, or empty matches. Supporting types and helpers organize the request, candidate search, degradation labels, and serialized read output so all cases are reported consistently.
[crates/gwiki/src/commands/read.rs:17-28]
[crates/gwiki/src/commands/read.rs:30-57]
[crates/gwiki/src/commands/read.rs:59-85]
[crates/gwiki/src/commands/read.rs:87-114]
[crates/gwiki/src/commands/read.rs:116-122]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `execute` | function | `pub(crate) fn execute(` | `execute [function]` | `8ef9ebe1-e821-5d37-a487-ea104e22da2f` | 17-28 [crates/gwiki/src/commands/read.rs:17-28] | Indexed function `execute` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:17-28] |
| `read_path` | function | `fn read_path(` | `read_path [function]` | `8b19ef2b-ddc2-58cf-ba52-edf8ce04d3a0` | 30-57 [crates/gwiki/src/commands/read.rs:30-57] | Indexed function `read_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:30-57] |
| `read_title` | function | `fn read_title(root: &Path, scope: ScopeIdentity, title: String) -> Result<ReadOutput, WikiError> {` | `read_title [function]` | `bc93b476-82e4-5872-a117-229688f09085` | 59-85 [crates/gwiki/src/commands/read.rs:59-85] | Indexed function `read_title` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:59-85] |
| `read_existing_path` | function | `fn read_existing_path(` | `read_existing_path [function]` | `618f961f-ece7-547c-9ef2-32dd21fcba44` | 87-114 [crates/gwiki/src/commands/read.rs:87-114] | Indexed function `read_existing_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:87-114] |
| `configured_read_max_bytes` | function | `fn configured_read_max_bytes() -> usize {` | `configured_read_max_bytes [function]` | `8db5548b-39f6-510b-afaf-eb7c903af6e0` | 116-122 [crates/gwiki/src/commands/read.rs:116-122] | Indexed function `configured_read_max_bytes` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:116-122] |
| `read_markdown_prefix` | function | `fn read_markdown_prefix(path: &Path, max_bytes: usize) -> Result<(String, bool), WikiError> {` | `read_markdown_prefix [function]` | `4752581d-a145-5cad-8492-936cf8aea52f` | 124-152 [crates/gwiki/src/commands/read.rs:124-152] | Indexed function `read_markdown_prefix` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:124-152] |
| `normalize_requested_path` | function | `fn normalize_requested_path(path: &Path) -> Result<PathBuf, ReadDegradation> {` | `normalize_requested_path [function]` | `c1d97539-ecb6-595f-9937-1ccf733333db` | 154-181 [crates/gwiki/src/commands/read.rs:154-181] | Indexed function `normalize_requested_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:154-181] |
| `readable_path_degradation` | function | `fn readable_path_degradation(path: &Path) -> Option<ReadDegradation> {` | `readable_path_degradation [function]` | `6dcd34d6-793b-5efe-b85a-6beaef1bc5f6` | 183-197 [crates/gwiki/src/commands/read.rs:183-197] | Indexed function `readable_path_degradation` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:183-197] |
| `is_readable_wiki_path` | function | `fn is_readable_wiki_path(path: &Path) -> bool {` | `is_readable_wiki_path [function]` | `ecf9bb0b-e2ed-5a88-89d0-7e1f5071c190` | 199-211 [crates/gwiki/src/commands/read.rs:199-211] | Indexed function `is_readable_wiki_path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:199-211] |
| `title_candidates` | function | `fn title_candidates(` | `title_candidates [function]` | `a3742e2b-25aa-58db-9922-9d586430e030` | 213-219 [crates/gwiki/src/commands/read.rs:213-219] | Indexed function `title_candidates` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:213-219] |
| `title_candidates_with_scan_budget` | function | `fn title_candidates_with_scan_budget(` | `title_candidates_with_scan_budget [function]` | `cc4905c4-a855-5f7a-9e8b-4a3da9ce20aa` | 221-235 [crates/gwiki/src/commands/read.rs:221-235] | Indexed function `title_candidates_with_scan_budget` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:221-235] |
| `TitleCandidateSearch` | class | `struct TitleCandidateSearch {` | `TitleCandidateSearch [class]` | `1a69fb0f-2831-5354-924f-1325af61f872` | 237-241 [crates/gwiki/src/commands/read.rs:237-241] | Indexed class `TitleCandidateSearch` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:237-241] |
| `collect_title_candidates` | function | `fn collect_title_candidates(` | `collect_title_candidates [function]` | `c69b92d5-d3fc-5490-a8f5-b05936460d1c` | 243-312 [crates/gwiki/src/commands/read.rs:243-312] | Indexed function `collect_title_candidates` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:243-312] |
| `first_heading` | function | `fn first_heading(content: &str) -> Option<String> {` | `first_heading [function]` | `3049abc2-c0f7-52de-ae38-e11f4371afbe` | 314-320 [crates/gwiki/src/commands/read.rs:314-320] | Indexed function `first_heading` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:314-320] |
| `normal_components` | function | `fn normal_components(path: &Path) -> Vec<&str> {` | `normal_components [function]` | `8e71259b-5b72-5508-bb44-9e19f4adef6e` | 322-329 [crates/gwiki/src/commands/read.rs:322-329] | Indexed function `normal_components` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:322-329] |
| `render` | function | `fn render(output: ReadOutput) -> Result<CommandOutcome, WikiError> {` | `render [function]` | `6d876fd2-62f4-5ba5-95b3-37fce8f8dcd5` | 331-340 [crates/gwiki/src/commands/read.rs:331-340] | Indexed function `render` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:331-340] |
| `render_text` | function | `fn render_text(output: &ReadOutput) -> String {` | `render_text [function]` | `fb431efe-60c4-5b5a-aa3d-ffab11d21221` | 342-361 [crates/gwiki/src/commands/read.rs:342-361] | Indexed function `render_text` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:342-361] |
| `ReadOutput` | class | `struct ReadOutput {` | `ReadOutput [class]` | `2a815644-c1f4-59b4-ba6c-f020352a3fdb` | 364-378 [crates/gwiki/src/commands/read.rs:364-378] | Indexed class `ReadOutput` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:364-378] |
| `ReadFoundContent` | class | `struct ReadFoundContent {` | `ReadFoundContent [class]` | `c868272f-3cd9-510b-b46c-204036a1672f` | 380-385 [crates/gwiki/src/commands/read.rs:380-385] | Indexed class `ReadFoundContent` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:380-385] |
| `ReadOutput::found` | method | `fn found(` | `ReadOutput::found [method]` | `b3275715-2e50-5156-98a7-2648588d4ca5` | 388-410 [crates/gwiki/src/commands/read.rs:388-410] | Indexed method `ReadOutput::found` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:388-410] |
| `ReadOutput::not_found` | method | `fn not_found(` | `ReadOutput::not_found [method]` | `63b15e49-ea04-5bc2-95a5-b3560b04c82c` | 412-427 [crates/gwiki/src/commands/read.rs:412-427] | Indexed method `ReadOutput::not_found` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:412-427] |
| `ReadOutput::invalid_request` | method | `fn invalid_request(` | `ReadOutput::invalid_request [method]` | `cc7aba31-b51c-5b99-b4d4-b3e3adc46694` | 429-442 [crates/gwiki/src/commands/read.rs:429-442] | Indexed method `ReadOutput::invalid_request` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:429-442] |
| `ReadOutput::ambiguous` | method | `fn ambiguous(` | `ReadOutput::ambiguous [method]` | `2c545177-9e04-59de-9af9-17290f47995f` | 444-461 [crates/gwiki/src/commands/read.rs:444-461] | Indexed method `ReadOutput::ambiguous` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:444-461] |
| `ReadOutput::empty` | method | `fn empty(` | `ReadOutput::empty [method]` | `d9117254-d2a7-557d-b482-7a4863ca8cad` | 463-486 [crates/gwiki/src/commands/read.rs:463-486] | Indexed method `ReadOutput::empty` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:463-486] |
| `ReadRequested` | class | `struct ReadRequested {` | `ReadRequested [class]` | `29316e64-2e34-5da2-828b-475ad7d11711` | 490-493 [crates/gwiki/src/commands/read.rs:490-493] | Indexed class `ReadRequested` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:490-493] |
| `ReadRequested::path` | method | `fn path(value: String) -> Self {` | `ReadRequested::path [method]` | `9cb98ce0-d9b4-52c5-a5ac-4209f757cf3e` | 496-501 [crates/gwiki/src/commands/read.rs:496-501] | Indexed method `ReadRequested::path` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:496-501] |
| `ReadRequested::title` | method | `fn title(value: String) -> Self {` | `ReadRequested::title [method]` | `12391654-7d30-530c-b678-89cbc2076241` | 503-508 [crates/gwiki/src/commands/read.rs:503-508] | Indexed method `ReadRequested::title` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:503-508] |
| `ReadCandidate` | class | `struct ReadCandidate {` | `ReadCandidate [class]` | `664c5e6e-cad1-52af-8437-be1a041bf562` | 512-515 [crates/gwiki/src/commands/read.rs:512-515] | Indexed class `ReadCandidate` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:512-515] |
| `ReadDegradation` | class | `struct ReadDegradation {` | `ReadDegradation [class]` | `f0e5b7e0-fb48-57da-a459-45dcae530e83` | 518-522 [crates/gwiki/src/commands/read.rs:518-522] | Indexed class `ReadDegradation` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:518-522] |
| `ReadDegradation::display_label` | method | `fn display_label(&self) -> &'static str {` | `ReadDegradation::display_label [method]` | `bf25fb1c-cf19-55b6-9e8d-867bd1c97991` | 525-532 [crates/gwiki/src/commands/read.rs:525-532] | Indexed method `ReadDegradation::display_label` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:525-532] |
| `ReadDegradation::invalid_request` | method | `fn invalid_request(message: impl Into<String>) -> Self {` | `ReadDegradation::invalid_request [method]` | `a9f22573-87ef-59fa-9fc3-5186f7eccee5` | 534-540 [crates/gwiki/src/commands/read.rs:534-540] | Indexed method `ReadDegradation::invalid_request` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:534-540] |
| `ReadDegradation::not_found` | method | `fn not_found(message: impl Into<String>) -> Self {` | `ReadDegradation::not_found [method]` | `bc192068-8595-5615-aa9e-abdd4bde19a0` | 542-548 [crates/gwiki/src/commands/read.rs:542-548] | Indexed method `ReadDegradation::not_found` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:542-548] |
| `ReadDegradation::ambiguous` | method | `fn ambiguous(message: impl Into<String>) -> Self {` | `ReadDegradation::ambiguous [method]` | `f0b6c883-863d-591c-8006-aaf9fb3cc649` | 550-556 [crates/gwiki/src/commands/read.rs:550-556] | Indexed method `ReadDegradation::ambiguous` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:550-556] |
| `read_path_caps_content_and_marks_truncated` | function | `fn read_path_caps_content_and_marks_truncated() {` | `read_path_caps_content_and_marks_truncated [function]` | `ced3ed5e-1c79-54b3-899d-50b780203db4` | 566-592 [crates/gwiki/src/commands/read.rs:566-592] | Indexed function `read_path_caps_content_and_marks_truncated` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:566-592] |
| `title_search_stops_at_max_depth` | function | `fn title_search_stops_at_max_depth() {` | `title_search_stops_at_max_depth [function]` | `78c0f306-caf7-5a6a-b5b6-0238d9da34d8` | 595-608 [crates/gwiki/src/commands/read.rs:595-608] | Indexed function `title_search_stops_at_max_depth` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:595-608] |
| `title_search_stops_at_scan_budget` | function | `fn title_search_stops_at_scan_budget() {` | `title_search_stops_at_scan_budget [function]` | `971e1604-aee8-565b-b053-8e25fb6b38d2` | 611-622 [crates/gwiki/src/commands/read.rs:611-622] | Indexed function `title_search_stops_at_scan_budget` in `crates/gwiki/src/commands/read.rs`. [crates/gwiki/src/commands/read.rs:611-622] |
