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
**Topic:** The Critic Pattern - Argue Your Way to a Better Result
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Use the "Critic Pattern" to audit AI output.
2. Force the AI to review its own draft for mistakes or gaps.
3. Iteratively improve a prompt by asking the AI for feedback.

---

## Lesson Content

### The "Yes Man" Problem
AI models are trained to be helpful assistants. They tend to avoid saying "No" or pointing out flaws unless asked. If you get a mediocre first draft, the AI might act like it's great.

**The Critic Pattern** assigns a specific persona to critique the output.

### Role 1: Self-Correction
**User:** "Write a simple Python script that divides two numbers I type in."
**AI:** *[Outputs a basic script]*
**User (Critic):** "Review your code above. What happens if I type in the number 0 as the second number? What happens if I type in text instead of a number? Rewrite it to handle these situations gracefully."

This 2-step process (Generate -> Critique -> Fix) often produces a much more solid result than a single step.

### Role 2: The Skeptical Reviewer
**Scenario:** You're about to reply to an online marketplace listing to buy a used couch.
**Prompt:**
> "Act as a skeptical consumer advocate. Review the listing description below. Point out any red flags, vague details, or signs this could be a scam. Be thorough and a little harsh."

**Result:** "The seller won't allow an in-person pickup and insists on a wire transfer only — that's a major red flag for a scam. Also, the price is unusually low for this item's condition."

### Role 3: The Prompt Improver
You can ask the AI to critique **your prompt**.

**Prompt:**
> "I want to ask you to summarize this article. Here is my draft prompt: 'Summarize this.'
> Critique my prompt. How can I make it better to get a clear, bulleted summary?"

**AI Response:** "Your prompt is too vague. Try: 'Summarize the key points of this article in 5 bullet points, written for someone who hasn't read it.'"

---

## Hands-On Exercise

### Exercise: The "Code Review"

**Objective:** Use the Critic Pattern to find a bug in a generated script.

**Step 1: Generate a Flawed Script**
> "Write a simple Python script that divides two numbers a user types in."
*(Likely output: `print(a/b)`)*

**Step 2: Apply the Critic**
> "Review the code. What happens if the user inputs 0 for the second number? What happens if they type in text instead of a number?"

**Step 3: The Fix**
> "Rewrite the code to handle both of those situations gracefully with a friendly error message."

**Reflection:**
You used the AI's own knowledge of common mistakes to catch and fix its own oversight. You simulated a mini "pair programming" session.

---

## Interactive Daily Quiz

### Question 1 (Concept)
**What is the core idea of the Critic Pattern?**

A) To insult the AI.
B) To ask the AI to evaluate an output (its own or yours) against specific criteria before accepting it.
C) To get free movie reviews.
D) To change the font color.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It adds a quality-check step before you trust or use the result.

### Question 2 (Persona)
**Which Persona is best for spotting red flags in an online listing?**

A) "Act as a Helpful Friend."
B) "Act as a Skeptical Consumer Advocate who trusts nothing at face value."
C) "Act as a Comedian."
D) "Act as a Calculator."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Biasing the model toward "skepticism" and "distrust" helps it surface issues it would otherwise politely ignore.

### Question 3 (Workflow)
**Why is "Generate -> Critique -> Fix" better than just "Generate"?**

A) It takes longer for no reason.
B) It mimics the human drafting process. First drafts are rarely perfect, and the review step catches errors.
C) It allows the AI to rest.
D) It isn't actually better.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Iteration is the key to quality, whether it's writing, code, or a plan.

### Question 4 (Prompt Improvement)
**You want to write a complex prompt but aren't sure how. What can you ask the AI?**

A) "I give up."
B) "Ask me clarifying questions about my goal so you can help me write the best possible prompt."
C) "Write it yourself, I don't care."
D) "Just guess."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Asking the AI to help you clarify your own goal is a powerful meta-prompting technique.

### Question 5 (Safety)
**Can the Critic Pattern catch 100% of mistakes?**

A) Yes, always.
B) No. It is still probabilistic and might miss subtle errors.
C) Only on certain days of the week.
D) Yes, if you use a premium model.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It reduces risk but doesn't eliminate it. Your own final review still matters, especially for anything important.

---

### Summary
Today you learned to stop accepting the first draft. The **Critic Pattern** turns the AI into a partner that reviews writing, checks for red flags, and even improves your prompts. Tomorrow, we connect everything with **Prompt Chaining**.
