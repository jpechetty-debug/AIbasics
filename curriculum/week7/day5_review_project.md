---
difficulty: Advanced
duration: ~90 minutes
tags:
- prompting
- rag
- agents
title: 'Week 7 - Day 5: Review & Mini-Project'
week: 7
---

# Week 7 - Day 5: Review & Mini-Project

## Overview
**Week 7 – Day 5**
**Topic:** Review & Mini-Project: The "Small Business Assistant"
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Review Function Calling, API Integration, and Multi-Agent patterns.
2. Design a comprehensive "Assistant" that integrates Tools and RAG.
3. Complete the Week 7 Assessment.

---

## Lesson Content

### The "Unified" Architecture

Real-world AI apps use all the components:
1.  **Chat UI:** Website widget or messaging app.
2.  **Supervisor:** Decides what to do.
3.  **Knowledge Base (RAG):** For "How-To" questions.
4.  **Tools (API):** For "Action" questions.

**Flow:**
User -> Supervisor -> (Decision) -> RAG Agent OR Tool Agent.

---

## Hands-On Mini-Project

### Project: The "Small Business Assistant" Design

**Objective:** Design the ultimate helper for a small business (a shop, a salon, a repair service — pick one that interests you).

**Capabilities:**
1.  **Q&A:** "What's your return policy?" (Source: FAQ/Policy RAG).
2.  **Status:** "Is my order ready?" (Source: Order Status API).
3.  **Action:** "Reschedule my appointment." (Source: Booking API + Human Confirmation).

**Part 1: The Tools**
- `search_faq(query)`
- `get_order_status(order_id)`
- `reschedule_appointment(appointment_id, new_time)`

**Part 2: The Logic (Supervisor Prompt)**
> "You are the Business Assistant.
> If the user asks a knowledge question, use `search_faq`.
> If the user asks for order/appointment status, use `get_order_status`.
> If the user wants to reschedule, use `reschedule_appointment` BUT ask for confirmation first."

**Part 3: The Simulation**
- **User:** "My order seems delayed."
- **Bot:** "I can check that. What's your order number?"
- **User:** "Order #5521."
- **Bot:** (Tool: `get_order_status`) "Order #5521 is running 2 days behind schedule."
- **User:** "How do I get a refund for late orders?"
- **Bot:** (Tool: `search_faq`) "Our policy says: Orders delayed more than 3 days qualify for a partial refund."

**Assignment:**
Map out this flow for a business idea of your own. Define the tool inputs/outputs.

---

## Weekly Interactive Quiz

### Question 1 (Flow)
**In a Unified Architecture, what usually happens first?**

A) The final action.
B) Intent Classification (Router/Supervisor).
C) Deleting old data.
D) Nothing, it starts randomly.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You must know *what* the user wants before you pick the right tool.

### Question 2 (Tools)
**A "Tool" in AI terms equates to:**

A) A physical hammer.
B) An API endpoint or script that the AI can trigger.
C) A user.
D) Raw data with no function.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Tools extend what the AI can actually do, beyond just talking.

### Question 3 (Safety)
**Why is "Confirmation" critical in an assistant that can reschedule or cancel things?**

A) Because AI can misunderstand which appointment or order is meant, or make a mistake. You don't want accidental cancellations.
B) It isn't important at all.
C) To annoy users on purpose.
D) To slow down the app for no reason.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** The "human check" is the ultimate safety layer before a real-world change happens.

### Question 4 (RAG vs Tools)
**User: "What's the procedure for returning an item?" -> Tool or RAG?**

A) Tool.
B) RAG (Search Docs/FAQ).

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Procedures and policies are knowledge/text, which is exactly what RAG retrieves.

### Question 5 (RAG vs Tools)
**User: "Cancel my order." -> Tool or RAG?**

A) Tool (Action API).
B) RAG.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Cancelling is a real action, which requires a Tool/Function Call, not a knowledge lookup.

---

### End of Week 7
**Congratulations!** You have reached the summit of **Low-Code Integration**.
You can build systems that **Think (AI model)**, **Remember (RAG)**, and **Act (Tools)**.
**Next Week:** The Grand Finale - **Capstone Project & Career**.
