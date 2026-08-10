# Day 10 (2026-08-10): Designing Lean Workplans

**McKinsey Forward alignment:** Session 4 - Data-Driven Analysis & Synthesis

## Framework breakdown
A lean workplan translates issue-tree branches into a hypothesis-to-analysis chain with a data source, owner and deadline. Effort caps prevent boiling the ocean: any analysis longer than five days is split or cut.

## Step-by-step methodology
1. Take each prioritised branch and restate it as a hypothesis.
2. Define the minimum analysis that would test it.
3. Identify the data source and any access risk.
4. Assign one owner and a deadline.
5. Cap effort at five days per analysis and review weekly.

## Real-world case study: SaaS churn diagnosis workplan
A six-row workplan covered seat counts, onboarding drop-off, pricing, support SLAs, competitor parity and journey mapping. The validator flagged one row with no owner, one overdue, and two over-scoped analyses, which the team split or dropped before work began.

## Common pitfalls
- Analyses without a hypothesis
- Owners with more than 40 percent of effort

## Files in this folder
- `README.md`
- `lean_workplan.yaml`
- `metadata.json`
- `playbook.md`
- `workplan.json`
- `workplan_validator.py`

Run the analytical tool with `python workplan_validator.py` (lean workplan validator).

## Self-reflection and action checklist
- [ ] Every row has hypothesis, analysis, source, owner and date
- [ ] No analysis exceeds five days
- [ ] Overdue items are visible
- [ ] The plan fits the engagement timeline

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
