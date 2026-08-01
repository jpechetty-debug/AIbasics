---
difficulty: Intermediate
duration: ~90 minutes
tags:
- prompting
- python
- agents
title: 'Week 4 - Day 5: Review & Mini-Project'
week: 4
---

# Week 4 - Day 5: Review & Mini-Project

## Overview
**Week 4 – Day 5**
**Topic:** Review & Mini-Project: Building a Troubleshooting Agent
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Review Zero-Shot, CoT, Critic, and Chaining patterns.
2. Combine all patterns into a cohesive "Manual Agent."
3. Complete the Week 4 Assessment.

---

## Lesson Content

### The Advanced Prompting Stack

You now possess the advanced tools:
1.  **Few-Shot:** Show, don't just tell.
2.  **Chain of Thought:** "Let's think step by step."
3.  **The Critic:** "Review your work."
4.  **Chaining:** "Step 1 -> Step 2 -> Step 3."

### How to "Think" Like an Agent

An AI Agent isn't magic. It's just a loop:
**Perceive (Read Data) -> Reason (CoT) -> Act (Generate) -> Criticize (Review).**

---

## Hands-On Mini-Project

### Project: The "Home Internet Outage Agent"

**Objective:** Simulate an AI Agent that diagnoses a home Wi-Fi outage report.

**Step 1: The Trigger (User Input)**
"The Wi-Fi at home is down."

**Step 2: The Analyst (Chain Link 1)**
> **Context:** You are a friendly home tech-support assistant.
> **Task:** Analyze the user report. List 3 clarifying questions to narrow down the cause.
> **Output:**
> 1. Is it every device, or just one?
> 2. Do wired connections (like a smart TV plugged into an ethernet cable) still work?
> 3. Are the lights on the router/modem on and normal-looking?

**Step 3: The Data Merger (Chain Link 2)**
*(Assume the answers are: every device is affected, no wired devices work either, and the router lights are off.)*
> **Context:** You are a home tech-support assistant.
> **Task:** Given the symptoms (nothing works, router lights off), determine the likely root cause. Use Chain of Thought.
> **Output:**
> 1. Every device is affected, including wired -> the problem is upstream of all devices.
> 2. Router lights are off entirely -> likely a power issue, not a Wi-Fi signal issue.
> 3. **Root Cause:** The router or modem has lost power, or the internet service itself is down.

**Step 4: The Communicator (Chain Link 3)**
> **Context:** You are explaining this to your household.
> **Task:** Write a short, calm message explaining the issue and the first thing to try (checking the router's power and cables).
> **Input:** "Router appears to have lost power."
> **Output:** "Hey everyone, looks like the router lost power — I'm going to check the outlet and cables now..."

**Assignment Submission:**
Perform this same chain on a problem of your choice (e.g., a car that won't start, a recipe that didn't turn out right, a plant that's dying) and capture the 3-step prompt chain you used.

---

## Weekly Interactive Quiz

### Question 1 (Patterns)
**Which pattern involves giving the AI 2-3 examples of "Input -> Output" before asking your real question?**

A) Zero-Shot
B) One-Shot
C) Few-Shot
D) Chain of Thought

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** "Few" implies a small number (typically 2-5) of examples.

### Question 2 (Reasoning)
**"Let's think step by step" is the trigger phrase for:**

A) The Critic
B) Chain of Thought (CoT)
C) The Formatter
D) The Extractor

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It triggers intermediate reasoning steps.

### Question 3 (Quality)
**You ask the AI to "Act as a Skeptic" and try to find flaws in your plan. Which pattern is this?**

A) The Critic Pattern
B) The Summarizer
C) The Fan
D) The Translator

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** You are soliciting a critique/audit.

### Question 4 (Architecture)
**Why is Chaining safer than a single giant prompt?**

A) It isn't.
B) It allows for checking each step before moving to the next, preventing errors from cascading.
C) It creates more AI.
D) It is always faster.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** If Step 1 is wrong, you catch it before Step 2 happens.

### Question 5 (Future)
**What is the next evolution after "Chaining"?**

A) Telepathy.
B) Autonomous Agents (where the AI chooses which tool/chain to run on its own).
C) Less AI.
D) Analog computers.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Agents are essentially dynamic chains where the AI picks the path itself.

---

### End of Week 4
**Congratulations!** You have completed the **Advanced Prompting** module.
You can now guide the AI to learn from examples, think logically, critique itself, and execute complex workflows.
**Next Week:** We will explore **AI for Everyday Automation**—using AI to help you write simple, beginner-friendly scripts.
