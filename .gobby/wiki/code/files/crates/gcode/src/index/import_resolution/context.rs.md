---
title: crates/gcode/src/index/import_resolution/context.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context.rs
  ranges:
  - 19-37
  - 39-53
  - 40-45
  - 47-52
  - 56-59
  - 62-67
  - 70-73
  - 76-79
  - 82-85
  - 152-162
  - 164-189
  - 191-228
  - 230-262
  - 264-271
  - 273-282
  - 284-308
  - 310-350
  - 352-361
  - 363-376
  - 378-380
  - 382-420
  - 422-462
  - 464-503
  - 505-545
  - 547-588
  - 590-609
  - 611-617
  - 619-655
  - 657-668
  - 670-691
  - 693-698
  - 700-706
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

`crates/gcode/src/index/import_resolution/context.rs` exposes 32 indexed API symbols.
[crates/gcode/src/index/import_resolution/context.rs:19-37]
[crates/gcode/src/index/import_resolution/context.rs:39-53]
[crates/gcode/src/index/import_resolution/context.rs:40-45]
[crates/gcode/src/index/import_resolution/context.rs:47-52]
[crates/gcode/src/index/import_resolution/context.rs:56-59]
[crates/gcode/src/index/import_resolution/context.rs:62-67]
[crates/gcode/src/index/import_resolution/context.rs:70-73]
[crates/gcode/src/index/import_resolution/context.rs:76-79]
[crates/gcode/src/index/import_resolution/context.rs:82-85]
[crates/gcode/src/index/import_resolution/context.rs:152-162]
[crates/gcode/src/index/import_resolution/context.rs:164-189]
[crates/gcode/src/index/import_resolution/context.rs:191-228]
[crates/gcode/src/index/import_resolution/context.rs:230-262]
[crates/gcode/src/index/import_resolution/context.rs:264-271]
[crates/gcode/src/index/import_resolution/context.rs:273-282]
[crates/gcode/src/index/import_resolution/context.rs:284-308]
[crates/gcode/src/index/import_resolution/context.rs:310-350]
[crates/gcode/src/index/import_resolution/context.rs:352-361]
[crates/gcode/src/index/import_resolution/context.rs:363-376]
[crates/gcode/src/index/import_resolution/context.rs:378-380]
[crates/gcode/src/index/import_resolution/context.rs:382-420]
[crates/gcode/src/index/import_resolution/context.rs:422-462]
[crates/gcode/src/index/import_resolution/context.rs:464-503]
[crates/gcode/src/index/import_resolution/context.rs:505-545]
[crates/gcode/src/index/import_resolution/context.rs:547-588]
[crates/gcode/src/index/import_resolution/context.rs:590-609]
[crates/gcode/src/index/import_resolution/context.rs:611-617]
[crates/gcode/src/index/import_resolution/context.rs:619-655]
[crates/gcode/src/index/import_resolution/context.rs:657-668]
[crates/gcode/src/index/import_resolution/context.rs:670-691]
[crates/gcode/src/index/import_resolution/context.rs:693-698]
[crates/gcode/src/index/import_resolution/context.rs:700-706]

## API Symbols

