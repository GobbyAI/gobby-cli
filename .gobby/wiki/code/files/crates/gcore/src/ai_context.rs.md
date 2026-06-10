---
title: crates/gcore/src/ai_context.rs
type: code_file
provenance:
- file: crates/gcore/src/ai_context.rs
  ranges:
  - 25-30
  - 32-69
  - 34-36
  - 39-64
  - 66-68
  - 73-76
  - 80-86
  - 88-124
  - 89-97
  - 99-107
  - 109-117
  - 119-123
  - 134-145
  - 148-155
  - 158-160
  - 164-166
  - 168-172
  - 174-222
  - 175-183
  - 185-187
  - 189-206
  - 208-221
  - 224-230
  - 225-229
  - 234-236
  - 238-248
  - 239-247
  - 250-256
  - 251-255
  - 263-266
  - '268'
  - 270-277
  - 271-276
  - 283-288
  - 290-298
  - 305-314
  - 316-327
  - '332'
  - 334-345
  - 335-337
  - 339-344
  - 349-353
  - 360-366
  - 368-370
  - 378-393
  - 395-400
  - 404-411
  - 425-428
  - 430-451
  - 431-439
  - 441-450
  - 453-464
  - 454-456
  - 458-463
  - 466-469
  - 471-483
  - 472-482
  - 485-489
  - 486-488
  - 491-495
  - 497-509
  - 512-565
  - 568-588
  - 591-619
  - 622-646
  - 649-660
  - 663-722
  - 725-747
  - 750-781
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/ai_context.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

`crates/gcore/src/ai_context.rs` exposes 69 indexed API symbols.
[crates/gcore/src/ai_context.rs:25-30]
[crates/gcore/src/ai_context.rs:32-69]
[crates/gcore/src/ai_context.rs:34-36]
[crates/gcore/src/ai_context.rs:39-64]
[crates/gcore/src/ai_context.rs:66-68]
[crates/gcore/src/ai_context.rs:73-76]
[crates/gcore/src/ai_context.rs:80-86]
[crates/gcore/src/ai_context.rs:88-124]
[crates/gcore/src/ai_context.rs:89-97]
[crates/gcore/src/ai_context.rs:99-107]
[crates/gcore/src/ai_context.rs:109-117]
[crates/gcore/src/ai_context.rs:119-123]
[crates/gcore/src/ai_context.rs:134-145]
[crates/gcore/src/ai_context.rs:148-155]
[crates/gcore/src/ai_context.rs:158-160]
[crates/gcore/src/ai_context.rs:164-166]
[crates/gcore/src/ai_context.rs:168-172]
[crates/gcore/src/ai_context.rs:174-222]
[crates/gcore/src/ai_context.rs:175-183]
[crates/gcore/src/ai_context.rs:185-187]
[crates/gcore/src/ai_context.rs:189-206]
[crates/gcore/src/ai_context.rs:208-221]
[crates/gcore/src/ai_context.rs:224-230]
[crates/gcore/src/ai_context.rs:225-229]
[crates/gcore/src/ai_context.rs:234-236]
[crates/gcore/src/ai_context.rs:238-248]
[crates/gcore/src/ai_context.rs:239-247]
[crates/gcore/src/ai_context.rs:250-256]
[crates/gcore/src/ai_context.rs:251-255]
[crates/gcore/src/ai_context.rs:263-266]
[crates/gcore/src/ai_context.rs:268]
[crates/gcore/src/ai_context.rs:270-277]
[crates/gcore/src/ai_context.rs:271-276]
[crates/gcore/src/ai_context.rs:283-288]
[crates/gcore/src/ai_context.rs:290-298]
[crates/gcore/src/ai_context.rs:305-314]
[crates/gcore/src/ai_context.rs:316-327]
[crates/gcore/src/ai_context.rs:332]
[crates/gcore/src/ai_context.rs:334-345]
[crates/gcore/src/ai_context.rs:335-337]
[crates/gcore/src/ai_context.rs:339-344]
[crates/gcore/src/ai_context.rs:349-353]
[crates/gcore/src/ai_context.rs:360-366]
[crates/gcore/src/ai_context.rs:368-370]
[crates/gcore/src/ai_context.rs:378-393]
[crates/gcore/src/ai_context.rs:395-400]
[crates/gcore/src/ai_context.rs:404-411]
[crates/gcore/src/ai_context.rs:425-428]
[crates/gcore/src/ai_context.rs:430-451]
[crates/gcore/src/ai_context.rs:431-439]
[crates/gcore/src/ai_context.rs:441-450]
[crates/gcore/src/ai_context.rs:453-464]
[crates/gcore/src/ai_context.rs:454-456]
[crates/gcore/src/ai_context.rs:458-463]
[crates/gcore/src/ai_context.rs:466-469]
[crates/gcore/src/ai_context.rs:471-483]
[crates/gcore/src/ai_context.rs:472-482]
[crates/gcore/src/ai_context.rs:485-489]
[crates/gcore/src/ai_context.rs:486-488]
[crates/gcore/src/ai_context.rs:491-495]
[crates/gcore/src/ai_context.rs:497-509]
[crates/gcore/src/ai_context.rs:512-565]
[crates/gcore/src/ai_context.rs:568-588]
[crates/gcore/src/ai_context.rs:591-619]
[crates/gcore/src/ai_context.rs:622-646]
[crates/gcore/src/ai_context.rs:649-660]
[crates/gcore/src/ai_context.rs:663-722]
[crates/gcore/src/ai_context.rs:725-747]
[crates/gcore/src/ai_context.rs:750-781]

