---
difficulty: Intermediate
duration: ~90 minutes
tags:
- prompting
- python
- agents
title: 'Week 4 - Day 5: Review & Mini-Project'
week: 4
---

# Week 4 - Day 5: Review & Mini-Project

## Overview
**Week 4 – Day 5**  
**Topic:** Review & Mini-Project: Building a Troubleshooting Agent  
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Review Zero-Shot, CoT, Critic, and Chaining patterns.
2. Combine all patterns into a cohesive "Manual Agent."
3. Complete the Week 4 Assessment.

---

## Lesson Content

### The Advanced Prompting Stack

You now possess the advanced tools:
1.  **Few-Shot:** Show, don't just tell.
2.  **Chain of Thought:** "Let's think step by step."
3.  **The Critic:** "Review your work."
4.  **Chaining:** "Step 1 -> Step 2 -> Step 3."

### How to "Think" Like an Agent

An AI Agent isn't magic. It's just a loop:
**Perceive (Read Data) -> Reason (CoT) -> Act (Generate) -> Criticize (Review).**

---

## Hands-On Mini-Project

### Project: The "Network Outage Agent"

**Objective:** Simulate an AI Agent that diagnoses a network outage report.

**Step 1: The Trigger (User Input)**
"The Wi-Fi in Building 3 is down."

**Step 2: The Analyst (Chain Link 1)**
> **Context:** You are a L1 Helpdesk AI.
> **Task:** Analyze the user report. List 3 clarifying questions to narrow the scope.
> **Output:**
> 1. Is it all users or just one?
> 2. Do wired connections work?
> 3. Are the lights on the Access Points on?

**Step 3: The Data Merger (Chain Link 2)**
*(Assume User answers: All users, Wired works, AP lights are off/amber)*
> **Context:** You are a Network Engineer.
> **Task:** Given the symptoms (Wired OK, APs off), determine the likely root cause. Use Chain of Thought.
> **Output:**
> 1. Wired works -> Internet/Gateway is fine.
> 2. APs are off -> Power issue.
> 3. APs use PoE.
> 4. **Root Cause:** PoE Switch in Building 3 likely lost power or PoE budget.

**Step 4: The Communicator (Chain Link 3)**
> **Context:** You are a Customer Service Rep.
> **Task:** Write a status update email to the users explaining the issue and the fix (Check the breaker).
> **Input:** "PoE Switch Failure."
> **Output:** "Team, we identified a power issue with the switches..."

**Assignment Submission:**
Perform this chain on a problem of your choice (e.g., Server Crash, Printer Jam) and capture the 3-step prompt chain.

---

## Weekly Interactive Quiz

### Question 1 (Patterns)
**Which pattern involves giving the AI 3 examples of "Input -> Output" before asking your question?**

A) Zero-Shot  
B) One-Shot  
C) Few-Shot  
D) Chain of Thought  

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** "Few" implies a small number (typically 2-5) of examples.

### Question 2 (Reasoning)
**"Let's think step by step" is the trigger phrase for:**

A) The Critic  
B) Chain of Thought (CoT)  
C) The Simulator  
D) The Terminator  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It triggers intermediate reasoning steps.

### Question 3 (Quality)
**You utilize "Role Prompting" to ask the AI to "Act as a Hacker" and try to break your code. Which pattern is this?**

A) The Critic Pattern  
B) The Summarizer  
C) The Fan  
D) The Translator  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** You are soliciting a critique/audit.

### Question 4 (Architecture)
**Why is Chaining safer than a single giant prompt?**

A) It isn't.  
B) It allows for human-in-the-loop verification between steps, preventing errors from cascading.  
C) It creates more AI.  
D) It is faster.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** If Step 1 is wrong, you catch it before Step 2 happens.

### Question 5 (Future)
**What is the next evolution after "Chaining"?**

A) Telepathy.  
B) Autonomous Agents (where the AI chooses which tool/chain to run).  
C) Less AI.  
D) Analog computers.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Agents are essentially dynamic chains where the AI picks the path.

---

### End of Week 4
**Congratulations!** You have completed the **Advanced Prompting** module.
You can now guide the AI to learn from examples, think logically, critique itself, and execute complex workflows.
**Next Week:** We will explore **AI Tools**—using AI to help you write actual Python and Ansible code.