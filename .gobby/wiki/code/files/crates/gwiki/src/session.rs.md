---
title: crates/gwiki/src/session.rs
type: code_file
provenance:
- file: crates/gwiki/src/session.rs
  ranges:
  - 15-18
  - 20-46
  - 48-57
  - 60-64
  - 68-76
  - 79-87
  - 89-95
  - 97-160
  - 163-170
  - 173-183
  - 186-198
  - 200-317
  - 319-338
  - 340-349
  - 351-356
  - 358-365
  - 367-369
  - 371-387
  - 394-427
  - 430-441
  - 444-456
  - 459-467
  - 470-478
  - 481-506
  - 509-530
  - 533-554
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/session.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/session.rs` exposes 45 indexed API symbols.
[crates/gwiki/src/session.rs:15-18]
[crates/gwiki/src/session.rs:20-46]
[crates/gwiki/src/session.rs:21-26]
[crates/gwiki/src/session.rs:28-33]
[crates/gwiki/src/session.rs:35-39]

## API Symbols

- `ResearchScope` (type) component `ResearchScope [type]` (`1808b916-b517-58f9-8b5b-768d4e88c30b`) lines 15-18 [crates/gwiki/src/session.rs:15-18]
  - Signature: `pub enum ResearchScope {`
  - Purpose: Indexed type `ResearchScope` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:15-18]
- `ResearchScope` (class) component `ResearchScope [class]` (`75d3efcd-a3ad-50f9-843d-66063a2ee929`) lines 20-46 [crates/gwiki/src/session.rs:20-46]
  - Signature: `impl ResearchScope {`
  - Purpose: Indexed class `ResearchScope` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:20-46]
- `ResearchScope.project_for_id` (method) component `ResearchScope.project_for_id [method]` (`a88407fe-2279-55c8-bba4-d009159e3066`) lines 21-26 [crates/gwiki/src/session.rs:21-26]
  - Signature: `pub fn project_for_id(project_id: impl Into<String>, root: impl Into<PathBuf>) -> Self {`
  - Purpose: Indexed method `ResearchScope.project_for_id` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:21-26]
- `ResearchScope.topic` (method) component `ResearchScope.topic [method]` (`4da0f5af-8b4e-5a85-abe6-4dae1bbcda1c`) lines 28-33 [crates/gwiki/src/session.rs:28-33]
  - Signature: `pub fn topic(name: impl Into<String>, root: impl Into<PathBuf>) -> Self {`
  - Purpose: Indexed method `ResearchScope.topic` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:28-33]
- `ResearchScope.root` (method) component `ResearchScope.root [method]` (`7f8ee952-6560-5959-9b6d-a0ea2da9ae1e`) lines 35-39 [crates/gwiki/src/session.rs:35-39]
  - Signature: `pub fn root(&self) -> &Path {`
  - Purpose: Indexed method `ResearchScope.root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:35-39]
- `ResearchScope.set_root` (method) component `ResearchScope.set_root [method]` (`6988bf97-21bc-5f28-89da-32c00f5315c7`) lines 41-45 [crates/gwiki/src/session.rs:41-45]
  - Signature: `fn set_root(&mut self, new_root: PathBuf) {`
  - Purpose: Indexed method `ResearchScope.set_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:41-45]
- `ResearchScope` (class) component `ResearchScope [class]` (`accee1a5-1d84-5df8-a377-65969a9a010b`) lines 48-57 [crates/gwiki/src/session.rs:48-57]
  - Signature: `impl From<&ResolvedScope> for ResearchScope {`
  - Purpose: Indexed class `ResearchScope` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:48-57]
- `ResearchScope.from` (method) component `ResearchScope.from [method]` (`4b031344-69e0-5a30-bc3d-0ee5e874e65d`) lines 49-56 [crates/gwiki/src/session.rs:49-56]
  - Signature: `fn from(scope: &ResolvedScope) -> Self {`
  - Purpose: Indexed method `ResearchScope.from` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:49-56]
- `DaemonDispatch` (class) component `DaemonDispatch [class]` (`8786f3d3-8940-5edd-870b-d6a09a562e10`) lines 60-64 [crates/gwiki/src/session.rs:60-64]
  - Signature: `pub struct DaemonDispatch {`
  - Purpose: Indexed class `DaemonDispatch` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:60-64]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`848bacba-97d0-545f-9adb-3928884d2393`) lines 68-76 [crates/gwiki/src/session.rs:68-76]
  - Signature: `pub struct ResearchCodeCitation {`
  - Purpose: Indexed class `ResearchCodeCitation` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:68-76]
- `ResearchCodeCitationUnchecked` (class) component `ResearchCodeCitationUnchecked [class]` (`7426a58b-3a12-5b3e-be54-faeb406f847e`) lines 79-87 [crates/gwiki/src/session.rs:79-87]
  - Signature: `struct ResearchCodeCitationUnchecked {`
  - Purpose: Indexed class `ResearchCodeCitationUnchecked` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:79-87]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`197f1d19-d6c7-5f3c-b833-87bdcb0395ca`) lines 89-95 [crates/gwiki/src/session.rs:89-95]
  - Signature: `impl TryFrom<ResearchCodeCitationUnchecked> for ResearchCodeCitation {`
  - Purpose: Indexed class `ResearchCodeCitation` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:89-95]
- `ResearchCodeCitation.Error` (type) component `ResearchCodeCitation.Error [type]` (`daa59587-004b-5d84-ba7f-d98bab48e98f`) lines 90-90 [crates/gwiki/src/session.rs:90]
  - Signature: `type Error = String;`
  - Purpose: Indexed type `ResearchCodeCitation.Error` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:90]
- `ResearchCodeCitation.try_from` (method) component `ResearchCodeCitation.try_from [method]` (`049f2fce-ca39-5af4-9394-a9ba74703653`) lines 92-94 [crates/gwiki/src/session.rs:92-94]
  - Signature: `fn try_from(value: ResearchCodeCitationUnchecked) -> Result<Self, Self::Error> {`
  - Purpose: Indexed method `ResearchCodeCitation.try_from` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:92-94]
- `ResearchCodeCitation` (class) component `ResearchCodeCitation [class]` (`65efdf7d-27ab-5197-8a87-afeba0172f4c`) lines 97-160 [crates/gwiki/src/session.rs:97-160]
  - Signature: `impl ResearchCodeCitation {`
  - Purpose: Indexed class `ResearchCodeCitation` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:97-160]
- `ResearchCodeCitation.new` (method) component `ResearchCodeCitation.new [method]` (`d9897627-5d63-57a1-905b-41701b00bc3f`) lines 98-110 [crates/gwiki/src/session.rs:98-110]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `ResearchCodeCitation.new` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:98-110]
- `ResearchCodeCitation.from_parts` (method) component `ResearchCodeCitation.from_parts [method]` (`8c3d8521-6753-5fdf-82ec-360def624ce9`) lines 112-139 [crates/gwiki/src/session.rs:112-139]
  - Signature: `fn from_parts(`
  - Purpose: Indexed method `ResearchCodeCitation.from_parts` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:112-139]
- `ResearchCodeCitation.file` (method) component `ResearchCodeCitation.file [method]` (`04bc8c33-97a7-58df-940d-1b2e2db7e4da`) lines 141-143 [crates/gwiki/src/session.rs:141-143]
  - Signature: `pub fn file(&self) -> &str {`
  - Purpose: Indexed method `ResearchCodeCitation.file` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:141-143]
- `ResearchCodeCitation.line` (method) component `ResearchCodeCitation.line [method]` (`a2dc0b6f-486a-574b-9c15-8d5ac00566c8`) lines 145-147 [crates/gwiki/src/session.rs:145-147]
  - Signature: `pub fn line(&self) -> Option<usize> {`
  - Purpose: Indexed method `ResearchCodeCitation.line` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:145-147]
- `ResearchCodeCitation.symbol` (method) component `ResearchCodeCitation.symbol [method]` (`2097b105-c186-5a4a-a38e-ad07ec5aaaf6`) lines 149-151 [crates/gwiki/src/session.rs:149-151]
  - Signature: `pub fn symbol(&self) -> Option<&str> {`
  - Purpose: Indexed method `ResearchCodeCitation.symbol` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:149-151]
- `ResearchCodeCitation.provenance` (method) component `ResearchCodeCitation.provenance [method]` (`086fdf1a-8fbe-5dac-ba71-e8d6475573f7`) lines 153-155 [crates/gwiki/src/session.rs:153-155]
  - Signature: `pub fn provenance(&self) -> &[String] {`
  - Purpose: Indexed method `ResearchCodeCitation.provenance` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:153-155]
- `ResearchCodeCitation.provenance_mut` (method) component `ResearchCodeCitation.provenance_mut [method]` (`d4c88106-7471-5aa5-b2b7-ee4392274b8a`) lines 157-159 [crates/gwiki/src/session.rs:157-159]
  - Signature: `pub(crate) fn provenance_mut(&mut self) -> &mut Vec<String> {`
  - Purpose: Indexed method `ResearchCodeCitation.provenance_mut` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:157-159]
- `AcceptedResearchNote` (class) component `AcceptedResearchNote [class]` (`c930b788-7c22-58aa-b133-8372aff6a016`) lines 163-170 [crates/gwiki/src/session.rs:163-170]
  - Signature: `pub struct AcceptedResearchNote {`
  - Purpose: Indexed class `AcceptedResearchNote` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:163-170]
- `CompileState` (class) component `CompileState [class]` (`56415b0e-6f1c-5d8a-9893-43aa6480c021`) lines 173-183 [crates/gwiki/src/session.rs:173-183]
  - Signature: `pub struct CompileState {`
  - Purpose: Indexed class `CompileState` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:173-183]
- `ResearchSession` (class) component `ResearchSession [class]` (`e27de505-c6f0-5680-8c3f-96d75cf86826`) lines 186-198 [crates/gwiki/src/session.rs:186-198]
  - Signature: `pub struct ResearchSession {`
  - Purpose: Indexed class `ResearchSession` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:186-198]
- `ResearchSession` (class) component `ResearchSession [class]` (`574300e3-bf43-5b06-9bd7-480009899e8c`) lines 200-317 [crates/gwiki/src/session.rs:200-317]
  - Signature: `impl ResearchSession {`
  - Purpose: Indexed class `ResearchSession` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:200-317]
- `ResearchSession.new` (method) component `ResearchSession.new [method]` (`e1fc863b-ec9b-5c0a-ae6b-02f9a3e262e6`) lines 201-228 [crates/gwiki/src/session.rs:201-228]
  - Signature: `pub fn new(`
  - Purpose: Indexed method `ResearchSession.new` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:201-228]
- `ResearchSession.checkpoint_path` (method) component `ResearchSession.checkpoint_path [method]` (`53d9d661-bce3-5ae1-88e6-6e69f9071b61`) lines 230-232 [crates/gwiki/src/session.rs:230-232]
  - Signature: `pub fn checkpoint_path(vault_root: &Path) -> PathBuf {`
  - Purpose: Indexed method `ResearchSession.checkpoint_path` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:230-232]
- `ResearchSession.save_checkpoint` (method) component `ResearchSession.save_checkpoint [method]` (`35e9aaaa-f348-57c2-bf51-f58f37cbe958`) lines 234-293 [crates/gwiki/src/session.rs:234-293]
  - Signature: `pub fn save_checkpoint(&self) -> Result<(), WikiError> {`
  - Purpose: Indexed method `ResearchSession.save_checkpoint` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:234-293]
- `ResearchSession.load_checkpoint` (method) component `ResearchSession.load_checkpoint [method]` (`6bd5e793-532a-5651-9527-0a8d65729887`) lines 295-311 [crates/gwiki/src/session.rs:295-311]
  - Signature: `pub fn load_checkpoint(vault_root: &Path) -> Result<Self, WikiError> {`
  - Purpose: Indexed method `ResearchSession.load_checkpoint` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:295-311]
- `ResearchSession.record_compile_state` (method) component `ResearchSession.record_compile_state [method]` (`0b55ff06-a73f-5ddd-9cb2-171e4e1e1cd1`) lines 313-316 [crates/gwiki/src/session.rs:313-316]
  - Signature: `pub fn record_compile_state(&mut self, state: CompileState) -> Result<(), WikiError> {`
  - Purpose: Indexed method `ResearchSession.record_compile_state` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:313-316]
- `validate_checkpoint_scope_root` (function) component `validate_checkpoint_scope_root [function]` (`3e4d94a5-a3ca-5cc2-9a22-3122bf9ebb76`) lines 319-338 [crates/gwiki/src/session.rs:319-338]
  - Signature: `fn validate_checkpoint_scope_root(`
  - Purpose: Indexed function `validate_checkpoint_scope_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:319-338]
- `comparable_path` (function) component `comparable_path [function]` (`7bb86727-544a-54f1-a056-ae25ebe58ac4`) lines 340-349 [crates/gwiki/src/session.rs:340-349]
  - Signature: `fn comparable_path(path: &Path, relative_base: Option<&Path>) -> PathBuf {`
  - Purpose: Indexed function `comparable_path` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:340-349]
- `checkpoint_vault_root` (function) component `checkpoint_vault_root [function]` (`f88d6f21-126b-5622-886f-0cca5f191ba8`) lines 351-356 [crates/gwiki/src/session.rs:351-356]
  - Signature: `fn checkpoint_vault_root(checkpoint_path: &Path) -> Option<PathBuf> {`
  - Purpose: Indexed function `checkpoint_vault_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:351-356]
- `new_session_id` (function) component `new_session_id [function]` (`4901e59b-9281-5885-a42e-db9c85d382ab`) lines 358-365 [crates/gwiki/src/session.rs:358-365]
  - Signature: `fn new_session_id() -> Result<String, WikiError> {`
  - Purpose: Indexed function `new_session_id` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:358-365]
- `unix_timestamp_ms` (function) component `unix_timestamp_ms [function]` (`ff28fc70-8f3a-5980-85cf-e55aba3af94a`) lines 367-369 [crates/gwiki/src/session.rs:367-369]
  - Signature: `fn unix_timestamp_ms() -> Result<u64, WikiError> {`
  - Purpose: Indexed function `unix_timestamp_ms` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:367-369]
- `research_prompt` (function) component `research_prompt [function]` (`8b7c9ffc-31c6-5e66-a877-ed54e38f3e10`) lines 371-387 [crates/gwiki/src/session.rs:371-387]
  - Signature: `pub(crate) fn research_prompt(`
  - Purpose: Indexed function `research_prompt` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:371-387]
- `compile_state_is_resumable` (function) component `compile_state_is_resumable [function]` (`4be29e74-4861-5f58-b21a-875c5772a6b4`) lines 394-427 [crates/gwiki/src/session.rs:394-427]
  - Signature: `fn compile_state_is_resumable() {`
  - Purpose: Indexed function `compile_state_is_resumable` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:394-427]
- `research_code_citation_rejects_empty_provenance` (function) component `research_code_citation_rejects_empty_provenance [function]` (`e82110fd-44a5-56f3-8b93-6b1f58805a2f`) lines 430-441 [crates/gwiki/src/session.rs:430-441]
  - Signature: `fn research_code_citation_rejects_empty_provenance() {`
  - Purpose: Indexed function `research_code_citation_rejects_empty_provenance` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:430-441]
- `research_code_citation_rejects_parent_path_components` (function) component `research_code_citation_rejects_parent_path_components [function]` (`a183eeb1-da89-5bc8-b30f-2f5637ee164d`) lines 444-456 [crates/gwiki/src/session.rs:444-456]
  - Signature: `fn research_code_citation_rejects_parent_path_components() {`
  - Purpose: Indexed function `research_code_citation_rejects_parent_path_components` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:444-456]
- `research_code_citation_deserialization_rejects_empty_provenance` (function) component `research_code_citation_deserialization_rejects_empty_provenance [function]` (`c9ba030c-7ec2-58f0-8dac-e187bce9ffc8`) lines 459-467 [crates/gwiki/src/session.rs:459-467]
  - Signature: `fn research_code_citation_deserialization_rejects_empty_provenance() {`
  - Purpose: Indexed function `research_code_citation_deserialization_rejects_empty_provenance` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:459-467]
- `research_code_citation_deserialization_rejects_parent_path_components` (function) component `research_code_citation_deserialization_rejects_parent_path_components [function]` (`c0cd4017-b53d-519a-b8ca-6d88f4af7d38`) lines 470-478 [crates/gwiki/src/session.rs:470-478]
  - Signature: `fn research_code_citation_deserialization_rejects_parent_path_components() {`
  - Purpose: Indexed function `research_code_citation_deserialization_rejects_parent_path_components` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:470-478]
- `load_checkpoint_rejects_legacy_project_vault_relative_scope_root` (function) component `load_checkpoint_rejects_legacy_project_vault_relative_scope_root [function]` (`ed8d6cdc-bb3f-5168-9dd9-25a5843b19b6`) lines 481-506 [crates/gwiki/src/session.rs:481-506]
  - Signature: `fn load_checkpoint_rejects_legacy_project_vault_relative_scope_root() {`
  - Purpose: Indexed function `load_checkpoint_rejects_legacy_project_vault_relative_scope_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:481-506]
- `load_checkpoint_rejects_mismatched_scope_root` (function) component `load_checkpoint_rejects_mismatched_scope_root [function]` (`54103125-2c94-5bb2-b752-bd6750a1eb10`) lines 509-530 [crates/gwiki/src/session.rs:509-530]
  - Signature: `fn load_checkpoint_rejects_mismatched_scope_root() {`
  - Purpose: Indexed function `load_checkpoint_rejects_mismatched_scope_root` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:509-530]
- `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault` (function) component `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault [function]` (`f8893375-e233-5462-acb1-e0973093c2d3`) lines 533-554 [crates/gwiki/src/session.rs:533-554]
  - Signature: `fn load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault() {`
  - Purpose: Indexed function `load_checkpoint_normalizes_relative_scope_root_against_checkpoint_vault` in `crates/gwiki/src/session.rs`. [crates/gwiki/src/session.rs:533-554]