## API Symbols

- `AiContext` (class) component `AiContext [class]` (`9cb3af3a-c7c3-5ec7-b482-816bea1f7727`) lines 25-30 [crates/gcore/src/ai_context.rs:25-30]
  - Signature: `pub struct AiContext {`
  - Purpose: Indexed class `AiContext` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:25-30]
- `AiContext` (class) component `AiContext [class]` (`147039af-17e6-5ed4-8147-8d24dfbf4f57`) lines 32-69 [crates/gcore/src/ai_context.rs:32-69]
  - Signature: `impl AiContext {`
  - Purpose: Indexed class `AiContext` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:32-69]
- `AiContext.resolve` (method) component `AiContext.resolve [method]` (`543c6e4c-5951-5f9d-810e-3c9ab1aa0fff`) lines 34-36 [crates/gcore/src/ai_context.rs:34-36]
  - Signature: `pub fn resolve(project_id: Option<String>, source: &mut impl ConfigSource) -> Self {`
  - Purpose: Indexed method `AiContext.resolve` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:34-36]
- `AiContext.resolve_with_options` (method) component `AiContext.resolve_with_options [method]` (`cc539a47-3f27-5fa5-a72a-f327d3a3ce93`) lines 39-64 [crates/gcore/src/ai_context.rs:39-64]
  - Signature: `pub fn resolve_with_options(`
  - Purpose: Indexed method `AiContext.resolve_with_options` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:39-64]
- `AiContext.binding` (method) component `AiContext.binding [method]` (`05991622-c709-52b7-bfc3-1d680970d380`) lines 66-68 [crates/gcore/src/ai_context.rs:66-68]
  - Signature: `pub fn binding(&self, capability: AiCapability) -> &CapabilityBinding {`
  - Purpose: Indexed method `AiContext.binding` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:66-68]
- `AiContextOptions` (class) component `AiContextOptions [class]` (`a81e31b4-fe5b-52e0-be99-d24cc4a5a7ab`) lines 73-76 [crates/gcore/src/ai_context.rs:73-76]
  - Signature: `pub struct AiContextOptions {`
  - Purpose: Indexed class `AiContextOptions` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:73-76]
- `AiBindings` (class) component `AiBindings [class]` (`acf8fbbc-105a-545c-a2f0-0f8f661e2ba4`) lines 80-86 [crates/gcore/src/ai_context.rs:80-86]
  - Signature: `pub struct AiBindings {`
  - Purpose: Indexed class `AiBindings` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:80-86]
- `AiBindings` (class) component `AiBindings [class]` (`62ecfb40-d7fe-5750-a466-153cfb5e3671`) lines 88-124 [crates/gcore/src/ai_context.rs:88-124]
  - Signature: `impl AiBindings {`
  - Purpose: Indexed class `AiBindings` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:88-124]
- `AiBindings.resolve` (method) component `AiBindings.resolve [method]` (`5c8f63f4-7954-5438-8450-61873d8e140a`) lines 89-97 [crates/gcore/src/ai_context.rs:89-97]
  - Signature: `pub fn resolve(source: &mut impl ConfigSource) -> Self {`
  - Purpose: Indexed method `AiBindings.resolve` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:89-97]
