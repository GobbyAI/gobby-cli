# Guides

Task-focused documentation for the released gobby-cli crates.

## Users

- [gcode User Guide](./gcode-user-guide.md) - search, symbols, dependency graphs, and project management.
- [gcode Codewiki Guide](./codewiki.md) - generated codebase docs, degraded graph output, and gwiki ingest.
- [gsqz User Guide](./gsqz-user-guide.md) - output compression pipelines and configuration.
- [gloc User Guide](./gloc-user-guide.md) - local LLM backend detection and client launch.
- [ghook User Guide](./ghook-user-guide.md) - hook dispatch, inbox replay, diagnostics, and troubleshooting.
- [AI Configuration](./ai-configuration.md) - capability/backend routing matrix, mixed routing, `--no-ai`, and local model budget.

## Maintainers

- [Release Guide](./release-guide.md) - release versions, tag order, and local binary installation.
- [gcode Development Guide](./gcode-development-guide.md) - code-index internals.
- [gcode Graph Core Migration Contract](./gcode-graph-core.md) - daemon transition contract.
- [AI Daemon Capability Contract](./ai-daemon-contract.md) - CLI-consumed daemon AI routes, probes, routing, and embedding namespace migration.
- [Hub Install Contract](./hub-install-contract.md) - standalone hub adoption and additive upgrade requirements.
- [gobby-core Development Guide](./gcore-development-guide.md) - shared foundation crate internals.
- [gsqz Development Guide](./gsqz-development-guide.md) - compressor implementation details.
- [gloc Development Guide](./gloc-development-guide.md) - local-launcher implementation details.
- [ghook Development Guide](./ghook-development-guide.md) - hook-dispatch implementation details.
- [gwiki Development Guide](./gwiki-development-guide.md) - unreleased wiki CLI internals.

`gobby-wiki` is documented for development only. It is not part of the current
published release set.

_Last verified: 2026-06-01_
