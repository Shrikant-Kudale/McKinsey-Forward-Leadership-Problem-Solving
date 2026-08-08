"""Profit driver simulator. Reads driver_case.json, ranks levers by profit impact and computes break-even volume."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("driver_case.json")


def profit(segments, fixed, price=1.0, vol=1.0, cost=1.0, fix=1.0, shift=0.0):
    segs = [dict(s) for s in segments]
    total = sum(s["volume"] for s in segs)
    if shift:
        margins = [s["price"] - s["unit_cost"] for s in segs]
        low, high = margins.index(min(margins)), margins.index(max(margins))
        moved = min(segs[low]["volume"], shift * total)
        segs[low]["volume"] -= moved
        segs[high]["volume"] += moved
    revenue = sum(s["price"] * price * s["volume"] * vol for s in segs)
    variable = sum(s["unit_cost"] * cost * s["volume"] * vol for s in segs)
    return revenue, variable, revenue - variable - fixed * fix


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    segs, fixed, step = data["segments"], data["fixed_costs"], data["lever_step"]
    revenue, variable, base = profit(segs, fixed)
    print(data["title"])
    print(f"Revenue {revenue:,.0f} | Variable cost {variable:,.0f} | Fixed cost {fixed:,.0f} | Profit {base:,.0f}")
    print(f"Operating margin: {100.0 * base / revenue:.2f}%")
    contribution = revenue - variable
    print(f"Break-even volume factor: {fixed / contribution:.3f}x of current volume\n")
    levers = [
        (f"Price +{step:.0%}", dict(price=1 + step)),
        (f"Volume +{step:.0%}", dict(vol=1 + step)),
        (f"Unit variable cost -{step:.0%}", dict(cost=1 - step)),
        (f"Fixed costs -{step:.0%}", dict(fix=1 - step)),
        (f"Mix shift {step:.0%} of volume to best-margin segment", dict(shift=step)),
    ]
    results = []
    for label, kwargs in levers:
        results.append((profit(segs, fixed, **kwargs)[2] - base, label))
    print("Lever ranking (profit uplift):")
    for rank, (delta, label) in enumerate(sorted(results, reverse=True), 1):
        print(f"  {rank}. {label:<52}{delta:>14,.0f}")


if __name__ == "__main__":
    main()
