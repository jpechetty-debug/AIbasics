# Week 8 - Day 1: Capstone Project Kickoff

## Overview
**Week 8 – Day 1**  
**Topic:** The "AI Network Assistant" Specification  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define the requirements for the unified "AI Network Assistant."
2. Architecture the solution using RAG, Tools, and a Supervisor.
3. Prepare the "Dataset" and "Toolbox" for the project.

---

## Lesson Content

### The Goal
For the past 7 weeks, you have built pieces. Now, you build the **Whole**.
You will create a single Interface (Chatbot) that can:
1.  **Answer Technical Questions** (using RAG on a Mock Documentation Set).
2.  **Diagnose Issues** (using Mock Diagnostic Tools).
3.  **Perform Safe Actions** (using Mock Action Tools).

### The Architecture

**Component 1: The Brain (Supervisor)**
- A centralized "Router" prompt that decides if the user needs Knowledge or Action.

**Component 2: The Library (RAG)**
- A Vector Store containing:
    - `standard_operating_procedures.md`
    - `network_diagram_specs.md`
    - `ip_address_plan.csv`

**Component 3: The Hands (Tools)**
- `ping_device(ip)`
- `get_interface_status(switch, port)`
- `backup_config(device)`

### The Mock Data

Since we don't have a real network, you will create **Synthetic Data**.
- **Docs:** Use AI to generate "Fake Company Network Policies."
- **Tools:** Write Python scripts that return "Mock" results (e.g., `ping` always returns "Success" for 10.1.1.1).

---

## Hands-On Exercise

### Exercise: The Specification Document

**Objective:** Write the "Spec Sheet" for your Assistant.

**1. Name:** (e.g., NetOps-9000).
**2. User Persona:** Junior Admin.
**3. Scope:**
- **In Scope:** Cisco Switches, SOPs, IP Lookups.
- **Out of Scope:** Servers, Emails, Coffee.
**4. Guardrails:**
- "Must always cite the SOP ID."
- "Must require 'YES' confirmation before rebooting."

**Reflection:**
A clear spec prevents "Scope Creep." This document is your roadmap for the week.

---

## Interactive Daily Quiz

### Question 1 (Strategy)
**Why use "Mock Data" for the Capstone?**

A) To cheat.  
B) Because building a real physical network lab is slow/expensive. Mock data allows us to test the *AI Logic* and *Workflow* instantly.  
C) Real data is boring.  
D) To use less disk space.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Validating the AI behavior is the goal.

### Question 2 (Architecture)
**Which component handles "How do I..." questions?**

A) The Supervisor.  
B) The RAG (Knowledge Base).  
C) The Tool (Action).  
D) The User.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** "How-To" = Knowledge Retrieval.

### Question 3 (Architecture)
**Which component handles "Check status of..." requests?**

A) The RAG.  
B) The Tool (Action API).  
C) The Database.  
D) The PDF.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Status = Live Data Fetching.

### Question 4 (Guardrails)
**"Scope Creep" in AI projects usually leads to:**

A) A better bot.  
B) A "Jack of all trades, master of none" that hallucinates often because the System Prompt is too complex.  
C) More money.  
D) Happiness.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Keep the scope narrow and deep.

### Question 5 (Final)
**Is this project "Low-Code" or "Code"?**

A) Low-Code only.  
B) Code only.  
C) Hybrid. You can use Low-Code orchestration (Flowise) calling Python Scripts (Tools).  

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** The best systems mix both.

---

### Summary
Today you designed the Blueprint. You defined the Brain, Library, and Hands of your Assistant. Tomorrow, we fill the Library.
