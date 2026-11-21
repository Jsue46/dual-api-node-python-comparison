# Dual API Comparison — Node.js and Python

Academic project developed for the **Systems Seminary 1** course at the Universidad de San Carlos de Guatemala.

This repository contains a comparative implementation of the same REST API built in two different server-side runtimes: **Node.js (Express)** and **Python (Flask)**. The project was developed collaboratively as a group assignment.

---

## Overview

The goal of this practice was to implement equivalent REST endpoints in two separate technology stacks and compare their behavior, performance characteristics, and development experience. Both APIs expose identical routes and are designed to run in parallel.

---

## Endpoints

Both implementations expose the following routes:

| Method | Route    | Description                          |
|--------|----------|--------------------------------------|
| GET    | /check   | Health check — returns `200 OK`      |
| GET    | /info    | Returns instance and course metadata |

---

## Technologies

- **API 1:** Node.js, Express — listening on port 80
- **API 2:** Python, Flask — listening on port 80

---

## Repository Structure

```
dual-api-node-python-comparison/
├── api-node/
│   ├── server.js          # Express server
│   └── package.json
├── api-python/
│   ├── app.py             # Flask server
│   └── requirements.txt
└── README.md
```

---

## Academic Context

| Field       | Detail                                         |
|-------------|------------------------------------------------|
| Course      | Systems Seminary 1 (SEMI1)                     |
| Institution | Universidad de San Carlos de Guatemala         |
| Type        | Group project                                  |
