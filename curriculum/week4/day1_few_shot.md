---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
title: 'Week 4 - Day 1: The Power of Examples (Few-Shot)'
week: 4
---

# Week 4 - Day 1: The Power of Examples (Few-Shot)

## Overview
**Week 4 – Day 1**
**Topic:** Few-Shot Prompting - Teaching by Example
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Distinguish between Zero-Shot, One-Shot, and Few-Shot prompting.
2. Use "Few-Shot" prompting to drastically improve output consistency.
3. Guide the AI to copy a specific format using examples.

---

## Lesson Content

### Zero-Shot vs. Few-Shot

Most people use **Zero-Shot** prompting:
> "Write a poem about autumn."
> *(No examples given. You get whatever the AI feels like.)*

**One-Shot** adds a single example:
> "Write a short poem about autumn. Style it like this example: 'Leaves turn to gold / Crisp air fills the morning walk / Summer says goodbye.'"

**Few-Shot** provides multiple examples to define a pattern. This is the **most powerful** technique for consistent formatting.

### The "Clone My Style" Technique

**Scenario:** You want the AI to write labels for your pantry organization bins, but you have a very specific personal style.

**Zero-Shot (Fail):**
> **Prompt:** "Write labels for these 3 bins."
> **Output:** "Bin 1: Snacks. Bin 2: Pasta. Bin 3: Baking." *(Too generic, doesn't match your style).*

**Few-Shot (Success):**
> **Prompt:** "Generate labels for these new bins, following the pattern below."
> **Examples:**
> Input: Crackers, chips -> Label: 🥨 SNACKS - EAT FIRST
> Input: Rice, beans -> Label: 🍚 GRAINS - PANTRY LEFT
> **Task:**
> Input: Flour, sugar, baking soda
> Input: Canned soup, canned beans

> **Output:**
> Label: 🧁 BAKING - PANTRY RIGHT
> Label: 🥫 CANNED GOODS - PANTRY LEFT

*The AI deduced the pattern (Emoji + Category + Location note) without being explicitly told the rules.*

### Why It Works
LLMs are "Pattern Completion Engines." When you give examples, you set the pattern. The AI just wants to complete it. It is easier to *show* the pattern than to *explain* it.

> [!IMPORTANT]
> **Ethics Checkpoint: Data Privacy in Examples**
> When using Few-Shot prompting, you are often providing snippets of your actual personal life or work.
> - **Sensitive Data**: Never include real passwords, account numbers, or other people's personal information in your few-shot examples.
> - **Ownership**: Remember that prompts sent to public AI models (like ChatGPT or Claude) may be used for future training. Be mindful of what personal details you're comfortable sharing with a third-party provider.

---

## Hands-On Exercise

### Exercise: The "Budget Tracker Formatter"

**Objective:** Force the AI to output a specific, personal format for tracking your spending.

**Scenario:** Your budget spreadsheet needs entries in this exact style: `{"category": "X", "amount": Y}`.

**Step 1: Write the Few-Shot Prompt**
> **System:** You are a budget entry formatter.
> **Task:** Convert the natural language description into the custom format.
> **Examples:**
> User: "Spent $12 on lunch" -> `{"category": "Food", "amount": 12}`
> User: "Paid $45 for gas" -> `{"category": "Transport", "amount": 45}`
> **User:** "Bought a $30 birthday gift for my sister"

**Step 2: Predicted Output**
`{"category": "Gifts", "amount": 30}`

**Reflection:**
If you hadn't given examples, it probably would have used keys like `type` or `cost` instead of `category` and `amount`. Examples constrain the vocabulary to exactly what you need.

---

## Interactive Daily Quiz

### Question 1 (Concepts)
**What is "Zero-Shot" prompting?**

A) Asking for help with zero hope.
B) Asking the AI to perform a task without providing any examples.
C) Prompting with zero words.
D) A type of coffee order.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It relies entirely on the model's training data, with no examples to guide the format.

### Question 2 (Benefits)
**Why is Few-Shot prompting effective for getting a very specific personal format (like your own budget-tracking style)?**

A) It isn't.
B) It "reminds" the model of your exact preferred pattern by showing valid examples, reducing generic or mismatched output.
C) It makes the model faster.
D) It uses less tokens.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Examples prime the model's context toward exactly what you want, rather than a generic guess.

### Question 3 (Quantity)
**How many examples should you generally provide for "Few-Shot"?**

A) 100+
B) 1-3 is usually sufficient.
C) Zero.
D) 50.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** 1 example (One-Shot) helps a lot. 2-3 examples (Few-Shot) is usually the sweet spot for accuracy vs. length.

### Question 4 (Formats)
**You want the AI to write a consistent set of thank-you note openers. Which prompt is better?**

A) "Write some thank-you note openers."
B) "Write thank-you note openers. Example: 'Gift: a scarf' -> 'Thank you so much for the beautiful scarf!' Task: 'Gift: a book.'"

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Providing an example guarantees the output uses the tone and structure you actually want.

### Question 5 (Debugging)
**The AI keeps formatting dates as "MM/DD/YYYY" but you need "YYYY-MM-DD". Simply asking clearly didn't work. What should you do?**

A) Give up and format them by hand.
B) Use Few-Shot prompting. Give 2-3 examples of inputs and the mapped outputs in the exact format you need.
C) Try a different app entirely.
D) Write a Python script instead.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Showing is often more effective than telling, especially for exact formatting.

---

### Summary
Today you learned that **Examples > Instructions**. When you need specific formatting or logic, don't just ask for it—show the AI what "Good" looks like. Tomorrow, we teach the AI how to *think*.
