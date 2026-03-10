from __future__ import annotations

from pathlib import Path

from time_filter_search import search_events


def main() -> None:
    base = Path(__file__).resolve().parent
    query = input("Query terms: ").strip()
    start = input("Start date (YYYY-MM-DD): ").strip()
    end = input("End date (YYYY-MM-DD): ").strip()
    results = search_events(base / "events.json", query, start, end)
    for item in results:
        print(f"- {item['date']}: {item['headline']}")


if __name__ == "__main__":
    main()
