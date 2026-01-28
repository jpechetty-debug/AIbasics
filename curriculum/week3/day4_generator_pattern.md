# Week 3 - Day 4: The Generator Pattern

## Overview
**Week 3 – Day 4**  
**Topic:** The Generator Pattern - Creating Code and Configs  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Define the "Generator Pattern"
2. Use AI to write complex Regex, SQL, and Python
3. Generate sample data for testing (Mock Logs)
4. Use "Persona" to generate documentation

---

## Lesson Content

### The Blank Page Problem

Starting from scratch is hard.
- "How do I start a Python script?"
- "What is the syntax for an Ansible Playbook?"
- "I need 100 fake users to test this database."

**The Generator Pattern** uses AI to create new content based on your constraints.

### Use Case 1: The "Code Drafter"

**The Prompt:**
> **Task:** Generate a Python script to scan a subnet for IP addresses.
> **Library:** Use `scapy`.
> **Feature:** Multithreading for speed.
> **Output:** Code block with comments.

**The Result:** A working prototype. It might not be perfect, but it saves you the first 30 minutes of "boilerplate setup."

### Use Case 2: The "Regex Writer"

**The Prompt:**
> **Task:** Generate a Regex pattern to match a standard MAC address (Cisco format `aaaa.bbbb.cccc` OR Windows format `AA-BB-CC...`).
> **Explanation:** Explain how the regex works.

**The Result:** `^([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}$`... (plus explanation).
*Note:* Always verify regex with a test case!

### Use Case 3: The "Data Fabricator" (Mock Data)

You built a log analyzer, but you don't have enough logs to test it.

**The Prompt:**
> **Task:** Generate 50 lines of fake Apache Web Server logs.
> **Scenario:** 80% success (200 OK), 15% missing (404), 5% server error (500).
> **Format:** Standard Common Log Format (CLF).

**The Result:** Instant test data.

### Use Case 4: The "Ansible Architect"

**The Prompt:**
> **Task:** Generate an Ansible Playbook to update all Ubuntu servers.
> **Steps:** 1. Update Apt cache. 2. Upgrade packages. 3. Check if reboot required. 4. Reboot if needed.
> **Idempotency:** Ensure the reboot only happens if the file `/var/run/reboot-required` exists.

---

## Hands-On Exercise

### Exercise: The "Config Generator"

**Objective:** Create a full Cisco Switch configuration for a new branch office.

**Scenario:** You have a standard branch template.
- VLAN 10: Data
- VLAN 20: Voice
- Uplink: Gigabit0/1 (Trunk)
- Access Ports: Gigabit0/2-24

**Step 1: Write the Prompt**
- **Persona:** Senior Network Engineer.
- **Task:** Generate a standard Cisco IOS config snippet.
- **Variables:**
  - Hostname: `Branch-NY`
  - VLAN 10 `10.1.10.1/24`
  - VLAN 20 `10.1.20.1/24`
- **Security:** Enable `service password-encryption`.

**Step 2: Analyze Output**
Did it handle the Trunk correctly? Did it assign the IP addresses to SVIs (Interface Vlan)?

**Reflection:**
This enables "Infrastructure as Code" workflows, where you define the intent (Variables), and the AI generates the syntax.

---

## Interactive Daily Quiz

### Question 1 (Usage)
**When asking AI to write code, what is the best mindset?**

A) "The AI is perfect, I will run this in production immediately."  
B) "The AI is a Junior Developer. It writes a good first draft, but I must review, test, and debug it."  
C) "AI cannot write code."  
D) "I don't need to know how to code anymore."  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Always Treat AI code as "Untrusted." Review it. Test it.

### Question 2 (Testing)
**Why is the Generator Pattern useful for "Mock Data"?**

A) It fills hard drives.  
B) It allows you to stress-test your scripts/tools without risking real sensitive production data.  
C) It creates real users.  
D) It is illegal.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Generating fake "PII" or logs allows safe development.

### Question 3 (Specificity)
**You ask: "Write a backup script." The AI writes it in Perl. You wanted PowerShell. What failed?**

A) The AI is old fashioned.  
B) You failed to specify the **Language Constraint** in your prompt.  
C) Perl is better.  
D) The internet is broken.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The Generator Pattern requires strict constraints to be useful.

### Question 4 (Regex)
**Why is asking AI to write Regex better than writing it yourself?**

A) Regex is a "Write Only" language (hard to read/write for humans). AI excels at pattern logic.  
B) AI types faster.  
C) Regex is obsolete.  
D) It isn't better.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Most humans struggle with Regex syntax. Describes the *logic* to the AI ("Match an email address ending in .com") is much easier.

### Question 5 (Infrastructure)
**Can AI generate Ansible YAML or Terraform HCL?**

A) No, only Python.  
B) Yes, it is excellent at configuration languages.  
C) Only JSON.  
D) Yes, but only for Azure.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** It has read millions of GitHub repos and knows syntax for Ansible, Terraform, Puppet, etc.

---

### Summary
Today you became a Creator. You used the **Generator Pattern** to draft scripts, regex, configs, and test data. You learned that while AI is a fast writer, *you* must remain the Editor-in-Chief. Tomorrow, we review the patterns and build your personal "AI Toolbox."
