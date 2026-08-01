---
difficulty: Beginner
duration: ~75 minutes
tags:
- prompting
- rag
- automation
title: 'Week 2 - Day 2: Large Language Models (LLMs) & Generative AI'
week: 2
---

# Week 2 - Day 2: Large Language Models (LLMs) & Generative AI

## Overview
**Week 2 – Day 2**
**Topic:** How ChatGPT and LLMs Actually Work
**Duration:** ~75 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define "Generative AI" and how it differs from predictive AI
2. Explain what a "Transformer" architecture is (simplified)
3. Understand "Tokens" – the atoms of LLM language
4. Explain "Context Window" using a suitcase-packing analogy
5. Distinguish between "Base Models" and "Fine-Tuned Models"

---

## Lesson Content

### From Prediction to Generation

Yesterday, we talked about AI that **predicts**: "Is this email spam? Yes/No."
Today, we talk about **Generative AI**: "Write me a birthday message for my friend."

**Generative AI creates new content** (text, images, code) that didn't exist before. The most famous type right now is the **Large Language Model (LLM)**, like GPT-4, Claude, or LLaMA.

### The Engine: The Transformer

In 2017, Google researchers published a paper called *"Attention Is All You Need."* This introduced the **Transformer** architecture, which changed everything.

**The "Attention" Mechanism (The Group Conversation Analogy):**
Imagine reading a complex sentence:
*"The **cake** was delicious even though **it** was slightly burnt."*

To understand what "**it**" refers to, your brain draws a connection back to "**cake**."
- Older AI read linearly (left to right) and often forgot earlier words.
- **Transformer AI** looks at the whole sentence at once, like someone following an entire group conversation instead of just the last thing said. It assigns "attention scores" between every word. The word "it" has a very strong link/weight to "cake."

This allows the AI to understand deep context and relationships, even across pages of text.

### The Fuel: Tokens

Computers don't read words; they read numbers. LLMs break text into chunks called **Tokens**.
- A token is roughly **0.75 of a word**.
- Short word: "apple" = 1 token.
- Complex word: "unbelievable" might be 2 tokens ("unbelieve" + "able").

**Why this matters:**
1.  **Cost:** most API pricing is "per 1,000 tokens."
2.  **Speed:** Processing speed is measured in "Tokens Per Second" (TPS).
3.  **Limits:** Models have maximum text limits defined in tokens.

### Critical Constraint: The "Context Window"

The **Context Window** is the maximum amount of text the AI can consider at one time (your question plus its answer).

**The Suitcase Analogy:**
Think of the Context Window like a **suitcase with a fixed size**.
- If you try to pack a 50-page document into a small suitcase, something has to fall out to make room.
- The AI literally "forgets" the earliest parts of a very long conversation once the suitcase is full.

**Evolution:**
- Older models: ~4k tokens (~3,000 words).
- Newer models (Claude, GPT-4 Turbo): 128k - 1M tokens (Entire books at once).

### Training Stages: Pre-Training vs. Fine-Tuning

How do we get a helpful assistant from a raw neural network?

**Stage 1: Pre-Training (The Library)**
- The model reads a huge portion of the internet (Wikipedia, books, articles, code).
- **Goal:** Learn how language works, facts about the world, and how ideas connect.
- **Result:** A "Base Model." It acts like a super-smart autocomplete. If you type "The capital of France is", it completes "Paris." It doesn't know how to chat; it just continues text.

**Stage 2: Fine-Tuning (The Job Training)**
- Humans give the model examples of good instructions: "Here is a question, here is a helpful answer."
- **Goal:** Teach it to follow instructions, be polite, and refuse harmful requests.
- **Result:** An "Instruct" or "Chat" model (like ChatGPT).

**Takeaway:**
You almost always want a **Fine-Tuned / Instruct** model for everyday use. Base models are unpredictable and hard to control.

---

## Hands-On Exercise

### Exercise: "Token" Estimation & Context Buffers

**Objective:** Develop an intuition for tokens and context windows.

**Part 1: The Tokenizer**
Use a mental rule of thumb: Word count × 1.3.

**Scenario:** You have a family group chat history that's grown to 10,000,000 words over the years.
- **Total Tokens:** ~13,000,000 tokens.

