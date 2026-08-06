# Executive Playbook: Root Cause Analysis: 5 Whys, Fishbone & Pareto 80/20

## Purpose
Give a repeatable, 60-minute routine for **root cause analysis and Pareto** that you can run on any project.

## Core idea
Five Whys drills down a single causal chain, the Ishikawa (fishbone) diagram organises candidate causes by category, and Pareto analysis shows which few causes account for most of the impact. Combined, they move teams from blame to systemic fixes.

## Procedure
### Step 1
State the problem with a measurable impact.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 2
Brainstorm causes on a fishbone: people, process, technology, data, environment.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 3
Run Five Whys on the top three candidates until you reach a controllable cause.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 4
Quantify each cause and build a Pareto chart.

**Deliverable:** one written paragraph or table that proves this step is complete.

### Step 5
Assign countermeasures to the vital few and define verification metrics.

**Deliverable:** one written paragraph or table that proves this step is complete.

## Watch-outs
- Stopping at the human error cause
- Fixing the loudest cause instead of the largest

## Worked example
**Payments API outage with 1,100 minutes of cumulative impact.** After a quarter of incidents an engineering group tallied impact minutes per cause. Three causes (config changes without canary, connection pool exhaustion and cache stampedes) accounted for 77 percent of minutes. Targeted fixes cut incident minutes by 58 percent the next quarter.

## Quality bar
- I used evidence, not opinion, at each Why
- My fishbone covers all five categories
- I quantified causes before choosing fixes
- Each countermeasure has an owner and a metric
