---
title: crates/gwiki/src/main.rs
type: code_file
provenance:
- file: crates/gwiki/src/main.rs
  ranges:
  - 45-59
  - 62-146
  - 149-164
  - 167-209
  - 212-222
  - 225-240
  - 243-251
  - 253-264
  - 267-282
  - 285-293
  - 301-309
  - 312-315
  - 318-321
  - 324-346
  - 349-352
  - 355-368
  - 371-385
  - 388-392
  - '399'
  - 403-415
  - 417-424
  - 426-430
  - 432-484
  - 491-510
  - 512-514
  - 516-530
  - 532-659
  - 662-668
  - 672-682
  - 686-693
  - 696-706
  - 708-725
  - 728-744
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/main.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/main.rs` defines the `gwiki` command-line entrypoint: it parses global CLI flags, scope selection, and a large subcommand enum, then turns those parsed arguments into internal `gobby_wiki::Command` values and runs the wiki workflow. It also normalizes `--project` usage, initializes stderr-based logging from `RUST_LOG` and `--quiet`, formats errors and exit codes, and provides small `From` conversions that map CLI-specific structs like compile, export, review-report, and setup arguments into the internal command model.
[crates/gwiki/src/main.rs:45-59]
[crates/gwiki/src/main.rs:62-146]
[crates/gwiki/src/main.rs:149-164]
[crates/gwiki/src/main.rs:167-209]
[crates/gwiki/src/main.rs:212-222]

## API Symbols

- `Cli` (class) component `Cli [class]` (`3cbbdbaa-5b94-54cb-bc40-4232c0ffb515`) lines 45-59 [crates/gwiki/src/main.rs:45-59]
  - Signature: `struct Cli {`
  - Purpose: 'Cli' is a top-level command-line argument parser struct that flattens 'ScopeArgs', defines global 'format' and 'quiet' flags, and dispatches to a 'CliCommand' subcommand. [crates/gwiki/src/main.rs:45-59]
- `CliCommand` (type) component `CliCommand [type]` (`877c3af2-494a-55b6-8bcb-aaa24477d1f2`) lines 62-146 [crates/gwiki/src/main.rs:62-146]
  - Signature: `enum CliCommand {`
  - Purpose: Indexed type `CliCommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:62-146]
- `ScopeArgs` (class) component `ScopeArgs [class]` (`42b0db07-df81-5859-bf3f-d51a0f374596`) lines 149-164 [crates/gwiki/src/main.rs:149-164]
  - Signature: `struct ScopeArgs {`
  - Purpose: 'ScopeArgs' is a Clap argument struct that defines two mutually exclusive global flags for selecting wiki scope: '--project' as an optional 'PathBuf' defaulting to the current directory when omitted with a value, and '--topic' as an optional named 'String' scope. [crates/gwiki/src/main.rs:149-164]
- `SetupArgs` (class) component `SetupArgs [class]` (`ce82c6a7-a8eb-59c8-88b6-77db52d40291`) lines 167-209 [crates/gwiki/src/main.rs:167-209]
  - Signature: `struct SetupArgs {`
  - Purpose: 'SetupArgs' is a CLI argument struct that configures Gobby setup behavior, including whether to provision a shared hub or Docker services and optional connection/settings for PostgreSQL, FalkorDB, Qdrant, and embedding-provider parameters. [crates/gwiki/src/main.rs:167-209]
- `SearchArgs` (class) component `SearchArgs [class]` (`f2162dd7-2e7b-59fd-b91c-c7a3f8060190`) lines 212-222 [crates/gwiki/src/main.rs:212-222]
  - Signature: `struct SearchArgs {`
  - Purpose: 'SearchArgs' is a CLI argument struct that captures a required search query, an optional result limit defaulting to 10, and a '--no-semantic' flag to disable semantic vector search for the query. [crates/gwiki/src/main.rs:212-222]
- `AskArgs` (class) component `AskArgs [class]` (`7efe1187-eb35-5739-8103-371f19cf1b91`) lines 225-240 [crates/gwiki/src/main.rs:225-240]
  - Signature: `struct AskArgs {`
  - Purpose: 'AskArgs' is a CLI argument struct that captures a required 'question' plus flags to enable LLM-based answer synthesis, override AI routing, and require a successful AI route when synthesis is requested. [crates/gwiki/src/main.rs:225-240]
- `BenchmarkArgs` (class) component `BenchmarkArgs [class]` (`9af108bc-f3b8-5f2c-9ffc-83977766195f`) lines 243-251 [crates/gwiki/src/main.rs:243-251]
  - Signature: `struct BenchmarkArgs {`
  - Purpose: 'BenchmarkArgs' is a command-line argument struct that defines a single 'usize' field, 'retrieval_candidates', parsed as a positive integer from '--retrieval-candidates' and defaulting to 'BenchmarkOptions::DEFAULT_RETRIEVAL_CANDIDATES' for seeded retrieval precision probes. [crates/gwiki/src/main.rs:243-251]
- `parse_positive_usize` (function) component `parse_positive_usize [function]` (`391076be-2b42-5e51-adbf-3cbb2504c420`) lines 253-264 [crates/gwiki/src/main.rs:253-264]
  - Signature: `fn parse_positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Parses 'value' as a 'usize' and returns it only if it is strictly greater than zero, otherwise converting the parse error to a string or returning '"must be greater than zero"'. [crates/gwiki/src/main.rs:253-264]
- `RemoveSourceArgs` (class) component `RemoveSourceArgs [class]` (`1a54ed3a-71cd-5059-9116-5b75f85952f4`) lines 267-282 [crates/gwiki/src/main.rs:267-282]
  - Signature: `struct RemoveSourceArgs {`
  - Purpose: 'RemoveSourceArgs' is a CLI argument struct for deleting a source by 'id', with flags to preview the operation ('dry_run'), explicitly confirm destructive removal ('yes'), and optionally retain the referenced raw asset ('keep_asset'). [crates/gwiki/src/main.rs:267-282]
- `RefreshArgs` (class) component `RefreshArgs [class]` (`158aba88-c463-5739-bbb7-f9931c8a74f8`) lines 285-293 [crates/gwiki/src/main.rs:285-293]
  - Signature: `struct RefreshArgs {`
  - Purpose: 'RefreshArgs' is a CLI argument struct that collects zero or more source IDs to refresh via repeated '--id SOURCE_ID' flags and a '--dry-run' boolean that previews refresh candidates without performing fetch, write, delete, or indexing operations. [crates/gwiki/src/main.rs:285-293]
- `ReadArgs` (class) component `ReadArgs [class]` (`80e6b34f-f21a-5038-a1e9-25e085ab6849`) lines 301-309 [crates/gwiki/src/main.rs:301-309]
  - Signature: `struct ReadArgs {`
  - Purpose: 'ReadArgs' is a CLI argument struct that accepts an optional vault-relative wiki 'path' and an optional first-heading 'title' to resolve within the selected scope. [crates/gwiki/src/main.rs:301-309]
- `BacklinksArgs` (class) component `BacklinksArgs [class]` (`064c9253-eac5-581d-af3c-c77bf62a2667`) lines 312-315 [crates/gwiki/src/main.rs:312-315]
  - Signature: `struct BacklinksArgs {`
  - Purpose: 'BacklinksArgs' is a struct containing a single required 'page: String' command-line argument, used to identify the target page for backlink retrieval. [crates/gwiki/src/main.rs:312-315]
- `LinkSuggestArgs` (class) component `LinkSuggestArgs [class]` (`ae2b3938-35dc-52d5-b988-a3bd036caa07`) lines 318-321 [crates/gwiki/src/main.rs:318-321]
  - Signature: `struct LinkSuggestArgs {`
  - Purpose: 'LinkSuggestArgs' is a CLI argument struct that defines a single 'limit: usize' option, exposed as '--limit' and defaulting to '10'. [crates/gwiki/src/main.rs:318-321]
- `CompileArgs` (class) component `CompileArgs [class]` (`bc6d427d-7dbb-5bc3-a948-4538a3792977`) lines 324-346 [crates/gwiki/src/main.rs:324-346]
  - Signature: `struct CompileArgs {`
  - Purpose: 'CompileArgs' is a Clap argument struct for a compile command that accepts an optional topic, zero or more outline headings, a compile kind enum defaulting to 'topic', an optional target page path, a 'write_intent' flag, and an AI routing mode for explainer synthesis. [crates/gwiki/src/main.rs:324-346]
- `ExportArgs` (class) component `ExportArgs [class]` (`830dbf0a-2138-5dd0-92df-4cede3379069`) lines 349-352 [crates/gwiki/src/main.rs:349-352]
  - Signature: `struct ExportArgs {`
  - Purpose: 'ExportArgs' is a command-line argument struct that holds a single 'ExportSubcommand' value as the parsed export subcommand. [crates/gwiki/src/main.rs:349-352]
- `ReviewReportArgs` (class) component `ReviewReportArgs [class]` (`7b67eba6-4bda-571e-8f51-18663c190975`) lines 355-368 [crates/gwiki/src/main.rs:355-368]
  - Signature: `struct ReviewReportArgs {`
  - Purpose: 'ReviewReportArgs' is a CLI argument struct that collects zero or more file paths and symbol IDs plus an optional diff path, and configures the markdown output filename with a default of 'review-report.md'. [crates/gwiki/src/main.rs:355-368]
- `ExportSubcommand` (type) component `ExportSubcommand [type]` (`1242b798-6e1c-5f45-a8b7-96ba7939a89b`) lines 371-385 [crates/gwiki/src/main.rs:371-385]
  - Signature: `enum ExportSubcommand {`
  - Purpose: Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:371-385]
- `CompileKind` (type) component `CompileKind [type]` (`1dfddad6-9ceb-5b05-a17b-1bb5ffa7765b`) lines 388-392 [crates/gwiki/src/main.rs:388-392]
  - Signature: `enum CompileKind {`
  - Purpose: Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:388-392]
- `StderrLogger` (class) component `StderrLogger [class]` (`84e6dbf1-3699-5d7e-97cd-bb6012b86d2a`) lines 399-399 [crates/gwiki/src/main.rs:399]
  - Signature: `struct StderrLogger;`
  - Purpose: A logger implementation that writes log output to standard error ('stderr'). [crates/gwiki/src/main.rs:399]
- `StderrLogger` (class) component `StderrLogger [class]` (`4a8798b7-b238-54e2-a185-7c424ae2000c`) lines 403-415 [crates/gwiki/src/main.rs:403-415]
  - Signature: `impl log::Log for StderrLogger {`
  - Purpose: 'StderrLogger' is a 'log::Log' implementation that accepts records at or below the global max log level and emits them to stderr as 'gwiki: <level>: <message>', with 'flush()' a no-op. [crates/gwiki/src/main.rs:403-415]
- `StderrLogger.enabled` (method) component `StderrLogger.enabled [method]` (`9b1bc4dc-df14-56a1-95bf-0b6d5543cce1`) lines 404-406 [crates/gwiki/src/main.rs:404-406]
  - Signature: `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {`
  - Purpose: Returns 'true' when the record’s 'log::Level' is less than or equal to the current global 'log::max_level()', thereby filtering out messages above the active logging threshold. [crates/gwiki/src/main.rs:404-406]
- `StderrLogger.log` (method) component `StderrLogger.log [method]` (`fb321d7c-1106-5955-a8a0-a441da28b063`) lines 408-412 [crates/gwiki/src/main.rs:408-412]
  - Signature: `fn log(&self, record: &log::Record<'_>) {`
  - Purpose: If the record’s metadata is enabled, it writes 'gwiki: {level}: {args}' to stderr via 'eprintln!'; otherwise it does nothing. [crates/gwiki/src/main.rs:408-412]
- `StderrLogger.flush` (method) component `StderrLogger.flush [method]` (`c4787935-ddc2-5184-b8a5-05901135e989`) lines 414-414 [crates/gwiki/src/main.rs:414]
  - Signature: `fn flush(&self) {}`
  - Purpose: 'flush' is a no-op method that takes an immutable reference to 'self' and performs no state changes or side effects. [crates/gwiki/src/main.rs:414]
- `log_level` (function) component `log_level [function]` (`d24ff0fb-c427-52e1-9699-c50aac3ffd84`) lines 417-424 [crates/gwiki/src/main.rs:417-424]
  - Signature: `fn log_level(quiet: bool, rust_log: Option<&str>) -> log::LevelFilter {`
  - Purpose: Returns 'log::LevelFilter::Off' when 'quiet' is true, otherwise attempts to parse the trimmed 'rust_log' string into a 'LevelFilter' and falls back to 'Off' if parsing fails or no value is provided. [crates/gwiki/src/main.rs:417-424]
- `init_logger` (function) component `init_logger [function]` (`ac9023f0-7424-584b-9f97-3836e01617e2`) lines 426-430 [crates/gwiki/src/main.rs:426-430]
  - Signature: `fn init_logger(quiet: bool) {`
  - Purpose: Initializes the global logger by reading 'RUST_LOG' from the environment, installing 'STDERR_LOGGER', and setting the maximum log level based on 'quiet' and the optional 'RUST_LOG' value. [crates/gwiki/src/main.rs:426-430]
- `main` (function) component `main [function]` (`3f7d20d5-0a03-5f7d-ac15-6f9e8392f184`) lines 432-484 [crates/gwiki/src/main.rs:432-484]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Parses CLI arguments, initializes logging, handles the 'Contract' subcommand by printing the CLI contract, otherwise converts the CLI request into an internal command and runs 'gobby_wiki::run', emitting status/result output or formatted errors and returning the corresponding 'ExitCode'. [crates/gwiki/src/main.rs:432-484]
- `normalize_project_flag_args` (function) component `normalize_project_flag_args [function]` (`26cb2358-900f-51c8-be14-0a611063cc4b`) lines 491-510 [crates/gwiki/src/main.rs:491-510]
  - Signature: `fn normalize_project_flag_args<I, S>(args: I) -> Vec<OsString>`
  - Purpose: It clones the input arguments into a 'Vec<OsString>' and, whenever it sees '--project' immediately followed by a string recognized as a CLI subcommand, inserts an extra '"."' project value after '--project' to normalize the argument list. [crates/gwiki/src/main.rs:491-510]
- `is_cli_subcommand` (function) component `is_cli_subcommand [function]` (`4e2963ff-426e-50d2-bd31-f09e9aedb472`) lines 512-514 [crates/gwiki/src/main.rs:512-514]
  - Signature: `fn is_cli_subcommand(value: &str) -> bool {`
  - Purpose: Returns 'true' if 'value' is present in the 'CLI_SUBCOMMANDS' collection, otherwise 'false'. [crates/gwiki/src/main.rs:512-514]
- `print_error` (function) component `print_error [function]` (`a8308966-0f68-5cfa-ad43-0fc74f84a18b`) lines 516-530 [crates/gwiki/src/main.rs:516-530]
  - Signature: `fn print_error(format: output::Format, error: &WikiError) {`
  - Purpose: Prints a 'WikiError' to stderr as JSON with 'code' and 'message' in 'Json' mode, falling back to 'gwiki: {error}' text if JSON serialization fails, or emits the text form directly in 'Text' mode. [crates/gwiki/src/main.rs:516-530]
- `command_from_cli` (function) component `command_from_cli [function]` (`d513c18f-7899-5308-9605-2a8ae40e75de`) lines 532-659 [crates/gwiki/src/main.rs:532-659]
  - Signature: `fn command_from_cli(command: CliCommand, scope: ScopeSelection) -> Result<Command, WikiError> {`
  - Purpose: 'command_from_cli' converts a parsed 'CliCommand' plus 'ScopeSelection' into the corresponding internal 'Command', propagating scope and options while rejecting invalid 'remove-source' flag combinations and treating 'CliCommand::Contract' as unreachable. [crates/gwiki/src/main.rs:532-659]
- `from` (function) component `from [function]` (`a79cdc88-cc62-5b5d-bc5c-175e3547a041`) lines 662-668 [crates/gwiki/src/main.rs:662-668]
  - Signature: `fn from(kind: CompileKind) -> Self {`
  - Purpose: Converts a 'CompileKind' into the corresponding 'Self' enum variant by matching 'Source', 'Concept', and 'Topic' to 'Self::Source', 'Self::Concept', and 'Self::Topic', respectively. [crates/gwiki/src/main.rs:662-668]
- `from` (function) component `from [function]` (`868d2cb7-b94a-52b3-b0bc-e6170dd29a74`) lines 672-682 [crates/gwiki/src/main.rs:672-682]
  - Signature: `fn from(args: ExportArgs) -> Self {`
  - Purpose: Converts an 'ExportArgs' value into the corresponding 'Self' variant by mapping 'WorkflowAssets { output }' to 'Self::WorkflowAssets { filename: output }' and 'Report { output, source }' to 'Self::ReportFile { filename: output, source_path: source }'. [crates/gwiki/src/main.rs:672-682]
- `from` (function) component `from [function]` (`abbe9b98-5e2f-540e-a43f-e749f133f748`) lines 686-693 [crates/gwiki/src/main.rs:686-693]
  - Signature: `fn from(args: ReviewReportArgs) -> Self {`
  - Purpose: Constructs a 'Self' value by moving 'files', 'symbols', 'diff_path', and 'output' from the provided 'ReviewReportArgs' into the corresponding fields. [crates/gwiki/src/main.rs:686-693]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`8afe00d1-13b2-55cf-aef3-a93909df4db6`) lines 696-706 [crates/gwiki/src/main.rs:696-706]
  - Signature: `impl From<ScopeArgs> for ScopeSelection {`
  - Purpose: 'ScopeSelection' is constructed from 'ScopeArgs' by choosing 'topic(topic)' if 'topic' is set, otherwise 'project(project_root)' if 'project' is set, and falling back to 'detect()' when neither scope is provided. [crates/gwiki/src/main.rs:696-706]
- `ScopeSelection.from` (method) component `ScopeSelection.from [method]` (`7e668ebe-36ce-523f-bc55-f7e5694e3377`) lines 697-705 [crates/gwiki/src/main.rs:697-705]
  - Signature: `fn from(scope: ScopeArgs) -> Self {`
  - Purpose: Constructs 'Self' by preferring 'scope.topic' via 'Self::topic', otherwise 'scope.project' via 'Self::project', and falling back to 'Self::detect()' when neither scope field is set. [crates/gwiki/src/main.rs:697-705]
- `exit_code_for_error` (function) component `exit_code_for_error [function]` (`4bf5358c-b177-5f00-8c16-34757680b2af`) lines 708-725 [crates/gwiki/src/main.rs:708-725]
  - Signature: `fn exit_code_for_error(error: &WikiError) -> ExitCode {`
  - Purpose: Maps each 'WikiError' variant to a process exit code, returning 'ExitCode::from(2)' for user/input/query-related errors ('NotImplemented', 'InvalidInput', 'Index', 'Search', 'InvalidScope', 'NotFound') and 'ExitCode::from(1)' for configuration, I/O, parsing, registry, daemon, timeout, or setup errors. [crates/gwiki/src/main.rs:708-725]
- `from` (function) component `from [function]` (`20087995-ae54-5e0e-b070-74d2cd8550ab`) lines 728-744 [crates/gwiki/src/main.rs:728-744]
  - Signature: `fn from(args: SetupArgs) -> Self {`
  - Purpose: Constructs 'Self' by copying each corresponding field from 'SetupArgs' into the struct, preserving the setup configuration values unchanged. [crates/gwiki/src/main.rs:728-744]

