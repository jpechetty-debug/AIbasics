---
difficulty: Advanced
duration: ~60 minutes
tags:
- prompting
- rag
title: 'Week 6 - Day 4: Building a RAG Knowledge Base'
week: 6
---

# Week 6 - Day 4: Building a RAG Knowledge Base

## Overview
**Week 6 – Day 4**
**Topic:** Implementing "Chat with Your Documents"
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Prepare documents for RAG (Chunking).
2. Configure a "Knowledge Base" in a low-code tool.
3. Specify citations (Where did the answer come from?).

---

## Lesson Content

### Step 1: Ingestion (Garbage In, Garbage Out)

You can't just dump a messy 500-page scanned document into RAG and expect great results.
**Preparation:**
- **OCR:** Make sure the text is actually readable text, not just a picture of text.
- **Chunking:** Split the text into manageable pieces (e.g., 500 characters). If chunks are too small, context is lost. If too big, they confuse the AI.

### Step 2: The Knowledge Base Configuration

In tools like Flowise or custom GPT builders:
1.  **Upload:** Drag and drop your "Employee_Handbook.pdf".
2.  **Process:** The tool automatically creates the searchable index behind the scenes.

### Step 3: The Retrieval Settings

**Top-K:** How many chunks should we retrieve for each question?
- **K=1:** Only one paragraph. (Might miss important context).
- **K=5:** Top 5 relevant paragraphs. (Better coverage, but uses more of the context window).

### Step 4: The System Prompt with RAG

> "You are a helpful assistant. Use the **provided context** to answer the user's question.
> If the answer is not in the context, say 'I don't know based on the documents I have.'
> **Always cite the source document name.**"

---

## Hands-On Exercise

### Exercise: The "Handbook Search" Bot

**Objective:** Create a RAG bot that answers questions about a company handbook.

**Data Source:** A text file `employee_handbook.txt` containing standard workplace policies.

**User Query:** "How many sick days do I get?"

**Backend Process:**
1.  RAG searches `employee_handbook.txt` for "sick days."
2.  Finds: `Employees receive 8 paid sick days per calendar year.`
3.  AI Response: "You receive 8 paid sick days per calendar year (Source: employee_handbook.txt)."

**Reflection:**
You turned a static text file into a queryable, chat-friendly knowledge base without writing any complex database code.

---

## Interactive Daily Quiz

### Question 1 (Data Prep)
**What is "Chunking"?**

A) Throwing data away.
B) Breaking a large document into smaller text segments for storage and retrieval.
C) Compressing a file to save space.
D) Encrypting data.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Essential for fitting relevant data into the AI's context window.

### Question 2 (Citations)
**Why ask the bot to "Cite sources"?**

A) To look more sophisticated.
B) So you can verify the answer is real and not a hallucination.
C) It is legally required in every case.
D) It slows the bot down on purpose.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Trust but verify. "Show me where you found that" is a healthy habit.

### Question 3 (Fallback)
**If the RAG bot says "I don't know," is that a failure?**

A) Yes, always.
B) No. It is a success of the "Anti-Hallucination" guardrails. You prefer honesty over confident guessing.
C) Maybe, depends on the mood.
D) Yes, you should delete the bot.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** A good RAG bot should strictly stick to what its source documents actually say.

### Question 4 (File Types)
**Which file format is easiest for RAG systems to read?**

A) Scanned images with no text layer.
B) Clean text or Markdown (.txt, .md).
C) Audio recordings.
D) Encrypted files.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Text is native. Images require OCR (Vision processing), which adds complexity and potential error.

### Question 5 (Maintenance)
**How do you update the RAG bot's knowledge when a document changes?**

A) Retrain the entire underlying AI model (expensive and slow).
B) Delete the old file from the Knowledge Base and upload the new version (fast and simple).
C) Buy a new computer.
D) You can't update it.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Easy, near-instant updates are the superpower of RAG.

---

### Summary
Today you built the "Brain" of your app. You learned to chunk, index, and retrieve data. Tomorrow, we deploy this to the "Real World" and review.
