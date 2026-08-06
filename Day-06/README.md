# Day 06 (2026-08-06): Root Cause Analysis: 5 Whys, Fishbone & Pareto 80/20

**McKinsey Forward alignment:** Session 2 - Defining the Problem

## Framework breakdown
Five Whys drills down a single causal chain, the Ishikawa (fishbone) diagram organises candidate causes by category, and Pareto analysis shows which few causes account for most of the impact. Combined, they move teams from blame to systemic fixes.

## Step-by-step methodology
1. State the problem with a measurable impact.
2. Brainstorm causes on a fishbone: people, process, technology, data, environment.
3. Run Five Whys on the top three candidates until you reach a controllable cause.
4. Quantify each cause and build a Pareto chart.
5. Assign countermeasures to the vital few and define verification metrics.

## Real-world case study: Payments API outage with 1,100 minutes of cumulative impact
After a quarter of incidents an engineering group tallied impact minutes per cause. Three causes (config changes without canary, connection pool exhaustion and cache stampedes) accounted for 77 percent of minutes. Targeted fixes cut incident minutes by 58 percent the next quarter.

## Common pitfalls
- Stopping at the human error cause
- Fixing the loudest cause instead of the largest

## Files in this folder
- `README.md`
- `metadata.json`
- `pareto_analyzer.py`
- `pareto_data.json`
- `playbook.md`
- `rca_worksheet.yaml`

Run the analytical tool with `python pareto_analyzer.py` (pareto 80/20 analyzer).

## Self-reflection and action checklist
- [ ] I used evidence, not opinion, at each Why
- [ ] My fishbone covers all five categories
- [ ] I quantified causes before choosing fixes
- [ ] Each countermeasure has an owner and a metric

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
