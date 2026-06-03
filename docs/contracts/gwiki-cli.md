# gwiki CLI Contract

The machine-readable contract lives at `crates/gwiki/contract/gwiki.contract.json`.
`gwiki contract --format json` must emit the same contract version and contents.

## Version

`contract_version`: 1

Version 1 covers the daemon-consumed surface:

- `contract`
- `index`
- `search`
- `ask`
- `read`
- `refresh`
- `ingest-file`
- `ingest-url`
- `collect`
- `research`
- `compile`
- `audit`
- `health`
- `sources`
- `backlinks`
- `status`
- `remove-source`

## Scope

`gwiki` accepts `--project <ROOT>` and `--topic <NAME>`.

No scope flag means detect the project from the current working directory. Bare
`--project` means the current directory. `--scope` is not part of this contract.

Every scoped JSON result consumed by Gobby carries a resolved `scope` identity
with `kind` and `id`.

## AI Routing

AI route flags use `auto|daemon|direct|off`. `direct` means any
OpenAI-compatible endpoint, local or remote. There is no `local` route.

## Research

`gwiki research` is governed by the standalone research contract in
[`gwiki-research.md`](gwiki-research.md). That contract defines the replacement
reason-act loop, audit mode, provenance rules, budgets, and the boundary between
gwiki-owned wiki mutation and Gobby-owned daemon enhancement.

## Drift Checks

Both the CLI and daemon tests load this contract. New daemon-facing flags or JSON
keys should update this document, the JSON contract, and the corresponding drift
tests in the same change.
