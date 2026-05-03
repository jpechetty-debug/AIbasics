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
2. Use AI to write Python parser logic (TextFSM substitute).
3. "Explain" a complex Regex string found in legacy code.

---

## Lesson Content

### The Regex Barrier

Regex is write-only code. `^(\d{1,3}\.){3}\d{1,3}$` matches an IP, but it hurts to read.
AI *loves* Regex. It is a pattern matching engine matching patterns.

### Task 1: Generate Regex

**Scenario:** You need to extract the Mac Address from a log line: `Host 0011.2233.4455 flapping`.

**The Prompt:**
> "Write a Regular Expression (Python flavor) to match a Cisco format mac address (xxxx.xxxx.xxxx) from a string."

**The Output:**
`r'[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}'`

### Task 2: Explain Regex

**Scenario:** You find this in a script: `r'^(?:[0-9a-fA-F]:?){12}$'`

**The Prompt:**
> "Explain this regex pattern step by step."

**The Output:**
1. `^`: Start of string.
2. `(?: ... )`: Non-capturing group.
3. `[0-9a-fA-F]`: Hex character.
4. `:?`: Optional colon.
5. `{12}`: Repeat 12 times.
**Summary:** It matches a standard Mac Address (like AA:BB:CC...).

### Task 3: The "Parser Generator"

**Scenario:** You have the output of `show cdp neighbors detail`. It's messy. You want a Dictionary.

**The Strategy:** Don't ask for Regex. Ask for a **Function**.

**The Prompt:**
> **Task:** Write a Python function `parse_cdp(output_string)` that takes the text below and returns a list of dictionaries.
> **Fields:** Device ID, IP Address, Platform.
> **Example Input:** [Paste CLI Output].

**The Output:**
The AI will likely write a function using `re.finditer` or simple string splitting to build your data structure.

---

## Hands-On Exercise

### Exercise: The "Log Scraper"

**Objective:** Parse an Apache Access Log.

**Log Sample:**
`192.168.1.5 - - [10/Oct/2023:13:55:36] "GET /index.html HTTP/1.1" 200 2326`

**Step 1: The Prompt**
> "Write a Python Regex to capture the IP, Timestamp, and HTTP Status Code from this log line."
> [Paste Sample]

**Step 2: The Test**
> "Generate a Python script to test this regex against the sample."

**Reflection:**
Writing that regex manually involves counting brackets and spaces. AI does it instantly.

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
- **B) ✓ Correct!** `import re` is standard.

### Question 3 (Debugging)
**Your Regex matches the IP `999.999.999.999`. What failed?**

A) Nothing, that's a valid IP.  
B) The Regex `\d{1,3}` allows any 3 digits (0-999). It didn't validate the 0-255 range.  
C) The computer is broken.  
D) AI hates numbers.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI often provides "Syntactic" matches, not "Semantic" validation. You need to ask for "Strict IP validation" or handle logic in code.

### Question 4 (TextFSM)
**Can AI write TextFSM templates (used by Netmiko)?**

A) No.  
B) Yes! You can paste the raw CLI output and ask "Write a TextFSM template to parse this."  
C) Only XML.  
D) Only JSON.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is a huge timesaver for creating custom Netmiko parsers.

### Question 5 (Safety)
**What is "ReDoS" (Regex Denial of Service)?**

A) A fast regex.  
B) A poorly written regex that takes infinite time to process specific inputs, crashing the CPU.  
C) A red operating system.  
D) A refund.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Another reason to "Critique" AI regex: "Is this efficient? Is it vulnerable to catastrophic backtracking?"

---

### Summary
Today you mastered the art of text extraction. You learned to generate **Regex**, **Parsers**, and **TextFSM** templates, turning the unstructured CLI world into structured data. Tomorrow, we look at the most hated part of coding: **Documentation**.