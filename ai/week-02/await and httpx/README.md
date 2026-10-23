# Async HTTP Requests Using Python

## 📌 Overview

This project demonstrates how to fetch multiple users from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) concurrently using Python's `asyncio` and `httpx` libraries.

Instead of waiting for each API request to finish before starting the next one, the program sends multiple requests concurrently, making network operations more efficient.

## 🎯 Features

- Fetch user details using an HTTP GET request.
- Use `async` and `await` for asynchronous programming.
- Use `httpx.AsyncClient` to make asynchronous HTTP requests.
- Use `asyncio.gather()` to execute multiple requests concurrently.
- Handle HTTP errors using `response.raise_for_status()`.
- Display user ID, name, and email.
- Print the total number of users fetched.

## 🛠️ Technologies Used

- Python 3.12+
- `asyncio` — manages asynchronous tasks.
- `httpx` — performs asynchronous HTTP requests.
- JSONPlaceholder API — provides sample user data.

## 📂 Project Structure

```text
async-http-requests/
├── async_httpx.py
└── README.md
```

## ⚙️ Installation

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install HTTPX

```bash
pip install httpx
```

Note: `asyncio` is included in Python's standard library, so it does not need to be installed separately.

## ▶️ How to Run

Run the following command in your terminal:

```bash
python async_httpx.py
```

## 📤 Sample Output

```text
User ID: 1
Name: Leanne Graham
Email: Sincere@april.biz
User ID: 2
Name: Ervin Howell
Email: Shanna@melissa.tv
User ID: 3