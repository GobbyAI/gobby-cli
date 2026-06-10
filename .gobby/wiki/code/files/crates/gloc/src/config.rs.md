---
title: crates/gloc/src/config.rs
type: code_file
provenance:
- file: crates/gloc/src/config.rs
  ranges:
  - 13-22
  - 25-32
  - 34-42
  - 35-41
  - 44-46
  - 48-50
  - 53-65
  - 67-166
  - 70-88
  - 90-100
  - 102-117
  - 120-125
  - 128-159
  - 163-165
  - 170-176
  - 183-188
  - 191-196
  - 199-210
  - 213-217
  - 220-235
  - 238-247
  - 250-254
  - 257-260
  - 263-266
  - 269-278
  - 281-290
  - 293-302
  - 305-316
  - 319-327
  - 330-335
  - 338-345
  - 348-355
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gloc/src/config.rs

Module: [[code/modules/crates/gloc/src|crates/gloc/src]]

## Purpose

`crates/gloc/src/config.rs` exposes 32 indexed API symbols.
[crates/gloc/src/config.rs:13-22]
[crates/gloc/src/config.rs:25-32]
[crates/gloc/src/config.rs:34-42]
[crates/gloc/src/config.rs:35-41]
[crates/gloc/src/config.rs:44-46]
[crates/gloc/src/config.rs:48-50]
[crates/gloc/src/config.rs:53-65]
[crates/gloc/src/config.rs:67-166]
[crates/gloc/src/config.rs:70-88]
[crates/gloc/src/config.rs:90-100]
[crates/gloc/src/config.rs:102-117]
[crates/gloc/src/config.rs:120-125]
[crates/gloc/src/config.rs:128-159]
[crates/gloc/src/config.rs:163-165]
[crates/gloc/src/config.rs:170-176]
[crates/gloc/src/config.rs:183-188]
[crates/gloc/src/config.rs:191-196]
[crates/gloc/src/config.rs:199-210]
[crates/gloc/src/config.rs:213-217]
[crates/gloc/src/config.rs:220-235]
[crates/gloc/src/config.rs:238-247]
[crates/gloc/src/config.rs:250-254]
[crates/gloc/src/config.rs:257-260]
[crates/gloc/src/config.rs:263-266]
[crates/gloc/src/config.rs:269-278]
[crates/gloc/src/config.rs:281-290]
[crates/gloc/src/config.rs:293-302]
[crates/gloc/src/config.rs:305-316]
[crates/gloc/src/config.rs:319-327]
[crates/gloc/src/config.rs:330-335]
[crates/gloc/src/config.rs:338-345]
[crates/gloc/src/config.rs:348-355]

## API Symbols

- `Config` (class) component `Config [class]` (`e4aeb1b6-b112-5577-b443-865dcc440b2c`) lines 13-22 [crates/gloc/src/config.rs:13-22]
  - Signature: `pub struct Config {`
  - Purpose: Indexed class `Config` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:13-22]
- `Settings` (class) component `Settings [class]` (`40246c2c-bc9a-53d2-a5da-24858cd67e6d`) lines 25-32 [crates/gloc/src/config.rs:25-32]
  - Signature: `pub struct Settings {`
  - Purpose: Indexed class `Settings` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:25-32]
- `Settings` (class) component `Settings [class]` (`3b989843-c2da-541d-908d-cf57f4f3759e`) lines 34-42 [crates/gloc/src/config.rs:34-42]
  - Signature: `impl Default for Settings {`
  - Purpose: Indexed class `Settings` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:34-42]
- `Settings.default` (method) component `Settings.default [method]` (`0de5951d-2ed3-58aa-905b-800fd4e0804b`) lines 35-41 [crates/gloc/src/config.rs:35-41]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `Settings.default` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:35-41]
- `default_probe_timeout_ms` (function) component `default_probe_timeout_ms [function]` (`123761e3-1ee3-58ad-9298-11ac7b82103f`) lines 44-46 [crates/gloc/src/config.rs:44-46]
  - Signature: `fn default_probe_timeout_ms() -> u64 {`
  - Purpose: Indexed function `default_probe_timeout_ms` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:44-46]
- `default_auto_load` (function) component `default_auto_load [function]` (`89009b7e-536e-522d-a4a2-2cefee9baad0`) lines 48-50 [crates/gloc/src/config.rs:48-50]
  - Signature: `fn default_auto_load() -> bool {`
  - Purpose: Indexed function `default_auto_load` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:48-50]
