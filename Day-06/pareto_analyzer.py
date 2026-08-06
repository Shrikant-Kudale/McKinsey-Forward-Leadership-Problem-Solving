"""Pareto 80/20 analyzer. Reads pareto_data.json and prints impact, cumulative share and the vital few."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("pareto_data.json")


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    items = sorted(data["items"], key=lambda i: i["value"], reverse=True)
    total = sum(i["value"] for i in items)
    print(data["title"])
    print(f'Total {data["unit"]}: {total:,.0f}\n')
    cumulative = 0.0
    vital = []
    for item in items:
        before = 100.0 * cumulative / total
        cumulative += item["value"]
        share = 100.0 * item["value"] / total
        bar = "#" * int(round(share / 2))
        print(f'{item["name"]:<38}{item["value"]:>8,.0f} {share:5.1f}%  cum {100.0 * cumulative / total:5.1f}%  {bar}')
        if before < 80.0:
            vital.append(item["name"])
    print("\nVital few (needed to pass 80% of impact):")
    for name in vital:
        print("  -", name)


if __name__ == "__main__":
    main()
