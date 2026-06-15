---
title: crates/gcore/src/config/tests.rs
type: code_file
provenance:
- file: crates/gcore/src/config/tests.rs
  ranges:
  - 5-7
  - 14-28
  - 30-43
  - 45-53
  - 57-59
  - 61-94
  - 96-100
  - 103-106
  - 108-128
  - 130-142
  - 145-148
  - 150-163
  - 165-176
  - 179-182
  - 184-194
  - 196-206
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config/tests.rs

Module: [[code/modules/crates/gcore/src/config|crates/gcore/src/config]]

## Purpose

This file provides test-only helpers for the config system: a thread-safe in-memory logger for capturing warning logs, an `EnvGuard` that serializes and resets process-environment mutations during tests, and several `ConfigSource` test doubles. `TestSource`, `FailingResolveSource`, and `LayeredTestSource` let tests exercise config lookup and value-resolution behavior under different scenarios, including raw-value decoding, forced resolution failures, environment-pattern expansion, and store-over-YAML fallback.
[crates/gcore/src/config/tests.rs:5-7]
[crates/gcore/src/config/tests.rs:14-28]
[crates/gcore/src/config/tests.rs:15-17]
[crates/gcore/src/config/tests.rs:19-21]
[crates/gcore/src/config/tests.rs:23-27]

## API Symbols

- `TestLogger` (class) component `TestLogger [class]` (`54cb1441-fd79-5d32-aeab-e474b688fac6`) lines 5-7 [crates/gcore/src/config/tests.rs:5-7]
  - Signature: `struct TestLogger {`
  - Purpose: 'TestLogger' is a thread-safe test logger that stores 'String' log records in a 'Mutex<Vec<String>>' for synchronized in-memory collection. [crates/gcore/src/config/tests.rs:5-7]
- `TestLogger` (class) component `TestLogger [class]` (`26a009a1-ea36-55a2-9d5c-d45d24de5fc5`) lines 14-28 [crates/gcore/src/config/tests.rs:14-28]
  - Signature: `impl TestLogger {`
  - Purpose: 'TestLogger' is a thread-safe test helper that stores log messages in a mutex-protected 'Vec<String>', provides methods to clear and clone the collected records, and recovers from mutex poisoning by taking the inner guard. [crates/gcore/src/config/tests.rs:14-28]
- `TestLogger.clear` (method) component `TestLogger.clear [method]` (`92582fd3-ff7d-5d8e-9422-a7a90d1604f2`) lines 15-17 [crates/gcore/src/config/tests.rs:15-17]
  - Signature: `fn clear(&self) {`
  - Purpose: Acquires the record lock via 'lock_records()' and clears all entries from the protected records collection. [crates/gcore/src/config/tests.rs:15-17]
- `TestLogger.records` (method) component `TestLogger.records [method]` (`5c02df42-a074-586e-a3ea-3a0cbeeb0846`) lines 19-21 [crates/gcore/src/config/tests.rs:19-21]
  - Signature: `fn records(&self) -> Vec<String> {`
  - Purpose: Returns a cloned 'Vec<String>' of the current records by acquiring the records lock via 'lock_records()' and cloning the underlying collection. [crates/gcore/src/config/tests.rs:19-21]
- `TestLogger.lock_records` (method) component `TestLogger.lock_records [method]` (`961fbc47-ebad-5d6a-8a8c-34548ce70129`) lines 23-27 [crates/gcore/src/config/tests.rs:23-27]
  - Signature: `fn lock_records(&self) -> std::sync::MutexGuard<'_, Vec<String>> {`
  - Purpose: Acquires the 'records' mutex and returns a 'MutexGuard<Vec<String>>', recovering from poisoning by taking the poisoned lock’s inner value. [crates/gcore/src/config/tests.rs:23-27]
- `TestLogger` (class) component `TestLogger [class]` (`14aa471a-2c1f-5692-afbc-7d1461c6002c`) lines 30-43 [crates/gcore/src/config/tests.rs:30-43]
  - Signature: `impl log::Log for TestLogger {`
  - Purpose: 'TestLogger' is a 'log::Log' implementation that accepts only 'Error' and 'Warn' records, appends each enabled message as '"<LEVEL>: <args>"' to a locked in-memory record buffer, and performs no action on 'flush()'. [crates/gcore/src/config/tests.rs:30-43]
- `TestLogger.enabled` (method) component `TestLogger.enabled [method]` (`d1e1448c-9382-5b69-8362-44c6fd5766ad`) lines 31-33 [crates/gcore/src/config/tests.rs:31-33]
  - Signature: `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {`
  - Purpose: Returns 'true' only for log records whose severity is 'Warn' or higher-priority, by comparing 'metadata.level()' against 'log::Level::Warn'. [crates/gcore/src/config/tests.rs:31-33]
