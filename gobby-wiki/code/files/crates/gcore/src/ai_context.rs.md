---
title: crates/gcore/src/ai_context.rs
type: code_file
provenance:
- file: crates/gcore/src/ai_context.rs
  ranges:
  - 25-30
  - 34-36
  - 39-64
  - 66-68
  - 73-76
  - 80-86
  - 89-97
  - 99-107
  - 109-117
  - 119-123
  - 127-129
  - 133-135
  - 137-141
  - 144-152
  - 154-156
  - 158-175
  - 177-190
  - 194-198
  - 203-205
  - 208-216
  - 220-224
  - 232-235
  - '237'
  - 240-245
  - 252-257
  - 259-267
  - 274-283
  - 285-296
  - 299-302
  - '306'
  - 309-311
  - 313-318
  - 323-327
  - 334-340
  - 342-344
  - 352-367
  - 369-374
  - 378-385
  - 399-402
  - 405-413
  - 415-424
  - 428-430
  - 432-437
  - 440-443
  - 446-456
  - 460-462
  - 465-469
  - 472-525
  - 528-548
  - 551-579
  - 582-606
  - 609-625
  - 628-637
  - 640-651
  - 654-713
  - 716-738
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/ai_context.rs:25-30](crates/gcore/src/ai_context.rs#L25-L30), [crates/gcore/src/ai_context.rs:34-36](crates/gcore/src/ai_context.rs#L34-L36), [crates/gcore/src/ai_context.rs:39-64](crates/gcore/src/ai_context.rs#L39-L64), [crates/gcore/src/ai_context.rs:66-68](crates/gcore/src/ai_context.rs#L66-L68), [crates/gcore/src/ai_context.rs:73-76](crates/gcore/src/ai_context.rs#L73-L76), [crates/gcore/src/ai_context.rs:80-86](crates/gcore/src/ai_context.rs#L80-L86), [crates/gcore/src/ai_context.rs:89-97](crates/gcore/src/ai_context.rs#L89-L97), [crates/gcore/src/ai_context.rs:99-107](crates/gcore/src/ai_context.rs#L99-L107), [crates/gcore/src/ai_context.rs:109-117](crates/gcore/src/ai_context.rs#L109-L117), [crates/gcore/src/ai_context.rs:119-123](crates/gcore/src/ai_context.rs#L119-L123), [crates/gcore/src/ai_context.rs:127-129](crates/gcore/src/ai_context.rs#L127-L129), [crates/gcore/src/ai_context.rs:133-135](crates/gcore/src/ai_context.rs#L133-L135), [crates/gcore/src/ai_context.rs:137-141](crates/gcore/src/ai_context.rs#L137-L141), [crates/gcore/src/ai_context.rs:144-152](crates/gcore/src/ai_context.rs#L144-L152), [crates/gcore/src/ai_context.rs:154-156](crates/gcore/src/ai_context.rs#L154-L156), [crates/gcore/src/ai_context.rs:158-175](crates/gcore/src/ai_context.rs#L158-L175), [crates/gcore/src/ai_context.rs:177-190](crates/gcore/src/ai_context.rs#L177-L190), [crates/gcore/src/ai_context.rs:194-198](crates/gcore/src/ai_context.rs#L194-L198), [crates/gcore/src/ai_context.rs:203-205](crates/gcore/src/ai_context.rs#L203-L205), [crates/gcore/src/ai_context.rs:208-216](crates/gcore/src/ai_context.rs#L208-L216), [crates/gcore/src/ai_context.rs:220-224](crates/gcore/src/ai_context.rs#L220-L224), [crates/gcore/src/ai_context.rs:232-235](crates/gcore/src/ai_context.rs#L232-L235), [crates/gcore/src/ai_context.rs:237](crates/gcore/src/ai_context.rs#L237), [crates/gcore/src/ai_context.rs:240-245](crates/gcore/src/ai_context.rs#L240-L245), [crates/gcore/src/ai_context.rs:252-257](crates/gcore/src/ai_context.rs#L252-L257), [crates/gcore/src/ai_context.rs:259-267](crates/gcore/src/ai_context.rs#L259-L267), [crates/gcore/src/ai_context.rs:274-283](crates/gcore/src/ai_context.rs#L274-L283), [crates/gcore/src/ai_context.rs:285-296](crates/gcore/src/ai_context.rs#L285-L296), [crates/gcore/src/ai_context.rs:299-302](crates/gcore/src/ai_context.rs#L299-L302), [crates/gcore/src/ai_context.rs:306](crates/gcore/src/ai_context.rs#L306), [crates/gcore/src/ai_context.rs:309-311](crates/gcore/src/ai_context.rs#L309-L311), [crates/gcore/src/ai_context.rs:313-318](crates/gcore/src/ai_context.rs#L313-L318), [crates/gcore/src/ai_context.rs:323-327](crates/gcore/src/ai_context.rs#L323-L327), [crates/gcore/src/ai_context.rs:334-340](crates/gcore/src/ai_context.rs#L334-L340), [crates/gcore/src/ai_context.rs:342-344](crates/gcore/src/ai_context.rs#L342-L344), [crates/gcore/src/ai_context.rs:352-367](crates/gcore/src/ai_context.rs#L352-L367), [crates/gcore/src/ai_context.rs:369-374](crates/gcore/src/ai_context.rs#L369-L374), [crates/gcore/src/ai_context.rs:378-385](crates/gcore/src/ai_context.rs#L378-L385), [crates/gcore/src/ai_context.rs:399-402](crates/gcore/src/ai_context.rs#L399-L402), [crates/gcore/src/ai_context.rs:405-413](crates/gcore/src/ai_context.rs#L405-L413), [crates/gcore/src/ai_context.rs:415-424](crates/gcore/src/ai_context.rs#L415-L424), [crates/gcore/src/ai_context.rs:428-430](crates/gcore/src/ai_context.rs#L428-L430), [crates/gcore/src/ai_context.rs:432-437](crates/gcore/src/ai_context.rs#L432-L437), [crates/gcore/src/ai_context.rs:440-443](crates/gcore/src/ai_context.rs#L440-L443), [crates/gcore/src/ai_context.rs:446-456](crates/gcore/src/ai_context.rs#L446-L456), [crates/gcore/src/ai_context.rs:460-462](crates/gcore/src/ai_context.rs#L460-L462), [crates/gcore/src/ai_context.rs:465-469](crates/gcore/src/ai_context.rs#L465-L469), [crates/gcore/src/ai_context.rs:472-525](crates/gcore/src/ai_context.rs#L472-L525), [crates/gcore/src/ai_context.rs:528-548](crates/gcore/src/ai_context.rs#L528-L548), [crates/gcore/src/ai_context.rs:551-579](crates/gcore/src/ai_context.rs#L551-L579), [crates/gcore/src/ai_context.rs:582-606](crates/gcore/src/ai_context.rs#L582-L606), [crates/gcore/src/ai_context.rs:609-625](crates/gcore/src/ai_context.rs#L609-L625), [crates/gcore/src/ai_context.rs:628-637](crates/gcore/src/ai_context.rs#L628-L637), [crates/gcore/src/ai_context.rs:640-651](crates/gcore/src/ai_context.rs#L640-L651), [crates/gcore/src/ai_context.rs:654-713](crates/gcore/src/ai_context.rs#L654-L713), [crates/gcore/src/ai_context.rs:716-738](crates/gcore/src/ai_context.rs#L716-L738)

</details>

# crates/gcore/src/ai_context.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

This file builds a transport-free AI context layer that resolves per-capability bindings, tuning, a concurrency limiter, and an optional project ID from caller-provided config sources. `AiContext` is the public resolved bundle, `resolve`/`resolve_with_options` assemble it, and `AiContextOptions` lets callers override routing for a command, including forcing a route or disabling AI entirely. `AiBindings` and the config-source types implement the layered lookup and routing fallback logic, while `AiLimiter` and `AiPermit` enforce the configured concurrency cap. The remaining helpers and tests cover local and Postgres-backed config resolution, environment-variable expansion, current-directory handling, and edge cases like missing config stores or forced routing.
[crates/gcore/src/ai_context.rs:25-30]
[crates/gcore/src/ai_context.rs:34-36]
[crates/gcore/src/ai_context.rs:39-64]
[crates/gcore/src/ai_context.rs:66-68]
[crates/gcore/src/ai_context.rs:73-76]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `AiContext` | class | `pub struct AiContext {` | `AiContext [class]` | `9cb3af3a-c7c3-5ec7-b482-816bea1f7727` | 25-30 [crates/gcore/src/ai_context.rs:25-30] | Indexed class `AiContext` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:25-30] |
| `AiContext::resolve` | method | `pub fn resolve(project_id: Option<String>, source: &mut impl ConfigSource) -> Self {` | `AiContext::resolve [method]` | `543c6e4c-5951-5f9d-810e-3c9ab1aa0fff` | 34-36 [crates/gcore/src/ai_context.rs:34-36] | Indexed method `AiContext::resolve` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:34-36] |
| `AiContext::resolve_with_options` | method | `pub fn resolve_with_options(` | `AiContext::resolve_with_options [method]` | `cc539a47-3f27-5fa5-a72a-f327d3a3ce93` | 39-64 [crates/gcore/src/ai_context.rs:39-64] | Indexed method `AiContext::resolve_with_options` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:39-64] |
| `AiContext::binding` | method | `pub fn binding(&self, capability: AiCapability) -> &CapabilityBinding {` | `AiContext::binding [method]` | `05991622-c709-52b7-bfc3-1d680970d380` | 66-68 [crates/gcore/src/ai_context.rs:66-68] | Indexed method `AiContext::binding` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:66-68] |
| `AiContextOptions` | class | `pub struct AiContextOptions {` | `AiContextOptions [class]` | `a81e31b4-fe5b-52e0-be99-d24cc4a5a7ab` | 73-76 [crates/gcore/src/ai_context.rs:73-76] | Indexed class `AiContextOptions` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:73-76] |
| `AiBindings` | class | `pub struct AiBindings {` | `AiBindings [class]` | `acf8fbbc-105a-545c-a2f0-0f8f661e2ba4` | 80-86 [crates/gcore/src/ai_context.rs:80-86] | Indexed class `AiBindings` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:80-86] |
| `AiBindings::resolve` | method | `pub fn resolve(source: &mut impl ConfigSource) -> Self {` | `AiBindings::resolve [method]` | `5c8f63f4-7954-5438-8450-61873d8e140a` | 89-97 [crates/gcore/src/ai_context.rs:89-97] | Indexed method `AiBindings::resolve` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:89-97] |
| `AiBindings::get` | method | `pub fn get(&self, capability: AiCapability) -> &CapabilityBinding {` | `AiBindings::get [method]` | `bd7b2126-a8e1-594e-b8d9-41aa41f38490` | 99-107 [crates/gcore/src/ai_context.rs:99-107] | Indexed method `AiBindings::get` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:99-107] |
| `AiBindings::get_mut` | method | `fn get_mut(&mut self, capability: AiCapability) -> &mut CapabilityBinding {` | `AiBindings::get_mut [method]` | `0b3b383f-beba-5c40-8cb5-833c1cd75da3` | 109-117 [crates/gcore/src/ai_context.rs:109-117] | Indexed method `AiBindings::get_mut` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:109-117] |
| `AiBindings::force_routing` | method | `fn force_routing(&mut self, routing: AiRouting) {` | `AiBindings::force_routing [method]` | `f19b04be-248e-5f82-8498-1733cf29a5df` | 119-123 [crates/gcore/src/ai_context.rs:119-123] | Indexed method `AiBindings::force_routing` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:119-123] |
| `route` | function | `pub fn route(context: &AiContext, capability: AiCapability) -> AiRouting {` | `route [function]` | `f9cc5895-1a74-5134-9fb9-4c51a62fc5c8` | 127-129 [crates/gcore/src/ai_context.rs:127-129] | Indexed function `route` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:127-129] |
| `AiLimiter` | class | `pub struct AiLimiter {` | `AiLimiter [class]` | `2d3bf6de-7689-5f9c-b32e-7360e08a5d6d` | 133-135 [crates/gcore/src/ai_context.rs:133-135] | Indexed class `AiLimiter` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:133-135] |
| `LimiterInner` | class | `struct LimiterInner {` | `LimiterInner [class]` | `fd8fbf30-3f51-5682-ad2a-e5c6c9364d73` | 137-141 [crates/gcore/src/ai_context.rs:137-141] | Indexed class `LimiterInner` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:137-141] |
| `AiLimiter::new` | method | `pub fn new(max_concurrency: u8) -> Self {` | `AiLimiter::new [method]` | `38beadea-7d61-5662-8437-555f650a45e8` | 144-152 [crates/gcore/src/ai_context.rs:144-152] | Indexed method `AiLimiter::new` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:144-152] |
| `AiLimiter::max_concurrency` | method | `pub fn max_concurrency(&self) -> u8 {` | `AiLimiter::max_concurrency [method]` | `45f15780-62dd-5724-a665-062d96156831` | 154-156 [crates/gcore/src/ai_context.rs:154-156] | Indexed method `AiLimiter::max_concurrency` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:154-156] |
| `AiLimiter::acquire` | method | `pub fn acquire(&self) -> AiPermit {` | `AiLimiter::acquire [method]` | `248d1930-dae8-524a-855e-5264dfc043c3` | 158-175 [crates/gcore/src/ai_context.rs:158-175] | Indexed method `AiLimiter::acquire` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:158-175] |
| `AiLimiter::try_acquire` | method | `pub fn try_acquire(&self) -> Option<AiPermit> {` | `AiLimiter::try_acquire [method]` | `6ca4a1fe-457d-54b6-af03-8a95e2b6d03c` | 177-190 [crates/gcore/src/ai_context.rs:177-190] | Indexed method `AiLimiter::try_acquire` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:177-190] |
| `AiLimiter::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `AiLimiter::fmt [method]` | `2a323b19-8b51-53fa-a59e-a58176f151ad` | 194-198 [crates/gcore/src/ai_context.rs:194-198] | Indexed method `AiLimiter::fmt` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:194-198] |
| `AiPermit` | class | `pub struct AiPermit {` | `AiPermit [class]` | `2ac94163-b6a5-5e17-9138-b75414246fa8` | 203-205 [crates/gcore/src/ai_context.rs:203-205] | Indexed class `AiPermit` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:203-205] |
| `AiPermit::drop` | method | `fn drop(&mut self) {` | `AiPermit::drop [method]` | `4932fbaa-a771-518f-840d-f685fc85f165` | 208-216 [crates/gcore/src/ai_context.rs:208-216] | Indexed method `AiPermit::drop` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:208-216] |
| `LimiterInner::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `LimiterInner::fmt [method]` | `98ea6271-079b-5af6-9b45-4a12bedc3975` | 220-224 [crates/gcore/src/ai_context.rs:220-224] | Indexed method `LimiterInner::fmt` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:220-224] |
| `AiConfigSource` | class | `pub struct AiConfigSource<P = NoPrimaryAiConfigSource> {` | `AiConfigSource [class]` | `bd857dc0-004a-5f25-9b35-ce4ce4178e0c` | 232-235 [crates/gcore/src/ai_context.rs:232-235] | Indexed class `AiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:232-235] |
| `LocalAiConfigSource` | type | `pub type LocalAiConfigSource = AiConfigSource<NoPrimaryAiConfigSource>;` | `LocalAiConfigSource [type]` | `176c1c0d-5e5b-557d-93ae-becf1053e71a` | 237-237 [crates/gcore/src/ai_context.rs:237] | Indexed type `LocalAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:237] |
| `LocalAiConfigSource::from_gobby_home` | method | `pub fn from_gobby_home(gobby_home: &std::path::Path) -> anyhow::Result<Self> {` | `LocalAiConfigSource::from_gobby_home [method]` | `8acc1edc-5ddc-5f41-92c9-1782a15a1de0` | 240-245 [crates/gcore/src/ai_context.rs:240-245] | Indexed method `LocalAiConfigSource::from_gobby_home` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:240-245] |
| `with_primary` | function | `pub fn with_primary(primary: P, standalone: Option<StandaloneConfig>) -> Self {` | `with_primary [function]` | `268a6175-f9c6-5fc5-8b0d-f65411eb6b4d` | 252-257 [crates/gcore/src/ai_context.rs:252-257] | Indexed function `with_primary` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:252-257] |
| `with_primary_from_gobby_home` | function | `pub fn with_primary_from_gobby_home(` | `with_primary_from_gobby_home [function]` | `4b40c228-dec3-5c7a-9d27-c7d0a2cf85af` | 259-267 [crates/gcore/src/ai_context.rs:259-267] | Indexed function `with_primary_from_gobby_home` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:259-267] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> Option<String> {` | `config_value [function]` | `a9483997-eb41-52b8-9e2c-f9a44500708a` | 274-283 [crates/gcore/src/ai_context.rs:274-283] | Indexed function `config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:274-283] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `89914207-4755-5423-a822-a60f147afd5c` | 285-296 [crates/gcore/src/ai_context.rs:285-296] | Indexed function `resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:285-296] |
| `resolve_non_secret_config_value` | function | `fn resolve_non_secret_config_value(value: &str) -> anyhow::Result<String> {` | `resolve_non_secret_config_value [function]` | `ffdffb45-ed2c-5d18-89f6-c0e246792a88` | 299-302 [crates/gcore/src/ai_context.rs:299-302] | Indexed function `resolve_non_secret_config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:299-302] |
| `NoPrimaryAiConfigSource` | class | `pub struct NoPrimaryAiConfigSource;` | `NoPrimaryAiConfigSource [class]` | `937575ba-b908-5c74-933b-3baa94e944dd` | 306-306 [crates/gcore/src/ai_context.rs:306] | Indexed class `NoPrimaryAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:306] |
| `NoPrimaryAiConfigSource::config_value` | method | `fn config_value(&mut self, _key: &str) -> Option<String> {` | `NoPrimaryAiConfigSource::config_value [method]` | `89b3df5c-a3c7-5975-9705-6729a6a4e69c` | 309-311 [crates/gcore/src/ai_context.rs:309-311] | Indexed method `NoPrimaryAiConfigSource::config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:309-311] |
| `NoPrimaryAiConfigSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `NoPrimaryAiConfigSource::resolve_value [method]` | `37b6f051-f2ff-5438-b074-9a3c22d7b0e5` | 313-318 [crates/gcore/src/ai_context.rs:313-318] | Indexed method `NoPrimaryAiConfigSource::resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:313-318] |
| `PostgresAiConfigSource` | class | `pub struct PostgresAiConfigSource<'a, R> {` | `PostgresAiConfigSource [class]` | `65af52db-c019-5bfd-a82c-00acb6935125` | 323-327 [crates/gcore/src/ai_context.rs:323-327] | Indexed class `PostgresAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:323-327] |
| `new` | function | `pub fn new(conn: &'a mut postgres::Client, resolver: R) -> Self {` | `new [function]` | `eaa41882-95bb-5e27-9fb5-e41a20d61d52` | 334-340 [crates/gcore/src/ai_context.rs:334-340] | Indexed function `new` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:334-340] |
| `config_store_available` | function | `pub fn config_store_available(&self) -> bool {` | `config_store_available [function]` | `178051a0-486b-5ac7-a085-cbc0156bc2d6` | 342-344 [crates/gcore/src/ai_context.rs:342-344] | Indexed function `config_store_available` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:342-344] |
| `config_value` | function | `fn config_value(&mut self, key: &str) -> Option<String> {` | `config_value [function]` | `21bea21d-8323-59b8-86bf-f7744fdc437d` | 352-367 [crates/gcore/src/ai_context.rs:352-367] | Indexed function `config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:352-367] |
| `resolve_value` | function | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `resolve_value [function]` | `517efd84-6cf4-52c3-85e8-11678e20469e` | 369-374 [crates/gcore/src/ai_context.rs:369-374] | Indexed function `resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:369-374] |
| `config_store_missing` | function | `fn config_store_missing(error: &anyhow::Error) -> bool {` | `config_store_missing [function]` | `6fc0dffd-0efb-5912-b786-0604f311b686` | 378-385 [crates/gcore/src/ai_context.rs:378-385] | Indexed function `config_store_missing` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:378-385] |
| `TestSource` | class | `struct TestSource {` | `TestSource [class]` | `63738309-b8d3-550b-94b9-8f85f02b3700` | 399-402 [crates/gcore/src/ai_context.rs:399-402] | Indexed class `TestSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:399-402] |
| `TestSource::with_values` | method | `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {` | `TestSource::with_values [method]` | `71ac913a-8aa3-5304-93bb-e4fac7206865` | 405-413 [crates/gcore/src/ai_context.rs:405-413] | Indexed method `TestSource::with_values` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:405-413] |
| `TestSource::with_resolved` | method | `fn with_resolved(` | `TestSource::with_resolved [method]` | `b2398108-d4ac-5456-8e11-7ae37442e46b` | 415-424 [crates/gcore/src/ai_context.rs:415-424] | Indexed method `TestSource::with_resolved` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:415-424] |
| `TestSource::config_value` | method | `fn config_value(&mut self, key: &str) -> Option<String> {` | `TestSource::config_value [method]` | `4da6442c-3fc5-59c2-9aed-70e443be421b` | 428-430 [crates/gcore/src/ai_context.rs:428-430] | Indexed method `TestSource::config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:428-430] |
| `TestSource::resolve_value` | method | `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {` | `TestSource::resolve_value [method]` | `05dfcbbc-d4af-59c1-a08f-caf2bae73f7a` | 432-437 [crates/gcore/src/ai_context.rs:432-437] | Indexed method `TestSource::resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:432-437] |
| `CurrentDirGuard` | class | `struct CurrentDirGuard {` | `CurrentDirGuard [class]` | `6c511941-78f7-5c5f-8588-069a8acefbbd` | 440-443 [crates/gcore/src/ai_context.rs:440-443] | Indexed class `CurrentDirGuard` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:440-443] |
| `CurrentDirGuard::set` | method | `fn set(path: &std::path::Path) -> Self {` | `CurrentDirGuard::set [method]` | `4c97e7c9-1600-5df7-a8f3-a658110b6d3f` | 446-456 [crates/gcore/src/ai_context.rs:446-456] | Indexed method `CurrentDirGuard::set` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:446-456] |
| `CurrentDirGuard::drop` | method | `fn drop(&mut self) {` | `CurrentDirGuard::drop [method]` | `83756c15-a24c-5a67-b668-fb0182e0ffd9` | 460-462 [crates/gcore/src/ai_context.rs:460-462] | Indexed method `CurrentDirGuard::drop` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:460-462] |
| `write_gcore_yaml` | function | `fn write_gcore_yaml(home: &std::path::Path, contents: &str) {` | `write_gcore_yaml [function]` | `97409b44-4b42-5d21-a798-ce9f79c7abf5` | 465-469 [crates/gcore/src/ai_context.rs:465-469] | Indexed function `write_gcore_yaml` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:465-469] |
| `resolves_in_db_and_no_db_modes` | function | `fn resolves_in_db_and_no_db_modes() {` | `resolves_in_db_and_no_db_modes [function]` | `b5c62105-1262-551f-8ad7-8f323be1ad70` | 472-525 [crates/gcore/src/ai_context.rs:472-525] | Indexed function `resolves_in_db_and_no_db_modes` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:472-525] |
| `project_id_is_caller_supplied` | function | `fn project_id_is_caller_supplied() {` | `project_id_is_caller_supplied [function]` | `80b0ae17-e2ed-5a94-a19c-3a67746ddfb0` | 528-548 [crates/gcore/src/ai_context.rs:528-548] | Indexed function `project_id_is_caller_supplied` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:528-548] |
| `db_without_config_store_falls_through` | function | `fn db_without_config_store_falls_through() {` | `db_without_config_store_falls_through [function]` | `698c3f61-f5c1-58d5-a04f-da46d1328523` | 551-579 [crates/gcore/src/ai_context.rs:551-579] | Indexed function `db_without_config_store_falls_through` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:551-579] |
| `standalone_values_expand_env_patterns_for_db_fallback` | function | `fn standalone_values_expand_env_patterns_for_db_fallback() {` | `standalone_values_expand_env_patterns_for_db_fallback [function]` | `89c925ba-21bc-5291-96c3-2866e4c748ab` | 582-606 [crates/gcore/src/ai_context.rs:582-606] | Indexed function `standalone_values_expand_env_patterns_for_db_fallback` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:582-606] |
| `primary_only_values_expand_env_patterns_without_standalone` | function | `fn primary_only_values_expand_env_patterns_without_standalone() {` | `primary_only_values_expand_env_patterns_without_standalone [function]` | `8cd50233-8f6d-5df4-82d0-6763a06de334` | 609-625 [crates/gcore/src/ai_context.rs:609-625] | Indexed function `primary_only_values_expand_env_patterns_without_standalone` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:609-625] |
| `no_primary_source_expands_env_patterns` | function | `fn no_primary_source_expands_env_patterns() {` | `no_primary_source_expands_env_patterns [function]` | `de346316-e272-5152-a8e9-2ba20c8494dd` | 628-637 [crates/gcore/src/ai_context.rs:628-637] | Indexed function `no_primary_source_expands_env_patterns` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:628-637] |
| `concurrency_cap_enforced` | function | `fn concurrency_cap_enforced() {` | `concurrency_cap_enforced [function]` | `c05cad91-d97a-54fe-81bb-fa473765a7d0` | 640-651 [crates/gcore/src/ai_context.rs:640-651] | Indexed function `concurrency_cap_enforced` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:640-651] |
| `forced_routing_and_no_ai_override` | function | `fn forced_routing_and_no_ai_override() {` | `forced_routing_and_no_ai_override [function]` | `08fd4c75-b4c1-5483-83fd-0d8baf82bf70` | 654-713 [crates/gcore/src/ai_context.rs:654-713] | Indexed function `forced_routing_and_no_ai_override` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:654-713] |
| `resolve_does_not_discover_local_backend_endpoints` | function | `fn resolve_does_not_discover_local_backend_endpoints() {` | `resolve_does_not_discover_local_backend_endpoints [function]` | `ec54efe4-4777-50c2-a4f7-83bad9a02209` | 716-738 [crates/gcore/src/ai_context.rs:716-738] | Indexed function `resolve_does_not_discover_local_backend_endpoints` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:716-738] |
