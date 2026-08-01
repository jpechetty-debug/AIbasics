---
difficulty: Advanced
duration: ~90 minutes
tags:
- prompting
- python
- rag
title: 'Week 6 - Day 5: Deployment & Review'
week: 6
---

# Week 6 - Day 5: Deployment & Review

## Overview
**Week 6 – Day 5**
**Topic:** Deploying Low-Code Apps & Weekly Review
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Understand deployment options (Web Chat, API, Chat Platforms).
2. Review the Low-Code Landscape (Bot vs. RAG).
3. Complete the Week 6 Assessment.

---

## Lesson Content

### Deployment Channels

You built a bot. Now where does it actually live?
1.  **Web Embed:** A small script snippet you paste onto your own website or community page.
2.  **API Endpoint:** You call it from your own script or app.
3.  **Chat Platform:** Integration into a team chat tool like Slack or Teams.

### Application Lifecycle

1.  **Prototype:** Build it in the low-code tool.
2.  **Test:** With a few trusted users. Check "Citations" and "Refusals" (does it decline correctly when it doesn't know?).
3.  **Deploy:** Publish to your chosen channel.
4.  **Monitor:** Read the chat logs! See what people are actually asking.

---

## Hands-On Mini-Project

### Project: The "New Hire Onboarding" Bot Architect

**Objective:** Design a RAG Application for a growing small business.

**Step 1: Define the Source**
- "We have 20 onboarding documents covering benefits, tools, and company policies."

**Step 2: Define the User**
- "New hires during their first two weeks."

**Step 3: Define the Config**
- **System Prompt:** "You are a friendly HR assistant. Answer strictly from the onboarding documents. Be warm and concise."
- **Retrieval:** Top-3 chunks.

**Step 4: The Pitch**
"This tool will reduce repetitive HR questions by answering common onboarding questions automatically using our existing documents."

**Assignment:** Draw this flow, or configure it in a free tool if one is available to you.

---

## Weekly Interactive Quiz

### Question 1 (Deployment)
**What is the easiest way to put a bot on a website?**

A) Rebuild the entire website from scratch.
B) Use an "Embed Bubble" (a small script snippet) provided by the platform.
C) Email the code to every visitor.
D) There's no easy way.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Most platforms give you a simple copy-paste snippet.

### Question 2 (Monitoring)
**Why should you monitor the chat logs of your deployed bot?**

A) To spy on people for no reason.
B) To identify "Missing Knowledge" (questions the bot couldn't answer) and refine the System Prompt or documents.
C) It's required by every platform.
D) So you can delete them.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** If people keep asking about "parking" and the bot says "I don't know," you know you need to add a parking document.

### Question 3 (Summary)
**RAG allows the bot to:**

A) Think faster overall.
B) Read and answer from your private/personal documents.
C) Generate audio.
D) Create images.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Knowledge retrieval from your own data.

### Question 4 (Summary)
**Low-Code tools typically use:**

A) Nodes and Edges (a visual, drag-and-drop structure).
B) Only Java and C++.
C) Bricks and Mortar.
D) Handwritten notes only.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Visual programming, built from connected blocks.

### Question 5 (Final)
**Can a Low-Code app call a Python script (like the ones from Week 5)?**

A) No, never.
B) Yes, via an API call or a "Function Calling" node.
C) Only in very rare cases.
D) Never, they're incompatible.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is where Week 5 and Week 6 meet. The Bot (Brain) calls the Script (Hands).

---

### End of Week 6
**Congratulations!** You are now an **App Builder**.
You understand **Bots**, **RAG**, and **Low-Code**.
**Next Week:** Week 7 continues this journey with **AI Agents & Tools** (Connecting Bots to APIs and Real Actions).
