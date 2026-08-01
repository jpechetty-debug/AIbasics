---
difficulty: Advanced
duration: ~90 minutes
tags:
- prompting
- python
title: 'Week 8 - Day 3: Building the Action Layer'
week: 8
---

# Week 8 - Day 3: Building the Action Layer

## Overview
**Week 8 – Day 3**
**Topic:** Coding the Mock Tools (Python/API)
**Duration:** ~90 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Write Python scripts that simulate business actions.
2. Wrap these scripts in a "Tool Definition" (JSON).
3. Connect them to the Assistant.

---

## Lesson Content

### The Mock Tool Strategy

We don't want to actually charge a real customer's card or cancel a real order. We want to **simulate** it.

### Tool 1: `check_order_status(order_id)`

**Python Logic:**
```python
def check_order_status(order_id):
    if order_id == "1001":
        return "SHIPPED: Arriving in 2 days"
    else:
        return "PROCESSING: Not yet shipped"
```
**JSON Definition:**
- Description: "Checks the shipping status of an order."
- Param: `order_id`.

### Tool 2: `cancel_order(order_id)`

**Python Logic:**
```python
def cancel_order(order_id):
    return f"SUCCESS: Order {order_id} has been cancelled and refunded."
```
**JSON Definition:**
- Description: "Cancels an order and issues a refund. WARNING: Cannot be undone."
- Param: `order_id`.

### Tool 3: `check_appointment(customer_name)`

**Python Logic:**
- Return a standard "Appointment found: [date/time]" string based on a small mock lookup table.

---

## Hands-On Exercise

### Exercise: The "Mock API"

**Objective:** Create these functions in a single Python file (`tools.py`) or within your Low-Code environment's "Custom Tool" block.

**Workflow:**
1.  **Define:** Write the Python code.
2.  **Describe:** Write the JSON schema.
3.  **Test:** Ask the bot: "Check status of order 1001."

**Success Criteria:**
- The bot replies: "Order 1001 has shipped and is arriving in 2 days."
- It did *not* make this up. It ran your code.

**Reflection:**
You have created a "Digital Twin" of a small business system. This allows you to demo the bot's capabilities safely, without touching any real customer data.

---

## Interactive Daily Quiz

### Question 1 (Simulation)
**Why do `if/else` statements make good mock tools?**

A) They allow you to deterministically test how the bot handles "Good" vs "Bad" scenarios.
B) They are fast to write.
C) They are simple to understand.
D) All of the above.

**Correct Answer:** D

**Feedback:**
- **D) ✓ Correct!** You can force the bot to deal with an "order not found" case by testing an ID that isn't in your mock data.

### Question 2 (Safety)
**What should the `cancel_order` tool description include?**

A) "Use this for fun."
B) "WARNING: Use only after confirmation, cannot be undone."
C) "Nothing in particular."
D) "This is magic."

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The description prompts the Supervisor to require confirmation before executing.

### Question 3 (Input)
**The bot calls `check_order_status` with `order_id="Order #1001"`. The code expects just `"1001"`. What failed?**

A) The Tool Logic (Robustness).
B) The AI model itself.
C) The User.
D) The Network connection.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Your tool code should sanitize inputs (e.g., strip out "Order #" and extra spaces). Don't expect the AI's formatting to be perfect every time.

### Question 4 (Feedback)
**The tool returns a JSON string `{ "status": "shipped", "days_left": 2 }`. What does the AI do with it?**

A) It displays the raw JSON to the user.
B) It reads it, interprets it, and says "Your order has shipped and will arrive in 2 days."
C) It crashes.
D) It ignores it completely.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** The AI translates the Tool's structured data back into natural, friendly language.

### Question 5 (Limits)
**Can you have a tool that calls another tool?**

A) Yes (Chaining).
B) No, never.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** A `diagnose_and_fix` style tool could call `check_order_status` and then `cancel_order` if needed, in sequence.

---

### Summary
Today you gave the bot Hands. It can now "Check" and "Act" on your simulated business data. Tomorrow, we turn it on.
