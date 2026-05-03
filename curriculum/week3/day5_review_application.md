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
| **Translator** | Change Language/Tone | Tech Jargon | Executives Speak | "Incident Report to CEO" |
| **Summarizer** | Compress Data | 100 Pages | 1 Page | "Summarize Logs" |
| **Extractor** | Structure Data | Messy Text | JSON / CSV | "Parse Email to Ticket" |
| **Generator** | Create New Content | Constraints | Code / Config | "Write Python Script" |

### Advanced: Pattern Chaining (The "Combo Move")

Real power comes from combining these.

**Scenario:** You receive a messy vendor security notification (PDF text). You need to patch your servers.

1.  **Step 1 (Summarize):** "Summarize this PDF to find the affected versions." -> *Output: v1.0 to v1.2.*
2.  **Step 2 (Generate):** "Write a Bash script to check if the local version is between v1.0 and v1.2." -> *Output: audit_script.sh*
3.  **Step 3 (Translate):** "Write an email to the Manager explaining we are running an audit script." -> *Output: Email draft.*

You just automated a complex workflow using 3 AI prompts.

---

## Hands-On Exercise

### Exercise: The "AI Toolbox" Construction

**Objective:** Create a text file (`my_prompts.txt`) with your 4 "Go-To" prompts.

**Task:** Write one high-quality, reusable prompt for each category below. Use the **PCTF** (Persona, Context, Task, Format) structure.

1.  **The "Log Cleaner" (Summarizer):** A prompt you can paste logs into to get a clean table of errors.
2.  **The "Script Fixer" (Translator/Generator):** A prompt to fix/explain broken code.
3.  **The "Config Parser" (Extractor):** A prompt to pull IP addresses from CLI output.
4.  **The "Email Polisher" (Translator):** A prompt to turn your bullet points into a professional email.

**Self-Check:**
- Do they have constraints? (e.g., "Do not hallucinate," "Use JSON format").
- Are they generic enough to reuse tomorrow?

---

## Weekly Assignment

### Assignment: The "Incident Response" Simulation

**Scenario:**
You are on call. Use AI to handle this incident.

**Input Data (The Alert):**
`Alert: High latency detected on Uplink-A (192.168.1.1). Pings dropping. Traffic 98% utilization.`

**Part 1 (Generate):**
Ask AI to generate 3 commands to diagnose high bandwidth on a Cisco router.
*(Expected: `show interface`, `show ip cache flow`, `show processes cpu`)*

**Part 2 (Summarize/Explain):**
Imagine the output shows "Protocol: UDP 53 (DNS)" is 90% of traffic.
Ask AI to explain: "What does a flood of UDP 53 traffic usually indicate?"
*(Expected: DNS Amplification DDoS attack).*

**Part 3 (Translator):**
Draft an update to the stakeholders using the Translator pattern.
*(Expected: "We are mitigating a cyber-attack targeting our DNS infrastructure...")*

**Submission:**
Submit the 3 prompts you used.

---

## Weekly Interactive Quiz

### Question 1 (Pattern Identification)
**You paste a list of 500 employee names and ask the AI: "Format this as a CSV file with columns First, Last, Email." Which pattern is this?**

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
**In the "Generator" pattern, why should you ask for "Comments explaining the code"?**

A) To make the file larger.  
B) To help you verify and understand what the AI wrote, ensuring it isn't doing something dangerous.  
C) AI cannot write comments.  
D) Comments are for weak programmers.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI code is a "Black Box" until you read it. Comments help you audit the logic.

### Question 4 (Toolbox)
**Which of these is a good reusable System Prompt for a "Translator" tool?**

A) "Hello."  
B) "You are a Corporate Communication Expert. Your goal is to rewrite technical notes into professional, clear, business-friendly emails."  
C) "Write code."  
D) "Summarize this."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It sets the Persona and the Goal clearly.

### Question 5 (Reality)
**Can AI replace the need for you to understand Networking?**

A) Yes, AI knows everything.  
B) No. You need domain knowledge to Prompt correctly ("Context") and to Verify the output ("Hallucination check").  
C) Maybe in 100 years.  
D) Yes, if you pay for premium.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI amplifies your knowledge; it doesn't replace it. You can't prompt for a BGP fix if you don't know what BGP is.

---

### End of Week 3
**Congratulations!** You now have a toolkit of **Practical Patterns**. You can Translate, Summarize, Extract, and Generate.
**Next Week:** We tack into **Advanced Prompting**—Building complex chains and "Agents" that do work for you.