---
difficulty: Advanced
duration: 30-60 min
tags:
- prompting
- rag
- agents
- assessment
title: Week 7 - Weekly Interactive Assessment
week: 7
---

# Week 7 - Weekly Interactive Assessment

## Advanced Integration Quiz

**Instructions:**
- 15 questions covering Function Calling, API Integration, and Multi-Agent Systems.
- Aim for 70% or higher.

**Scoring Guide:**
- 13-15: Integration Architect 🌐
- 10-12: Tool Builder 🛠️
- <10: Review Week 7 🔌

---

### Question 1 (Function Calling)
**"Function Calling" allows an AI model to:**

A) Execute code directly on its own hardware.
B) Output specific JSON arguments to trigger an external function/API.
C) Make phone calls.
D) Write poetry.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It requests the action; the application executes it.

---

### Question 2 (APIs)
**Which HTTP verb is "Safe" (read-only, no changes)?**

A) POST.
B) GET.
C) DELETE.
D) PATCH.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** GET should never change data.

---

### Question 3 (APIs)
**To send data to an API (like creating a support ticket), you typically use:**

A) Headers only.
B) The Body (Payload), usually in JSON format.
C) A verification code.
D) FTP.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** `{"description": "Broken item received"}` goes in the Body.

---

### Question 4 (Multi-Agent)
**The "Supervisor" pattern involves:**

A) One agent doing everything itself.
B) A top-level agent routing tasks to specialized sub-agents (Workers).
C) Randomly generating new agents.
D) Ignoring the user's request.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Centralized orchestration and routing.

---

### Question 5 (Tools)
**In a tool definition, the "Description" is vital because:**

A) The AI uses it to decide **when** to use the tool.
B) It is used for documentation only, and nothing else.
C) It is required by law.
D) It sets how fast the tool runs.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** A clear description guides the AI's intent matching.

---

### Question 6 (Workflow)
**What is the correct order for a "Write" operation?**

A) Write -> Read.
B) Read (Check current state) -> Confirm (Ask User) -> Write (Execute).
C) Write -> Hope for the best.
D) Confirm -> Read.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Look before you leap.

---

### Question 7 (Integration)
**An API Key is typically passed in the:**

A) URL's visible text.
B) HTTP Header (e.g., `Authorization`).
C) The filename.
D) The page title.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Headers are the standard, secure way to transport tokens.

---

### Question 8 (Security)
**Why restrict which tools an AI can use?**

A) To limit its power and prevent accidental damage (principle of least privilege).
B) To save money in every case.
C) Because AI is inherently untrustworthy.
D) There's no real reason.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Never give a "delete everything" tool to a chatbot without very good reason and safeguards.

---

### Question 9 (State)
**A "Transactional Bot" implies:**

A) It always costs money to use.
B) It performs state-changing actions (transactions) like updating a record.
C) It only translates languages.
D) It only reads data, never changes anything.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Transaction = Action that changes something.

---

### Question 10 (Design)
**If you have 50 different tools, what is the best architecture?**

A) Put them all in one giant prompt.
B) Use a Multi-Agent system to group tools by category to keep each agent's context clean.
C) Delete most of them.
D) Assign tools randomly.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Categories/groups help the AI select the right toolset for each situation.

---

### Question 11 (Debugging)
**The API returns `500 Internal Server Error`. Whose fault is it likely to be?**

A) The Client (your bot/app).
B) The Server (the API provider).
C) The end user.
D) Your home Wi-Fi.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** 500 typically indicates a server-side issue. (400 would usually be a client/request error.)

---

### Question 12 (JSON)
**`{"id": 1, "name": "Order"}` is an example of:**

A) XML.
B) HTML.
C) JSON.
D) SQL.

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** Key-value pairs are the hallmark of JSON.

---

### Question 13 (Low-Code)
**In a visual flow builder, a "Tool Agent" node typically requires:**

A) An AI Model and a List of Tools.
B) A specific user account.
C) A printer connection.
D) A physical database server.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** The AI model is the "Brain" that drives the Tools.

---

### Question 14 (Strategy)
**When should you use RAG vs. Function Calling?**

A) RAG for Information. Function Calling for Action.
B) RAG for Action, always.
C) Both do the exact same thing.
D) Neither is ever needed.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Retrieval (knowing things) vs. Execution (doing things).

---

### Question 15 (Final)
**This course has taken you from "Prompting" to "Building Agents." The key differentiator of an Agent is:**

A) Raw intelligence.
B) Agency (the ability to perceive, decide, and act on the environment using tools).
C) How much it costs.
D) How fast it responds.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Agents DO things, not just talk about them.

---

## Assessment Complete!

**13-15:** You are an Integration Master.
**10-12:** Solid Builder.
**<10:** Review the API lessons.
