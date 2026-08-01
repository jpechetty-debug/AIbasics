---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
title: 'Week 5 - Day 2: AI for Spreadsheet & Macro Automation'
week: 5
---

# Week 5 - Day 2: AI for Spreadsheet & Macro Automation

## Overview
**Week 5 – Day 2**
**Topic:** Generating Spreadsheet Formulas and Macros with AI
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Generate complex spreadsheet formulas (Excel/Google Sheets) using AI.
2. Use AI to convert a manual task into an automated macro or script.
3. Validate AI-generated formulas before trusting them with real data.

---

## Lesson Content

### The Formula Headache

Spreadsheets are powerful, but formula syntax is easy to get wrong.
- "Is that a comma or a semicolon between arguments?"
- "Do I need dollar signs to lock that cell reference?"

**AI is a fantastic formula generator.** It rarely makes syntax mistakes, and it can explain exactly what it wrote.

### Use Case 1: Plain English to Formula

**The Problem:** You know what you want in plain English: "If the amount in column B is over $100, mark it as 'Review' in column C, otherwise mark it 'OK'."

**The Prompt:**
> **Task:** Write a Google Sheets/Excel formula for this logic: If the value in B2 is over 100, output "Review", otherwise output "OK".
> **Constraint:** Show the formula ready to paste into cell C2, and explain each part briefly.

**The Output:**
```
=IF(B2>100, "Review", "OK")
```

### Use Case 2: The Full Automation (Macro)

**The Prompt:**
> **Task:** Write a Google Apps Script that automatically sends me an email summary every Monday morning listing any spreadsheet rows marked "Review" from last week.
> **Steps:**
> 1. Loop through all rows.
> 2. Collect any row where column C says "Review".
> 3. Email me (my address) a simple bulleted list.
> **Trigger:** Should run automatically every Monday at 8am.

**The Output:**
A complete Apps Script function, plus instructions on how to set up the time-based trigger in the Apps Script editor.

### Use Case 3: The "Nested Formula" Decoder

Long spreadsheet formulas someone else wrote can look like a wall of parentheses.

**The Prompt:**
> **Task:** Explain what this formula does, step by step, in plain English.
> **Input:** `=IFERROR(VLOOKUP(A2,Sheet2!A:B,2,FALSE),"Not Found")`

**The Output:**
"This looks up the value in cell A2 within a table on Sheet2. If it finds a match, it returns the corresponding value from column B. If no match is found (which would normally show an error), it displays 'Not Found' instead."

---

## Hands-On Exercise

### Exercise: The "Household Budget Tracker" Automation

**Objective:** Create an automated monthly budget summary.

**Step 1: The Prompt**
> "Write a Google Sheets formula that adds up all expenses in column B where the category in column A is 'Groceries', and shows the total in cell E1."

**Step 2: The Critic Check**
> A common mistake: does the formula only sum an exact match, or would it accidentally include "Groceries - Bulk" too?
> **Prompt:** "Check this formula. Would it match 'Groceries' exactly, or partially match other categories too?"

**Step 3: Verification**
> **Prompt:** "Explain exactly what `SUMIF` does versus `SUMIFS` in this context, and when I'd need the second one."

**Reflection:**
Spreadsheet formula documentation is dense and often confusing. AI acts like a patient tutor who writes the formula for you and explains it in plain terms.

---

## Interactive Daily Quiz

### Question 1 (Syntax)
**What happens if you mismatch a comma or parenthesis in a spreadsheet formula?**

A) It works fine anyway.
B) The formula shows an error or doesn't calculate correctly.
C) It runs faster.
D) Nothing happens.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Formula syntax is precise. AI helps avoid these small but frustrating errors.

### Question 2 (Conversion)
**You ask AI: "Turn my weekly manual task of copying data between two sheets into an automatic script." What kind of tool should it generate?**

A) A single static formula
B) A macro/script (like Google Apps Script or an Excel macro) that runs automatically
C) A printed instruction sheet
D) A new spreadsheet template only

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Repeated, multi-step manual tasks are best automated with a script/macro rather than a single formula.

### Question 3 (Structure)
**Can AI help you design an entire spreadsheet layout (which columns to use, what each tab is for)?**

A) Yes, describe your goal and ask it to suggest a layout, then refine from there.
B) No.
C) Only for accounting professionals.
D) No, it only writes single formulas.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** "Suggest a simple spreadsheet layout for tracking my monthly budget" is a great starting prompt.

### Question 4 (Automation Triggers)
**What lets a spreadsheet macro run automatically on a schedule (e.g., every Monday) instead of manually?**

A) A magic formula
B) A time-based trigger set up in the scripting tool
C) Restarting your computer
D) Printing the sheet

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI can write the trigger setup instructions along with the script itself.

### Question 5 (Safety)
**The AI suggests a macro that automatically emails your full spreadsheet (including sensitive personal data) to an address you didn't specify. Is this good practice?**

A) Yes, run it as-is.
B) No. Always double-check that any automated email/sharing step only sends what you intend, to who you intend.
C) Yes, it's convenient.
D) It doesn't matter.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Always critique AI-generated automations for unintended data sharing before running them.

---

### Summary
Today you conquered formulas and macros. You used AI to generate **spreadsheet formulas** and **automation scripts**, turning plain English requirements into working tools. Tomorrow, we explore **Regex** and text parsing.
