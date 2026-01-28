# Week 5 - Day 5: Review & Mini-Project

## Overview
**Week 5 – Day 5**  
**Topic:** Review & Mini-Project: The Automation Agent  
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Review Python, Ansible, Regex, and Documentation patterns.
2. Build a complete "Automation Agent" workflow (Plan -> Code -> Document).
3. Complete the Week 5 Assessment.

---

## Lesson Content

### The Full Stack Workflow

You now have the full stack of skills to operate as an "AI-Augmented Network Engineer."

1.  **Plan:** Use AI to outline the solution (`Generative`).
2.  **Code:** Use AI to write the Python/Ansible (`Generator`).
3.  **Parse:** Use AI to write Regex/Parsers (`Extractor`).
4.  **Document:** Use AI to write READMEs (`Summarizer`).

---

## Hands-On Mini-Project

### Project: The "Intelligent Interface Auditor"

**Objective:** Create a full package to audit switch interfaces.

**Step 1: The Plan (Chain Link 1)**
> **Prompt:** "I need to audit Cisco switches for ports that have been down for > 30 days. Outline a Python script logic to do this using `Netmiko`."
> **Output:** Plan (Connect -> `show interfaces` -> Parse 'Last Input' -> Report).

**Step 2: The Parser (Chain Link 2)**
> **Prompt:** "Write a Python function to parse the `Last input 00:00:21` or `Last input 4w2d` line from `show interface` output. Return the duration in days."
> **Output:** A time-parsing function.

**Step 3: The Code (Chain Link 3)**
> **Prompt:** "Write the full script based on the plan. Use the parser function above. Output a CSV file `unused_ports.csv`."
> **Output:** The Python Script.

**Step 4: The Documentation (Chain Link 4)**
> **Prompt:** "Write a README.md for this script. Explain how to install dependencies and run it."
> **Output:** `README.md`.

**Step 5: Peer Review (The Critic)**
> **Prompt:** "Review the script for safety. Does it handle 'Never' input correctly?"

**Submission:**
You now have a folder with `audit.py` and `README.md`, created 10x faster than manual coding.

---

## Weekly Interactive Quiz

### Question 1 (Tool Selection)
**You need to configure 100 switches with the exact same VLANs. Which tool is "best fit" to generate?**

A) A Python script with complex loops.  
B) An Ansible Playbook (Idempotent, readable).  
C) Manual SSH.  
D) A Regex.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** For configuration management, Ansible is usually preferred over raw Python scripts.

### Question 2 (Python)
**Which library is the de-facto standard for Network SSH in Python?**

A) Requests  
B) Netmiko  
C) PyGame  
D) NumPy  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Built by Kirk Byers, it handles the quirks of CLI devices.

### Question 3 (Parsing)
**Why use AI to write Regex?**

A) Regex syntax is hard to memorize and error-prone. AI is a pattern-matching machine.  
B) It isn't helpful.  
C) Real engineers memorize every regex token.  
D) Regex is dead.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Offloading the syntax of regex to AI is a massive productivity boost.

### Question 4 (Documentation)
**A Docstring is found where?**

A) At the end of the file.  
B) Immediately after a class or function definition, inside triple quotes.  
C) In the README.  
D) In the email.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** `def func(): """Docstring"""`

### Question 5 (Evolution)
**The shift from "Manual Coding" to "AI-Assisted Coding" means:**

A) You stop thinking.  
B) You shift from being a "Typist" to being an "Architect" and "Reviewer."  
C) You get paid less.  
D) You only write implementation plans.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You focus on the *Design* and the *Quality Assurance*, letting AI handle the *Implementation details*.

---

### End of Week 5
**Congratulations!** You are now an **AI-Augmented Automation Engineer**.
You can generate scripts, playbooks, and parsers at light speed.
**Next Week:** We move to **Low-Code AI Apps**—building Chatbots and Tools without writing complex backend code.