- `Client` (class) component `Client [class]` (`ec61d699-24de-5049-8e7c-7d3fc8ae4d8d`) lines 53-65 [crates/gloc/src/config.rs:53-65]
  - Signature: `pub struct Client {`
  - Purpose: Indexed class `Client` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:53-65]
- `Config` (class) component `Config [class]` (`c5648d9d-918e-5b51-bb23-0cca54761e20`) lines 67-166 [crates/gloc/src/config.rs:67-166]
  - Signature: `impl Config {`
  - Purpose: Indexed class `Config` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:67-166]
- `Config.load` (method) component `Config.load [method]` (`1ca7c657-fd0e-526a-857b-2eca445f719b`) lines 70-88 [crates/gloc/src/config.rs:70-88]
  - Signature: `pub fn load(config_override: Option<&Path>) -> Self {`
  - Purpose: Indexed method `Config.load` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:70-88]
- `Config.try_load` (method) component `Config.try_load [method]` (`11880536-a723-50de-accb-ec46b5e68789`) lines 90-100 [crates/gloc/src/config.rs:90-100]
  - Signature: `fn try_load(path: &Path) -> Option<Self> {`
  - Purpose: Indexed method `Config.try_load` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:90-100]
- `Config.load_or_exit` (method) component `Config.load_or_exit [method]` (`e8915c05-78b6-51bf-b6f4-9807ea9616f2`) lines 102-117 [crates/gloc/src/config.rs:102-117]
  - Signature: `fn load_or_exit(path: &Path) -> Self {`
  - Purpose: Indexed method `Config.load_or_exit` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:102-117]
- `Config.resolve_alias` (method) component `Config.resolve_alias [method]` (`14c1e7aa-fa81-5f57-8123-4aaddcaccdac`) lines 120-125 [crates/gloc/src/config.rs:120-125]
  - Signature: `pub fn resolve_alias(&self, model: &str) -> String {`
  - Purpose: Indexed method `Config.resolve_alias` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:120-125]
- `Config.dump` (method) component `Config.dump [method]` (`2801df61-3b74-5451-94f2-92579d68917f`) lines 128-159 [crates/gloc/src/config.rs:128-159]
  - Signature: `pub fn dump(&self) -> String {`
  - Purpose: Indexed method `Config.dump` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:128-159]
- `Config.load_builtin` (method) component `Config.load_builtin [method]` (`cdeb6423-fbd5-59e1-ba4a-e97c91fe6fb1`) lines 163-165 [crates/gloc/src/config.rs:163-165]
  - Signature: `pub fn load_builtin() -> Self {`
  - Purpose: Indexed method `Config.load_builtin` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:163-165]
- `resolve_template` (function) component `resolve_template [function]` (`4b437605-9873-5a6e-b484-6cad6b6310aa`) lines 170-176 [crates/gloc/src/config.rs:170-176]
  - Signature: `pub fn resolve_template(template: &str, backend: &Backend, model: &str) -> String {`
  - Purpose: Indexed function `resolve_template` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:170-176]
- `test_load_default_config` (function) component `test_load_default_config [function]` (`cbca34e6-8444-57c8-9ba1-a32e0818b04e`) lines 183-188 [crates/gloc/src/config.rs:183-188]
  - Signature: `fn test_load_default_config() {`
  - Purpose: Indexed function `test_load_default_config` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:183-188]
- `test_default_config_has_backends` (function) component `test_default_config_has_backends [function]` (`0d424988-0203-56c1-ba0c-9e706a5f4a30`) lines 191-196 [crates/gloc/src/config.rs:191-196]
  - Signature: `fn test_default_config_has_backends() {`
  - Purpose: Indexed function `test_default_config_has_backends` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:191-196]
- `test_backend_fields` (function) component `test_backend_fields [function]` (`c08aca9d-a7b3-555a-9ec0-5e5c65703cfb`) lines 199-210 [crates/gloc/src/config.rs:199-210]
  - Signature: `fn test_backend_fields() {`
  - Purpose: Indexed function `test_backend_fields` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:199-210]
- `test_default_config_has_clients` (function) component `test_default_config_has_clients [function]` (`c2e6a01d-d40a-53a0-a091-106e834bafab`) lines 213-217 [crates/gloc/src/config.rs:213-217]
  - Signature: `fn test_default_config_has_clients() {`
  - Purpose: Indexed function `test_default_config_has_clients` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:213-217]
- `test_claude_client_env` (function) component `test_claude_client_env [function]` (`97cf4d3f-ecfc-57c1-9ede-199a7b1891b9`) lines 220-235 [crates/gloc/src/config.rs:220-235]
  - Signature: `fn test_claude_client_env() {`
  - Purpose: Indexed function `test_claude_client_env` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:220-235]
