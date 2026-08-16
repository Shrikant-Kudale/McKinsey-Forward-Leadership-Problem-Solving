"""Power-interest grid and coalition index. Reads stakeholders.json."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("stakeholders.json")

ACTIONS = {
    "Manage closely": "Co-design, meet frequently, secure explicit commitment",
    "Keep satisfied": "Brief concisely, remove surprises, address concerns early",
    "Keep informed": "Regular updates, use as advocates and early testers",
    "Monitor": "Light-touch communication, watch for changes",
}


def quadrant(s):
    high_power, high_interest = s["power"] >= 6, s["interest"] >= 6
    if high_power and high_interest:
        return "Manage closely"
    if high_power:
        return "Keep satisfied"
    if high_interest:
        return "Keep informed"
    return "Monitor"


def role(s):
    if s["stance"] >= 1:
        return "champion"
    if s["stance"] <= -1:
        return "blocker"
    return "swing"


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    people = sorted(data["stakeholders"], key=lambda s: s["power"] * s["interest"], reverse=True)
    print(data["title"])
    print(f'Decision: {data["decision"]}\n')
    for s in people:
        q = quadrant(s)
        print(f'{s["name"]:<26} P={s["power"]:<2} I={s["interest"]:<2} stance={s["stance"]:+d} {role(s):<9} {q:<15} -> {ACTIONS[q]}')
    total_power = sum(s["power"] for s in people)
    index = sum(s["stance"] * s["power"] for s in people) / (2.0 * total_power)
    print(f"\nCoalition index (power-weighted, -1 to +1): {index:+.2f}")
    blockers = [s for s in people if s["power"] >= 6 and s["stance"] <= -1]
    print("Pre-wire first:", ", ".join(b["name"] for b in blockers) if blockers else "no high-power blockers")
    print("Concern notes:")
    for s in people:
        if s.get("concern"):
            print(f'  - {s["name"]}: {s["concern"]}')


if __name__ == "__main__":
    main()
