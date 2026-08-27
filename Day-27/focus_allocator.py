"""Weekly focus allocator. Reads weekly_time_log.json and summarises Eisenhower and deep-work allocation."""
import json
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).with_name("weekly_time_log.json")
LABELS = {"Q1": "Urgent + important", "Q2": "Important, not urgent", "Q3": "Urgent, not important", "Q4": "Neither"}


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    log = data["activities"]
    total = sum(a["hours"] for a in log)
    by_quadrant = defaultdict(float)
    by_type = defaultdict(float)
    for a in log:
        by_quadrant[a["quadrant"]] += a["hours"]
        by_type[a["type"]] += a["hours"]
    print(data["title"])
    print(f"Total logged: {total:.1f}h\n")
    for q in ("Q1", "Q2", "Q3", "Q4"):
        print(f"{q} {LABELS[q]:<24}{by_quadrant[q]:>5.1f}h {100.0 * by_quadrant[q] / total:5.1f}%")
    deep = by_type["deep"]
    target = data["deep_work_target_hours"]
    print(f"\nDeep work {deep:.1f}h vs target {target}h -> {'on target' if deep >= target else f'short by {target - deep:.1f}h'}")
    print(f"Meetings {by_type['meeting']:.1f}h | Shallow {by_type['shallow']:.1f}h")
    cut = sorted((a for a in log if a["quadrant"] in ("Q3", "Q4")), key=lambda a: a["hours"], reverse=True)[:3]
    print("\nBest candidates to delegate, batch or decline:")
    for a in cut:
        print(f'  - {a["activity"]} ({a["hours"]}h, {a["quadrant"]})')
    freed = sum(a["hours"] for a in cut) * 0.5
    print(f"Recovering half of that time frees about {freed:.1f}h for Q2 deep work.")


if __name__ == "__main__":
    main()