- `AiBindings.get` (method) component `AiBindings.get [method]` (`bd7b2126-a8e1-594e-b8d9-41aa41f38490`) lines 99-107 [crates/gcore/src/ai_context.rs:99-107]
  - Signature: `pub fn get(&self, capability: AiCapability) -> &CapabilityBinding {`
  - Purpose: Indexed method `AiBindings.get` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:99-107]
- `AiBindings.get_mut` (method) component `AiBindings.get_mut [method]` (`0b3b383f-beba-5c40-8cb5-833c1cd75da3`) lines 109-117 [crates/gcore/src/ai_context.rs:109-117]
  - Signature: `fn get_mut(&mut self, capability: AiCapability) -> &mut CapabilityBinding {`
  - Purpose: Indexed method `AiBindings.get_mut` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:109-117]
- `AiBindings.force_routing` (method) component `AiBindings.force_routing [method]` (`f19b04be-248e-5f82-8498-1733cf29a5df`) lines 119-123 [crates/gcore/src/ai_context.rs:119-123]
  - Signature: `fn force_routing(&mut self, routing: AiRouting) {`
  - Purpose: Indexed method `AiBindings.force_routing` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:119-123]
- `apply_discovered_local_backend` (function) component `apply_discovered_local_backend [function]` (`2e8c4c47-6e0f-5acf-8cfa-85fb25d451d9`) lines 134-145 [crates/gcore/src/ai_context.rs:134-145]
  - Signature: `pub(crate) fn apply_discovered_local_backend(`
  - Purpose: Indexed function `apply_discovered_local_backend` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:134-145]
- `binding_needs_local_api_base` (function) component `binding_needs_local_api_base [function]` (`1d93d156-4b53-5db0-9328-ce5ba04fac22`) lines 148-155 [crates/gcore/src/ai_context.rs:148-155]
  - Signature: `fn binding_needs_local_api_base(binding: &CapabilityBinding) -> bool {`
  - Purpose: Indexed function `binding_needs_local_api_base` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:148-155]
- `route` (function) component `route [function]` (`68034a1a-6673-51b6-bb4c-de2623bcfe0b`) lines 158-160 [crates/gcore/src/ai_context.rs:158-160]
  - Signature: `pub fn route(context: &AiContext, capability: AiCapability) -> AiRouting {`
  - Purpose: Indexed function `route` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:158-160]
- `AiLimiter` (class) component `AiLimiter [class]` (`97bea2bf-f588-56de-b826-d953fb39cab6`) lines 164-166 [crates/gcore/src/ai_context.rs:164-166]
  - Signature: `pub struct AiLimiter {`
  - Purpose: Indexed class `AiLimiter` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:164-166]
- `LimiterInner` (class) component `LimiterInner [class]` (`2c084d85-bc72-5699-a5d4-c175a2307c96`) lines 168-172 [crates/gcore/src/ai_context.rs:168-172]
  - Signature: `struct LimiterInner {`
  - Purpose: Indexed class `LimiterInner` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:168-172]
- `AiLimiter` (class) component `AiLimiter [class]` (`ed0da3fc-a501-57fe-aba1-8ad2992e1e12`) lines 174-222 [crates/gcore/src/ai_context.rs:174-222]
  - Signature: `impl AiLimiter {`
  - Purpose: Indexed class `AiLimiter` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:174-222]
- `AiLimiter.new` (method) component `AiLimiter.new [method]` (`a61c640b-ba7c-5286-93d3-f5d4c88096ef`) lines 175-183 [crates/gcore/src/ai_context.rs:175-183]
  - Signature: `pub fn new(max_concurrency: u8) -> Self {`
  - Purpose: Indexed method `AiLimiter.new` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:175-183]
- `AiLimiter.max_concurrency` (method) component `AiLimiter.max_concurrency [method]` (`ad1fa252-aa1d-55c5-9223-1f5cc69cb882`) lines 185-187 [crates/gcore/src/ai_context.rs:185-187]
  - Signature: `pub fn max_concurrency(&self) -> u8 {`
  - Purpose: Indexed method `AiLimiter.max_concurrency` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:185-187]
- `AiLimiter.acquire` (method) component `AiLimiter.acquire [method]` (`334b5127-21db-5412-9630-e1d10f9defd5`) lines 189-206 [crates/gcore/src/ai_context.rs:189-206]
  - Signature: `pub fn acquire(&self) -> AiPermit {`
  - Purpose: Indexed method `AiLimiter.acquire` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:189-206]
