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
| `AiContext` | class | 'AiContext' is a public struct that aggregates AI system configuration comprising variable bindings, tuning parameters, a rate limiter, and an optional project identifier. [crates/gcore/src/ai_context.rs:25-30] |
| `AiContext::resolve` | method | Instantiates 'Self' by delegating to 'resolve_with_options' with the provided 'ConfigSource' and optional 'project_id', using default 'AiContextOptions'. [crates/gcore/src/ai_context.rs:34-36] |
| `AiContext::resolve_with_options` | method | Constructs an 'AiContext' by resolving AI bindings and tuning configuration from a 'ConfigSource', applying routing options (either disabling AI or forcing a specified routing), enforcing minimum concurrency of 1, and instantiating an 'AiLimiter'. [crates/gcore/src/ai_context.rs:39-64] |
| `AiContext::binding` | method | Returns a reference to a 'CapabilityBinding' retrieved from the internal bindings collection using the provided 'AiCapability' as a key. [crates/gcore/src/ai_context.rs:66-68] |
| `AiContextOptions` | class | # Summary 'AiContextOptions' is a configuration struct that provides a boolean flag to disable AI processing and an optional field to override routing behavior with a specific 'AiRouting' variant. [crates/gcore/src/ai_context.rs:73-76] |
| `AiBindings` | class | 'AiBindings' is a struct that groups five 'CapabilityBinding' fields corresponding to distinct AI operations: embedding, audio transcription, audio translation, vision extraction, and text generation. [crates/gcore/src/ai_context.rs:80-86] |
| `AiBindings::resolve` | method | Constructs and returns a Self instance by resolving five AI capability bindings (Embed, AudioTranscribe, AudioTranslate, VisionExtract, TextGenerate) from the provided ConfigSource trait implementation. [crates/gcore/src/ai_context.rs:89-97] |
| `AiBindings::get` | method | Returns an immutable reference to the 'CapabilityBinding' field corresponding to the given 'AiCapability' enum variant via pattern matching. [crates/gcore/src/ai_context.rs:99-107] |
| `AiBindings::get_mut` | method | Returns a mutable reference to the 'CapabilityBinding' field corresponding to the specified 'AiCapability' enum variant. [crates/gcore/src/ai_context.rs:109-117] |
| `AiBindings::force_routing` | method | This method assigns the provided 'AiRouting' value to the 'routing' field of every capability in the collection. [crates/gcore/src/ai_context.rs:119-123] |
| `route` | function | This function retrieves and returns the 'AiRouting' configuration for a specified 'AiCapability' by accessing its binding within the provided 'AiContext'. [crates/gcore/src/ai_context.rs:127-129] |
| `AiLimiter` | class | 'AiLimiter' is a thread-safe wrapper struct that provides shared access to rate limiting functionality through an atomically reference-counted ('Arc') inner implementation. [crates/gcore/src/ai_context.rs:133-135] |
| `LimiterInner` | class | 'LimiterInner' is a thread-safe semaphore-like structure that maintains a maximum resource capacity and current active count protected by a mutex, with a condition variable for signaling resource availability to waiting threads. [crates/gcore/src/ai_context.rs:137-141] |
| `AiLimiter::new` | method | Creates a new concurrency limiter with an atomically reference-counted inner state initialized with a maximum concurrency threshold (clamped to at least 1), a mutex-protected active counter starting at 0, and a condition variable for thread synchronization. [crates/gcore/src/ai_context.rs:144-152] |
| `AiLimiter::max_concurrency` | method | This method returns the maximum concurrency limit as a 'u8' by accessing the 'max' field of the inner struct. [crates/gcore/src/ai_context.rs:154-156] |
| `AiLimiter::acquire` | method | This method blocks until the active permit count is below the maximum threshold, then increments the count and returns an 'AiPermit' that holds a reference to the shared internal state. [crates/gcore/src/ai_context.rs:158-175] |
| `AiLimiter::try_acquire` | method | Atomically increments a shared active permit counter if below the maximum limit, returning 'Some(AiPermit)' on success or 'None' if at capacity. [crates/gcore/src/ai_context.rs:177-190] |
| `AiLimiter::fmt` | method | Implements the 'Debug' trait for 'AiLimiter' by formatting it as a debug struct containing the 'max_concurrency' field while suppressing exhaustive field enumeration via 'finish_non_exhaustive()'. [crates/gcore/src/ai_context.rs:194-198] |
| `AiPermit` | class | AiPermit is a thread-safe, reference-counted wrapper struct that encapsulates a LimiterInner instance via Arc for managing rate-limited access permissions. [crates/gcore/src/ai_context.rs:203-205] |
| `AiPermit::drop` | method | Decrements a mutex-protected active counter via saturating subtraction and notifies one waiting thread on a condition variable. [crates/gcore/src/ai_context.rs:208-216] |
| `LimiterInner::fmt` | method | This method implements the 'Debug' trait to format a 'LimiterInner' struct by displaying the 'max' field and marking remaining fields as non-exhaustive. [crates/gcore/src/ai_context.rs:220-224] |
| `AiConfigSource` | class | 'AiConfigSource' is a generic struct that encapsulates an optional primary configuration of a parameterized type P (defaulting to 'NoPrimaryAiConfigSource') or an optional 'StandaloneConfig', providing flexible configuration source composition. [crates/gcore/src/ai_context.rs:232-235] |
| `LocalAiConfigSource` | type | Indexed type `LocalAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:237] |
| `LocalAiConfigSource::from_gobby_home` | method | Constructs a new instance by reading a 'StandaloneConfig' from a path derived from the provided 'gobby_home' directory and initializing it with 'NoPrimaryAiConfigSource'. [crates/gcore/src/ai_context.rs:240-245] |

_23 more symbol(s) not shown — run `gcode outline crates/gcore/src/ai_context.rs` for the full list._

_Verified by 9 in-file unit tests._

