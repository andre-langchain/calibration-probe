"""Regenerate results/SUMMARY.md and results/ITEMS.md from the frozen results/probe.json (no model calls)."""
from __future__ import annotations

import json
from pathlib import Path

from calibration_probe.report import items_markdown, summary_markdown

ROOT = Path(__file__).resolve().parent.parent
results = json.loads((ROOT / "results/probe.json").read_text(encoding="utf-8"))
(ROOT / "results/SUMMARY.md").write_text(summary_markdown(results), encoding="utf-8")
(ROOT / "results/ITEMS.md").write_text(items_markdown(results), encoding="utf-8")
print("rebuilt results/SUMMARY.md and results/ITEMS.md")
