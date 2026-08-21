"""RACI validator. Checks exactly one Accountable, at least one Responsible and a sane consulted count per task."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("raci_matrix.json")


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    tasks = data["tasks"]
    responsible_count = {r: 0 for r in data["roles"]}
    print(data["title"])
    for t in tasks:
        a = [r for r, v in t["assign"].items() if "A" in v]
        r_roles = [r for r, v in t["assign"].items() if "R" in v]
        c = [r for r, v in t["assign"].items() if v == "C"]
        issues = []
        if len(a) != 1:
            issues.append(f"needs exactly one A (found {len(a)})")
        if not r_roles:
            issues.append("no Responsible")
        if len(c) > 3:
            issues.append(f"too many Consulted ({len(c)})")
        for role in r_roles:
            responsible_count[role] += 1
        print(f'- {t["task"]:<28} {"OK" if not issues else "; ".join(issues)}')
    print("\nResponsible load:")
    for role, count in responsible_count.items():
        share = 100.0 * count / len(tasks)
        note = "  <-- overloaded" if share > 40 else ""
        print(f"  {role:<18}{count} of {len(tasks)} tasks ({share:.0f}%){note}")


if __name__ == "__main__":
    main()
