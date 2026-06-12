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
  - 354-372
  - 375-378
  - 381-394
  - 397-411
  - 414-418
  - '425'
  - 429-441
  - 443-450
  - 452-456
  - 458-510
  - 517-536
  - 538-540
  - 542-556
  - 558-709
  - 712-718
  - 722-732
  - 736-743
  - 746-756
  - 758-775
  - 778-794
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
  - Purpose: `Cli` is the top-level command-line argument container that flattens shared `ScopeArgs`, defines global `--format` and `--quiet` flags, and dispatches execution to a `CliCommand` subcommand. [crates/gwiki/src/main.rs:46-60]
- `CliCommand` (type) component `CliCommand [type]` (`2d1d3783-7c05-5ec3-88cb-2ef1e61ba34e`) lines 63-149 [crates/gwiki/src/main.rs:63-149]
  - Signature: `enum CliCommand {`
  - Purpose: Indexed type `CliCommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:63-149]
- `ScopeArgs` (class) component `ScopeArgs [class]` (`0041e70b-7127-5b3c-844e-87b1eff8f202`) lines 152-167 [crates/gwiki/src/main.rs:152-167]
  - Signature: `struct ScopeArgs {`
  - Purpose: `ScopeArgs` is a Clap argument struct that defines mutually exclusive global `--project [ROOT]` and `--topic NAME` options for selecting a Gobby wiki scope, with bare `--project` defaulting to the current directory (`.`). [crates/gwiki/src/main.rs:152-167]
- `SetupArgs` (class) component `SetupArgs [class]` (`cba31c93-694c-52b9-9c54-dac8833582fb`) lines 170-212 [crates/gwiki/src/main.rs:170-212]
  - Signature: `struct SetupArgs {`
  - Purpose: `SetupArgs` is a `clap`-parsed configuration struct for the setup command that controls standalone hub resolution, Docker service provisioning, PostgreSQL connectivity, FalkorDB/Qdrant endpoints, and embedding provider/model/API parameters. [crates/gwiki/src/main.rs:170-212]
- `SearchArgs` (class) component `SearchArgs [class]` (`b838b613-d550-5bae-b339-3f3dfc9b6b6e`) lines 215-225 [crates/gwiki/src/main.rs:215-225]
  - Signature: `struct SearchArgs {`
  - Purpose: `SearchArgs` is a command-line argument struct that captures a required search `query`, an optional result `limit` defaulting to `10`, and a `--no-semantic` flag to disable semantic vector search for the request. [crates/gwiki/src/main.rs:215-225]
- `AskArgs` (class) component `AskArgs [class]` (`7fdc4c76-6859-5620-bfc0-000e08a203c9`) lines 228-243 [crates/gwiki/src/main.rs:228-243]
  - Signature: `struct AskArgs {`
  - Purpose: `AskArgs` is a CLI argument struct that takes a required `QUESTION` string and optional `--llm`, `--ai` routing, and `--require-ai` flags to control AI-backed synthesis of retrieved wiki hits. [crates/gwiki/src/main.rs:228-243]
- `BenchmarkArgs` (class) component `BenchmarkArgs [class]` (`7ed6ada6-e9c2-55cd-b19f-c6f86a7f2aec`) lines 246-254 [crates/gwiki/src/main.rs:246-254]
  - Signature: `struct BenchmarkArgs {`
  - Purpose: `BenchmarkArgs` is a CLI argument struct that configures the number of seeded retrieval precision probes to run via the `--retrieval-candidates` option, which must parse as a positive `usize` and defaults to `BenchmarkOptions::DEFAULT_RETRIEVAL_CANDIDATES`. [crates/gwiki/src/main.rs:246-254]
- `parse_positive_usize` (function) component `parse_positive_usize [function]` (`5deeca42-eb60-5d2b-a630-24147c60d4ae`) lines 256-267 [crates/gwiki/src/main.rs:256-267]
  - Signature: `fn parse_positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Parses `value` as a `usize`, returning the parsed number when it is strictly greater than zero, otherwise returning either the parse error as a `String` or `"must be greater than zero"` for `0`. [crates/gwiki/src/main.rs:256-267]
- `RemoveSourceArgs` (class) component `RemoveSourceArgs [class]` (`8c605949-9ed9-5f9c-82d5-85b11af2242e`) lines 270-285 [crates/gwiki/src/main.rs:270-285]
  - Signature: `struct RemoveSourceArgs {`
  - Purpose: `RemoveSourceArgs` is a CLI argument struct for removing a source by `--id`, with flags to preview the operation via `--dry-run`, confirm destructive deletion via `--yes`, and preserve the referenced raw asset via `--keep-asset`. [crates/gwiki/src/main.rs:270-285]
- `RefreshArgs` (class) component `RefreshArgs [class]` (`eb9e3055-9055-55aa-b7c0-4e4bce26bf1d`) lines 288-296 [crates/gwiki/src/main.rs:288-296]
  - Signature: `struct RefreshArgs {`
  - Purpose: `RefreshArgs` is a CLI options struct that collects zero or more explicit `--id <SOURCE_ID>` values to refresh and an optional `--dry-run` flag to preview refresh candidates without fetching, writing, deleting, or indexing. [crates/gwiki/src/main.rs:288-296]
- `ReadArgs` (class) component `ReadArgs [class]` (`b93d9fb0-06f1-5256-a433-035bb3f32225`) lines 304-312 [crates/gwiki/src/main.rs:304-312]
  - Signature: `struct ReadArgs {`
  - Purpose: `ReadArgs` is a CLI argument struct that accepts an optional vault-relative wiki `path` and an optional first-heading `title` used to resolve which document to read within the selected scope. [crates/gwiki/src/main.rs:304-312]
- `BacklinksArgs` (class) component `BacklinksArgs [class]` (`f2f6a1a6-bb27-5d3d-bc5f-2f7e62394be5`) lines 315-318 [crates/gwiki/src/main.rs:315-318]
  - Signature: `struct BacklinksArgs {`
  - Purpose: `BacklinksArgs` is a CLI argument struct that defines one required positional `PAGE` parameter, stored as a `String` in the `page` field. [crates/gwiki/src/main.rs:315-318]
- `LinkSuggestArgs` (class) component `LinkSuggestArgs [class]` (`8b9603aa-862a-5f96-84b6-578c054b0544`) lines 321-324 [crates/gwiki/src/main.rs:321-324]
  - Signature: `struct LinkSuggestArgs {`
  - Purpose: `LinkSuggestArgs` is a command-line argument struct that exposes a single `--limit` `usize` option with a default value of `10` to bound the number of link suggestions returned. [crates/gwiki/src/main.rs:321-324]
- `ResearchArgs` (class) component `ResearchArgs [class]` (`82cbced1-8e6b-5c0f-903b-e7714c662870`) lines 327-351 [crates/gwiki/src/main.rs:327-351]
  - Signature: `struct ResearchArgs {`
  - Purpose: `ResearchArgs` is a Clap CLI argument struct for a research command that captures an optional `QUESTION`, a list of `source-constraint` filters, audit mode, configurable caps on steps/tokens/sources, and AI routing controls (`ai` and `require-ai`). [crates/gwiki/src/main.rs:327-351]
- `CompileArgs` (class) component `CompileArgs [class]` (`681e096e-f7e8-559a-a165-5c3eb9277d72`) lines 354-372 [crates/gwiki/src/main.rs:354-372]
  - Signature: `struct CompileArgs {`
  - Purpose: `CompileArgs` is a Clap argument struct for a compile operation that carries an optional topic selector, one or more outline headings, a `CompileKind` enum defaulting to `topic`, an optional target page path, and a `write-intent` flag. [crates/gwiki/src/main.rs:354-372]
- `ExportArgs` (class) component `ExportArgs [class]` (`f7bff84b-d8ab-5117-8c89-21bc75acca55`) lines 375-378 [crates/gwiki/src/main.rs:375-378]
  - Signature: `struct ExportArgs {`
  - Purpose: `ExportArgs` is a CLI argument struct that holds a single `ExportSubcommand` field, marking the selected export-related subcommand as the command-line entry point. [crates/gwiki/src/main.rs:375-378]
- `ReviewReportArgs` (class) component `ReviewReportArgs [class]` (`8081f265-2506-5aeb-a447-d2ff5e98e105`) lines 381-394 [crates/gwiki/src/main.rs:381-394]
  - Signature: `struct ReviewReportArgs {`
  - Purpose: `ReviewReportArgs` is a Clap-derived Rust CLI argument struct that collects zero or more input file paths and symbol IDs, an optional diff file path, and an output filename defaulting to `review-report.md` for generating a review report. [crates/gwiki/src/main.rs:381-394]
- `ExportSubcommand` (type) component `ExportSubcommand [type]` (`fe579df5-f884-5c6f-85fc-03c4e0b7a779`) lines 397-411 [crates/gwiki/src/main.rs:397-411]
  - Signature: `enum ExportSubcommand {`
  - Purpose: Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:397-411]
- `CompileKind` (type) component `CompileKind [type]` (`f6f63a3d-4124-5dd4-ade9-6129a15fa3e4`) lines 414-418 [crates/gwiki/src/main.rs:414-418]
  - Signature: `enum CompileKind {`
  - Purpose: Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:414-418]
- `StderrLogger` (class) component `StderrLogger [class]` (`748d5eb7-0581-5610-a61a-a6f7b6661bb7`) lines 425-425 [crates/gwiki/src/main.rs:425]
  - Signature: `struct StderrLogger;`
  - Purpose: `StderrLogger` is an opaque forward declaration for a `struct` type intended to represent a logger that writes to standard error, with no members or behavior defined in the provided source. [crates/gwiki/src/main.rs:425]
- `StderrLogger` (class) component `StderrLogger [class]` (`c1eb4d4c-149b-5f8f-aa20-9e8fa2053431`) lines 429-441 [crates/gwiki/src/main.rs:429-441]
  - Signature: `impl log::Log for StderrLogger {`
  - Purpose: `StderrLogger` is a `log::Log` implementation that accepts records at or below `log::max_level()` and emits them to standard error as `gwiki: <level>: <message>`, with `flush()` as a no-op. [crates/gwiki/src/main.rs:429-441]
- `StderrLogger.enabled` (method) component `StderrLogger.enabled [method]` (`59651516-9e4a-5652-9761-10d06b461186`) lines 430-432 [crates/gwiki/src/main.rs:430-432]
  - Signature: `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {`
  - Purpose: It returns `true` only when the record’s `log::Level` is less than or equal to the current global `log::max_level()`, effectively filtering out messages above the configured maximum verbosity. [crates/gwiki/src/main.rs:430-432]
- `StderrLogger.log` (method) component `StderrLogger.log [method]` (`51afb49d-8dbd-5ea8-8042-7ffcc77fb5b7`) lines 434-438 [crates/gwiki/src/main.rs:434-438]
  - Signature: `fn log(&self, record: &log::Record<'_>) {`
  - Purpose: If `record.metadata()` is enabled, this method writes the log message to stderr as `gwiki: <level>: <args>` using `eprintln!`. [crates/gwiki/src/main.rs:434-438]
- `StderrLogger.flush` (method) component `StderrLogger.flush [method]` (`ddce8139-98ce-5e84-bf3c-c4b1343278f4`) lines 440-440 [crates/gwiki/src/main.rs:440]
  - Signature: `fn flush(&self) {}`
  - Purpose: `flush` is a no-op method that takes an immutable reference to `self` and immediately returns `()`, performing no output synchronization or buffered-state handling. [crates/gwiki/src/main.rs:440]
- `log_level` (function) component `log_level [function]` (`b336c7d1-2887-5a83-b1b4-be4e322649aa`) lines 443-450 [crates/gwiki/src/main.rs:443-450]
  - Signature: `fn log_level(quiet: bool, rust_log: Option<&str>) -> log::LevelFilter {`
  - Purpose: Returns `log::LevelFilter::Off` when `quiet` is true, otherwise trims and parses `rust_log` into a `LevelFilter` and falls back to `Off` if the option is `None` or parsing fails. [crates/gwiki/src/main.rs:443-450]
- `init_logger` (function) component `init_logger [function]` (`d07b2233-9e9d-55b0-8e5c-657e0caa08b8`) lines 452-456 [crates/gwiki/src/main.rs:452-456]
  - Signature: `fn init_logger(quiet: bool) {`
  - Purpose: `init_logger` installs `STDERR_LOGGER` as the global logger and sets the maximum log level using `quiet` plus the optional `RUST_LOG` environment variable. [crates/gwiki/src/main.rs:452-456]
- `main` (function) component `main [function]` (`4e6bfab9-2541-5ea8-9eea-b01450777fd4`) lines 458-510 [crates/gwiki/src/main.rs:458-510]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Parses and normalizes CLI arguments, initializes logging, optionally prints the CLI contract, otherwise converts the CLI into an internal command and runs `gobby_wiki::run`, emitting status/result output or formatted errors and returning the corresponding `ExitCode`. [crates/gwiki/src/main.rs:458-510]
- `normalize_project_flag_args` (function) component `normalize_project_flag_args [function]` (`21cd01db-0cc3-5730-b721-64d313de8582`) lines 517-536 [crates/gwiki/src/main.rs:517-536]
  - Signature: `fn normalize_project_flag_args<I, S>(args: I) -> Vec<OsString>`
  - Purpose: It copies the input arguments into a new `Vec<OsString>`, and whenever it sees `--project` immediately followed by a token recognized by `is_cli_subcommand`, it inserts an extra `"."` argument after `--project` to normalize the flag form. [crates/gwiki/src/main.rs:517-536]
- `is_cli_subcommand` (function) component `is_cli_subcommand [function]` (`1b3f3b67-4078-51a7-ab0a-caf617c6072f`) lines 538-540 [crates/gwiki/src/main.rs:538-540]
  - Signature: `fn is_cli_subcommand(value: &str) -> bool {`
  - Purpose: Returns `true` if `value` exactly matches one of the predefined entries in `CLI_SUBCOMMANDS`, and `false` otherwise. [crates/gwiki/src/main.rs:538-540]
- `print_error` (function) component `print_error [function]` (`5c5ea924-40fb-5e26-aab8-bd76d4acb6fe`) lines 542-556 [crates/gwiki/src/main.rs:542-556]
  - Signature: `fn print_error(format: output::Format, error: &WikiError) {`
  - Purpose: `print_error` writes a `WikiError` to stderr as either a JSON object containing its `code` and `message` when `format` is `Json` (falling back to `eprintln!` if JSON emission fails) or as a plain `gwiki: {error}` text line when `format` is `Text`. [crates/gwiki/src/main.rs:542-556]
- `command_from_cli` (function) component `command_from_cli [function]` (`1d30693b-1db3-5b50-a329-d0d8363808f5`) lines 558-709 [crates/gwiki/src/main.rs:558-709]
  - Signature: `fn command_from_cli(command: CliCommand, scope: ScopeSelection) -> Result<Command, WikiError> {`
  - Purpose: I’m checking the implementation so the summary is exact rather than inferred from the snippet alone.`gcode` is unavailable in this environment because it can’t reach the local hub, so I’m falling back to direct source search to verify the remaining branches.It converts a `CliCommand` and `ScopeSelection` into the corresponding runtime `Command`, threading `scope` through each variant, reconstructing variant-specific payloads such as `Setup`, `Refresh`, and `IngestFileOptions`, and rejecting invalid `RemoveSource` flag combinations while treating `Contract` as unreachable at dispatch time. [crates/gwiki/src/main.rs:558-709]
- `from` (function) component `from [function]` (`084fdec6-06f0-5c32-8f0c-a6141ac12070`) lines 712-718 [crates/gwiki/src/main.rs:712-718]
  - Signature: `fn from(kind: CompileKind) -> Self {`
  - Purpose: Converts a `CompileKind` into the corresponding `Self` enum variant by mapping `Source`, `Concept`, and `Topic` one-to-one. [crates/gwiki/src/main.rs:712-718]
- `from` (function) component `from [function]` (`ca1f196f-c32e-595e-b2ba-3f7b9ab9e962`) lines 722-732 [crates/gwiki/src/main.rs:722-732]
  - Signature: `fn from(args: ExportArgs) -> Self {`
  - Purpose: Converts `ExportArgs` into the corresponding `Self` variant by mapping `WorkflowAssets` to `Self::WorkflowAssets { filename: output }` and `Report` to `Self::ReportFile { filename: output, source_path: source }`. [crates/gwiki/src/main.rs:722-732]
- `from` (function) component `from [function]` (`0121443e-703d-50bc-951f-ad1105b0702f`) lines 736-743 [crates/gwiki/src/main.rs:736-743]
  - Signature: `fn from(args: ReviewReportArgs) -> Self {`
  - Purpose: Constructs a `Self` value by moving `files`, `symbols`, `diff_path`, and `output` directly from the provided `ReviewReportArgs`. [crates/gwiki/src/main.rs:736-743]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`20b9fb42-ed64-5b2d-b6b9-6d7eddb46fa8`) lines 746-756 [crates/gwiki/src/main.rs:746-756]
  - Signature: `impl From<ScopeArgs> for ScopeSelection {`
  - Purpose: `ScopeSelection` implements `From<ScopeArgs>` by constructing a topic selection if `scope.topic` is set, otherwise a project selection if `scope.project` is set, and otherwise falling back to automatic detection. [crates/gwiki/src/main.rs:746-756]
- `ScopeSelection.from` (method) component `ScopeSelection.from [method]` (`f3286122-5a03-533a-8764-e0d0672d9806`) lines 747-755 [crates/gwiki/src/main.rs:747-755]
  - Signature: `fn from(scope: ScopeArgs) -> Self {`
  - Purpose: It converts `ScopeArgs` into `Self` by preferring `Self::topic(topic)` when `scope.topic` is present, otherwise `Self::project(project_root)` when `scope.project` is present, and falling back to `Self::detect()` if neither field is set. [crates/gwiki/src/main.rs:747-755]
- `exit_code_for_error` (function) component `exit_code_for_error [function]` (`6d332b60-d38f-52f7-8a47-22fea45d28ac`) lines 758-775 [crates/gwiki/src/main.rs:758-775]
  - Signature: `fn exit_code_for_error(error: &WikiError) -> ExitCode {`
  - Purpose: `exit_code_for_error` maps `WikiError` variants to process exit codes, returning `ExitCode::from(2)` for `NotImplemented`, `InvalidInput`, `Index`, `Search`, `InvalidScope`, and `NotFound`, and `ExitCode::from(1)` for `Config`, `Io`, `Json`, `Yaml`, `Registry`, `Daemon`, `Timeout`, and `Setup`. [crates/gwiki/src/main.rs:758-775]
- `from` (function) component `from [function]` (`27ce3536-51b4-5744-8fef-761d34bb2eb6`) lines 778-794 [crates/gwiki/src/main.rs:778-794]
  - Signature: `fn from(args: SetupArgs) -> Self {`
  - Purpose: It constructs `Self` by directly moving each corresponding configuration field from `SetupArgs` into the new instance without any transformation or validation. [crates/gwiki/src/main.rs:778-794]

