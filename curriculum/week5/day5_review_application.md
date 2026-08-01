---
difficulty: Intermediate
duration: ~90 minutes
tags:
- prompting
- python
- agents
- automation
title: 'Week 5 - Day 5: Review & Mini-Project'
week: 5
---

# Week 5 - Day 5: Review & Mini-Project

## Overview
**Week 5 – Day 5**
**Topic:** Review & Mini-Project: The Automation Agent
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Review Python, Spreadsheet Automation, Regex, and Documentation patterns.
2. Build a complete "Automation Agent" workflow (Plan -> Code -> Document).
3. Complete the Week 5 Assessment.

---

## Lesson Content

### The Full Stack Workflow

You now have the full stack of skills to operate as an "AI-Augmented Everyday Automator."

1.  **Plan:** Use AI to outline the solution (`Generative`).
2.  **Code:** Use AI to write the Python script or spreadsheet macro (`Generator`).
3.  **Parse:** Use AI to write Regex/parsers for messy input (`Extractor`).
4.  **Document:** Use AI to write clear comments and READMEs (`Summarizer`).

---

## Hands-On Mini-Project

### Project: The "Personal Expense Auditor"

**Objective:** Create a full mini-toolkit to audit your own monthly spending.

**Step 1: The Plan (Chain Link 1)**
> **Prompt:** "I want to review my monthly expenses and flag any category where I spent more than $200. Outline a Python script's logic to do this from a CSV file."
> **Output:** Plan (Read CSV -> Group by category -> Compare to $200 -> Report flagged categories).

**Step 2: The Parser (Chain Link 2)**
> **Prompt:** "Write a Python function to read a CSV with columns Date, Category, Amount, and return a dictionary of total spending per category."
> **Output:** A parsing function.

**Step 3: The Code (Chain Link 3)**
> **Prompt:** "Write the full script based on the plan. Use the parsing function above. Output a summary showing categories over $200."
> **Output:** The Python script.

**Step 4: The Documentation (Chain Link 4)**
> **Prompt:** "Write a README.md for this script. Explain how to run it and what the CSV format should look like."
> **Output:** `README.md`.

**Step 5: Peer Review (The Critic)**
> **Prompt:** "Review the script. Does it handle a CSV with missing or blank amounts correctly?"

**Submission:**
You now have a small folder with `audit.py` and `README.md`, created far faster than doing it fully manually.

---

## Weekly Interactive Quiz

### Question 1 (Tool Selection)
**You need to apply the same formula-based calculation across hundreds of spreadsheet rows every week. Which tool is the "best fit"?**

A) A fully custom Python script from scratch every time.
B) A spreadsheet formula or automated macro (reusable and simple to maintain).
C) Manually typing each result.
D) A regex pattern.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** For repeated spreadsheet-based calculations, a formula or macro is usually the simplest, most maintainable choice.

### Question 2 (Python)
**Which library is the standard, beginner-friendly way to make web API calls in Python?**

A) `requests`
B) `PyGame`
C) `NumPy`
D) `turtle`

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** `requests` is the standard library for calling web APIs.

### Question 3 (Parsing)
**Why use AI to write Regex?**

A) Regex syntax is hard to memorize and error-prone. AI is a pattern-matching machine.
B) It isn't helpful.
C) Everyone should memorize every regex token by hand.
D) Regex is obsolete.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Offloading the syntax of regex to AI is a genuine productivity boost.

### Question 4 (Documentation)
**A Docstring is found where?**

A) At the end of the file.
B) Immediately after a function or class definition, inside triple quotes.
C) In the README only.
D) In an email.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** `def func(): """Docstring"""`

### Question 5 (Evolution)
**The shift from "Manual Coding" to "AI-Assisted Coding" for a beginner means:**

A) You stop thinking about the problem.
B) You shift from being a "Typist" to being a "Planner" and "Reviewer."
C) You get penalized for using AI.
D) You only write implementation plans and never see any code.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You focus on the *design* and the *quality check*, letting AI handle a lot of the raw typing.

---

### End of Week 5
**Congratulations!** You are now an **AI-Augmented Everyday Automator**.
You can generate scripts, spreadsheet automations, and parsers at high speed.
**Next Week:** We move to **Low-Code AI Apps**—building chatbots and tools without writing complex backend code.
