# Day 07 (2026-08-07): MECE Principle & Logic Trees

**McKinsey Forward alignment:** Session 3 - Structuring the Problem

## Framework breakdown
MECE means branches are mutually exclusive (no overlap) and collectively exhaustive (no gaps). Diagnostic trees ask why, while lever trees ask how. Quantitative trees can be validated arithmetically; qualitative trees need a single organising principle at each level.

## Step-by-step methodology
1. Choose a tree type: diagnostic (why) or lever (how).
2. Pick one organising principle per level, such as a formula, process stages or segments.
3. Draw branches and test exclusivity: could an item sit in two boxes?
4. Test exhaustiveness: what is missing, and would an Other bucket exceed 10 percent?
5. Validate numbers and prune branches that will not change the decision.

## Real-world case study: Ecommerce profit decline decomposed into a driver tree
A profit decline was decomposed as Revenue minus Cost, with Revenue as customers times orders times average order value. The first version of the cost branch omitted G&A, leaving 2.8M unexplained; the checker flagged the gap and the corrected tree reconciled to the reported profit.

## Common pitfalls
- Mixing criteria such as segment and channel in one level
- A catch-all Other bucket that hides a major driver

## Files in this folder
- `README.md`
- `issue_tree_checker.py`
- `issue_tree_template.yaml`
- `issue_trees.json`
- `metadata.json`
- `playbook.md`

Run the analytical tool with `python issue_tree_checker.py` (mece issue-tree reconciliation checker).

## Self-reflection and action checklist
- [ ] Each level uses one organising principle
- [ ] No item can sit under two branches
- [ ] Numbers reconcile to the stated total
- [ ] Branches map to analyses I can run

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
