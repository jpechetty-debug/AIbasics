---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
- agents
- automation
title: 'Week 5 - Day 4: AI for Documentation'
week: 5
---

# Week 5 - Day 4: AI for Documentation

## Overview
**Week 5 – Day 4**
**Topic:** Automated Documentation (Docstrings, READMEs, Comments)
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Use AI to auto-generate Python Docstrings.
2. Generate a clear README.md file for a small personal project.
3. Use AI to comment unclear code for better understanding.

---

## Lesson Content

### The "Future You" Problem

If you write a script today and come back to it in six months, will you remember why you wrote it that way?
**Documentation is a gift to your future self** (and to anyone else who might use your project). Most people find it tedious to write. AI doesn't.

### Use Case 1: Docstrings

**Scenario:** You wrote a function but left it bare.

**The Code:**
```python
def check_budget(spent, limit):
    remaining = limit - spent
    return remaining >= 0
```

**The Prompt:**
> "Add a clear Python docstring to this function. Explain the arguments and what it returns."

**The Output:**
```python
def check_budget(spent, limit):
    """Checks whether spending is within budget.

    Args:
        spent (float): Amount already spent.
        limit (float): The budget limit.

    Returns:
        bool: True if spending is within the limit, False otherwise.
    """
    ...
```

### Use Case 2: The README

**Scenario:** You have a small project folder with `tracker.py` and `expenses.csv`.

**The Prompt:**
> "Write a README.md for this project.
> - Title: Personal Expense Tracker.
> - Features: Reads a CSV of expenses and totals spending by category.
> - Usage: `python tracker.py`.
> - Requirements: Just standard Python, no extra installs needed.
> - Add a short note about keeping the CSV file backed up."

**The Output:** A clean, well-organized Markdown file with a description, installation steps, and usage examples.

### Use Case 3: Explaining "Magic" Code

**Scenario:** You inherited (or found online) a script with a confusing line.
`data = [x for x in raw if x['status'] == 'active' and x['amount'] > 100]`

**The Prompt:**
> "Add a comment above this line explaining exactly what it filters, in plain English."

**The Output:**
`# Keep only entries that are marked "active" and have an amount over 100`

---

## Hands-On Exercise

### Exercise: The "Self-Documenting" Script

**Objective:** Take a rough script and polish it.

**Step 1: Write (or generate) a rough script**
A simple script that calculates a tip and splits a bill among friends, with no comments.

**Step 2: The "Polisher" Prompt**
> "Refactor this script.
> 1. Add clear variable names if any are unclear.
> 2. Add a docstring to any function.
> 3. Add short inline comments explaining the trickier lines."

**Step 3: Compare**
Compare the "Raw" script vs. the "Polished" script. Which one would you rather come back to in six months?

**Reflection:**
Clear comments and docstrings make any script easier to trust and reuse later. AI makes adding them nearly zero-effort.

---

## Interactive Daily Quiz

### Question 1 (Definition)
**What is a "Docstring"?**

A) A string used to tie documents together.
B) A special comment string used to document a specific piece of code (like a function).
C) A variable type.
D) A type of computer virus.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** In Python, it's the triple-quoted string right after a function or class definition.

### Question 2 (Clarity)
**Why add clear variable names and comments to your scripts?**

A) It makes the code run faster.
B) It helps you (and anyone else, including AI helping you later) understand what the code is meant to do, preventing confusion and mistakes.
C) It is required by law.
D) It makes the file smaller.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Clarity helps humans and tools alike understand your intent.

### Question 3 (README)
**What is the first file most people look at when they open a shared project folder or repository?**

A) `main.py`
B) `data.csv`
C) `README.md`
D) `license.txt`

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** A good README is the "front door" of your project.

### Question 4 (Maintenance)
**You change the code logic but forget to update the comments. This is called:**

A) Code Drift / Comment Rot.
B) Good practice.
C) Innovation.
D) Security.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Misleading comments are worse than no comments at all. Use AI to "Update the comments to match the new code."

### Question 5 (Process)
**Can AI help you write a clear summary of what changed in your script, for your own notes or to share with a friend?**

A) No.
B) Yes. "Summarize these 3 changes I made to my script into a short, plain-English changelog."
C) Only for professional software teams.
D) Never.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The Translator Pattern applies here too: turning code changes into a plain-English summary.

---

### Summary
Today you cleaned up. You learned to use AI to generate **docstrings**, **comments**, and **READMEs**. This transforms "quick hack" code into something you (and others) can actually trust and reuse. Tomorrow, we verify your skills with a full mini-project.
