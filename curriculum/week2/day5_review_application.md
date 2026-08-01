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
- **Training:** Expensive, hard, massive data (Building the "new employee").
- **Inference:** Cheap, fast (Asking that trained employee a question).

**2. The Vehicle (LLMs - Day 2)**
- **Transformers:** The architecture that understands context/attention.
- **Tokens:** The fuel (chunks of words).
- **Context Window:** The suitcase size (how much it can hold at once).
- **Base vs. Instruct:** Autocomplete vs. Helpful Chatbot.

**3. The Steering Wheel (Prompt Engineering - Days 3 & 4)**
- **PCTF:** (Persona, Context, Task, Format) – The recipe for good instructions.
- **System Prompts:** The "handbook" that sets the rules.
- **Chaining:** Taking things step by step to reach a destination (breaking work into stages).

### Practical Scenario: "The Sunday Night Panic"

Imagine it's Sunday night. You have a big presentation tomorrow and you're stuck. You turn to AI.

**Step 1: Application of Theory (Inference)**
You're using the model (Inference). You know it has already read countless examples of presentations and writing advice (Training/Weights).

**Step 2: Understanding Limits (Context Window)**
You have 40 pages of research notes. *Recall Day 2:* "I can't paste 40 pages at once and expect it to remember all of it perfectly." You decide to paste your outline first, then feed in the details section by section.

**Step 3: Crafting the Prompt (PCTF - Day 3)**
*Bad Prompt:* "Help me with my presentation."
*Good Prompt:*
- **Persona:** Expert presentation coach.
- **Context:** I'm giving a 10-minute presentation tomorrow to my team about our project's progress. I have an outline but I'm stuck on the opening.
- **Task:** Suggest 3 strong opening lines. Explain why each works.
- **Format:** Numbered list with a one-sentence explanation for each.
- **Data:** `<outline> ... </outline>` (Delimiters - Day 4).

**Step 4: Judging the Output (Hallucination Check - Day 1)**
The AI suggests an opening statistic about your industry.
*Fact Check:* Is that statistic actually accurate? You quickly verify it before using it.
*Result:* You confirm it's roughly correct and use it.

**This is the AI-Augmented workflow.** It's not magic; it's a systematic application of the tools you learned this week.

---

## Hands-On Exercise

### Exercise: The "Prompt Doctor"

**Objective:** Fix broken prompts using Week 2 concepts.

**Scenario:** A friend sends you these failed prompts. Explain **WHY** they failed and **REWRITE** them.

**Case 1:**
- *Prompt:* "Summarize this book." (Pastes an entire 300-page novel, gets an error).
- *Diagnosis:* **Context Window Overflow.**
- *Fix:* "Chunk the text into a few parts. Summarize each part, then ask AI to summarize the summaries (Chaining)."

**Case 2:**
- *Prompt:* "Write me a workout plan." (AI writes an intense gym routine, the person actually wants a beginner home routine).
- *Diagnosis:* **Missing Context.**
- *Fix:* Add "Context: I'm a beginner working out at home with no equipment. Task: Write a 20-minute bodyweight routine..."

**Case 3:**
- *Prompt:* "Who won the World Cup in 2030?" (AI creates a fake answer).
- *Diagnosis:* **Hallucination.** (Future event).
- *Fix:* Add a rule: "If you do not know the answer, or the event is in the future, state 'I do not know'."

---

## Weekly Assignment

### Assignment: Build Your Prompt Library

**Objective:** Create 3 high-quality "Tool Prompts" you can use in your actual life.

**Deliverable:** A text file containing 3 PCTF-structured prompts.

**Requirement 1: The Translator**
- A prompt that takes a complicated or technical topic and turns it into a plain-language explanation for a friend or family member.

**Requirement 2: The Planner**
- A prompt that takes a goal description and outputs a clear, step-by-step plan with realistic timelines.

**Requirement 3: The Reviewer**
- A prompt structured to review a piece of writing (an email, an essay, a resume) using delimiters, and output specific, actionable feedback.

**Submission Checklist:**
- [ ] 3 Distinct Prompts
- [ ] Each uses Persona/Context/Task/Format
- [ ] One uses Delimiters
- [ ] One uses System Prompt style instructions

**Evaluation Rubric:**
- **Pro:** Prompts allow for variable input, handle edge cases, and define strict output formats.
- **Pass:** Prompts are clear but might lack safety rails.
- **Fail:** "Write something" (Too vague).

---

## Weekly Interactive Quiz

### Question 1 (Synthesis)
**You want to summarize a 500-page book using an AI model with a small context window. Why will pasting the whole text fail, and what is the solution?**

A) It fails because of internet speed. Solution: Get faster wifi.
B) It fails because of Context Window limits. Solution: Chunking (breaking it into parts and summarizing each).
C) It fails because AI can't read books. Solution: Read it yourself.
D) It fails because ebooks are encrypted. Solution: Buy a paperback.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** 500 pages >> a small context window. You must break the task into smaller chunks (Prompt Chaining) to fit the model's memory limits.

### Question 2 (Definition)
**Which component of the PCTF framework prevents the AI from writing an intense gym routine when you actually need a beginner home routine?**

A) Persona
B) Context
C) Task
D) Format

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Context (e.g., "I am a beginner working out at home") defines your actual situation. Format defines the visual look (list/table), but Context defines the *logic/situation*.

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
D) The Wi-Fi router

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** The System Prompt persists and sets the boundaries (e.g., "Be polite," "Never give medical advice as fact").

### Question 5 (Reality Check)
**True or False: Once you write a perfect prompt, it will work forever on every future AI model exactly the same way.**

A) True
B) False

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Models change. A prompt optimized for one model might need tweaking for a newer one. Prompt Engineering is an iterative, ongoing skill.

---

### End of Week 2
**Congratulations!** You now understand the *mechanics* of AI. You aren't just a user; you're becoming a prompt engineer.
**Next Week:** We stop talking *about* AI and start *using* it. Week 3 covers **Practical Prompt Engineering Patterns for Everyday Life**.
