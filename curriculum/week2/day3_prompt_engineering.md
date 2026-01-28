# Week 2 - Day 3: Prompt Engineering Fundamentals - The New Syntax

## Overview
**Week 2 – Day 3**  
**Topic:** How to Speak "AI" – Basic Prompting Strategies  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define "Prompt Engineering" as "coding with natural language"
2. Apply the "Persona, Context, Task, Format" framework
3. Explain why being specific reduces "hallucination"
4. Write a prompt to generate a usable Python/Bash script
5. Critique and improve a vague prompt

---

## Lesson Content

### Prompting = Coding

As a network admin, you know the CLI syntax.
- `show ip int brief` works.
- `show me the interfaces please` fails.

With AI, "show me the interfaces please" *works*, but it might give you a generic explanation instead of the command.
**Prompt Engineering** is the skill of crafting inputs to get the *exact* output you want. It's the new CLI syntax, but the syntax is English (or any language).

### The Framework: PCTF

To get consistent results, use the **PCTF** Framework:

1.  **P - Persona:** Who should the AI be?
2.  **C - Context:** What is the situation?
3.  **T - Task:** What exactly applies?
4.  **F - Format:** How do you want the answer?

#### Example: Generating a Script

**Bad Prompt:**
"Write a backup script."

**Good Prompt (PCTF):**
- **Persona:** Act as a Senior Linux Systems Administrator.
- **Context:** We have a PostgreSQL database on Ubuntu 20.04 that needs nightly backups to an S3 bucket.
- **Task:** Write a bash script to dump the database, compress it, upload to S3, and delete local files older than 7 days. Add error handling.
- **Format:** Provide only the code block with comments explaining each step.

**Why the "Bad Prompt" Fails:**
The AI has to guess: Windows or Linux? SQL or Files? Local or Cloud? Python or Bash?
**Guessing = Hallucination Risk.** By providing constraints, you force the AI into a narrow lane of success.

### Zero-Shot vs. Few-Shot Prompting

**Zero-Shot:**
Asking the AI to do something without examples.
> "Classify this log: [Log Line]"

**Few-Shot (The Power Move):**
Giving the AI examples of what you want *before* asking.

> "Classify these logs.
> Example 1: `Connection refused` -> Network Error
> Example 2: `Disk full` -> Storage Error
>
> Task: `User not found` -> [AI Fills this in]"

**Why this matters for Admins:**
If you want the AI to parse your proprietary custom log format, **give it 3 examples**. It will learn the pattern instantly (In-Context Learning) and parse the 4th one correctly.

### Iterative Refinement

Your first prompt will rarely be perfect. Treat it like debugging code.
1.  Run Prompt.
2.  Check Output: "It gave me Python, I wanted Bash."
3.  Refine Prompt: "Rewrite in Bash."
4.  Check Output: "It didn't check for sudo."
5.  Refine Prompt: "Add a check to ensure the script is run as root."

### The "Chain of Thought" Trick

For complex reasoning, tell the AI:
**"Let's think step by step."**

This magic phrase forces the model to output its reasoning *before* the final answer.
- **Without it:** AI tries to jump to the answer (Risk of math/logic errors).
- **With it:** AI writes: "First, I need to check the mask. /24 means 256 IPs. Then reserve gateway..." -> Correct Answer.

---

## Hands-On Exercise

### Exercise: The "Ticket Responder" Prompt

**Objective:** Write a prompt to turn rude/vague user tickets into polite, professional responses.

**Scenario:** A user sends a ticket: *"INTERNET BROKEN. FIX NOW. I CANT WORK."*

**Task 1: Try a Basic Prompt** (Mental or scratchpad)
"Reply to this email."
*Result:* Likely too generic, maybe too apologetic, or misses the troubleshooting steps.

**Task 2: Build a PCTF Prompt**
Fill in the blanks:

- **Persona:** Experienced IT Helpdesk Manager. Calm, professional, empathetic but firm.
- **Context:** User is reporting connectivity issues. We need to verify if it's Wi-Fi or wired, and if other users are affected.
- **Task:** Draft a reply acknowledging the frustration. Ask 3 specific troubleshooting questions. Do not promise a fix time yet.
- **Format:** Email format, ready to send.

**Task 3: Apply "Few-Shot" (Optional)**
Add an example of your company's tone.
"Style Example: 'Hi [Name], thanks for reaching out. I understand this is blocking your work...'"

**Reflection:**
How much time would this save your helpdesk team if they had a button that auto-generated these drafts?

---

## Interactive Daily Quiz

### Question 1 (Strategy)
**Which prompt is most likely to generate a high-quality Python script for network scanning?**

A) "Code a scanner."  
B) "Write a Python script."  
C) "Act as a security engineer. Write a flexible Python 3 script using the 'scapy' library to scan subnet 192.168.1.0/24 for open port 80. Include comments and error handling."  
D) "Can you help me with my computer?"  

**Correct Answer:** C

**Feedback:**
- **A) Incorrect.** Too vague.
- **B) Incorrect.** Language is specified, but function is not.
- **C) ✓ Correct!** Uses PCTF: Persona (Sec Eng), Context (Scapy/Port 80), Task (Scan subnet), Format (Python 3 w/ comments).
- **D) Incorrect.**

**Why this matters:** Time spent writing a detailed prompt saves 10x the time fixing bad code later.

### Question 2 (Technique)
**You want the AI to categorize alerts into "Critical", "Warning", or "Info". You provide the AI with 3 examples of previous alerts and their correct categories before asking it to categorize a new one. What is this technique called?**

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

**Why this matters:** Few-shot prompting is the single most powerful tool for getting AI to follow your specific company standards/formats.

### Question 3 (Concept)
**Why does adding "Let's think step by step" help with complex network subnetting math problems?**

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

**Why this matters:** Always use this phrase when asking the AI to diagnose a root cause or calculate IP ranges.

### Question 4 (Application)
**You prompt ChatGPT: "Write a config for a switch." It responds with a Juniper config, but you have Cisco switches. Which element of the PCTF framework did you miss?**

A) Persona  
B) Context  
C) Task  
D) Format  

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.**
- **B) ✓ Correct!** You failed to provide the **Context** that you operate a Cisco environment. The AI guessed (hallucinated) the wrong vendor.
- **C) Incorrect.** It did the task (write config).
- **D) Incorrect.**

**Why this matters:** Context is king. Never assume the AI knows your environment unless you tell it.

### Question 5 (Safety)
**What happens if you input your company's sensitive root passwords into a public standard ChatGPT prompt?**

A) Nothing, it's safe.  
B) The passwords might be used for training future models and could theoretically be exposed.  
C) The AI will refuse to read them.  
D) It encrypts them automatically.  

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Dangerous assumption.
- **B) ✓ Correct!** Most public AI terms of service allow them to use your chats for training. **NEVER** paste secrets (keys, passwords, PII) into public chatbots.
- **C) Incorrect.** It will happily read them.
- **D) Incorrect.**

**Why this matters:** Data Privacy 101. If you wouldn't post it on Reddit, don't paste it into public ChatGPT.

---

### Summary
Today you learned to Program in English. You mastered the **PCTF Framework** (Persona, Context, Task, Format) and learned why **Few-Shot Prompts** (examples) are superior to vague requests. You also learned the "Step by Step" magic phrase. Tomorrow, we go deeper into **Advanced Prompting**—automating complex workflows.
