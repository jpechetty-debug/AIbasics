---
difficulty: Advanced
duration: ~60 minutes
tags:
- prompting
- python
- agents
title: 'Week 7 - Day 4: Multi-Agent Patterns in Low-Code'
week: 7
---

# Week 7 - Day 4: Multi-Agent Patterns in Low-Code

## Overview
**Week 7 – Day 4**  
**Topic:** Multi-Agent Systems (Supervisor/Worker Pattern)  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define **Multi-Agent Architecture**.
2. Explain the **Supervisor/Worker** pattern.
3. Build a "Routing Agent" that delgates tasks to specialist bots.

---

## Lesson Content

### Why Multiple Agents?

A single bot that tries to be a Coder, a Legal Expert, and a Network Engineer often gets confused (e.g., trying to write "Legal Code").
**Specialization** improves performance.
- Agent A: Network Diagnostic Expert.
- Agent B: IT Policy Expert.
- Agent C: Python Scripting Expert.

### The Supervisor Pattern

You need a **Supervisor** (or Router) to manage these experts.
1.  **User:** "Why is my VPN slow?"
2.  **Supervisor:** "This looks like a Network issue. I will hand off to **Network Agent**."
3.  **Network Agent:** Analyzes the issue. Returns text to Supervisor.
4.  **Supervisor:** "Here is the diagnosis..."

### How Low-Code Handles It

In tools like Flowise/LangFlow:
- You create a **Top-Level Chain** (The Supervisor).
- You utilize **Tools** that are actually other Chains.
- Tool 1: "Ask Network Expert".
- Tool 2: "Ask HR Expert".

### State Handoff

The difficult part is passing the context.
When Supervisor hands off to Network Agent, it must pass the User's question ("Why is VPN slow?").

---

## Hands-On Exercise

### Exercise: The "IT Dept" Simulator

**Objective:** Design a router for IT requests.

**Agents:**
1.  **Password Bot:** Can only reset passwords.
2.  **Hardware Bot:** Can only order laptops/mice.

**Supervisor Logic:**
- If user mentions "login", "auth", "password" -> Route to Password Bot.
- If user mentions "broken", "screen", "keyboard", "buy" -> Route to Hardware Bot.
- Else -> Respond "I can only help with Passwords or Hardware."

**Scenario:**
- User: "I need a new mouse."
- Supervisor: Keyword "mouse" detected. Routing to Hardware Bot.
- Hardware Bot: "Which model mouse do you need?"

**Reflection:**
This keeps the "Password Bot" simple and secure. It doesn't need to know about mice prices.

---

## Interactive Daily Quiz

### Question 1 (Architecture)
**What is the "Supervisor" role in a Multi-Agent system?**

A) To do all the work.  
B) To analyze the user's intent and route the task to the correct Sub-Agent/Worker.  
C) To delete data.  
D) To make coffee.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It is the Traffic Cop or Manager.

### Question 2 (Benefit)
**Why split a bot into multiple agents?**

A) It costs more.  
B) Specialization reduces hallucinations and complexity. Each agent has a focused System Prompt and limited Tools.  
C) To use more RAM.  
D) Confusion.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Separation of Concerns.

### Question 3 (Structure)
**Can a Sub-Agent have its own Tools?**

A) Yes. The Network Agent might have the "Ping" tool, while the HR Agent has the "Vacation" tool.  
B) No. Only the Supervisor can have tools.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** This is the power of the architecture. Each agent encapsulates its capabilities.

### Question 4 (Term)
**What do we call the process of one agent calling another?**

A) Handoff / Delegation.  
B) Calling.  
C) Sleeping.  
D) Fighting.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** "I am handing this off to X."

### Question 5 (Complexity)
**Is Multi-Agent always better?**

A) Yes.  
B) No. It adds latency and complexity. For simple tasks, a single Agent is better.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Don't over-engineer. Use it when prompts get too long/conflicting.

---

### Summary
Today you escalated to **Management**. You learned how to orchestrate a team of specialized AI Agents using the Supervisor pattern. Tomorrow, we combine everything into a final project.