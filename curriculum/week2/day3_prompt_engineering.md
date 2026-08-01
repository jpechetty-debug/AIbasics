---
difficulty: Beginner
duration: ~60 minutes
tags:
- prompting
- python
- rag
title: 'Week 2 - Day 3: Prompt Engineering Fundamentals - The New Syntax'
week: 2
---

# Week 2 - Day 3: Prompt Engineering Fundamentals - The New Syntax

## Overview
**Week 2 – Day 3**
**Topic:** How to Speak "AI" – Basic Prompting Strategies
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define "Prompt Engineering" as "giving clear instructions in plain language"
2. Apply the "Persona, Context, Task, Format" framework
3. Explain why being specific reduces "hallucination"
4. Write a prompt to generate a usable piece of writing or plan
5. Critique and improve a vague prompt

---

## Lesson Content

### Prompting = Giving Great Instructions

Think about ordering coffee.
- "Coffee" gets you... something. Maybe not what you wanted.
- "A medium oat milk latte, extra hot, no foam" gets you exactly what you wanted.

With AI, a vague request *works*, but it often gives you a generic, unhelpful answer instead of exactly what you need.
**Prompt Engineering** is the skill of crafting inputs to get the *exact* output you want. It's a new kind of communication skill, and the "language" is plain English (or any language you speak).

### The Framework: PCTF

To get consistent results, use the **PCTF** Framework:

1.  **P - Persona:** Who should the AI be?
2.  **C - Context:** What is the situation?
3.  **T - Task:** What exactly do you want?
4.  **F - Format:** How do you want the answer?

#### Example: Generating a Plan

**Bad Prompt:**
"Help me plan a trip."

**Good Prompt (PCTF):**
- **Persona:** Act as an experienced travel planner who specializes in budget trips.
- **Context:** I'm traveling with my partner to Portugal for 7 days in October, with a total budget of $2,000 for both of us excluding flights.
- **Task:** Suggest a day-by-day itinerary covering 2 cities, with a mix of sightseeing and relaxation. Include rough daily budget estimates.
- **Format:** A table with Day, City, Activities, and Estimated Cost columns.

**Why the "Bad Prompt" Fails:**
The AI has to guess: Solo or with someone? What budget? What interests? Which countries?
**Guessing = Hallucination Risk.** By providing constraints, you force the AI into a narrow lane of success.

### Zero-Shot vs. Few-Shot Prompting

**Zero-Shot:**
Asking the AI to do something without examples.
> "Is this review positive or negative: [Review text]"

**Few-Shot (The Power Move):**
Giving the AI examples of what you want *before* asking.

> "Classify these reviews.
> Example 1: 'Loved every minute of it!' -> Positive
> Example 2: 'Waste of my time and money.' -> Negative
>
> Task: 'It was fine, nothing special.' -> [AI Fills this in]"

**Why this matters:**
If you want the AI to follow your own personal style or a specific format you use often, **give it 2-3 examples**. It will learn the pattern instantly (In-Context Learning) and apply it to new cases correctly.

### Iterative Refinement

Your first prompt will rarely be perfect. Treat it like refining a recipe.
1.  Try Prompt.
2.  Check Output: "It gave me a formal tone, I wanted something casual."
3.  Refine Prompt: "Rewrite this in a casual, friendly tone."
4.  Check Output: "It's too long now."
5.  Refine Prompt: "Shorten this to 3 sentences."

### The "Chain of Thought" Trick

For complex reasoning, tell the AI:
**"Let's think step by step."**

This magic phrase forces the model to output its reasoning *before* the final answer.
- **Without it:** AI tries to jump to the answer (Risk of math/logic errors).
- **With it:** AI writes: "First, let's figure out the total budget. Then divide by the number of days..." -> Correct Answer.

---

## Hands-On Exercise

### Exercise: The "Difficult Email Responder"

**Objective:** Write a prompt to turn a stressful, emotional situation into a calm, professional response.

**Scenario:** A frustrated customer emails: *"THIS PRODUCT IS BROKEN. I WANT A REFUND NOW. TERRIBLE SERVICE."*

**Task 1: Try a Basic Prompt** (Mental or scratchpad)
"Reply to this email."
*Result:* Likely too generic, maybe too apologetic, or misses gathering the details needed to actually help.

**Task 2: Build a PCTF Prompt**
Fill in the blanks:

