---
difficulty: Advanced
duration: ~60 minutes
tags:
- prompting
- python
- rag
title: 'Week 6 - Day 2: Building Your First Custom Bot'
week: 6
---

# Week 6 - Day 2: Building Your First Custom Bot

## Overview
**Week 6 – Day 2**
**Topic:** Configuring a Custom "Persona" Bot
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure a "System Prompt" to strictly define a bot's behavior.
2. Set up "Knowledge Limits" (keep the bot on-topic).
3. Build a small "Customer Help" bot.

---

## Lesson Content

### The "Regular Chat" vs. The "Custom Bot"

A standard AI chat session resets every time you start a new one. A **Custom Bot** saves the instructions (System Prompt) permanently, so it behaves consistently every time anyone uses it.

### Step 1: The Persona (System Prompt)

The most important configuration setting is the **System Prompt**.
> "You are **ShelfBot**, a friendly assistant for a small independent bookstore.
> Your tone is warm and helpful.
> If you don't know the answer, say 'Let me check with a staff member for you.' Do not guess."

### Step 2: Guardrails

You don't want your bookstore bot writing unrelated essays or giving out medical advice if it's just meant to help with store questions.
> **Constraint:** "Only answer questions related to the store's books, hours, and events. Politely redirect anything else."

### Step 3: Temperature

- **High Temp (0.8+):** Creative, more varied and surprising. (Good for brainstorming, less ideal for support).
- **Low Temp (0.0-0.2):** Consistent, focused, predictable. (Good for factual help and support bots).

---

## Hands-On Exercise

### Exercise: The "Home Cooking Tutor" Bot

**Objective:** Define the configuration for a bot that teaches cooking basics to beginners.

**System Prompt:**
> "You are a friendly, patient home cooking instructor for total beginners.
> When a user asks a cooking question, explain the concept simply first, then give the specific steps.
> Always warn about food safety basics, like cooking chicken to a safe internal temperature."

**Test Case:**
User: "How do I know when my chicken is done?"
Bot (Expected): "Great question! The safest way to check is with a meat thermometer. Chicken should reach an internal temperature of 165°F (74°C). **Never rely on color alone—always check the temperature.**"

**Reflection:**
By hardcoding the "patient instructor" persona and the food-safety rule, you save the user from having to type "explain this simply" and "remind me about safety" every single time.

---

## Interactive Daily Quiz

### Question 1 (Configuration)
**What setting controls the "Creativity" or "Randomness" of the bot's responses?**

A) Volume.
B) Temperature.
C) Pressure.
D) Speed.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Lower temperature = more consistent and focused. Higher = more creative and varied.

### Question 2 (Safety)
**Why add "Guardrails" (topic restrictions) to a small business's customer bot?**

A) To be unhelpful.
B) To keep the bot focused on relevant business tasks and avoid giving advice it shouldn't (like medical or legal advice).
C) It saves money automatically.
D) It makes it faster.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You don't want your bookstore's bot giving out medical or legal advice, for example.

### Question 3 (Persona)
**"You are a helpful assistant." Is this a good System Prompt?**

A) Yes, it's perfect.
B) No, it's too vague. It doesn't define the scope, tone, or limitations.
C) It's too long.
D) It's rude.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Be specific. "You are a friendly bookstore assistant who only discusses our books, hours, and events" is far more useful.

### Question 4 (Persistence)
**What is the benefit of a saved Custom Bot over starting a fresh chat every time?**

A) You don't have to retype the instructions (System Prompt) every time you use it.
B) It runs without any internet connection.
C) It is always free.
D) It has more colors.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** It packages your prompt engineering work into a reusable tool.

### Question 5 (Tone)
**For a bot that helps people troubleshoot a technical issue calmly, what tone should you specify?**

A) "Excited and hyper."
B) "Calm, clear, and step-by-step."
C) "Sad."
D) "Sarcastic."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The tone should match the bot's actual purpose.

---

### Summary
Today you built a **Personality**. You learned that a "Bot" is just a wrapper around a strictly-defined System Prompt with tuned Temperature settings. Tomorrow, we give the bot a memory—introducing **RAG**.
