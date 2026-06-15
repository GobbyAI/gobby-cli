---
title: crates/gsqz/src/main.rs
type: code_file
provenance:
- file: crates/gsqz/src/main.rs
  ranges:
  - 25-48
  - 50-65
  - 67-139
  - 141-184
  - 186-276
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/main.rs

Module: [[code/modules/crates/gsqz/src|crates/gsqz/src]]

## Purpose

`main.rs` is the CLI entry point for `gsqz`, a tool that runs a command or reads stdin and compresses the resulting text for LLM use. `Cli` defines the top-level flags for config handling, stats, and subcommand dispatch; `parse_input_level` extracts a `--level` setting for stdin compression, defaulting to `Standard` when absent or invalid. `main` loads configuration, auto-initializes a default config file on first run, and routes execution to `run_input_mode` or `run_output_mode`, which either compress stdin directly or run a shell command, strip ANSI escape codes, and compress the cleaned output with optional config and daemon integration.
[crates/gsqz/src/main.rs:25-48]
[crates/gsqz/src/main.rs:50-65]
[crates/gsqz/src/main.rs:67-139]
[crates/gsqz/src/main.rs:141-184]
[crates/gsqz/src/main.rs:186-276]

## API Symbols

- `Cli` (class) component `Cli [class]` (`c7adc044-6efa-5afc-8862-690c339ee32c`) lines 25-48 [crates/gsqz/src/main.rs:25-48]
  - Signature: `struct Cli {`
  - Purpose: A command-line interface argument struct for a compression utility that accepts optional configuration management and statistics flags alongside a required subcommand for compression operations. [crates/gsqz/src/main.rs:25-48]
- `parse_input_level` (function) component `parse_input_level [function]` (`7cfcfe2a-4b46-532c-ac5f-3feba564bde7`) lines 50-65 [crates/gsqz/src/main.rs:50-65]
  - Signature: `fn parse_input_level(args: &[String]) -> primitives::prose::Level {`
  - Purpose: Parses a `--level` command-line argument into a `primitives::prose::Level`, defaulting to `Level::Standard` if absent or unparseable. [crates/gsqz/src/main.rs:50-65]
- `main` (function) component `main [function]` (`9eb0d9c5-2df1-5539-b212-9319fd97f9bb`) lines 67-139 [crates/gsqz/src/main.rs:67-139]
  - Signature: `fn main() {`
  - Purpose: Entry point that parses CLI arguments, auto-initializes global and project configuration files, and dispatches to subcommands. [crates/gsqz/src/main.rs:67-139]
- `run_input_mode` (function) component `run_input_mode [function]` (`d93d6c6c-b216-5905-8e4d-4f9a3637730c`) lines 141-184 [crates/gsqz/src/main.rs:141-184]
  - Signature: `fn run_input_mode(args: &[String], config: &Config, stats: bool) {`
  - Purpose: Compresses prose read from stdin at a specified level, optionally logs compression statistics, reports metrics to a configured daemon, and outputs the compressed result. [crates/gsqz/src/main.rs:141-184]
- `run_output_mode` (function) component `run_output_mode [function]` (`88896e39-f136-5069-b7d1-73b094ae2ee7`) lines 186-276 [crates/gsqz/src/main.rs:186-276]
  - Signature: `fn run_output_mode(cmd: &str, config: &Config, stats: bool) {`
  - Purpose: Executes a cross-platform shell command, sanitizes its output by stripping ANSI escape codes, and compresses the result using a configurable Compressor with optional daemon-fetched configuration overrides. [crates/gsqz/src/main.rs:186-276]

