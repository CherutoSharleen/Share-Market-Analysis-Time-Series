# Time-Filtered Event Search

This mini project demonstrates date-range filtering followed by keyword-overlap ranking for fictional market events.

## Run

```bash
cd retrieval_timeseries
python -c "from pathlib import Path; from time_filter_search import search_events; print(search_events(Path('events.json'), 'policy bank', '2026-01-01', '2026-01-10'))"
```

## Test

```bash
cd retrieval_timeseries
python -m unittest test_time_filter_search.py
```

All event headlines are synthetic.
