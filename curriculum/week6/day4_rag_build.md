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
**Topic:** Implementing "Chat with PDF"  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Prepare documents for RAG (Chunking).
2. Configure a "Knowledge Base" in a low-code tool.
3. specificy citations (Where did the answer come from?).

---

## Lesson Content

### Step 1: Ingestion (Garbage In, Garbage Out)

You can't just dump a messy 1000-page scan into RAG.
**Preparation:**
- **OCR:** Make sure the text is readable.
- **Chunking:** Split the text into manageable pieces (e.g., 500 characters). If chunks are too small, context is lost. If too big, they confuse the LLM.

### Step 2: The Knowledge Base Configuration

In tools like Flowise or GPTs:
1.  **Upload:** Drag and Drop your "Cisco_Command_Reference.pdf".
2.  **Process:** The tool automatically creates the Vector Index.

### Step 3: The Retrieval Settings

**Top-K:** How many chunks should we retrieve?
- **K=1:** Only one paragraph. (Might miss context).
- **K=5:** Top 5 relevant paragraphs. (Better, but uses more tokens).

### Step 4: The System Prompt with RAG

> "You are a helpful assistant. Use the **provided context** to answer the user's question.
> If the answer is not in the context, say 'I don't know'.
> **Always cite the source document name.**"

---

## Hands-On Exercise

### Exercise: The "Device Config Search"

**Objective:** Create a RAG bot that answers questions about a specific switch configuration.

**Data Source:** A text file `switch_config.txt` containing a standard `show run`.

**User Query:** "What is the IP of VLAN 20?"

**Backend Process:**
1.  RAG searches `switch_config.txt` for "VLAN 20" and "IP".
2.  Finds: `interface Vlan20` and `ip address 10.2.2.1`.
3.  LLM Response: "The IP address of VLAN 20 is 10.2.2.1 (Source: switch_config.txt)."

**Reflection:**
You turned a static text file into a queryable database without writing SQL.

---

## Interactive Daily Quiz

### Question 1 (Data Prep)
**What is "Chunking"?**

A) Throwing data away.  
B) Breaking a large document into smaller text segments for storage and retrieval.  
C) Making the robot fat.  
D) Encrypting data.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Essential for fitting data into the context window.

### Question 2 (Citations)
**Why ask the bot to "Cite sources"?**

A) To look smart.  
B) So you can verify the answer is real and not a hallucination.  
C) It is required by copyright.  
D) It slows it down.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Trust but Verify. "Show me where you found that."

### Question 3 (Fallback)
**If the RAG bot says "I don't know," is that a failure?**

A) Yes.  
B) No. It is a success of the "Anti-Hallucination" guardrails. You prefer silence over lies.  
C) Maybe.  
D) Yes, delete the bot.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** A RAG bot should strictly adhere to the source.

### Question 4 (File Types)
**Which file format is easiest for RAG systems to read?**

A) Scanned Images (PNG).  
B) Clean Text / Markdown (.txt, .md).  
C) Audio files.  
D) Encrypted Binaries.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Text is native. Images require OCR (Vision) which adds error/cost.

### Question 5 (Maintenance)
**How do you update the RAG bot when a manual changes?**

A) Re-train the model (Costs $100k).  
B) Delete the old file from the Knowledge Base and upload the new one (Costs $0).  
C) Buy a new server.  
D) Valid question.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Dynamic updates are the superpower of RAG.

---

### Summary
Today you built the "Brain" of your app. You learned to Chunk, Index, and Retrieve data. Tomorrow, we deploy this to the "Real World" and review.