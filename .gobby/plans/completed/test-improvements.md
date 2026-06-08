# Rust Testing: Skill Guidance + gobby-cli Tooling

## Context

The ask was advice: "research Rust testing best practices, compare to our Rust skill,
Python testing just seems more robust." After comparing the **Rust skill** (in the sibling
`gobby` repo), the **Python skill**, the **actual gobby-cli test suite** (1,019 tests), and
the current Rust ecosystem, the verdict is:

**The "Python is more robust" feeling is ~60% tooling gap, ~40% perception — not a language
limitation.** Two concrete causes:

1. **The skill under-specifies.** The Python skill's `references/testing.md` shows fixtures,
   `parametrize`, mocking, markers, and `freezegun`. The Rust `references/testing.md` already
   covers unit layout, `Result` tests, builders, `proptest`, trait mocking, and `insta` — but
   the main `SKILL.md` Testing section is 5 bullets and **never mentions the runner
   (`cargo-nextest`), parameterization (`rstest`), CLI testing (`assert_cmd`), coverage, or
   async test time-control.** A pytest-trained reader sees a thinner menu and assumes Rust is
   thinner.

2. **The codebase hand-rolls what the ecosystem already solves.** gwiki re-implements a CLI
   runner 4 times (`fn gwiki(...)` + `assert_success` duplicated across `cli_smoke.rs`,
   `cli_parse.rs`, `cli_output.rs`, `cli_collect.rs`) instead of `assert_cmd`; uses
   `for args in cases` loops instead of `rstest` (first failure hides the rest); hand-checks
   `serde_json::Value` fields instead of `insta` snapshots; CI runs serial per-crate
   `cargo test` with **no coverage and no parallelism**.

**Where Rust is actually *better* than pytest** (worth telling the user, and putting in the
skill): `#[tokio::test(start_paused = true)]` gives deterministic time control pytest can't
match; `cargo-nextest` process-per-test isolation kills a whole class of flaky tests;
`proptest` ≥ `hypothesis`; `cargo-llvm-cov` region coverage ≥ `coverage.py`; the compiler
itself eliminates test categories Python needs. The genuine pytest wins that Rust can't fully
close: no `conftest.py` equivalent, no session-scoped fixtures, smaller plugin ecosystem,
macro-heavy syntax.

**Decisions (confirmed with user):** do **both** the skill and the codebase; adopt a **curated
stack** (`nextest` + `insta` + `assert_cmd` + `rstest` + `proptest` + `pretty_assertions` +
`cargo-llvm-cov`) but **keep mocking trait-based** — no `mockall`/`wiremock`. Trait/generic
dependency injection stays the idiom.

---

## Track A — Rust skill (sibling repo `gobby`)

Files (source of the gobby-skills hub install):
- `…/gobby/src/gobby/install/shared/skills/rust/SKILL.md`
- `…/gobby/src/gobby/install/shared/skills/rust/references/testing.md`

### A1. Rewrite `SKILL.md` → Testing section

Replace the 5-bullet section with the curated stack, mirroring the Python skill's altitude
(concise bullets, defer detail to the reference). Keep the "repo conventions take precedence"
framing. New bullets to cover:

- **Runner**: prefer `cargo nextest run` (process-per-test isolation, parallel, retries);
  fall back to `cargo test`. Run `cargo test --doc` separately for doctests (nextest skips them).
- **Layout**: unit tests in `#[cfg(test)] mod tests`; integration tests in `tests/`, one file
  per feature, shared helpers in `tests/common/mod.rs`. *(keep)*
- **Result tests**: `-> anyhow::Result<()>` over `.unwrap()` chains. *(keep)*
- **Parameterize** with `rstest` `#[case(...)]` instead of `for`-loops over input vectors — each
  case reports independently. *(new — the `parametrize` analogue)*
- **CLI tests**: `assert_cmd` + `predicates` for binaries; `assert_fs`/`tempfile` for filesystem.
  *(new — these are CLI tools)*
- **Property tests** with `proptest` for parsers, serialization, id/hash determinism. *(keep)*
- **Snapshot** CLI/serialized output with `insta` (`cargo insta review`); redact nondeterministic
  fields. *(promote from reference to main)*
- **Mock external I/O with trait objects or generics — not heavy mock frameworks.** *(keep
  verbatim — the confirmed stance)*
- **Async**: `#[tokio::test]`; use `start_paused = true` for deterministic time. *(new)*
- **Coverage**: `cargo llvm-cov` locally/CI. *(new)*
- Close with the existing "verify fmt/clippy/test pass" line. *(keep)*

### A2. Extend `references/testing.md`

Keep all existing sections (unit layout, Result tests, integration, builders, proptest,
trait mocking, insta). **Add**:

- **`cargo-nextest`** — why (isolation/speed/retries), `.config/nextest.toml` test-groups for
  serialized resources, and the `cargo test --doc` caveat.
- **Parameterized tests with `rstest`** — `#[rstest] #[case(...)]` + `#[fixture]`. Note the
  tradeoff vs `for`-loops (independent reporting) and the one-assertion-per-case guidance.
