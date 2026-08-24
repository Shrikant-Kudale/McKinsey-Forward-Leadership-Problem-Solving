# Day 24 (2026-08-24): Ethical AI Governance, Data Privacy & Responsible Deployment

**McKinsey Forward alignment:** Session 8 - Digital Fluency & AI-Augmented Productivity

## Framework breakdown
Responsible AI combines bias auditing, explainability appropriate to the stakes, data privacy by design, and clear accountability. Higher-stakes decisions need more transparency, even at some cost to accuracy.

## Step-by-step methodology
1. Classify the use case by risk: low, medium or high stakes.
2. Audit training data and outcomes for bias across groups.
3. Choose the explainability level appropriate to the decision.
4. Check privacy: purpose limitation, minimisation, retention.
5. Assign an accountable owner and an incident process.

## Real-world case study: Bank deploys a credit-limit model
A bank found approval rates differed by region after controlling for income, traced to a proxy variable. Removing it and adding reason codes slightly lowered accuracy but satisfied regulators and improved customer trust.

## Common pitfalls
- Auditing only overall accuracy
- Treating privacy as a legal sign-off at the end

## Files in this folder
- `README.md`
- `metadata.json`
- `playbook.md`
- `readiness_scorer.py`
- `responsible_ai_checklist.yaml`
- `scorecard.csv`
- `self_assessment.json`

Run the analytical tool with `python readiness_scorer.py` (weighted readiness scorer for the day's checklist).

## Self-reflection and action checklist
- [ ] The use case has a risk class
- [ ] A bias audit is documented
- [ ] Explainability matches the stakes
- [ ] An accountable owner exists

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
