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
  - 417-468
  - 470-489
  - 491-493
  - 495-509
  - 511-662
  - 665-671
  - 675-685
  - 689-696
  - 699-709
  - 700-708
  - 711-728
  - 731-747
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/main.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/main.rs` exposes 31 indexed API symbols.
[crates/gwiki/src/main.rs:46-60]
[crates/gwiki/src/main.rs:63-149]
[crates/gwiki/src/main.rs:152-167]
[crates/gwiki/src/main.rs:170-212]
[crates/gwiki/src/main.rs:215-225]
[crates/gwiki/src/main.rs:228-243]
[crates/gwiki/src/main.rs:246-254]
[crates/gwiki/src/main.rs:256-267]
[crates/gwiki/src/main.rs:270-285]
[crates/gwiki/src/main.rs:288-296]
[crates/gwiki/src/main.rs:304-312]
[crates/gwiki/src/main.rs:315-318]
[crates/gwiki/src/main.rs:321-324]
[crates/gwiki/src/main.rs:327-351]
[crates/gwiki/src/main.rs:354-369]
[crates/gwiki/src/main.rs:372-375]
[crates/gwiki/src/main.rs:378-391]
[crates/gwiki/src/main.rs:394-408]
[crates/gwiki/src/main.rs:411-415]
[crates/gwiki/src/main.rs:417-468]
[crates/gwiki/src/main.rs:470-489]
[crates/gwiki/src/main.rs:491-493]
[crates/gwiki/src/main.rs:495-509]
[crates/gwiki/src/main.rs:511-662]
[crates/gwiki/src/main.rs:665-671]
[crates/gwiki/src/main.rs:675-685]
[crates/gwiki/src/main.rs:689-696]
[crates/gwiki/src/main.rs:699-709]
[crates/gwiki/src/main.rs:700-708]
[crates/gwiki/src/main.rs:711-728]
[crates/gwiki/src/main.rs:731-747]

## API Symbols

- `Cli` (class) component `Cli [class]` (`86726852-c29c-5e14-9fee-c96524fac045`) lines 46-60 [crates/gwiki/src/main.rs:46-60]
  - Signature: `struct Cli {`
  - Purpose: A CLI argument struct (using clap macros) that flattens scope arguments and aggregates global output format and quiet-mode flags with a subcommand dispatcher. [crates/gwiki/src/main.rs:46-60]
- `CliCommand` (type) component `CliCommand [type]` (`2d1d3783-7c05-5ec3-88cb-2ef1e61ba34e`) lines 63-149 [crates/gwiki/src/main.rs:63-149]
  - Signature: `enum CliCommand {`
  - Purpose: Indexed type `CliCommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:63-149]
- `ScopeArgs` (class) component `ScopeArgs [class]` (`0041e70b-7127-5b3c-844e-87b1eff8f202`) lines 152-167 [crates/gwiki/src/main.rs:152-167]
  - Signature: `struct ScopeArgs {`
  - Purpose: `ScopeArgs` is a CLI argument struct that provides mutually-exclusive global flags `--project` and `--topic` for selecting a wiki scope by either a project directory path or a named topic. [crates/gwiki/src/main.rs:152-167]
- `SetupArgs` (class) component `SetupArgs [class]` (`cba31c93-694c-52b9-9c54-dac8833582fb`) lines 170-212 [crates/gwiki/src/main.rs:170-212]
  - Signature: `struct SetupArgs {`
  - Purpose: SetupArgs is a command-line argument struct that defines optional configuration parameters for initializing the Gobby hub, including PostgreSQL connectivity, FalkorDB graph database, Qdrant vector store, and embedding service settings. [crates/gwiki/src/main.rs:170-212]
- `SearchArgs` (class) component `SearchArgs [class]` (`b838b613-d550-5bae-b339-3f3dfc9b6b6e`) lines 215-225 [crates/gwiki/src/main.rs:215-225]
  - Signature: `struct SearchArgs {`
  - Purpose: `SearchArgs` is a command-line argument struct that captures a required search query string, a configurable result limit (defaulting to 10), and an optional boolean flag to disable semantic vector search. [crates/gwiki/src/main.rs:215-225]
- `AskArgs` (class) component `AskArgs [class]` (`7fdc4c76-6859-5620-bfc0-000e08a203c9`) lines 228-243 [crates/gwiki/src/main.rs:228-243]
  - Signature: `struct AskArgs {`
  - Purpose: `AskArgs` is a command-line argument struct that accepts a question and optionally synthesizes answers from wiki retrieval using LLM with configurable AI routing modes and mandatory success enforcement. [crates/gwiki/src/main.rs:228-243]
- `BenchmarkArgs` (class) component `BenchmarkArgs [class]` (`7ed6ada6-e9c2-55cd-b19f-c6f86a7f2aec`) lines 246-254 [crates/gwiki/src/main.rs:246-254]
  - Signature: `struct BenchmarkArgs {`
  - Purpose: BenchmarkArgs is a struct containing a CLI-parsed, positively-validated `usize` parameter that specifies the count of seeded retrieval precision probes to execute during benchmarking. [crates/gwiki/src/main.rs:246-254]
- `parse_positive_usize` (function) component `parse_positive_usize [function]` (`5deeca42-eb60-5d2b-a630-24147c60d4ae`) lines 256-267 [crates/gwiki/src/main.rs:256-267]
  - Signature: `fn parse_positive_usize(value: &str) -> Result<usize, String> {`
  - Purpose: Parses a string into a `usize` and returns the value only if it is strictly positive (greater than zero), otherwise returns a string error. [crates/gwiki/src/main.rs:256-267]
- `RemoveSourceArgs` (class) component `RemoveSourceArgs [class]` (`8c605949-9ed9-5f9c-82d5-85b11af2242e`) lines 270-285 [crates/gwiki/src/main.rs:270-285]
  - Signature: `struct RemoveSourceArgs {`
  - Purpose: RemoveSourceArgs defines CLI arguments for removing a vault source by ID, with options for dry-run preview, destructive operation confirmation, and raw asset preservation. [crates/gwiki/src/main.rs:270-285]
- `RefreshArgs` (class) component `RefreshArgs [class]` (`eb9e3055-9055-55aa-b7c0-4e4bce26bf1d`) lines 288-296 [crates/gwiki/src/main.rs:288-296]
  - Signature: `struct RefreshArgs {`
  - Purpose: `RefreshArgs` is a command-line argument struct that accepts one or more source IDs to refresh and includes a dry-run flag to preview refresh candidates without performing fetch, write, delete, or indexing operations. [crates/gwiki/src/main.rs:288-296]
- `ReadArgs` (class) component `ReadArgs [class]` (`b93d9fb0-06f1-5256-a433-035bb3f32225`) lines 304-312 [crates/gwiki/src/main.rs:304-312]
  - Signature: `struct ReadArgs {`
  - Purpose: ReadArgs is a clap-derived struct that parses optional command-line arguments for specifying a vault-relative wiki path and heading title to resolve content within a given scope. [crates/gwiki/src/main.rs:304-312]
- `BacklinksArgs` (class) component `BacklinksArgs [class]` (`f2f6a1a6-bb27-5d3d-bc5f-2f7e62394be5`) lines 315-318 [crates/gwiki/src/main.rs:315-318]
  - Signature: `struct BacklinksArgs {`
  - Purpose: `BacklinksArgs` is a command-line argument struct containing a single required `page` parameter of type `String` for specifying the target page in a backlinks operation. [crates/gwiki/src/main.rs:315-318]
- `LinkSuggestArgs` (class) component `LinkSuggestArgs [class]` (`8b9603aa-862a-5f96-84b6-578c054b0544`) lines 321-324 [crates/gwiki/src/main.rs:321-324]
  - Signature: `struct LinkSuggestArgs {`
  - Purpose: `LinkSuggestArgs` is a command-line argument struct that exposes a `--limit` flag of type `usize` with a default value of 10. [crates/gwiki/src/main.rs:321-324]
- `ResearchArgs` (class) component `ResearchArgs [class]` (`82cbced1-8e6b-5c0f-903b-e7714c662870`) lines 327-351 [crates/gwiki/src/main.rs:327-351]
  - Signature: `struct ResearchArgs {`
  - Purpose: A CLI argument struct that configures research operations with an optional question input, source constraints, resource limits (steps, tokens, sources), AI routing strategy, and audit mode. [crates/gwiki/src/main.rs:327-351]
- `CompileArgs` (class) component `CompileArgs [class]` (`681e096e-f7e8-559a-a165-5c3eb9277d72`) lines 354-369 [crates/gwiki/src/main.rs:354-369]
  - Signature: `struct CompileArgs {`
  - Purpose: `CompileArgs` is a CLI argument structure that accepts an optional topic, multiple outline headings, a compile-kind enumeration (defaulting to "topic"), an optional target path, and a write-intent flag. [crates/gwiki/src/main.rs:354-369]
- `ExportArgs` (class) component `ExportArgs [class]` (`b32f0410-7cc6-5a63-88ab-d8a207f94991`) lines 372-375 [crates/gwiki/src/main.rs:372-375]
  - Signature: `struct ExportArgs {`
  - Purpose: ExportArgs is a clap-derive argument struct that encapsulates an ExportSubcommand subcommand for routing command-line input to specific export variants. [crates/gwiki/src/main.rs:372-375]
- `ReviewReportArgs` (class) component `ReviewReportArgs [class]` (`c543bbfa-65f8-5994-b916-7fad331d87d1`) lines 378-391 [crates/gwiki/src/main.rs:378-391]
  - Signature: `struct ReviewReportArgs {`
  - Purpose: ReviewReportArgs is a clap-derived Rust struct that defines command-line arguments accepting multiple source files and symbols, an optional diff file path, and a configurable output file destination (defaulting to "review-report.md"). [crates/gwiki/src/main.rs:378-391]
- `ExportSubcommand` (type) component `ExportSubcommand [type]` (`dfd94326-d3f7-54f4-9df3-8689dd6496f4`) lines 394-408 [crates/gwiki/src/main.rs:394-408]
  - Signature: `enum ExportSubcommand {`
  - Purpose: Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:394-408]
