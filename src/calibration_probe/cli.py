"""calibration-probe run | ask

    run   run the 48-item battery against one or more backends; writes results/
    ask   ask one question (noul, choice or score) about some text and print the raw typed
          answers, both as written and re-asked as a choice with an insufficient_evidence option
"""

from __future__ import annotations

import argparse
import json
import os
import warnings
from pathlib import Path

from dotenv import load_dotenv

DEFAULT_SPECS = ["gateway:semif-qwen3.5-4b", "gateway:typesafe/jev-1.13.0", "llm:claude-sonnet-5"]


def _ask(args: argparse.Namespace) -> None:
    from calibration_probe.backends import get_backend
    from calibration_probe.probe import abstain_question, base_question

    if args.type == "noul":
        spec = {"type": "noul", "instructions": args.question}
    elif args.type == "choice":
        if not args.options:
            raise SystemExit("--options a,b,c is required for --type choice")
        spec = {"type": "choice", "instructions": args.question, "criteria": {o.strip(): o.strip() for o in args.options.split(",")}}
    else:
        if not args.levels:
            raise SystemExit("--levels low,medium,high is required for --type score")
        spec = {"type": "score", "instructions": args.question, "criteria": [l.strip() for l in args.levels.split(",")]}

    for s in args.spec or DEFAULT_SPECS:
        b = get_backend(s)
        base = b.ask(args.text, "q", base_question(spec))
        abst = b.ask(args.text, "q", abstain_question(spec))
        print(f"\n== {b.model}")
        print(f"as written ({args.type}), {base.latency_ms:.0f} ms:")
        print("  " + json.dumps(base.answer.model_dump(), ensure_ascii=False))
        print(f"re-asked as a choice with insufficient_evidence, {abst.latency_ms:.0f} ms:")
        print("  " + json.dumps(abst.answer.model_dump(), ensure_ascii=False))


def main(argv: list[str] | None = None) -> None:
    load_dotenv()
    os.environ.setdefault("LANGSMITH_TRACING", "false")
    warnings.filterwarnings("ignore", message=".*TypeSafeClassifier.*")
    p = argparse.ArgumentParser(prog="calibration-probe", description="Does a decision model's confidence drop when it should?")
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="run the battery against one or more backends and write results/")
    r.add_argument("--spec", action="append", help=f"backend spec, repeatable. Default: {DEFAULT_SPECS}")
    r.add_argument("--category", action="append", help="restrict to categories, repeatable")
    r.add_argument("--out-dir", default="results")

    a = sub.add_parser("ask", help="ask one question and print the raw typed answers for both variants")
    a.add_argument("text", help="the state the model sees")
    a.add_argument("--question", required=True, help="the instruction / statement to judge")
    a.add_argument("--type", choices=["noul", "choice", "score"], default="noul")
    a.add_argument("--options", help="comma-separated options for --type choice")
    a.add_argument("--levels", help="comma-separated ordered levels for --type score")
    a.add_argument("--spec", action="append", help="backend spec, repeatable. Default: all three")
    args = p.parse_args(argv)

    if args.cmd == "run":
        from calibration_probe.probe import run_many
        from calibration_probe.report import summary_markdown

        results = run_many(args.spec or DEFAULT_SPECS, categories=args.category, out_dir=Path(args.out_dir))
        print(summary_markdown(results))
        print(f"\nwritten: {args.out_dir}/probe.json, probe.xlsx, SUMMARY.md, ITEMS.md")
    else:
        _ask(args)


if __name__ == "__main__":  # pragma: no cover
    main()
