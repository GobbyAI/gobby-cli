# Task 306 TDD Evidence

Task: #306 Implement compile to wiki articles

## Original Compile Acceptance Cycle

Red phase, before compile implementation:

```bash
cargo test -p gobby-wiki --no-default-features compile::tests::compile_writes_obsidian_markdown
```

Result: failed with exit code `101`. Captured failures included missing
`SynthesizedPage`, `compile_to_wiki`, `render_source_citations`, `WritePolicy`,
and `write_synthesized_page`.

Green and final checks after implementation:

```bash
cargo test -p gobby-wiki --no-default-features compile::tests::compile_writes_obsidian_markdown
cargo test -p gobby-wiki --no-default-features citations::tests::renders_source_citations
cargo test -p gobby-wiki --no-default-features synthesis::tests::existing_page_requires_merge_intent
cargo test -p gobby-wiki --no-default-features compile::tests::index_update_preserves_unrelated_entries
```

Each acceptance filter passed. Final hardening also passed:

```bash
cargo fmt -p gobby-wiki -- --check
cargo clippy -p gobby-wiki --no-default-features --all-targets -- -D warnings
```

## Shared-Scope Follow-Up Cycle

Root holistic QA reopened #306 because compile loaded research checkpoints
through a divergent scope path. Red phase:

```bash
cargo test -p gobby-wiki --no-default-features --test cli_smoke public_cli_smoke_uses_gwiki_modules -- --exact --nocapture
```

Result: failed with exit code `101`; stderr showed research checkpoint lookup
under `$HOME/wiki/topics/rust/.gwiki/research-session.json` instead of the
`GOBBY_WIKI_HUB/topics/rust` vault.

Green phase: the same command passed after research scope resolution delegated to
the shared resolver.

Final merged validation after coordinator conflict resolution:

```bash
cargo fmt -p gobby-wiki -- --check
cargo test -p gobby-wiki --no-default-features compile::tests::compile_writes_obsidian_markdown
cargo test -p gobby-wiki --no-default-features citations::tests::renders_source_citations
cargo test -p gobby-wiki --no-default-features synthesis::tests::existing_page_requires_merge_intent
cargo test -p gobby-wiki --no-default-features compile::tests::index_update_preserves_unrelated_entries
cargo test -p gobby-wiki --no-default-features --test cli_smoke public_cli_smoke_uses_gwiki_modules -- --exact
cargo test -p gobby-wiki --no-default-features --test cli_smoke public_cli_smoke_continues_research_compile_audit_in_topic_scope -- --exact
cargo clippy -p gobby-wiki --no-default-features --all-targets -- -D warnings
uv run gobby test-quality audit crates/gwiki/tests/cli_smoke.rs --baseline .gobby/test-quality-baseline.json --fail-on-new --min-severity high
```

All final commands passed; test-quality reported 0 issues.
