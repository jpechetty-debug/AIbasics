---
difficulty: Advanced
duration: ~90 minutes
tags:
- prompting
- rag
title: 'Week 8 - Day 2: Building the Knowledge Base'
week: 8
---

# Week 8 - Day 2: Building the Knowledge Base

## Overview
**Week 8 – Day 2**
**Topic:** Generating & Ingesting the RAG Dataset
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Use AI (Generator Pattern) to create synthetic documentation.
2. Structure the data for optimal retrieval (Headings, Keywords).
3. Ingest the data into your Knowledge Base.

---

## Lesson Content

### Step 1: Generating the "Business FAQ" Document

We need a "Truth Source" for the bot to read.
**Prompt:**
> "Generate a Markdown document titled '[Your Business Name] FAQ & Policies'.
> Include sections on:
> 1. Return/Refund Policy.
> 2. Shipping or Appointment Timeframes.
> 3. Contact/Escalation Information.
> 4. Common Troubleshooting Questions."

**Output:** A structured `.md` file.

### Step 2: Generating the "Product/Service Catalog"

**Prompt:**
> "Generate a CSV file with headers: Item Name, Price, Category, In Stock.
> Create 20 rows of realistic sample data for a [type of business]."

**Output:** `catalog.csv`.

### Step 3: Optimization for RAG

**Rule:** "Garbage In, Garbage Out."
- **Add Metadata:** Ensure the CSV has clear headers.
- **Add Context:** In the Markdown, explicitly state "Refunds are accepted within 30 days of purchase" rather than just "Refunds: 30 days".
- **Chunking:** If using a visual tool, set chunk size to roughly 500-1000 tokens.

### Step 4: Testing Retrieval

Before connecting the bot, test the Search.
- Query: "What's your refund policy?"
- Result: Should return the specific paragraph from the FAQ document.
- *If it returns nothing, check your chunk settings.*

---

## Hands-On Exercise

### Exercise: The "Search Test"

**Objective:** Verify your Knowledge Base.

**Action:**
1.  Upload `faq.md` and `catalog.csv` to your RAG tool.
2.  Ask: "What's your return policy?"
3.  Ask: "How much does [item] cost?"

**Success Criteria:**
- The bot answers correctly.
- The bot **CITES** the file (`faq.md`).

**Reflection:**
If the bot answers from "General Knowledge" (e.g., "Most stores allow 30-day returns") instead of *your* actual policy, it failed. It must use *your* definition from the file.

---

## Interactive Daily Quiz

### Question 1 (Data)
**Why do we use "Synthetic Data" for the capstone?**

A) To protect real personal or business data while learning.
B) It's faster than gathering real files.
C) To test specific edge cases (like a missing item).
D) All of the above.

**Correct Answer:** D

**Feedback:**
- **D) ✓ Correct!** It is safe, fast, and lets you control every scenario.

### Question 2 (Formats)
**Which format is better for RAG: a scanned image of a document, or a Markdown text file?**

A) Scanned image.
B) Markdown file.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Text is native to AI models. OCR (image-to-text) adds errors.

### Question 3 (Testing)
**"Ground Truth" refers to:**

A) Literal dirt.
B) The actual correct answer found in the document, used to verify if the RAG system is working.
C) The device's power voltage.
D) The prompt itself.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You compare the bot's answer to the Ground Truth to check accuracy.

### Question 4 (Structure)
**What happens if your CSV lacks clear headers?**

A) The AI gets confused about what a number like "29.99" represents (Price? Quantity? ID?).
B) Nothing changes.
C) It works better without them.
D) The file becomes corrupted.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Semantics matter — clear headers give meaning to raw numbers.

### Question 5 (Refinement)
**If the bot can't find the answer, what should you do first?**

A) Rewrite the document to be clearer (essentially "Prompt Engineering the Data").
B) Give up on the project.
C) Increase the Temperature setting.
D) Try a completely different AI provider immediately.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Often, the real issue is that the source text is ambiguous or poorly organized.

---

### Summary
Today you built the Library. Your Assistant now "Knows" things about your business idea. Tomorrow, we give it "Hands" to do things.
