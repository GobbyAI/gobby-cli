---
title: crates/gcode/src/index/semantic.rs
type: code_file
provenance:
- file: crates/gcode/src/index/semantic.rs
  ranges:
  - 15-23
  - 26-29
  - 33-43
  - 45-50
  - 53-55
  - 57-85
  - 87-105
  - 107-122
  - 124-135
  - 137-145
  - 147-153
  - 155-175
  - 177-210
  - 215-231
  - 233-240
  - 242-248
  - 251-256
  - 259-271
  - 274-295
  - 297-302
  - 304-330
  - 332-335
  - 337-339
  - 341-356
  - 358-366
  - 369-399
  - 401-413
  - 415-433
  - 435-463
  - 465-475
  - 477-483
  - 485-490
  - 492-494
  - 498-504
  - 508-543
  - 546-552
  - 554-572
  - 574-596
  - 598-630
  - 632-640
  - 651-658
  - 661-673
  - 676-685
  - 688-693
  - 696-702
  - 705-723
  - 726-746
  - 749-762
  - 765-798
  - 801-819
  - 823-827
  - 831-835
  - 839-844
  - 848-853
  - 858-882
  - 885-920
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/semantic.rs:15-23](crates/gcode/src/index/semantic.rs#L15-L23), [crates/gcode/src/index/semantic.rs:26-29](crates/gcode/src/index/semantic.rs#L26-L29), [crates/gcode/src/index/semantic.rs:33-43](crates/gcode/src/index/semantic.rs#L33-L43), [crates/gcode/src/index/semantic.rs:45-50](crates/gcode/src/index/semantic.rs#L45-L50), [crates/gcode/src/index/semantic.rs:53-55](crates/gcode/src/index/semantic.rs#L53-L55), [crates/gcode/src/index/semantic.rs:57-85](crates/gcode/src/index/semantic.rs#L57-L85), [crates/gcode/src/index/semantic.rs:87-105](crates/gcode/src/index/semantic.rs#L87-L105), [crates/gcode/src/index/semantic.rs:107-122](crates/gcode/src/index/semantic.rs#L107-L122), [crates/gcode/src/index/semantic.rs:124-135](crates/gcode/src/index/semantic.rs#L124-L135), [crates/gcode/src/index/semantic.rs:137-145](crates/gcode/src/index/semantic.rs#L137-L145), [crates/gcode/src/index/semantic.rs:147-153](crates/gcode/src/index/semantic.rs#L147-L153), [crates/gcode/src/index/semantic.rs:155-175](crates/gcode/src/index/semantic.rs#L155-L175), [crates/gcode/src/index/semantic.rs:177-210](crates/gcode/src/index/semantic.rs#L177-L210), [crates/gcode/src/index/semantic.rs:215-231](crates/gcode/src/index/semantic.rs#L215-L231), [crates/gcode/src/index/semantic.rs:233-240](crates/gcode/src/index/semantic.rs#L233-L240), [crates/gcode/src/index/semantic.rs:242-248](crates/gcode/src/index/semantic.rs#L242-L248), [crates/gcode/src/index/semantic.rs:251-256](crates/gcode/src/index/semantic.rs#L251-L256), [crates/gcode/src/index/semantic.rs:259-271](crates/gcode/src/index/semantic.rs#L259-L271), [crates/gcode/src/index/semantic.rs:274-295](crates/gcode/src/index/semantic.rs#L274-L295), [crates/gcode/src/index/semantic.rs:297-302](crates/gcode/src/index/semantic.rs#L297-L302), [crates/gcode/src/index/semantic.rs:304-330](crates/gcode/src/index/semantic.rs#L304-L330), [crates/gcode/src/index/semantic.rs:332-335](crates/gcode/src/index/semantic.rs#L332-L335), [crates/gcode/src/index/semantic.rs:337-339](crates/gcode/src/index/semantic.rs#L337-L339), [crates/gcode/src/index/semantic.rs:341-356](crates/gcode/src/index/semantic.rs#L341-L356), [crates/gcode/src/index/semantic.rs:358-366](crates/gcode/src/index/semantic.rs#L358-L366), [crates/gcode/src/index/semantic.rs:369-399](crates/gcode/src/index/semantic.rs#L369-L399), [crates/gcode/src/index/semantic.rs:401-413](crates/gcode/src/index/semantic.rs#L401-L413), [crates/gcode/src/index/semantic.rs:415-433](crates/gcode/src/index/semantic.rs#L415-L433), [crates/gcode/src/index/semantic.rs:435-463](crates/gcode/src/index/semantic.rs#L435-L463), [crates/gcode/src/index/semantic.rs:465-475](crates/gcode/src/index/semantic.rs#L465-L475), [crates/gcode/src/index/semantic.rs:477-483](crates/gcode/src/index/semantic.rs#L477-L483), [crates/gcode/src/index/semantic.rs:485-490](crates/gcode/src/index/semantic.rs#L485-L490), [crates/gcode/src/index/semantic.rs:492-494](crates/gcode/src/index/semantic.rs#L492-L494), [crates/gcode/src/index/semantic.rs:498-504](crates/gcode/src/index/semantic.rs#L498-L504), [crates/gcode/src/index/semantic.rs:508-543](crates/gcode/src/index/semantic.rs#L508-L543), [crates/gcode/src/index/semantic.rs:546-552](crates/gcode/src/index/semantic.rs#L546-L552), [crates/gcode/src/index/semantic.rs:554-572](crates/gcode/src/index/semantic.rs#L554-L572), [crates/gcode/src/index/semantic.rs:574-596](crates/gcode/src/index/semantic.rs#L574-L596), [crates/gcode/src/index/semantic.rs:598-630](crates/gcode/src/index/semantic.rs#L598-L630), [crates/gcode/src/index/semantic.rs:632-640](crates/gcode/src/index/semantic.rs#L632-L640), [crates/gcode/src/index/semantic.rs:651-658](crates/gcode/src/index/semantic.rs#L651-L658), [crates/gcode/src/index/semantic.rs:661-673](crates/gcode/src/index/semantic.rs#L661-L673), [crates/gcode/src/index/semantic.rs:676-685](crates/gcode/src/index/semantic.rs#L676-L685), [crates/gcode/src/index/semantic.rs:688-693](crates/gcode/src/index/semantic.rs#L688-L693), [crates/gcode/src/index/semantic.rs:696-702](crates/gcode/src/index/semantic.rs#L696-L702), [crates/gcode/src/index/semantic.rs:705-723](crates/gcode/src/index/semantic.rs#L705-L723), [crates/gcode/src/index/semantic.rs:726-746](crates/gcode/src/index/semantic.rs#L726-L746), [crates/gcode/src/index/semantic.rs:749-762](crates/gcode/src/index/semantic.rs#L749-L762), [crates/gcode/src/index/semantic.rs:765-798](crates/gcode/src/index/semantic.rs#L765-L798), [crates/gcode/src/index/semantic.rs:801-819](crates/gcode/src/index/semantic.rs#L801-L819), [crates/gcode/src/index/semantic.rs:823-827](crates/gcode/src/index/semantic.rs#L823-L827), [crates/gcode/src/index/semantic.rs:831-835](crates/gcode/src/index/semantic.rs#L831-L835), [crates/gcode/src/index/semantic.rs:839-844](crates/gcode/src/index/semantic.rs#L839-L844), [crates/gcode/src/index/semantic.rs:848-853](crates/gcode/src/index/semantic.rs#L848-L853), [crates/gcode/src/index/semantic.rs:858-882](crates/gcode/src/index/semantic.rs#L858-L882), [crates/gcode/src/index/semantic.rs:885-920](crates/gcode/src/index/semantic.rs#L885-L920)

</details>

# crates/gcode/src/index/semantic.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Provides C/C++ semantic call indexing for `gcode` by wrapping `clangd` and turning `textDocument/definition` responses into `SemanticCallTarget` values. `SemanticCallRequest`, `SemanticCallResolver`, and `ClangdResolver` drive the request/response flow, while helpers handle compile_commands discovery, command parsing, URI/path conversion, macro and definition classification, and JSON-RPC/stdout plumbing. The file also includes tests covering resolver behavior, path handling, command parsing, and local-vs-external definition resolution.
[crates/gcode/src/index/semantic.rs:15-23]
[crates/gcode/src/index/semantic.rs:26-29]
[crates/gcode/src/index/semantic.rs:33-43]
[crates/gcode/src/index/semantic.rs:45-50]
[crates/gcode/src/index/semantic.rs:53-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `SemanticCallRequest` | class | `pub(crate) struct SemanticCallRequest<'a> {` | `SemanticCallRequest [class]` | `d7e257c7-bd4e-5cf9-9346-e9eb9fc2c15a` | 15-23 [crates/gcode/src/index/semantic.rs:15-23] | Indexed class `SemanticCallRequest` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:15-23] |
| `SemanticCallTarget` | class | `pub(crate) struct SemanticCallTarget {` | `SemanticCallTarget [class]` | `2d49e560-6cb2-56b3-a686-6949008c9a57` | 26-29 [crates/gcode/src/index/semantic.rs:26-29] | Indexed class `SemanticCallTarget` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:26-29] |
| `SemanticTargetKind` | type | `pub(crate) enum SemanticTargetKind {` | `SemanticTargetKind [type]` | `b2a845c2-f545-5988-8564-0a89e440e368` | 33-43 [crates/gcode/src/index/semantic.rs:33-43] | Indexed type `SemanticTargetKind` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:33-43] |
| `SemanticCallResolver` | type | `pub(crate) trait SemanticCallResolver {` | `SemanticCallResolver [type]` | `ddef2595-7abc-5c61-9ac4-fcd6cb14edd9` | 45-50 [crates/gcode/src/index/semantic.rs:45-50] | Indexed type `SemanticCallResolver` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:45-50] |
| `DefinitionLocation` | class | `pub(crate) struct DefinitionLocation {` | `DefinitionLocation [class]` | `ea93d601-e579-5d8b-8819-005291841354` | 53-55 [crates/gcode/src/index/semantic.rs:53-55] | Indexed class `DefinitionLocation` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:53-55] |
| `create_cpp_semantic_resolver` | function | `pub(crate) fn create_cpp_semantic_resolver(` | `create_cpp_semantic_resolver [function]` | `3c7cdeca-6958-5dc9-b6c1-bfe0442af9e1` | 57-85 [crates/gcode/src/index/semantic.rs:57-85] | Indexed function `create_cpp_semantic_resolver` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:57-85] |
| `discover_compile_commands_dir` | function | `pub(crate) fn discover_compile_commands_dir(root_path: &Path) -> Option<PathBuf> {` | `discover_compile_commands_dir [function]` | `480291b1-4729-5dce-956b-6f1cdd9cc82a` | 87-105 [crates/gcode/src/index/semantic.rs:87-105] | Indexed function `discover_compile_commands_dir` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:87-105] |
| `classify_definition` | function | `pub(crate) fn classify_definition(` | `classify_definition [function]` | `da58cc68-e2a7-57dd-ae49-a493a8525043` | 107-122 [crates/gcode/src/index/semantic.rs:107-122] | Indexed function `classify_definition` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:107-122] |
| `locations_from_lsp_response` | function | `pub(crate) fn locations_from_lsp_response(response: &Value) -> Vec<DefinitionLocation> {` | `locations_from_lsp_response [function]` | `87ca6c91-4d51-530b-8738-20da6c99fca7` | 124-135 [crates/gcode/src/index/semantic.rs:124-135] | Indexed function `locations_from_lsp_response` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:124-135] |
| `location_from_lsp_value` | function | `fn location_from_lsp_value(value: &Value) -> Option<DefinitionLocation> {` | `location_from_lsp_value [function]` | `38861617-1632-5848-b331-2df0d8ffdaf0` | 137-145 [crates/gcode/src/index/semantic.rs:137-145] | Indexed function `location_from_lsp_value` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:137-145] |
| `source_defines_macro` | function | `fn source_defines_macro(source: &[u8], callee_name: &str) -> bool {` | `source_defines_macro [function]` | `a79e8fb6-8834-5511-8ca9-3bb8763ebbcd` | 147-153 [crates/gcode/src/index/semantic.rs:147-153] | Indexed function `source_defines_macro` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:147-153] |
| `logical_source_lines` | function | `fn logical_source_lines(text: &str) -> Vec<String> {` | `logical_source_lines [function]` | `c3887d7c-b89d-57ab-8229-cbde7dd4cc69` | 155-175 [crates/gcode/src/index/semantic.rs:155-175] | Indexed function `logical_source_lines` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:155-175] |
| `macro_definition_name` | function | `fn macro_definition_name(line: &str) -> Option<&str> {` | `macro_definition_name [function]` | `eab128ba-f13a-5566-8f98-7cd3406dcfa9` | 177-210 [crates/gcode/src/index/semantic.rs:177-210] | Indexed function `macro_definition_name` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:177-210] |
| `definition_target_kind` | function | `fn definition_target_kind(path: &Path, root_path: &Path) -> Option<SemanticTargetKind> {` | `definition_target_kind [function]` | `9c89adb8-07bd-576f-887e-7ac8870af043` | 215-231 [crates/gcode/src/index/semantic.rs:215-231] | Indexed function `definition_target_kind` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:215-231] |
| `resolve_clangd_command` | function | `fn resolve_clangd_command() -> Option<String> {` | `resolve_clangd_command [function]` | `88c025bd-92af-5674-9b52-4102f50ae443` | 233-240 [crates/gcode/src/index/semantic.rs:233-240] | Indexed function `resolve_clangd_command` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:233-240] |
| `parse_clangd_command` | function | `fn parse_clangd_command(command: &str) -> anyhow::Result<Vec<String>> {` | `parse_clangd_command [function]` | `b2ebb8d5-944e-5b4c-9574-19f3d15c7193` | 242-248 [crates/gcode/src/index/semantic.rs:242-248] | Indexed function `parse_clangd_command` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:242-248] |
| `find_executable_in_path` | function | `fn find_executable_in_path(name: &str) -> Option<PathBuf> {` | `find_executable_in_path [function]` | `718c1aa3-809e-5cf1-ba80-aba562d73f8a` | 251-256 [crates/gcode/src/index/semantic.rs:251-256] | Indexed function `find_executable_in_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:251-256] |
| `find_executable_in_path` | function | `fn find_executable_in_path(name: &str) -> Option<PathBuf> {` | `find_executable_in_path [function]` | `381b8633-022a-5f1c-86cd-44344f0123a9` | 259-271 [crates/gcode/src/index/semantic.rs:259-271] | Indexed function `find_executable_in_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:259-271] |
| `executable_name_candidates` | function | `fn executable_name_candidates(name: &str) -> Vec<PathBuf> {` | `executable_name_candidates [function]` | `bc9ce92a-d077-501c-8a50-d60d24041a8d` | 274-295 [crates/gcode/src/index/semantic.rs:274-295] | Indexed function `executable_name_candidates` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:274-295] |
| `env_flag` | function | `fn env_flag(name: &str) -> bool {` | `env_flag [function]` | `fd67c4fb-9ad9-57bb-9fa7-883e4d27cf1e` | 297-302 [crates/gcode/src/index/semantic.rs:297-302] | Indexed function `env_flag` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:297-302] |
| `path_to_uri` | function | `fn path_to_uri(path: &Path) -> String {` | `path_to_uri [function]` | `ab339207-f159-566c-91dc-a3ef689b0486` | 304-330 [crates/gcode/src/index/semantic.rs:304-330] | Indexed function `path_to_uri` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:304-330] |
| `is_windows_drive_prefix` | function | `fn is_windows_drive_prefix(part: &str) -> bool {` | `is_windows_drive_prefix [function]` | `c591fdad-23a3-5b3d-b91e-386553fd7246` | 332-335 [crates/gcode/src/index/semantic.rs:332-335] | Indexed function `is_windows_drive_prefix` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:332-335] |
| `is_windows_drive_path` | function | `fn is_windows_drive_path(path: &str) -> bool {` | `is_windows_drive_path [function]` | `337b8f90-dfc1-51b1-824e-bd550f76967f` | 337-339 [crates/gcode/src/index/semantic.rs:337-339] | Indexed function `is_windows_drive_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:337-339] |
| `file_uri_to_path` | function | `fn file_uri_to_path(uri: &str) -> Option<PathBuf> {` | `file_uri_to_path [function]` | `d1da41ff-c0a1-5f73-a38d-3e9f202db80c` | 341-356 [crates/gcode/src/index/semantic.rs:341-356] | Indexed function `file_uri_to_path` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:341-356] |
| `ClangdResolver` | class | `struct ClangdResolver {` | `ClangdResolver [class]` | `71337d66-7242-5196-a2d8-6f2b4db5b2ab` | 358-366 [crates/gcode/src/index/semantic.rs:358-366] | Indexed class `ClangdResolver` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:358-366] |
| `ClangdResolver::start` | method | `fn start(root_path: &Path, compile_commands_dir: &Path, clangd: &str) -> anyhow::Result<Self> {` | `ClangdResolver::start [method]` | `69ecd6ca-55a9-5d9c-89e0-e8908fd38311` | 369-399 [crates/gcode/src/index/semantic.rs:369-399] | Indexed method `ClangdResolver::start` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:369-399] |
| `ClangdResolver::initialize` | method | `fn initialize(&mut self) -> anyhow::Result<()> {` | `ClangdResolver::initialize [method]` | `19be58a9-d3aa-5a52-80f3-6a03b50e7306` | 401-413 [crates/gcode/src/index/semantic.rs:401-413] | Indexed method `ClangdResolver::initialize` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:401-413] |
| `ClangdResolver::ensure_open` | method | `fn ensure_open(&mut self, request: &SemanticCallRequest<'_>) -> anyhow::Result<()> {` | `ClangdResolver::ensure_open [method]` | `324a5fca-4f0e-5dee-a81f-fee2c499d7f8` | 415-433 [crates/gcode/src/index/semantic.rs:415-433] | Indexed method `ClangdResolver::ensure_open` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:415-433] |
| `ClangdResolver::close_open_files` | method | `fn close_open_files(&mut self) -> anyhow::Result<()> {` | `ClangdResolver::close_open_files [method]` | `7cff9c52-f397-5370-ae9b-c8427c5a8564` | 435-463 [crates/gcode/src/index/semantic.rs:435-463] | Indexed method `ClangdResolver::close_open_files` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:435-463] |
| `ClangdResolver::send_request` | method | `fn send_request(&mut self, method: &str, params: Value) -> anyhow::Result<u64> {` | `ClangdResolver::send_request [method]` | `dc69bc13-c5d5-5d7b-980e-1b582547f071` | 465-475 [crates/gcode/src/index/semantic.rs:465-475] | Indexed method `ClangdResolver::send_request` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:465-475] |
| `ClangdResolver::send_notification` | method | `fn send_notification(&mut self, method: &str, params: Value) -> anyhow::Result<()> {` | `ClangdResolver::send_notification [method]` | `545e8891-050e-5247-ae86-37e69ad7f05d` | 477-483 [crates/gcode/src/index/semantic.rs:477-483] | Indexed method `ClangdResolver::send_notification` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:477-483] |
| `ClangdResolver::write_message` | method | `fn write_message(&mut self, value: Value) -> anyhow::Result<()> {` | `ClangdResolver::write_message [method]` | `6033e934-7240-5c19-904f-4789db61690c` | 485-490 [crates/gcode/src/index/semantic.rs:485-490] | Indexed method `ClangdResolver::write_message` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:485-490] |
| `ClangdResolver::read_response` | method | `fn read_response(&mut self, id: u64) -> anyhow::Result<Value> {` | `ClangdResolver::read_response [method]` | `80fc5614-3a8e-512e-9ce5-873a7b5b5c1b` | 492-494 [crates/gcode/src/index/semantic.rs:492-494] | Indexed method `ClangdResolver::read_response` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:492-494] |
| `ClangdResolver::drop` | method | `fn drop(&mut self) {` | `ClangdResolver::drop [method]` | `22b75ded-a786-522d-b670-61ac69ac7a4b` | 498-504 [crates/gcode/src/index/semantic.rs:498-504] | Indexed method `ClangdResolver::drop` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:498-504] |
| `ClangdResolver::resolve` | method | `fn resolve(` | `ClangdResolver::resolve [method]` | `bd7161b8-2543-541b-865c-953f7a1f3a44` | 508-543 [crates/gcode/src/index/semantic.rs:508-543] | Indexed method `ClangdResolver::resolve` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:508-543] |
| `spawn_clangd_stdout_reader` | function | `fn spawn_clangd_stdout_reader(` | `spawn_clangd_stdout_reader [function]` | `1735713e-e726-5657-98a1-1363a95d068e` | 546-552 [crates/gcode/src/index/semantic.rs:546-552] | Indexed function `spawn_clangd_stdout_reader` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:546-552] |
| `read_clangd_stdout` | function | `fn read_clangd_stdout(mut reader: impl BufRead, tx: Sender<anyhow::Result<Value>>) {` | `read_clangd_stdout [function]` | `e7b3c5c3-67ca-59c6-a9c2-e6b15c36aa0a` | 554-572 [crates/gcode/src/index/semantic.rs:554-572] | Indexed function `read_clangd_stdout` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:554-572] |
| `read_json_rpc_message` | function | `fn read_json_rpc_message(reader: &mut impl BufRead) -> anyhow::Result<Option<Value>> {` | `read_json_rpc_message [function]` | `73e1090c-8e7c-5cfc-a6a9-4bd7df5907ae` | 574-596 [crates/gcode/src/index/semantic.rs:574-596] | Indexed function `read_json_rpc_message` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:574-596] |
| `read_response_from_channel` | function | `fn read_response_from_channel(` | `read_response_from_channel [function]` | `6276a983-4a75-55d8-97c0-cbf1ead9b9e5` | 598-630 [crates/gcode/src/index/semantic.rs:598-630] | Indexed function `read_response_from_channel` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:598-630] |
| `format_clangd_timeout` | function | `fn format_clangd_timeout(timeout: Duration) -> String {` | `format_clangd_timeout [function]` | `36ef92eb-0c35-5f04-8437-21a5bb09f84f` | 632-640 [crates/gcode/src/index/semantic.rs:632-640] | Indexed function `format_clangd_timeout` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:632-640] |
| `discovers_compile_commands_in_root_and_build_dirs` | function | `fn discovers_compile_commands_in_root_and_build_dirs() {` | `discovers_compile_commands_in_root_and_build_dirs [function]` | `f6a21484-2daf-53a8-bcee-538ffa0d9b2d` | 651-658 [crates/gcode/src/index/semantic.rs:651-658] | Indexed function `discovers_compile_commands_in_root_and_build_dirs` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:651-658] |
| `parses_lsp_location_and_location_link_results` | function | `fn parses_lsp_location_and_location_link_results() {` | `parses_lsp_location_and_location_link_results [function]` | `2b6fd088-c8cb-59d2-a776-64595ceba6ab` | 661-673 [crates/gcode/src/index/semantic.rs:661-673] | Indexed function `parses_lsp_location_and_location_link_results` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:661-673] |
| `parses_quoted_clangd_command_arguments` | function | `fn parses_quoted_clangd_command_arguments() {` | `parses_quoted_clangd_command_arguments [function]` | `8ce0343d-e812-5a32-a8e5-ae89903f1537` | 676-685 [crates/gcode/src/index/semantic.rs:676-685] | Indexed function `parses_quoted_clangd_command_arguments` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:676-685] |
| `rejects_empty_and_invalid_clangd_commands` | function | `fn rejects_empty_and_invalid_clangd_commands() {` | `rejects_empty_and_invalid_clangd_commands [function]` | `7336cc47-b290-51a2-9e87-7a0f91dcc180` | 688-693 [crates/gcode/src/index/semantic.rs:688-693] | Indexed function `rejects_empty_and_invalid_clangd_commands` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:688-693] |
| `channel_response_wait_times_out` | function | `fn channel_response_wait_times_out() {` | `channel_response_wait_times_out [function]` | `d59ddf83-efa5-52c2-ac84-b90d353f7c03` | 696-702 [crates/gcode/src/index/semantic.rs:696-702] | Indexed function `channel_response_wait_times_out` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:696-702] |
| `classifies_single_definition_outside_project_as_external` | function | `fn classifies_single_definition_outside_project_as_external() {` | `classifies_single_definition_outside_project_as_external [function]` | `20f4d65d-af15-5dc4-bc20-7e83d030ad03` | 705-723 [crates/gcode/src/index/semantic.rs:705-723] | Indexed function `classifies_single_definition_outside_project_as_external` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:705-723] |
| `classifies_single_definition_inside_project_as_local_candidate` | function | `fn classifies_single_definition_inside_project_as_local_candidate() {` | `classifies_single_definition_inside_project_as_local_candidate [function]` | `2e70c2b4-b254-5a1f-a646-481bf3cfc5d9` | 726-746 [crates/gcode/src/index/semantic.rs:726-746] | Indexed function `classifies_single_definition_inside_project_as_local_candidate` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:726-746] |
| `drops_single_definition_when_canonicalization_fails` | function | `fn drops_single_definition_when_canonicalization_fails() {` | `drops_single_definition_when_canonicalization_fails [function]` | `38e9a9d5-7c1d-5fea-a7a5-983c68219847` | 749-762 [crates/gcode/src/index/semantic.rs:749-762] | Indexed function `drops_single_definition_when_canonicalization_fails` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:749-762] |
| `leaves_empty_multiple_and_macro_definitions_unresolved` | function | `fn leaves_empty_multiple_and_macro_definitions_unresolved() {` | `leaves_empty_multiple_and_macro_definitions_unresolved [function]` | `fe404d73-0e18-5199-a513-99b83c1d7403` | 765-798 [crates/gcode/src/index/semantic.rs:765-798] | Indexed function `leaves_empty_multiple_and_macro_definitions_unresolved` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:765-798] |
| `detects_function_like_and_backslash_continued_macros` | function | `fn detects_function_like_and_backslash_continued_macros() {` | `detects_function_like_and_backslash_continued_macros [function]` | `dd91e3b4-3b60-5cf7-9e3f-e7626cde6641` | 801-819 [crates/gcode/src/index/semantic.rs:801-819] | Indexed function `detects_function_like_and_backslash_continued_macros` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:801-819] |
| `path_to_uri_encodes_absolute_path_components` | function | `fn path_to_uri_encodes_absolute_path_components() {` | `path_to_uri_encodes_absolute_path_components [function]` | `61fec119-d995-5d0a-a61b-2c7fa8301b8c` | 823-827 [crates/gcode/src/index/semantic.rs:823-827] | Indexed function `path_to_uri_encodes_absolute_path_components` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:823-827] |
| `path_to_uri_preserves_windows_drive_prefix` | function | `fn path_to_uri_preserves_windows_drive_prefix() {` | `path_to_uri_preserves_windows_drive_prefix [function]` | `1ea5d48b-398e-5c63-84a0-645b3dc0b3b8` | 831-835 [crates/gcode/src/index/semantic.rs:831-835] | Indexed function `path_to_uri_preserves_windows_drive_prefix` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:831-835] |
| `file_uri_to_path_strips_windows_drive_leading_slash` | function | `fn file_uri_to_path_strips_windows_drive_leading_slash() {` | `file_uri_to_path_strips_windows_drive_leading_slash [function]` | `8250e7ea-ff88-5c0a-b7f8-a7843923994a` | 839-844 [crates/gcode/src/index/semantic.rs:839-844] | Indexed function `file_uri_to_path_strips_windows_drive_leading_slash` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:839-844] |
| `file_uri_to_path_keeps_decoded_path_on_non_windows` | function | `fn file_uri_to_path_keeps_decoded_path_on_non_windows() {` | `file_uri_to_path_keeps_decoded_path_on_non_windows [function]` | `1fab5ff9-13c8-5666-85df-0722dd713d52` | 848-853 [crates/gcode/src/index/semantic.rs:848-853] | Indexed function `file_uri_to_path_keeps_decoded_path_on_non_windows` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:848-853] |
| `find_executable_in_path_honors_pathext_on_windows` | function | `fn find_executable_in_path_honors_pathext_on_windows() {` | `find_executable_in_path_honors_pathext_on_windows [function]` | `6ec18527-38fb-5703-8f26-32a4913fdc90` | 858-882 [crates/gcode/src/index/semantic.rs:858-882] | Indexed function `find_executable_in_path_honors_pathext_on_windows` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:858-882] |
| `optional_clangd_integration_resolves_external_definition` | function | `fn optional_clangd_integration_resolves_external_definition() {` | `optional_clangd_integration_resolves_external_definition [function]` | `d8d5f5a4-83f1-515c-9496-330e7563205d` | 885-920 [crates/gcode/src/index/semantic.rs:885-920] | Indexed function `optional_clangd_integration_resolves_external_definition` in `crates/gcode/src/index/semantic.rs`. [crates/gcode/src/index/semantic.rs:885-920] |
