---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
title: 'Week 4 - Day 2: Chain of Thought (CoT)'
week: 4
---

# Week 4 - Day 2: Chain of Thought (CoT)

## Overview
**Week 4 – Day 2**
**Topic:** Chain of Thought (CoT) - Teaching the AI to Reason
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define "Chain of Thought" (CoT) prompting.
2. Use CoT to solve tricky multi-step math or logic problems.
3. Reduce "Hallucinations" by forcing the AI to show its work.

---

## Lesson Content

### The "Thinking" Problem

LLMs are probabilistic. They guess the next word.
If you ask: *"I have three $25 gift cards and want to buy something for $68. After the purchase, do I have at least $5 left across all cards combined?"*
The AI might instantly guess "Yes" or "No" based on a quick pattern match, often getting the arithmetic wrong.

**Chain of Thought (CoT)** forces the AI to break the problem down *before* answering.

### The Magic Phrase: "Let's think step by step."

Research showed that simply adding **"Let's think step by step"** to a prompt significantly increased accuracy on math and logic problems.

**Without CoT:**
> **User:** Do I have enough gift card balance left over?
> **AI:** Yes, you're fine. *(Might be wrong — didn't actually calculate.)*

**With CoT:**
> **User:** I have three $25 gift cards and want to buy something for $68. After the purchase, do I have at least $5 left across all cards combined? Let's think step by step.
> **AI:**
> 1. Total gift card balance: 3 × $25 = $75.
> 2. Purchase cost: $68.
> 3. Remaining balance: $75 - $68 = $7.
> 4. Is $7 ≥ $5? Yes.
> **Answer:** Yes, you'll have $7 left, which is enough.

By calculating step-by-step, the AI corrects itself.

### Use Case: Troubleshooting Logic

**Scenario:** Your car won't start this morning.
**Prompt:**
> "Analyze the potential causes for a car that won't start. Use a step-by-step reasoning chain, starting from the most common/cheap-to-check causes to the least common."

**Output:**
1.  **Check first:** Is the battery dead? (Dashboard lights dim or off)
2.  **Check next:** Is there enough fuel?
3.  **Check next:** Is the starter motor making a clicking sound?
4.  **Check last:** Could it be the ignition switch or a more complex electrical issue?

This structure ensures a comprehensive, logically ordered answer rather than a random guess.

---

## Hands-On Exercise

### Exercise: The "Trip Budget" Validator

**Objective:** Use CoT to prevent the AI from failing simple multi-step math.

**Scenario:** You're planning a road trip: 450 miles total, your car gets 30 miles per gallon, gas costs $3.60/gallon, and you're splitting the cost evenly with 2 friends.

**Step 1: Write a Standard Prompt (The Control Group)**
> "How much does each person owe for gas on this trip?"
> *(It might guess a rough number without doing the actual math correctly.)*

**Step 2: Write a CoT Prompt**
> "How much does each person owe for gas on this trip? Break down each calculation step so I can double check the math."

**Predicted Output:**
> 1. Total gallons needed: 450 miles ÷ 30 mpg = 15 gallons.
> 2. Total gas cost: 15 gallons × $3.60 = $54.
> 3. Split 3 ways (you + 2 friends): $54 ÷ 3 = $18 each.
> **Answer:** Each person owes $18.

**Reflection:**
Reasoning allows the model to access its "Logic" capabilities rather than just its "Language" capabilities.

---

## Interactive Daily Quiz

### Question 1 (Mechanism)
**How does "Chain of Thought" improve accuracy?**

A) It connects to the internet.
B) It forces the model to generate intermediate reasoning steps, which helps it arrive at the correct final answer.
C) It uses a bigger font.
D) It slows down the server.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It's like showing your work on a math test.

### Question 2 (Trigger)
**What is the classic "Zero-Shot CoT" trigger phrase?**

A) "Please."
B) "Let's think step by step."
C) "Abracadabra."
D) "Be smart."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This specific phrase triggers the reasoning behavior in most models.

### Question 3 (Application)
**When should you use CoT?**

A) "Write a birthday greeting."
B) "Calculate how much I'll save monthly if I switch to a cheaper phone plan."
C) "What color is the sky?"
D) "Translate 'thank you' to French."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Use CoT for math, logic, troubleshooting, or complex multi-step reasoning. Simple facts or creative requests don't need it.

### Question 4 (Limitations)
**Does CoT guarantee the answer is right?**

A) Yes, 100%.
B) No. The AI can still have a flaw in its logic chain.
C) Only on certain topics.
D) Yes, if you pay for a premium plan.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It significantly *improves* accuracy, but guarantees nothing. Always verify important calculations yourself.

### Question 5 (Debugging)
**The AI gives you a wrong answer. You add "Let's think step by step" and it gives you the right answer. Why?**

A) It was lying before.
B) It generated more reasoning text, allowing it to "compute" the answer step by step rather than jumping straight to a probable-sounding guess.
C) It likes you more now.
D) It restarted.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** LLMs "think" by generating text. If they output the reasoning, they condition their own next words to be more accurate.

---

### Summary
Today you learned to ask the AI to **Show Its Work**. Chain of Thought is essential for anything involving math, budgeting, or multi-step logic, where "close enough" isn't good enough. Tomorrow, we learn to argue with the AI using the **Critic Pattern**.
