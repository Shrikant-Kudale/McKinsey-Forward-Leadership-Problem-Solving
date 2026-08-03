"""Habit and consistency tracker. Reads tracker_log.json and reports consistency, trend and streaks."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("tracker_log.json")


def meets(value, spec):
    return value >= spec["target"] if spec["direction"] == "max" else value <= spec["target"]


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    records = data["records"]
    metrics = data["metrics"]
    print(data["title"])
    print("=" * len(data["title"]))
    half = len(records) // 2
    for name, spec in metrics.items():
        values = [r["values"][name] for r in records]
        consistency = 100.0 * sum(meets(v, spec) for v in values) / len(values)
        first = sum(values[:half]) / half
        second = sum(values[half:]) / (len(values) - half)
        streak = 0
        for v in reversed(values):
            if meets(v, spec):
                streak += 1
            else:
                break
        warn = "  <-- early warning" if consistency < 50 else ""
        print(f"{name:<20} avg={sum(values) / len(values):6.2f} target={spec['target']:<5} ({spec['direction']}) "
              f"consistency={consistency:5.1f}% trend={second - first:+.2f} streak={streak}{warn}")
    mix = data.get("learning_mix_hours")
    if mix:
        total = sum(mix.values())
        ideal = {"experience": 70, "exposure": 20, "education": 10}
        print("\n70-20-10 learning mix")
        for key, hours in mix.items():
            share = 100.0 * hours / total
            print(f"  {key:<11} {hours:5.1f}h  {share:5.1f}%  (ideal {ideal[key]}%, gap {share - ideal[key]:+.1f} pts)")
        days = len(records)
        print(f"Learning velocity: {total / days:.2f} hours/day over {days} days")


if __name__ == "__main__":
    main()