- `TestLogger.log` (method) component `TestLogger.log [method]` (`ac99cd84-a06a-546e-8814-3a2f3e441fb4`) lines 35-40 [crates/gcore/src/config/tests.rs:35-40]
  - Signature: `fn log(&self, record: &log::Record<'_>) {`
  - Purpose: If the record’s metadata is enabled, this method acquires the record buffer lock and appends a formatted '"LEVEL: message"' string built from 'record.level()' and 'record.args()'. [crates/gcore/src/config/tests.rs:35-40]
- `TestLogger.flush` (method) component `TestLogger.flush [method]` (`2cb144b2-df30-5d8e-bbe9-a1cf1038ef41`) lines 42-42 [crates/gcore/src/config/tests.rs:42]
  - Signature: `fn flush(&self) {}`
  - Purpose: 'flush' is a no-op method that takes an immutable reference to 'self' and performs no side effects. [crates/gcore/src/config/tests.rs:42]
- `capture_warn_logs` (function) component `capture_warn_logs [function]` (`4eb74720-221b-5075-82f6-089342a162b3`) lines 45-53 [crates/gcore/src/config/tests.rs:45-53]
  - Signature: `fn capture_warn_logs<R>(f: impl FnOnce() -> R) -> (R, Vec<String>) {`
  - Purpose: Initializes a test logger once at 'Warn' level, clears any prior records, runs 'f', and returns its result together with the collected warning log messages as 'Vec<String>'. [crates/gcore/src/config/tests.rs:45-53]
- `EnvGuard` (class) component `EnvGuard [class]` (`2ceee697-a9c3-5817-99b5-b62aef1c2bad`) lines 57-59 [crates/gcore/src/config/tests.rs:57-59]
  - Signature: `struct EnvGuard {`
  - Purpose: 'EnvGuard' is a RAII wrapper around a 'MutexGuard<'static, ()>' that holds a global mutex lock for the lifetime of the guard. [crates/gcore/src/config/tests.rs:57-59]
- `EnvGuard` (class) component `EnvGuard [class]` (`d39ee767-212c-5b32-8548-c470e9e0013e`) lines 61-94 [crates/gcore/src/config/tests.rs:61-94]
  - Signature: `impl EnvGuard {`
  - Purpose: EnvGuard is a test-only wrapper that serializes process-environment access with a global mutex, clears a fixed set of Gobby-related variables on construction, and provides locked 'set' and 'clear' methods for safely mutating those environment variables. [crates/gcore/src/config/tests.rs:61-94]
- `EnvGuard.new` (method) component `EnvGuard.new [method]` (`e074357c-ef01-58c1-a8c0-3acf3ee71e7f`) lines 62-70 [crates/gcore/src/config/tests.rs:62-70]
  - Signature: `fn new() -> Self {`
  - Purpose: Constructs a 'Self' by acquiring 'TEST_ENV_LOCK', recovering the inner lock if poisoned, clearing the guarded test environment state, and returning the initialized guard. [crates/gcore/src/config/tests.rs:62-70]
- `EnvGuard.clear` (method) component `EnvGuard.clear [method]` (`60cb3fb2-36c2-55f4-8334-dadb66dd4fcf`) lines 72-88 [crates/gcore/src/config/tests.rs:72-88]
  - Signature: `fn clear(&self) {`
  - Purpose: Acquires the environment mutation lock and then removes a fixed set of Gobby test/configuration variables from the process environment via 'std::env::remove_var'. [crates/gcore/src/config/tests.rs:72-88]
- `EnvGuard.set` (method) component `EnvGuard.set [method]` (`76d236dd-4b18-597b-9762-6cd1a648b42d`) lines 90-93 [crates/gcore/src/config/tests.rs:90-93]
  - Signature: `fn set(&self, key: &str, value: &str) {`
  - Purpose: Acquires the internal environment lock and then unsafely calls 'std::env::set_var' to set the process environment variable 'key' to 'value'. [crates/gcore/src/config/tests.rs:90-93]
- `EnvGuard` (class) component `EnvGuard [class]` (`5fc47acb-0eea-5662-88fa-c02432721afc`) lines 96-100 [crates/gcore/src/config/tests.rs:96-100]
  - Signature: `impl Drop for EnvGuard {`
  - Purpose: 'EnvGuard' is a RAII drop guard whose 'Drop' implementation invokes 'self.clear()' to automatically clear its managed environment state when the value goes out of scope. [crates/gcore/src/config/tests.rs:96-100]
- `EnvGuard.drop` (method) component `EnvGuard.drop [method]` (`2db841ce-8b56-5272-b030-fe174f4a797e`) lines 97-99 [crates/gcore/src/config/tests.rs:97-99]
  - Signature: `fn drop(&mut self) {`
  - Purpose: 'drop' invokes 'self.clear()' to remove all elements from the collection when the value is dropped. [crates/gcore/src/config/tests.rs:97-99]
