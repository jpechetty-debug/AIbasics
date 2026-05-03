---
difficulty: Beginner
duration: ~90 minutes
tags:
- prompting
- python
title: 'Week 2 - Day 5: Review and Practical Application'
week: 2
---

# Week 2 - Day 5: Review and Practical Application

## Overview
**Week 2 – Day 5**  
**Topic:** How AI Works – Consolidation and Assessment  
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Synthesize neural networks, LLMs, and prompting into a unified concept
2. Explain the full "Data -> Training -> Fine-Tuning -> Inference" pipeline
3. Apply the PCTF Prompting Framework to a difficult real-world scenario
4. Demonstrate understanding of "Tokens" and "Context" in tool selection
5. Complete the Week 2 Comprehensive Assessment

---

## Lesson Content

### The Big Picture: How It All Fits

Let's assemble the puzzle pieces from this week.

**1. The Engine (Neural Networks - Day 1)**
- It's a pattern-matching machine inspired by the brain.
- **Parameters:** The trillions of "knobs" tuned during training.
- **Training:** Expensive, hard, massive data (Building the "Junior Engineer").
- **Inference:** Cheap, fast (Asking the Engineer a question).

**2. The Vehicle (LLMs - Day 2)**
- **Transformers:** The architecture that understands context/attention.
- **Tokens:** The fuel (chunks of words).
- **Context Window:** The windshield size (how much it can see at once).
- **Base vs. Instruct:** Autocomplete vs. Helpful Chatbot.

**3. The Steering Wheel (Prompt Engineering - Days 3 & 4)**
- **PCTF:** (Persona, Context, Task, Format) – The protocol for good instructions.
- **System Prompts:** The "Driver's Manual" that sets the rules.
- **Chaining:** Making left and right turns to reach a destination (Step-by-step workflows).

### Practical Scenario: "The Saturday Outage"

Imagine it's Saturday. A critical router is acting up. You turn to AI.

**Step 1: Application of Theory (Inference)**
You assume the role of the user (Inference). You know the model (GPT-4) has read the router manuals (Training/Weights).

**Step 2: Understanding Limits (Context Window)**
You grab the logs. They are 10MB.
*Recall Day 2:* "I can't paste 10MB. I must chunk it." You grab the last 50 lines (the error).

**Step 3: Crafting the Prompt (PCTF - Day 3)**
*Bad Prompt:* "Fix this."
*Good Prompt:*
- **Persona:** Expert Cisco Troubleshooter.
- **Context:** Router 2960, IOS v15. Logs show OSPF neighbor flapping.
- **Task:** Analyze log snippets. Suggest 3 root causes.
- **Format:** Bullet points prioritized by probability.
- **Data:** `<logs> ... </logs>` (Delimiters - Day 4).

**Step 4: Judging the Output (Hallucination Check - Day 1)**
AI suggests: `debug ip ospf packet detail`
*Fact Check:* Is `packet detail` a valid keyword on 2960? You check the CLI help `?`.
*Result:* Correct. You proceed.

**This is the AI-Augmented Admin workflow.** It’s not magic; it’s a systematic application of the tools you learned this week.

---

## Hands-On Exercise

### Exercise: The "Prompt Doctor"

**Objective:** Fix broken prompts using Week 2 concepts.

**Scenario:** A colleague sends you these failed prompts. Explain **WHY** they failed and **REWRITE** them.

**Case 1:**
- *Prompt:* "Summarize the meeting notes." (Pastes 4 hours of transcripts, gets error).
- *Diagnosis:* **Context Window Overflow.**
- *Fix:* "Chunk the text into 3 parts. Summarize each part, then ask AI to summarize the 3 summaries (Chaining)."

**Case 2:**
- *Prompt:* "Write a script to delete old files." (AI writes PowerShell, user is on Linux).
- *Diagnosis:* **Missing Context.**
- *Fix:* Add "Context: Linux Ubuntu Server. Task: Write a Bash script..."

**Case 3:**
- *Prompt:* "Who won the Super Bowl in 2030?" (AI creates a fake answer).
- *Diagnosis:* **Hallucination.** (Future event).
- *Fix:* Add System Prompt rule: "If you do not know the answer or if the event is in the future, state 'I do not know'."

---

## Weekly Assignment

### Assignment: Build Your Prompt Library

**Objective:** Create 3 high-quality "Tool Prompts" you can use in your actual job.

**Deliverable:** A text file containing 3 PCTF-structured prompts.

**Requirement 1: The Translator**
- A prompt that takes technical jargon/logs and translates it into a "CEO-friendly" email update.

**Requirement 2: The Script Helper**
- A prompt that takes a logic description and outputs robust code (Python/Bash/Powershell) with comments and error handling mandated.

**Requirement 3: The Sentinel (Log Analyzer)**
- A prompt structured to ingest log data (using delimiters) and output a security assessment.

**Submission Checklist:**
- [ ] 3 Distinct Prompts
- [ ] Each uses Person/Context/Task/Format
- [ ] One uses Delimiters
- [ ] One uses System Prompt style instructions

**Evaluation Rubric:**
- **Pro:** Prompts allow for variable input, handle edge cases, and define strict output formats.
- **Pass:** Prompts are clear but might lack safety rails.
- **Fail:** "Write a script" (Too vague).

---

## Weekly Interactive Quiz

### Question 1 (Synthesis)
**You want to summarize a 500-page technician manual using an AI model with a 4k token limit. Why will pasting the whole text fail, and what is the solution?**

A) It fails because of Internet speed. Solution: Get fiber.  
B) It fails because of Context Window limits. Solution: Chunking (Chain of Thought / Map-Reduce).  
C) It fails because AI can't read manuals. Solution: Read it yourself.  
D) It fails because PDFs are encrypted. Solution: Print it.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** 500 pages >> 4k tokens. You must break the task into smaller chunks (Prompt Chaining) to fit the specific constraints of the model's memory buffer.

### Question 2 (Definition)
**Which component of the PCTF framework prevents the AI from writing a Windows PowerShell script when you need a Linux Bash script?**

A) Persona  
B) Context  
C) Task  
D) Format  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Context (e.g., "I am on a Linux Ubuntu server") defines the environment constraints. Format defines the visual look (table/code block), but Context defines the *logic/environment*.

### Question 3 (Process)
**When observing an AI "Training" run, you notice the Loss/Error rate is decreasing. What does this mean fundamentally?**

A) The AI is getting worse.  
B) The "Knobs" (Weights) are being tuned correctly to match the expected output.  
C) The hardware is overheating.  
D) The Context Window is shrinking.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Training is the process of minimizing error. Lower error = Better tuned weights = "Smarter" model.

### Question 4 (Safety)
**What serves as the "Guardrails" or "Employee Handbook" for an AI session?**

A) The System Prompt  
B) The User Prompt  
C) The GPU  
D) The Network Cable  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** The System Prompt persists and sets the boundaries (e.g., "Be polite," "Don't act maliciously").

### Question 5 (Reality Check)
**True or False: Once you write a perfect prompt, it will work forever on every future AI model exactly the same way.**

A) True  
B) False  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Models change. A prompt optimized for GPT-3 might need tweaking for GPT-4 or Claude. Prompt Engineering is an iterative, ongoing skill, much like updating scripts for new OS versions.

---

### End of Week 2
**Congratulation!** You now understand the *mechanics* of AI. You aren't just a user; you're a prompt engineer.
**Next Week:** We stop talking *about* AI and start *using* it. Week 3 covers **Practical Prompt Engineering Patterns for Network Admins**.