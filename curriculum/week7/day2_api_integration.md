---
difficulty: Advanced
duration: ~60 minutes
tags: []
title: 'Week 7 - Day 2: Connecting Bots to APIs'
week: 7
---

# Week 7 - Day 2: Connecting Bots to APIs

## Overview
**Week 7 – Day 2**  
**Topic:** HTTP Requests & API Integration (GET/POST)  
**Duration:** ~60 minutes

### Learning Objectives
By the end of this lesson, you will be able to:
1. Configure an **HTTP Request Node** in a low-code tool.
2. Authenticate with APIs (Bearer Tokens, API Keys).
3. Process API responses so the Bot can read them.

---

## Lesson Content

### The Universal Connector: HTTP

Almost every modern tool has a REST API:
- **Meraki:** `GET /organizations`
- **ServiceNow:** `GET /incidents`
- **Slack:** `POST /chat.postMessage`

Your Low-Code Bot connects to these using an **HTTP Request** block.

### Anatomy of a Request

1.  **Method:**
    - `GET` (Read data).
    - `POST` (Create/Change data).
2.  **URL:** The address (e.g., `https://api.meraki.com/v1/...`).
3.  **Headers:** Authentication (`Authorization: Bearer <Key>`).
4.  **Body (JSON):** The data to send (for POST).

### The Integration Flow

1.  **User:** "Who owns the ticket INC12345?"
2.  **LLM:** Extracts `INC12345`.
3.  **Tool:** Calls ServiceNow API: `GET /table/incident?number=INC12345`.
4.  **API Response:** `{"assigned_to": "Alice", "status": "WIP"}`.
5.  **LLM:** Reads JSON.
6.  **Bot:** "Ticket INC12345 is currently assigned to Alice."

### Dynamic Inputs

In a Low-Code tool, you map the **LLM Variables** to the **API Params**.
- User Input -> Variable `$ticket_id` -> API URL `.../tickets/$ticket_id`.

---

## Hands-On Exercise

### Exercise: The "IP Geolocation" Bot

**Objective:** Build a simple tool that looks up an IP address.

**Service:** `ip-api.com` (Free, no auth).
**Endpoint:** `http://ip-api.com/json/{IP_ADDRESS}`.

**Step 1: The Input**
User: "Where is 8.8.8.8?"

**Step 2: The API Call**
Method: `GET`
URL: `http://ip-api.com/json/8.8.8.8`

**Step 3: The Output**
JSON: `{"country": "United States", "regionName": "Virginia"}`

**Step 4: The Bot Response**
"The IP 8.8.8.8 is located in Virginia, United States."

**Reflection:**
You successfully connected the Chat interface to the Outside World.

---

## Interactive Daily Quiz

### Question 1 (Protocol)
**What standard protocol allows different software systems to talk to each other?**

A) HTML.  
B) REST API (HTTP).  
C) USB.  
D) Bluetooth.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** REST APIs are the language of integration.

### Question 2 (Methods)
**Which HTTP method should you use to REBOOT a server via API?**

A) GET.  
B) POST (or PUT).  
C) SLEEP.  
D) CONNECT.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** GET is for safe reading. POST implies an action/change.

### Question 3 (Security)
**What is a "Bearer Token"?**

A) A coin.  
B) A security credential string sent in the Header to prove you are allowed to access the API.  
C) A bear.  
D) A username.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** `Authorization: Bearer xyz123`.

### Question 4 (JSON)
**Why is JSON important for APIs?**

A) It is the standard format for sending/receiving structured data.  
B) It is faster than binary.  
C) It is older than XML.  
D) It is colorful.  

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Bots read JSON easily.

### Question 5 (Debugging)
**You get a "403 Forbidden" error. What does it mean?**

A) Server down.  
B) You are not authenticated or don't have permission.  
C) Page not found.  
D) Success.  

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Check your API Key/Token.

---

### Summary
Today you plugged your Bot into the **Matrix**. You learned to make calls to external APIs. Tomorrow, we build a transactional bot that can Read AND Write.