---
difficulty: Intermediate
duration: ~90 minutes
tags:
- prompting
- python
- agents
title: 'Week 3 - Day 5: Review and Application'
week: 3
---

# Week 3 - Day 5: Review and Application

## Overview
**Week 3 – Day 5**
**Topic:** Practical Patterns Review & Building Your Toolbox
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Identify which pattern (Translate, Summarize, Extract, Generate) to use for a given problem
2. Combine patterns (e.g., Extract -> Generate) for complex workflows
3. Build a personal "Prompt Library" for daily use
4. Complete the Week 3 Comprehensive Assessment

---

## Lesson Content

### The Pattern Matrix

We covered 4 key patterns this week. Here is when to use them:

| Pattern | Goal | Input | Output | Example |
| :--- | :--- | :--- | :--- | :--- |
| **Translator** | Change Language/Tone | Jargon or another language | Plain, friendly language | "Explain my medical notes simply" |
| **Summarizer** | Compress Information | Long thread or manual | A few key bullets | "Summarize this email thread" |
| **Extractor** | Structure Data | Messy Text | Table / List | "Turn this text into a shopping list" |
| **Generator** | Create New Content | Constraints | Draft / Plan / Recipe | "Write a first draft cover letter" |

### Advanced: Pattern Chaining (The "Combo Move")

Real power comes from combining these.

**Scenario:** You receive a long, messy group chat about planning a trip. You need an actual plan.

1.  **Step 1 (Summarize):** "Summarize this chat to find what's been decided so far." -> *Output: Dates and destination confirmed, budget still undecided.*
2.  **Step 2 (Generate):** "Generate a simple day-by-day itinerary based on these decided details." -> *Output: draft itinerary.*
3.  **Step 3 (Translate):** "Write a friendly group message sharing this itinerary and asking for the budget decision." -> *Output: Message draft.*

You just automated a complex workflow using 3 AI prompts.

---

## Hands-On Exercise

### Exercise: The "AI Toolbox" Construction

**Objective:** Create a text file (`my_prompts.txt`) with your 4 "Go-To" prompts.

**Task:** Write one high-quality, reusable prompt for each category below. Use the **PCTF** (Persona, Context, Task, Format) structure.

1.  **The "Inbox Cleaner" (Summarizer):** A prompt you can paste a long email thread into to get a clean summary of decisions made.
2.  **The "Explainer" (Translator):** A prompt to turn a confusing document into plain language.
3.  **The "List Builder" (Extractor):** A prompt to pull a checklist or table out of a messy text message.
4.  **The "Draft Starter" (Generator):** A prompt to create a first draft of something you write often (an email, a note, a plan).

**Self-Check:**
- Do they have constraints? (e.g., "Do not invent information," "Use a table format").
- Are they generic enough to reuse tomorrow?

---

## Weekly Assignment

### Assignment: The "Weekend Planning" Simulation

**Scenario:**
You're organizing a weekend visit from out-of-town friends. Use AI to handle this.

**Input Data (a group text):**
`"We land Friday at 6pm, leave Sunday at noon. We love hiking and good food, not really into museums. Budget is tight, maybe $60/person for the whole weekend excluding lodging."`

**Part 1 (Generate):**
Ask AI to generate 3 possible weekend activity ideas that fit the hiking/food preference and the budget.

**Part 2 (Summarize/Explain):**
Imagine a friend then sends a long, messy message about food allergies and preferences.
Ask AI to summarize: "What are the key dietary restrictions I need to plan around?"

**Part 3 (Translator):**
Draft a friendly group message sharing your finalized weekend plan using the Translator pattern (turning your rough notes into a clear, warm message).

**Submission:**
Submit the 3 prompts you used.

---

## Weekly Interactive Quiz

### Question 1 (Pattern Identification)
**You paste a list of 30 guest names and ask the AI: "Format this as a table with columns First Name, Last Name, Meal Preference." Which pattern is this?**

A) Summarizer
B) Extractor
C) Translator
D) Generator

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You are reformatting/extracting structure from unstructured text.

### Question 2 (Usage)
**Why is "Chaining" patterns powerful?**

A) It allows you to handle complex, multi-step workflows that a single prompt cannot handle well.
B) It uses more electricity.
C) It confuses the AI.
D) It is required by law.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Breaking a task into "Read (Summarize) -> Think (Plan) -> Do (Generate)" usually yields better results.

### Question 3 (Best Practice)
**In the "Generator" pattern, why should you ask for an explanation alongside any generated plan or content?**

A) To make the file larger.
B) To help you verify and understand what the AI created, so you can catch mistakes or things that don't quite fit your situation.
C) AI cannot explain itself.
D) Explanations are unnecessary.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI output is a "black box" until you understand the reasoning behind it. Asking for explanations helps you audit and personalize the result.

### Question 4 (Toolbox)
**Which of these is a good reusable System Prompt for a "Translator" tool?**

A) "Hello."
B) "You are a friendly communication expert. Your goal is to rewrite dense or technical text into clear, warm, everyday language."
C) "Write code."
D) "Summarize this."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It sets the Persona and the Goal clearly.

### Question 5 (Reality)
**Can AI replace the need for you to understand your own situation and goals?**

A) Yes, AI knows everything.
B) No. You need to know your own context to prompt correctly, and to verify the output makes sense for your life.
C) Maybe in 100 years.
D) Yes, if you pay for premium.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI amplifies your ability to communicate and organize; it doesn't replace your own judgment and knowledge of your situation.

---

### End of Week 3
**Congratulations!** You now have a toolkit of **Practical Patterns**. You can Translate, Summarize, Extract, and Generate.
**Next Week:** We move into **Advanced Prompting**—building complex chains and simple "agents" that do work for you.
