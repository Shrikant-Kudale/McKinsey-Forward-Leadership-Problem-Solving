"""Weighted self-assessment scorer. Reads self_assessment.json and prints a readiness report."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("self_assessment.json")

BANDS = [
    (85, "Strong - sustain it and teach it to others"),
    (70, "Solid - target the weakest criteria"),
    (50, "Developing - run a focused two-week practice sprint"),
    (0, "Foundational - restart with the playbook steps"),
]


def weighted_percent(criteria):
    total_weight = sum(c["weight"] for c in criteria)
    earned = sum(c["weight"] * c["score"] for c in criteria)
    return 100.0 * earned / (5.0 * total_weight)


def band(pct):
    for floor, label in BANDS:
        if pct >= floor:
            return label
    return BANDS[-1][1]


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    criteria = data["criteria"]
    print(data["title"])
    print("=" * len(data["title"]))
    for c in criteria:
        print(f'{c["criterion"]:<62} weight={c["weight"]} score={c["score"]}/5')
    pct = weighted_percent(criteria)
    print(f"\nWeighted readiness: {pct:.1f}% -> {band(pct)}")
    gaps = sorted(criteria, key=lambda c: (5 - c["score"]) * c["weight"], reverse=True)[:2]
    print("Highest-leverage gaps:")
    for g in gaps:
        print(f'  - {g["criterion"]} (gap x weight = {(5 - g["score"]) * g["weight"]})')
    print("Next action:", data["next_action"])


if __name__ == "__main__":
    main()
