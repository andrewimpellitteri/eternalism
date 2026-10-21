"""Rerun the scalar product-BC/MSR/norm-GC certificate.

The operator-level commutativity results are cited from the primary; this
script checks output markers of the scalar seed, not operator equations or
vector general covariance. A nontrivial phase prevents vector path equality.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SEED = ROOT / "research/longshots/bc-nonzero/nonzero_continuation.py"


def main():
    out = subprocess.run([sys.executable, str(SEED)], cwd=ROOT,
                         capture_output=True, text=True, check=True).stdout
    assert "CERTIFICATE: PASS" in out
    assert "cp-plus-top holonomies: [1, 1, (3/5-4/5i)]" in out
    assert "stage-4 BC product equations: 109 checked; failures: 0" in out
    assert "all transition amplitudes nonzero: 49 checked" in out
    print("scalar BCPH seed: 49 nonzero transitions, 109 product-BC equations, PASS")
    print("stage-4 cp-plus-top holonomy: (3-4i)/5")
    print("PASS: scalar product-BC/MSR/norm-GC seed certificate")
    print("Scope: no operator residuals or vector-GC checks in this wrapper.")
    print("The nontrivial phase obstructs primary vector path equality.")


if __name__ == "__main__":
    main()
