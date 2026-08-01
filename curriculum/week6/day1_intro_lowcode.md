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
2. Identify key platform categories (visual builders, enterprise assistant builders, custom GPT builders).
3. Understand the "Canvas" metaphor: Nodes and Edges.

---

## Lesson Content

### Why Low-Code?

You know how to Prompt (Weeks 1-4) and how to write simple Scripts (Week 5).
**Low-Code** sits in the middle. It lets you build more complete applications (like a "Community FAQ Bot" or "Document Search Tool") by dragging and dropping blocks instead of writing extensive code by hand.

### The Landscape

1.  **Visual Flow Builders** (like Flowise or LangFlow): Open-source, visual tools for building AI-powered apps. They look like flowchart diagrams.
2.  **Enterprise Assistant Builders** (like Microsoft Copilot Studio): Popular for building internal bots that live inside company chat tools.
3.  **Custom GPTs / Simple Bot Builders**: The simplest version—custom chatbots you configure with plain, natural-language instructions.

### Core Concepts: Nodes & Edges

Behind the scenes with code, you might write:
`response = ai_client.chat(prompt)`

In Low-Code, you drag a **Prompt Node**, connect it to an **AI Model Node**, and connect that to an **Output Node**.
- **Nodes:** The steps (Input, Model, Data Source, Output).
- **Edges:** The lines connecting them (passing data from one step to the next).

---

## Hands-On Exercise

### Exercise: The "Paper Prototype"

**Objective:** Design a logical flow for a "Library Help Bot" on paper.

**Scenario:** A visitor asks "Is the library open right now?"
**Logic Flow:**
1.  **Input:** User Question.
2.  **Decision:** Is the intent "Hours Check" or "General Question"?
3.  **Action (if Hours Check):** Look up today's opening hours from a schedule.
4.  **Action (if General Question):** Send to the AI model for a normal chat response.
5.  **Output:** Final Answer.

**Reflection:**
Building AI apps is 90% logic/flow design and 10% configuration. If you can draw it, you can build it.

---

## Interactive Daily Quiz

### Question 1 (Definition)
**What is the main advantage of Low-Code AI platforms?**

A) They are always free.
B) They allow rapid building of AI-powered tools without deep software engineering skills.
C) They use no electricity.
D) They are always faster than writing regular code.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Speed and accessibility are the key advantages.

### Question 2 (Visuals)
**In a visual editor, what represents the flow of data between steps?**

A) Nodes.
B) Edges (Wires/Lines).
C) The background color.
D) The Save button.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Data flows along the edges from one node to the next.

### Question 3 (Platform)
**Which type of tool is known for being open-source and building visual AI workflows?**

A) Visual flow builders like Flowise or LangFlow.
B) A spreadsheet program.
C) Photo editing software.
D) A basic text editor.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** These are popular open-source visual builders for AI workflows.

### Question 4 (Limitations)
**Are Low-Code tools limited to just simple "Chat"?**

A) Yes.
B) No. They can perform tasks (API calls), search documents (RAG), and process files.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** They are fully functional application builders, not just chat windows.

### Question 5 (Enterprise)
**For a company already using Microsoft Teams and Office, which type of low-code tool tends to integrate best?**

A) A generic open-source flow builder.
B) An enterprise assistant builder designed for that ecosystem (like Microsoft Copilot Studio).
C) A random unrelated app.
D) A basic spreadsheet.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Enterprise-focused tools tend to have native integration with that company's existing software.

---

### Summary
Today you entered the **App Builder** phase. You learned that you don't need to be a full software developer to build an AI app. Tomorrow, we build your first custom chatbot.