- `CompileKind` (type) component `CompileKind [type]` (`88d13355-ab0d-5ff9-b1a3-2745892cf99e`) lines 411-415 [crates/gwiki/src/main.rs:411-415]
  - Signature: `enum CompileKind {`
  - Purpose: Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:411-415]
- `main` (function) component `main [function]` (`03d39e8d-1954-5ff7-a47e-11f43294b1cb`) lines 417-468 [crates/gwiki/src/main.rs:417-468]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Parses CLI arguments and either outputs the CLI contract or executes a scoped gwiki command via `gobby_wiki::run()`, printing formatted results and status messages with appropriate exit codes. [crates/gwiki/src/main.rs:417-468]
- `normalize_project_flag_args` (function) component `normalize_project_flag_args [function]` (`8e480012-b58a-53b7-a18b-b9c90b18a476`) lines 470-489 [crates/gwiki/src/main.rs:470-489]
  - Signature: `fn normalize_project_flag_args<I, S>(args: I) -> Vec<OsString>`
  - Purpose: Normalizes command-line arguments by inserting "." as an implicit project value when a `--project` flag is immediately followed by a CLI subcommand. [crates/gwiki/src/main.rs:470-489]
- `is_cli_subcommand` (function) component `is_cli_subcommand [function]` (`a31ac4b7-e9d7-50d7-8392-30bbf5800553`) lines 491-493 [crates/gwiki/src/main.rs:491-493]
  - Signature: `fn is_cli_subcommand(value: &str) -> bool {`
  - Purpose: Returns a boolean indicating whether the input string is contained in the `CLI_SUBCOMMANDS` collection. [crates/gwiki/src/main.rs:491-493]