- `TestSource` (class) component `TestSource [class]` (`8cf2cea3-ba6a-5a53-8d6e-f63a464ac9c3`) lines 103-106 [crates/gcore/src/config/tests.rs:103-106]
  - Signature: `struct TestSource {`
  - Purpose: 'TestSource' is a data-only Rust struct that stores a 'HashMap<&'static str, String>' of keyed values alongside a 'Vec<String>' of resolved values. [crates/gcore/src/config/tests.rs:103-106]
- `TestSource` (class) component `TestSource [class]` (`6610c6db-c6f0-5e0b-9e7d-fc4b8fc17331`) lines 108-128 [crates/gcore/src/config/tests.rs:108-128]
  - Signature: `impl TestSource {`
  - Purpose: 'TestSource' is a test-only source type that builds an internal key-to-string value map either from literal values or from decoded raw config values, initializing 'resolved_values' as an empty 'Vec'. [crates/gcore/src/config/tests.rs:108-128]
- `TestSource.with_values` (method) component `TestSource.with_values [method]` (`28f1b392-b583-5f76-9047-c0569952cb2c`) lines 109-117 [crates/gcore/src/config/tests.rs:109-117]
  - Signature: `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {`
  - Purpose: Constructs a new instance by consuming an iterator of '(&'static str, &'static str)' pairs, converting each value to 'String' and collecting them into 'values' while initializing 'resolved_values' as an empty 'Vec'. [crates/gcore/src/config/tests.rs:109-117]
- `TestSource.with_raw_values` (method) component `TestSource.with_raw_values [method]` (`75d2732f-f203-5bf4-8e38-7dfddb316728`) lines 119-127 [crates/gcore/src/config/tests.rs:119-127]
  - Signature: `fn with_raw_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {`
  - Purpose: Constructs 'Self' by decoding each provided static key/value pair with 'decode_config_value', collecting only successfully decoded entries into 'values', and initializing 'resolved_values' as an empty 'Vec'. [crates/gcore/src/config/tests.rs:119-127]
- `TestSource` (class) component `TestSource [class]` (`68c7f910-0c67-57e0-8771-fe2361abfa6e`) lines 130-142 [crates/gcore/src/config/tests.rs:130-142]
  - Signature: `impl ConfigSource for TestSource {`
  - Purpose: 'TestSource' is a 'ConfigSource' test double that returns cloned entries from 'values' for 'config_value', records every 'resolve_value' input in 'resolved_values', maps '$secret:<name>' to 'resolved-<name>', and otherwise resolves environment-pattern substitutions or falls back to the original string. [crates/gcore/src/config/tests.rs:130-142]
- `TestSource.config_value` (method) component `TestSource.config_value [method]` (`b7dd7640-4901-5a4e-b6de-eeca84269c62`) lines 131-133 [crates/gcore/src/config/tests.rs:131-133]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Returns a cloned 'String' value associated with 'key' from 'self.values' if present, otherwise 'None'. [crates/gcore/src/config/tests.rs:131-133]
- `TestSource.resolve_value` (method) component `TestSource.resolve_value [method]` (`a37d2b42-e464-5a39-8980-2b8a3884868c`) lines 135-141 [crates/gcore/src/config/tests.rs:135-141]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Records the input in 'resolved_values', returns 'resolved-{secret_name}' for values prefixed with '$secret:', and otherwise returns the result of 'resolve_env_pattern(value)' or the original string if no pattern is resolved. [crates/gcore/src/config/tests.rs:135-141]
- `FailingResolveSource` (class) component `FailingResolveSource [class]` (`f503cb76-08ae-5f84-9f98-e75ac6b41b55`) lines 145-148 [crates/gcore/src/config/tests.rs:145-148]
  - Signature: `struct FailingResolveSource {`
  - Purpose: 'FailingResolveSource' is a data container struct that stores a 'HashMap<&'static str, String>' of resolved values alongside a 'Vec<String>' of values designated to fail resolution. [crates/gcore/src/config/tests.rs:145-148]
- `FailingResolveSource` (class) component `FailingResolveSource [class]` (`55b7ce1a-101c-588a-a083-327e4233b30d`) lines 150-163 [crates/gcore/src/config/tests.rs:150-163]
  - Signature: `impl FailingResolveSource {`
  - Purpose: 'FailingResolveSource' is a test helper that constructs a source from an iterator of static string key-value pairs and a separate iterator of keys that should resolve as failures, storing the values as owned 'String's and the failing keys as owned 'String's. [crates/gcore/src/config/tests.rs:150-163]
