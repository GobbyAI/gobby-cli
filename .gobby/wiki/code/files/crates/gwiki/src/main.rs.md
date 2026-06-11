---
title: crates/gwiki/src/main.rs
type: code_file
provenance:
- file: crates/gwiki/src/main.rs
  ranges:
  - 46-60
  - 63-149
  - 152-167
  - 170-212
  - 215-225
  - 228-243
  - 246-254
  - 256-267
  - 270-285
  - 288-296
  - 304-312
  - 315-318
  - 321-324
  - 327-351
  - 354-369
  - 372-375
  - 378-391
  - 394-408
  - 411-415
  - '422'
  - 426-438
  - 427-429
  - 431-435
  - '437'
  - 440-447
  - 449-453
  - 455-507
  - 509-528
  - 530-532
  - 534-548
  - 550-701
  - 704-710
  - 714-724
  - 728-735
  - 738-748
  - 739-747
  - 750-767
  - 770-786
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/main.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/main.rs` exposes 38 indexed API symbols.
[crates/gwiki/src/main.rs:46-60]
[crates/gwiki/src/main.rs:63-149]
[crates/gwiki/src/main.rs:152-167]
[crates/gwiki/src/main.rs:170-212]
[crates/gwiki/src/main.rs:215-225]

## API Symbols

- `Cli` (class) component `Cli [class]` (`86726852-c29c-5e14-9fee-c96524fac045`) lines 46-60 [crates/gwiki/src/main.rs:46-60]
  - Signature: `struct Cli {`
  - Purpose: A clap-based CLI argument struct that flattens `ScopeArgs`, provides global `--format` (default: JSON) and `--quiet` flags, and routes execution to a subcommand. [crates/gwiki/src/main.rs:46-60]
- `CliCommand` (type) component `CliCommand [type]` (`2d1d3783-7c05-5ec3-88cb-2ef1e61ba34e`) lines 63-149 [crates/gwiki/src/main.rs:63-149]
  - Signature: `enum CliCommand {`
  - Purpose: Indexed type `CliCommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:63-149]
- `ScopeArgs` (class) component `ScopeArgs [class]` (`0041e70b-7127-5b3c-844e-87b1eff8f202`) lines 152-167 [crates/gwiki/src/main.rs:152-167]
  - Signature: `struct ScopeArgs {`
  - Purpose: `ScopeArgs` defines mutually exclusive global CLI arguments for specifying a wiki scope using either a Gobby project root directory (defaulting to the current directory) or a named topic identifier. [crates/gwiki/src/main.rs:152-167]
- `SetupArgs` (class) component `SetupArgs [class]` (`cba31c93-694c-52b9-9c54-dac8833582fb`) lines 170-212 [crates/gwiki/src/main.rs:170-212]
  - Signature: `struct SetupArgs {`
  - Purpose: `SetupArgs` is a CLI argument struct that configures provisioning of a Gobby wiki instance with optional backends for PostgreSQL, FalkorDB (graph database), Qdrant (vector database), and embedding services. [crates/gwiki/src/main.rs:170-212]
- `SearchArgs` (class) component `SearchArgs [class]` (`b838b613-d550-5bae-b339-3f3dfc9b6b6e`) lines 215-225 [crates/gwiki/src/main.rs:215-225]
  - Signature: `struct SearchArgs {`
  - Purpose: SearchArgs is a command-line argument struct that configures a search operation with a required query string, an optional result limit (defaulting to 10), and a boolean flag to disable semantic vector search. [crates/gwiki/src/main.rs:215-225]
- `AskArgs` (class) component `AskArgs [class]` (`7fdc4c76-6859-5620-bfc0-000e08a203c9`) lines 228-243 [crates/gwiki/src/main.rs:228-243]
  - Signature: `struct AskArgs {`
  - Purpose: `AskArgs` defines CLI arguments for question answering with optional LLM-based synthesis of wiki results, configurable AI routing modes (auto/daemon/direct/off), and optional strict enforcement of synthesis success. [crates/gwiki/src/main.rs:228-243]
- `BenchmarkArgs` (class) component `BenchmarkArgs [class]` (`7ed6ada6-e9c2-55cd-b19f-c6f86a7f2aec`) lines 246-254 [crates/gwiki/src/main.rs:246-254]
  - Signature: `struct BenchmarkArgs {`
  - Purpose: BenchmarkArgs is a command-line argument struct that specifies the number of retrieval candidates to use for benchmarking seeded retrieval precision probes, with a required positive integer value and default configuration. [crates/gwiki/src/main.rs:246-254]
- `parse_positive_usize` (function) component `parse_positive_usize [function]` (`5deeca42-eb60-5d2b-a630-24147c60d4ae`) lines 256-267 [crates/gwiki/src/main.rs:256-267]
  - Signature: `fn parse_positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Parses a string into a `usize` and validates that it is strictly positive (greater than zero), returning the value or a string error message. [crates/gwiki/src/main.rs:256-267]
- `RemoveSourceArgs` (class) component `RemoveSourceArgs [class]` (`8c605949-9ed9-5f9c-82d5-85b11af2242e`) lines 270-285 [crates/gwiki/src/main.rs:270-285]
  - Signature: `struct RemoveSourceArgs {`
  - Purpose: RemoveSourceArgs defines command-line arguments for removing a vault source by ID, with optional flags for non-destructive preview (dry_run), confirmation of destructive deletion (yes), and preservation of the associated raw source asset (keep_asset). [crates/gwiki/src/main.rs:270-285]
- `RefreshArgs` (class) component `RefreshArgs [class]` (`eb9e3055-9055-55aa-b7c0-4e4bce26bf1d`) lines 288-296 [crates/gwiki/src/main.rs:288-296]
  - Signature: `struct RefreshArgs {`
  - Purpose: RefreshArgs is a command-line argument struct that accepts multiple source IDs to refresh and provides an optional dry-run flag to preview candidates without performing any persistence operations (fetching, writing, deleting, or indexing). [crates/gwiki/src/main.rs:288-296]
- `ReadArgs` (class) component `ReadArgs [class]` (`b93d9fb0-06f1-5256-a433-035bb3f32225`) lines 304-312 [crates/gwiki/src/main.rs:304-312]
  - Signature: `struct ReadArgs {`
  - Purpose: `ReadArgs` is a command-line argument struct that accepts an optional vault-relative wiki path and an optional first-heading title to resolve within the selected scope. [crates/gwiki/src/main.rs:304-312]
- `BacklinksArgs` (class) component `BacklinksArgs [class]` (`f2f6a1a6-bb27-5d3d-bc5f-2f7e62394be5`) lines 315-318 [crates/gwiki/src/main.rs:315-318]
  - Signature: `struct BacklinksArgs {`
  - Purpose: `BacklinksArgs` is a command-line argument struct that captures a single required `page` parameter of type `String` to specify the target page for backlink operations. [crates/gwiki/src/main.rs:315-318]
- `LinkSuggestArgs` (class) component `LinkSuggestArgs [class]` (`8b9603aa-862a-5f96-84b6-578c054b0544`) lines 321-324 [crates/gwiki/src/main.rs:321-324]
  - Signature: `struct LinkSuggestArgs {`
  - Purpose: LinkSuggestArgs is a clap-based CLI argument struct with a single `limit: usize` field that accepts a `--limit` long flag argument, defaulting to 10 when unspecified. [crates/gwiki/src/main.rs:321-324]
- `ResearchArgs` (class) component `ResearchArgs [class]` (`82cbced1-8e6b-5c0f-903b-e7714c662870`) lines 327-351 [crates/gwiki/src/main.rs:327-351]
  - Signature: `struct ResearchArgs {`
  - Purpose: ResearchArgs is a Rust CLI argument struct that configures a research operation with parameters for a target question, source constraints, execution limits (max steps, tokens, and sources), AI routing mode, and audit controls. [crates/gwiki/src/main.rs:327-351]
- `CompileArgs` (class) component `CompileArgs [class]` (`681e096e-f7e8-559a-a165-5c3eb9277d72`) lines 354-369 [crates/gwiki/src/main.rs:354-369]
  - Signature: `struct CompileArgs {`
  - Purpose: CompileArgs is a command-line argument structure that captures compilation configuration through an optional topic string, variable outline headings, a CompileKind enum selector, an optional target PathBuf, and a boolean write-intent flag. [crates/gwiki/src/main.rs:354-369]
- `ExportArgs` (class) component `ExportArgs [class]` (`b32f0410-7cc6-5a63-88ab-d8a207f94991`) lines 372-375 [crates/gwiki/src/main.rs:372-375]
  - Signature: `struct ExportArgs {`
  - Purpose: `ExportArgs` is a clap CLI argument struct that contains a single `ExportSubcommand` field annotated for subcommand routing. [crates/gwiki/src/main.rs:372-375]
- `ReviewReportArgs` (class) component `ReviewReportArgs [class]` (`c543bbfa-65f8-5994-b916-7fad331d87d1`) lines 378-391 [crates/gwiki/src/main.rs:378-391]
  - Signature: `struct ReviewReportArgs {`
  - Purpose: `ReviewReportArgs` is a clap CLI argument struct that collects multiple file paths, symbol identifiers, an optional diff file path, and an output filename for review report generation. [crates/gwiki/src/main.rs:378-391]
- `ExportSubcommand` (type) component `ExportSubcommand [type]` (`dfd94326-d3f7-54f4-9df3-8689dd6496f4`) lines 394-408 [crates/gwiki/src/main.rs:394-408]
  - Signature: `enum ExportSubcommand {`
  - Purpose: Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:394-408]
- `CompileKind` (type) component `CompileKind [type]` (`88d13355-ab0d-5ff9-b1a3-2745892cf99e`) lines 411-415 [crates/gwiki/src/main.rs:411-415]
  - Signature: `enum CompileKind {`
  - Purpose: Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:411-415]
- `StderrLogger` (class) component `StderrLogger [class]` (`7b96e88c-3c5f-5695-9f62-a6400f1bc062`) lines 422-422 [crates/gwiki/src/main.rs:422]
  - Signature: `struct StderrLogger;`
  - Purpose: StderrLogger is a struct that implements a logger which writes output to the standard error stream (stderr). [crates/gwiki/src/main.rs:422]
- `StderrLogger` (class) component `StderrLogger [class]` (`ca1ecce0-d046-5977-b3ae-422c264a456f`) lines 426-438 [crates/gwiki/src/main.rs:426-438]
  - Signature: `impl log::Log for StderrLogger {`
  - Purpose: StderrLogger implements Rust's `log::Log` trait to write log records to stderr with format `gwiki: {level}: {message}` when their severity level is at or below the configured maximum. [crates/gwiki/src/main.rs:426-438]
- `StderrLogger.enabled` (method) component `StderrLogger.enabled [method]` (`5ce1048d-cf0a-5464-9695-6dd8de9a69ba`) lines 427-429 [crates/gwiki/src/main.rs:427-429]
  - Signature: `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {`
  - Purpose: This method determines whether logging is enabled for a given metadata entry by comparing its log level against the globally configured maximum log level. [crates/gwiki/src/main.rs:427-429]
- `StderrLogger.log` (method) component `StderrLogger.log [method]` (`aa8bcc06-1676-5705-a052-896cded0f007`) lines 431-435 [crates/gwiki/src/main.rs:431-435]
  - Signature: `fn log(&self, record: &log::Record<'_>) {`
  - Purpose: This method conditionally writes log records to stderr with a "gwiki:" prefix and message level if logging is enabled for the record's metadata. [crates/gwiki/src/main.rs:431-435]
- `StderrLogger.flush` (method) component `StderrLogger.flush [method]` (`c04e2c0d-b1ac-5978-a8dd-1677505a27d3`) lines 437-437 [crates/gwiki/src/main.rs:437]
  - Signature: `fn flush(&self) {}`
  - Purpose: A no-op method that takes an immutable self reference and performs no operation. [crates/gwiki/src/main.rs:437]
- `log_level` (function) component `log_level [function]` (`098f390b-f723-58a1-b07a-c66838025980`) lines 440-447 [crates/gwiki/src/main.rs:440-447]
  - Signature: `fn log_level(quiet: bool, rust_log: Option<&str>) -> log::LevelFilter {`
  - Purpose: Determines the log level filter by returning `LevelFilter::Off` if quiet mode is enabled, otherwise parsing the provided `rust_log` string as a filter level with a fallback to `Off`. [crates/gwiki/src/main.rs:440-447]
- `init_logger` (function) component `init_logger [function]` (`6abc7d36-eb0a-54bc-bfc6-c60adde49957`) lines 449-453 [crates/gwiki/src/main.rs:449-453]
  - Signature: `fn init_logger(quiet: bool) {`
  - Purpose: Initializes the logging framework by setting STDERR_LOGGER as the global logger and configuring its maximum level based on the `quiet` flag and optional `RUST_LOG` environment variable. [crates/gwiki/src/main.rs:449-453]
- `main` (function) component `main [function]` (`f1e3d959-2f55-564f-848f-8a55c15deba3`) lines 455-507 [crates/gwiki/src/main.rs:455-507]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: This function parses CLI arguments, outputs the contract specification if the contract subcommand is requested, otherwise executes the specified command via `gobby_wiki::run()` and returns an appropriate exit code reflecting the outcome. [crates/gwiki/src/main.rs:455-507]
- `normalize_project_flag_args` (function) component `normalize_project_flag_args [function]` (`964d611f-f2ae-50f5-af29-0956223b070f`) lines 509-528 [crates/gwiki/src/main.rs:509-528]
  - Signature: `fn normalize_project_flag_args<I, S>(args: I) -> Vec<OsString>`
  - Purpose: Normalizes command-line arguments by inserting a default project path (`"."`) when a `--project` flag is immediately followed by a CLI subcommand instead of a project identifier. [crates/gwiki/src/main.rs:509-528]
- `is_cli_subcommand` (function) component `is_cli_subcommand [function]` (`9248d8cd-920f-5ce7-bc04-1c4f901c9e66`) lines 530-532 [crates/gwiki/src/main.rs:530-532]
  - Signature: `fn is_cli_subcommand(value: &str) -> bool {`
  - Purpose: This function returns a boolean indicating whether the input string is a member of the `CLI_SUBCOMMANDS` collection. [crates/gwiki/src/main.rs:530-532]
- `print_error` (function) component `print_error [function]` (`8ac52c82-1530-56cd-9c49-803b1cc5d797`) lines 534-548 [crates/gwiki/src/main.rs:534-548]
  - Signature: `fn print_error(format: output::Format, error: &WikiError) {`
  - Purpose: Writes a WikiError to standard error in either JSON format (with code and message fields) or plaintext based on the Format parameter, with automatic fallback to plaintext on JSON serialization failure. [crates/gwiki/src/main.rs:534-548]
- `command_from_cli` (function) component `command_from_cli [function]` (`a43d2393-a4cb-5b28-8d56-b11e6e2d42c1`) lines 550-701 [crates/gwiki/src/main.rs:550-701]
  - Signature: `fn command_from_cli(command: CliCommand, scope: ScopeSelection) -> Result<Command, WikiError> {`
  - Purpose: Converts CLI command enum variants into internal `Command` enum variants while injecting scope context, translating arguments into domain-specific options, and validating flag constraints. [crates/gwiki/src/main.rs:550-701]
- `from` (function) component `from [function]` (`4d96842b-77c6-5951-9884-fb5b4b0dad0c`) lines 704-710 [crates/gwiki/src/main.rs:704-710]
  - Signature: `fn from(kind: CompileKind) -> Self {`
  - Purpose: This function implements the `From` trait to convert a `CompileKind` enum value to the implementing type by exhaustively mapping each source variant to its corresponding target variant. [crates/gwiki/src/main.rs:704-710]
- `from` (function) component `from [function]` (`18d2618d-d9fa-5872-83c8-e85c2d31f280`) lines 714-724 [crates/gwiki/src/main.rs:714-724]
  - Signature: `fn from(args: ExportArgs) -> Self {`
  - Purpose: A `From<ExportArgs>` trait implementation that converts command-line export arguments into `Self` by pattern matching on the command subtype and remapping the enum variants with field name transformations. [crates/gwiki/src/main.rs:714-724]
- `from` (function) component `from [function]` (`7d2c9b6f-9a6d-5549-bd2c-1b90e24e30d6`) lines 728-735 [crates/gwiki/src/main.rs:728-735]
  - Signature: `fn from(args: ReviewReportArgs) -> Self {`
  - Purpose: Converts a `ReviewReportArgs` struct into `Self` by extracting and directly mapping its four fields (`files`, `symbols`, `diff_path`, `output`). [crates/gwiki/src/main.rs:728-735]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`2a283de8-2c1e-5b8c-b9af-820bd8b0ba85`) lines 738-748 [crates/gwiki/src/main.rs:738-748]
  - Signature: `impl From<ScopeArgs> for ScopeSelection {`
  - Purpose: This implementation converts `ScopeArgs` into `ScopeSelection` using cascading conditional logic that prioritizes topic scope, then project scope, and defaults to auto-detection. [crates/gwiki/src/main.rs:738-748]
- `ScopeSelection.from` (method) component `ScopeSelection.from [method]` (`e3784a84-4677-5fe8-80e9-eb1e89d20b03`) lines 739-747 [crates/gwiki/src/main.rs:739-747]
  - Signature: `fn from(scope: ScopeArgs) -> Self {`
  - Purpose: This method constructs an instance of `Self` from `ScopeArgs` by attempting initialization from an explicit topic, then an explicit project root, before falling back to automatic detection. [crates/gwiki/src/main.rs:739-747]
- `exit_code_for_error` (function) component `exit_code_for_error [function]` (`c59e8657-a24f-5678-a16a-14261568da94`) lines 750-767 [crates/gwiki/src/main.rs:750-767]
  - Signature: `fn exit_code_for_error(error: &WikiError) -> ExitCode {`
  - Purpose: Converts `WikiError` variants to exit codes, returning 2 for user/input errors (NotImplemented, InvalidInput, Index, Search, InvalidScope, NotFound) and 1 for system/configuration errors (Config, Io, Json, Yaml, Registry, Daemon, Timeout, Setup). [crates/gwiki/src/main.rs:750-767]
- `from` (function) component `from [function]` (`caa49523-7b3a-541c-91d2-41babcfe1eba`) lines 770-786 [crates/gwiki/src/main.rs:770-786]
  - Signature: `fn from(args: SetupArgs) -> Self {`
  - Purpose: Implements the `From` trait to convert `SetupArgs` into `Self` by mapping each argument field to the corresponding struct field. [crates/gwiki/src/main.rs:770-786]