- **Persona:** Experienced, calm customer support specialist. Empathetic but professional.
- **Context:** Customer is upset about a product issue and wants a refund. We need order details before we can process anything.
- **Task:** Draft a reply acknowledging the frustration. Ask for the order number and a description of the issue. Do not promise a refund yet.
- **Format:** Email format, ready to send.

**Task 3: Apply "Few-Shot" (Optional)**
Add an example of your own preferred tone.
"Style Example: 'Hi [Name], I completely understand how frustrating this is, and I want to help sort it out...'"

**Reflection:**
How much time would this save you if you had a tool that could draft calm, professional responses to stressful messages instantly?

---

## Interactive Daily Quiz

### Question 1 (Strategy)
**Which prompt is most likely to generate a genuinely useful weekly meal plan?**

A) "Give me a meal plan."
B) "Write some recipes."
C) "Act as a nutrition-conscious meal planner. Create a 7-day dinner plan for 2 adults who are vegetarian and want quick meals (under 30 minutes). Include a shopping list."
D) "Can you help me with food?"

**Correct Answer:** C

**Feedback:**
- **A) Incorrect.** Too vague.
- **B) Incorrect.** Doesn't specify structure or constraints.
- **C) ✓ Correct!** Uses PCTF: Persona (meal planner), Context (vegetarian, 2 adults), Task (7-day plan, quick meals), Format (with shopping list).
- **D) Incorrect.**

**Why this matters:** Time spent writing a detailed prompt saves 10x the time fixing an unhelpful answer later.

### Question 2 (Technique)
**You want the AI to sort messages into "Urgent", "Can Wait", or "Spam". You provide the AI with 3 examples of previous messages and their correct categories before asking it to categorize a new one. What is this technique called?**

A) Zero-Shot Prompting
B) Few-Shot Prompting
C) Fine-Tuning
D) Rebooting

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Zero-shot is asking with *no* examples.
- **B) ✓ Correct!** "Few-shot" provides a few examples to guide the model's pattern matching.
- **C) Incorrect.** Fine-tuning involves changing the model's weights (training). Prompting does not change weights.
- **D) Incorrect.**

**Why this matters:** Few-shot prompting is the single most powerful tool for getting AI to follow your specific personal style or standards.

### Question 3 (Concept)
**Why does adding "Let's think step by step" help with tricky math or logic problems?**

A) It makes the AI slower, which implies accuracy.
B) It forces the AI to generate its reasoning "chain of thought," allowing it to catch logic errors before stating the final answer.
C) It accesses a calculator module.
D) It is a cheat code.

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.**
- **B) ✓ Correct!** This triggers "Chain of Thought" reasoning. The AI talks through the problem, which significantly increases accuracy on logic/math tasks.
- **C) Incorrect.** Not necessarily.
- **D) Incorrect.**

**Why this matters:** Always use this phrase when asking the AI to work through budgeting, planning, or any multi-step reasoning.

### Question 4 (Application)
**You prompt an AI: "Write me a workout plan." It responds with an intense gym routine, but you actually wanted a beginner-friendly at-home plan. Which element of the PCTF framework did you miss?**

A) Persona
B) Context
C) Task
D) Format

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.**
- **B) ✓ Correct!** You failed to provide the **Context** that you're a beginner working out at home. The AI guessed (hallucinated) an experience level and setting that wasn't right.
- **C) Incorrect.** It did the task (write a plan).
- **D) Incorrect.**

**Why this matters:** Context is king. Never assume the AI knows your situation unless you tell it.

### Question 5 (Safety)
**What happens if you type your bank account number or medical details into a public standard AI chatbot?**

A) Nothing, it's safe.
B) That information might be used for training future models and could theoretically be exposed.
C) The AI will refuse to read it.
D) It encrypts the information automatically.

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Dangerous assumption.
- **B) ✓ Correct!** Most public AI terms of service allow them to use your chats for training. **NEVER** paste sensitive personal information (account numbers, passwords, medical details) into public chatbots.
- **C) Incorrect.** It will happily read them.
- **D) Incorrect.**

**Why this matters:** Data Privacy 101. If you wouldn't post it publicly online, don't paste it into public AI chat.

---

### Summary
Today you learned to communicate clearly with AI. You mastered the **PCTF Framework** (Persona, Context, Task, Format) and learned why **Few-Shot Prompts** (examples) are superior to vague requests. You also learned the "Step by Step" magic phrase. Tomorrow, we go deeper into **Advanced Prompting**—automating complex workflows.
