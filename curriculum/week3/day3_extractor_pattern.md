---
difficulty: Intermediate
duration: ~60 minutes
tags:
- prompting
- python
- rag
- automation
title: 'Week 3 - Day 3: The Extractor Pattern'
week: 3
---

# Week 3 - Day 3: The Extractor Pattern

## Overview
**Week 3 – Day 3**  
**Topic:** The Extractor Pattern - Unstructured to Structured Data  
**Duration:** ~60 minutes  

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define the "Extractor Pattern"
2. Use AI to parse human text (emails/messages) into a clean table or list
3. Extract dates, prices, or names from messy text
4. Build a prompt that acts as a smart "find and organize" tool

---

## Lesson Content

### The Structure Problem

Spreadsheets and apps love **Structured Data** (neat rows, columns, and categories).
The World provides **Unstructured Data** (emails, texts, receipts, casual messages).

Traditionally, you might painstakingly copy-paste details by hand, or write complex **Regular Expressions (Regex)** to bridge this gap.
This is brittle and often technical. If the format changes slightly, the old approach breaks.

**The Extractor Pattern** uses AI to read the messy text and output clean, structured data — no technical pattern-matching required.

> [!NOTE]
> ### 💡 Reading JSON in 30 Seconds
> Don't be intimidated by terms like **JSON** (JavaScript Object Notation). 
> Think of JSON as simply a **digital form with labeled fields and answers**:
> - Curly braces `{ }` wrap the whole form.
> - Quotes contain field names and text `"key": "value"`.
> - Square brackets `[ ]` represent a list of items.
> 
> For example: `{ "item": "chips", "quantity": "2 bags" }` is just a clean way of saying **Item:** chips, **Quantity:** 2 bags!

### Use Case 1: The "Message Parser"

**Input (a text from a friend):**
> "Hey, can you bring 2 bags of chips, a case of soda, and paper plates for like 20 people to the party at 7pm on Saturday?"

**The Prompt:**
> **Task:** Extract the shopping list and event details from the text.
> **Format:** JSON.
> **Schema:** `{ "items": [{ "item": string, "quantity": string }], "event_time": string, "guest_count": int }`
> **Input:** [Message]

**The Output:**
```json
{
  "items": [
    { "item": "chips", "quantity": "2 bags" },
    { "item": "soda", "quantity": "1 case" },
    { "item": "paper plates", "quantity": "enough for 20" }
  ],
  "event_time": "Saturday 7pm",
  "guest_count": 20
}
```
The AI even inferred the plates quantity from context, handling ambiguity gracefully.

### Use Case 2: The "Receipt Scraper"

**Input (a scanned receipt, transcribed as text):**
> Coffee Shop Co.
> Latte - $4.50
> Muffin - $3.25
> Total - $7.75
> ...

**The Prompt:**
> **Task:** Extract the purchased items into a table.
> **Columns:** Item, Price.
> **Input:** [Receipt text]

**The Output:**
`Latte, $4.50`
`Muffin, $3.25`

### Use Case 3: The "Notice Reader"

**Input (a notice from your utility company):**
> "Your account will see a rate change effective March 1st, from $0.12/kWh to $0.14/kWh."

**The Prompt:**
> **Task:** Extract the effective date and the old and new rates.
> **Format:** JSON.

---

## Hands-On Exercise

### Exercise: The "Inventory Builder"

**Objective:** Turn a messy text message into an organized packing list.

**Scenario:** A friend texts you before a camping trip:
*"I've got the tent (sleeps 4) and 2 sleeping bags. Sam is bringing a cooler and a first aid kit. Nobody has brought a flashlight yet."*

**Step 1: Write the Prompt**
- **System:** You are a helpful trip-planning assistant.
- **Task:** Extract the packing inventory.
- **Format:** Table: `| Item | Brought By | Status |`
- **Rule:** If an item is missing/needed, mark Status as "NEEDED".

**Step 2: Predicted Output**
```text
| Item             | Brought By | Status  |
|-------------------|------------|---------|
| Tent (sleeps 4)   | You        | Packed  |
| Sleeping bags (2) | You        | Packed  |
| Cooler            | Sam        | Packed  |
| First aid kit     | Sam        | Packed  |
| Flashlight        | -          | NEEDED  |
```

**Reflection:**
Manually re-reading that text message and building a checklist would take a few minutes of careful reading. The AI did it in seconds.

---

## Interactive Daily Quiz

### Question 1 (Analogy)
**If manually copy-pasting details is a "hand tool," what is the AI Extractor Pattern?**

A) A hammer
B) A reading comprehension engine that understands context and organizes it for you
C) A random number generator
D) A spell checker

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Old rule-based tools look for exact character patterns. AI looks for *meaning* (e.g., understanding that "for like 20 people" implies a guest count).

### Question 2 (Formats)
**Which format is best to request if you plan to use the extracted data in a spreadsheet or app?**

A) A poem
B) JSON or a table (JavaScript Object Notation / CSV-style)
C) A long paragraph
D) Spoken word

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Structured formats like JSON or tables are easy to plug directly into spreadsheets or other tools.

### Question 3 (Capabilities)
**Can the Extractor Pattern handle messy/inconsistent formatting (e.g., some dates written as "3/1", others as "March 1st")?**

A) No, it needs perfectly formatted inputs.
B) Yes, AI is robust to formatting inconsistencies.
C) Only with special software.
D) Only on certain days.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is the superpower of AI extraction—normalizing messy, inconsistent inputs into a clean, consistent structure.

### Question 4 (Constraint)
**What is the key difference between the Extractor Pattern and the Summarizer Pattern?**

A) Extraction gets specific data points (structured). Summarizing gets the general idea (unstructured prose).
B) Extraction is slower.
C) Summarizing is only for computers.
D) There is no difference.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Extraction = a clean spreadsheet row. Summary = a short paragraph capturing the gist.

### Question 5 (Reliability)
**True or False: AI can sometimes "Hallucinate" data during extraction (e.g., inventing a price that wasn't actually mentioned).**

A) True
B) False

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Always check the output. Use instructions like "If the data is missing, write 'N/A', do not invent data" to reduce this risk.

---

### Summary
Today you merged messy human text with clean, organized data. The **Extractor Pattern** lets you turn messages, receipts, and notices into tidy tables or lists. Tomorrow, we explore the **Generator Pattern**—using AI to create new content, plans, and even simple code from scratch.