- `print_error` (function) component `print_error [function]` (`301512ac-b87d-585e-9034-5a567eaba9eb`) lines 495-509 [crates/gwiki/src/main.rs:495-509]
  - Signature: `fn print_error(format: output::Format, error: &WikiError) {`
  - Purpose: Prints a WikiError to stderr in JSON format (with code and message fields) or plaintext, based on the specified output format, with JSON output falling back to plaintext on serialization failure. [crates/gwiki/src/main.rs:495-509]
- `command_from_cli` (function) component `command_from_cli [function]` (`b92c3785-cd74-5985-885c-8c06a0583406`) lines 511-662 [crates/gwiki/src/main.rs:511-662]
  - Signature: `fn command_from_cli(command: CliCommand, scope: ScopeSelection) -> Result<Command, WikiError> {`
  - Purpose: Transforms CLI commands into internal Command variants through pattern matching, argument processing, and flag validation, returning a Result that either succeeds with the transformed command or fails with a WikiError. [crates/gwiki/src/main.rs:511-662]
- `from` (function) component `from [function]` (`59c4af52-4e42-5785-b87e-6a37ab0fc1e1`) lines 665-671 [crates/gwiki/src/main.rs:665-671]
  - Signature: `fn from(kind: CompileKind) -> Self {`
  - Purpose: This function implements the `From` trait to convert a `CompileKind` enum variant to an identically-named variant of the target type via exhaustive pattern matching. [crates/gwiki/src/main.rs:665-671]
