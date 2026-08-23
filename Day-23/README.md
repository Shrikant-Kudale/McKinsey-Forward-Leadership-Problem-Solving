# Day 23 (2026-08-23): Generative AI & Human-in-the-Loop Workflows

**McKinsey Forward alignment:** Session 8 - Digital Fluency & AI-Augmented Productivity

## Framework breakdown
Generative AI accelerates synthesis, brainstorming and red-teaming, but it can hallucinate and invite automation bias. Reliable workflows define the task, supply context, require sources, and place a human review gate before decisions.

## Step-by-step methodology
1. Define the task, audience and output format in the prompt.
2. Supply context and constraints; ask for assumptions explicitly.
3. Require citations and verify the top claims.
4. Use AI to red-team your argument for risks and counterexamples.
5. Keep a human decision gate with a log of overrides.

## Real-world case study: Analyst uses an LLM to draft a market synthesis
An analyst prompted with context and required sources, then verified five key claims; two figures were wrong and were corrected. A red-team prompt surfaced a competitor risk that was missing, and the override log showed the model was useful but never authoritative.

## Common pitfalls
- Accepting fluent text as verified fact
- Sharing confidential data with unapproved tools

## Files in this folder
- `README.md`
- `hitl_workflow.yaml`
- `metadata.json`
- `playbook.md`
- `readiness_scorer.py`
- `scorecard.csv`
- `self_assessment.json`

Run the analytical tool with `python readiness_scorer.py` (weighted readiness scorer for the day's checklist).

## Self-reflection and action checklist
- [ ] My prompts state task, context and format
- [ ] I verified key claims
- [ ] I used AI to challenge my view
- [ ] A human gate exists before decisions

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
