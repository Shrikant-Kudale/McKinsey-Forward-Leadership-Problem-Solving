"""Weighted decision matrix with an impact-vs-feasibility 2x2 and an equal-weights sensitivity check."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("options.json")


def score(option, weights):
    return sum(option["scores"][k] * w for k, w in weights.items())


def quadrant(option, threshold):
    hi_impact = option["scores"]["impact"] >= threshold
    hi_feasible = option["scores"]["feasibility"] >= threshold
    if hi_impact and hi_feasible:
        return "Do now (high impact, high feasibility)"
    if hi_impact:
        return "Plan (high impact, low feasibility)"
    if hi_feasible:
        return "Quick win (low impact, high feasibility)"
    return "Deprioritise"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    weights = data["weights"]
    options = data["options"]
    equal = {k: 1.0 / len(weights) for k in weights}
    print(data["title"])
    print("Weights:", ", ".join(f"{k}={w:.2f}" for k, w in weights.items()), "\n")
    ranked = sorted(options, key=lambda o: score(o, weights), reverse=True)
    equal_rank = {o["name"]: i for i, o in enumerate(sorted(options, key=lambda o: score(o, equal), reverse=True), 1)}
    for i, o in enumerate(ranked, 1):
        print(f'{i}. {o["name"]:<28} weighted={score(o, weights):.2f}  equal-weights rank={equal_rank[o["name"]]}  '
              f'{quadrant(o, data["threshold"])}')
    moved = [o["name"] for i, o in enumerate(ranked, 1) if abs(equal_rank[o["name"]] - i) >= 2]
    if moved:
        print("\nRanking is sensitive to weights for:", ", ".join(moved))


if __name__ == "__main__":
    main()
