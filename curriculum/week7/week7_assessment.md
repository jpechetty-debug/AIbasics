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
**"Function Calling" allows an LLM to:**

A) Execute code directly on its own CPU.  
B) Output specific JSON arguments to trigger an external function/API.  
C) Make phone calls.  
D) Write poetry.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It requests the action; the app executes it.

---

### Question 2 (APIs)
**Which HTTP verb is "Safe" (Idempotent/Read-Only)?**

A) POST.  
B) GET.  
C) DELETE.  
D) PATCH.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** GET should never change data.

---

### Question 3 (APIs)
**To send data to an API (like creating a ticket), you use:**

A) Headers only.  
B) The Body (Payload), usually in JSON format.  
C) Verification.  
D) FTP.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** `{"description": "Broken printer"}` goes in the Body.

---

### Question 4 (Multi-Agent)
**The "Supervisor" pattern involves:**

A) One agent doing everything.  
B) A top-level agent routing tasks to specialized sub-agents (Workers).  
C) Generating random agents.  
D) Ignoring the user.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Centralized Orchestration.

---

### Question 5 (Tools)
**In a tool definition, the "Description" is vital because:**

A) The LLM uses it to decide **when** to use the tool.  
B) It is used for documentation only.  
C) It is required by law.  
D) It sets the speed.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Semantic description guides the intent matching.

---

### Question 6 (Workflow)
**What is the correct order for a "Write" operation?**

A) Write -> Read.  
B) Read (Check current state) -> Confirm (Ask User) -> Write (Execute).  
C) Write -> Hope.  
D) Confirm -> Read.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Look before you leap.

---

### Question 7 (Integration)
**An API Key is typically passed in the:**

A) URL.  
B) HTTP Header (e.g., `Authorization`).  
C) Body.  
D) Filename.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Headers are the standard secure transport for tokens.

---

### Question 8 (Security)
**Why restrict which tools an AI can use?**

A) To limit its power and prevent accidental damage (Least Privilege).  
B) To save money.  
C) AI is evil.  
D) No reason.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Never give `drop_table` to a chatbot.

---

### Question 9 (State)
**A "Transactional Bot" implies:**

A) It costs money.  
B) It performs state-changing actions (Transactions) like updating a database.  
C) It translates languages.  
D) It only reads.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Transaction = Action.

---

### Question 10 (Design)
**If you have 50 tools, what is the best architecture?**

A) Put them all in one prompt.  
B) Use a Multi-Agent system to group tools by category (Network Tools, HR Tools) to keep the context window clean.  
C) Delete them.  
D) Use random tools.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Categories/Groups help the LLM select the right toolset.

---

### Question 11 (Debugging)
**The API returns `500 Internal Server Error`. Who's fault is it?**

A) The Client (Bot).  
B) The Server (API Provider).  
C) The User.  
D) The Network.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** 500 = Server side issue. (400 would be user/bot error).

---

### Question 12 (JSON)
**`{"id": 1, "name": "Server"}` is an example of:**

A) XML.  
B) HTML.  
C) JSON.  
D) SQL.  

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** Key-Value pairs.

---

### Question 13 (Low-Code)
**In Flowise/LangFlow, the "Tool Agent" node requires:**

A) A Language Model and a List of Tools.  
B) A User.  
C) A Printer.  
D) A Database.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** The LLM is the "Brain" that drives the Tools.

---

### Question 14 (Strategy)
**When should you use RAG vs Function Calling?**

A) RAG for Information. Function Calling for Action.  
B) RAG for Action.  
C) Both for everything.  
D) Neither.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Retrieval vs Execution.

---

### Question 15 (Final)
**This course has taken you from "Prompting" to "Building Agents." The key differentiator of an Agent is:**

A) Intelligence.  
B) Agency (The ability to perceive, decide, and act on the environment using tools).  
C) Cost.  
D) Speed.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Agents DO things.

---

## Assessment Complete!

**13-15:** You are an Integration Master.
**10-12:** Solid Builder.
**<10:** Review the API lessons.