- `AiLimiter.try_acquire` (method) component `AiLimiter.try_acquire [method]` (`e21292aa-55d3-5dc4-968f-ea8d05663e91`) lines 208-221 [crates/gcore/src/ai_context.rs:208-221]
  - Signature: `pub fn try_acquire(&self) -> Option<AiPermit> {`
  - Purpose: Indexed method `AiLimiter.try_acquire` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:208-221]
- `AiLimiter` (class) component `AiLimiter [class]` (`085a9662-b917-58ba-9b35-a73b5ffd38c5`) lines 224-230 [crates/gcore/src/ai_context.rs:224-230]
  - Signature: `impl std::fmt::Debug for AiLimiter {`
  - Purpose: Indexed class `AiLimiter` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:224-230]
- `AiLimiter.fmt` (method) component `AiLimiter.fmt [method]` (`fb09f5fe-f258-5884-9133-ba71763f075d`) lines 225-229 [crates/gcore/src/ai_context.rs:225-229]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Indexed method `AiLimiter.fmt` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:225-229]
- `AiPermit` (class) component `AiPermit [class]` (`409bcbe2-1ac0-56a5-9fcb-cc1d5ac25a1a`) lines 234-236 [crates/gcore/src/ai_context.rs:234-236]
  - Signature: `pub struct AiPermit {`
  - Purpose: Indexed class `AiPermit` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:234-236]
- `AiPermit` (class) component `AiPermit [class]` (`2e6636ba-7367-5379-81e9-29ba04acd732`) lines 238-248 [crates/gcore/src/ai_context.rs:238-248]
  - Signature: `impl Drop for AiPermit {`
  - Purpose: Indexed class `AiPermit` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:238-248]
- `AiPermit.drop` (method) component `AiPermit.drop [method]` (`9bae624d-5653-5758-9fef-f9efbd0b57b8`) lines 239-247 [crates/gcore/src/ai_context.rs:239-247]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `AiPermit.drop` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:239-247]
- `LimiterInner` (class) component `LimiterInner [class]` (`9f4b8dff-09ad-59fa-ba9b-1231a7614c5c`) lines 250-256 [crates/gcore/src/ai_context.rs:250-256]
  - Signature: `impl std::fmt::Debug for LimiterInner {`
  - Purpose: Indexed class `LimiterInner` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:250-256]
- `LimiterInner.fmt` (method) component `LimiterInner.fmt [method]` (`d26dd629-9b30-5621-8146-fc8ac3cd0c61`) lines 251-255 [crates/gcore/src/ai_context.rs:251-255]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Indexed method `LimiterInner.fmt` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:251-255]
- `AiConfigSource` (class) component `AiConfigSource [class]` (`007b2077-b5cf-57e4-84ad-b9831ef20152`) lines 263-266 [crates/gcore/src/ai_context.rs:263-266]
  - Signature: `pub struct AiConfigSource<P = NoPrimaryAiConfigSource> {`
  - Purpose: Indexed class `AiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:263-266]
- `LocalAiConfigSource` (type) component `LocalAiConfigSource [type]` (`97e9be81-060c-51fd-bf40-e15ff3af5748`) lines 268-268 [crates/gcore/src/ai_context.rs:268]
  - Signature: `pub type LocalAiConfigSource = AiConfigSource<NoPrimaryAiConfigSource>;`
  - Purpose: Indexed type `LocalAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:268]
