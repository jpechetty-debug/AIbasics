---
difficulty: Advanced
duration: ~90 minutes
tags:
- prompting
- rag
- agents
title: 'Week 7 - Day 5: Review & Mini-Project'
week: 7
---

# Week 7 - Day 5: Review & Mini-Project

## Overview
**Week 7 – Day 5**  
**Topic:** Review & Mini-Project: The "Ops Assistant"  
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Review Function Calling, API Integration, and Multi-Agent patterns.
2. Design a comprehensive "Ops Assistant" that integrates Tools and RAG.
3. Complete the Week 7 Assessment.

---

## Lesson Content

### The "Unified" Architecture

Real-world AI apps use all the components:
1.  **Chat UI:** Teams or Web.
2.  **Supervisor:** Decides what to do.
3.  **Knowledge Base (RAG):** For "How-To" questions.
4.  **Tools (API):** For "Action" questions.

**Flow:**
User -> Supervisor -> (Decision) -> RAG Agent OR Tool Agent.

---

## Hands-On Mini-Project

### Project: The "Ops Assistant" Design

**Objective:** Design the ultimate helper for your team.

**Capabilities:**
1.  **Q&A:** "How do I configure a VLAN?" (Source: Wiki/Docs RAG).
2.  **Status:** "Is Server X up?" (Source: Monitoring API).
3.  **Action:** "Restart Server X." (Source: Server Control API + Human Confirmation).

**Part 1: The Tools**
- `search_wiki(query)`
- `get_server_status(hostname)`
- `restart_server(hostname)`

**Part 2: The Logic (Supervisor Prompt)**
> "You are the Ops Assistant.
> If the user asks a knowledge question, use `search_wiki`.
> If the user asks for status, use `get_server_status`.
> If the user wants to restart, use `restart_server` BUT ask for confirmation first."

**Part 3: The Simulation**
- **User:** "The web server seems slow."
- **Bot:** "I can check the status. Which server?"
- **User:** "Web-01."
- **Bot:** (Tool: `get_server_status`) "Web-01 CPU is at 99%."
- **User:** "How do I fix high CPU?"
- **Bot:** (Tool: `search_wiki`) "Docs say: Check for runaway processes."

**Assignment:**
Map out this flow. Define the tool inputs/outputs.

---

## Weekly Interactive Quiz

### Question 1 (Flow)
**In a Unified Architecture, what usually happens first?**

A) Action.  
B) Intent Classification (Router/Supervisor).  
C) Database Drop.  
D) Sleep.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You must know *what* the user wants before you pick the tool.

### Question 2 (Tools)
**A "Tool" in AI terms equates to:**

A) A physical hammer.  
B) An API endpoint or Script that the AI can trigger.  
C) A user.  
D) Data.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Capability extension.

### Question 3 (Safety)
**Why is "Confirmation" critical in the Ops Assistant?**

A) Because LLMs can misunderstand which server "Server X" is, or hallucinate a command. You don't want accidental reboots.  
B) It isn't.  
C) To annoy users.  
D) To slow down the network.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** The "Human Check" is the ultimate safety layer.

### Question 4 (RAG vs Tools)
**User: "What is the procedure for a reboot?" -> Tool or RAG?**

A) Tool.  
B) RAG (Search Docs).  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Procedures are knowledge/text.

### Question 5 (RAG vs Tools)
**User: "Reboot the server." -> Tool or RAG?**

A) Tool (Action API).  
B) RAG.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Rebooting is an action.

---

### End of Week 7
**Congratulations!** You have reached the summit of **Low-Code Integration**.
You can build systems that **Think (LLM)**, **Remember (RAG)**, and **Act (Tools)**.
**Next Week:** The Grand Finale - **Capstone Project & Career**.