# Week 7 - Day 3: Building a "Ticket Master" Bot

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
**Scenario:** A user wants to upgrade a ticket priority.

**Step 1: Read (Validation)**
- **User:** "Escalate Ticket #500."
- **Bot:** (Calls API) "Check Ticket #500".
- **Result:** "Ticket #500 exists. Current Priority: Low."

**Step 2: Reason & Confirm**
- **Bot:** "Ticket #500 is currently 'Low'. Do you want to set it to 'High'?"
- **User:** "Yes."

**Step 3: Write (Action)**
- **Bot:** (Calls API) `PATCH /tickets/500 { "priority": "high" }`.
- **Bot:** "Done. Priority is now High."

### The "DANGER" of Write Actions

Writing data (POST/PATCH/DELETE) requires safety.
**Always ask for confirmation.**
- Bad: User says "Delete everything" -> Bot deletes everything.
- Good: User says "Delete everything" -> Bot says "I found 50 items. Are you sure? (Yes/No)".

### Managing ID Confusion

Humans say: "Escalate **my** ticket."
API needs: "Escalate **INC-998877**."
The Bot's job is to look up the ID associated with the user first (Context Lookup), *then* perform the action.

---

## Hands-On Exercise

### Exercise: The "Note Taker"

**Objective:** A bot that appends notes to a specific server log.

**Tools:**
1.  `find_server(name)` -> Returns Server ID.
2.  `add_note(server_id, text)` -> POSTs note.

**Flow:**
1.  User: "Add a note to the web server that I'm patching it."
2.  Bot: Calling `find_server("web server")`.
3.  Tool: Returns `{"id": 42, "name": "Web-Prod-01"}`.
4.  Bot: "I found 'Web-Prod-01' (ID: 42). Adding note: 'Patching it'. Confirm?"
5.  User: "Yes."
6.  Bot: Calling `add_note(42, "Patching it")`.
7.  Bot: "Note added."

**Reflection:**
Notice the intermediate step where the Bot confirmed the Server ID. This prevents adding notes to the wrong server.

---

## Interactive Daily Quiz

### Question 1 (Safety)
**What is "Human in the Loop"?**

A) A person stuck in a spinning door.  
B) Pausing the automated workflow to ask the user for confirmation before executing a critical action.  
C) A looping script.  
D) A continuous deployment.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Critical for "Write" actions.

### Question 2 (API)
**Which HTTP method updates existing data?**

A) GET.  
B) PATCH or PUT.  
C) DELETE.  
D) OPTION.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** POST creates, PATCH/PUT updates.

### Question 3 (Logic)
**Why must the bot "Read" before it "Writes"?**

A) To verify the resource exists and the current state is valid for the change.  
B) It takes longer.  
C) To use more bandwidth.  
D) It isn't necessary.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Never update a Phantom.

### Question 4 (Identity)
**The API requires a User ID, but the user didn't provide it. What should the bot do?**

A) Guess.  
B) Use ID 1.  
C) Ask the user for their ID or look it up based on their email.  
D) Quit.  

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** "Slot Filling" is the process of asking for missing parameters.

### Question 5 (State)
**In a multi-turn conversation, where is the "Ticket ID" stored while waiting for confirmation?**

A) In the Vector DB.  
B) In the Conversation Memory/Context.  
C) On a piece of paper.  
D) Nowhere.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The history of the chat allows the bot to "remember" what we are talking about.

---

### Summary
Today you built a **Ticket Master**. You learned the critical pattern of "Read -> Confirm -> Write" to safely modify data systems. Tomorrow, we scale up to **Multi-Agent** systems.
