"""The probe: items, variants, metrics, run, report.

Two variants per item:

* ``base``     the question exactly as written
* ``abstain``  the same question with an explicit way to say "the state does not decide this":
               Noul  -> Choice {yes, no, insufficient_evidence}
               Choice -> the same options + insufficient_evidence
               Score -> Choice over the rubric levels + insufficient_evidence

Running the abstain variant on *every* item lets us measure both halves of the fix:
does the model abstain when it should (uncertain categories) and does it keep answering
when it should (answerable items, "false abstain" rate).
"""

from __future__ import annotations

import json
import statistics
from collections import defaultdict
from importlib import resources
from pathlib import Path
from typing import Any

from langchain_typesafe import Choice, ChoiceAnswer, Noul, NoulAnswer, Score

from calibration_probe.backends import Answer, BackendError, Question, entropy, get_backend

ABSTAIN = "insufficient_evidence"
ABSTAIN_TEXT = "The state does not contain enough information to decide."
NOUL_CONFIDENT = 0.4  # certainty = |p-0.5|*2 ; confident when p outside [0.3, 0.7]
CHOICE_CONFIDENT = 0.5  # confidence = 1 - normalised entropy, computed the same way for every model


def distribution_confidence(probs: list[float]) -> float:
    """1 - normalised entropy: 1 for a one-hot answer, 0 for a flat one.

    Computed by us for every model so the "confident" threshold means the same thing
    everywhere. Vendors report their own confidence with different formulas; that value is
    kept as ``reported_confidence`` for reference only.
    """
    return max(0.0, min(1.0, 1.0 - entropy(probs)))


# ------------------------------------------------------------------------------ items
def load_items(path: str | Path | None = None) -> list[dict[str, Any]]:
    text = Path(path).read_text(encoding="utf-8") if path else resources.files("calibration_probe").joinpath("items.json").read_text(encoding="utf-8")
    items = json.loads(text)["items"]
    seen: set[str] = set()
    for it in items:
        for k in ("id", "category", "expect", "state", "question"):
            if k not in it:
                raise ValueError(f"item missing {k!r}: {it.get('id')}")
        if it["id"] in seen:
            raise ValueError(f"duplicate id {it['id']}")
        seen.add(it["id"])
        if it["expect"] not in ("confident", "uncertain"):
            raise ValueError(f"{it['id']}: bad expect")
        base_question(it["question"])
    return items


def base_question(spec: dict[str, Any]) -> Question:
    t = spec["type"]
    if t == "noul":
        return Noul(instructions=spec["instructions"])
    if t == "choice":
        return Choice(instructions=spec["instructions"], criteria=dict(spec["criteria"]))
    if t == "score":
        return Score(instructions=spec["instructions"], criteria=list(spec["criteria"]))
    raise ValueError(f"unknown question type {t!r}")


def abstain_question(spec: dict[str, Any]) -> Choice:
    t = spec["type"]
    if t == "noul":
        criteria = {"yes": "The statement is true.", "no": "The statement is false.", ABSTAIN: ABSTAIN_TEXT}
    elif t == "choice":
        criteria = {**spec["criteria"], ABSTAIN: ABSTAIN_TEXT}
    else:
        criteria = {**{f"level_{i}": c for i, c in enumerate(spec["criteria"])}, ABSTAIN: ABSTAIN_TEXT}
    return Choice(instructions=spec["instructions"], criteria=criteria)


def abstain_truth(item: dict[str, Any]) -> str | None:
    """The correct option in the abstain variant, when the item has a truth."""
    if "truth" not in item:
        return None
    t, truth = item["question"]["type"], item["truth"]
    if t == "noul":
        return "yes" if truth else "no"
    if t == "choice":
        return str(truth)
    return f"level_{int(truth)}"


