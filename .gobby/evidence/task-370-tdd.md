# Task 370 TDD Evidence

Task: #370 Add gcore `ai` feature and transport skeleton

## Red Recovery

The original development handoff recorded red checks before implementation. I
also recovered the retry-path red command in a detached temporary worktree at
the parent commit of the feature implementation:

- Base commit: `066bade5c1ddce9186abac8f2e411a3895d71b02`
- Implementation commit: `1fbed17d695c6103d6eb73d1c16d8f3afe53998e`
- Follow-up type-fix commit: `119442bd2f000ccdd7384ef4f42bd688a8972711`
- Temporary worktree: `/private/tmp/gobby-task-370-red.qXiydp`

Exact red command:

```bash
cargo test -p gobby-core --features ai retry_caps_at_two
```

Result: Cargo reported the pre-implementation feature boundary failure:

```text
error: the package 'gobby-core' does not contain this feature: ai
help: there is a similarly named feature: sha2
```

The original task handoff also recorded that
`cargo test -p gobby-core --test public_boundary cargo_features_define_public_boundary`
failed before the feature update because the manifest did not define
`local_backend`.

## Minimal Green

Implementation commit `1fbed17d695c6103d6eb73d1c16d8f3afe53998e` added:

- `local_backend = ["dep:ureq"]`
- `ai = ["dep:reqwest", "reqwest/multipart", "local_backend"]`
- always-compiled `gobby_core::ai_types`
- `#[cfg(feature = "ai")] pub mod ai`
- shared limiter coverage in `ai_context`
- retry and rate-limit backoff tests under the `ai` feature
- updated public-boundary assertions

That commit made the feature boundary and acceptance tests build, but QA found
one type-inference gap in `retry_caps_at_two`: the retry closure only returned
`Err`, so the generic `Ok` type of `retry_with_backoff<T>` was unconstrained.

## Refactor And Final Green

Follow-up commit `119442bd2f000ccdd7384ef4f42bd688a8972711` made the smallest
test-only fix by annotating:

```rust
let result: Result<(), AiError> = retry_with_backoff(...);
```

Final validation for the accepted code paths:

```bash
cargo test -p gobby-core --features ai retry_caps_at_two
cargo test -p gobby-core --features ai retry_honors_retry_after_before_exponential_backoff
cargo test -p gobby-core ai_error_is_transport_neutral
cargo test -p gobby-core transcription_wire_seconds_round_to_integer_milliseconds
cargo test -p gobby-core concurrency_cap_enforced
cargo test -p gobby-core --test public_boundary cargo_features_define_public_boundary
cargo test -p gobby-core --features ai --test public_boundary cargo_features_define_public_boundary
cargo clippy -p gobby-core --no-default-features -- -D warnings
cargo clippy -p gobby-core --features ai -- -D warnings
```

Result: all commands passed after this evidence artifact was added.

Feature dependency boundary checks:

```bash
cargo tree -p gobby-core --no-default-features -i reqwest
cargo tree -p gobby-core --no-default-features -i ureq
cargo tree -p gobby-core --features ai -i reqwest
cargo tree -p gobby-core --features ai -i ureq
```

Results:

- no-feature `reqwest`: Cargo reported `package ID specification 'reqwest' did not match any packages`
- no-feature `ureq`: Cargo reported `package ID specification 'ureq' did not match any packages`
- `--features ai` `reqwest`: `reqwest v0.12.28 -> gobby-core v0.3.0`
- `--features ai` `ureq`: `ureq v2.12.1 -> gobby-core v0.3.0`

## Test-Quality Audit

Exact command:

```bash
uv run gobby test-quality audit crates/gcore/src/ai/mod.rs crates/gcore/src/ai_types.rs crates/gcore/src/ai_context.rs crates/gcore/tests/public_boundary.rs --baseline .gobby/test-quality-baseline.json --fail-on-new --min-severity high
```

Output:

```text
Test quality audit
Files scanned: 4
Tests scanned: 12
Issues: 0
Severity: none
Codes: none
Baseline: loaded (.gobby/test-quality-baseline.json)
Baseline mode: diff
New issues: 0
Failing new issues >= high: 0
```
