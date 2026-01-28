# Week 3 - Day 3: The Extractor Pattern

## Overview
**Week 3 – Day 3**  
**Topic:** The Extractor Pattern - Unstructured to Structured Data  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define the "Extractor Pattern"
2. Use AI to parse human text (emails/tickets) into JSON/CSV
3. Extract IP addresses, CVEs, or MAC addresses from messy text
4. Build a prompt that acts as a "Regex Replacement"

---

## Lesson Content

### The Structure Problem

Automation scripts (Python/Ansible) love **Structured Data** (JSON, YAML, CSV).
The World provides **Unstructured Data** (Emails, PDFs, CLI Output).

Traditionally, you write complex **Regular Expressions (Regex)** to bridge this gap.
*Example:* `\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b` (Matches an IP).
This is brittle. If the format changes slightly, the Regex breaks.

**The Extractor Pattern** uses AI to read the messy text and output clean, structured data.

### Use Case 1: The "Ticket parser"

**Input (Email):**
> "Hi, please open port 443 and 80 for the server at 192.168.1.50. Also allow 22 from the jumper."

**The Prompt:**
> **Task:** Extract the firewall rules requested in the text.
> **Format:** JSON.
> **Schema:** `[{ "port": int, "ip": string, "action": "allow" }]`
> **Input:** [Email]

**The Output:**
```json
[
  { "port": 443, "ip": "192.168.1.50", "action": "allow" },
  { "port": 80,  "ip": "192.168.1.50", "action": "allow" },
  { "port": 22,  "ip": "jumper",       "action": "allow" }
]
```
The AI even inferred "jumper" was the source, handling the ambiguity better than Regex.

### Use Case 2: The "ClI Scraper"

**Input (show cdp neighbors):**
> Device ID: Switch-B
> IP address: 10.1.1.2
> Platform: cisco WS-C2960
> ...

**The Prompt:**
> **Task:** Extract the neighbor details into a CSV format.
> **Columns:** Hostname, IP, Model.
> **Input:** [CLI Output]

**The Output:**
`Switch-B, 10.1.1.2, WS-C2960`

### Use Case 3: The "Vuln Scanner"

**Input (Security Bulletin):**
> "A critical vulnerability (CVE-2023-1234) affects IOS XE versions 16.1 to 17.3."

**The Prompt:**
> **Task:** Extract the CVE ID and the affected version range.
> **Format:** JSON.

---

## Hands-On Exercise

### Exercise: The "Inventory Builder"

**Objective:** Turn a messy email chain into an inventory spreadsheet.

**Scenario:** Your boss emails you:
*"We have a Dell R740 in the NY office (Asset #991), two HP DL380s in London (Assets #882, #883), and a random Mac Mini in the lobby."*

**Step 1: Write the Prompt**
- **System:** You are a Data Extraction Assistant.
- **Task:** Extract the server inventory.
- **Format:** Pipe-separated table: `| Location | Model | Asset Tag |`
- **Rule:** If Asset Tag is missing, write "MISSING".

**Step 2: Predicted Output**
```text
| Location | Model      | Asset Tag |
|----------|------------|-----------|
| NY       | Dell R740  | #991      |
| London   | HP DL380   | #882      |
| London   | HP DL380   | #883      |
| Lobby    | Mac Mini   | MISSING   |
```

**Reflection:**
Writing a script to parse that natural language sentence would take hours. The AI did it in seconds.

---

## Interactive Daily Quiz

### Question 1 (Analogy)
**If Regular Expressions (Regex) are a "Scalpel," what is the AI Extractor Pattern?**

A) A Hammer  
B) A reading comprehension engine that understands the context  
C) A random number generator  
D) A spell checker  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Regex looks for character patterns. AI looks for *meaning* (e.g., understanding that "Jumper" implies a source host).

### Question 2 (Formats)
**Which format is best to request if you plan to feed the AI output directly into a Python script?**

A) A poem  
B) JSON (JavaScript Object Notation)  
C) A long paragraph  
D) Spoken Word  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** JSON is the standard for data exchange. `json.loads()` makes it instant to use.

### Question 3 (Capabilities)
**Can the Extractor Pattern handle messy/inconsistent formatting (e.g., some phone numbers have dashes, some don't)?**

A) No, it needs perfect inputs.  
B) Yes, AI is robust to formatting inconsistencies.  
C) Only if you use Regex first.  
D) Only on Sundays.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** This is the superpower of AI extraction—normalization of messy inputs.

### Question 4 (Constraint)
**You ask the AI to extract data vs. summary. What is the key difference?**

A) Extraction gets specific data points (structured). Summary gets the general idea (unstructured).  
B) Extraction is slower.  
C) Summary is for computers.  
D) There is no difference.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Extraction = Database rows. Summary = Executive Briefing.

### Question 5 (Reliability)
**True or False: LLMs can sometimes "Hallucinate" data during extraction (e.g., inventing an Asset Tag that wasn't there).**

A) True  
B) False  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Always check the output. Use prompt instructions like "If the data is missing, write 'NULL', do not invent data" to mitigate this.

---

### Summary
Today you merged the world of Human Text with Computer Data. The **Extractor Pattern** allows you to turn emails, tickets, and CLI dumps into JSON/CSV grids. Tomorrow, we explore the **Generator Pattern**—using AI to write the scripts and configs you've been extracting data for.
