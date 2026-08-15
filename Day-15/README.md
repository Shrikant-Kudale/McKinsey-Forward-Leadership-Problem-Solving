# Day 15 (2026-08-15): Executive Data Storytelling & High-Impact Visuals

**McKinsey Forward alignment:** Session 5 - Communicating for Impact

## Framework breakdown
Choose visuals by message: bars for comparisons, lines for trends, stacked bars for composition, scatter for relationships. Every chart carries an action title, a labelled unit and one highlighted insight.

## Step-by-step methodology
1. Write the message the chart must prove.
2. Pick the chart type: comparison, trend, composition or relationship.
3. Remove clutter: gridlines, legends and decimals that do not help.
4. Highlight the single data point that proves the title.
5. Generate SVG charts from the spec file and review them.

## Real-world case study: Three charts for a retail board pack
The board pack used three charts: contribution margin by channel (bar), repeat purchase by month (line), and outage minutes by cause (bar). The chart generator turned a JSON spec into clean SVGs in seconds, so edits to titles and values took minutes.

## Common pitfalls
- Pie charts for many categories
- Truncated axes that exaggerate differences

## Files in this folder
- `README.md`
- `chart_generator.py`
- `chart_spec.yaml`
- `chart_specs.json`
- `metadata.json`
- `playbook.md`

Run the analytical tool with `python chart_generator.py` (svg consulting-style chart generator).

## Self-reflection and action checklist
- [ ] Each chart proves its action title
- [ ] I chose the chart type by message
- [ ] Units and sources are labelled
- [ ] I removed non-essential decoration

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
