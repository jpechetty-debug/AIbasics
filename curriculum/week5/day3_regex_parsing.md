---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
title: 'Week 5 - Day 3: AI for Regex & Parsing (The Extractor Pattern II)'
week: 5
---

# Week 5 - Day 3: AI for Regex & Parsing (The Extractor Pattern II)

## Overview
**Week 5 – Day 3**
**Topic:** AI for Regex & Parsing (Applying the Extractor Pattern to Code)
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Use AI to generate complex Regular Expressions (Regex).
2. Use AI to write simple Python parsing logic for messy text files.
3. "Explain" a complex Regex pattern found in someone else's code.

---

## Lesson Content

### The Regex Barrier

Regex is famously hard to read. `^[\w.-]+@[\w.-]+\.\w+$` matches an email address, but it hurts to read at a glance.
AI *loves* Regex. It is a pattern-matching engine, matching patterns.

### Task 1: Generate Regex

**Scenario:** You have a text file of customer messages and want to pull out every phone number mentioned.

**The Prompt:**
> "Write a Python Regular Expression to match a standard US phone number in formats like `(555) 123-4567` or `555-123-4567`."

**The Output:**
`r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'`

### Task 2: Explain Regex

**Scenario:** You find this in a script someone shared with you: `r'^[\w.-]+@[\w.-]+\.\w+$'`

**The Prompt:**
> "Explain this regex pattern step by step."

**The Output:**
1. `^`: Start of string.
2. `[\w.-]+`: One or more letters, numbers, dots, or dashes (the username part).
3. `@`: A literal @ symbol.
4. `[\w.-]+`: The domain name.
5. `\.\w+`: A dot followed by the extension (like .com).
6. `$`: End of string.
**Summary:** It matches a standard email address.

### Task 3: The "Parser Generator"

**Scenario:** You have a messy, exported text file of order confirmations. You want it as clean data.

**The Strategy:** Don't ask for Regex directly. Ask for a **Function**.

**The Prompt:**
> **Task:** Write a Python function `parse_orders(text)` that takes the text below and returns a list of dictionaries.
> **Fields:** Order Number, Customer Name, Total.
> **Example Input:** [Paste sample text].

**The Output:**
The AI will likely write a function using `re.finditer` or simple string splitting to build your data structure.

---

## Hands-On Exercise

### Exercise: The "Contact List Scraper"

**Objective:** Parse a messy pasted list of contacts.

**Sample Text:**
`Jane Doe, jane.doe@email.com, (555) 234-5678`

**Step 1: The Prompt**
> "Write a Python Regex to capture the Name, Email, and Phone Number from this line."
> [Paste Sample]

**Step 2: The Test**
> "Generate a Python script to test this regex against the sample and print the results."

**Reflection:**
Writing that regex manually involves careful counting of characters and symbols. AI does it instantly.

---

## Interactive Daily Quiz

### Question 1 (Analogy)
**If Regex is a "Scalpel," what is AI?**

A) The Surgeon who knows where to cut.
B) A hammer.
C) A rock.
D) A spoon.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** AI generates and wields the tool (Regex) for you.

### Question 2 (Library)
**What Python module handles Regex?**

A) `os`
B) `re`
C) `sys`
D) `pandas`

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** `import re` is the standard Python module for regex.

### Question 3 (Debugging)
**Your regex matches an obviously invalid phone number like `999-999-9999` as valid. What's going on?**

A) Nothing, that's a valid number.
B) The regex only checks the *shape* (digits and dashes), not whether the number is a real, assigned phone number.
C) The computer is broken.
D) AI hates numbers.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI often provides "Syntactic" matches (does it look like a phone number?), not "Semantic" validation (is it a real, working number?). Be aware of this limitation.

### Question 4 (Practice)
**Can AI help you write a parser for a messy, non-standard text export from an app you use?**

A) No.
B) Yes! You can paste a sample of the raw text and ask "Write a function to parse this into structured data."
C) Only for XML files.
D) Only for JSON files.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is a huge timesaver for turning any messy, repeated text format into usable data.

### Question 5 (Safety)
**What is "ReDoS" (Regex Denial of Service)?**

A) A fast regex.
B) A poorly written regex that can take an extremely long time to process certain inputs, potentially freezing your program.
C) A type of computer virus.
D) A refund process.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Another reason to "Critique" AI-generated regex: "Is this efficient? Could it hang on unusual input?"

---

### Summary
Today you mastered the art of text extraction. You learned to generate **Regex** and simple **parsers**, turning messy real-world text into clean, structured data. Tomorrow, we look at the most skipped part of scripting: **Documentation**.
