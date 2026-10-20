#!/usr/bin/env bash
# Reproducible checks for the selected complex-percolation certificate.
# No Lean, no mathlib, no dependency installs.
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== Toolchain =="
LEAN_BIN="${LEAN_BIN:-}"
if [ -z "$LEAN_BIN" ]; then
  if command -v lean >/dev/null 2>&1; then
    LEAN_BIN="lean"
  elif [ -x "$HOME/.elan/bin/lean" ]; then
    LEAN_BIN="$HOME/.elan/bin/lean"
  fi
fi
if [ -n "$LEAN_BIN" ]; then
  "$LEAN_BIN" --version
else
  echo "lean: absent (see formal/INFEASIBILITY.md)"
fi

echo
echo "== Light Lean kernel =="
if [ -n "$LEAN_BIN" ]; then
  "$LEAN_BIN" formal/lean/Certificate.lean
else
  echo "skipped: no lean toolchain"
fi

echo
echo "== Baseline unit tests =="
(cd experiments/baseline && python3 -m unittest test_poscau)

echo
echo "== Exact finite certificate and Fig. 6/7 reproduction =="
python3 experiments/baseline/reproduce.py

echo
echo "== Independent fresh-audit script =="
python3 research/creative/proof-audit/verify_small.py

echo
echo "== Dirac countermodel =="
python3 experiments/extensions/countermodel.py

echo
echo "== Changed-assumption boundary =="
python3 experiments/extensions/boundary.py

echo
echo "== Source hashes =="
shasum -a 256 \
  research/creative/RESULT.md \
  research/creative/COVARIANT_RESULT.md \
  research/creative/proof-audit/AUDIT.md \
  experiments/baseline/poscau.py \
  experiments/baseline/reproduce.py \
  experiments/extensions/countermodel.py