- `test_codex_client_env` (function) component `test_codex_client_env [function]` (`7f874d50-c295-5597-aea3-b431859f3931`) lines 238-247 [crates/gloc/src/config.rs:238-247]
  - Signature: `fn test_codex_client_env() {`
  - Purpose: Indexed function `test_codex_client_env` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:238-247]
- `test_default_config_has_aliases` (function) component `test_default_config_has_aliases [function]` (`06a4c4b3-e6a9-5401-a000-d8439866d03e`) lines 250-254 [crates/gloc/src/config.rs:250-254]
  - Signature: `fn test_default_config_has_aliases() {`
  - Purpose: Indexed function `test_default_config_has_aliases` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:250-254]
- `test_resolve_alias_hit` (function) component `test_resolve_alias_hit [function]` (`b01c369a-ed84-5408-9712-5553f83b9ad2`) lines 257-260 [crates/gloc/src/config.rs:257-260]
  - Signature: `fn test_resolve_alias_hit() {`
  - Purpose: Indexed function `test_resolve_alias_hit` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:257-260]
- `test_resolve_alias_miss` (function) component `test_resolve_alias_miss [function]` (`f927f447-87d2-5b5f-bcf6-273687eb7cfd`) lines 263-266 [crates/gloc/src/config.rs:263-266]
  - Signature: `fn test_resolve_alias_miss() {`
  - Purpose: Indexed function `test_resolve_alias_miss` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:263-266]
- `test_resolve_template_all_vars` (function) component `test_resolve_template_all_vars [function]` (`977cecda-12b9-5c6d-98cf-513eddffe657`) lines 269-278 [crates/gloc/src/config.rs:269-278]
  - Signature: `fn test_resolve_template_all_vars() {`
  - Purpose: Indexed function `test_resolve_template_all_vars` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:269-278]
- `test_resolve_template_auth_token` (function) component `test_resolve_template_auth_token [function]` (`8677cf28-7bcd-5ecb-b423-987ef0315d20`) lines 281-290 [crates/gloc/src/config.rs:281-290]
  - Signature: `fn test_resolve_template_auth_token() {`
  - Purpose: Indexed function `test_resolve_template_auth_token` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:281-290]
- `test_resolve_template_model` (function) component `test_resolve_template_model [function]` (`2f9bfc66-80a9-5c4b-ba32-8d9432fc8190`) lines 293-302 [crates/gloc/src/config.rs:293-302]
  - Signature: `fn test_resolve_template_model() {`
  - Purpose: Indexed function `test_resolve_template_model` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:293-302]
- `test_resolve_template_no_vars` (function) component `test_resolve_template_no_vars [function]` (`06d0529f-e596-549c-bbd1-f788368ec7ab`) lines 305-316 [crates/gloc/src/config.rs:305-316]
  - Signature: `fn test_resolve_template_no_vars() {`
  - Purpose: Indexed function `test_resolve_template_no_vars` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:305-316]
- `test_resolve_template_empty` (function) component `test_resolve_template_empty [function]` (`3c04ef55-d208-53a5-9262-f642a9163304`) lines 319-327 [crates/gloc/src/config.rs:319-327]
  - Signature: `fn test_resolve_template_empty() {`
  - Purpose: Indexed function `test_resolve_template_empty` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:319-327]
- `test_settings_default` (function) component `test_settings_default [function]` (`c2874e82-2998-5f9a-88e7-7b7f14d171df`) lines 330-335 [crates/gloc/src/config.rs:330-335]
  - Signature: `fn test_settings_default() {`
  - Purpose: Indexed function `test_settings_default` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:330-335]
- `test_dump_contains_key_sections` (function) component `test_dump_contains_key_sections [function]` (`7a2ed3f7-835c-5239-97e7-cd391c748e7b`) lines 338-345 [crates/gloc/src/config.rs:338-345]
  - Signature: `fn test_dump_contains_key_sections() {`
  - Purpose: Indexed function `test_dump_contains_key_sections` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:338-345]
- `test_config_from_valid_override` (function) component `test_config_from_valid_override [function]` (`8958b812-3eed-53a5-a1f7-d7bf21c21b0d`) lines 348-355 [crates/gloc/src/config.rs:348-355]
  - Signature: `fn test_config_from_valid_override() {`
  - Purpose: Indexed function `test_config_from_valid_override` in `crates/gloc/src/config.rs`. [crates/gloc/src/config.rs:348-355]

