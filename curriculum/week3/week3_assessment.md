---
difficulty: Intermediate
duration: 30-60 min
tags:
- prompting
- python
- rag
- automation
- assessment
title: Week 3 - Weekly Interactive Assessment
week: 3
---

# Week 3 - Weekly Interactive Assessment

## Practical Prompt Patterns Quiz

**Instructions:**
- 15 questions covering Translator, Summarizer, Extractor, and Generator patterns.
- Aim for 70% or higher to advance.

**Scoring Guide:**
- 13-15: Prompt Master 🧙‍♂️
- 10-12: Pattern Practitioner 👷
- <10: Needs Practice 🔧

---

### Question 1 (The Translator Pattern)
**You use AI to rewrite a dense medical report into a calm explanation for a worried family member. What capability of the Translator Pattern are you leveraging?**

A) Code Conversion
B) Tone and Audience Adaptation
C) Data Compression
D) Fact Checking

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Adjusting the "Tone" and "Audience" is the hallmark of the Translator pattern.

---

### Question 2 (The Summarizer Pattern)
**Which instruction typically improves the quality of a long email thread summary?**

A) "Read every line."
B) "Ignore small talk and group repeated topics together."
C) "Translate to French."
D) "Write a poem."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Filtering noise (small talk) and grouping duplicates prevents the summary from being as long as the original thread.

---

### Question 3 (The Extractor Pattern)
**You want to pull item names and prices from a receipt. Why might you prefer AI extraction over manually copying each line?**

A) AI is faster at math.
B) AI handles unstructured/messy formatting (e.g., inconsistent spacing or abbreviations) based on context.
C) Manual copying cannot capture prices.
D) AI uses less memory.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI matches meaning and context, not just exact character patterns, so it handles messy real-world formatting well.

---

### Question 4 (The Generator Pattern)
**When asking AI to generate a first draft of something important (like a cover letter), what is a critical step before using it?**

A) Send it immediately with no changes.
B) Read it carefully to check for accuracy and personalize it to your actual situation (Review & Verify).
C) Ask it to sign your name.
D) Submit it to a contest immediately.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Always review and personalize AI-generated drafts before using them for something important.

---

### Question 5 (Pattern Selection)
**Scenario: You have a 60-page instruction manual and need to find the specific steps to reset a device. You don't want to read the whole book. Which pattern helps?**

A) Generator
B) Translator
C) Summarizer (Extractive)
D) Extractor (Structured data)

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** You are summarizing/finding a specific needle in a haystack of pages.

---

### Question 6 (Limitations)
**What happens if you ask the Extractor Pattern to pull data that isn't actually in the source text?**

A) It crashes.
B) It might "Hallucinate" (invent) the data to satisfy the request.
C) It always says "Null."
D) It emails the author.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You must instruct it: "If data is missing, output N/A," otherwise it might make up a plausible-sounding value.

---

### Question 7 (Formats)
**Which structured data format is generally best for passing data between AI and a spreadsheet or app?**

A) JSON or a clean table
B) ASCII Art
C) An audio file
D) A video

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** JSON or a well-formatted table is the standard for moving structured data between tools.

---

### Question 8 (Translator Pattern)
**Can the Translator Pattern convert an old-fashioned, wordy letter into a modern, concise style?**

A) Yes, and it's a great use case for rewriting.
B) No, AI doesn't understand older writing styles.
C) Only if the letter is very short.
D) No, it violates copyright.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** AI models are trained on huge amounts of writing across eras and styles.

---

### Question 9 (Scenario)
**You want to create 20 realistic fake grocery-spending entries to test a budgeting spreadsheet. Which pattern is this?**

A) Summarizer
B) Generator (Practice Data)
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
C) Running the prompt overnight.
D) Writing the prompt in a different app.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Chaining builds complex workflows from simple, reliable building blocks.

---

### Question 11 (Terminology)
**"Abstractive Summarization" means:**

A) Highlighting exact sentences.
B) Rewriting the summary in new words/synthesis.
C) Deleting the file.
D) Making it abstract art.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Abstractive = Rephrasing/Synthesizing. Extractive = Copy-pasting exact fragments.

---

### Question 12 (Use Case)
**"Take this rough list of bullet points and turn it into a polite, professional email to a landlord."**

A) Translator
B) Generator
C) Summarizer
D) Extractor

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** You are translating "rough/casual" language into "professional/polite" language.

---

### Question 13 (Ethics/Safety)
**When using the Generator pattern to write something on someone else's behalf (like a reference letter), what constraint should you include?**

A) "Make it sound like someone else entirely."
B) "Keep it honest and only include things I can verify are true."
C) "Exaggerate everything."
D) "Hide who wrote it."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Responsible AI usage means setting boundaries to ensure generated content stays honest and appropriate.

---

### Question 14 (Debugging)
**The Extractor pattern keeps failing to output valid, clean data (extra chatter mixed in). What is the likely fix?**

A) Ask nicely.
B) Add a constraint: "Output ONLY the structured data with no extra commentary or formatting."
C) Buy a new computer.
D) Switch to a different pattern entirely.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Tightening the "Format" constraint usually fixes messy or inconsistent output.

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