# ---------------------------------------------------------------------------- metrics
def measure(answer: Answer, truth: Any = None, calibrated_p: float | None = None) -> dict[str, Any]:
    if isinstance(answer, NoulAnswer):
        p = answer.noul
        cert = abs(p - 0.5) * 2
        m: dict[str, Any] = {"kind": "noul", "p": round(p, 4), "certainty": round(cert, 4), "confident": cert >= NOUL_CONFIDENT, "probabilities": {"yes": round(p, 4), "no": round(1 - p, 4)}}
        if truth is not None:
            m["correct"] = (p >= 0.5) == bool(truth)
            m["brier"] = round((p - (1.0 if truth else 0.0)) ** 2, 4)
        if calibrated_p is not None:
            m["calibrated_p"] = calibrated_p
            m["error_vs_base_rate"] = round(abs(p - calibrated_p), 4)
        return m
    if isinstance(answer, ChoiceAnswer):
        probs = answer.probabilities
        conf = distribution_confidence(list(probs.values()))
        m = {"kind": "choice", "choice": answer.choice, "confidence": round(conf, 4), "reported_confidence": round(answer.confidence, 4), "top_p": round(max(probs.values()), 4), "entropy": round(entropy(list(probs.values())), 4), "confident": conf >= CHOICE_CONFIDENT, "abstained": answer.choice == ABSTAIN, "abstain_p": round(probs[ABSTAIN], 4) if ABSTAIN in probs else None, "probabilities": {k: round(v, 4) for k, v in probs.items()}}
        if truth is not None:
            m["correct"] = answer.choice == truth
        return m
    levels = [answer.probabilities[k] for k in sorted(answer.probabilities)]
    conf = distribution_confidence(levels)
    m = {"kind": "score", "score": round(answer.score, 4), "confidence": round(conf, 4), "reported_confidence": round(answer.confidence, 4), "entropy": round(entropy(levels), 4), "confident": conf >= CHOICE_CONFIDENT, "probabilities": {str(answer.legend[k]): round(answer.probabilities[k], 4) for k in sorted(answer.probabilities)}}
    if truth is not None:
        m["correct"] = round(answer.score) == int(truth)
    return m


def rescore_rows(rows: list[dict[str, Any]]) -> None:
    """Recompute choice/score confidence from stored distributions (no model calls)."""
    for r in rows:
        m = r.get("measure")
        if not m or m["kind"] == "noul":
            continue
        if "reported_confidence" not in m:
            m["reported_confidence"] = m["confidence"]
        conf = distribution_confidence(list(m["probabilities"].values()))
        m["confidence"] = round(conf, 4)
        m["confident"] = conf >= CHOICE_CONFIDENT


def _cert(m: dict[str, Any]) -> float:
    return m.get("certainty", m.get("confidence", 0.0))