- **CLI testing with `assert_cmd` + `predicates`** — `Command::cargo_bin("app")`, `.assert()
  .success().stdout(predicate::str::contains(...))`, env setup.
- **Async tests** — `#[tokio::test]`, `start_paused = true` time control, `flavor =
  "multi_thread"`, `tokio_test::io` mock I/O.
- **`pretty_assertions`** — drop-in `assert_eq!` for readable diffs.
- **Coverage** — `cargo llvm-cov --html` / `--lcov`.
- **A "Coming from pytest" mapping table** so a Python-trained reader gets a direct translation:

  | pytest | Rust |
  |---|---|
  | `pytest` runner | `cargo nextest run` |
  | `@pytest.mark.parametrize` | `rstest` `#[case]` |
  | `@pytest.fixture` (+ yield) | `rstest` `#[fixture]`; `Drop` for teardown |
  | `unittest.mock` / `pytest-mock` | trait injection (no framework) |
  | `responses` / HTTP mock | trait at the I/O boundary |
  | `syrupy` snapshots | `insta` |
  | `hypothesis` | `proptest` |
  | `pytest-cov` | `cargo llvm-cov` |
  | `freezegun` | `#[tokio::test(start_paused)]` / inject a `Clock` trait |
  | `CliRunner` | `assert_cmd` |
  | markers `-m slow` | `#[ignore]` / `cfg` features / nextest `-E` filtersets |

  Add a short note: **no `conftest.py` / session-scoped fixtures** in Rust — use `tests/common/
  mod.rs` modules and `once_cell`/`OnceLock` for shared expensive setup.

> Skill changes are docs-only; no version bump needed unless the hub tracks skill versions
> (both skills are currently `1.0.0` — bump to `1.1.0` if that field is enforced on reinstall).

---

## Track B — gobby-cli codebase (phased, low-risk first)

Sequencing principle: **additive/zero-rewrite first** (reversible, no risk to 1,019 tests),
**targeted de-duplication next**, **broad adoption last**.

### Phase 1 — Additive (no test rewrites)

- **`Cargo.toml`** (root): add a `[workspace.dependencies]` section (none exists today,
  `Cargo.toml:1`). **Don't blanket-move every shared dep.** Centralize only (a) deps with real
  version drift — `temp-env` is `0.3` in gcode vs `0.3.6` in ghook — and (b) the new test
  tooling: `assert_cmd`, `predicates`, `rstest`, `proptest`, `pretty_assertions`, `insta`
  (features `json`, `redactions`, `filters`). **Keep each crate's dependency table semantically
  correct**: `tempfile` is a *runtime* dep in gcode/gwiki and a dev-dep elsewhere — don't
  collapse that distinction just to share a version; only point it at `.workspace = true` if the
  version is actually unified, and keep it in the right `[dependencies]` vs `[dev-dependencies]`
  table per crate. Leave per-package `[profile.release.package.*]` untouched.
- **`.config/nextest.toml`** (new): `[profile.default]`/`[profile.ci]` with `fail-fast = false`;
  a `serial-db` `[test-groups]` entry with `max-threads = 1`. **The filter must cover ALL
  live-Postgres tests, not just `setup`** — they appear across `setup`, `schema`, `search::fts`,
  the `gcode/tests/*standalone.rs` integration files, and the gwiki configured-Postgres tests
  (`ProjectCleanup`/`GwikiScopeCleanup`). Use a filterset that unions those, e.g.
  `package(gobby-code) & (test(/setup/) | test(/schema/) | test(/fts/) | binary(/standalone/))`
  plus `package(gobby-wiki) & test(/configured/)`; verify the final set with
  `cargo nextest list -E '<filter>'` before trusting it. **Why this matters:** under nextest's
  process-per-test model, `#[serial_test::serial]` becomes a no-op (each test is its own
  process), so the *cross-process* DB resource needs the test-group as the real serialization
  mechanism. Keep the `#[serial]` attrs so plain `cargo test` still works.
