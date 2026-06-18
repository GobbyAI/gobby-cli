---
title: crates/gcore/src/ai_context.rs
type: code_file
provenance:
- file: crates/gcore/src/ai_context.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai_context.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/ai_context.rs` exposes 56 indexed API symbols.

## How it fits

`crates/gcore/src/ai_context.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `AiContext` | class | Indexed class `AiContext` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:25-30] |
| `AiContext::resolve` | method | Indexed method `AiContext::resolve` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:34-36] |
| `AiContext::resolve_with_options` | method | Indexed method `AiContext::resolve_with_options` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:39-64] |
| `AiContext::binding` | method | Indexed method `AiContext::binding` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:66-68] |
| `AiContextOptions` | class | Indexed class `AiContextOptions` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:73-76] |
| `AiBindings` | class | Indexed class `AiBindings` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:80-86] |
| `AiBindings::resolve` | method | Indexed method `AiBindings::resolve` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:89-97] |
| `AiBindings::get` | method | Indexed method `AiBindings::get` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:99-107] |
| `AiBindings::get_mut` | method | Indexed method `AiBindings::get_mut` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:109-117] |
| `AiBindings::force_routing` | method | Indexed method `AiBindings::force_routing` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:119-123] |
| `route` | function | Indexed function `route` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:127-129] |
| `AiLimiter` | class | Indexed class `AiLimiter` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:133-135] |
| `LimiterInner` | class | Indexed class `LimiterInner` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:137-141] |
| `AiLimiter::new` | method | Indexed method `AiLimiter::new` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:144-152] |
| `AiLimiter::max_concurrency` | method | Indexed method `AiLimiter::max_concurrency` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:154-156] |
| `AiLimiter::acquire` | method | Indexed method `AiLimiter::acquire` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:158-175] |
| `AiLimiter::try_acquire` | method | Indexed method `AiLimiter::try_acquire` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:177-190] |
| `AiLimiter::fmt` | method | Indexed method `AiLimiter::fmt` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:194-198] |
| `AiPermit` | class | Indexed class `AiPermit` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:203-205] |
| `AiPermit::drop` | method | Indexed method `AiPermit::drop` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:208-216] |
| `LimiterInner::fmt` | method | Indexed method `LimiterInner::fmt` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:220-224] |
| `AiConfigSource` | class | Indexed class `AiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:232-235] |
| `LocalAiConfigSource` | type | Indexed type `LocalAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:237] |
| `LocalAiConfigSource::from_gobby_home` | method | Indexed method `LocalAiConfigSource::from_gobby_home` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:240-245] |
| `with_primary` | function | Indexed function `with_primary` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:252-257] |
| `with_primary_from_gobby_home` | function | Indexed function `with_primary_from_gobby_home` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:259-267] |
| `config_value` | function | Indexed function `config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:274-283] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:285-296] |
| `resolve_non_secret_config_value` | function | Indexed function `resolve_non_secret_config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:299-302] |
| `NoPrimaryAiConfigSource` | class | Indexed class `NoPrimaryAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:306] |
| `NoPrimaryAiConfigSource::config_value` | method | Indexed method `NoPrimaryAiConfigSource::config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:309-311] |
| `NoPrimaryAiConfigSource::resolve_value` | method | Indexed method `NoPrimaryAiConfigSource::resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:313-318] |
| `PostgresAiConfigSource` | class | Indexed class `PostgresAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:323-327] |
| `new` | function | Indexed function `new` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:334-340] |
| `config_store_available` | function | Indexed function `config_store_available` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:342-344] |
| `config_value` | function | Indexed function `config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:352-367] |
| `resolve_value` | function | Indexed function `resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:369-374] |
| `config_store_missing` | function | Indexed function `config_store_missing` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:378-385] |
| `TestSource` | class | Indexed class `TestSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:399-402] |
| `TestSource::with_values` | method | Indexed method `TestSource::with_values` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:405-413] |
| `TestSource::with_resolved` | method | Indexed method `TestSource::with_resolved` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:415-424] |
| `TestSource::config_value` | method | Indexed method `TestSource::config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:428-430] |
| `TestSource::resolve_value` | method | Indexed method `TestSource::resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:432-437] |
| `CurrentDirGuard` | class | Indexed class `CurrentDirGuard` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:440-443] |
| `CurrentDirGuard::set` | method | Indexed method `CurrentDirGuard::set` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:446-456] |
| `CurrentDirGuard::drop` | method | Indexed method `CurrentDirGuard::drop` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:460-462] |
| `write_gcore_yaml` | function | Indexed function `write_gcore_yaml` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:465-469] |
| `resolves_in_db_and_no_db_modes` | function | Indexed function `resolves_in_db_and_no_db_modes` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:472-525] |
| `project_id_is_caller_supplied` | function | Indexed function `project_id_is_caller_supplied` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:528-548] |
| `db_without_config_store_falls_through` | function | Indexed function `db_without_config_store_falls_through` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:551-579] |
| `standalone_values_expand_env_patterns_for_db_fallback` | function | Indexed function `standalone_values_expand_env_patterns_for_db_fallback` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:582-606] |
| `primary_only_values_expand_env_patterns_without_standalone` | function | Indexed function `primary_only_values_expand_env_patterns_without_standalone` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:609-625] |
| `no_primary_source_expands_env_patterns` | function | Indexed function `no_primary_source_expands_env_patterns` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:628-637] |
| `concurrency_cap_enforced` | function | Indexed function `concurrency_cap_enforced` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:640-651] |
| `forced_routing_and_no_ai_override` | function | Indexed function `forced_routing_and_no_ai_override` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:654-713] |
| `resolve_does_not_discover_local_backend_endpoints` | function | Indexed function `resolve_does_not_discover_local_backend_endpoints` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:716-738] |

