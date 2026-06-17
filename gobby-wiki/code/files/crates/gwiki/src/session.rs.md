---
title: crates/gwiki/src/session.rs
type: code_file
provenance:
- file: crates/gwiki/src/session.rs
  ranges:
  - 15-18
  - 21-26
  - 28-33
  - 35-39
  - 41-45
  - 49-56
  - 60-64
  - 68-76
  - 79-87
  - '90'
  - 92-94
  - 98-110
  - 112-139
  - 141-143
  - 145-147
  - 149-151
  - 153-155
  - 159-166
  - 169-179
  - 182-194
  - 197-224
  - 226-228
  - 230-289
  - 291-307
  - 309-312
  - 315-334
  - 336-345
  - 347-352
  - 354-361
  - 363-365
  - 367-383
  - 390-423
  - 426-437
  - 440-452
  - 455-463
  - 466-474
  - 477-502
  - 505-526
  - 529-550
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/session.rs:15-18](crates/gwiki/src/session.rs#L15-L18), [crates/gwiki/src/session.rs:21-26](crates/gwiki/src/session.rs#L21-L26), [crates/gwiki/src/session.rs:28-33](crates/gwiki/src/session.rs#L28-L33), [crates/gwiki/src/session.rs:35-39](crates/gwiki/src/session.rs#L35-L39), [crates/gwiki/src/session.rs:41-45](crates/gwiki/src/session.rs#L41-L45), [crates/gwiki/src/session.rs:49-56](crates/gwiki/src/session.rs#L49-L56), [crates/gwiki/src/session.rs:60-64](crates/gwiki/src/session.rs#L60-L64), [crates/gwiki/src/session.rs:68-76](crates/gwiki/src/session.rs#L68-L76), [crates/gwiki/src/session.rs:79-87](crates/gwiki/src/session.rs#L79-L87), [crates/gwiki/src/session.rs:90](crates/gwiki/src/session.rs#L90), [crates/gwiki/src/session.rs:92-94](crates/gwiki/src/session.rs#L92-L94), [crates/gwiki/src/session.rs:98-110](crates/gwiki/src/session.rs#L98-L110), [crates/gwiki/src/session.rs:112-139](crates/gwiki/src/session.rs#L112-L139), [crates/gwiki/src/session.rs:141-143](crates/gwiki/src/session.rs#L141-L143), [crates/gwiki/src/session.rs:145-147](crates/gwiki/src/session.rs#L145-L147), [crates/gwiki/src/session.rs:149-151](crates/gwiki/src/session.rs#L149-L151), [crates/gwiki/src/session.rs:153-155](crates/gwiki/src/session.rs#L153-L155), [crates/gwiki/src/session.rs:159-166](crates/gwiki/src/session.rs#L159-L166), [crates/gwiki/src/session.rs:169-179](crates/gwiki/src/session.rs#L169-L179), [crates/gwiki/src/session.rs:182-194](crates/gwiki/src/session.rs#L182-L194), [crates/gwiki/src/session.rs:197-224](crates/gwiki/src/session.rs#L197-L224), [crates/gwiki/src/session.rs:226-228](crates/gwiki/src/session.rs#L226-L228), [crates/gwiki/src/session.rs:230-289](crates/gwiki/src/session.rs#L230-L289), [crates/gwiki/src/session.rs:291-307](crates/gwiki/src/session.rs#L291-L307), [crates/gwiki/src/session.rs:309-312](crates/gwiki/src/session.rs#L309-L312), [crates/gwiki/src/session.rs:315-334](crates/gwiki/src/session.rs#L315-L334), [crates/gwiki/src/session.rs:336-345](crates/gwiki/src/session.rs#L336-L345), [crates/gwiki/src/session.rs:347-352](crates/gwiki/src/session.rs#L347-L352), [crates/gwiki/src/session.rs:354-361](crates/gwiki/src/session.rs#L354-L361), [crates/gwiki/src/session.rs:363-365](crates/gwiki/src/session.rs#L363-L365), [crates/gwiki/src/session.rs:367-383](crates/gwiki/src/session.rs#L367-L383), [crates/gwiki/src/session.rs:390-423](crates/gwiki/src/session.rs#L390-L423), [crates/gwiki/src/session.rs:426-437](crates/gwiki/src/session.rs#L426-L437), [crates/gwiki/src/session.rs:440-452](crates/gwiki/src/session.rs#L440-L452), [crates/gwiki/src/session.rs:455-463](crates/gwiki/src/session.rs#L455-L463), [crates/gwiki/src/session.rs:466-474](crates/gwiki/src/session.rs#L466-L474), [crates/gwiki/src/session.rs:477-502](crates/gwiki/src/session.rs#L477-L502), [crates/gwiki/src/session.rs:505-526](crates/gwiki/src/session.rs#L505-L526), [crates/gwiki/src/session.rs:529-550](crates/gwiki/src/session.rs#L529-L550)

</details>

# crates/gwiki/src/session.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the session and checkpoint model for `gwiki` research runs. `ResearchScope` represents either a project or topic root and can be converted from a resolved scope, while `ResearchCodeCitation` validates and stores file/line/symbol provenance for cited code. `ResearchSession` ties these together by creating sessions, tracking compile state, and saving/loading checkpoints under a vault root, with helpers to validate scope roots, normalize paths, generate session IDs, and build the research prompt.
[crates/gwiki/src/session.rs:15-18]
[crates/gwiki/src/session.rs:21-26]
[crates/gwiki/src/session.rs:28-33]
[crates/gwiki/src/session.rs:35-39]
[crates/gwiki/src/session.rs:41-45]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ResearchScope` | type | `pub enum ResearchScope {` | `ResearchScope [type]` | `1808b916-b517-58f9-8b5b-768d4e88c30b` | 15-18 [crates/gwiki/src/session.rs:15-18] | Indexed type `ResearchScope` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:15-18] |
| `ResearchScope::project_for_id` | method | `pub fn project_for_id(project_id: impl Into<String>, root: impl Into<PathBuf>) -> Self {` | `ResearchScope::project_for_id [method]` | `a88407fe-2279-55c8-bba4-d009159e3066` | 21-26 [crates/gwiki/src/session.rs:21-26] | Indexed method `ResearchScope::project_for_id` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:21-26] |
| `ResearchScope::topic` | method | `pub fn topic(name: impl Into<String>, root: impl Into<PathBuf>) -> Self {` | `ResearchScope::topic [method]` | `4da0f5af-8b4e-5a85-abe6-4dae1bbcda1c` | 28-33 [crates/gwiki/src/session.rs:28-33] | Indexed method `ResearchScope::topic` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:28-33] |
| `ResearchScope::root` | method | `pub fn root(&self) -> &Path {` | `ResearchScope::root [method]` | `7f8ee952-6560-5959-9b6d-a0ea2da9ae1e` | 35-39 [crates/gwiki/src/session.rs:35-39] | Indexed method `ResearchScope::root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:35-39] |
| `ResearchScope::set_root` | method | `fn set_root(&mut self, new_root: PathBuf) {` | `ResearchScope::set_root [method]` | `6988bf97-21bc-5f28-89da-32c00f5315c7` | 41-45 [crates/gwiki/src/session.rs:41-45] | Indexed method `ResearchScope::set_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:41-45] |
| `ResearchScope::from` | method | `fn from(scope: &ResolvedScope) -> Self {` | `ResearchScope::from [method]` | `4b031344-69e0-5a30-bc3d-0ee5e874e65d` | 49-56 [crates/gwiki/src/session.rs:49-56] | Indexed method `ResearchScope::from` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:49-56] |
| `DaemonDispatch` | class | `pub struct DaemonDispatch {` | `DaemonDispatch [class]` | `8786f3d3-8940-5edd-870b-d6a09a562e10` | 60-64 [crates/gwiki/src/session.rs:60-64] | Indexed class `DaemonDispatch` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:60-64] |
| `ResearchCodeCitation` | class | `pub struct ResearchCodeCitation {` | `ResearchCodeCitation [class]` | `848bacba-97d0-545f-9adb-3928884d2393` | 68-76 [crates/gwiki/src/session.rs:68-76] | Indexed class `ResearchCodeCitation` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:68-76] |
| `ResearchCodeCitationUnchecked` | class | `struct ResearchCodeCitationUnchecked {` | `ResearchCodeCitationUnchecked [class]` | `7426a58b-3a12-5b3e-be54-faeb406f847e` | 79-87 [crates/gwiki/src/session.rs:79-87] | Indexed class `ResearchCodeCitationUnchecked` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:79-87] |
| `ResearchCodeCitation::Error` | type | `type Error = String;` | `ResearchCodeCitation::Error [type]` | `daa59587-004b-5d84-ba7f-d98bab48e98f` | 90-90 [crates/gwiki/src/session.rs:90] | Indexed type `ResearchCodeCitation::Error` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:90] |
| `ResearchCodeCitation::try_from` | method | `fn try_from(value: ResearchCodeCitationUnchecked) -> Result<Self, Self::Error> {` | `ResearchCodeCitation::try_from [method]` | `049f2fce-ca39-5af4-9394-a9ba74703653` | 92-94 [crates/gwiki/src/session.rs:92-94] | Indexed method `ResearchCodeCitation::try_from` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:92-94] |
| `ResearchCodeCitation::new` | method | `pub fn new(` | `ResearchCodeCitation::new [method]` | `d9897627-5d63-57a1-905b-41701b00bc3f` | 98-110 [crates/gwiki/src/session.rs:98-110] | Indexed method `ResearchCodeCitation::new` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:98-110] |
| `ResearchCodeCitation::from_parts` | method | `fn from_parts(` | `ResearchCodeCitation::from_parts [method]` | `8c3d8521-6753-5fdf-82ec-360def624ce9` | 112-139 [crates/gwiki/src/session.rs:112-139] | Indexed method `ResearchCodeCitation::from_parts` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:112-139] |
| `ResearchCodeCitation::file` | method | `pub fn file(&self) -> &str {` | `ResearchCodeCitation::file [method]` | `04bc8c33-97a7-58df-940d-1b2e2db7e4da` | 141-143 [crates/gwiki/src/session.rs:141-143] | Indexed method `ResearchCodeCitation::file` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:141-143] |
| `ResearchCodeCitation::line` | method | `pub fn line(&self) -> Option<usize> {` | `ResearchCodeCitation::line [method]` | `a2dc0b6f-486a-574b-9c15-8d5ac00566c8` | 145-147 [crates/gwiki/src/session.rs:145-147] | Indexed method `ResearchCodeCitation::line` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:145-147] |
| `ResearchCodeCitation::symbol` | method | `pub fn symbol(&self) -> Option<&str> {` | `ResearchCodeCitation::symbol [method]` | `2097b105-c186-5a4a-a38e-ad07ec5aaaf6` | 149-151 [crates/gwiki/src/session.rs:149-151] | Indexed method `ResearchCodeCitation::symbol` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:149-151] |
| `ResearchCodeCitation::provenance` | method | `pub fn provenance(&self) -> &[String] {` | `ResearchCodeCitation::provenance [method]` | `086fdf1a-8fbe-5dac-ba71-e8d6475573f7` | 153-155 [crates/gwiki/src/session.rs:153-155] | Indexed method `ResearchCodeCitation::provenance` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:153-155] |
| `AcceptedResearchNote` | class | `pub struct AcceptedResearchNote {` | `AcceptedResearchNote [class]` | `eeee9703-20ec-5cf2-bad7-38e27c167591` | 159-166 [crates/gwiki/src/session.rs:159-166] | Indexed class `AcceptedResearchNote` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:159-166] |
| `CompileState` | class | `pub struct CompileState {` | `CompileState [class]` | `f8374798-95ad-5e36-b227-f563bc53b4e3` | 169-179 [crates/gwiki/src/session.rs:169-179] | Indexed class `CompileState` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:169-179] |
| `ResearchSession` | class | `pub struct ResearchSession {` | `ResearchSession [class]` | `d50bae3a-1c79-575e-b4e6-86dbf4f56ae4` | 182-194 [crates/gwiki/src/session.rs:182-194] | Indexed class `ResearchSession` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:182-194] |
| `ResearchSession::new` | method | `pub fn new(` | `ResearchSession::new [method]` | `8a539915-4364-5cc3-9c42-f8698563cc04` | 197-224 [crates/gwiki/src/session.rs:197-224] | Indexed method `ResearchSession::new` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:197-224] |
| `ResearchSession::checkpoint_path` | method | `pub fn checkpoint_path(vault_root: &Path) -> PathBuf {` | `ResearchSession::checkpoint_path [method]` | `abbad0d5-a7da-53d6-b16c-044a1ca3ba0f` | 226-228 [crates/gwiki/src/session.rs:226-228] | Indexed method `ResearchSession::checkpoint_path` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:226-228] |
| `ResearchSession::save_checkpoint` | method | `pub fn save_checkpoint(&self) -> Result<(), WikiError> {` | `ResearchSession::save_checkpoint [method]` | `b9196d71-81b3-5493-af62-96df968cc8a0` | 230-289 [crates/gwiki/src/session.rs:230-289] | Indexed method `ResearchSession::save_checkpoint` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:230-289] |
| `ResearchSession::load_checkpoint` | method | `pub fn load_checkpoint(vault_root: &Path) -> Result<Self, WikiError> {` | `ResearchSession::load_checkpoint [method]` | `af9b87b7-98ac-58d7-8994-2357193c2b13` | 291-307 [crates/gwiki/src/session.rs:291-307] | Indexed method `ResearchSession::load_checkpoint` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:291-307] |
| `ResearchSession::record_compile_state` | method | `pub fn record_compile_state(&mut self, state: CompileState) -> Result<(), WikiError> {` | `ResearchSession::record_compile_state [method]` | `155c09a6-abca-5a3b-921b-1b30b0e9b394` | 309-312 [crates/gwiki/src/session.rs:309-312] | Indexed method `ResearchSession::record_compile_state` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:309-312] |
| `validate_checkpoint_scope_root` | function | `fn validate_checkpoint_scope_root(` | `validate_checkpoint_scope_root [function]` | `89484546-b51f-5390-a6c3-2a9f40b9dbca` | 315-334 [crates/gwiki/src/session.rs:315-334] | Indexed function `validate_checkpoint_scope_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:315-334] |
| `comparable_path` | function | `fn comparable_path(path: &Path, relative_base: Option<&Path>) -> PathBuf {` | `comparable_path [function]` | `98fc7de2-941f-508d-ab65-681426c09c1e` | 336-345 [crates/gwiki/src/session.rs:336-345] | Indexed function `comparable_path` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:336-345] |
| `checkpoint_vault_root` | function | `fn checkpoint_vault_root(checkpoint_path: &Path) -> Option<PathBuf> {` | `checkpoint_vault_root [function]` | `2ad606ed-735e-515b-8efa-83c466994295` | 347-352 [crates/gwiki/src/session.rs:347-352] | Indexed function `checkpoint_vault_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:347-352] |
| `new_session_id` | function | `fn new_session_id() -> Result<String, WikiError> {` | `new_session_id [function]` | `8fc3a09f-6cfd-531f-bed9-f6f70ee8ac1a` | 354-361 [crates/gwiki/src/session.rs:354-361] | Indexed function `new_session_id` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:354-361] |
| `unix_timestamp_ms` | function | `fn unix_timestamp_ms() -> Result<u64, WikiError> {` | `unix_timestamp_ms [function]` | `92bde559-866b-562d-a39b-adc4b4df8c04` | 363-365 [crates/gwiki/src/session.rs:363-365] | Indexed function `unix_timestamp_ms` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:363-365] |
| `research_prompt` | function | `pub(crate) fn research_prompt(` | `research_prompt [function]` | `a8cb78dd-fc49-52a1-ae37-18ebb8b72b8b` | 367-383 [crates/gwiki/src/session.rs:367-383] | Indexed function `research_prompt` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:367-383] |
| `compile_state_is_resumable` | function | `fn compile_state_is_resumable() {` | `compile_state_is_resumable [function]` | `36f6d594-e200-5587-a13d-469bc5d0d11f` | 390-423 [crates/gwiki/src/session.rs:390-423] | Indexed function `compile_state_is_resumable` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:390-423] |
| `research_code_citation_rejects_empty_provenance` | function | `fn research_code_citation_rejects_empty_provenance() {` | `research_code_citation_rejects_empty_provenance [function]` | `17bf2072-3673-5bc2-a482-705ca996fcdf` | 426-437 [crates/gwiki/src/session.rs:426-437] | Indexed function `research_code_citation_rejects_empty_provenance` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:426-437] |
| `research_code_citation_rejects_parent_path_components` | function | `fn research_code_citation_rejects_parent_path_components() {` | `research_code_citation_rejects_parent_path_components [function]` | `3fd0abe0-236a-56b3-9c4a-2b293a2fb97a` | 440-452 [crates/gwiki/src/session.rs:440-452] | Indexed function `research_code_citation_rejects_parent_path_components` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:440-452] |
| `research_code_citation_deserialization_rejects_empty_provenance` | function | `fn research_code_citation_deserialization_rejects_empty_provenance() {` | `research_code_citation_deserialization_rejects_empty_provenance [function]` | `f034753b-66c4-503a-9751-6f4050fbeb23` | 455-463 [crates/gwiki/src/session.rs:455-463] | Indexed function `research_code_citation_deserialization_rejects_empty_provenance` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:455-463] |
| `research_code_citation_deserialization_rejects_parent_path_components` | function | `fn research_code_citation_deserialization_rejects_parent_path_components() {` | `research_code_citation_deserialization_rejects_parent_path_components [function]` | `8385f8c9-8fe9-5e70-8038-7c553b67f27e` | 466-474 [crates/gwiki/src/session.rs:466-474] | Indexed function `research_code_citation_deserialization_rejects_parent_path_components` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:466-474] |
| `load_checkpoint_rejects_legacy_project_vault_relative_scope_root` | function | `fn load_checkpoint_rejects_legacy_project_vault_relative_scope_root() {` | `load_checkpoint_rejects_legacy_project_vault_relative_scope_root [function]` | `9f3ec953-1ca8-5218-936f-f692e1bec553` | 477-502 [crates/gwiki/src/session.rs:477-502] | Indexed function `load_checkpoint_rejects_legacy_project_vault_relative_scope_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:477-502] |
| `load_checkpoint_rejects_mismatched_scope_root` | function | `fn load_checkpoint_rejects_mismatched_scope_root() {` | `load_checkpoint_rejects_mismatched_scope_root [function]` | `c71d8a0c-ab8b-5557-be7e-12d7156ebb75` | 505-526 [crates/gwiki/src/session.rs:505-526] | Indexed function `load_checkpoint_rejects_mismatched_scope_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:505-526] |
| `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault` | function | `fn load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault() {` | `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault [function]` | `3bcf2e89-5b28-5a08-9ca8-7f5d3d730d3b` | 529-550 [crates/gwiki/src/session.rs:529-550] | Indexed function `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:529-550] |
