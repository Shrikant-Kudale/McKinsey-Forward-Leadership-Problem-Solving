"""Sanity-check and business-case model: Fermi sizing, triangulation, IQR outliers, NPV, IRR and payback."""
import json
import statistics
from pathlib import Path

DATA = Path(__file__).with_name("model_inputs.json")


def npv(rate, flows):
    return sum(f / (1 + rate) ** t for t, f in enumerate(flows))


def irr(flows):
    low, high = -0.99, 10.0
    mid = 0.0
    for _ in range(200):
        mid = (low + high) / 2
        if npv(mid, flows) > 0:
            low = mid
        else:
            high = mid
    return mid


def payback_years(flows):
    cumulative = 0.0
    for t, f in enumerate(flows):
        previous = cumulative
        cumulative += f
        if cumulative >= 0 and t > 0:
            return t - 1 + (-previous / f)
    return None


def main():
    data = json.loads(DATA.read_text(encoding="utf-8"))
    bottom_up = 1.0
    print(data["title"])
    print("\nBottom-up Fermi estimate")
    for f in data["fermi_factors"]:
        bottom_up *= f["value"]
        print(f'  x {f["name"]:<40}{f["value"]:>16,.2f}')
    top_down = data["top_down_estimate"]
    ratio = bottom_up / top_down
    verdict = "consistent" if 0.5 <= ratio <= 2.0 else "investigate: more than 2x apart"
    print(f"  = bottom-up {bottom_up:,.0f} | top-down {top_down:,.0f} | ratio {ratio:.2f} ({verdict})")

    series = data["monthly_series"]
    q1, _, q3 = statistics.quantiles(series, n=4)
    low, high = q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1)
    outliers = [(i + 1, v) for i, v in enumerate(series) if v < low or v > high]
    print(f"\nOutlier scan (IQR fences {low:.1f} to {high:.1f}): {outliers if outliers else 'none'}")
    clean = [v for v in series if low <= v <= high]
    print(f"Mean with outliers {statistics.mean(series):.1f} | without {statistics.mean(clean):.1f}")

    flows = data["cash_flows"]
    rate = data["discount_rate"]
    print(f"\nBusiness case at {rate:.0%} discount rate")
    print(f"  NPV {npv(rate, flows):,.0f}")
    print(f"  IRR {irr(flows):.1%}")
    pb = payback_years(flows)
    print(f"  Payback {pb:.2f} years" if pb is not None else "  Payback not reached")


if __name__ == "__main__":
    main()
