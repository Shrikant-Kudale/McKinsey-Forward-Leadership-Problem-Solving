# Day 11 (2026-08-11): Data Sanity Checks, Triangulation & Quantitative Modelling

**McKinsey Forward alignment:** Session 4 - Data-Driven Analysis & Synthesis

## Framework breakdown
Before modelling, size the answer with Fermi estimation, check for outliers, and triangulate bottom-up against top-down figures. Business cases then convert assumptions into cash flows, NPV, IRR and payback.

## Step-by-step methodology
1. Build a bottom-up Fermi estimate by multiplying independent factors.
2. Build a top-down estimate from a different source and compare.
3. Scan the data series for outliers using the IQR rule.
4. Model cash flows and compute NPV, IRR and payback.
5. Flag correlation-causation risks before presenting.

## Real-world case study: Sizing an expense-software market and evaluating the build
Bottom-up sizing gave 2.16B and top-down 2.9B, within a factor of 1.4, enough to proceed. A monthly revenue series contained an outlier (260 vs. a 120 range) traced to a one-off contract; removing it changed the trend. The investment showed a positive NPV at 12 percent.

## Common pitfalls
- Precision theatre on weak assumptions
- Reading correlation as causation

## Files in this folder
- `README.md`
- `business_case_model.py`
- `metadata.json`
- `model_inputs.json`
- `playbook.md`
- `sanity_check_log.yaml`

Run the analytical tool with `python business_case_model.py` (fermi, outlier and npv/irr business-case model).

## Self-reflection and action checklist
- [ ] I triangulated two independent estimates
- [ ] I examined outliers before averaging
- [ ] My model shows NPV, IRR and payback
- [ ] I listed my top three assumptions

**Reflection prompts:** What will I do differently on Monday? Who will I ask for feedback this week?
