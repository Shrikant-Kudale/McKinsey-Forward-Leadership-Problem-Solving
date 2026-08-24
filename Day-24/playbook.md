# Executive Playbook: Ethical AI Governance, Data Privacy & Responsible Deployment

## Purpose
Give a repeatable, 60-minute routine for **responsible AI governance** that you can run on any project.

## Core idea
Responsible AI combines bias auditing, explainability appropriate to the stakes, data privacy by design, and clear accountability. Higher-stakes decisions need more transparency, even at some cost to accuracy.

## Procedure
### Step 1
Classify the use case by risk: low, medium or high stakes.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 2
Audit training data and outcomes for bias across groups.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 3
Choose the explainability level appropriate to the decision.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 4
Check privacy: purpose limitation, minimisation, retention.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 5
Assign an accountable owner and an incident process.

**Deliverable:** one written paragraph or table that proves this step is complete.

## Watch-outs
- Auditing only overall accuracy
- Treating privacy as a legal sign-off at the end

## Worked example
**Bank deploys a credit-limit model.** A bank found approval rates differed by region after controlling for income, traced to a proxy variable. Removing it and adding reason codes slightly lowered accuracy but satisfied regulators and improved customer trust.

## Quality bar
- The use case has a risk class
- A bias audit is documented
- Explainability matches the stakes
- An accountable owner exists
