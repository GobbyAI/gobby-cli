---
title: crates/gwiki/src/main.rs
type: code_file
provenance:
- file: crates/gwiki/src/main.rs
  ranges:
  - 47-61
  - 64-150
  - 153-168
  - 171-213
  - 216-226
  - 229-244
  - 247-255
  - 258-266
  - 268-279
  - 282-297
  - 300-308
  - 316-324
  - 327-330
  - 333-336
  - 339-364
  - 367-370
  - 373-386
  - 389-403
  - 406-410
  - '417'
  - 422-424
  - 426-430
  - '432'
  - 435-442
  - 444-448
  - 450-502
  - 509-528
  - 530-532
  - 534-548
  - 550-685
  - 688-694
  - 698-708
  - 712-719
  - 723-731
  - 734-751
  - 754-770
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/main.rs:47-61](crates/gwiki/src/main.rs#L47-L61), [crates/gwiki/src/main.rs:64-150](crates/gwiki/src/main.rs#L64-L150), [crates/gwiki/src/main.rs:153-168](crates/gwiki/src/main.rs#L153-L168), [crates/gwiki/src/main.rs:171-213](crates/gwiki/src/main.rs#L171-L213), [crates/gwiki/src/main.rs:216-226](crates/gwiki/src/main.rs#L216-L226), [crates/gwiki/src/main.rs:229-244](crates/gwiki/src/main.rs#L229-L244), [crates/gwiki/src/main.rs:247-255](crates/gwiki/src/main.rs#L247-L255), [crates/gwiki/src/main.rs:258-266](crates/gwiki/src/main.rs#L258-L266), [crates/gwiki/src/main.rs:268-279](crates/gwiki/src/main.rs#L268-L279), [crates/gwiki/src/main.rs:282-297](crates/gwiki/src/main.rs#L282-L297), [crates/gwiki/src/main.rs:300-308](crates/gwiki/src/main.rs#L300-L308), [crates/gwiki/src/main.rs:316-324](crates/gwiki/src/main.rs#L316-L324), [crates/gwiki/src/main.rs:327-330](crates/gwiki/src/main.rs#L327-L330), [crates/gwiki/src/main.rs:333-336](crates/gwiki/src/main.rs#L333-L336), [crates/gwiki/src/main.rs:339-364](crates/gwiki/src/main.rs#L339-L364), [crates/gwiki/src/main.rs:367-370](crates/gwiki/src/main.rs#L367-L370), [crates/gwiki/src/main.rs:373-386](crates/gwiki/src/main.rs#L373-L386), [crates/gwiki/src/main.rs:389-403](crates/gwiki/src/main.rs#L389-L403), [crates/gwiki/src/main.rs:406-410](crates/gwiki/src/main.rs#L406-L410), [crates/gwiki/src/main.rs:417](crates/gwiki/src/main.rs#L417), [crates/gwiki/src/main.rs:422-424](crates/gwiki/src/main.rs#L422-L424), [crates/gwiki/src/main.rs:426-430](crates/gwiki/src/main.rs#L426-L430), [crates/gwiki/src/main.rs:432](crates/gwiki/src/main.rs#L432), [crates/gwiki/src/main.rs:435-442](crates/gwiki/src/main.rs#L435-L442), [crates/gwiki/src/main.rs:444-448](crates/gwiki/src/main.rs#L444-L448), [crates/gwiki/src/main.rs:450-502](crates/gwiki/src/main.rs#L450-L502), [crates/gwiki/src/main.rs:509-528](crates/gwiki/src/main.rs#L509-L528), [crates/gwiki/src/main.rs:530-532](crates/gwiki/src/main.rs#L530-L532), [crates/gwiki/src/main.rs:534-548](crates/gwiki/src/main.rs#L534-L548), [crates/gwiki/src/main.rs:550-685](crates/gwiki/src/main.rs#L550-L685), [crates/gwiki/src/main.rs:688-694](crates/gwiki/src/main.rs#L688-L694), [crates/gwiki/src/main.rs:698-708](crates/gwiki/src/main.rs#L698-L708), [crates/gwiki/src/main.rs:712-719](crates/gwiki/src/main.rs#L712-L719), [crates/gwiki/src/main.rs:723-731](crates/gwiki/src/main.rs#L723-L731), [crates/gwiki/src/main.rs:734-751](crates/gwiki/src/main.rs#L734-L751), [crates/gwiki/src/main.rs:754-770](crates/gwiki/src/main.rs#L754-L770)

</details>

# crates/gwiki/src/main.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Defines the `gwiki` command-line entry point and all of its argument types, subcommands, and conversion helpers. The file uses `clap` to parse global options like output format and quiet mode, then maps each CLI subcommand into the corresponding `gobby_wiki::Command`, `ScopeSelection`, or option struct used by the core wiki layer. It also provides utility code for validating numeric flags, normalizing project-related arguments, detecting subcommands, printing errors, initializing a stderr logger, and translating `WikiError` values into process exit codes so the binary can run and report failures consistently.
[crates/gwiki/src/main.rs:47-61]
[crates/gwiki/src/main.rs:64-150]
[crates/gwiki/src/main.rs:153-168]
[crates/gwiki/src/main.rs:171-213]
[crates/gwiki/src/main.rs:216-226]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `Cli` | class | `struct Cli {` | `Cli [class]` | `42dd806b-d523-5710-91f0-330e04d8af61` | 47-61 [crates/gwiki/src/main.rs:47-61] | Indexed class `Cli` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:47-61] |
| `CliCommand` | type | `enum CliCommand {` | `CliCommand [type]` | `c754c59e-c867-50e3-8cea-6dcddfc1158b` | 64-150 [crates/gwiki/src/main.rs:64-150] | Indexed type `CliCommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:64-150] |
| `ScopeArgs` | class | `struct ScopeArgs {` | `ScopeArgs [class]` | `4d94496b-5ae8-5ff8-8f5f-7a695d14acf4` | 153-168 [crates/gwiki/src/main.rs:153-168] | Indexed class `ScopeArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:153-168] |
| `SetupArgs` | class | `struct SetupArgs {` | `SetupArgs [class]` | `de8aa56e-a058-5875-8123-870b41bb6170` | 171-213 [crates/gwiki/src/main.rs:171-213] | Indexed class `SetupArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:171-213] |
| `SearchArgs` | class | `struct SearchArgs {` | `SearchArgs [class]` | `e1439096-a49c-57a0-a25b-346bfa4b1e12` | 216-226 [crates/gwiki/src/main.rs:216-226] | Indexed class `SearchArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:216-226] |
| `AskArgs` | class | `struct AskArgs {` | `AskArgs [class]` | `29e2c75b-96fd-5140-8fc9-dda90c4b5c2c` | 229-244 [crates/gwiki/src/main.rs:229-244] | Indexed class `AskArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:229-244] |
| `SyncSessionsArgs` | class | `struct SyncSessionsArgs {` | `SyncSessionsArgs [class]` | `6f223e73-b197-5162-a68e-db4739d2663e` | 247-255 [crates/gwiki/src/main.rs:247-255] | Indexed class `SyncSessionsArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:247-255] |
| `BenchmarkArgs` | class | `struct BenchmarkArgs {` | `BenchmarkArgs [class]` | `2644615f-335c-54a0-9792-2e85c1b38823` | 258-266 [crates/gwiki/src/main.rs:258-266] | Indexed class `BenchmarkArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:258-266] |
| `parse_positive_usize` | function | `fn parse_positive_usize(value: &str) -> Result<usize, String> {` | `parse_positive_usize [function]` | `9ebbf2b4-2640-506e-9952-acbea14df617` | 268-279 [crates/gwiki/src/main.rs:268-279] | Indexed function `parse_positive_usize` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:268-279] |
| `RemoveSourceArgs` | class | `struct RemoveSourceArgs {` | `RemoveSourceArgs [class]` | `cac119b7-7b75-5df8-90b8-87e5471b6417` | 282-297 [crates/gwiki/src/main.rs:282-297] | Indexed class `RemoveSourceArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:282-297] |
| `RefreshArgs` | class | `struct RefreshArgs {` | `RefreshArgs [class]` | `278d0bc2-02eb-5fce-b237-3c4832c76cb7` | 300-308 [crates/gwiki/src/main.rs:300-308] | Indexed class `RefreshArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:300-308] |
| `ReadArgs` | class | `struct ReadArgs {` | `ReadArgs [class]` | `f2666891-3599-5423-8f75-5c5721cd40bb` | 316-324 [crates/gwiki/src/main.rs:316-324] | Indexed class `ReadArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:316-324] |
| `BacklinksArgs` | class | `struct BacklinksArgs {` | `BacklinksArgs [class]` | `672a05b6-3fe5-5694-afce-addd7a8794df` | 327-330 [crates/gwiki/src/main.rs:327-330] | Indexed class `BacklinksArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:327-330] |
| `LinkSuggestArgs` | class | `struct LinkSuggestArgs {` | `LinkSuggestArgs [class]` | `2858d9f1-e2bd-5607-9aed-6bbba37c2f4d` | 333-336 [crates/gwiki/src/main.rs:333-336] | Indexed class `LinkSuggestArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:333-336] |
| `CompileArgs` | class | `struct CompileArgs {` | `CompileArgs [class]` | `75f6cc89-f515-5dc3-86b8-c1c220eba4bc` | 339-364 [crates/gwiki/src/main.rs:339-364] | Indexed class `CompileArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:339-364] |
| `ExportArgs` | class | `struct ExportArgs {` | `ExportArgs [class]` | `35f4785a-cd33-5189-bce7-39d54d14c333` | 367-370 [crates/gwiki/src/main.rs:367-370] | Indexed class `ExportArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:367-370] |
| `ReviewReportArgs` | class | `struct ReviewReportArgs {` | `ReviewReportArgs [class]` | `fda0f363-c550-5b16-84af-572b91da6686` | 373-386 [crates/gwiki/src/main.rs:373-386] | Indexed class `ReviewReportArgs` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:373-386] |
| `ExportSubcommand` | type | `enum ExportSubcommand {` | `ExportSubcommand [type]` | `ca807683-fb2e-54aa-8a6f-28ff74fe26fb` | 389-403 [crates/gwiki/src/main.rs:389-403] | Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:389-403] |
| `CompileKind` | type | `enum CompileKind {` | `CompileKind [type]` | `0b04a836-12c1-5fde-b509-9e640abc2aba` | 406-410 [crates/gwiki/src/main.rs:406-410] | Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:406-410] |
| `StderrLogger` | class | `struct StderrLogger;` | `StderrLogger [class]` | `13203bfd-33ca-59c6-bf49-60bf4c290dba` | 417-417 [crates/gwiki/src/main.rs:417] | Indexed class `StderrLogger` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:417] |
| `StderrLogger::enabled` | method | `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {` | `StderrLogger::enabled [method]` | `d7e518a9-63a8-564c-94ca-46066935c559` | 422-424 [crates/gwiki/src/main.rs:422-424] | Indexed method `StderrLogger::enabled` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:422-424] |
| `StderrLogger::log` | method | `fn log(&self, record: &log::Record<'_>) {` | `StderrLogger::log [method]` | `04f761b7-2c66-59e7-b6dc-dad24fe09c04` | 426-430 [crates/gwiki/src/main.rs:426-430] | Indexed method `StderrLogger::log` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:426-430] |
| `StderrLogger::flush` | method | `fn flush(&self) {}` | `StderrLogger::flush [method]` | `965886fb-0f09-5c09-88f8-9131ff211495` | 432-432 [crates/gwiki/src/main.rs:432] | Indexed method `StderrLogger::flush` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:432] |
| `log_level` | function | `fn log_level(quiet: bool, rust_log: Option<&str>) -> log::LevelFilter {` | `log_level [function]` | `ba671d8e-fa04-5162-b7a7-53853c259c84` | 435-442 [crates/gwiki/src/main.rs:435-442] | Indexed function `log_level` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:435-442] |
| `init_logger` | function | `fn init_logger(quiet: bool) {` | `init_logger [function]` | `730dff2f-e590-511a-bc3a-1fc4ce5bb85a` | 444-448 [crates/gwiki/src/main.rs:444-448] | Indexed function `init_logger` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:444-448] |
| `main` | function | `fn main() -> ExitCode {` | `main [function]` | `47fbfdf3-6931-5fb7-94d5-613582ff8650` | 450-502 [crates/gwiki/src/main.rs:450-502] | Indexed function `main` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:450-502] |
| `normalize_project_flag_args` | function | `fn normalize_project_flag_args<I, S>(args: I) -> Vec<OsString>` | `normalize_project_flag_args [function]` | `9a4832b6-b7ce-54a8-b1e6-37d5cd76ddae` | 509-528 [crates/gwiki/src/main.rs:509-528] | Indexed function `normalize_project_flag_args` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:509-528] |
| `is_cli_subcommand` | function | `fn is_cli_subcommand(value: &str) -> bool {` | `is_cli_subcommand [function]` | `69282d24-6bb3-54b3-9f2a-a0c7cf8d6bf1` | 530-532 [crates/gwiki/src/main.rs:530-532] | Indexed function `is_cli_subcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:530-532] |
| `print_error` | function | `fn print_error(format: output::Format, error: &WikiError) {` | `print_error [function]` | `e6d2869e-e7d8-53f1-b85e-c2355c444ce8` | 534-548 [crates/gwiki/src/main.rs:534-548] | Indexed function `print_error` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:534-548] |
| `command_from_cli` | function | `fn command_from_cli(command: CliCommand, scope: ScopeSelection) -> Result<Command, WikiError> {` | `command_from_cli [function]` | `a55d32aa-987f-56a0-ba2e-fd48497d631f` | 550-685 [crates/gwiki/src/main.rs:550-685] | Indexed function `command_from_cli` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:550-685] |
| `from` | function | `fn from(kind: CompileKind) -> Self {` | `from [function]` | `5beadc68-f1fb-5e6b-b4d5-169a1939fdd9` | 688-694 [crates/gwiki/src/main.rs:688-694] | Indexed function `from` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:688-694] |
| `from` | function | `fn from(args: ExportArgs) -> Self {` | `from [function]` | `b75b0a0d-763a-5a5c-b87d-f1bb4fdeef1a` | 698-708 [crates/gwiki/src/main.rs:698-708] | Indexed function `from` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:698-708] |
| `from` | function | `fn from(args: ReviewReportArgs) -> Self {` | `from [function]` | `075c295c-fc09-5fef-8cc2-121cf1f0062d` | 712-719 [crates/gwiki/src/main.rs:712-719] | Indexed function `from` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:712-719] |
| `ScopeSelection::from` | method | `fn from(scope: ScopeArgs) -> Self {` | `ScopeSelection::from [method]` | `6767084b-6655-5750-a767-16166a6227ef` | 723-731 [crates/gwiki/src/main.rs:723-731] | Indexed method `ScopeSelection::from` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:723-731] |
| `exit_code_for_error` | function | `fn exit_code_for_error(error: &WikiError) -> ExitCode {` | `exit_code_for_error [function]` | `4431fd59-cc8e-5104-b212-0e725eaa8c66` | 734-751 [crates/gwiki/src/main.rs:734-751] | Indexed function `exit_code_for_error` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:734-751] |
| `from` | function | `fn from(args: SetupArgs) -> Self {` | `from [function]` | `1e5ae5dd-1a05-5116-b9b1-6bcc4a8702cc` | 754-770 [crates/gwiki/src/main.rs:754-770] | Indexed function `from` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:754-770] |
