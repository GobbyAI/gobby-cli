---
title: crates/gloc/src/main.rs
type: code_file
provenance:
- file: crates/gloc/src/main.rs
  ranges:
  - 16-52
  - 54-118
  - 120-130
  - 132-155
  - 157-202
  - 204-213
  - 215-223
  - 225-250
  - 252-255
  - 257-288
  - 294-301
  - 304-318
  - 321-327
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc/src/main.rs

Module: [[code/modules/crates/gloc/src|crates/gloc/src]]

## Purpose

This file is the `gloc` CLI entry point that parses command-line options, loads configuration, and orchestrates startup for an AI client launcher that auto-detects local LLM backends. `Cli` captures user overrides for client, backend, model, backend URL, config path, and control actions like `--init`, `--status`, and `--dump_config`, plus passthrough args for the client binary. `main` handles the early-exit commands first, loads config, optionally auto-writes a default config, then resolves the backend, client, and model before either printing status or validating that the model is ready and continuing into execution. The helper functions keep that flow modular: `auto_export_config` seeds a default config in the user gobby home, `handle_init` initializes a project-local `.gobby/gloc.yaml`, `resolve_backend` and `resolve_client` select concrete config entries with error handling and URL overrides, `resolve_model` canonicalizes model aliases, and `print_status` reports the resolved runtime state. The remaining helpers build backend configs and verify URL-override behavior.
[crates/gloc/src/main.rs:16-52]
[crates/gloc/src/main.rs:54-118]
[crates/gloc/src/main.rs:120-130]
[crates/gloc/src/main.rs:132-155]
[crates/gloc/src/main.rs:157-202]

## API Symbols

- `Cli` (class) component `Cli [class]` (`4f9b85cf-7812-598e-a21b-5c1368511d2f`) lines 16-52 [crates/gloc/src/main.rs:16-52]
  - Signature: `struct Cli {`
  - Purpose: `Cli` is a `clap`-parsed command-line options struct that configures which AI client and backend to launch, optionally overrides model/URL/config resolution, supports `status`/`init`/`dump_config` control actions, and captures trailing passthrough arguments for the client binary. [crates/gloc/src/main.rs:16-52]
- `main` (function) component `main [function]` (`2679f7d7-f4bb-5c79-a06e-537fc750cf7c`) lines 54-118 [crates/gloc/src/main.rs:54-118]
  - Signature: `fn main() {`
  - Purpose: Parses CLI flags, handles `--init`/`--dump-config`/`--status` as early exits, loads and optionally auto-exports config, resolves the backend/client/model, enforces model readiness with fatal handling for missing/pull/network errors and a non-fatal warmup warning, then proceeds into the main execution path. [crates/gloc/src/main.rs:54-118]
- `auto_export_config` (function) component `auto_export_config [function]` (`54307264-6cff-5244-af17-1dbc2b3602dd`) lines 120-130 [crates/gloc/src/main.rs:120-130]
  - Signature: `fn auto_export_config() {`
  - Purpose: If `gobby_core::gobby_home()` resolves successfully, `auto_export_config` ensures `<gobby_home>/gloc.yaml` exists by creating the directory as needed and writing `config::DEFAULT_CONFIG_YAML` when the file is missing, emitting a stderr warning only if the write fails. [crates/gloc/src/main.rs:120-130]
- `handle_init` (function) component `handle_init [function]` (`35e60a15-0461-5842-8f99-d112b9e7f80e`) lines 132-155 [crates/gloc/src/main.rs:132-155]
  - Signature: `fn handle_init() {`
  - Purpose: `handle_init` verifies the current directory is a Gobby project by requiring `.gobby/`, backs up any existing `.gobby/gloc.yaml` to `.gobby/gloc.yaml.bak`, and then writes `config::DEFAULT_CONFIG_YAML` to `.gobby/gloc.yaml`, terminating the process on any failure. [crates/gloc/src/main.rs:132-155]
- `resolve_backend` (function) component `resolve_backend [function]` (`dfb631c4-7c31-59e2-b1f4-fc716efe1cbd`) lines 157-202 [crates/gloc/src/main.rs:157-202]
  - Signature: `fn resolve_backend(cli: &Cli, cfg: &Config) -> config::Backend {`
  - Purpose: `resolve_backend` returns the selected `config::Backend` by either looking up `cli.backend` in `cfg.backends` and applying an optional `--url` override with reachability validation, or by auto-detecting a backend from the overridden backend list, printing an error and exiting if the backend is unknown, unreachable, or none is detected. [crates/gloc/src/main.rs:157-202]
