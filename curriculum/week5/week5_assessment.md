# Week 5 - Weekly Interactive Assessment

## AI for Tools & Automation Quiz

**Instructions:**
- 15 questions covering Python, Ansible, Regex, and Documentation.
- Aim for 70% or higher.

**Scoring Guide:**
- 13-15: Automation Archmage 🦾
- 10-12: Scripting Specialist 🛠️
- <10: Review Week 5 📖

---

### Question 1 (Python)
**Which Python library is most commonly used for making HTTP API requests (e.g., to Meraki or Cloud)?**

A) `netmiko`  
B) `requests`  
C) `socket`  
D) `flask`  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The `requests` library is the standard for REST APIs.

---

### Question 2 (Ansible)
**When Asking AI to write an Ansible tasks, why specify `state: present`?**

A) To make sure it happens now.  
B) To ensure "Idempotency" (It only changes if needed).  
C) To delete the file.  
D) To make it faster.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Declarative state is key to Ansible.

---

### Question 3 (Regex)
**You need to match an email address. Is it better to write the regex from scratch or ask AI?**

A) Scratch.  
B) AI, because email regex is notoriously complex and standard patterns exist.  
C) Neither, use `grep`.  
D) Use a string split.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Standard patterns (email, IP, URL) are perfect for AI generation.

---

### Question 4 (Documentation)
**Why are Type Hints (e.g., `def add(x: int, y: int) -> int:`) useful for AI?**

A) They help the AI understand your code's intent when you ask it for help/refactoring later.  
B) They slow down Python.  
C) They are ignored by AI.  
D) They are mandatory in Python 2.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Explicit types give the model (and IDEs) context.

---

### Question 5 (Parsing)
**"TextFSM" is a tool used for:**

A) Sending SMS.  
B) Parsing semi-structured CLI output (like `show ip int brief`) into structured data.  
C) Formatting text.  
D) Writing emails.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It handles the tabular data common in networking.

---

### Question 6 (Workflow)
**What is the "Critic" step in Code Generation?**

A) Telling the AI it is bad.  
B) Asking the AI (or yourself) to review the generated code for bugs/security before running it.  
C) Deleting the code.  
D) Posting it to prod.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Audit before Execution.

---

### Question 7 (Security)
**The AI generates code with `verify=False` in a `requests.get()` call. What does this mean?**

A) It verifies the data.  
B) It disables SSL Certificate verification (Insecure).  
C) It is strictly secure.  
D) It verifies the password.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is a common "Dev" setting that AI often defaults to. You must catch this for Prod.

---

### Question 8 (YAML)
**YAML files use what for structure?**

A) Braces `{}`.  
B) Indentation (Spaces).  
C) Tags `<>`.  
D) Semicolons `;`.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Whitespace matters.

---

### Question 9 (Jinja2)
**What syntax denotes a variable in a Jinja2 template?**

A) `{{ var }}`  
B) `[[ var ]]`  
C) `$var`  
D) `%var%`  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Double curly braces output the variable value.

---

### Question 10 (Netmiko)
**What exception handles a bad username/password in Netmiko?**

A) `NetmikoAuthenticationException`  
B) `ValueError`  
C) `LoginError`  
D) `BadPass`  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** AI knows this specific class name.

---

### Question 11 (Refactoring)
**"Refactoring" code usually means:**

A) Changing what it does.  
B) Cleaning up the internal structure without changing the external behavior (e.g., adding comments, simplifying loops).  
C) Deleting it.  
D) Compiling it.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Improving quality/readability.

---

### Question 12 (Prompting)
**Which prompt is better for a Python script?**

A) "Script for backups."  
B) "Write a Python script using Netmiko ConnectHandler to loop through a list of IPs and save `show run` to a file. Handle SSH exceptions."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** PCTF: Specific constraints yield better code.

---

### Question 13 (Environment)
**Where should API Keys be stored?**

A) Hardcoded in the script (`api_key = "123"`).  
B) In Environment Variables (`os.getenv('API_KEY')`).  
C) In the README.  
D) In a public text file.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Never hardcode secrets.

---

### Question 14 (Generative AI)
**Can AI translate a Python script into an Ansible Playbook?**

A) No.  
B) Yes, this is a "Translation" pattern task.  
C) Only if it is short.  
D) Only if it is simple.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** "Translate the logic of this script into an Ansible Task" is a valid prompt.

---

### Question 15 (Final)
**Does using AI make you less of a programmer?**

A) Yes.  
B) No. It allows you to solve harder problems faster, shifting focus from syntax to architecture.  
C) Yes, if you tell anyone.  
D) Maybe.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It leverages your skills.

---

## Assessment Complete!

**13-15:** You are ready to automate the world.
**10-12:** Effective scripter.
**<10:** Review the syntax lessons.
