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

`crates/gcore/src/ai_context.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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

_23 more symbol(s) not shown — run `gcode outline crates/gcore/src/ai_context.rs` for the full list._

_Verified by 9 in-file unit tests._

