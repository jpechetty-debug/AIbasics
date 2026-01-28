# Week 8 - Day 4: Integration & Testing (The Demo)

## Overview
**Week 8 – Day 4**  
**Topic:** Final Integration and "The Demo"  
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Integrate the Supervisor, RAG, and Tools into one flow.
2. Run a full "End-to-End" test scenario.
3. Record a "Walkthrough" of your Assistant.

---

## Lesson Content

### The "Happy Path" Test

**Scenario:**
1.  **User:** "I'm setting up a new switch for the Voice team. What VLAN should I use?"
    - **Step:** Supervisor -> RAG -> SOP.md.
    - **Bot:** "Per the SOP, Voice devices should use VLAN 20."
2.  **User:** "Great. Also, `critical-server` seems slow."
    - **Step:** Supervisor -> Tool -> `check_status`.
    - **Bot:** "I checked `critical-server`. It is reporting Critical CPU (99%)."
3.  **User:** "Reboot it."
    - **Step:** Supervisor -> Permission Check.
    - **Bot:** "Are you sure you want to reboot `critical-server`?"
4.  **User:** "Yes."
    - **Step:** Supervisor -> Tool -> `reboot_device`.
    - **Bot:** "Success: Device has been rebooted."

### Debugging the "Sad Path"

**Scenario:**
1.  **User:** "Reboot the coffee maker."
2.  **Expected:** Supervisor refuses ("Out of Scope").
    - *If it tries to reboot 'coffee-maker', your Prompt is too loose.*
3.  **User:** "Check status of `unknown-server`."
    - **Expected:** Tool returns "Not Found." Bot says "I can't find that server."

---

## Hands-On Exercise

### Exercise: The Demo Video

**Objective:** Prove it works.

**Task:**
Run through the "Happy Path" scenario above. Screen record it (or take screenshots).
This is your **Portfolio Piece**.

**Checklist:**
- [ ] RAG citation works?
- [ ] Tool execution works?
- [ ] Confirmation step appears?
- [ ] Tone is professional ("NetOps")?

**Reflection:**
You have built a system that behaves like a Senior Engineer: It looks up standards, checks facts, and safeguards critical actions.

---

## Interactive Daily Quiz

### Question 1 (Testing)
**What is "End-to-End" (E2E) testing?**

A) Testing only the Python script.  
B) Testing the entire flow from User Prompt -> Decision -> Tool/RAG -> Response.  
C) Testing the internet connection.  
D) Testing the User.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It verifies all components work together.

### Question 2 (Edge Cases)
**Why test the "Sad Path" (failures)?**

A) To make sure the bot fails gracefully (e.g., "I don't know") rather than hallucinating or crashing.  
B) To break the bot.  
C) It is fun.  
D) To waste time.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Robustness is defined by how well you handle failure.

### Question 3 (Demo)
**What is the value of a recorded demo?**

A) You can put it on LinkedIn/Resume to prove you have "Applied AI" skills.  
B) It uses disk space.  
C) It's required by law.  
D) None.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** "I built a chatbot" is common. "Here is a video of my RAG agent diagnosing a server" is rare.

### Question 4 (Latency)
**If the bot takes 10 seconds to answer, what is usually the bottleneck?**

A) The Tool/API call or the Retrieval step.  
B) The LLM typing speed.  
C) The User.  
D) The Monitor.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** External calls add latency. "Thinking..." indicators help user patience.

### Question 5 (Completion)
**You have finished the technical build. What is left?**

A) Career Strategy.  
B) Nothing.  
C) Sleep.  
D) Retirement.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Technical skills need a career narrative.

---

### Summary
Today you validated your creation. The **NetOps Assistant** is alive. Tomorrow, we discuss how to use this project to upgrade your career.