**Question:** Can you paste this entire chat history into ChatGPT (Context limit ~32k or 128k)?
**Answer:** No. It's wildly too big.

**Part 2: The "Sliding Window" Strategy**
Since we can't fit the whole thing, we need a strategy: **Chunking.**

Imagine you have a context window of just **10 words**.
Text: `Mom said dinner is at 7. Bring dessert. Don't forget the wine.` (10 words total).

If you add one new sentence ("Also bring napkins"), the first few words must drop out.
**New State:** `said dinner is at 7. Bring dessert. Don't forget the wine. Also bring napkins`
**Lost Info:** We lost "Mom said" — we might forget who gave the instruction!

**Reflection:**
When working with AI and very long documents or chat histories, you must split data into chunks that fit the window. You cannot just "feed it everything at once."

---

## Interactive Daily Quiz

### Question 1 (Analogy)
**If an LLM is like a person's short-term memory, what is the "Context Window"?**

A) How fast they can talk
B) How much they remember overall in their life
C) How much they can hold in mind at once before forgetting earlier details
D) How loud they can speak

**Correct Answer:** C

**Feedback:**
- **A) Incorrect.** Speed is Tokens Per Second.
- **B) Incorrect.** Long-term knowledge is closer to the model's trained weights.
- **C) ✓ Correct!** The context window is the short-term working memory. Once it fills up, old info gets dropped or overwritten.
- **D) Incorrect.** Irrelevant.

**Why this matters:** You need to know how much text (a document, a long conversation) you can paste into the AI before it starts forgetting the beginning.

---

### Question 2 (Process)
**Predictive AI classifies data (e.g., "Spam or Not"). What does Generative AI do?**

A) Creates new content (text, images, code)
B) Deletes old data
C) Sorts spreadsheets
D) Only plays chess

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** It generates *new* content based on patterns learned from training data.
- **B) Incorrect.**
- **C) Incorrect.** That's traditional automation.
- **D) Incorrect.**

**Why this matters:** Generative AI is a creative tool. You can use it to *write* messages, *draft* documents, or *create* new ideas, not just categorize things.

---

### Question 3 (Fact Check)
**You want to deploy an open-source model to help answer customer questions on your website. Which type should you choose?**

A) A "Base" model
B) An "Instruct" or "Chat" fine-tuned model
C) An image diffusion model
D) A raw untrained neural net

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Base models just autocomplete text. If a customer says "Help me," it might reply "Help you what?" or just continue a random sentence.
- **B) ✓ Correct!** Instruct/Chat models are fine-tuned to understand questions and provide helpful answers.
- **C) Incorrect.** That makes images.
- **D) Incorrect.** Useless without training.

**Why this matters:** Selecting the right model version (often labeled `-instruct` or `-chat`) saves huge headaches.

---

### Question 4 (Math)
**An API charges $0.01 per 1,000 tokens. You send a document with 750 words. Approximately how many tokens is that, and what is the cost? (Rule of thumb: 1 word ≈ 1.3 tokens)**

A) 750 tokens, Cost $0.0075
B) ~1,000 tokens, Cost $0.01
C) 100,000 tokens, Cost $1.00
D) 500 tokens, Cost $0.005

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Tokens > words.
- **B) ✓ Correct!** 750 words * 1.3 ≈ 975 tokens, which is close to 1,000. Cost is roughly 1 cent.
- **C) Incorrect.** Way too high.
- **D) Incorrect.** Tokens are not fewer than words.

**Why this matters:** Estimating costs prevents surprise bills when using AI regularly.

---

### Question 5 (Mechanism)
**What is the core mechanism in "Transformer" models that allows them to understand context better than older AI?**

A) Backups
B) Attention
C) Encryption
D) Compression

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.**
- **B) ✓ Correct!** The "Self-Attention" mechanism allows the model to weigh the relationships between all words in a sentence simultaneously.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** "Attention" is why modern AI can remember that "the cake" mentioned 3 sentences ago is what "it" refers to now.

---

### Summary
Today we opened the hood of the Chatbot. You learned about **Transformers** (the engine), **Tokens** (the fuel), and the **Context Window** (the memory buffer). You also learned that **Fine-Tuning** is what turns a raw pattern-matcher into a helpful assistant. Tomorrow, we explore "Prompt Engineering"—the art of programming this engine using plain English.
