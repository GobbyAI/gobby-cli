#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE' >&2
Usage: scripts/verify.sh [build|unit_tests|doc_tests|format|lint ...]

With no arguments, runs all checks.
USAGE
}

run_check() {
  case "$1" in
    build)
      cargo build --workspace --no-default-features
      ;;
    unit_tests)
      cargo nextest run --workspace --no-default-features
      ;;
    doc_tests)
      cargo test --doc --workspace --no-default-features
      ;;
    format)
      cargo fmt --all --check
      ;;
    lint)
      cargo clippy --workspace --no-default-features -- -D warnings
      ;;
    -h | --help | help)
      usage
      exit 0
      ;;
    *)
      usage
      echo "unknown check: $1" >&2
      exit 2
      ;;
  esac
}

if [ "$#" -eq 0 ]; then
  set -- build unit_tests doc_tests format lint
fi

for check in "$@"; do
  run_check "$check"
done
