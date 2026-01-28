# Week 5 - Day 2: AI for Ansible Playbooks

## Overview
**Week 5 – Day 2**  
**Topic:** Generating Ansible Playbooks with AI  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Generate Ansible YAML structure (Playbooks, Roles) using AI.
2. Use AI to convert Shell commands into Ansible Modules.
3. Validate AI-generated YAML syntax.

---

## Lesson Content

### The YAML Headache

Ansible is powerful, but YAML indentation is painful.
- "Is that 2 spaces or 4?"
- "Do I use a list `-` here?"

**AI is the perfect YAML generator.** It doesn't make indentation errors.

### Use Case 1: Shell to Ansible

**The Problem:** You know the CLI command: `apt-get install nginx`. You want the Ansible module.

**The Prompt:**
> **Task:** Convert this shell command to an Ansible Task: `apt-get install nginx`.
> **Constraint:** Ensure state is 'present' and use `become: yes`.

**The Output:**
```yaml
- name: Install nginx
  apt:
    name: nginx
    state: present
  become: yes
```

### Use Case 2: The Full Playbook

**The Prompt:**
> **Task:** Write an Ansible playbook to configure a Cisco IOS Switch.
> **Steps:**
> 1. Set hostname.
> 2. Create VLAN 10 (Name: Data).
> **Library:** Use `cisco.ios.ios_config` collection.
> **Inventory:** Target `switches` group.

**The Output:**
A complete `site.yml` with the correct `hosts`, `gather_facts`, and `tasks` structure using the modern collection syntax.

### Use Case 3: Jinja2 Templating

Generating Jinja2 templates for config generation is complex.

**The Prompt:**
> **Task:** Create a Jinja2 template (`switch.j2`) for Interface configuration.
> **Variables:** Iterate over a list called `interfaces` with `name` and `desc`.
> **Example Data:** `[{name: Gi1, desc: Uplink}, {name: Gi2, desc: User}]`

**The Output:**
```jinja2
{% for interface in interfaces %}
interface {{ interface.name }}
 description {{ interface.desc }}
 exit
{% endfor %}
```

---

## Hands-On Exercise

### Exercise: The "LAMP Stack" Playbook

**Objective:** Create a playbook to install Apache and PHP.

**Step 1: The Prompt**
> "Write an Ansible Playbook for Ubuntu. Install Apache2 and PHP module. Start the generic Apache service."

**Step 2: The Critic Check**
> A common mistake: Did it update the cache (`update_cache: yes`)?
> **Prompt:** "Check the playbook. Did you update the apt cache before installing?"

**Step 3: Verification**
> **Prompt:** "Explain exactly what `state: present` vs `state: latest` does in this context."

**Reflection:**
Ansible documentation is huge. AI acts as a search engine that writes the config for you.

---

## Interactive Daily Quiz

### Question 1 (Syntax)
**What happens if you mess up indentation in YAML?**

A) It works fine.  
B) The playbook fails (Syntax Error).  
C) It runs faster.  
D) Nothing.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** YAML is whitespace-sensitive. AI helps avoid these errors.

### Question 2 (Conversion)
**You ask AI: "Turn `service httpd restart` into an Ansible task." What module should it use?**

A) `command`  
B) `service` or `systemd`  
C) `file`  
D) `ping`  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** While `command` works, the native `service` module is "Idempotent" (better practice).

### Question 3 (Structure)
**Can AI generate the folder structure for an Ansible Role (tasks/, vars/, templates/)?**

A) Yes, utilize the "Generator" pattern to ask for the structure or a shell script to create it.  
B) No.  
C) Only on Linux.  
D) No, it handles single files only.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** "Write a bash script to `mkdir` the standard Ansible Role structure" is a great prompt.

### Question 4 (Templating)
**What language does Ansible use for templates?**

A) HTML  
B) Jinja2  
C) COBOL  
D) Python  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** AI excels at Jinja2 loops and conditionals.

### Question 5 (Safety)
**The AI suggests using `shell: echo "password" | sudo -S command`. Is this good practice?**

A) Yes.  
B) No. It exposes passwords in logs. Use `become` (sudo) directives instead.  
C) Yes, it's fast.  
D) Maybe.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Always critique AI output for security bad practices.

---

### Summary
Today you conquered YAML. You used AI to generate **Ansible Playbooks** and **Jinja2 Templates**, turning English requirements into Infrastructure-as-Code. Tomorrow, we explore **Regex** and Data Parsing.
