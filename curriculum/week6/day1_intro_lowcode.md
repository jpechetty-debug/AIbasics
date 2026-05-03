---
difficulty: Advanced
duration: ~60 minutes
tags:
- prompting
- python
- rag
- agents
title: 'Week 6 - Day 1: Introduction to Low-Code AI'
week: 6
---

# Week 6 - Day 1: Introduction to Low-Code AI

## Overview
**Week 6 – Day 1**  
**Topic:** The Low-Code Revolution & Tool Landscape  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define "Low-Code" AI development.
2. Identify key platforms (Flowise, LangFlow, Microsoft Copilot Studio).
3. Understand the "Canvas" metaphor: Nodes and Edges.

---

## Lesson Content

### Why Low-Code?

You know how to Prompt (Weeks 1-4) and how to Script (Week 5).
**Low-Code** sits in the middle. It allows you to build complex Applications (like a "Support Bot" or "Doc Searcher") by dragging and dropping blocks instead of writing thousands of lines of Python.

### The Landscape

1.  **Flowise / LangFlow:** Open-source, visual tools for building LLM apps. They look like Visio diagrams.
2.  **Microsoft Copilot Studio:** The enterprise standard for building internal bots on Teams.
3.  **OpenAI GPTs:** The simplest version—custom chatbots you configure with natural language.

### Core Concepts: Nodes & Edges

In Code, you write:
`response = openai.chat(prompt)`

In Low-Code, you drag a **Prompt Node**, connect it to an **LLM Node**, and connect that to an **Output Node**.
- **Nodes:** The steps (Input, Model, Database, Output).
- **Edges:** The lines connecting them (passing data).

---

## Hands-On Exercise

### Exercise: The "Paper Prototype"

**Objective:** Design a logical flow for a "Network Status Bot" on paper.

**Scenario:** A user asks "Is the network down?"
**Logic Flow:**
1.  **Input:** User Question.
2.  **Decision:** Is the intent "Status Check" or "General Chat"?
3.  **Action (if Status):** API Call to Monitoring System.
4.  **Action (if Chat):** Send to LLM.
5.  **Output:** Final Answer.

**Reflection:**
Building AI apps is 90% logic/flow design and 10% configuration. If you can draw it, you can build it.

---

## Interactive Daily Quiz

### Question 1 (Definition)
**What is the main advantage of Low-Code AI platforms?**

A) They are free.  
B) They allow rapid prototyping and deployment of complex AI workflows without deep software engineering skills.  
C) They use no electricity.  
D) They are faster than Python.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Speed and Accessibility are the key drivers.

### Question 2 (Visuals)
**In a visual editor like Flowise, what represents the flow of data?**

A) Nodes.  
B) Edges (Wires/Lines).  
C) The background.  
D) The Save button.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Data flows along the edges from one node to the next.

### Question 3 (Platform)
**Which tool is known for being Open Source and creating LangChain flows visually?**

A) Flowise / LangFlow.  
B) Excel.  
C) Photoshop.  
D) Notepad.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** These are popular UIs for the LangChain library.

### Question 4 (Limitations)
**Are Low-Code tools limited to just "Chat"?**

A) Yes.  
B) No. They can perform tasks (API calls), search databases (RAG), and process files.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** They are fully functional application builders.

### Question 5 (Enterprise)
**For a Windows-centric company, which low-code tool integrates best with Teams/Office?**

A) Flowise.  
B) Microsoft CoPilot Studio (formerly Power Virtual Agents).  
C) Slack.  
D) Python.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It is built into the M365 ecosystem.

---

### Summary
Today you entered the **App Builder** phase. You learned that you don't need to be a Full Stack Developer to build an AI App. Tomorrow, we build your first custom Chatbot.