- `FailingResolveSource.with_values_and_failures` (method) component `FailingResolveSource.with_values_and_failures [method]` (`dc5edda0-e798-5cbc-89ae-69ccca023e87`) lines 151-162 [crates/gcore/src/config/tests.rs:151-162]
  - Signature: `fn with_values_and_failures(`
  - Purpose: Constructs 'Self' by collecting the provided '(&'static str, &'static str)' pairs into a 'values' map with 'String' values and collecting the provided failing keys into a 'failing_values' set of owned 'String's. [crates/gcore/src/config/tests.rs:151-162]
- `FailingResolveSource` (class) component `FailingResolveSource [class]` (`7b277258-d066-5b2a-a258-737bbba93a1e`) lines 165-176 [crates/gcore/src/config/tests.rs:165-176]
  - Signature: `impl ConfigSource for FailingResolveSource {`
  - Purpose: 'FailingResolveSource' is a 'ConfigSource' implementation that returns stored config values unchanged via 'config_value' but makes 'resolve_value' fail with 'anyhow!("resolver failed")' for any value listed in 'failing_values', otherwise resolving environment patterns and falling back to the original string. [crates/gcore/src/config/tests.rs:165-176]
- `FailingResolveSource.config_value` (method) component `FailingResolveSource.config_value [method]` (`71538b30-8720-5dd7-81ba-eb60ef17fbf2`) lines 166-168 [crates/gcore/src/config/tests.rs:166-168]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Returns a cloned 'String' from 'self.values' for the given 'key', or 'None' if the key is absent. [crates/gcore/src/config/tests.rs:166-168]
- `FailingResolveSource.resolve_value` (method) component `FailingResolveSource.resolve_value [method]` (`baba1a5e-e35b-54d6-b801-da11796794db`) lines 170-175 [crates/gcore/src/config/tests.rs:170-175]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: 'resolve_value' returns an error if 'value' matches any configured failing value; otherwise it expands any environment-variable pattern in 'value' and returns the resolved string, or the original string if no pattern is present. [crates/gcore/src/config/tests.rs:170-175]
- `LayeredTestSource` (class) component `LayeredTestSource [class]` (`0eee1644-d484-5829-ac94-ae4b3168f183`) lines 179-182 [crates/gcore/src/config/tests.rs:179-182]
  - Signature: `struct LayeredTestSource {`
  - Purpose: 'LayeredTestSource' is a two-layer test source wrapper that composes a 'store' 'TestSource' with an underlying 'yaml' 'TestSource'. [crates/gcore/src/config/tests.rs:179-182]
- `LayeredTestSource` (class) component `LayeredTestSource [class]` (`511441cb-a8ec-509a-9663-ce6fbf00a112`) lines 184-194 [crates/gcore/src/config/tests.rs:184-194]
  - Signature: `impl LayeredTestSource {`
  - Purpose: 'LayeredTestSource' is a test source wrapper that builds a layered configuration source from separate store and YAML 'TestSource' instances initialized with '(&'static str, &'static str)' key-value pairs. [crates/gcore/src/config/tests.rs:184-194]
- `LayeredTestSource.with_layers` (method) component `LayeredTestSource.with_layers [method]` (`93165376-8483-50e7-a129-13e47a69ec2e`) lines 185-193 [crates/gcore/src/config/tests.rs:185-193]
  - Signature: `fn with_layers(`
  - Purpose: Constructs and returns a 'Self' instance by initializing 'store' and 'yaml' with 'TestSource::with_values' from the provided iterator pairs of '&'static str' key-value entries. [crates/gcore/src/config/tests.rs:185-193]
- `LayeredTestSource` (class) component `LayeredTestSource [class]` (`16289731-b9ae-51a5-9c96-5f2b50280b84`) lines 196-206 [crates/gcore/src/config/tests.rs:196-206]
  - Signature: `impl ConfigSource for LayeredTestSource {`
  - Purpose: 'LayeredTestSource' is a 'ConfigSource' that resolves 'config_value' by querying 'store' first and falling back to 'yaml', while delegating 'resolve_value' exclusively to 'store'. [crates/gcore/src/config/tests.rs:196-206]
- `LayeredTestSource.config_value` (method) component `LayeredTestSource.config_value [method]` (`2bb025b8-4abf-5fa6-a6d7-5b2576cf5075`) lines 197-201 [crates/gcore/src/config/tests.rs:197-201]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: 'config_value' returns the first available configuration value for 'key' by querying 'self.store' and, if absent there, falling back to 'self.yaml', yielding 'Option<String>'. [crates/gcore/src/config/tests.rs:197-201]
- `LayeredTestSource.resolve_value` (method) component `LayeredTestSource.resolve_value [method]` (`00fcb270-174d-5305-b915-713696c44cd6`) lines 203-205 [crates/gcore/src/config/tests.rs:203-205]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: 'resolve_value' forwards the input string to 'self.store.resolve_value' and returns the resulting 'anyhow::Result<String>'. [crates/gcore/src/config/tests.rs:203-205]

