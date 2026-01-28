# Week 5 - Day 4: AI for Documentation

## Overview
**Week 5 – Day 4**  
**Topic:** Automated Documentation (Docstrings, READMEs, Comments)  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Use AI to auto-generate Python Docstrings.
2. Generate comprehensive README.md files for your scripts.
3. Use AI to comment legacy code for better understanding.

---

## Lesson Content

### The "Bus Factor"

If you are the only one who knows how the script works, and you get hit by a bus, the network is in trouble.
**Documentation lowers the Bus Factor.**
Developers hate writing it. AI loves writing it.

### Use Case 1: Docstrings

**Scenario:** You wrote a function but left it bare.

**The Code:**
```python
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0
```

**The Prompt:**
> "Add Google-Style Python Docstrings to this function. Explain the arguments and return values."

**The Output:**
```python
def check_port(host, port):
    """Checks if a TCP port is open on a remote host.

    Args:
        host (str): IP address or hostname.
        port (int): TCP port number.

    Returns:
        bool: True if port is open, False otherwise.
    """
    ...
```

### Use Case 2: The README

**Scenario:** You have a repository with `backup.py`, `inventory.csv`, and `requirements.txt`.

**The Prompt:**
> "Write a README.md for this project.
> - Title: Network Backup Tool.
> - Features: Backs up Cisco IOS config via SSH.
> - Usage: `python backup.py`.
> - Requirements: listed in `requirements.txt`.
> - Add a Warning about storing passwords."

**The Output:** A professional Markdown file with badges, installation steps (`pip install -r requirements.txt`), and usage examples.

### Use Case 3: Explaining "Magic" Code

**Scenario:** You inherited a script with a complex list comprehension.
`data = [x for x in raw if x['status'] == 'up' and x['speed'] > 1000]`

**The Prompt:**
> "Add a comment above this line explaining exactly what it filters."

**The Output:**
`# Filter list to keep only interfaces that are UP and have speed > 1Gbps`

---

## Hands-On Exercise

### Exercise: The "Self-Documenting" Script

**Objective:** Take a rough script and polish it.

**Step 1: Write a rough script**
(Or ask AI to generate one). simple loop printing numbers.

**Step 2: The "Polisher" Prompt**
> "Refactor this script.
> 1. Add Type Hinting (e.g., `def func(x: int) -> str:`).
> 2. Add Docstrings.
> 3. Add inline comments for logic."

**Step 3: Compare**
Compare the "Raw" script vs the "Polished" script. Which one would you rather maintain 6 months from now?

**Reflection:**
Docstrings and Type Hints make your IDE (VS Code) smarter. AI makes adding them zero-effort.

---

## Interactive Daily Quiz

### Question 1 (Definition)
**What is a "Docstring"?**

A) A string used to tie documents together.  
B) A special comment string used to document a specific code segment (function, class).  
C) A variable type.  
D) A virus.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** In Python, it's the triple-quoted string right after a definition.

### Question 2 (Type Hints)
**Why add Type Hints (e.g., `host: str`)?**

A) It makes the code faster.  
B) It helps developers (and IDEs/AI) understand what kind of data is expected, preventing bugs.  
C) It is required by law.  
D) It makes the file smaller.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It enables static analysis.

### Question 3 (README)
**What is the first file a user looks at in your project?**

A) `main.py`  
B) `config.json`  
C) `README.md`  
D) `license.txt`  

**Correct Answer:** C

**Feedback:**
- **C) ✓ Correct!** A good README is the "Landing Page" of your tool.

### Question 4 (Maintenance)
**You change the code logic but forget to update the comments. This is called:**

A) Code Drift / Comment Rot.  
B) Agile.  
C) Innovation.  
D) Security.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Misleading comments are worse than no comments. Use AI to "Update the comments to match the new code."

### Question 5 (Process)
**Can AI write your Change Management ticket descriptions?**

A) No.  
B) Yes. "Summarize these 3 script changes into a Change Request description focusing on risk and rollback."  
C) Only for Azure.  
D) Never.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The Translator Pattern applies here: Code -> English Description.

---

### Summary
Today you cleaned up. You learned to use AI to generate **Docstrings**, **Type Hints**, and **READMEs**. This transforms "Hobby Code" into "Professional Tooling." Tomorrow, we verify your skills with the **Automation Agent**.
