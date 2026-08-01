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

Almost every modern online service has a REST API:
- **A weather service:** `GET /forecast`
- **A store's order system:** `GET /orders/{id}`
- **A messaging app:** `POST /send-message`

Your Low-Code Bot connects to these using an **HTTP Request** block.

### Anatomy of a Request

1.  **Method:**
    - `GET` (Read data).
    - `POST` (Create/Change data).
2.  **URL:** The address (e.g., `https://api.weatherservice.com/v1/...`).
3.  **Headers:** Authentication (`Authorization: Bearer <Key>`).
4.  **Body (JSON):** The data to send (for POST).

### The Integration Flow

1.  **User:** "What's the status of order #12345?"
2.  **AI:** Extracts `12345`.
3.  **Tool:** Calls the store's API: `GET /orders?number=12345`.
4.  **API Response:** `{"status": "shipped", "eta": "2 days"}`.
5.  **AI:** Reads JSON.
6.  **Bot:** "Order #12345 has shipped and should arrive in about 2 days."

### Dynamic Inputs

In a Low-Code tool, you map the **Extracted Variables** to the **API Params**.
- User Input -> Variable `$order_id` -> API URL `.../orders/$order_id`.

---

## Hands-On Exercise

### Exercise: The "IP Geolocation" Bot

**Objective:** Build a simple tool that looks up roughly where an IP address is located — a fun, free way to practice API integration.

**Service:** `ip-api.com` (Free, no authentication needed).
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
**What standard protocol allows different software systems to talk to each other online?**

A) HTML.
B) REST API (HTTP).
C) USB.
D) Bluetooth.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** REST APIs are the common language of integration between apps and services.

### Question 2 (Methods)
**Which HTTP method should you use to CANCEL an order via API?**

A) GET.
B) POST (or PATCH).
C) SLEEP.
D) CONNECT.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** GET is for safely reading data. POST/PATCH implies an action or change.

### Question 3 (Security)
**What is a "Bearer Token"?**

A) A coin.
B) A security credential string sent in the Header to prove you're allowed to access the API.
C) A physical bear.
D) A username.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** `Authorization: Bearer xyz123`.

### Question 4 (JSON)
**Why is JSON important for APIs?**

A) It is the standard format for sending/receiving structured data.
B) It is faster than binary.
C) It is older than XML.
D) It looks colorful.

**Correct Answer:** A

**Feedback:**
- **A) ✓ Correct!** Bots and apps can easily read and generate JSON.

### Question 5 (Debugging)
**You get a "403 Forbidden" error. What does it mean?**

A) The server is down.
B) You are not authenticated or don't have permission for that request.
C) The page doesn't exist.
D) The request succeeded.

**Correct Answer:** B

**Feedback:**
- **B) ✓ Correct!** Check your API Key or Token first.

---

### Summary
Today you plugged your bot into the wider world. You learned to make calls to external APIs. Tomorrow, we build a bot that can Read AND Write.
