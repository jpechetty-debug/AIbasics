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

### Step 1: Generating the "CorpNet" Wiki

We need a "Truth Source" for the bot to read.
**Prompt:**
> "Generate a Markdown document titled 'CorpNet Standard Operating Procedures'.
> Include sections on:
> 1. VLAN Standards (10=Data, 20=Voice).
> 2. IP Addressing Schema (10.Site.VLAN.Host).
> 3. Incident Severity Levels (Sev1 to Sev4).
> 4. Escalation Contacts."

**Output:** A structured `.md` file.

### Step 2: Generating the "Device Inventory"

**Prompt:**
> "Generate a CSV file with headers: Hostname, IP, Model, Location.
> Create 20 rows of realistic switch data."

**Output:** `inventory.csv`.

### Step 3: Optimization for RAG

**Rule:** "Garbage In, Garbage Out."
- **Add Metadata:** Ensure the CSV has clear headers.
- **Add Context:** In the Markdown, explicitly state "The standard for Voice VLAN is 20" rather than just "Voice: 20".
- **Chunking:** If using a visual tool, set chunk size to ~500-1000 tokens.

### Step 4: Testing Retrieval

Before connecting the bot, test the Search.
- Query: "What is the Voice VLAN?"
- Result: Should return the specific paragraph from the SOP.
- *If it returns nothing, check your Chunk overlap.*

---

## Hands-On Exercise

### Exercise: The "Search Test"

**Objective:** Verify your Knowledge Base.

**Action:**
1.  Upload `sop.md` and `inventory.csv` to your RAG tool (GPTs/Flowise).
2.  Ask: "Who is the contact for Sev1 issues?"
3.  Ask: "What model is the switch in New York?"

**Success Criteria:**
- The bot answers correctly.
- The bot **CITES** the file (`sop.md`).

**Reflection:**
If the bot answers from "General Knowledge" (e.g., "Sev1 is usually critical"), it failed. It must use *your* definition from the file.

---

## Interactive Daily Quiz

### Question 1 (Data)
**Why do we use "Synthetic Data" for the capstone?**

A) To protect real company secrets while learning.  
B) It's faster than finding real files.  
C) To test specific edge cases (like a missing IP).  
D) All of the above.  

**Correct Answer:** D

**Feedback:**
- **D) ✓ Correct!** It is safe, fast, and controlled.

### Question 2 (Formats)
**Which format is better for RAG: A scanned PDF image or a Markdown file?**

A) Scanned PDF.  
B) Markdown file.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Text is native to LLMs. OCR adds errors.

### Question 3 (Testing)
**"Ground Truth" refers to:**

A) The dirt.  
B) The actual correct answer found in the document, used to verify if the RAG system is working.  
C) The voltage.  
D) The prompt.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You compare the Bot's answer to the Ground Truth.

### Question 4 (Structure)
**What happens if your CSV lacks headers?**

A) The LLM gets confused about what "10.1.1.1" represents (IP? Gateway? DNS?).  
B) Nothing.  
C) It works better.  
D) It crashes.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Semantics matter.

### Question 5 (Refinement)
**If the bot can't find the answer, what should you do?**

A) Rewrite the document to be clearer (Prompt Engineering the Data).  
B) Yell at it.  
C) Increase Temperature.  
D) Switch to Quantum Computing.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Often, the issue is the source text is ambiguous.

---

### Summary
Today you built the Library. Your Assistant now "Knows" things about CorpNet. Tomorrow, we give it "Hands" to do things.