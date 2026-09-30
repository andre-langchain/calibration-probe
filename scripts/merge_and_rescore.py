"""Merge a re-run backend into results/probe.json, re-score every row with one confidence
definition, and regenerate every report. Model calls happen only in `calibration-probe run`;
this script is offline.

    uv run python scripts/merge_and_rescore.py [path/to/rerun/probe.json ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from calibration_probe.probe import rescore_rows, summarise
from calibration_probe.report import items_markdown, summary_markdown, write_xlsx

ROOT = Path(__file__).resolve().parent.parent
main_path = ROOT / "results/probe.json"
results = json.loads(main_path.read_text(encoding="utf-8"))
for extra in sys.argv[1:]:
    for spec, res in json.loads(Path(extra).read_text(encoding="utf-8")).items():
        results[spec] = res  # replaces the old entry for that backend, order kept
for res in results.values():
    rescore_rows(res["rows"])
    res["summary"] = summarise(res["rows"])
main_path.write_text(json.dumps(results, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
(ROOT / "results/SUMMARY.md").write_text(summary_markdown(results), encoding="utf-8")
(ROOT / "results/ITEMS.md").write_text(items_markdown(results), encoding="utf-8")
write_xlsx(results, ROOT / "results/probe.xlsx")
print("merged, re-scored and regenerated reports for:", [r["model"] for r in results.values()])
