"""Lean workplan validator. Flags missing fields, overdue work and over-scoped analyses."""
import json
from collections import defaultdict
from datetime import date
from pathlib import Path

DATA = Path(__file__).with_name("workplan.json")
REQUIRED = ["hypothesis", "analysis", "data_source", "owner", "deadline"]


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    as_of = date.fromisoformat(data["as_of"])
    max_days = data["max_effort_days"]
    load = defaultdict(float)
    print(data["title"], f"(as of {as_of})")
    for i, item in enumerate(data["items"], 1):
        issues = [f"missing {k}" for k in REQUIRED if not item.get(k)]
        if item.get("effort_days", 0) > max_days:
            issues.append(f"over-scoped ({item['effort_days']}d > {max_days}d): split or cut")
        if item.get("deadline") and item["status"] != "done" and date.fromisoformat(item["deadline"]) < as_of:
            issues.append("overdue")
        if item.get("owner"):
            load[item["owner"]] += item.get("effort_days", 0)
        label = item.get("hypothesis") or item.get("analysis")
        print(f"{i}. {label[:70]:<70} {'OK' if not issues else '; '.join(issues)}")
    total = sum(load.values())
    print(f"\nTotal effort: {total:.0f} days")
    for owner, days in sorted(load.items(), key=lambda kv: -kv[1]):
        note = "  <-- concentration risk" if total and days / total > 0.4 else ""
        print(f"  {owner:<20}{days:>4.0f}d{note}")


if __name__ == "__main__":
    main()
