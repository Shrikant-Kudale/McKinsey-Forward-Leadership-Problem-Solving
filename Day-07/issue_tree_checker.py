"""Issue-tree checker. Validates that quantitative branches reconcile to stated totals (MECE gap/overlap test)."""
import json
from pathlib import Path

DATA = Path(__file__).with_name("issue_trees.json")


def value(node):
    if "children" not in node:
        return node["value"]
    vals = [value(c) for c in node["children"]]
    op = node["op"]
    if op == "sum":
        return sum(vals)
    if op == "difference":
        return vals[0] - sum(vals[1:])
    result = 1.0
    for v in vals:
        result *= v
    return result


def leaves(node):
    if "children" not in node:
        return [node["name"]]
    names = []
    for child in node["children"]:
        names.extend(leaves(child))
    return names


def walk(node, depth, findings):
    computed = value(node)
    stated = node.get("stated")
    flag = ""
    if stated is not None and abs(computed - stated) > 0.005 * abs(stated):
        diff = stated - computed
        if node.get("op") == "sum":
            kind = "GAP (not collectively exhaustive)" if diff > 0 else "OVERLAP (not mutually exclusive)"
        else:
            kind = "DOES NOT RECONCILE (check the child branches)"
        flag = f"   <-- {kind}: {abs(diff):,.0f}"
        findings.append((node["name"], kind, abs(diff)))
    print("  " * depth + f'{node["name"]}: {computed:,.2f}' + flag)
    for child in node.get("children", []):
        walk(child, depth + 1, findings)


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    for tree in data["trees"]:
        print(f'\n{tree["label"]}')
        print("-" * len(tree["label"]))
        findings = []
        walk(tree["root"], 0, findings)
        names = [n.lower() for n in leaves(tree["root"])]
        dupes = sorted({n for n in names if names.count(n) > 1})
        if dupes:
            print("Duplicate leaves (possible overlap):", ", ".join(dupes))
        print("Result:", "reconciles" if not findings else f"{len(findings)} issue(s) to fix before analysis")


if __name__ == "__main__":
    main()
