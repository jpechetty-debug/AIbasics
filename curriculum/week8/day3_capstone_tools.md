---
difficulty: Advanced
duration: ~90 minutes
tags:
- prompting
- python
title: 'Week 8 - Day 3: Building the Action Layer'
week: 8
---

# Week 8 - Day 3: Building the Action Layer

## Overview
**Week 8 – Day 3**  
**Topic:** Coding the Mock Tools (Python/API)  
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Write Python scripts that simulate network actions.
2. Wrap these scripts in a "Tool Definition" (JSON).
3. Connect them to the Assistant.

---

## Lesson Content

### The Mock Tool Strategy

We don't want to actually reboot a real server. We want to **simulate** it.

### Tool 1: `check_status(hostname)`

**Python Logic:**
```python
def check_status(hostname):
    if hostname == "critical-server":
        return "CRITICAL: High CPU (99%)"
    else:
        return "NORMAL: CPU (12%)"
```
**JSON Definition:**
- Description: "Checks the health of a device."
- Param: `hostname`.

### Tool 2: `reboot_device(hostname)`

**Python Logic:**
```python
def reboot_device(hostname):
    return f"SUCCESS: Device {hostname} has been rebooted. Uptime is now 0."
```
**JSON Definition:**
- Description: "Reboots a device. WARNING: Service impact."
- Param: `hostname`.

### Tool 3: `run_diagnostic(ip)`

**Python Logic:**
- Return a standard "Ping Success, Traceroute Complete" string.

---

## Hands-On Exercise

### Exercise: The "Mock API"

**Objective:** Create these functions in a single Python file (`tools.py`) or within your Low-Code environment's "Custom Tool" block.

**Workflow:**
1.  **Define:** Write the Python code.
2.  **Describe:** Write the JSON schema.
3.  **Test:** Ask the bot: "Check status of critical-server."

**Success Criteria:**
- The bot replies: "The status of critical-server is CRITICAL: High CPU (99%)."
- It did *not* make this up. It ran your code.

**Reflection:**
You have created a "Digital Twin" of a network environment. This allows you to demo the bot's capabilities safely.

---

## Interactive Daily Quiz

### Question 1 (Simulation)
**Why do `if/else` statements make good mock tools?**

A) They allow you to deterministically test how the bot handles "Good" vs "Bad" scenarios.  
B) They are fast.  
C) They are simple.  
D) All of the above.  

**Correct Answer:** D

**Feedback:**
- **D) ✓ Correct!** You can force the bot to deal with a "Down" server by naming it "critical-server".

### Question 2 (Safety)
**What should the `reboot_device` tool description include?**

A) "Use this for fun."  
B) "WARNING: Use only after confirmation."  
C) "Nothing."  
D) "Magic."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The description prompts the Supervisor to ask for user permission.

### Question 3 (Input)
**The bot calls `check_status` with `hostname="Server 1"`. The code expects `server-1` (lowercase). What failed?**

A) The Tool Logic (Robustness).  
B) The LLM.  
C) The User.  
D) The Network.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Your tool code should sanitize inputs (e.g., `hostname.lower().replace(" ", "-")`). Don't expect the LLM to be perfect.

### Question 4 (Feedback)
**The tool returns a JSON string `{ "cpu": 99, "status": "bad" }`. What does the LLM do?**

A) It displays the raw JSON to the user.  
B) It reads it, interprets it, and says "The CPU is high."  
C) It crashes.  
D) It ignores it.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The LLM translates the Tool Data back into Natural Language.

### Question 5 (Limits)
**Can you have a tool that calls another tool?**

A) Yes (Chain).  
B) No.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** `diagnose_and_fix` could call `check_status` then `reboot`.

---

### Summary
Today you gave the bot Hands. It can now "Check" and "Fix" your simulated network. Tomorrow, we turn it on.