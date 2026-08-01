---
difficulty: Beginner
duration: 30-60 min
tags:
- prompting
- assessment
title: Week 2 - Weekly Interactive Assessment
week: 2
---

# Week 2 - Weekly Interactive Assessment

## How AI Works Comprehensive Quiz

**Instructions:**
- 15 questions covering Neural Networks, LLMs, and Prompt Engineering
- Aim for 70% or higher to advance

**Scoring Guide:**
- 13-15: Expert Prompt Engineer 🧙
- 10-12: Junior Prompt Engineer 👨‍💻
- <10: Needs Retraining 🤖

---

### Question 1 (Core Concept)
**What component of a Neural Network is modified during the "Training" phase to make the model learn?**

A) The input data
B) The architecture diagrams
C) The Weights (Parameters)
D) The output screen

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** Learning is literally the mathematical process of adjusting billions of internal weights (knobs) until the output error is minimized.

---

### Question 2 (Terminology)
**In the context of LLMs, what is a "Token"?**

A) A crypto coin
B) A fundamental unit of text (part of a word) that the AI processes
C) An API key
D) A hardware slot

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** LLMs process numbers representing tokens. One word ≈ 1.3 tokens. Pricing and limits use tokens.

---

### Question 3 (Prompt Engineering)
**What does the "System Prompt" primarily control?**

A) The specific creative writing task
B) The persistent persona, constraints, and behavior of the AI
C) The font size of the output
D) The internet connection speed

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It acts as the master instruction set that governs the entire conversation session.

---

### Question 4 (Limitations)
**If you paste a 100-page document into a standard chat window, why does it fail or forget the beginning?**

A) It gets bored.
B) It runs out of Context Window (Memory Buffer) space.
C) It prefers PDF format.
D) The internet timed out.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The Context Window is finite. Data exceeding it falls off the edge.

---

### Question 5 (Technique)
**"Answer this question. Example 1: [Data]->[Answer]. Example 2: [Data]->[Answer]. Task: [New Data]->..."**
**What technique is this?**

A) Zero-Shot
B) Few-Shot Prompting
C) Fine-Tuning
D) Backpropagation

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Providing a "few" examples guides the AI pattern matching significantly better than zero examples.

---

### Question 6 (Architecture)
**What is "Inference"?**

A) The process of training a model for months
B) The process of using a trained model to get an answer/prediction
C) Buying a computer
D) Cleaning data

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Inference is the "Run" phase. Training is the "Build" phase.

---

### Question 7 (Prompt Framework)
**In the PCTF framework, what does "C" stand for, and why does it matter?**

A) Code – It forces code output.
B) Context – It tells the AI the specific situation (e.g., "I'm a beginner cooking at home")
C) Computer – It turns on the device.
D) Color – It highlights text.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Without Context, the AI might guess wrong about your situation, skill level, or constraints.

---

### Question 8 (Safety)
**True or False: It is standard practice to type private bank details or passwords into public AI chatbots to get help with them.**

A) True
B) False

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** NEVER do this. Data sent to public models is often used for training and can be exposed.

---

### Question 9 (AI Types)
**Which model type is best suited for a customer-facing chatbot?**

A) A raw Base Model
B) An Instruct/Chat Fine-Tuned Model
C) An Image Generation Model
D) A Spreadsheet

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Base models just autocomplete. Instruct models are trained to be helpful, answer questions, and follow dialogue.

---

### Question 10 (Analogy)
**If Training an AI is like "years of schooling," then Inference is like:**

A) Writing the textbook
B) Using what you learned on a single test or task
C) Enrolling in school
D) Buying a laptop

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Training (schooling) is hard/slow. Inference (using what you learned) is fast/immediate.

---

### Question 11 (Troubleshooting)
**The AI gives you a generic answer. You realize you didn't tell it *who* it should be acting as. Which Prompt element is missing?**

A) Format
B) Task
C) Persona
D) Delimiters

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** Defining Persona (e.g., "Act as an experienced career coach") calibrates the tone and depth of the answer.

---

### Question 12 (Advanced Technique)
**What is "Prompt Chaining"?**

A) Asking the same question 10 times.
B) Breaking a complex workflow into sequential steps (Step 1 output -> Step 2 input).
C) Linking multiple devices together.
D) A cryptocurrency term.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It allows the AI to focus on one sub-task at a time, improving accuracy for complex workflows.

---

### Question 13 (Math)
**Which typically requires more computational power?**

A) Training a Foundation Model (like GPT-4)
B) Running Inference on a single prompt

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Training takes months on thousands of chips. Inference takes seconds on far less hardware.

---

### Question 14 (Hallucination)
**Why might an AI invent a fact that doesn't exist?**

A) It is trying to trick you on purpose.
B) It is predicting the most probable next word based on patterns, not checking a fact database.
C) It has malicious code.
D) It is angry.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI is probabilistic. If a certain type of answer is usually followed by certain details, it might generate similar-sounding details even when they're wrong, if the context is weak.

---

### Question 15 (Delimiters)
**Which input is safer and clearer for an AI to process?**

A) Fix this: the meeting is cancelled tomorrow
B) Task: Fix any grammar errors in the text below. Text: `### the meeting is cancelled tomorrow ###`

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Clearly separating instructions from data using delimiters (`###`) prevents the AI from confusing the content with the task instructions.

---

## Assessment Complete!

**13-15:** You are ready to start "coding" with plain English.
**10-12:** You understand the concepts but review PCTF.
**<10:** Review Day 2 (LLMs) and Day 3 (Prompting).