- `LocalAiConfigSource` (class) component `LocalAiConfigSource [class]` (`2c9057e6-af0c-57e6-8917-d7b402a7edae`) lines 270-277 [crates/gcore/src/ai_context.rs:270-277]
  - Signature: `impl LocalAiConfigSource {`
  - Purpose: Indexed class `LocalAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:270-277]
- `LocalAiConfigSource.from_gobby_home` (method) component `LocalAiConfigSource.from_gobby_home [method]` (`755dc7ec-8f39-51f4-b10f-5fef4247d84e`) lines 271-276 [crates/gcore/src/ai_context.rs:271-276]
  - Signature: `pub fn from_gobby_home(gobby_home: &std::path::Path) -> anyhow::Result<Self> {`
  - Purpose: Indexed method `LocalAiConfigSource.from_gobby_home` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:271-276]
- `with_primary` (function) component `with_primary [function]` (`2c7292ca-f998-51e2-9153-2174af1ee602`) lines 283-288 [crates/gcore/src/ai_context.rs:283-288]
  - Signature: `pub fn with_primary(primary: P, standalone: Option<StandaloneConfig>) -> Self {`
  - Purpose: Indexed function `with_primary` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:283-288]
- `with_primary_from_gobby_home` (function) component `with_primary_from_gobby_home [function]` (`a15de566-2149-573a-a954-6216505f7f9e`) lines 290-298 [crates/gcore/src/ai_context.rs:290-298]
  - Signature: `pub fn with_primary_from_gobby_home(`
  - Purpose: Indexed function `with_primary_from_gobby_home` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:290-298]
- `config_value` (function) component `config_value [function]` (`b1e29bdc-ebc0-5a3f-a355-42a69034e3b1`) lines 305-314 [crates/gcore/src/ai_context.rs:305-314]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed function `config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:305-314]
- `resolve_value` (function) component `resolve_value [function]` (`8ae75b1d-743c-5b64-bee4-79c50a36c58f`) lines 316-327 [crates/gcore/src/ai_context.rs:316-327]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:316-327]
- `NoPrimaryAiConfigSource` (class) component `NoPrimaryAiConfigSource [class]` (`33f1467b-eb75-5f29-9dc0-618dde7d10bb`) lines 332-332 [crates/gcore/src/ai_context.rs:332]
  - Signature: `pub struct NoPrimaryAiConfigSource;`
  - Purpose: Indexed class `NoPrimaryAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:332]
- `NoPrimaryAiConfigSource` (class) component `NoPrimaryAiConfigSource [class]` (`3c7707d1-52cf-54fa-b0bb-94e96eaf66a8`) lines 334-345 [crates/gcore/src/ai_context.rs:334-345]
  - Signature: `impl ConfigSource for NoPrimaryAiConfigSource {`
  - Purpose: Indexed class `NoPrimaryAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:334-345]
- `NoPrimaryAiConfigSource.config_value` (method) component `NoPrimaryAiConfigSource.config_value [method]` (`9912b151-e272-5571-b335-cf5ee091ac7e`) lines 335-337 [crates/gcore/src/ai_context.rs:335-337]
  - Signature: `fn config_value(&mut self, _key: &str) -> Option<String> {`
  - Purpose: Indexed method `NoPrimaryAiConfigSource.config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:335-337]
- `NoPrimaryAiConfigSource.resolve_value` (method) component `NoPrimaryAiConfigSource.resolve_value [method]` (`655919de-fec3-50f0-802a-f60b40f3866c`) lines 339-344 [crates/gcore/src/ai_context.rs:339-344]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `NoPrimaryAiConfigSource.resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:339-344]
- `PostgresAiConfigSource` (class) component `PostgresAiConfigSource [class]` (`66290f1b-1caf-5763-b78e-30a969a82ff7`) lines 349-353 [crates/gcore/src/ai_context.rs:349-353]
  - Signature: `pub struct PostgresAiConfigSource<'a, R> {`
  - Purpose: Indexed class `PostgresAiConfigSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:349-353]
- `new` (function) component `new [function]` (`aad14da2-21fc-5ea1-ac4b-5cf7ba31537c`) lines 360-366 [crates/gcore/src/ai_context.rs:360-366]
  - Signature: `pub fn new(conn: &'a mut postgres::Client, resolver: R) -> Self {`
  - Purpose: Indexed function `new` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:360-366]
- `config_store_available` (function) component `config_store_available [function]` (`500d8275-4f1b-5dcf-9b93-8517a94f44c7`) lines 368-370 [crates/gcore/src/ai_context.rs:368-370]
  - Signature: `pub fn config_store_available(&self) -> bool {`
  - Purpose: Indexed function `config_store_available` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:368-370]
- `config_value` (function) component `config_value [function]` (`d8aa99a8-62e0-5237-bae3-4fe2a033605e`) lines 378-393 [crates/gcore/src/ai_context.rs:378-393]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed function `config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:378-393]
- `resolve_value` (function) component `resolve_value [function]` (`c9a1fa51-e54c-53fe-b536-fbce33e385ad`) lines 395-400 [crates/gcore/src/ai_context.rs:395-400]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed function `resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:395-400]
- `config_store_missing` (function) component `config_store_missing [function]` (`dfc9e82a-edca-5c3e-b93e-b143ea11a556`) lines 404-411 [crates/gcore/src/ai_context.rs:404-411]
  - Signature: `fn config_store_missing(error: &anyhow::Error) -> bool {`
  - Purpose: Indexed function `config_store_missing` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:404-411]
