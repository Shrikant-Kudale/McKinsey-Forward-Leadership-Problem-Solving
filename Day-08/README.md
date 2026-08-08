# Day 08 (2026-08-08): Quantitative Profitability & Driver Trees

**McKinsey Forward alignment:** Session 3 - Structuring the Problem

## Framework breakdown
Profit equals revenue minus costs. Revenue decomposes into price, volume and mix; cost into fixed and variable. Driver trees expose which lever moves profit most per unit of effort, and a sensitivity run ranks them.

## Step-by-step methodology
1. Decompose profit into revenue and cost drivers.
2. Split revenue by segment into price x volume and note mix.
3. Split cost into variable per unit and fixed.
4. Apply a uniform 5 percent move to each lever and rank the impact.
5. Compute break-even volume and decide which lever to pursue first.

## Real-world case study: Hardware maker with three tiers and thin margin
The company earned 0.56M profit on 8.8M revenue. Sensitivity showed a 5 percent variable-cost reduction was worth about 0.29M more than a 5 percent volume increase, so procurement became the first workstream rather than sales incentives.

## Common pitfalls
- Comparing levers with unequal effort assumptions
- Ignoring mix when segment margins differ

## Files in this folder
- `README.md`
- `driver_case.json`
- `driver_tree.yaml`
- `metadata.json`
- `playbook.md`
- `profit_driver_simulator.py`

Run the analytical tool with `python profit_driver_simulator.py` (profit driver sensitivity simulator).

## Self-reflection and action checklist
- [ ] My driver tree reconciles to reported profit
- [ ] I ranked levers on equal footing
- [ ] I know my break-even volume
- [ ] I chose a first lever with a rationale

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
