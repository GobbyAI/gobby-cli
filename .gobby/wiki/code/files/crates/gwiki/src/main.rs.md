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
  - 324-349
  - 352-355
  - 358-371
  - 374-388
  - 391-395
  - '402'
  - 406-418
  - 420-427
  - 429-433
  - 435-487
  - 494-513
  - 515-517
  - 519-533
  - 535-663
  - 666-672
  - 676-686
  - 690-697
  - 700-710
  - 712-729
  - 732-748
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/main.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file is the `gwiki` binary entrypoint and CLI definition. It uses `clap` to parse global scope and output options plus a large subcommand enum, then maps those parsed arguments into internal `gobby_wiki::Command` and related config types. It also normalizes `--project` usage, selects the active wiki scope, initializes a stderr logger, formats errors and exit codes, and runs `main` to execute the chosen command or print the CLI contract.
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
- `CompileArgs` (class) component `CompileArgs [class]` (`bc6d427d-7dbb-5bc3-a948-4538a3792977`) lines 324-349 [crates/gwiki/src/main.rs:324-349]
  - Signature: `struct CompileArgs {`
  - Purpose: 'CompileArgs' is a 'clap' argument struct for a compile command that accepts an optional positional 'topic' (with a distinct internal id to avoid scope-arg collisions), repeated '--outline' and '--source' values, a '--kind' enum defaulting to 'topic', an optional '--target' page path, a '--write-intent' flag, and an '--ai' routing mode defaulting to 'auto'. [crates/gwiki/src/main.rs:324-349]
- `ExportArgs` (class) component `ExportArgs [class]` (`085f610e-6c34-5454-8f33-8615f672c50f`) lines 352-355 [crates/gwiki/src/main.rs:352-355]
  - Signature: `struct ExportArgs {`
  - Purpose: 'ExportArgs' is a Rust command-line argument struct that contains a single required 'command' field of type 'ExportSubcommand', which is registered as a subcommand via '#[command(subcommand)]'. [crates/gwiki/src/main.rs:352-355]
- `ReviewReportArgs` (class) component `ReviewReportArgs [class]` (`a4016c1e-da5c-5af1-94e3-728bb8b2be91`) lines 358-371 [crates/gwiki/src/main.rs:358-371]
  - Signature: `struct ReviewReportArgs {`
  - Purpose: 'ReviewReportArgs' is a command-line argument struct that collects zero or more '--file' paths and '--symbol' IDs, an optional '--diff' path, and an '--output' filename defaulting to 'review-report.md' for generating a review report. [crates/gwiki/src/main.rs:358-371]
- `ExportSubcommand` (type) component `ExportSubcommand [type]` (`54aab7a6-b37d-5cde-a79b-0cae98d467ab`) lines 374-388 [crates/gwiki/src/main.rs:374-388]
  - Signature: `enum ExportSubcommand {`
  - Purpose: Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:374-388]
- `CompileKind` (type) component `CompileKind [type]` (`9cf6eb93-0dd9-55aa-99ee-b8deaa1f1c19`) lines 391-395 [crates/gwiki/src/main.rs:391-395]
  - Signature: `enum CompileKind {`
  - Purpose: Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:391-395]
- `StderrLogger` (class) component `StderrLogger [class]` (`68df5012-f8bc-52f1-9b4e-d54301f3b356`) lines 402-402 [crates/gwiki/src/main.rs:402]
  - Signature: `struct StderrLogger;`
  - Purpose: 'StderrLogger' is an empty struct type that represents a logger implementation intended to emit log output to standard error. [crates/gwiki/src/main.rs:402]
- `StderrLogger` (class) component `StderrLogger [class]` (`a374035c-1882-5a86-98db-a7b0594cb601`) lines 406-418 [crates/gwiki/src/main.rs:406-418]
  - Signature: `impl log::Log for StderrLogger {`
  - Purpose: 'StderrLogger' is a 'log::Log' implementation that emits enabled log records at or below the global max level to stderr in the format 'gwiki: <level>: <message>', and otherwise ignores them. [crates/gwiki/src/main.rs:406-418]