- `TestSource` (class) component `TestSource [class]` (`73308cb9-59be-5ae2-8e96-f4eff4aa56f8`) lines 425-428 [crates/gcore/src/ai_context.rs:425-428]
  - Signature: `struct TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:425-428]
- `TestSource` (class) component `TestSource [class]` (`7a99f84e-abe2-5946-b2ec-662e6ee14971`) lines 430-451 [crates/gcore/src/ai_context.rs:430-451]
  - Signature: `impl TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:430-451]
- `TestSource.with_values` (method) component `TestSource.with_values [method]` (`4db78557-64f3-5690-b76d-971a431af3f9`) lines 431-439 [crates/gcore/src/ai_context.rs:431-439]
  - Signature: `fn with_values(values: impl IntoIterator<Item = (&'static str, &'static str)>) -> Self {`
  - Purpose: Indexed method `TestSource.with_values` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:431-439]
- `TestSource.with_resolved` (method) component `TestSource.with_resolved [method]` (`a1df831c-6f05-50b2-970a-28ceff68e61e`) lines 441-450 [crates/gcore/src/ai_context.rs:441-450]
  - Signature: `fn with_resolved(`
  - Purpose: Indexed method `TestSource.with_resolved` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:441-450]
- `TestSource` (class) component `TestSource [class]` (`ad3ffc9f-c755-554b-a2ea-4f00b93c4db9`) lines 453-464 [crates/gcore/src/ai_context.rs:453-464]
  - Signature: `impl ConfigSource for TestSource {`
  - Purpose: Indexed class `TestSource` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:453-464]
