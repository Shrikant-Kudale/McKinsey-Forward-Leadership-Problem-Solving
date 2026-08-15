"""Consulting-style SVG chart generator. Reads chart_specs.json and writes SVG files to ./charts_output."""
import json
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).parent
DATA = HERE / "chart_specs.json"
OUT = HERE / "charts_output"
PALETTE = ["#051C2C", "#2251FF", "#00A9F4", "#7F8C99"]
W, H, L, R, T, B = 720, 420, 70, 30, 90, 70


def frame(ch, vmax):
    plot_h = H - T - B
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="Arial, sans-serif">',
        f'<rect width="{W}" height="{H}" fill="white"/>',
        f'<text x="{L}" y="36" font-size="20" font-weight="bold" fill="#051C2C">{escape(ch["title"])}</text>',
        f'<text x="{L}" y="58" font-size="12" fill="#7F8C99">{escape(ch["unit"])} | Source: {escape(ch["source"])}</text>',
    ]
    for i in range(5):
        y = T + plot_h * i / 4
        parts.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W - R}" y2="{y:.1f}" stroke="#E5E8EB"/>')
        parts.append(f'<text x="{L - 8}" y="{y + 4:.1f}" font-size="11" text-anchor="end" fill="#7F8C99">{vmax * (4 - i) / 4:.0f}</text>')
    return parts


def bar_chart(ch):
    series, labels = ch["series"], ch["labels"]
    vmax = max(v for s in series for v in s["values"]) * 1.15
    parts = frame(ch, vmax)
    plot_w, plot_h = W - L - R, H - T - B
    group_w = plot_w / len(labels)
    bar_w = group_w * 0.7 / len(series)
    for i, label in enumerate(labels):
        gx = L + i * group_w + group_w * 0.15
        for j, s in enumerate(series):
            v = s["values"][i]
            h = plot_h * v / vmax
            x, y = gx + j * bar_w, T + plot_h - h
            parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" fill="{PALETTE[j % len(PALETTE)]}"/>')
            parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y - 5:.1f}" font-size="11" text-anchor="middle" fill="#051C2C">{v:g}</text>')
        parts.append(f'<text x="{L + i * group_w + group_w / 2:.1f}" y="{H - B + 20}" font-size="12" text-anchor="middle" fill="#051C2C">{escape(label)}</text>')
    return parts


def line_chart(ch):
    series, labels = ch["series"], ch["labels"]
    vmax = max(v for s in series for v in s["values"]) * 1.15
    parts = frame(ch, vmax)
    plot_w, plot_h = W - L - R, H - T - B
    step = plot_w / (len(labels) - 1)
    for j, s in enumerate(series):
        pts = [(L + i * step, T + plot_h - plot_h * v / vmax) for i, v in enumerate(s["values"])]
        color = PALETTE[j % len(PALETTE)]
        parts.append(f'<polyline fill="none" stroke="{color}" stroke-width="3" points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}"/>')
        for (x, y), v in zip(pts, s["values"]):
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{color}"/>')
        x, y = pts[-1]
        parts.append(f'<text x="{x - 4:.1f}" y="{y - 10:.1f}" font-size="11" text-anchor="end" fill="{color}">{s["values"][-1]:g}</text>')
    for i, label in enumerate(labels):
        parts.append(f'<text x="{L + i * step:.1f}" y="{H - B + 20}" font-size="12" text-anchor="middle" fill="#051C2C">{escape(label)}</text>')
    return parts


def legend(ch):
    if len(ch["series"]) < 2:
        return []
    parts = []
    for j, s in enumerate(ch["series"]):
        x = L + j * 170
        parts.append(f'<rect x="{x}" y="{H - 24}" width="12" height="12" fill="{PALETTE[j % len(PALETTE)]}"/>')
        parts.append(f'<text x="{x + 18}" y="{H - 14}" font-size="12" fill="#051C2C">{escape(s["name"])}</text>')
    return parts


def main():
    specs = json.loads(DATA.read_text(encoding="utf-8"))["charts"]
    OUT.mkdir(exist_ok=True)
    for i, ch in enumerate(specs, 1):
        parts = line_chart(ch) if ch["type"] == "line" else bar_chart(ch)
        svg = "\n".join(parts + legend(ch) + ["</svg>"])
        path = OUT / f"chart_{i}.svg"
        path.write_text(svg, encoding="utf-8")
        print("wrote", path.name, "-", ch["title"])


if __name__ == "__main__":
    main()
