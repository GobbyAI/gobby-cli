# Task 376 TDD Evidence

Task: #376 Build the shared capability probe and probe-backed effective router

## Red

Exact command:

```bash
cargo test -p gobby-core --no-default-features --features ai capability_status_routes
```

Result: failed before implementation. The compiler reported missing probe and
router API symbols, including `ProbeObservation`, `DaemonProbeTransport`,
`capability_status_route`, `probe_daemon_capabilities_with`, and
`effective_route_with_probe`.

## Minimal Green

Exact commands:

```bash
cargo test -p gobby-core --no-default-features --features ai capability_status_routes
cargo test -p gobby-core --no-default-features --features ai attachments_not_vision_extraction
cargo test -p gobby-core --no-default-features --features ai status_body_capability_truth
cargo test -p gobby-core --no-default-features --features ai status_route_is_availability_truth
cargo test -p gobby-core --no-default-features --features ai effective_route_auto_falls_through_per_capability
```

Result: all five focused tests passed after adding the shared probe module,
capability-level status-body parsing, and the probe-backed effective router.

## Refactor And Final Green

Exact commands:

```bash
cargo test -p gobby-core --no-default-features --features ai ai::probe::tests
cargo test -p gobby-core --no-default-features --features ai effective_route_auto_falls_through_per_capability
cargo test -p gobby-wiki --no-default-features missing_optional_endpoint_degrades
cargo clippy -p gobby-core --no-default-features --features ai -- -D warnings
cargo clippy -p gobby-wiki --no-default-features -- -D warnings
cargo fmt --check --package gobby-core --package gobby-wiki
```

Result: all commands passed.

## Test-Quality Audit

Exact command:

```bash
uv run gobby test-quality audit crates/gcore/src/ai/probe.rs crates/gcore/src/ai/mod.rs crates/gwiki/src/daemon.rs --baseline .gobby/test-quality-baseline.json --fail-on-new --min-severity high
```

Output:

```text
Test quality audit
Files scanned: 3
Tests scanned: 9
Issues: 0
Severity: none
Codes: none
Baseline: loaded (.gobby/test-quality-baseline.json)
Baseline mode: diff
New issues: 0
Failing new issues >= high: 0
```