- `TestSource.config_value` (method) component `TestSource.config_value [method]` (`86320ee3-a044-5f42-b7ea-a6474c0defbd`) lines 454-456 [crates/gcore/src/ai_context.rs:454-456]
  - Signature: `fn config_value(&mut self, key: &str) -> Option<String> {`
  - Purpose: Indexed method `TestSource.config_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:454-456]
- `TestSource.resolve_value` (method) component `TestSource.resolve_value [method]` (`1479772e-ca33-5d2f-ab25-57bbdc9a7732`) lines 458-463 [crates/gcore/src/ai_context.rs:458-463]
  - Signature: `fn resolve_value(&mut self, value: &str) -> anyhow::Result<String> {`
  - Purpose: Indexed method `TestSource.resolve_value` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:458-463]
- `CurrentDirGuard` (class) component `CurrentDirGuard [class]` (`4abaec77-c72b-569a-ba62-ffd2253fef03`) lines 466-469 [crates/gcore/src/ai_context.rs:466-469]
  - Signature: `struct CurrentDirGuard {`
  - Purpose: Indexed class `CurrentDirGuard` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:466-469]
- `CurrentDirGuard` (class) component `CurrentDirGuard [class]` (`7f39f5e9-6599-536a-ab70-262711eca0b3`) lines 471-483 [crates/gcore/src/ai_context.rs:471-483]
  - Signature: `impl CurrentDirGuard {`
  - Purpose: Indexed class `CurrentDirGuard` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:471-483]
- `CurrentDirGuard.set` (method) component `CurrentDirGuard.set [method]` (`0a0b04cf-45a0-598d-b42c-de99f3ca67b5`) lines 472-482 [crates/gcore/src/ai_context.rs:472-482]
  - Signature: `fn set(path: &std::path::Path) -> Self {`
  - Purpose: Indexed method `CurrentDirGuard.set` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:472-482]
- `CurrentDirGuard` (class) component `CurrentDirGuard [class]` (`1780f925-0063-5382-ad50-702752ca4cd8`) lines 485-489 [crates/gcore/src/ai_context.rs:485-489]
  - Signature: `impl Drop for CurrentDirGuard {`
  - Purpose: Indexed class `CurrentDirGuard` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:485-489]
- `CurrentDirGuard.drop` (method) component `CurrentDirGuard.drop [method]` (`53859474-e725-5d37-aef4-4c76ece5505a`) lines 486-488 [crates/gcore/src/ai_context.rs:486-488]
  - Signature: `fn drop(&mut self) {`
  - Purpose: Indexed method `CurrentDirGuard.drop` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:486-488]
- `write_gcore_yaml` (function) component `write_gcore_yaml [function]` (`af37d7c7-944e-549b-9294-cc8a6931d56e`) lines 491-495 [crates/gcore/src/ai_context.rs:491-495]
  - Signature: `fn write_gcore_yaml(home: &std::path::Path, contents: &str) {`
  - Purpose: Indexed function `write_gcore_yaml` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:491-495]
- `binding` (function) component `binding [function]` (`77b37c92-dc33-51f8-a94a-af03e3bc93dc`) lines 497-509 [crates/gcore/src/ai_context.rs:497-509]
  - Signature: `fn binding(routing: AiRouting, api_base: Option<&str>) -> CapabilityBinding {`
  - Purpose: Indexed function `binding` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:497-509]
- `resolves_in_db_and_no_db_modes` (function) component `resolves_in_db_and_no_db_modes [function]` (`be8fba2e-a006-576b-a53e-e83444e3b1c7`) lines 512-565 [crates/gcore/src/ai_context.rs:512-565]
  - Signature: `fn resolves_in_db_and_no_db_modes() {`
  - Purpose: Indexed function `resolves_in_db_and_no_db_modes` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:512-565]
- `project_id_is_caller_supplied` (function) component `project_id_is_caller_supplied [function]` (`729f8e88-0846-5f37-ac07-e51fadea816c`) lines 568-588 [crates/gcore/src/ai_context.rs:568-588]
  - Signature: `fn project_id_is_caller_supplied() {`
  - Purpose: Indexed function `project_id_is_caller_supplied` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:568-588]
- `db_without_config_store_falls_through` (function) component `db_without_config_store_falls_through [function]` (`e3a9e81c-4774-5080-8af1-0bd7cb872c8c`) lines 591-619 [crates/gcore/src/ai_context.rs:591-619]
  - Signature: `fn db_without_config_store_falls_through() {`
  - Purpose: Indexed function `db_without_config_store_falls_through` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:591-619]
- `standalone_values_expand_env_patterns_for_db_fallback` (function) component `standalone_values_expand_env_patterns_for_db_fallback [function]` (`fc31bca9-a390-5d65-a0cd-e2b20e1dc493`) lines 622-646 [crates/gcore/src/ai_context.rs:622-646]
  - Signature: `fn standalone_values_expand_env_patterns_for_db_fallback() {`
  - Purpose: Indexed function `standalone_values_expand_env_patterns_for_db_fallback` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:622-646]
- `concurrency_cap_enforced` (function) component `concurrency_cap_enforced [function]` (`6e6cbf1d-49eb-5db6-b36d-3294b69635dc`) lines 649-660 [crates/gcore/src/ai_context.rs:649-660]
  - Signature: `fn concurrency_cap_enforced() {`
  - Purpose: Indexed function `concurrency_cap_enforced` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:649-660]
- `forced_routing_and_no_ai_override` (function) component `forced_routing_and_no_ai_override [function]` (`dbd3e3b8-34c9-528d-b2d7-8929352a1852`) lines 663-722 [crates/gcore/src/ai_context.rs:663-722]
  - Signature: `fn forced_routing_and_no_ai_override() {`
  - Purpose: Indexed function `forced_routing_and_no_ai_override` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:663-722]
- `resolve_does_not_discover_local_backend_endpoints` (function) component `resolve_does_not_discover_local_backend_endpoints [function]` (`fb71760f-dd92-5a14-9e15-c850180d0aa7`) lines 725-747 [crates/gcore/src/ai_context.rs:725-747]
  - Signature: `fn resolve_does_not_discover_local_backend_endpoints() {`
  - Purpose: Indexed function `resolve_does_not_discover_local_backend_endpoints` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:725-747]
- `stt_not_autodiscovered_to_chat_backend` (function) component `stt_not_autodiscovered_to_chat_backend [function]` (`3847ffac-b9bc-5cc0-92b1-6886e1e6d092`) lines 750-781 [crates/gcore/src/ai_context.rs:750-781]
  - Signature: `fn stt_not_autodiscovered_to_chat_backend() {`
  - Purpose: Indexed function `stt_not_autodiscovered_to_chat_backend` in `crates/gcore/src/ai_context.rs`. [crates/gcore/src/ai_context.rs:750-781]

