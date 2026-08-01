---
difficulty: Advanced
duration: ~90 minutes
tags:
- prompting
- python
- rag
- agents
title: 'Week 8 - Day 4: Integration & Testing (The Demo)'
week: 8
---

# Week 8 - Day 4: Integration & Testing (The Demo)

## Overview
**Week 8 – Day 4**
**Topic:** Final Integration and "The Demo"
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Integrate the Supervisor, RAG, and Tools into one flow.
2. Run a full "End-to-End" test scenario.
3. Record a "Walkthrough" of your Assistant.

---

## Lesson Content

### The "Happy Path" Test

**Scenario:**
1.  **User:** "What's your return policy?"
    - **Step:** Supervisor -> RAG -> `faq.md`.
    - **Bot:** "Per our FAQ, returns are accepted within 30 days with a receipt."
2.  **User:** "Great. Also, can you check order #1001?"
    - **Step:** Supervisor -> Tool -> `check_order_status`.
    - **Bot:** "I checked order #1001. It has shipped and arrives in 2 days."
3.  **User:** "Actually, cancel it."
    - **Step:** Supervisor -> Permission Check.
    - **Bot:** "Are you sure you want to cancel order #1001?"
4.  **User:** "Yes."
    - **Step:** Supervisor -> Tool -> `cancel_order`.
    - **Bot:** "Done: Order #1001 has been cancelled and refunded."

### Debugging the "Sad Path"

**Scenario:**
1.  **User:** "What's the meaning of life?"
2.  **Expected:** Supervisor politely declines ("That's outside what I can help with here").
    - *If it tries to answer at length anyway, your Prompt's scope is too loose.*
3.  **User:** "Check status of order #9999" (doesn't exist).
    - **Expected:** Tool returns "Not Found." Bot says "I can't find that order number."

---

## Hands-On Exercise

### Exercise: The Demo Video

**Objective:** Prove it works.

**Task:**
Run through the "Happy Path" scenario above. Screen record it (or take screenshots).
This is your **Portfolio Piece**.

**Checklist:**
- [ ] RAG citation works?
- [ ] Tool execution works?
- [ ] Confirmation step appears?
- [ ] Tone matches your bot's intended persona?

**Reflection:**
You have built a system that behaves thoughtfully: it looks up policies, checks facts, and safeguards actions that change real data.

---

## 🏆 Project Self-Assessment Rubric
Evaluate your **Business Assistant** against these criteria to see where you stand.

| Category | Level 1: Basic | Level 2: Advanced | Level 3: Portfolio-Ready |
| :--- | :--- | :--- | :--- |
| **Logic (Supervisor)** | Often gets confused between tools. | Correctly routes to Tools vs. RAG 90% of the time. | Handles complex, multi-step tasks (e.g., Check -> Explain -> Cancel). |
| **Data (RAG)** | Simply repeats text from a document. | Synthesizes information from multiple source chunks. | Cites specific documents by name (e.g., "Per our FAQ..."). |
| **Safety** | Will cancel/change anything without asking. | Asks for confirmation before "Write" actions. | Uses the "Critic Pattern" to double-check its own plan before executing. |
| **Interface** | Text-only, no polish. | Simple, clean Chat UI. | Includes status indicators (e.g., "Searching FAQ...", "Checking order..."). |

---

## ✅ Submission Checklist
If you were showing this to a friend or a potential employer today, is it ready?
- [ ] **Code Quality**: Are there any hardcoded passwords or API keys? (Remove them!)
- [ ] **Documentation**: Is there a `README.md` explaining how to run the bot?
- [ ] **The Demo**: Does your video show the bot handling a "Sad Path" gracefully?
- [ ] **Ethics**: Does the bot have a clear disclaimer about being an AI assistant?

---

## Interactive Daily Quiz

### Question 1 (Testing)
**What is "End-to-End" (E2E) testing?**

A) Testing only the Python script in isolation.
B) Testing the entire flow from User Prompt -> Decision -> Tool/RAG -> Response.
C) Testing your internet connection.
D) Testing the user's patience.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It verifies all components work together correctly.

### Question 2 (Edge Cases)
**Why test the "Sad Path" (failures)?**

A) To make sure the bot fails gracefully (e.g., "I don't know") rather than making things up or crashing.
B) To intentionally break the bot for fun.
C) It's not really necessary.
D) To waste time.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Robustness is defined by how well you handle failure cases, not just the easy ones.

### Question 3 (Demo)
**What is the value of a recorded demo of your project?**

A) You can share it to prove you have hands-on "Applied AI" skills.
B) It uses disk space.
C) It's required by law.
D) There's no real value.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** "I built a chatbot" is common. "Here's a video of my RAG agent handling a real order lookup" is much more memorable.

### Question 4 (Latency)
**If the bot takes 10 seconds to answer, what is usually the bottleneck?**

A) The Tool/API call or the document retrieval step.
B) How fast the AI can generate text visually.
C) The user typing speed.
D) Your monitor's refresh rate.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** External calls (tools, retrieval) typically add the most latency. A "Thinking..." indicator helps user patience.

### Question 5 (Completion)
**You have finished the technical build. What is left?**

A) Thinking about your own career/goals with these new skills.
B) Nothing at all.
C) Taking a long nap.
D) Nothing more to learn, ever.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Technical skills are more valuable with a clear personal narrative around them.

---

### Summary
Today you validated your creation. Your **Business Assistant** is alive. Tomorrow, we discuss how to use this project to grow in your own career or interests.
