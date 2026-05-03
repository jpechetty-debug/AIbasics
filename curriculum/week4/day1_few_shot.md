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
3. Guide the AI to copy a specific JSON or CLI format using examples.

---

## Lesson Content

### Zero-Shot vs. Few-Shot

Most people use **Zero-Shot** prompting:
> "Write a poem about routing."  
> *(No examples given. You get whatever the AI feels like.)*

**One-Shot** adds a single example:
> "Write a poem about routing. Style it like a Haiku. Example: 'Packets flow so fast / Router decides where to go / Network is alive'."

**Few-Shot** provides multiple examples to define a pattern. This is the **most powerful** technique for consistent formatting.

### The "Clone My Style" Technique

**Scenario:** You want the AI to write CLI descriptions for switch interfaces, but you have a very specific naming convention.

**Zero-Shot (Fail):**
> **Prompt:** "Write descriptions for ports 1-3."
> **Output:** "Port 1 is for the printer. Port 2 is for the PC." *(Too generic).*

**Few-Shot (Success):**
> **Prompt:** "Generate interface descriptions for ports Gi1/0/3-5 following the pattern below."
> **Examples:**
> Input: Gi1/0/1 -> Description: DATA_FLOOR1_USER_PC
> Input: Gi1/0/2 -> Description: VOICE_FLOOR1_PHONE
> **Task:**
> Input: Gi1/0/3 (Printer)
> Input: Gi1/0/4 (Camera)
> Input: Gi1/0/5 (Access Point)

> **Output:**
> Description: DATA_FLOOR1_PRINTER
> Description: SEC_FLOOR1_CAMERA
> Description: MGMT_FLOOR1_AP

*The AI deduced the naming convention (Category_Location_Device) without being explicitly told the rules.*

### Why It Works
LLMs are "Pattern Completion Engines." When you give examples, you set the pattern. The AI just wants to complete it. It is easier to *show* the pattern than to *explain* it.

---

## Hands-On Exercise

### Exercise: The "JSON Formatter"

**Objective:** Force the AI to output a specific, non-standard JSON format for your legacy firewall script.

**Scenario:** Your script needs: `{"rule_id": "X", "src": "IP"}`.

**Step 1: Write the Few-Shot Prompt**
> **System:** You are a config generator.
> **Task:** Convert the natural language request into the Custom JSON format.
> **Examples:**
> User: "Allow 10.1.1.1" -> `{"rule_id": "AUTO", "src": "10.1.1.1", "action": "permit"}`
> User: "Block 8.8.8.8" -> `{"rule_id": "AUTO", "src": "8.8.8.8", "action": "deny"}`
> **User:** "Please permit traffic from 192.168.100.5"

**Step 2: Predicted Output**
`{"rule_id": "AUTO", "src": "192.168.100.5", "action": "permit"}`

**Reflection:**
If you hadn't given examples, it probably would have used keys like `source_ip` or `allow` instead of `permit`. Examples constrain the vocabulary.

---

## Interactive Daily Quiz

### Question 1 (concepts)
**What is "Zero-Shot" prompting?**

A) Asking for help with zero hope.  
B) Asking the AI to perform a task without providing any examples.  
C) Prompting with zero words.  
D) A type of espresso.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It relies entirely on the model's training data.

### Question 2 (Benefits)
**Why is Few-Shot prompting effective for obscure coding languages (like older Cisco IOS configurations)?**

A) It isn't.  
B) It "reminds" the model of the syntax by showing it valid snippets, reducing hallucinations.  
C) It makes the model faster.  
D) It uses less tokens.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Examples prime the model's context.

### Question 3 (Quantity)
**How many examples should you generally provide for "Few-Shot"?**

A) 100+  
B) 1-3 is usually sufficient.  
C) Zero.  
D) 50.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** 1 example (One-Shot) helps a lot. 3 examples (Few-Shot) is usually the sweet spot for accuracy vs context window usage.

### Question 4 (Formats)
**You want the AI to write SQL queries. Which prompt is better?**

A) "Write SQL for my users table."  
B) "Write SQL. Table Schema: Users(id, name). Example: 'Get all' -> 'SELECT * FROM Users'. Task: 'Get Bob'."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Providing the schema and an example query guarantees the output uses the correct table/column names.

### Question 5 (Debugging)
**The AI keeps formatting the date as "MM/DD/YYYY" but you need "YYYY-MM-DD". Detailed instructions didn't work. What should you do?**

A) Yell at it.  
B) Use Few-Shot prompting. Give 3 examples of inputs and the mapped outputs with YYYY-MM-DD.  
C) Give up.  
D) Write a Python script.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Showing is often better than telling.

---

### Summary
Today you learned that **Examples > Instructions**. When you need specific formatting or logic, don't just ask for it—show the AI what "Good" looks like. Tomorrow, we teach the AI how to *think*.