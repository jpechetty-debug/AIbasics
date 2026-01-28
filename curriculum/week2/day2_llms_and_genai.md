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
4. Explain "Context Window" using a RAM/buffer analogy
5. Distinguish between "Base Models" and "Fine-Tuned Models"

---

## Lesson Content

### From Prediction to Generation

Last week, we talked about AI that **predicts**: "Is this email spam? Yes/No."
Today, we talk about **Generative AI**: "Write a phishing email to test our employees."

**Generative AI creates new data** (text, images, code) that didn't exist before. The most famous type right now is the **Large Language Model (LLM)**, like GPT-4, Claude, or LLaMA.

### The Engine: The Transformer

In 2017, Google researchers published a paper called *"Attention Is All You Need."* This introduced the **Transformer** architecture, which changed everything.

**The "Attention" Mechanism (The Network Switch Analogy):**
Imagine reading a complex sentence:
*"The **server** kept crashing because **it** was overheated."*

To understand what "**it**" refers to, your brain draws a connection back to "**server**."
- Old AI read linearly (left to right) and often forgot early words.
- **Transformer AI** looks at the whole sentence at once (like a mesh network). It assigns "attention scores" between every word. The word "it" has a very strong link/weight to "server."

This allows the AI to understand deep context and relationships, even across pages of text.

### The Fuel: Tokens

Computers don't read words; they read numbers. LLMs break text into chunks called **Tokens**.
- A token is roughly **0.75 of a word**.
- Short word: "apple" = 1 token.
- Complex word: "ingestion" might be 2 tokens ("ingest" + "ion").

**Why this matters for Admins:**
1.  **Cost:** most API pricing is "per 1,000 tokens."
2.  **Performance:** Processing speed is measured in "Tokens Per Second" (TPS).
3.  **Limits:** Models have maximum text limits defined in tokens.

### Critical Constraint: The "Context Window"

The **Context Window** is the maximum amount of text the AI can consider at one time (prompt + answer).

**The RAM Analogy:**
Think of the Context Window like **RAM** on a router.
- If you paste a 50-page log file into a model with a small context window, it's like overflowing a router's buffer. The beginning of the log falls out of memory to make room for the end.
- The AI literally "forgets" the start of your message.

**Evolution:**
- Older models: ~4k tokens (~3,000 words).
- Newer models (Claude 3, GPT-4 Turbo): 128k - 1M tokens (Entire books of logs).

### Training Stages: Pre-Training vs. Fine-Tuning

How do we get a helpful assistant from a raw neural network?

**Stage 1: Pre-Training (The Library)**
- The model reads the entire internet (Wikipedia, GitHub, Reddit, Books).
- **Goal:** Learn how language works, facts about the world, and coding syntax.
- **Result:** A "Base Model." It acts like a super-smart autocomplete. If you type "The capital of France is", it completes "Paris." It doesn't know how to chat; it just continues text.

**Stage 2: Fine-Tuning (The Job Training)**
- Humans give the model examples of good instructions: "Here is a question, here is a helpful answer."
- **Goal:** Teach it to follow instructions, be polite, and refuse dangerous requests.
- **Result:** An "Instruct" or "Chat" model (like ChatGPT).

**Network Admin Takeaway:**
You usually want a **Fine-Tuned / Instruct** model for your work. Base models are wild and hard to control.

---

## Hands-On Exercise

### Exercise: "Token" Estimation & Context Buffers

**Objective:** Develop an intuition for tokens and context windows.

**Part 1: The Tokenizer**
Go to a text tokenizer tool (mentally, or use a mental rule of thumb: Word count × 1.3).

**Scenario:** You have a `syslog` file that is 100MB.
- Average log line: 20 words.
- Total lines: 500,000.
- Total words: 10,000,000 words.
- **Total Tokens:** ~13,000,000 tokens.

**Question:** Can you paste this file into ChatGPT (Context limit ~32k or 128k)?
**Answer:** No. It's wildly too big.

**Part 2: The "Sliding Window" Strategy**
Since we can't fit the whole log, we need a strategy network admins use: **Chunking.**

Imagine you have a context window of just **10 words**.
Log: `Error at 10:00. Service stopped. Retry 1. Retry 2. Failed.` (10 words total).

If you add one new word ("Alert"), the first word must drop out.
**New State:** `at 10:00. Service stopped. Retry 1. Retry 2. Failed. Alert`
**Lost Info:** We lost the "Error" timestamp!

**Reflection:**
When working with AI and large log files, you must split data into chunks that fit the window. You cannot just "feed it the database."

---

## Interactive Daily Quiz

### Question 1 (Analogy)
**If an LLM is a router, what is the "Context Window"?**

A) The bandwidth speed (Gbps)  
B) The routing table size  
C) The Packet Buffer / RAM memory  
D) The power supply wattage  

**Correct Answer:** C

**Feedback:**
- **A) Incorrect.** Speed is Tokens Per Second.
- **B) Incorrect.** Knowledge is closer to the routing table/weights.
- **C) ✓ Correct!** The context window is the short-term working memory. Once it fills up, old info (packets) gets dropped or overwritten.
- **D) Incorrect.** Irrelevant.

**Why this matters:** You need to know how much data (logs, config files) you can paste into the AI before it starts forgetting the beginning.

---

### Question 2 (Process)
**Predictive AI classifies data (e.g., "Spam or Not"). What does Generative AI do?**

A) Creates new data (text, images, code)  
B) Deletes old data  
C) Sorts spreadsheets  
D) Only plays chess  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** It generates *new* patterns based on training data.
- **B) Incorrect.**
- **C) Incorrect.** That's traditional automation.
- **D) Incorrect.**

**Why this matters:** Generative AI is a creative tool. You can use it to *write* scripts, *draft* emails, or *create* documentation, not just categorize things.

---

### Question 3 (Fact Check)
**You want to deploy an open-source model to help users reset passwords. Which type should you choose?**

A) A "Base" model  
B) An "Instruct" or "Chat" fine-tuned model  
C) An image diffusion model  
D) A raw untreated neural net  

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Base models just autocomplete text. If a user says "Help me," it might reply "Help you what?" or just continue a sentence.
- **B) ✓ Correct!** Instruct/Chat models are fine-tuned to understand questions and provide helpful answers.
- **C) Incorrect.** That makes images.
- **D) Incorrect.** Useless without training.

**Why this matters:** Selecting the right model version (often labeled `-instruct` or `-chat` on HuggingFace) saves huge headaches.

---

### Question 4 (Math)
**An API charges $0.01 per 1,000 tokens. You send a log file with 750 words. Approximately how many tokens is that, and what is the cost? (Rule of thumb: 1 word ≈ 1.3 tokens)**

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

**Why this matters:** Estimating API costs prevents "cloud bill shock" when building AI automations.

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

**Why this matters:** "Attention" is the "A" in many Acronyms. It's why modern AI can remember that "IP address" mentioned 3 paragraphs ago refers to the "Firewall" mentioned now.

---

### Summary
Today we opened the hood of the Chatbot. You learned about **Transformers** (the engine), **Tokens** (the fuel), and the **Context Window** (the memory buffer). You also learned that **Fine-Tuning** is what turns a raw pattern-matcher into a helpful assistant. Tomorrow, we explore "Prompt Engineering"—the art of programming this engine using plain English.
