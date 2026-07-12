import unittest
from pathlib import Path

from time_filter_search import available_date_range, search_events, search_events_with_scores


class TimeFilterSearchTests(unittest.TestCase):
    def test_range_and_query_filter(self) -> None:
        base = Path(__file__).resolve().parent
        results = search_events(base / "events.json", "policy bank", "2026-01-01", "2026-01-07")
        self.assertGreaterEqual(len(results), 1)
        self.assertIn("policy", results[0]["headline"].lower())

    def test_top_k_limit(self) -> None:
        base = Path(__file__).resolve().parent
        results = search_events(base / "events.json", "bank", "2026-01-01", "2026-01-31", top_k=1)
        self.assertEqual(len(results), 1)

    def test_available_date_range(self) -> None:
        base = Path(__file__).resolve().parent
        start, end = available_date_range(base / "events.json")
        self.assertLessEqual(start, end)

    def test_search_events_with_scores(self) -> None:
        base = Path(__file__).resolve().parent
        rows = search_events_with_scores(base / "events.json", "bank policy", "2026-01-01", "2026-01-10")
        self.assertGreaterEqual(len(rows), 1)
        self.assertGreaterEqual(rows[0][1], 1)


if __name__ == "__main__":
    unittest.main()
