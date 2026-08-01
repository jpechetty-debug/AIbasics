---
difficulty: Intermediate
duration: 30-60 min
tags:
- prompting
- python
- agents
- assessment
title: Week 4 - Weekly Interactive Assessment
week: 4
---

# Week 4 - Weekly Interactive Assessment

## Advanced Prompting Quiz

**Instructions:**
- 15 questions covering Few-Shot, CoT, Critic, and Chaining.
- Aim for 70% or higher.

**Scoring Guide:**
- 13-15: Prompt Engineer Level 2 🧙‍♂️
- 10-12: Advanced Practitioner 🎓
- <10: Review Week 4 📚

---

### Question 1 (Few-Shot)
**What is the "One-Shot" prompting technique?**

A) You only get one chance to ask.
B) Providing exactly one example of the desired output format in the prompt.
C) Asking the AI a one-word question.
D) Writing a one-line prompt.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** "Shot" refers to the number of examples provided.

---

### Question 2 (Chain of Thought)
**Which problem type benefits MOST from Chain of Thought prompting?**

A) Creative writing (e.g., poems).
B) Math, logic, and multi-step troubleshooting.
C) Basic facts (e.g., "Capital of France").
D) Simple translations.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** CoT helps break down complex reasoning, which is needed for math and logic problems.

---

### Question 3 (Critic)
**When using the Critic Pattern, who provides the critique?**

A) You (The User), typing it manually.
B) The AI, acting in a specific persona (e.g., skeptical reviewer).
C) A third party service.
D) The computer hardware.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You ask the AI to critique itself (or a previous output).

---

### Question 4 (Chaining)
**You want to summarize a long personal journal and then translate the summary. Why might you use a Chain?**

A) Context Window limits might prevent pasting the entire journal at once.
B) To ensure the summary is accurate *before* translating it (Quality Control).
C) Both A and B.
D) Neither.

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** Chaining solves both length limits and quality control issues.

---

### Question 5 (Zero-Shot)
**"Write a short poem about the ocean." This is an example of:**

A) Few-Shot Prompting.
B) Zero-Shot Prompting.
C) Chain of Thought.
D) Critic.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** No examples or reasoning steps were requested.

---

### Question 6 (Application)
**Your AI output is inconsistent (sometimes a list, sometimes a paragraph). What is the best fix?**

A) Chain of Thought.
B) Few-Shot Prompting (Show 2-3 examples of the exact format you want).
C) Ask nicely and hope.
D) Try again later.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Few-Shot is the strongest pattern for enforcing format consistency.

---

### Question 7 (Reasoning)
**Why does stating "Let's think step by step" work?**

A) It's magic.
B) It conditions the model to generate reasoning text, which grounds its final answer in logic rather than just a probable-sounding guess.
C) It connects to a calculator app.
D) It unlocks a hidden feature.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It changes the way the model builds its answer, favoring logical steps over quick guesses.

---

### Question 8 (Critic)
**True or False: The Critic Pattern is useful for finding red flags in something like an online listing or contract.**

A) True.
B) False.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Asking AI to "act as a skeptical reviewer" is a great preliminary check before you commit to something.

---

### Question 9 (Chaining)
**In a prompt chain, the data passed between steps is often called the:**

A) Handshake.
B) Context / State.
C) Chain link.
D) Token.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** You are maintaining the context or state of the task across multiple prompts.

---

### Question 10 (Agents)
**An "Agent" can be described as:**

A) A loop of Prompt Chains that can perceive and act, with some autonomy in deciding what to do next.
B) A spy.
C) A database.
D) A single prompt.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Agents add a loop/decision capability to standard chains.

---

### Question 11 (Debugging)
**The AI generates a "fact" or detail that sounds confident but turns out to be made up. What is this called?**

A) Creativity.
B) Hallucination.
C) Optimization.
D) A bug fix.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Hallucination is confident but factually wrong generation.

---

### Question 12 (Correction)
**How can CoT help reduce Hallucinations?**

A) It doesn't.
B) By forcing the AI to derive the answer from stated facts/logic rather than just guessing the final word.
C) It deletes them automatically.
D) It highlights them in red.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It slows down the "guessing" process in favor of explicit reasoning.

---

### Question 13 (Persona)
**When chaining, why assign unique Personas to each step?**

A) To keep it fun.
B) To access specific tones and vocabulary suited to each step (e.g., "organizer" vocabulary vs. "writer" vocabulary).
C) It is strictly required by the software.
D) To use less memory.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** "Act as a friendly editor" produces different results than "Act as a strict fact-checker."

---

### Question 14 (Iterative Refinement)
**"Critique my prompt and rewrite it to be better." This is an example of:**

A) Meta-Prompting.
B) Zero-Shot.
C) A mistake.
D) Cheating.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Using the AI to improve how you use the AI.

---

### Question 15 (Final Review)
**Which combination is structured as "Show, Reason, Check"?**

A) Few-Shot -> CoT -> Critic.
B) Zero-Shot -> Critic.
C) Generator -> Extractor.
D) None of the above.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** This is the "Golden Trio" of high-reliability prompting: Give Examples (Few-Shot), Ask for Reasoning (CoT), Review the Result (Critic).

---

## Assessment Complete!

**13-15:** You are an AI Whisperer.
**10-12:** Solid skills.
**<10:** Review the materials.