- `from` (function) component `from [function]` (`ad05dcc5-3068-57b6-b1f1-701b770f9d1f`) lines 675-685 [crates/gwiki/src/main.rs:675-685]
  - Signature: `fn from(args: ExportArgs) -> Self {`
  - Purpose: Converts `ExportArgs` into `Self` via pattern matching on `ExportSubcommand` variants, remapping output and source fields to corresponding target enum variants with renamed fields. [crates/gwiki/src/main.rs:675-685]
- `from` (function) component `from [function]` (`038ce78b-d074-50de-9c4f-7ee1f7551832`) lines 689-696 [crates/gwiki/src/main.rs:689-696]
  - Signature: `fn from(args: ReviewReportArgs) -> Self {`
  - Purpose: This function implements the `From` trait to convert a `ReviewReportArgs` into `Self` by directly mapping its four fields (`files`, `symbols`, `diff_path`, `output`). [crates/gwiki/src/main.rs:689-696]
- `ScopeSelection` (class) component `ScopeSelection [class]` (`87510eca-d123-5085-a489-08188e9d6864`) lines 699-709 [crates/gwiki/src/main.rs:699-709]
  - Signature: `impl From<ScopeArgs> for ScopeSelection {`
  - Purpose: Converts `ScopeArgs` into a `ScopeSelection` via a prioritized fallback chain: explicit topic selection, explicit project root selection, or automatic detection. [crates/gwiki/src/main.rs:699-709]
- `ScopeSelection.from` (method) component `ScopeSelection.from [method]` (`93de8162-545c-5eb2-ab70-f0011ede2931`) lines 700-708 [crates/gwiki/src/main.rs:700-708]
  - Signature: `fn from(scope: ScopeArgs) -> Self {`
  - Purpose: This method constructs a `Self` instance from `ScopeArgs` by prioritizing an explicit topic, falling back to a project root, and finally attempting automatic detection. [crates/gwiki/src/main.rs:700-708]
- `exit_code_for_error` (function) component `exit_code_for_error [function]` (`f0a85793-6d59-5a48-860e-3d7316af3d97`) lines 711-728 [crates/gwiki/src/main.rs:711-728]
  - Signature: `fn exit_code_for_error(error: &WikiError) -> ExitCode {`
  - Purpose: Maps `WikiError` variants to exit codes, returning 2 for input/search/logic errors and 1 for system/configuration/I/O errors. [crates/gwiki/src/main.rs:711-728]
- `from` (function) component `from [function]` (`98832f55-068a-5a0f-af58-117542339956`) lines 731-747 [crates/gwiki/src/main.rs:731-747]
  - Signature: `fn from(args: SetupArgs) -> Self {`
  - Purpose: Implements the `From` trait to construct `Self` from a `SetupArgs` struct via direct field mapping. [crates/gwiki/src/main.rs:731-747]

