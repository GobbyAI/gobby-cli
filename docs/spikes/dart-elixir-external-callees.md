# Dart and Elixir External Callee Provenance Spike

## Decision

Dart and Elixir need parser-surface work before external callee classification can be implemented safely. Both language specs currently have empty call queries, so gcode cannot produce call relations for either language, external or otherwise.

The minimum path is:

1. Add call query captures.
2. Capture import or alias provenance with enough structure to distinguish local, package, and standard-library roots.
3. Add manifest-backed external provenance.
4. Classify only direct, explicit, module-qualified calls.

## Dart

### Current Surface

`languages.rs` captures Dart symbols from function, class, method, and enum declarations. It captures imports through `import_or_export`, but `call_query` is empty.

### Required Query Additions

Dart needs call captures for:

- Bare function calls, kept unresolved unless local same-file resolution applies.
- Prefixed calls such as `json.decode(...)`.
- Static or constructor-like qualified calls such as `http.Client(...)` when the prefix maps to an imported package alias.
- Method invocations on receivers, kept unresolved.

The query layer must capture the callee name and the root prefix separately. Capturing only the final identifier is not enough because `decode(...)`, `json.decode(...)`, and `client.decode(...)` have different provenance.

### Provenance Needed

Dart imports need structured parsing of:

- `import 'dart:convert';`
- `import 'package:http/http.dart' as http;`
- `import './local.dart';`
- `show` and `hide` combinators.

External roots come from:

- `dart:` SDK imports.
- `package:` imports whose package name is present in `pubspec.yaml` dependencies, dev dependencies, or dependency overrides.

Relative imports and `package:` imports that point back to the current package remain local or unresolved.

### Minimum Fail-Closed Path

Classify only:

- `alias.member(...)` where `alias` comes from an explicit external `as alias` import.
- `dartSdkRoot.member(...)` only if the syntax exposes a stable prefix.

Leave unresolved:

- Unqualified calls.
- Receiver methods.
- Calls imported through `show` without an alias.
- Dynamic calls and `Function.apply`.
- Relative imports.

## Elixir

### Current Surface

`languages.rs` captures Elixir functions through `def`, `defp`, and `defmacro`, modules through `defmodule`, and imports through calls to `import`, `alias`, `use`, and `require`. `call_query` is empty.

### Required Query Additions

Elixir needs call captures for:

- Remote calls such as `Jason.decode!(body)`.
- Aliased module calls such as `HTTPoison.get(url)`.
- Local calls such as `decode!(body)`, kept unresolved except for local symbol resolution.
- Pipeline calls, where the final AST shape may still be a remote call but arguments are transformed by the pipe operator.

The query must capture module alias/root and function name separately. It also needs to avoid treating macro declarations as ordinary call sites.

### Provenance Needed

External roots come from:

- `mix.exs` dependencies.
- `mix.lock` package resolution.
- Explicit `alias External.Module, as: LocalAlias`.
- Explicit `require External.Module` for macro calls.

Local roots come from project `defmodule` captures. If a local module root collides with a dependency module, leave the call unresolved.

### Minimum Fail-Closed Path

Classify only:

- Direct remote calls where the module root or alias has explicit dependency provenance.
- Macro calls only when `require` provides explicit external provenance.

Leave unresolved:

- Local unqualified calls.
- Calls made available through `import`.
- Calls introduced by `use`.
- Dynamic `apply/3`, computed module aliases, and generated functions.
- Pipeline calls unless the captured remote call target remains structurally explicit.

## Shared Implementation Notes

- Add call queries before adding external classification.
- Extend `ImportBindings` only with explicit roots or aliases.
- Preserve local-symbol and local-module collision checks.
- Add parser tests for positive external remote calls and fail-closed local, wildcard/imported, receiver, and dynamic cases.

_Last verified: 2026-05-24_
