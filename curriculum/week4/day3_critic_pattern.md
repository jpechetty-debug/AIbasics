---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
title: 'Week 4 - Day 3: The Critic Pattern (Iterative Refinement)'
week: 4
---

# Week 4 - Day 3: The Critic Pattern (Iterative Refinement)

## Overview
**Week 4 – Day 3**  
**Topic:** The Critic Pattern - Argue Your Way to Perfection  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Use the "Critic Pattern" to audit AI output.
2. Force the AI to review its own code for security flaws.
3. Iteratively improve a prompt by asking the AI for feedback.

---

## Lesson Content

### The "Yes Man" Problem
AI models are trained to be helpful assistants. They hate to say "No" or point out flaws unless asked. If you write bad code, the AI might praise it.

**The Critic Pattern** assigns a specific persona to critique the output.

### Role 1: Self-Correction
**User:** "Write a Python script to backup files."
**AI:** *[Outputs a script]*
**User (Critic):** "Review your code above. Does it handle open files errors? Does it log failures? Rewrite it to handle these edge cases."

This 2-step process (Generate -> Critique -> Fix) often produces production-grade code where a single step fails.

### Role 2: The Security Auditor
**Scenario:** You pasted a firewall config.
**Prompt:**
> "Act as a Senior Security Engineer. Review the configuration above. Point out any security risks, overly permissive rules, or compliance violations. Be harsh."

**Result:** "Rule 10 permits 'Any' to Port 3389 (RDP). This is a critical risk."

### Role 3: The Prompt Impver
You can ask the AI to critique **your prompt**.

**Prompt:**
> "I want to ask you to write a summary of this document. Here is my draft prompt: 'Summarize this.'
> Critique my prompt. How can I make it better to get a bulleted executive summary?"

**AI Response:** "Your prompt is too vague. Try: 'Act as a Business Analyst. Summarize the key findings in 5 bullet points focused on ROI.'"

---

## Hands-On Exercise

### Exercise: The "Code Review"

**Objective:** Use the Critic Pattern to find a bug in a generated script.

**Step 1: Generate a Flawed Script**
> "Write a python script that divides two numbers input by the user."
*(Likely output: `print(a/b)`)*

**Step 2: Apply the Critic**
> "Review the code. What happens if the user inputs Zero? What happens if they input text?"

**Step 3: The Fix**
> "Rewrite the code to handle ZeroDivisionError and ValueError."

**Reflection:**
You utilized the AI's knowledge of errors to fix its own oversight. You simulated "Pair Programming."

---

## Interactive Daily Quiz

### Question 1 (Concept)
**What is the core idea of the Critic Pattern?**

A) To insult the AI.  
B) To ask the AI to evaluate an output (its own or yours) against specific criteria before accepting it.  
C) To get free movie reviews.  
D) To make the font red.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It adds a Quality Assurance (QA) step.

### Question 2 (Persona)
**Which Persona is best for finding vulnerabilities?**

A) "Act as a Helpful Friend."  
B) "Act as a Pessimistic Security Auditor who trusts nothing."  
C) "Act as a Clown."  
D) "Act as a Database."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Biasing the model towards "Pessimism" and "Distrust" helps it find edge cases it would otherwise ignore to be "nice."

### Question 3 (Workflow)
**Why is "Generate -> Critique -> Fix" better than just "Generate"?**

A) It takes longer.  
B) It mimics the human drafting process. First drafts are rarely perfect. The review step catches errors.  
C) It allows the AI to sleep.  
D) It isn't better.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Iteration is the key to quality.

### Question 4 (Prompt Improvement)
**You want to write a complex prompt but don't know how. What can you ask the AI?**

A) "I give up."  
B) "Ask me clarifying questions about my goal so you can generate the perfect prompt for me."  
C) "Write it yourself."  
D) "Guess."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** asking the AI to "profile" your needs is a powerful meta-prompting technique.

### Question 5 (Safety)
**Can the Critic Pattern catch 100% of bugs?**

A) Yes.  
B) No. It is still probabilistic. It might miss subtle logic errors.  
C) Only on Tuesdays.  
D) Yes, if you use GPT-4.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It reduces risk, but does not eliminate it. Human review is still final.

---

### Summary
Today you learned to stop accepting the first draft. The **Critic Pattern** turns the AI into a partner that reviews code, checks security, and even improves your prompts. Tomorrow, we connect everything with **Prompt Chaining**.