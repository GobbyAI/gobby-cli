---
title: crates/gcode/src/index/languages.rs
type: code_file
provenance:
- file: crates/gcode/src/index/languages.rs
  ranges:
  - 9-14
  - 443-459
  - 461-480
  - 482-484
  - 486-492
  - 494-500
  - 502-533
  - 535-548
  - 550-555
  - 557-566
  - 568-570
  - 572-574
  - 577-582
  - 591-595
  - 598-624
  - 627-638
  - 645-649
  - 652-657
  - 660-663
  - 666-669
  - 672-675
  - 678-680
  - 683-686
  - 689-691
  - 694-708
  - 711-722
  - 725-740
  - 743-757
  - 760-766
  - 769-775
  - 777-782
  - 784-789
  - 792-802
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/languages.rs:9-14](crates/gcode/src/index/languages.rs#L9-L14), [crates/gcode/src/index/languages.rs:443-459](crates/gcode/src/index/languages.rs#L443-L459), [crates/gcode/src/index/languages.rs:461-480](crates/gcode/src/index/languages.rs#L461-L480), [crates/gcode/src/index/languages.rs:482-484](crates/gcode/src/index/languages.rs#L482-L484), [crates/gcode/src/index/languages.rs:486-492](crates/gcode/src/index/languages.rs#L486-L492), [crates/gcode/src/index/languages.rs:494-500](crates/gcode/src/index/languages.rs#L494-L500), [crates/gcode/src/index/languages.rs:502-533](crates/gcode/src/index/languages.rs#L502-L533), [crates/gcode/src/index/languages.rs:535-548](crates/gcode/src/index/languages.rs#L535-L548), [crates/gcode/src/index/languages.rs:550-555](crates/gcode/src/index/languages.rs#L550-L555), [crates/gcode/src/index/languages.rs:557-566](crates/gcode/src/index/languages.rs#L557-L566), [crates/gcode/src/index/languages.rs:568-570](crates/gcode/src/index/languages.rs#L568-L570), [crates/gcode/src/index/languages.rs:572-574](crates/gcode/src/index/languages.rs#L572-L574), [crates/gcode/src/index/languages.rs:577-582](crates/gcode/src/index/languages.rs#L577-L582), [crates/gcode/src/index/languages.rs:591-595](crates/gcode/src/index/languages.rs#L591-L595), [crates/gcode/src/index/languages.rs:598-624](crates/gcode/src/index/languages.rs#L598-L624), [crates/gcode/src/index/languages.rs:627-638](crates/gcode/src/index/languages.rs#L627-L638), [crates/gcode/src/index/languages.rs:645-649](crates/gcode/src/index/languages.rs#L645-L649), [crates/gcode/src/index/languages.rs:652-657](crates/gcode/src/index/languages.rs#L652-L657), [crates/gcode/src/index/languages.rs:660-663](crates/gcode/src/index/languages.rs#L660-L663), [crates/gcode/src/index/languages.rs:666-669](crates/gcode/src/index/languages.rs#L666-L669), [crates/gcode/src/index/languages.rs:672-675](crates/gcode/src/index/languages.rs#L672-L675), [crates/gcode/src/index/languages.rs:678-680](crates/gcode/src/index/languages.rs#L678-L680), [crates/gcode/src/index/languages.rs:683-686](crates/gcode/src/index/languages.rs#L683-L686), [crates/gcode/src/index/languages.rs:689-691](crates/gcode/src/index/languages.rs#L689-L691), [crates/gcode/src/index/languages.rs:694-708](crates/gcode/src/index/languages.rs#L694-L708), [crates/gcode/src/index/languages.rs:711-722](crates/gcode/src/index/languages.rs#L711-L722), [crates/gcode/src/index/languages.rs:725-740](crates/gcode/src/index/languages.rs#L725-L740), [crates/gcode/src/index/languages.rs:743-757](crates/gcode/src/index/languages.rs#L743-L757), [crates/gcode/src/index/languages.rs:760-766](crates/gcode/src/index/languages.rs#L760-L766), [crates/gcode/src/index/languages.rs:769-775](crates/gcode/src/index/languages.rs#L769-L775), [crates/gcode/src/index/languages.rs:777-782](crates/gcode/src/index/languages.rs#L777-L782), [crates/gcode/src/index/languages.rs:784-789](crates/gcode/src/index/languages.rs#L784-L789), [crates/gcode/src/index/languages.rs:792-802](crates/gcode/src/index/languages.rs#L792-L802)

</details>

# crates/gcode/src/index/languages.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

Defines the language registry used by the code indexer to map file extensions and source signals to tree-sitter grammars. `LanguageSpec` stores each language’s extensions plus symbol, import, and call queries; the registry is populated with specs for supported languages and the helper functions resolve the right spec or grammar from a path or snippet. The detection helpers handle extension-based matching, header-language heuristics, and special cases such as Objective-C/C++, TSX/TypeScript, and data formats like JSON/YAML, with the test functions verifying those detection rules.
[crates/gcode/src/index/languages.rs:9-14]
[crates/gcode/src/index/languages.rs:443-459]
[crates/gcode/src/index/languages.rs:461-480]
[crates/gcode/src/index/languages.rs:482-484]
[crates/gcode/src/index/languages.rs:486-492]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `LanguageSpec` | class | `pub struct LanguageSpec {` | `LanguageSpec [class]` | `41f086c5-f782-53b4-948d-a621c535379d` | 9-14 [crates/gcode/src/index/languages.rs:9-14] | Indexed class `LanguageSpec` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:9-14] |
| `detect_language` | function | `pub fn detect_language(file_path: &str) -> Option<&'static str> {` | `detect_language [function]` | `6e4b6bc0-84ed-578b-8fbd-6a497eb2b2c7` | 443-459 [crates/gcode/src/index/languages.rs:443-459] | Indexed function `detect_language` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:443-459] |
| `detect_header_language` | function | `fn detect_header_language(path: &Path) -> &'static str {` | `detect_header_language [function]` | `0dd382c8-dcae-5655-b4b7-fdcbcfad86c2` | 461-480 [crates/gcode/src/index/languages.rs:461-480] | Indexed function `detect_header_language` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:461-480] |
| `objc_header_has_sibling_implementation` | function | `fn objc_header_has_sibling_implementation(path: &Path) -> bool {` | `objc_header_has_sibling_implementation [function]` | `7023216e-daf3-56e1-a1b5-c75e7346d236` | 482-484 [crates/gcode/src/index/languages.rs:482-484] | Indexed function `objc_header_has_sibling_implementation` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:482-484] |
| `source_contains_objc_header_signal` | function | `fn source_contains_objc_header_signal(source: &str) -> bool {` | `source_contains_objc_header_signal [function]` | `a1aa403a-41c6-5673-b1ce-2475d74f0db8` | 486-492 [crates/gcode/src/index/languages.rs:486-492] | Indexed function `source_contains_objc_header_signal` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:486-492] |
| `source_contains_cpp_header_signal` | function | `fn source_contains_cpp_header_signal(source: &str) -> bool {` | `source_contains_cpp_header_signal [function]` | `b9167fc9-6143-5202-bb5e-da838286694a` | 494-500 [crates/gcode/src/index/languages.rs:494-500] | Indexed function `source_contains_cpp_header_signal` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:494-500] |
| `source_contains_header_signal` | function | `fn source_contains_header_signal<F>(source: &str, mut signal_at: F) -> bool` | `source_contains_header_signal [function]` | `51f7a737-3f84-50bc-814e-a21a85b0b8cd` | 502-533 [crates/gcode/src/index/languages.rs:502-533] | Indexed function `source_contains_header_signal` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:502-533] |
| `skip_quoted` | function | `fn skip_quoted(bytes: &[u8], start: usize) -> usize {` | `skip_quoted [function]` | `ee1bb16c-82fb-5610-9d88-a8c93d51e627` | 535-548 [crates/gcode/src/index/languages.rs:535-548] | Indexed function `skip_quoted` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:535-548] |
| `objc_directive_at` | function | `fn objc_directive_at(bytes: &[u8], idx: usize, directive: &[u8]) -> bool {` | `objc_directive_at [function]` | `d494e47d-5d90-51ad-b6d1-38b96af7d63b` | 550-555 [crates/gcode/src/index/languages.rs:550-555] | Indexed function `objc_directive_at` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:550-555] |
| `c_like_keyword_at` | function | `fn c_like_keyword_at(bytes: &[u8], idx: usize, keyword: &[u8]) -> bool {` | `c_like_keyword_at [function]` | `8103229f-edd2-5b9e-8c35-0989faa326be` | 557-566 [crates/gcode/src/index/languages.rs:557-566] | Indexed function `c_like_keyword_at` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:557-566] |
| `literal_at` | function | `fn literal_at(bytes: &[u8], idx: usize, literal: &[u8]) -> bool {` | `literal_at [function]` | `62be466d-a2ed-5f76-9970-54173d797a20` | 568-570 [crates/gcode/src/index/languages.rs:568-570] | Indexed function `literal_at` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:568-570] |
| `is_ascii_identifier_byte` | function | `fn is_ascii_identifier_byte(byte: u8) -> bool {` | `is_ascii_identifier_byte [function]` | `6199ec6a-2ef6-5b66-b4a6-d62d0a157f76` | 572-574 [crates/gcode/src/index/languages.rs:572-574] | Indexed function `is_ascii_identifier_byte` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:572-574] |
| `get_spec` | function | `pub fn get_spec(lang: &str) -> Option<&'static LanguageSpec> {` | `get_spec [function]` | `cb2c4595-dd0b-5a14-87f4-873c4430d4b3` | 577-582 [crates/gcode/src/index/languages.rs:577-582] | Indexed function `get_spec` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:577-582] |
| `is_data_language` | function | `pub fn is_data_language(lang: &str) -> bool {` | `is_data_language [function]` | `6a11adb9-51d4-546b-b4e9-e68c9e7932fa` | 591-595 [crates/gcode/src/index/languages.rs:591-595] | Indexed function `is_data_language` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:591-595] |
| `get_ts_language` | function | `pub fn get_ts_language(lang: &str) -> Option<Language> {` | `get_ts_language [function]` | `4ceb4d36-7a07-5473-8e2a-634d2ef743d2` | 598-624 [crates/gcode/src/index/languages.rs:598-624] | Indexed function `get_ts_language` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:598-624] |
| `get_ts_language_for_path` | function | `pub fn get_ts_language_for_path(lang: &str, file_path: &str) -> Option<Language> {` | `get_ts_language_for_path [function]` | `d9caa448-c50d-58e8-a0a1-40f1460ff8a1` | 627-638 [crates/gcode/src/index/languages.rs:627-638] | Indexed function `get_ts_language_for_path` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:627-638] |
| `markdown_extensions_are_not_detected` | function | `fn markdown_extensions_are_not_detected() {` | `markdown_extensions_are_not_detected [function]` | `bb4925c3-1506-57a8-a748-cca76abdd039` | 645-649 [crates/gcode/src/index/languages.rs:645-649] | Indexed function `markdown_extensions_are_not_detected` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:645-649] |
| `javascript_extensions_still_detect` | function | `fn javascript_extensions_still_detect() {` | `javascript_extensions_still_detect [function]` | `0e53a04c-b331-564f-bb17-2ad049c0e552` | 652-657 [crates/gcode/src/index/languages.rs:652-657] | Indexed function `javascript_extensions_still_detect` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:652-657] |
| `typescript_extensions_still_detect` | function | `fn typescript_extensions_still_detect() {` | `typescript_extensions_still_detect [function]` | `48fb93e1-f7b7-5f45-95cd-0918aa166ae6` | 660-663 [crates/gcode/src/index/languages.rs:660-663] | Indexed function `typescript_extensions_still_detect` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:660-663] |
| `bash_extensions_detect` | function | `fn bash_extensions_detect() {` | `bash_extensions_detect [function]` | `30705974-990e-5db8-9e0d-7707ef0b7d67` | 666-669 [crates/gcode/src/index/languages.rs:666-669] | Indexed function `bash_extensions_detect` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:666-669] |
| `scala_extensions_detect` | function | `fn scala_extensions_detect() {` | `scala_extensions_detect [function]` | `a0fe3040-c356-5737-b300-b959461a48d0` | 672-675 [crates/gcode/src/index/languages.rs:672-675] | Indexed function `scala_extensions_detect` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:672-675] |
| `lua_extensions_detect` | function | `fn lua_extensions_detect() {` | `lua_extensions_detect [function]` | `9bd19d66-3d51-54d1-bc8f-b588b025ad0e` | 678-680 [crates/gcode/src/index/languages.rs:678-680] | Indexed function `lua_extensions_detect` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:678-680] |
| `objc_extensions_detect` | function | `fn objc_extensions_detect() {` | `objc_extensions_detect [function]` | `07a8dca6-a1ce-5b6e-918d-f8820ba94cbf` | 683-686 [crates/gcode/src/index/languages.rs:683-686] | Indexed function `objc_extensions_detect` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:683-686] |
| `c_header_detects_without_objc_or_cpp_signal` | function | `fn c_header_detects_without_objc_or_cpp_signal() {` | `c_header_detects_without_objc_or_cpp_signal [function]` | `c4e678d8-15b6-55cd-acff-ae5bcfadf96e` | 689-691 [crates/gcode/src/index/languages.rs:689-691] | Indexed function `c_header_detects_without_objc_or_cpp_signal` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:689-691] |
| `objc_header_detects_declaration_signal` | function | `fn objc_header_detects_declaration_signal() {` | `objc_header_detects_declaration_signal [function]` | `a262d6bb-13cf-5496-a0cf-504583389997` | 694-708 [crates/gcode/src/index/languages.rs:694-708] | Indexed function `objc_header_detects_declaration_signal` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:694-708] |
| `objc_header_detects_sibling_implementation_signal` | function | `fn objc_header_detects_sibling_implementation_signal() {` | `objc_header_detects_sibling_implementation_signal [function]` | `3de7fe9b-a887-56e2-8090-552f722ad1c4` | 711-722 [crates/gcode/src/index/languages.rs:711-722] | Indexed function `objc_header_detects_sibling_implementation_signal` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:711-722] |
| `cpp_header_detects_cpp_signal` | function | `fn cpp_header_detects_cpp_signal() {` | `cpp_header_detects_cpp_signal [function]` | `94014bbc-7910-5b23-9117-ef46a5b43073` | 725-740 [crates/gcode/src/index/languages.rs:725-740] | Indexed function `cpp_header_detects_cpp_signal` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:725-740] |
| `objcxx_paths_use_objc_grammar` | function | `fn objcxx_paths_use_objc_grammar() {` | `objcxx_paths_use_objc_grammar [function]` | `5e5c88c5-340e-5204-9c23-4d69af8947b5` | 743-757 [crates/gcode/src/index/languages.rs:743-757] | Indexed function `objcxx_paths_use_objc_grammar` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:743-757] |
| `tsx_paths_use_tsx_grammar` | function | `fn tsx_paths_use_tsx_grammar() {` | `tsx_paths_use_tsx_grammar [function]` | `5e9adea7-1cd4-579d-a7b7-064da69e462a` | 760-766 [crates/gcode/src/index/languages.rs:760-766] | Indexed function `tsx_paths_use_tsx_grammar` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:760-766] |
| `ts_paths_keep_typescript_grammar` | function | `fn ts_paths_keep_typescript_grammar() {` | `ts_paths_keep_typescript_grammar [function]` | `3ea55040-4e93-5c6b-a92c-2897342b0c1b` | 769-775 [crates/gcode/src/index/languages.rs:769-775] | Indexed function `ts_paths_keep_typescript_grammar` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:769-775] |
| `parses_without_error` | function | `fn parses_without_error(language: Language, source: &str) -> bool {` | `parses_without_error [function]` | `d2445e5b-bd8e-5d13-b68a-f8ffcc4418d1` | 777-782 [crates/gcode/src/index/languages.rs:777-782] | Indexed function `parses_without_error` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:777-782] |
| `parses_with_error` | function | `fn parses_with_error(language: Language, source: &str) -> bool {` | `parses_with_error [function]` | `0ba562b3-56d2-5d35-a4b5-cca04ddb4868` | 784-789 [crates/gcode/src/index/languages.rs:784-789] | Indexed function `parses_with_error` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:784-789] |
| `is_data_language_matches_only_json_and_yaml` | function | `fn is_data_language_matches_only_json_and_yaml() {` | `is_data_language_matches_only_json_and_yaml [function]` | `54591821-f63e-5155-8de6-2b01ce0e568c` | 792-802 [crates/gcode/src/index/languages.rs:792-802] | Indexed function `is_data_language_matches_only_json_and_yaml` in `crates/gcode/src/index/languages.rs`. [crates/gcode/src/index/languages.rs:792-802] |
