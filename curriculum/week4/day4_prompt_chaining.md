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
> "Read these logs, identify the errors, write a script to fix them, and draft an email to the boss."
*(This fails. The AI tries to do too much at once and hallucinates.)*

**The Chain Strategy (Good):**
1.  **Prompt A (Analyst):** "Identify the errors in these logs." -> *Output A*
2.  **Prompt B (Coder):** "Write a script to fix the errors listed in *Output A*." -> *Output B*
3.  **Prompt C (Writer):** "Write an email summarizing the fix in *Output B*." -> *Output C*

This is **Prompt Chaining**. It is the foundation of AI Agents.

### Why Chain?
1.  **Context Window Management:** You process data in chunks.
2.  **Specialization:** Different "Personas" for different steps (Analyst vs Coder vs Writer).
3.  **Checkpointing:** You can verify Step 1 before moving to Step 2.

### Step-by-Step: The "Documentation Builder" Chain

**Goal:** Create a user manual for a Python script.

**Link 1: The Reader**
> "Read this Python code. List every function and what it does in simple English."
> *Output: Function List.*

**Link 2: The Example Generator**
> "For each function in the list above, generate a code example showing how to use it."
> *Output: Usage Examples.*

**Link 3: The Formatter**
> "Combine the Function Descriptions and Usage Examples into a Markdown document."
> *Output: Final Manual.*

---

## Hands-On Exercise

### Exercise: The "Legacy Code Refactor" Chain

**Objective:** Safely rewrite a legacy Perl script into Python.

**Step 1: Comprehension (The Translator)**
> **Prompt:** "Explain this Perl script line-by-line. Do not rewrite it yet. Just explain the logic."
> **Result:** A logic map.

**Step 2: Architecture (The Planner)**
> **Prompt:** "Using the logic map above, outline a Python script structure (Functions/Classes) to achieve the same goal."
> **Result:** A skeleton plan.

**Step 3: Implementation (The Generator)**
> **Prompt:** "Write the Python code based on the skeleton plan."
> **Result:** The Python Code.

**Step 4: Verification (The Critic)**
> **Prompt:** "Compare the original Perl logic with the new Python code. Are any steps missing?"

**Reflection:**
If you just asked "Convert this Perl to Python" in one shot, it might miss subtle logic. Chaining ensures fidelity.

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
- **B) ✓ Correct!** It creates a pipeline of tasks.

### Question 2 (Benefit)
**Why break a task into a chain?**

A) To annoy the AI.  
B) To isolate errors. If Step 1 fails, you fix it before wasting tokens on Step 2.  
C) To use more electricity.  
D) It is mandatory.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Error isolation and quality control are the main benefits.

### Question 3 (Structure)
**True or False: You should change Personas between links in a chain.**

A) False.  
B) True. It is often beneficial (e.g., Engineer for step 1, Comm Specialist for step 2).  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Use the best specialist for each "Link" in the chain.

### Question 4 (Agents)
**What distinguishes a "Chain" from an "Agent"?**

A) Nothing.  
B) A Chain is usually linear (A->B->C). An Agent is often autonomous (A decides if it needs to go to B or C).  
C) Agents costs money.  
D) Chains are made of metal.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Chains are defined workflows. Agents have a "decision loop."

### Question 5 (Practice)
**Which task requires chaining?**

A) "What is the capital of France?"  
B) "Read this 50-page Report, Extract the financial data, Compare it to last year's data, and Write a forecast."  
C) "Write a for loop."  
D) "Translate 'Hello' to Spanish."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is a multi-step cognitive process (Read -> Extract -> Compare -> Write).

---

### Summary
Today you moved from being a Prompter to being an **Architect**. You learned how to chain prompts together to build reliable workflows. Tomorrow, we review Week 4 and build your own "Troubleshooting Agent."
