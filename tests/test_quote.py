"""Acceptance examples from specs/001-shipping-quote/spec.md."""

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_quote(subtotal: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ROOT / "quote.py"), subtotal],
        capture_output=True,
        text=True,
        check=False,
    )


class QuoteAcceptanceTests(unittest.TestCase):
    def test_below_minimum_fr1_fr2(self) -> None:
        result = run_quote("49")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "shipping=5\ntotal=54\n")

    def test_at_minimum_fr1_fr2(self) -> None:
        result = run_quote("50")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "shipping=0\ntotal=50\n")

    def test_negative_subtotal_fr3(self) -> None:
        result = run_quote("-1")
        self.assertEqual(result.returncode, 2)
        self.assertIn("subtotal must be nonnegative", result.stderr)
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