- `StderrLogger.enabled` (method) component `StderrLogger.enabled [method]` (`4bd62c3a-8283-5aaf-99a8-bede6114fad9`) lines 407-409 [crates/gwiki/src/main.rs:407-409]
  - Signature: `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {`
  - Purpose: Returns 'true' when the record’s 'metadata.level()' is less than or equal to the current global 'log::max_level()', and 'false' otherwise. [crates/gwiki/src/main.rs:407-409]
- `StderrLogger.log` (method) component `StderrLogger.log [method]` (`8388e620-88ac-5d17-8ff9-25662519313d`) lines 411-415 [crates/gwiki/src/main.rs:411-415]
  - Signature: `fn log(&self, record: &log::Record<'_>) {`
  - Purpose: If the record’s metadata passes 'enabled', this method writes a 'gwiki: <level>: <args>' line to standard error using 'eprintln!'. [crates/gwiki/src/main.rs:411-415]
- `StderrLogger.flush` (method) component `StderrLogger.flush [method]` (`cad07935-ecac-5d19-866a-c4faad6211b3`) lines 417-417 [crates/gwiki/src/main.rs:417]
  - Signature: `fn flush(&self) {}`
  - Purpose: 'flush' is a no-op method that takes an immutable reference to 'self' and returns '()', performing no state changes or side effects. [crates/gwiki/src/main.rs:417]
- `log_level` (function) component `log_level [function]` (`9e2c65de-80dd-57ae-8fe3-82b356b8a6da`) lines 420-427 [crates/gwiki/src/main.rs:420-427]
  - Signature: `fn log_level(quiet: bool, rust_log: Option<&str>) -> log::LevelFilter {`
  - Purpose: Returns 'log::LevelFilter::Off' when 'quiet' is 'true', otherwise attempts to parse the trimmed 'rust_log' string into a 'LevelFilter' and falls back to 'Off' if absent or invalid. [crates/gwiki/src/main.rs:420-427]
- `init_logger` (function) component `init_logger [function]` (`dd8c671d-c4b2-552e-a789-fe523f31ef98`) lines 429-433 [crates/gwiki/src/main.rs:429-433]
  - Signature: `fn init_logger(quiet: bool) {`
  - Purpose: Initializes the global logger by reading 'RUST_LOG', installing 'STDERR_LOGGER', and setting the maximum log level via 'log_level(quiet, rust_log.as_deref())'. [crates/gwiki/src/main.rs:429-433]
- `main` (function) component `main [function]` (`25498bb2-221c-5ac1-bce9-5d59a7480ecf`) lines 435-487 [crates/gwiki/src/main.rs:435-487]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Parses CLI arguments, initializes logging, optionally prints the gwiki CLI contract, otherwise constructs and runs a 'gobby_wiki' command and renders either the result or any error before returning an appropriate 'ExitCode'. [crates/gwiki/src/main.rs:435-487]
- `normalize_project_flag_args` (function) component `normalize_project_flag_args [function]` (`07fb5f5e-ec02-5463-834d-140ba5081d8a`) lines 494-513 [crates/gwiki/src/main.rs:494-513]
  - Signature: `fn normalize_project_flag_args<I, S>(args: I) -> Vec<OsString>`
  - Purpose: Takes an iterator of arguments, clones them into a new 'Vec<OsString>', and inserts an extra '"."' immediately after any '--project' argument whose following argument is a CLI subcommand string. [crates/gwiki/src/main.rs:494-513]
- `is_cli_subcommand` (function) component `is_cli_subcommand [function]` (`ad93918c-b867-5af0-9d41-2059558e624d`) lines 515-517 [crates/gwiki/src/main.rs:515-517]
  - Signature: `fn is_cli_subcommand(value: &str) -> bool {`
  - Purpose: Returns 'true' if 'value' is present in the 'CLI_SUBCOMMANDS' collection, and 'false' otherwise. [crates/gwiki/src/main.rs:515-517]
- `print_error` (function) component `print_error [function]` (`a1dfbac8-0a57-5866-a4c0-46a611343e23`) lines 519-533 [crates/gwiki/src/main.rs:519-533]
  - Signature: `fn print_error(format: output::Format, error: &WikiError) {`
  - Purpose: Prints a 'WikiError' to stderr either as JSON with 'code' and 'message' fields, falling back to 'gwiki: {error}' if JSON emission fails, or as plain 'gwiki: {error}' text for 'output::Format::Text'. [crates/gwiki/src/main.rs:519-533]
