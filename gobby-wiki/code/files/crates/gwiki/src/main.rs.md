---
title: crates/gwiki/src/main.rs
type: code_file
provenance:
- file: crates/gwiki/src/main.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/main.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/main.rs` exposes 39 indexed API symbols.

## How it fits

`crates/gwiki/src/main.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `Cli` | class | 'Cli' is the top-level command-line argument struct that flattens shared scope options, exposes global '--format' and '--quiet' flags, and dispatches to a required subcommand via 'command'. [crates/gwiki/src/main.rs:48-62] |
| `CliCommand` | type | Indexed type `CliCommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:65-153] |
| `ScopeArgs` | class | 'ScopeArgs' is a CLI argument struct that defines two mutually exclusive global scope selectors for Gobby wiki operations: '--project' optionally takes a project root path and defaults to the current directory when passed without a value, while '--topic' selects a named topic scope. [crates/gwiki/src/main.rs:156-171] |
| `NormalizeArgs` | class | 'NormalizeArgs' is a CLI argument struct containing a '--check' boolean flag that enables reporting which authored documents need normalization without modifying them. [crates/gwiki/src/main.rs:174-178] |
| `SetupArgs` | class | 'SetupArgs' is a CLI argument struct that configures Gobby/gwiki setup behavior, including standalone and service-provisioning flags, PostgreSQL and vector-store connection settings, and optional embedding provider/API/model parameters. [crates/gwiki/src/main.rs:181-223] |
| `SearchArgs` | class | 'SearchArgs' is a CLI argument struct for a search command that accepts a required 'query' string, an optional '--limit' 'usize' defaulting to '10', and a '--no-semantic' flag to disable semantic vector search for that query. [crates/gwiki/src/main.rs:226-236] |
| `AskArgs` | class | 'AskArgs' is a CLI argument struct that captures the required 'question' string plus flags controlling wiki-hit answer synthesis ('--llm'), AI routing override ('--ai' with 'auto\|daemon\|direct\|off'), and hard-failure behavior when no AI route succeeds ('--require-ai'). [crates/gwiki/src/main.rs:239-254] |
| `SyncSessionsArgs` | class | 'SyncSessionsArgs' is a CLI argument struct that optionally specifies the path to a directory of archived '*.jsonl.gz' session transcripts and an optional positive upper bound on how many archives to process. [crates/gwiki/src/main.rs:257-265] |
| `BenchmarkArgs` | class | 'BenchmarkArgs' is a command-line argument struct that defines a single 'retrieval_candidates: usize' option, parsed as a positive integer and defaulting to 'BenchmarkOptions::DEFAULT_RETRIEVAL_CANDIDATES', for configuring seeded retrieval precision probes. [crates/gwiki/src/main.rs:268-276] |
| `parse_positive_usize` | function | Parses 'value' as a 'usize' and returns it only if it is strictly greater than zero, otherwise converting the parse error or a zero value into a 'String' error. [crates/gwiki/src/main.rs:278-289] |
| `RemoveSourceArgs` | class | 'RemoveSourceArgs' is a CLI argument struct for removing a source by 'id', with flags to enable a non-mutating 'dry_run', bypass confirmation via 'yes', and preserve the referenced raw asset via 'keep_asset'. [crates/gwiki/src/main.rs:292-307] |
| `RefreshArgs` | class | 'RefreshArgs' is a CLI argument struct that collects zero or more source IDs to refresh via repeated '--id SOURCE_ID' flags and an optional '--dry-run' flag to preview refresh candidates without performing fetch, write, delete, or index operations. [crates/gwiki/src/main.rs:310-318] |
| `ReadArgs` | class | 'ReadArgs' is a CLI argument struct containing two optional flags, 'path: Option<PathBuf>' for selecting a vault-relative wiki path to read and 'title: Option<String>' for resolving a first-heading title within that selected scope. [crates/gwiki/src/main.rs:326-334] |
| `BacklinksArgs` | class | 'BacklinksArgs' is a command-line argument struct containing a single required 'page' field of type 'String', accepted as a positional value named 'PAGE'. [crates/gwiki/src/main.rs:337-340] |
| `LinkSuggestArgs` | class | 'LinkSuggestArgs' is a CLI argument struct that defines a single '--limit' option of type 'usize', defaulting to '10', to cap the number of suggestions returned. [crates/gwiki/src/main.rs:343-346] |
| `CompileArgs` | class | 'CompileArgs' is a clap-parsed argument struct for a compile command that optionally accepts a topic positional, multiple outline and source values, a 'CompileKind' selector defaulting to 'topic', an optional target page path, a 'write-intent' flag, and an AI routing mode defaulting to 'auto'. [crates/gwiki/src/main.rs:349-374] |
| `ExportArgs` | class | 'ExportArgs' is a Rust CLI argument struct that contains a single 'command' field of type 'ExportSubcommand', declared as the program’s subcommand selector via '#[command(subcommand)]'. [crates/gwiki/src/main.rs:377-380] |
| `ReviewReportArgs` | class | 'ReviewReportArgs' is a CLI argument struct that collects repeated '--file' and '--symbol' identifiers, an optional '--diff' path, and an '--output' filename defaulting to 'review-report.md' for generating a review report. [crates/gwiki/src/main.rs:383-396] |
| `ExportSubcommand` | type | Indexed type `ExportSubcommand` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:399-413] |
| `CompileKind` | type | Indexed type `CompileKind` in `crates/gwiki/src/main.rs`. [crates/gwiki/src/main.rs:416-420] |
| `StderrLogger` | class | 'StderrLogger' is a zero-sized struct type that serves as a stderr-backed logger implementation. [crates/gwiki/src/main.rs:427] |
| `StderrLogger::enabled` | method | Returns 'true' when the log record’s level is less than or equal to the current global maximum log level, and 'false' otherwise. [crates/gwiki/src/main.rs:432-434] |
| `StderrLogger::log` | method | Checks whether the record’s metadata is enabled and, if so, writes a formatted log line of the form 'gwiki: <level>: <message>' to standard error via 'eprintln!'. [crates/gwiki/src/main.rs:436-440] |
| `StderrLogger::flush` | method | 'flush' is a no-op method that takes an immutable reference to 'self' and performs no state changes or I/O. [crates/gwiki/src/main.rs:442] |
| `log_level` | function | Returns 'log::LevelFilter::Off' when 'quiet' is 'true', otherwise tries to parse the trimmed 'rust_log' string into a 'log::LevelFilter' and falls back to 'Off' if parsing fails or the option is 'None'. [crates/gwiki/src/main.rs:445-452] |
| `init_logger` | function | Initializes the global logger by reading 'RUST_LOG', installing 'STDERR_LOGGER', and setting the maximum log level based on 'quiet' and the environment variable. [crates/gwiki/src/main.rs:454-458] |
| `reset_sigpipe` | function | Resets the process’s 'SIGPIPE' disposition to the default handler by calling 'libc::signal(SIGPIPE, SIG_DFL)' inside an unsafe block. [crates/gwiki/src/main.rs:467-473] |
| `reset_sigpipe` | function | Resets the process's SIGPIPE handling to the default disposition. [crates/gwiki/src/main.rs:476] |
| `main` | function | Parses CLI arguments, initializes logging and SIGPIPE handling, optionally emits the GWiki contract, otherwise converts the CLI into a runtime command, executes 'gobby_wiki::run', prints any status/result output in the requested format, and maps successes or errors to an appropriate 'ExitCode'. [crates/gwiki/src/main.rs:478-531] |
| `normalize_project_flag_args` | function | Clones the input arguments into a new 'Vec<OsString>', and whenever it encounters '--project' immediately followed by a string recognized as a CLI subcommand, it inserts an extra '.' argument after '--project' to normalize the flag form. [crates/gwiki/src/main.rs:538-557] |
| `is_cli_subcommand` | function | Returns 'true' if 'value' is contained in the 'CLI_SUBCOMMANDS' list, and 'false' otherwise. [crates/gwiki/src/main.rs:559-561] |
| `print_error` | function | Prints a 'WikiError' to standard error as either JSON '{"code", "message"}' via 'output::print_json' with 'eprintln!' fallback on failure, or as plain text prefixed with 'gwiki:'. [crates/gwiki/src/main.rs:563-577] |
| `command_from_cli` | function | 'command_from_cli' converts a parsed 'CliCommand' plus 'ScopeSelection' into the corresponding typed 'Command' variant, constructing per-command option structs and rejecting invalid 'remove-source' flag combinations such as '--dry-run' with '--yes'. [crates/gwiki/src/main.rs:579-718] |
| `from` | function | Converts a 'CompileKind' into the corresponding 'Self' variant by matching 'Source', 'Concept', and 'Topic' one-to-one. [crates/gwiki/src/main.rs:721-727] |
| `from` | function | Converts an 'ExportArgs' into the corresponding 'Self' variant by mapping 'WorkflowAssets { output }' to 'Self::WorkflowAssets { filename: output }' and 'Report { output, source }' to 'Self::ReportFile { filename: output, source_path: source }'. [crates/gwiki/src/main.rs:731-741] |
| `from` | function | Constructs a 'Self' by moving 'files', 'symbols', 'diff_path', and 'output' directly from 'ReviewReportArgs' into the corresponding fields. [crates/gwiki/src/main.rs:745-752] |
| `ScopeSelection::from` | method | Constructs a 'Self' by dispatching to 'Self::topic(scope.topic)' if 'scope.topic' is set, else 'Self::project(scope.project)' if 'scope.project' is set, otherwise falling back to 'Self::detect()'. [crates/gwiki/src/main.rs:756-764] |
| `exit_code_for_error` | function | Maps a 'WikiError' variant to a process 'ExitCode', returning '2' for user/input/search/not-found-related errors and '1' for configuration, I/O, parsing, registry, daemon, timeout, and setup errors. [crates/gwiki/src/main.rs:767-784] |
| `from` | function | Constructs a 'Self' instance by directly copying each configuration field from 'SetupArgs' into the corresponding struct field. [crates/gwiki/src/main.rs:787-803] |

