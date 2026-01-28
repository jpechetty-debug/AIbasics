# Week 3 - Weekly Interactive Assessment

## Practical Prompt Patterns Quiz

**Instructions:**
- 15 questions covering Translator, Summarizer, Extractor, and Generator patterns.
- Aim for 70% or higher to advance.

**Scoring Guide:**
- 13-15: Prompt Master 🧙‍♂️
- 10-12: Pattern Practitioner 👷
- <10: Needs Refactoring 🔧

---

### Question 1 (The Translator Pattern)
**You use AI to rewrite a technical incident report into a calm email for the CEO. What capability of the Translator Pattern are you leveraging?**

A) Code Conversion  
B) Tone and Audience Adaptation  
C) Data Compression  
D) Fact Checking  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Adjusting the "Tone" and "Audience" is the hallmark of the Translator pattern.

---

### Question 2 (The Summarizer Pattern)
**Which instruction typically improves the quality of a Log Summary prompt?**

A) "Read every line."  
B) "Ignore trivial 'Info/Debug' messages and group duplicate errors."  
C) "Translate to French."  
D) "Write a poem."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Filtering noise (Info/Debug) and grouping duplicates prevents the summary from being as long as the original log.

---

### Question 3 (The Extractor Pattern)
**You want to extract IP addresses from a text file. Why might you prefer AI Extraction over Regex?**

A) AI is faster at math.  
B) AI handles unstructured/messy context (e.g., distinguishing "Source IP" vs "Destination IP" based on sentence structure).  
C) Regex cannot match IPs.  
D) AI uses less memory.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Regex matches patterns; AI matches meaning/context.

---

### Question 4 (The Generator Pattern)
**When asking AI to generate a Python script, what is a critical safety step before running it?**

A) Check if it compiles.  
B) Read the code to ensure it doesn't delete files or send data externally (Review & Verify).  
C) Run it as Root/Administrator immediately.  
D) Submit it to the App Store.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Never run unverified AI code, especially with elevated privileges.

---

### Question 5 (Pattern Selection)
**Scenario:** You have a PDF manual and need to find the specific command to enable SSH. You don't want to read the whole book. Which pattern helps?**

A) Generator  
B) Translator  
C) Summarizer (Extractive)  
D) Extractor (Structured)  

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** You are summarizing/finding a needle in a haystack.

---

### Question 6 (Limitations)
**What happens if you ask the Extractor Pattern to pull data that isn't in the source text?**

A) It crashes.  
B) It might "Hallucinate" (invent) the data to satisfy the request.  
C) It always says "Null."  
D) It emails the author.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You must instruct it: "If data is missing, output NULL," otherwise it might make up a plausible value.

---

### Question 7 (Formats)
**Which structured data format is generally best for passing data between AI and Scripts?**

A) JSON  
B) ASCII Art  
C) RTF  
D) MP3  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** JSON is the lingua franca of APIs and automation.

---

### Question 8 (Translator Pattern)
**Can the Translator Pattern convert code from an old language (COBOL/Perl) to a modern one (Python/Go)?**

A) Yes, and it's a great use case for modernization.  
B) No, AI doesn't know old languages.  
C) Only if the code is < 10 lines.  
D) No, it violates copyright.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** AI models are trained on massive codebases, including legacy languages.

---

### Question 9 (Scenario)
**You want to create 100 fake user accounts (Name, Email, Role) to test your Active Directory script. Which pattern is this?**

A) Summarizer  
B) Generator (Mock Data)  
C) Extractor  
D) Translator  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You are generating new synthetic data based on a schema.

---

### Question 10 (Chaining)
**What does "Chaining" mean in the context of these patterns?**

A) Wearing jewelry.  
B) Using the output of one pattern (e.g., Extractor) as the input for another (e.g., Generator).  
C) Running the prompt on a blockchain.  
D) Writing the prompt in C#.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Chaining builds complex workflows from simple, reliable building blocks.

---

### Question 11 (Terminology)
**"Abstractive Summarization" means:**

A) Highlighting exact sentences.  
B) Rewriting the summary in new words/sysnthesis.  
C) Deleting the file.  
D) Making it abstract art.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Abstractive = Rephrasing/Synthesizing. Extractive = Copy-pasting fragments.

---

### Question 12 (Use Case)
**"Take this rough list of bullet points and turn it into a polite, professional client email."**

A) Translator  
B) Generator  
C) Summarizer  
D) Extractor  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** You are translating "Draft/Rough" language into "Professional/Polite" language.

---

### Question 13 (Ethics/Safety)
**When using the Generator pattern to write a security pentest script, what constraint should you include?**

A) "Make it undetectable."  
B) "Ensure it targets only authorized IP ranges (Ethics/Safety)."  
C) "Make it a virus."  
D) "Hide the code."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Responsible AI usage requires setting boundaries to ensure code is used for defensive/authorized purposes only.

---

### Question 14 (Debugging)
**University the Extractor pattern fails to output valid JSON. What is the likely fix?**

A) Ask nicely.  
B) Add a constraint: "Output ONLY raw JSON with no markdown formatting or chatter."  
C) Buy a new computer.  
D) Use XML.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Refining the "Format" constraint usually fixes syntax errors.

---

### Question 15 (Review)
**The "PCTF" framework (Persona, Context, Task, Format) applies to:**

A) Only the Generator Pattern.  
B) Only the Translator Pattern.  
C) All Prompt Engineering Patterns.  
D) None of them.  

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** PCTF is the universal structure for a good prompt, regardless of the specific pattern used.

---

## Assessment Complete!

**13-15:** You are a Pattern Architect.
**10-12:** You know the tools, now practice building.
**<10:** Review the patterns. Try the hands-on exercises again.
