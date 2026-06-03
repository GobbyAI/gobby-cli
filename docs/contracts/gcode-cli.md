# gcode CLI Contract

The machine-readable contract lives at `crates/gcode/contract/gcode.contract.json`.
`gcode contract --format json` must emit the same contract version and contents.

## Version

`contract_version`: 1

Version 1 covers the daemon-consumed surface:

- `contract`
- `index`
- `search`
- `search-symbol`
- `codewiki`

## Scope

`--project <ROOT>` selects a project root. Without `--project`, gcode detects the
project from the current working directory. JSON output consumed by Gobby must
identify the resolved project with `project_id` and, where path context matters,
`project_root`.

## Format

Use `--format json` for daemon calls. Text output is for humans and is not a
stable integration surface.

## Drift Checks

Both the CLI and daemon tests load this contract. New daemon-facing flags or JSON
keys should update this document, the JSON contract, and the corresponding drift
tests in the same change.