def summarise(rows: list[dict[str, Any]]) -> dict[str, Any]:
    base = [r for r in rows if r["variant"] == "base" and "measure" in r]
    abst = [r for r in rows if r["variant"] == "abstain" and "measure" in r]
    by_cat: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in base:
        by_cat[r["category"]].append(r)

    cats: dict[str, Any] = {}
    for cat, rs in sorted(by_cat.items()):
        unc = [r for r in rs if r["expect"] == "uncertain"]
        con = [r for r in rs if r["expect"] == "confident"]
        truth_rows = [r for r in rs if "correct" in r["measure"]]
        briers = [r["measure"]["brier"] for r in rs if "brier" in r["measure"]]
        errs = [r["measure"]["error_vs_base_rate"] for r in rs if "error_vs_base_rate" in r["measure"]]
        a_rows = [r for r in abst if r["category"] == cat]
        a_unc = [r for r in a_rows if r["expect"] == "uncertain"]
        a_con = [r for r in a_rows if r["expect"] == "confident"]
        cats[cat] = {
            "n": len(rs),
            "mean_certainty": round(statistics.mean(_cert(r["measure"]) for r in rs), 3),
            "overconfidence_rate": round(sum(1 for r in unc if r["measure"]["confident"]) / len(unc), 3) if unc else None,
            "underconfidence_rate": round(sum(1 for r in con if not r["measure"]["confident"]) / len(con), 3) if con else None,
            "accuracy": round(sum(1 for r in truth_rows if r["measure"]["correct"]) / len(truth_rows), 3) if truth_rows else None,
            "brier": round(statistics.mean(briers), 4) if briers else None,
            "error_vs_base_rate": round(statistics.mean(errs), 3) if errs else None,
            "mean_latency_ms": round(statistics.mean(r["latency_ms"] for r in rs), 1),
            # the fix, measured on the same items
            "with_abstain_option": {
                "abstain_rate_when_uncertain": round(sum(1 for r in a_unc if r["measure"]["abstained"]) / len(a_unc), 3) if a_unc else None,
                "false_abstain_rate_when_answerable": round(sum(1 for r in a_con if r["measure"]["abstained"]) / len(a_con), 3) if a_con else None,
                "accuracy_when_answerable": round(sum(1 for r in a_con if r["measure"].get("correct")) / len(a_con), 3) if a_con else None,
                "still_overconfident_rate": round(sum(1 for r in a_unc if r["measure"]["confident"] and not r["measure"]["abstained"]) / len(a_unc), 3) if a_unc else None,
            },
        }

    bins: dict[str, list[tuple[float, bool]]] = defaultdict(list)
    for r in base:
        m = r["measure"]
        if m["kind"] == "noul" and "correct" in m:
            edge = min(int(m["p"] * 5), 4)
            bins[f"{edge * 0.2:.1f}-{(edge + 1) * 0.2:.1f}"].append((m["p"], bool(r["truth"])))
    reliability = {k: {"n": len(v), "mean_p": round(statistics.mean(p for p, _ in v), 3), "observed_true": round(sum(t for _, t in v) / len(v), 3)} for k, v in sorted(bins.items())}

    unc_all = [r for r in base if r["expect"] == "uncertain"]
    unc_abst = [r for r in abst if r["expect"] == "uncertain"]
    con_abst = [r for r in abst if r["expect"] == "confident"]
    ans_cert = cats.get("answerable", {}).get("mean_certainty")
    other = [c["mean_certainty"] for k, c in cats.items() if k != "answerable"]
    return {
        "categories": cats,
        "overall": {
            "uncertain_items": len(unc_all),
            "overconfidence_rate_base": round(sum(1 for r in unc_all if r["measure"]["confident"]) / len(unc_all), 3) if unc_all else None,
            "abstain_rate_with_option": round(sum(1 for r in unc_abst if r["measure"]["abstained"]) / len(unc_abst), 3) if unc_abst else None,
            "still_overconfident_with_option": round(sum(1 for r in unc_abst if r["measure"]["confident"] and not r["measure"]["abstained"]) / len(unc_abst), 3) if unc_abst else None,
            "false_abstain_rate_answerable": round(sum(1 for r in con_abst if r["measure"]["abstained"]) / len(con_abst), 3) if con_abst else None,
            "accuracy_answerable_with_option": round(sum(1 for r in con_abst if r["measure"].get("correct")) / len(con_abst), 3) if con_abst else None,
            "separation": round(ans_cert - statistics.mean(other), 3) if ans_cert is not None and other else None,
            "median_latency_ms": round(statistics.median(r["latency_ms"] for r in base), 1) if base else None,
            "errors": sum(1 for r in rows if "error" in r),
        },
        "reliability_noul": reliability,
    }


# ------------------------------------------------------------------------------- run
def run(spec: str, items: list[dict[str, Any]] | None = None, categories: list[str] | None = None, variants: tuple[str, ...] = ("base", "abstain")) -> dict[str, Any]:
    items = items or load_items()
    if categories:
        items = [it for it in items if it["category"] in categories]
    backend = get_backend(spec)
    rows: list[dict[str, Any]] = []
    for it in items:
        for variant in variants:
            q = base_question(it["question"]) if variant == "base" else abstain_question(it["question"])
            truth = it.get("truth") if variant == "base" else abstain_truth(it)
            row: dict[str, Any] = {"id": it["id"], "variant": variant, "category": it["category"], "expect": it["expect"], "truth": it.get("truth"), "question_type": it["question"]["type"]}
            try:
                res = backend.ask(it["state"], it["id"], q)
            except BackendError as exc:
                rows.append({**row, "error": str(exc)})
                continue
            rows.append({**row, "measure": measure(res.answer, truth, it.get("calibrated_p") if variant == "base" else None), "latency_ms": round(res.latency_ms, 1), "model": res.model})
    return {"spec": spec, "model": next((r.get("model") for r in rows if r.get("model")), spec), "n_items": len(items), "summary": summarise(rows), "rows": rows}


def run_many(specs: list[str], categories: list[str] | None = None, out_dir: Path = Path("results")) -> dict[str, Any]:
    results = {s: run(s, categories=categories) for s in specs}
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "probe.json").write_text(json.dumps(results, indent=1, ensure_ascii=False, default=str), encoding="utf-8")
    from calibration_probe.report import items_markdown, summary_markdown, write_xlsx

    (out_dir / "SUMMARY.md").write_text(summary_markdown(results), encoding="utf-8")
    (out_dir / "ITEMS.md").write_text(items_markdown(results), encoding="utf-8")
    write_xlsx(results, out_dir / "probe.xlsx")
    return results