- `apply_backend_url_override` (function) component `apply_backend_url_override [function]` (`80170efa-b391-5bfd-bcc2-c818c6b3ec61`) lines 204-213 [crates/gloc/src/main.rs:204-213]
  - Signature: `fn apply_backend_url_override(`
  - Purpose: Returns a cloned `config::Backend` with its `url` field replaced by `url_override` when `Some`, otherwise returns an unchanged clone of the input backend. [crates/gloc/src/main.rs:204-213]
- `backends_with_url_override` (function) component `backends_with_url_override [function]` (`67b18f9c-15b3-57c4-bd48-1761a0e4b1b9`) lines 215-223 [crates/gloc/src/main.rs:215-223]
  - Signature: `fn backends_with_url_override(`
  - Purpose: Returns a new `Vec<config::Backend>` by iterating over `backends` and applying `apply_backend_url_override` to each backend with the provided optional `url_override`. [crates/gloc/src/main.rs:215-223]
- `resolve_client` (function) component `resolve_client [function]` (`65a042fe-e2ee-5878-9e01-26b1c2f0a546`) lines 225-250 [crates/gloc/src/main.rs:225-250]
  - Signature: `fn resolve_client(cli: &Cli, cfg: &Config) -> (String, config::Client) {`
  - Purpose: `resolve_client` returns the CLI-specified client name and cloned `config::Client` if `cli.client` is set and found in `cfg.clients`, otherwise it falls back to the first configured client, terminating the process with an error if the named client is unknown or no clients are configured. [crates/gloc/src/main.rs:225-250]
- `resolve_model` (function) component `resolve_model [function]` (`a3d5db2c-8890-5b16-90da-6767d68c5e42`) lines 252-255 [crates/gloc/src/main.rs:252-255]
  - Signature: `fn resolve_model(cli: &Cli, client: &config::Client, cfg: &Config) -> String {`
  - Purpose: `resolve_model` returns the CLI-specified model name if present, otherwise `client.default_model`, and then canonicalizes that value through `cfg.resolve_alias` before returning it as a `String`. [crates/gloc/src/main.rs:252-255]
- `print_status` (function) component `print_status [function]` (`c6062f0e-c3d4-5982-80a3-b19a5c29b2f9`) lines 257-288 [crates/gloc/src/main.rs:257-288]
  - Signature: `fn print_status(`
  - Purpose: `print_status` emits a stderr diagnostic summary of the selected backend, client, resolved client binary path or PATH miss, model, generated environment variables, and any constructed CLI arguments. [crates/gloc/src/main.rs:257-288]
- `backend` (function) component `backend [function]` (`e9d0901f-58ab-5fda-bd04-0ef6e6da1942`) lines 294-301 [crates/gloc/src/main.rs:294-301]
  - Signature: `fn backend(name: &str, url: &str, probe: &str) -> config::Backend {`
  - Purpose: Constructs and returns a `config::Backend` by copying `name`, `url`, and `probe` into the corresponding fields and initializing `auth_token` to an empty string. [crates/gloc/src/main.rs:294-301]
- `backend_candidates_apply_url_override_before_probe` (function) component `backend_candidates_apply_url_override_before_probe [function]` (`dae1b910-0dee-53fc-a051-bac36191b44b`) lines 304-318 [crates/gloc/src/main.rs:304-318]
  - Signature: `fn backend_candidates_apply_url_override_before_probe() {`
  - Purpose: It verifies that `backends_with_url_override` replaces each backend candidate’s base URL with the provided override while preserving the original probe path and candidate order. [crates/gloc/src/main.rs:304-318]
- `backend_candidates_keep_config_urls_without_override` (function) component `backend_candidates_keep_config_urls_without_override [function]` (`6f5b1fba-b61a-5d91-868f-c5bda190e3f3`) lines 321-327 [crates/gloc/src/main.rs:321-327]
  - Signature: `fn backend_candidates_keep_config_urls_without_override() {`
  - Purpose: It verifies that `backends_with_url_override` returns the original backend list unchanged when no URL override is provided, preserving the configured backend URL and path. [crates/gloc/src/main.rs:321-327]

