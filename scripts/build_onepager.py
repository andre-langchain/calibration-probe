"""Rebuild docs/onepager.html from results/probe.json and docs/onepager.template.html."""
from __future__ import annotations

import json
from pathlib import Path

from calibration_probe.probe import load_items

ROOT = Path(__file__).resolve().parent.parent
d = json.loads((ROOT / "results/probe.json").read_text(encoding="utf-8"))
models = [d[s]["model"] for s in d]
items = load_items()
out = []
for it in items:
    row = {"id": it["id"], "category": it["category"], "state": it["state"], "question": it["question"]["instructions"], "type": it["question"]["type"], "expect": it["expect"], "truth": it.get("truth"), "calibrated_p": it.get("calibrated_p"), "options": list(it["question"].get("criteria", {})) if it["question"]["type"] == "choice" else it["question"].get("criteria")}
    for s in d:
        base = next(r for r in d[s]["rows"] if r["id"] == it["id"] and r["variant"] == "base")
        ab = next(r for r in d[s]["rows"] if r["id"] == it["id"] and r["variant"] == "abstain")
        row[d[s]["model"]] = {"base": base.get("measure"), "abstain": ab.get("measure")}
    out.append(row)
data = {"models": models, "items": out, "overall": {d[s]["model"]: d[s]["summary"]["overall"] for s in d}, "categories": {d[s]["model"]: d[s]["summary"]["categories"] for s in d}}
tpl = (ROOT / "docs/onepager.template.html").read_text(encoding="utf-8")
(ROOT / "docs/onepager.html").write_text(tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
print("built docs/onepager.html")