- `ImportResolutionContext` (class) component `ImportResolutionContext [class]` (`e24f1e4c-2253-5ebc-9e69-07b59cc9aabd`) lines 19-37 [crates/gcode/src/index/import_resolution/context.rs:19-37]
  - Signature: `pub struct ImportResolutionContext {`
  - Purpose: ImportResolutionContext encapsulates multi-language import resolution metadata, aggregating external packages, local symbols, self-references, and override mappings across eleven programming languages (Python, JavaScript, Go, Rust, Java, C#, PHP, Ruby, Swift, Dart, and Elixir). [crates/gcode/src/index/import_resolution/context.rs:19-37]
- `ImportResolutionContext` (class) component `ImportResolutionContext [class]` (`8c8a0c4e-f900-59c3-ad03-0ef6ff240633`) lines 39-53 [crates/gcode/src/index/import_resolution/context.rs:39-53]
  - Signature: `impl ImportResolutionContext {`
  - Purpose: ImportResolutionContext resolves import roots by checking configured override mappings first before delegating to default lookup functions for Ruby requires and Elixir external modules. [crates/gcode/src/index/import_resolution/context.rs:39-53]
- `ImportResolutionContext.ruby_require_root` (method) component `ImportResolutionContext.ruby_require_root [method]` (`82f5659f-6af8-53fe-9228-a6929b8cfbf4`) lines 40-45 [crates/gcode/src/index/import_resolution/context.rs:40-45]
  - Signature: `pub(super) fn ruby_require_root(&self, required: &str) -> Option<&str> {`
  - Purpose: This method resolves the root path for a Ruby require by first checking an overrides map, then falling back to a default resolver function. [crates/gcode/src/index/import_resolution/context.rs:40-45]
- `ImportResolutionContext.elixir_external_root_module` (method) component `ImportResolutionContext.elixir_external_root_module [method]` (`c1228792-e981-55f7-8c95-c5efa6f00a4f`) lines 47-52 [crates/gcode/src/index/import_resolution/context.rs:47-52]
  - Signature: `pub(super) fn elixir_external_root_module(&self, root: &str) -> Option<&str> {`
  - Purpose: This method performs a prioritized lookup of an Elixir external root module, first checking override mappings before falling back to default root mappings, and returns an optional string reference. [crates/gcode/src/index/import_resolution/context.rs:47-52]
- `ExternalImportBinding` (class) component `ExternalImportBinding [class]` (`beb87e1c-a626-5f1f-9345-c5232b40fefc`) lines 56-59 [crates/gcode/src/index/import_resolution/context.rs:56-59]
  - Signature: `pub(crate) struct ExternalImportBinding {`
  - Purpose: ExternalImportBinding is a crate-internal struct that associates an external module with the name of an imported callable, representing a binding reference to an external dependency. [crates/gcode/src/index/import_resolution/context.rs:56-59]
- `ImportBindings` (class) component `ImportBindings [class]` (`dca34dcb-3a01-58c1-87d8-da808a075ee4`) lines 62-67 [crates/gcode/src/index/import_resolution/context.rs:62-67]
  - Signature: `pub(crate) struct ImportBindings {`
  - Purpose: `ImportBindings` is a crate-scoped struct that aggregates bare module imports, member bindings, wildcard modules, and external root mappings for managing module import resolution. [crates/gcode/src/index/import_resolution/context.rs:62-67]
- `ExternalRootBinding` (class) component `ExternalRootBinding [class]` (`5c10f9e3-8195-5c5b-a967-4ca6c793c248`) lines 70-73 [crates/gcode/src/index/import_resolution/context.rs:70-73]
  - Signature: `pub(crate) struct ExternalRootBinding {`
  - Purpose: ExternalRootBinding is a crate-internal struct that represents a binding to an external module with a flag indicating whether the module path was derived from a qualifier. [crates/gcode/src/index/import_resolution/context.rs:70-73]
- `ExtractedImports` (class) component `ExtractedImports [class]` (`d4bb6afb-9ded-5045-bd7c-91b497c69db0`) lines 76-79 [crates/gcode/src/index/import_resolution/context.rs:76-79]
  - Signature: `pub(crate) struct ExtractedImports {`
  - Purpose: ExtractedImports is a crate-private struct that encapsulates a vector of ImportRelation objects and an ImportBindings instance to represent extracted import declarations and their associated variable bindings. [crates/gcode/src/index/import_resolution/context.rs:76-79]
- `ExternalCallTarget` (class) component `ExternalCallTarget [class]` (`7ca0f75f-8ff2-5204-9791-050efa1d7965`) lines 82-85 [crates/gcode/src/index/import_resolution/context.rs:82-85]
  - Signature: `pub(crate) struct ExternalCallTarget {`
  - Purpose: `ExternalCallTarget` is a crate-internal struct that identifies an external function call by storing the module and function name of the callee. [crates/gcode/src/index/import_resolution/context.rs:82-85]
- `build_import_resolution_context` (function) component `build_import_resolution_context [function]` (`de706f3b-489f-5058-8dcf-306a7df250ce`) lines 152-162 [crates/gcode/src/index/import_resolution/context.rs:152-162]
  - Signature: `pub fn build_import_resolution_context(`
  - Purpose: Constructs an `ImportResolutionContext` from a root path and list of candidate files by delegating to `build_import_resolution_context_with_overrides` with empty override maps. [crates/gcode/src/index/import_resolution/context.rs:152-162]
- `build_import_resolution_context_with_overrides` (function) component `build_import_resolution_context_with_overrides [function]` (`20f62109-b4b8-589b-8404-2a3d49722dff`) lines 164-189 [crates/gcode/src/index/import_resolution/context.rs:164-189]
  - Signature: `pub fn build_import_resolution_context_with_overrides(`
  - Purpose: Constructs a multi-language `ImportResolutionContext` by building language-specific module indices from candidate files and loading external package metadata, with optional Ruby and Elixir root override mappings. [crates/gcode/src/index/import_resolution/context.rs:164-189]
- `build_python_module_index` (function) component `build_python_module_index [function]` (`e1682169-e23a-543d-8a3f-980c8fca3bb0`) lines 191-228 [crates/gcode/src/index/import_resolution/context.rs:191-228]
  - Signature: `pub(super) fn build_python_module_index(`
  - Purpose: Constructs a HashSet of Python module identifiers by converting relative paths of .py/.pyi files to dot-separated module names, removing `__init__` suffixes, and including variants without "src." prefixes. [crates/gcode/src/index/import_resolution/context.rs:191-228]
- `load_js_external_packages` (function) component `load_js_external_packages [function]` (`7ba7179b-456f-57ee-816e-a2659bf976b5`) lines 230-262 [crates/gcode/src/index/import_resolution/context.rs:230-262]
  - Signature: `pub(super) fn load_js_external_packages(root_path: &Path) -> HashSet<String> {`
  - Purpose: Reads a package.json file and returns a HashSet of all package names aggregated from its dependencies, devDependencies, peerDependencies, optionalDependencies, bundledDependencies, and bundleDependencies fields. [crates/gcode/src/index/import_resolution/context.rs:230-262]
- `load_js_self_package_name` (function) component `load_js_self_package_name [function]` (`fd5d8525-3676-5763-874c-711e900e07af`) lines 264-271 [crates/gcode/src/index/import_resolution/context.rs:264-271]
  - Signature: `pub(super) fn load_js_self_package_name(root_path: &Path) -> Option<String> {`
  - Purpose: Loads and parses the `"name"` field from a package.json file at the specified root path, returning it as an `Option<String>`. [crates/gcode/src/index/import_resolution/context.rs:264-271]
- `load_go_module_path` (function) component `load_go_module_path [function]` (`fc0d68ad-f171-5100-b2fd-a9c81b419072`) lines 273-282 [crates/gcode/src/index/import_resolution/context.rs:273-282]
  - Signature: `pub(super) fn load_go_module_path(root_path: &Path) -> Option<String> {`
  - Purpose: Parses the go.mod file at root_path and returns the module name specified in the 'module' directive, or None if the file cannot be read or the directive is absent. [crates/gcode/src/index/import_resolution/context.rs:273-282]
- `load_rust_external_crates` (function) component `load_rust_external_crates [function]` (`49a757df-a6df-58a8-a6b5-cb2d92d804fd`) lines 284-308 [crates/gcode/src/index/import_resolution/context.rs:284-308]
  - Signature: `pub(super) fn load_rust_external_crates(root_path: &Path) -> HashSet<String> {`
  - Purpose: Recursively scans all Cargo.toml manifests under a root path and aggregates all declared external crate dependencies (including dev, build, and platform-specific variants) into a deduplicated HashSet. [crates/gcode/src/index/import_resolution/context.rs:284-308]
- `rust_manifest_paths` (function) component `rust_manifest_paths [function]` (`52ccd516-377e-52c0-bcc3-595db26a415e`) lines 310-350 [crates/gcode/src/index/import_resolution/context.rs:310-350]
  - Signature: `fn rust_manifest_paths(root_path: &Path) -> Vec<PathBuf> {`
  - Purpose: Collects all Cargo.toml paths in a Rust workspace by parsing the root manifest's workspace members (with glob pattern expansion) and returning a sorted, deduplicated vector of manifest paths. [crates/gcode/src/index/import_resolution/context.rs:310-350]
- `load_rust_self_crate_name` (function) component `load_rust_self_crate_name [function]` (`5958e922-0af7-552c-81a6-891a17beaf6d`) lines 352-361 [crates/gcode/src/index/import_resolution/context.rs:352-361]
  - Signature: `pub(super) fn load_rust_self_crate_name(root_path: &Path) -> Option<String> {`
  - Purpose: Reads and parses the Cargo.toml file at the given root path, extracting the normalized package name as an Option<String>. [crates/gcode/src/index/import_resolution/context.rs:352-361]
- `collect_rust_dependency_keys` (function) component `collect_rust_dependency_keys [function]` (`2e711541-2bba-5bba-8dba-4f9fb59e65bf`) lines 363-376 [crates/gcode/src/index/import_resolution/context.rs:363-376]
  - Signature: `pub(super) fn collect_rust_dependency_keys(`
  - Purpose: Extracts Rust crate names from a TOML table, normalizes each name, and inserts non-empty normalized names into the provided HashSet. [crates/gcode/src/index/import_resolution/context.rs:363-376]
- `normalize_rust_crate_name` (function) component `normalize_rust_crate_name [function]` (`c49321da-1712-5774-918d-95128f238d98`) lines 378-380 [crates/gcode/src/index/import_resolution/context.rs:378-380]
  - Signature: `pub(super) fn normalize_rust_crate_name(name: &str) -> String {`
  - Purpose: Normalizes a Rust crate name by trimming whitespace and replacing all hyphens with underscores. [crates/gcode/src/index/import_resolution/context.rs:378-380]
- `build_java_local_class_index` (function) component `build_java_local_class_index [function]` (`1916df87-11f9-5c71-a142-83c4c1d86c8c`) lines 382-420 [crates/gcode/src/index/import_resolution/context.rs:382-420]
  - Signature: `pub(super) fn build_java_local_class_index(candidate_files: &[PathBuf]) -> HashSet<String> {`
  - Purpose: Builds a HashSet of Java class names (both simple and package-qualified) from candidate files by parallel parsing of package and type declarations. [crates/gcode/src/index/import_resolution/context.rs:382-420]
- `build_csharp_local_roots` (function) component `build_csharp_local_roots [function]` (`858dff17-95c0-552d-9531-9e03c4e80028`) lines 422-462 [crates/gcode/src/index/import_resolution/context.rs:422-462]
  - Signature: `pub(super) fn build_csharp_local_roots(candidate_files: &[PathBuf]) -> HashSet<String> {`
  - Purpose: Parallelizes extraction of C# namespace roots and declared type names from candidate source files, returning a deduplicated `HashSet<String>` of identifiers. [crates/gcode/src/index/import_resolution/context.rs:422-462]
- `build_php_local_symbol_index` (function) component `build_php_local_symbol_index [function]` (`a8899244-81c7-5851-b841-761da9b4337d`) lines 464-503 [crates/gcode/src/index/import_resolution/context.rs:464-503]
  - Signature: `pub(super) fn build_php_local_symbol_index(candidate_files: &[PathBuf]) -> HashSet<String> {`
  - Purpose: Constructs a case-insensitive HashSet of PHP symbols (both unqualified and namespace-qualified) by parallel extraction and parsing of namespace declarations from candidate PHP files. [crates/gcode/src/index/import_resolution/context.rs:464-503]
- `build_ruby_local_constant_roots` (function) component `build_ruby_local_constant_roots [function]` (`36c33943-45c4-56a6-a86c-7e386caf98f7`) lines 505-545 [crates/gcode/src/index/import_resolution/context.rs:505-545]
  - Signature: `pub(super) fn build_ruby_local_constant_roots(candidate_files: &[PathBuf]) -> HashSet<String> {`
  - Purpose: Extracts and aggregates the root-level constant names (first namespace segment before `::`) from class and module declarations across Ruby source files using parallel processing. [crates/gcode/src/index/import_resolution/context.rs:505-545]
- `build_swift_local_modules` (function) component `build_swift_local_modules [function]` (`f56ce8bc-3a86-5c7b-904d-709b101e4612`) lines 547-588 [crates/gcode/src/index/import_resolution/context.rs:547-588]
  - Signature: `pub(super) fn build_swift_local_modules(`
  - Purpose: Extracts unique Swift module names from candidate files by identifying directory components following 'Sources'/'Tests' in the path hierarchy or serving as parent directories, aggregated via parallel iteration. [crates/gcode/src/index/import_resolution/context.rs:547-588]
- `load_dart_external_packages` (function) component `load_dart_external_packages [function]` (`7f4d4363-fe89-51aa-829d-0ee94609faa5`) lines 590-609 [crates/gcode/src/index/import_resolution/context.rs:590-609]
  - Signature: `pub(super) fn load_dart_external_packages(root_path: &Path) -> HashSet<String> {`
  - Purpose: Extracts all non-sdk package dependencies declared in a Dart project's pubspec.yaml file (from dependencies, dev_dependencies, and dependency_overrides fields) and returns them as a HashSet. [crates/gcode/src/index/import_resolution/context.rs:590-609]
- `load_dart_self_package_name` (function) component `load_dart_self_package_name [function]` (`43bc3bfa-f233-500f-a022-b41ea83a5c4d`) lines 611-617 [crates/gcode/src/index/import_resolution/context.rs:611-617]
  - Signature: `pub(super) fn load_dart_self_package_name(root_path: &Path) -> Option<String> {`
  - Purpose: Reads and parses the pubspec.yaml file at the given root path to extract and return the Dart package name as an owned String, or None if the file is not found or lacks a name field. [crates/gcode/src/index/import_resolution/context.rs:611-617]
- `build_elixir_local_module_roots` (function) component `build_elixir_local_module_roots [function]` (`4ce37be2-33ae-5331-82e6-afaa3c389553`) lines 619-655 [crates/gcode/src/index/import_resolution/context.rs:619-655]
  - Signature: `pub(super) fn build_elixir_local_module_roots(candidate_files: &[PathBuf]) -> HashSet<String> {`
  - Purpose: Parses Elixir source files in parallel to extract and deduplicate the root module identifiers from all `defmodule` declarations. [crates/gcode/src/index/import_resolution/context.rs:619-655]
- `load_elixir_external_roots` (function) component `load_elixir_external_roots [function]` (`f6e24e4b-9f00-53b9-9028-0b3b8aaa1497`) lines 657-668 [crates/gcode/src/index/import_resolution/context.rs:657-668]
  - Signature: `pub(super) fn load_elixir_external_roots(root_path: &Path) -> HashMap<String, String> {`
  - Purpose: Collects root paths of Elixir external dependencies and returns them as a HashMap with identity key-value mapping. [crates/gcode/src/index/import_resolution/context.rs:657-668]
- `load_elixir_dependency_names` (function) component `load_elixir_dependency_names [function]` (`41594132-4ef6-50b6-a67b-621a3c3ac5fb`) lines 670-691 [crates/gcode/src/index/import_resolution/context.rs:670-691]
  - Signature: `pub(super) fn load_elixir_dependency_names(root_path: &Path) -> HashSet<String> {`
  - Purpose: Extracts Elixir project dependency names from `mix.exs` and `mix.lock` files using regex pattern matching, returning a deduplicated `HashSet<String>`. [crates/gcode/src/index/import_resolution/context.rs:670-691]
- `elixir_mix_dependency_regex` (function) component `elixir_mix_dependency_regex [function]` (`a6cf91da-e087-5ac1-8fd8-6c64b8313da4`) lines 693-698 [crates/gcode/src/index/import_resolution/context.rs:693-698]
  - Signature: `fn elixir_mix_dependency_regex() -> &'static Regex {`
  - Purpose: Returns a thread-safe, lazily-initialized static regex that matches Elixir atom identifiers immediately following `{:` in Mix dependency declarations. [crates/gcode/src/index/import_resolution/context.rs:693-698]
- `elixir_lock_dependency_regex` (function) component `elixir_lock_dependency_regex [function]` (`1d00d95f-4489-5e2f-b842-bd3c2e0b6b79`) lines 700-706 [crates/gcode/src/index/import_resolution/context.rs:700-706]
  - Signature: `fn elixir_lock_dependency_regex() -> &'static Regex {`
  - Purpose: Returns a lazily-initialized static regex that matches and captures Elixir dependency identifiers from lock file entries with the pattern `"identifier":`. [crates/gcode/src/index/import_resolution/context.rs:700-706]

