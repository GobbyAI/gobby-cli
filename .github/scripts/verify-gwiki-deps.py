#!/usr/bin/env python3
"""Validate gobby-wiki release dependency preconditions."""

import sys
import tomllib
from pathlib import Path


def error(message: str) -> None:
    print(f"::error::{message}", file=sys.stderr)


def main() -> int:
    manifest = tomllib.loads(Path("crates/gwiki/Cargo.toml").read_text())
    features = manifest.get("features", {})
    default_features = features.get("default", [])
    ai_features = features.get("ai", [])
    dependency = manifest.get("dependencies", {}).get("gobby-core")

    if not isinstance(dependency, dict):
        error("gobby-wiki must depend on gobby-core with an explicit version.")
        return 1

    core_version = dependency.get("version")
    if not core_version:
        error("gobby-wiki's gobby-core dependency must include a crates.io version.")
        return 1

    if "ai" not in default_features:
        error("gobby-wiki default features must include ai for release builds.")
        return 1

    if "gobby-core/ai" not in ai_features:
        error("gobby-wiki's ai feature must enable gobby-core/ai.")
        return 1

    print(core_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
