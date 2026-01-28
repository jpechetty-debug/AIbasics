# Week 6 - Day 5: Deployment & Review

## Overview
**Week 6 – Day 5**  
**Topic:** Deploying Low-Code Apps & Weekly Review  
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Understand deployment options (Web Chat, API, Teams).
2. Review the Low-Code Landscape (Bot vs RAG).
3. Complete the Week 6 Assessment.

---

## Lesson Content

### Deployment Channels

You built a bot. Now where does it live?
1.  **Web Embed:** A bubble script `<script>` you paste onto your Intranet/SharePoint.
2.  **API Endpoint:** You call it from your script (`curl POST /chat`).
3.  **Chat Platform:** Teams/Slack integration.

### Application Lifecycle

1.  **Prototype:** In the tool (Flowise/GPTs).
2.  **Test:** With trusted users. Check "Citations" and "Refusals."
3.  **Deploy:** Publish to the channel.
4.  **Monitor:** Read the chat logs! See what users are actually asking.

---

## Hands-On Mini-Project

### Project: The "Intranet Search" Architect

**Objective:** Design a RAG Application for your department.

**Step 1: Define the Source**
- "We have 200 PDFs of 'Standard Operating Procedures' (SOPs)."

**Step 2: Define the User**
- "Junior NOC Engineers on the night shift."

**Step 3: Define the Config**
- **System Prompt:** "You are a Senior NOC Lead. Answer strictly from the SOPs. Be concise."
- **Retrieval:** Top-3 chunks.

**Step 4: The Pitch**
"This tool will reduce escalation calls by 30% by answering common questions automatically using our existing SOPs."

**Assignment:** Draw this flow or configure it in a free tool if available.

---

## Weekly Interactive Quiz

### Question 1 (Deployment)
**What is the easiest way to put a bot on an internal website?**

A) Rewrite the website in React.  
B) Use an "Embed Bubble" (Javascript snippet) provided by the platform.  
C) Email the code to users.  
D) Use a floppy disk.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Most platforms give you a simple copy-paste snippet.

### Question 2 (Monitoring)
**Why must you monitor the chat logs of your deployed bot?**

A) To spy on users.  
B) To identify "Missing Knowledge" (Questions the bot couldn't answer) and Refine the System Prompt.  
C) It is fun.  
D) To delete them.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** If users keep asking about "VPN" and the bot says "I don't know," you know you need to upload the VPN PDF.

### Question 3 (Summary)
**RAG allows the bot to:**

A) Think faster.  
B) Read your private documents.  
C) Speak audio.  
D) Paint.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Knowledge Retrieval.

### Question 4 (Summary)
**Low-Code tools use:**

A) Nodes and Edges.  
B) Java and C++.  
C) Bricks and Mortar.  
D) 0s and 1s.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Visual programming.

### Question 5 (Final)
**Can a Low-Code app call a Python script (from Week 5)?**

A) No.  
B) Yes, via API or "Function Calling" nodes.  
C) Only on Tuesdays.  
D) Never.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is where Week 5 and Week 6 meet. The Bot (Brain) calls the Script (Hands).

---

### End of Week 6
**Congratulations!** You are now an **App Builder**.
You understand **Bots**, **RAG**, and **Low-Code**.
**Next Week:** Week 7 continues this journey with **Advanced Integrations** (Connecting Bots to APIs and Real Actions).
