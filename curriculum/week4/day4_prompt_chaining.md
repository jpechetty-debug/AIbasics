---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
- agents
title: 'Week 4 - Day 4: Prompt Chaining (Building Agents)'
week: 4
---

# Week 4 - Day 4: Prompt Chaining (Building Agents)

## Overview
**Week 4 – Day 4**
**Topic:** Prompt Chaining - Building Manual Agents
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define "Prompt Chaining."
2. Break a complex task into a series of small, reliable prompts.
3. Simulate an "AI Agent" manually by passing outputs between prompts.

---

## Lesson Content

### One Prompt vs. A Chain

**The Monolith Strategy (Bad):**
> "Read this messy pile of family recipe notes, organize them, rewrite each one clearly, and format it all as a printable recipe book."
*(This fails. The AI tries to do too much at once and starts making things up or skipping steps.)*

**The Chain Strategy (Good):**
1.  **Prompt A (Organizer):** "List every distinct recipe mentioned in these notes." -> *Output A*
2.  **Prompt B (Writer):** "For each recipe in *Output A*, rewrite it with clear, precise measurements and steps." -> *Output B*
3.  **Prompt C (Formatter):** "Format all the recipes in *Output B* into a clean recipe-book layout." -> *Output C*

This is **Prompt Chaining**. It is the foundation of AI Agents.

### Why Chain?
1.  **Context Window Management:** You process information in manageable chunks.
2.  **Specialization:** Different "personas" for different steps (Organizer vs. Writer vs. Formatter).
3.  **Checkpointing:** You can verify Step 1 before moving to Step 2.

### Step-by-Step: The "Home Project Guide" Chain

**Goal:** Turn your rough notes from fixing a leaky faucet into a clear guide you can reuse or share.

**Link 1: The Reader**
> "Read these rough notes. List every distinct step I took, in plain English."
> *Output: Step List.*

**Link 2: The Detail Adder**
> "For each step in the list above, add a helpful tip or common mistake to avoid."
> *Output: Steps with Tips.*

**Link 3: The Formatter**
> "Combine the steps and tips above into a clean, numbered how-to guide."
> *Output: Final Guide.*

---

## Hands-On Exercise

### Exercise: The "Old Family Recipe" Modernizer Chain

**Objective:** Safely turn a vague, old-fashioned recipe ("a pinch of this, a handful of that") into a precise, modern one — without losing anything important.

**Step 1: Comprehension (The Translator)**
> **Prompt:** "Explain this old recipe step-by-step in plain English. Do not rewrite it yet, just explain what's happening at each step."
> **Result:** A logic map of the cooking process.

**Step 2: Architecture (The Planner)**
> **Prompt:** "Using the explanation above, outline a modern recipe structure (Ingredients list, then numbered steps) to achieve the same result."
> **Result:** A skeleton plan.

**Step 3: Implementation (The Generator)**
> **Prompt:** "Write the full modern recipe based on the skeleton plan, with precise measurements (cups, teaspoons, minutes)."
> **Result:** The finished recipe.

**Step 4: Verification (The Critic)**
> **Prompt:** "Compare the original recipe's steps with the new modern version. Is anything missing or changed?"

**Reflection:**
If you'd just asked "modernize this recipe" in one shot, it might have quietly dropped a key step or ingredient. Chaining ensures nothing important gets lost in translation.

---

## Interactive Daily Quiz

### Question 1 (Definition)
**What is Prompt Chaining?**

A) Using multiple monitors.
B) Using the output of one prompt as the input for the next prompt.
C) Asking the same question twice.
D) Using AI on a blockchain.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It creates a pipeline of tasks, each building on the last.

### Question 2 (Benefit)
**Why break a task into a chain?**

A) To make things more complicated on purpose.
B) To isolate errors. If Step 1 is wrong, you catch and fix it before it affects Step 2 and beyond.
C) To use more electricity.
D) It is mandatory for all AI use.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Error isolation and quality control are the main benefits.

### Question 3 (Structure)
**True or False: You should change Personas between links in a chain.**

A) False.
B) True. It is often beneficial (e.g., "organizer" for step 1, "writer" for step 2).

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Use the best "specialist persona" for each link in the chain.

### Question 4 (Agents)
**What distinguishes a "Chain" from an "Agent"?**

A) Nothing, they're identical.
B) A Chain is usually linear (A->B->C, fixed in advance). An Agent is often more autonomous (it decides on its own whether it needs to go to B or C).
C) Agents cost more money in every case.
D) Chains are only used for code.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Chains are defined workflows you design. Agents have more of a "decision loop" built in.

### Question 5 (Practice)
**Which task requires chaining?**

A) "What is the capital of France?"
B) "Read this 50-page personal journal, pull out the recurring themes, compare them to last year's journal, and write a short reflection."
C) "Translate 'hello' to Spanish."
D) "Give me a synonym for 'happy.'"

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is a multi-step cognitive process (Read -> Extract -> Compare -> Write) that benefits from being broken into stages.

---

### Summary
Today you moved from being a Prompter to being an **Architect**. You learned how to chain prompts together to build reliable workflows. Tomorrow, we review Week 4 and build your own mini "Troubleshooting Agent."
