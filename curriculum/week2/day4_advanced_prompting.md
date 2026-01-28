# Week 2 - Day 4: Advanced Prompting - System Prompts and Chaining

## Overview
**Week 2 – Day 4**  
**Topic:** Automating Workflows with Advanced Prompt Structures  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Distinguish between "System Prompts" and "User Prompts"
2. Create a "Meta-Prompt" to turn the AI into a specific tool (e.g., Log Analyzer)
3. Understand "Prompt Chaining" (breaking complex tasks into steps)
4. Use Delimiters to structure complex data inputs
5. Build a reusable "Troubleshooting Assistant" prompt template

---

## Lesson Content

### System vs. User Prompts

Most modern AI models (like GPT-4) take two main inputs:
1.  **System Prompt:** The "God Mode" instructions. Who the AI *is* and how it *must* behave. These persist throughout the conversation.
2.  **User Prompt:** The specific request you type right now.

**Analogy:**
- **System Prompt:** The HR Job Description and Employee Handbook (Defines the role).
- **User Prompt:** The daily email task assignment (Defines the work).

**Example System Prompt:**
> "You are a specialized Network Security Analyst. You act conservatively. You NEVER recommend 'allow all' rules. You always cite the specific CVE when discussing vulnerabilities. If you don't know, say 'I need more investigation'."

**Why this matters:**
Setting a strong System Prompt prevents the AI from drifting out of character. It keeps the "Junior Engineer" focused.

### The Power of Delimiters

When pasting logs or configs, the AI can get confused about where instructions end and data begins.
Use **XML tags** or **Triple Backticks** to fence your data.

**Bad:**
Analyze this log error: connection refused at 10:00

**Good:**
> Analyze the log data located inside the `<log>` tags.
>
> `<log>`
> timestamp=10:00 msg="connection refused" src=192.168.1.5
> `</log>`

This is safer and more accurate. It separates **Code (Instructions)** from **Data (Logs)**.

### Prompt Chaining: Break it Down

Don't ask the AI to "Analyze the logs, find the error, write a fix, and email the report" in one giant breath. It will likely do a mediocre job at all four.

**Chain it:**
1.  **Prompt 1:** "Analyze these logs and list the top 3 anomalies." -> *Get Output X.*
2.  **Prompt 2:** "Take Output X. For anomaly #1, write a remediation script." -> *Get Output Y.*
3.  **Prompt 3:** "Draft an incident report summarizing X and Y."

**Why this matters:**
This mimics how you work. You don't do everything instantly. You analyze, *then* code, *then* report. Breaking it down (Chaining) drastically improves quality.

### Building a "Tool" Prompt

You can save a prompt that acts like a software tool.

**The "Config Auditor" Prompt:**
> **System:** You are a Cisco Configuration Auditor.
> **Task:** I will paste a config. You will check it against these 3 rules ONLY:
> 1. No weak encryption (DES/3DES).
> 2. SSH timeout must be < 10 mins.
> 3. Passwords must be hashed (Type 5 or 9).
>
> **Output:** A table: | Violation | Line Number | Severity |

Once saved, you just paste configs into this chat. You've built a "No-Code Compliance Tool."

---

## Hands-On Exercise

### Exercise: Build Your Own "Documentation Generator"

**Objective:** Create a reusable prompt that turns messy CLI output into clean documentation.

**Scenario:** You often run `show ip interface brief` and need to put that into a report table.

**Task 1: Architect the System Prompt**
- **Persona:** Technical Documentation Specialist.
- **Rules:** Output must be Markdown. Do not include unassigned interfaces. Convert status codes (up/up) to Emojis (✅/❌).

**Task 2: Draft the User Prompt Structure**
> "Here is the raw CLI output:
> ```
> [PASTE OUTPUT HERE]
> ```
> Convert this to the requested table format."

**Task 3: Test and Refine**
- Does it handle "Administrative Down" correctly?
- Did it exclude unassigned IPs?
- **Iterate:** Add a rule: "If description is missing, mark as 'Needs Audit'."

**Reflection:**
You just built a "text processing app" without writing a line of Python or Regex.

---

## Interactive Daily Quiz

### Question 1 (Architecture)
**What is the primary purpose of the "System Prompt"?**

A) To provide the specific question for the day.  
B) To set the persistent behavior, persona, and constraints of the AI.  
C) To reboot the server.  
D) To format the text as bold.  

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** That's the User Prompt.
- **B) ✓ Correct!** The System Prompt defines "Who" the AI is (e.g., "You are a Python Expert") and stays active for the whole chat.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** Using System Prompts is key to creating reliable, specialized AI assistants for your team.

### Question 2 (Technique)
**Why should you use delimiters like `<config>` ... `</config>` or ` ``` ` when pasting technical data?**

A) It looks pretty.  
B) It triggers the developer mode.  
C) It clearly separates the "Instructions" (what the AI should do) from the "Data" (the content to process).  
D) It encrypts the data.  

**Correct Answer:** C

**Feedback:**
- **A) Incorrect.**
- **B) Incorrect.**
- **C) ✓ Correct!** Without limits, the AI might try to "execute" a command found in your logs. Delimiters prevent this confusion.
- **D) Incorrect.**

**Why this matters:** It prevents "Prompt Injection" (accidental or intentional) where data confuses the model instructions.

### Question 3 (Strategy)
**You have a complex task: "Analyze 50 router configs, identify VLAN mismatches, propose a fix, and write a change request ticket." What is the best approach?**

A) Put it all in one massive prompt.  
B) Prompt Chaining: Break it into 3 steps (Analyze -> Fix -> Report).  
C) Don't use AI.  
D) Use a Base model.  

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Too complex; the AI will likely hallway-do each part or forget constraints.
- **B) ✓ Correct!** Chaining results in higher quality. Step 1's output becomes Step 2's input.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** Complex logic requires "time to think." Splitting tasks gives the AI that focus.

### Question 4 (Application)
**You are creating a "Security Guard" chatbot. What instruction belongs in the SYSTEM prompt?**

A) "Check if IP 1.2.3.4 is malicious."  
B) "You must never generate code that exploits vulnerabilities. You answer only defensively."  
C) "Write a poem about firewalls."  
D) "Hello, how are you?"  

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Specific task = User Prompt.
- **B) ✓ Correct!** Global behavioral constraint ("Never exploit") = System Prompt.
- **C) Incorrect.**
- **D) Incorrect.**

**Why this matters:** Safety rails belong in the System rules so users can't override them easily.

### Question 5 (Troubleshooting)
**The AI keeps giving you Python code when you want Bash. How do you fix this permanently for this session?**

A) Keep asking "In Bash please" every time.  
B) Update the System Prompt (or custom instructions) to say: "Always provide solutions in Bash unless requested otherwise."  
C) Revert to Google.  
D) Yell at the screen.  

**Correct Answer:** B

**Feedback:**
- **A) Incorrect.** Tedious and inefficient.
- **B) ✓ Correct!** Set the rule once in the Global instructions, and the AI will follow it for every subsequent reply.
- **C) Incorrect.**
- **D) Incorrect.** Therapeutic, but ineffective.

**Why this matters:** Customize the AI to your environment. If you are a Windows shop, set "Default to PowerShell" as a global rule.

---

### Summary
Today you moved from "User" to "Architect." You learned how **System Prompts** define the AI's role, how **Delimiters** keep data safe, and how **Prompt Chaining** handles complex workflows. You are effectively learning how to "program" the AI using English. Tomorrow, we finish the week with a review and a deeper look at AI Tools.