- **`.github/workflows/ci.yml`**: install via `taiki-e/install-action@nextest` /
  `@cargo-llvm-cov`; swap each `cargo test -p X [--features…]` → `cargo nextest run -p X
  [--features…]` (current steps are serial `cargo test`, `ci.yml:31`+; preserve the per-crate +
  feature-variant matrix; the `codewiki` filter becomes `-E 'test(codewiki)'`); add a
  `cargo test --doc --workspace --no-default-features` step (defensive — zero doctests today, but
  nextest never runs doctests so this keeps the contract alive); add a **separate parallel
  `coverage` job** that installs the **`llvm-tools-preview` rustup component** (required by
  cargo-llvm-cov — called out in nextest's coverage docs) and runs `cargo llvm-cov --workspace
  --no-default-features nextest --lcov`, `continue-on-error: true`, report-only (no threshold gate
  initially).

### Phase 2 — Targeted de-duplication

- **`crates/gwiki/tests/common/mod.rs`**: add a **fixture struct, not a bare
  `gwiki_cmd()`**. A function that creates a `TempDir` internally and returns an `assert_cmd::
  Command` is a use-after-free waiting to happen — the `TempDir` drops at end of the function and
  the dir is gone before the command runs. Instead define a `GwikiFixture` that **owns** the
  `TempDir` (and hub path) for the test's lifetime and exposes `fn cmd(&self) -> assert_cmd::
  Command`. The builder centralizes the env contract (`GOBBY_WIKI_HUB`, isolated `HOME`, and
  `env_remove` of the **full superset** of DB vars found across the 4 duplicated copies —
  `cli_parse.rs:6`, `cli_collect.rs:5`, `cli_output.rs:3`, `cli_smoke.rs:10`:
  `GWIKI_DATABASE_URL`, `GOBBY_POSTGRES_DSN`, `GCODE_DATABASE_URL`,
  `GWIKI_POSTGRES_TEST_DATABASE_URL`, `GCODE_POSTGRES_TEST_DATABASE_URL`). The test binds
  `let fx = GwikiFixture::new();` so the tempdir lives until the test ends, then calls
  `fx.cmd().args([...]).assert()...`. Move auto-init logic into `fx.seed_topic()`/`seed_project()`
  methods; keep `json_output`/`assert_json_path` helpers.
- **Migrate file-by-file** (simplest → largest): `cli_output.rs` → `cli_collect.rs` →
  `cli_parse.rs` → `cli_search.rs` → `cli_smoke.rs`, deleting each file's private `gwiki()`/
  `assert_success` copy and switching assertions to `.assert().success().stdout(predicate…)`.
  A temporary `Output`-returning compat method on the fixture lets a file migrate its helper
  without rewriting every assertion in one PR; remove it once all files are migrated.
- **rstest-ify only the genuine parametrized behavior tables**:
  `cli_parse.rs::core_commands_parse_scope_flags` (14 cases) and
  `cli_collect.rs::collect_parses_scope_flags` → `#[rstest] #[case(...)]`, one assertion per case.
  **Do NOT rstest-ify `cli_init.rs`** — its directory/file loops are helper assertions on a
  single behavior, not a parametrized input table; leave them as plain `#[test]`s.

### Phase 3 — Broad adoption

- **`insta` snapshots** for the JSON-output tests in `cli_search.rs` / `cli_output.rs` that
  currently hand-check fields. **Mandatory redactions** for nondeterministic fields (topic/scope
  ids from `unique_topic`/`unique_suffix` = pid+nanos+uuid, chunker `epoch_secs` timestamps,
  tempdir paths). CI sets `INSTA_UPDATE=no` (fail on mismatch); commit `.snap`, gitignore
  `*.snap.new`. Where UUID5 parity *is* the contract, assert exact values — don't redact.
- **`proptest`** on the pure targets where a *property* is the contract:
  `gcode/src/index/chunker.rs::chunk_file_content` (no line loss, overlap math, monotonic
  indices); `gobby_core::search::rrf_merge` in **gcore** (sorted-descending, empty→empty — note
  `gcode/src/search/rrf.rs` just delegates here). For the UUID5 id generators in
  `gcode/src/models.rs`, proptest can only prove **determinism/injectivity within Rust** — it
  **cannot** prove parity with the Python daemon's `Symbol.make_id()`. **Lock parity with golden
  vectors instead**: a small table of hardcoded `(project_id, file_path, name, kind, byte_start)`
  inputs with the exact UUID strings the Python implementation produces, asserted with
  `assert_eq!`. Use proptest there only as a secondary determinism check.
- **`pretty_assertions`**: fold into rewritten files opportunistically.

### Risks & mitigations (top items)
- **nextest exposes order-dependent tests** → run `cargo nextest run` locally across all
  crates+features *before* touching CI; any new failure was already latently broken.
- **`#[serial]` becomes a no-op** → `serial-db` test-group is the real fix for the DB tests.
- **Coverage ~2× build cost** → separate parallel job, `--no-default-features`,
  `continue-on-error`, restrict heavy runs to `main` if needed.
- **insta snapshot churn** → redact before committing any `.snap`; start with 2–3 snapshots only.

---

## Verification

- **Skill**: re-read both edited files; confirm `SKILL.md` Testing section altitude matches the
  Python skill and the pytest→Rust table renders. If the hub caches installs, reinstall and
  `get_skill(name="rust")` via gobby-skills to confirm the new content serves.
- **Phase 1**: `cargo nextest run --workspace --no-default-features` and the per-feature variants
  pass locally with the same green/red set as `cargo test`; `cargo test --doc` passes;
  `cargo llvm-cov … --lcov` produces `lcov.info`; CI green on a draft PR.
- **Phase 2/3**: after each migration, `cargo nextest run -p gobby-wiki` (+ `--no-default-features`)
  stays green; `cargo insta test` then `cargo insta review` for snapshots; `cargo nextest run
  -p gobby-code -p gobby-core` for proptest. `cargo fmt --all --check` and
  `cargo clippy --workspace -- -D warnings` clean throughout.

## Suggested first commits
1. Track A skill edits (docs-only, independent, ship anytime).
2. Track B Phase 1 (`Cargo.toml` + `.config/nextest.toml` + CI) as one PR — additive, reversible.
3. Track B Phase 2 gwiki consolidation as a follow-up PR; Phase 3 last.