- `command_from_cli` (function) component `command_from_cli [function]` (`7317f4b6-d3bc-5d0e-b87d-18df80a3dcb9`) lines 535-663 [crates/gwiki/src/main.rs:535-663]
  - Signature: `fn command_from_cli(command: CliCommand, scope: ScopeSelection) -> Result<Command, WikiError> {`
  - Purpose: 'command_from_cli' translates a parsed 'CliCommand' plus 'ScopeSelection' into the corresponding internal 'Command' variant, preserving scope and options while rejecting invalid 'remove-source' flag combinations and treating 'CliCommand::Contract' as unreachable. [crates/gwiki/src/main.rs:535-663]
- `from` (function) component `from [function]` (`4b1470ad-4514-5652-b046-e2702016efad`) lines 666-672 [crates/gwiki/src/main.rs:666-672]
  - Signature: `fn from(kind: CompileKind) -> Self {`
  - Purpose: Converts a 'CompileKind' value into the corresponding 'Self' enum variant by matching 'Source', 'Concept', and 'Topic' one-to-one. [crates/gwiki/src/main.rs:666-672]
- `from` (function) component `from [function]` (`cab483bb-d571-5f3e-82ae-f059c391ce47`) lines 676-686 [crates/gwiki/src/main.rs:676-686]
  - Signature: `fn from(args: ExportArgs) -> Self {`
  - Purpose: Converts an 'ExportArgs' into the corresponding 'Self' variant by mapping 'WorkflowAssets { output }' to 'Self::WorkflowAssets { filename: output }' and 'Report { output, source }' to 'Self::ReportFile { filename: output, source_path: source }'. [crates/gwiki/src/main.rs:676-686]
- `from` (function) component `from [function]` (`a1cd11cc-4250-564a-bec3-d87e53ec7d55`) lines 690-697 [crates/gwiki/src/main.rs:690-697]
  - Signature: `fn from(args: ReviewReportArgs) -> Self {`
  - Purpose: Constructs a 'Self' by moving 'files', 'symbols', 'diff_path', and 'output' from 'ReviewReportArgs' into the corresponding fields. [crates/gwiki/src/main.rs:690-697]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`5229a1ee-cf2b-518f-9f32-b7d05c65cfc4`) lines 700-710 [crates/gwiki/src/main.rs:700-710]
  - Signature: `impl From<ScopeArgs> for ScopeSelection {`
  - Purpose: 'ScopeSelection' is constructed from 'ScopeArgs' by choosing the first available scope in priority order: 'topic', then 'project', otherwise falling back to automatic detection. [crates/gwiki/src/main.rs:700-710]
- `ScopeSelection.from` (method) component `ScopeSelection.from [method]` (`9ab30698-6ae5-5135-901c-c9f6408c7c53`) lines 701-709 [crates/gwiki/src/main.rs:701-709]
  - Signature: `fn from(scope: ScopeArgs) -> Self {`
  - Purpose: Constructs a 'Self' by preferring 'scope.topic' via 'Self::topic', otherwise 'scope.project' via 'Self::project', and falling back to 'Self::detect()' when neither is present. [crates/gwiki/src/main.rs:701-709]
- `exit_code_for_error` (function) component `exit_code_for_error [function]` (`4e872ca4-4ab8-59f4-b12b-1ec5fe037b29`) lines 712-729 [crates/gwiki/src/main.rs:712-729]
  - Signature: `fn exit_code_for_error(error: &WikiError) -> ExitCode {`
  - Purpose: Maps a 'WikiError' variant to a process 'ExitCode', returning '2' for user/input and lookup failures ('NotImplemented', 'InvalidInput', 'Index', 'Search', 'InvalidScope', 'NotFound') and '1' for configuration, I/O, parsing, registry, daemon, timeout, and setup errors. [crates/gwiki/src/main.rs:712-729]
- `from` (function) component `from [function]` (`99f6613a-35c0-56a6-aaf2-b61db1d7c1ad`) lines 732-748 [crates/gwiki/src/main.rs:732-748]
  - Signature: `fn from(args: SetupArgs) -> Self {`
  - Purpose: Constructs 'Self' by copying each configuration field from the provided 'SetupArgs' into the corresponding struct fields without transformation. [crates/gwiki/src/main.rs:732-748]

