---
difficulty: Advanced
duration: ~60 minutes
tags:
- agents
title: 'Week 7 - Day 3: Building an "Appointment Manager" Bot'
week: 7
---

# Week 7 - Day 3: Building an "Appointment Manager" Bot

## Overview
**Week 7 – Day 3**
**Topic:** Building a Read/Write Transactional Bot
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Design a workflow that involves multiple API steps (Search -> Confirm -> Action).
2. Handle "State" (Remembering the user's intent across the flow).
3. Implement a "Human in the Loop" confirmation step.

---

## Lesson Content

### The "Read-Modify-Write" Loop

A true "Agent" doesn't just look things up. It changes things.
**Scenario:** A user wants to reschedule a hair salon appointment.

**Step 1: Read (Validation)**
- **User:** "Move my appointment to Friday."
- **Bot:** (Calls API) "Check appointments for this user."
- **Result:** "Found an appointment: Thursday 2pm, Haircut with Alex."

**Step 2: Reason & Confirm**
- **Bot:** "I found your Thursday 2pm haircut with Alex. Do you want to move it to Friday at the same time?"
- **User:** "Yes."

**Step 3: Write (Action)**
- **Bot:** (Calls API) `PATCH /appointments/882 { "date": "Friday", "time": "2pm" }`.
- **Bot:** "Done! Your appointment is now Friday at 2pm."

### The "DANGER" of Write Actions

Writing data (creating, changing, or deleting) requires safety.
**Always ask for confirmation.**
- Bad: User says "Cancel my appointments" -> Bot cancels every appointment on file.
- Good: User says "Cancel my appointments" -> Bot says "I found 3 upcoming appointments. Cancel all of them? (Yes/No)".

### Managing ID Confusion

Humans say: "Reschedule **my** appointment."
The API needs: "Reschedule **Appointment #882**."
The Bot's job is to look up the ID associated with the user first (Context Lookup), *then* perform the action.

---

## Hands-On Exercise

### Exercise: The "Note Taker"

**Objective:** A bot that appends notes to a specific customer's file.

**Tools:**
1.  `find_customer(name)` -> Returns Customer ID.
2.  `add_note(customer_id, text)` -> Saves a note.

**Flow:**
1.  User: "Add a note to Sarah Chen's file that she prefers morning appointments."
2.  Bot: Calling `find_customer("Sarah Chen")`.
3.  Tool: Returns `{"id": 42, "name": "Sarah Chen"}`.
4.  Bot: "I found Sarah Chen (ID: 42). Adding note: 'Prefers morning appointments'. Confirm?"
5.  User: "Yes."
6.  Bot: Calling `add_note(42, "Prefers morning appointments")`.
7.  Bot: "Note added."

**Reflection:**
Notice the intermediate step where the Bot confirmed the customer's identity. This prevents adding notes to the wrong person's file.

---

## Interactive Daily Quiz

### Question 1 (Safety)
**What is "Human in the Loop"?**

A) A person stuck in a revolving door.
B) Pausing the automated workflow to ask the user for confirmation before executing a meaningful action.
C) A looping script.
D) A type of software deployment.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Critical for "Write" actions that change real data.

### Question 2 (API)
**Which HTTP method updates existing data?**

A) GET.
B) PATCH or PUT.
C) DELETE.
D) OPTIONS.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** POST creates new data, PATCH/PUT updates existing data.

### Question 3 (Logic)
**Why must the bot "Read" before it "Writes"?**

A) To verify the resource exists and the current state is valid for the change.
B) It takes longer to do so, which is inherently better.
C) To use more bandwidth.
D) It isn't actually necessary.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Never update something that doesn't exist, or that you haven't correctly identified.

### Question 4 (Identity)
**The API requires a Customer ID, but the user just said "my file." What should the bot do?**

A) Guess a random ID.
B) Always use ID 1.
C) Ask the user for identifying details, or look them up based on name/contact info.
D) Give up immediately.

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** "Slot Filling" is the process of asking for or looking up missing parameters.

### Question 5 (State)
**In a multi-turn conversation, where is the "Appointment ID" stored while waiting for confirmation?**

A) In the Vector Database.
B) In the Conversation Memory/Context.
C) On a piece of paper somewhere.
D) Nowhere, it's forgotten.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The chat history lets the bot "remember" what's being discussed across the back-and-forth.

---

### Summary
Today you built an **Appointment Manager**. You learned the critical pattern of "Read -> Confirm -> Write" to safely modify real data. Tomorrow, we scale up to **Multi-Agent** systems.
