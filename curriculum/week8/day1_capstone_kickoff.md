---
difficulty: Advanced
duration: ~60 minutes
tags:
- prompting
- python
- rag
title: 'Week 8 - Day 1: Capstone Project Kickoff'
week: 8
---

# Week 8 - Day 1: Capstone Project Kickoff

## Overview
**Week 8 – Day 1**
**Topic:** The "AI Business Assistant" Specification
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define the requirements for a unified "AI Business Assistant."
2. Architect the solution using RAG, Tools, and a Supervisor.
3. Prepare the "Dataset" and "Toolbox" for the project.

---

## Lesson Content

### The Goal
For the past 7 weeks, you have built pieces. Now, you build the **Whole**.
You will create a single Interface (Chatbot) for a small business or personal project idea of your choice, that can:
1.  **Answer Common Questions** (using RAG on a mock set of policies/FAQs).
2.  **Check Status** (using mock lookup tools).
3.  **Perform Safe Actions** (using mock action tools, with confirmation).

### The Architecture

**Component 1: The Brain (Supervisor)**
- A centralized "Router" prompt that decides if the user needs Knowledge or Action.

**Component 2: The Library (RAG)**
- A knowledge base containing:
    - `faq_and_policies.md`
    - `product_or_service_catalog.csv`

**Component 3: The Hands (Tools)**
- `check_order_status(order_id)`
- `check_appointment(customer_name)`
- `reschedule_appointment(appointment_id, new_time)`

### The Mock Data

Since we don't have a real business database, you will create **Synthetic Data**.
- **Docs:** Use AI to generate "Fake Company Policies and FAQs."
- **Tools:** Write Python scripts that return "Mock" results (e.g., `check_order_status` always returns "Shipped" for order #1001).

---

## Hands-On Exercise

### Exercise: The Specification Document

**Objective:** Write the "Spec Sheet" for your Assistant.

**1. Name:** (e.g., ShopBot, StudioBot, ClinicBot — pick something for a business or project you find interesting).
**2. User Persona:** A customer or client of the business.
**3. Scope:**
- **In Scope:** Orders/appointments, FAQs, basic status checks.
- **Out of Scope:** Payments processing, legal advice, anything outside the business's core function.
**4. Guardrails:**
- "Must always cite the source document when answering policy questions."
- "Must require 'YES' confirmation before rescheduling or cancelling anything."

**Reflection:**
A clear spec prevents "Scope Creep." This document is your roadmap for the week.

---

## Interactive Daily Quiz

### Question 1 (Strategy)
**Why use "Mock Data" for the Capstone?**

A) To cheat.
B) Because building a real production system is slow/expensive. Mock data allows us to test the *AI Logic* and *Workflow* instantly.
C) Real data is boring.
D) To use less disk space.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Validating the AI's behavior and logic is the goal, not building real infrastructure.

### Question 2 (Architecture)
**Which component handles "What's your policy on..." questions?**

A) The Supervisor.
B) The RAG (Knowledge Base).
C) The Tool (Action).
D) The User.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** "What's your policy" = Knowledge Retrieval.

### Question 3 (Architecture)
**Which component handles "Check the status of my order" requests?**

A) The RAG.
B) The Tool (Action/Lookup API).
C) The general knowledge of the AI.
D) A PDF file.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Status checks = live data fetching via a tool.

### Question 4 (Guardrails)
**"Scope Creep" in AI projects usually leads to:**

A) A better bot automatically.
B) A "Jack of all trades, master of none" that makes more mistakes because the System Prompt has become too complex.
C) More money automatically.
D) Nothing in particular.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Keep the scope narrow and deep for your first project.

### Question 5 (Final)
**Is this project "Low-Code" or "Code"?**

A) Low-Code only.
B) Code only.
C) Hybrid. You can use Low-Code orchestration calling small Python scripts (Tools).

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** The best systems often mix both approaches.

---

### Summary
Today you designed the Blueprint. You defined the Brain, Library, and Hands of your Assistant. Tomorrow, we fill the Library.
