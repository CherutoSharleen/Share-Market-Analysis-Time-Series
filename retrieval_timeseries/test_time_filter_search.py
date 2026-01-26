import unittest
from pathlib import Path

from time_filter_search import search_events


class TimeFilterSearchTests(unittest.TestCase):
    def test_range_and_query_filter(self) -> None:
        base = Path(__file__).resolve().parent
        results = search_events(base / "events.json", "policy bank", "2026-01-01", "2026-01-07")
        self.assertGreaterEqual(len(results), 1)
        self.assertIn("policy", results[0]["headline"].lower())


if __name__ == "__main__":
    unittest.main()
