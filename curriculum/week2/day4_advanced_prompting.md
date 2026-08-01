---
difficulty: Beginner
duration: ~60 minutes
tags:
- prompting
- python
title: 'Week 2 - Day 4: Advanced Prompting - System Prompts and Chaining'
week: 2
---

# Week 2 - Day 4: Advanced Prompting - System Prompts and Chaining

## Overview
**Week 2 – Day 4**
**Topic:** Automating Workflows with Advanced Prompt Structures
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Distinguish between "System Prompts" and "User Prompts"
2. Create a "Meta-Prompt" to turn the AI into a specific reusable tool
3. Understand "Prompt Chaining" (breaking complex tasks into steps)
4. Use Delimiters to structure complex data inputs
5. Build a reusable "Assistant" prompt template

---

## Lesson Content

### System vs. User Prompts

Most modern AI models (like GPT-4 or Claude) take two main inputs:
1.  **System Prompt:** The "master" instructions. Who the AI *is* and how it *must* behave. These persist throughout the conversation.
2.  **User Prompt:** The specific request you type right now.

**Analogy:**
- **System Prompt:** A job description and employee handbook (Defines the role).
- **User Prompt:** The specific task assigned today (Defines the work).

**Example System Prompt:**
> "You are a supportive personal finance coach. You are encouraging but honest. You NEVER recommend risky investments. You always mention that you're not a licensed financial advisor. If you don't know something, say 'I'd recommend checking with a professional.'"

**Why this matters:**
Setting a strong System Prompt prevents the AI from drifting out of character. It keeps the "assistant" focused and consistent.

### The Power of Delimiters

When pasting long text or data, the AI can get confused about where instructions end and data begins.
Use **XML tags** or **Triple Backticks** to fence your data.

**Bad:**
Analyze this feedback: the app keeps crashing

**Good:**
> Analyze the customer feedback located inside the `<feedback>` tags.
>
> `<feedback>`
> "The app keeps crashing every time I try to upload a photo."
> `</feedback>`

This is safer and more accurate. It separates **Instructions** from **Data**.

### Prompt Chaining: Break it Down

Don't ask the AI to "Read these reviews, find the top complaints, write a response plan, and draft a customer email" in one giant breath. It will likely do a mediocre job at all four.

**Chain it:**
1.  **Prompt 1:** "Read these reviews and list the top 3 recurring complaints." -> *Get Output X.*
2.  **Prompt 2:** "Take Output X. For complaint #1, suggest a fix." -> *Get Output Y.*
3.  **Prompt 3:** "Draft a customer-facing update summarizing X and Y."

**Why this matters:**
This mimics how you naturally work through a problem. You don't do everything instantly — you understand, *then* plan, *then* communicate. Breaking it down (Chaining) drastically improves quality.

### Building a "Tool" Prompt

You can save a prompt that acts like a mini software tool.

**The "Resume Reviewer" Prompt:**
> **System:** You are a career coach reviewing resumes for clarity and impact.
> **Task:** I will paste a resume bullet point. You will check it against these 3 rules ONLY:
> 1. Does it start with a strong action verb?
> 2. Does it include a measurable result (a number or outcome)?
> 3. Is it under 2 lines long?
>
> **Output:** A table: | Issue | Suggestion |

Once saved, you just paste bullet points into this chat. You've built a "no-code resume tool."

---

## Hands-On Exercise

### Exercise: Build Your Own "Note Cleaner"

**Objective:** Create a reusable prompt that turns messy meeting notes into a clean summary.

**Scenario:** You often take rushed, messy notes during meetings or calls and need them turned into a clean action list.

**Task 1: Architect the System Prompt**
- **Persona:** Executive Assistant who is excellent at organizing information.
- **Rules:** Output must be in Markdown. Group items into "Decisions Made" and "Action Items." Assign an owner to each action item if mentioned.

**Task 2: Draft the User Prompt Structure**
> "Here are my raw notes:
> ```
> [PASTE NOTES HERE]
> ```
> Convert this to the requested format."

**Task 3: Test and Refine**
- Does it correctly separate decisions from action items?
- Did it catch every owner mentioned?
- **Iterate:** Add a rule: "If no owner is mentioned, mark as 'Unassigned.'"

**Reflection:**
You just built a "text processing tool" without writing a single line of code.

---

## Interactive Daily Quiz

### Question 1 (Architecture)
**What is the primary purpose of the "System Prompt"?**

A) To provide the specific question for the day.
B) To set the persistent behavior, persona, and constraints of the AI.
C) To restart the app.
D) To format the text as bold.

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** That's the User Prompt.
- **B) ✓ Correct!** The System Prompt defines "Who" the AI is (e.g., "You are a career coach") and stays active for the whole chat.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** Using System Prompts is key to creating reliable, specialized AI assistants for anything you do repeatedly.

### Question 2 (Technique)
**Why should you use delimiters like `<notes>` ... `</notes>` or ` ``` ` when pasting long text?**

A) It looks pretty.
B) It triggers a special mode.
C) It clearly separates the "Instructions" (what the AI should do) from the "Data" (the content to process).
D) It encrypts the data.

**Correct Answer:** C

**Feedback:**
- **A) Incorrect.**
- **B) Incorrect.**
- **C) ✓ Correct!** Without limits, the AI might try to "follow" an instruction found accidentally inside your pasted text. Delimiters prevent this confusion.
- **D) Incorrect.**

**Why this matters:** It prevents your data from being mistaken for instructions, especially with long or messy pasted text.

### Question 3 (Strategy)
**You have a complex task: "Read these 50 customer reviews, identify common complaints, propose fixes, and draft a summary email to the team." What is the best approach?**

A) Put it all in one massive prompt.
B) Prompt Chaining: Break it into steps (Analyze -> Propose Fixes -> Draft Email).
C) Don't use AI.
D) Use a Base model.

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Too complex; the AI will likely do a mediocre job on each part or forget constraints.
- **B) ✓ Correct!** Chaining results in higher quality. Step 1's output becomes Step 2's input.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** Complex thinking requires "time to think." Splitting tasks gives the AI that focus, and gives you a chance to check its work along the way.

### Question 4 (Application)
**You are creating a "Study Buddy" chatbot for yourself. What instruction belongs in the SYSTEM prompt?**

A) "Explain photosynthesis to me."
B) "You always explain concepts with an everyday analogy before giving the technical definition."
C) "Write a poem about spring."
D) "Hello, how are you?"

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Specific task = User Prompt.
- **B) ✓ Correct!** A global, persistent behavior rule ("always use an analogy first") = System Prompt.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** Rules you want followed in every response belong in the System Prompt, not repeated every time.

### Question 5 (Troubleshooting)
**The AI keeps giving you long, formal responses when you want short, casual ones. How do you fix this permanently for a conversation?**

A) Keep asking "shorter please" every time.
B) Update the System Prompt (or custom instructions) to say: "Always respond briefly and casually unless asked otherwise."
C) Switch to a different app entirely.
D) Give up on using AI.

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Tedious and inefficient.
- **B) ✓ Correct!** Set the rule once in the system instructions, and the AI will follow it for every subsequent reply.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** Customize the AI to your own preferences. Setting a tone or format rule once saves repeating yourself constantly.

---

### Summary
Today you moved from "User" to "Designer." You learned how **System Prompts** define the AI's role, how **Delimiters** keep data safe, and how **Prompt Chaining** handles complex workflows. You are effectively learning how to "program" the AI using plain English. Tomorrow, we finish the week with a review and a deeper look at putting it all together.
