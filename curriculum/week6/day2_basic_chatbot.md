# Week 6 - Day 2: Building Your First Custom Bot

## Overview
**Week 6 – Day 2**  
**Topic:** Configuring a Custom "Persona" Bot  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure a "System Prompt" to strictly define a bot's behavior.
2. Set up "Knowledge Limits" (Stop the bot from talking about cooking).
3. Build a "Helpdesk Triage Bot."

---

## Lesson Content

### The "GPT" vs The "Custom Bot"

A standard ChatGPT session resets every time. A **Custom Bot** saves the instructions (System Prompt) forever.

### Step 1: The Persona (System Prompt)

The most important configuration setting is the **System Prompt**.
> "You are **NetBot**, a Tier 1 Support Assistant for Acme Corp.
> Your tone is professional and concise.
> If you don't know the answer, say 'Please open a ticket.' Do not guess."

### Step 2: Guardrails

You don't want your corporate bot generating poems or Python code if it's just for password resets.
> **Constraint:** "Refuse to answer questions unrelated to Network Support or Ticket Status."

### Step 3: Temperature

- **High Temp (0.8+):** Creative, random. (Bad for support).
- **Low Temp (0.0-0.2):** Deterministic, factual. (Good for support).

---

## Hands-On Exercise

### Exercise: The "Cisco CLI Tutor" Bot

**Objective:** Define the configuration for a bot that teaches Junior Admins.

**System Prompt:**
> "You are an expert Cisco CCNA Instructor.
> When a user asks a question, explain the concept of Networking first, then provide the CLI command.
> Always warn about the dangers of the `write erase` command."

**Test Case:**
User: "How do I reset the switch?"
Bot (Expected): "To reset a switch, you clear the startup configuration. Conceptually, this removes the saved file from NVRAM. The command is `write erase`. **WARNING: This deletes everything.**"

**Reflection:**
By hardcoding the "Instructor" persona, you save the user from having to type "Explain this like a teacher" every time.

---

## Interactive Daily Quiz

### Question 1 (Configuration)
**What setting controls the "Creativity" or "Randomness" of the bot?**

A) Volume.  
B) Temperature.  
C) Pressure.  
D) Speed.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Lower temperature = More consistent/boring. Higher = More creative/hallucinatory.

### Question 2 (Safety)
**Why add "Guardrails" (Refusal instructions) to a corporate bot?**

A) To be mean.  
B) To prevent "Jailbreaking" and keeping the bot focused on business tasks, avoiding liability.  
C) It saves money.  
D) It makes it faster.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You don't want your Support Bot giving advice on political candidates.

### Question 3 (Persona)
**"You are a helpful assistant." Is this a good System Prompt?**

A) Yes, it's perfect.  
B) No, it's too vague. It doesn't define the scope, tone, or limitations.  
C) It's too long.  
D) It's rude.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Be specific. "You are Python Bot" is better.

### Question 4 (Persistence)
**What is the benefit of a saved Custom Bot over a fresh Chat session?**

A) You don't have to copy-paste the instructions (System Prompt) every time you use it.  
B) It runs locally.  
C) It is free.  
D) It has more colors.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** It packages the Prompt Engineering into a reusable tool.

### Question 5 (Tone)
**For a "Root Cause Analysis" bot, what tone should you specify?**

A) "Excited and Hyper."  
B) "Analytical, Objective, and Concise."  
C) "Sad."  
D) "Helpful."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The tone should match the business function.

---

### Summary
Today you built a **Personality**. You learned that a "Bot" is just a wrapper around a strictly-defined System Prompt with Temperature settings. Tomorrow, we give the bot a memory—introducing **RAG**.
