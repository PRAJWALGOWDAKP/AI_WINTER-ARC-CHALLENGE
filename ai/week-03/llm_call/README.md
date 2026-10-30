# First LLM API – Google Gemini

## 📌 Project Overview

This project demonstrates how to interact with Google's Gemini Large Language Model (LLM) directly using the official Python SDK (`google-genai`).

It covers making a basic API call, accepting user input, and implementing streaming responses to receive generated text incrementally.

## 🚀 Features

- Connect to Google Gemini using the official Python SDK.
- Generate responses using user prompts.
- Implement normal (non-streaming) API calls.
- Implement streaming API calls.
- Securely manage API keys using environment variables.

## 🛠️ Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv
- uv

## 📂 Project Structure

```text
first-llm-api/
│
├── main.py          # Normal Gemini API call
├── streaming.py     # Streaming Gemini API call
├── .env             # API key configuration
├── .gitignore
└── pyproject.toml
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd first-llm-api
```

### 2. Install dependencies

```bash
uv add google-genai python-dotenv
```

### 3. Configure API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 4. Run the application

**Normal API call:**

```bash
uv run main.py
```

**Streaming API call:**

```bash
uv run streaming.py
```

## 💡 Key Concepts Learned

| Concept | Description |
|---|---|
| API Client | Establishes a connection with Gemini. |
| `generate_content()` | Generates a complete response. |
| `generate_content_stream()` | Generates responses incrementally. |
| `response.text` | Extracts the complete generated response. |
| `chunk.text` | Extracts individual streaming chunks. |
| Environment Variables | Securely stores API credentials. |

## 🔄 Normal Response vs Streaming

**Normal API Call:**
- Sends a prompt to Gemini.
- Waits for the complete response.
- Returns the generated text.

**Streaming API Call:**
- Sends a prompt to Gemini.
- Receives generated text in chunks.
- Displays the output progressively.

## 🎯 Learning Outcome

Through this project, I learned how to:

- Make direct LLM API calls using Python.
- Integrate Google Gemini into Python applications.
- Handle normal and streaming responses.
- Manage API keys securely using environment variables.
- Understand the fundamentals of LLM application development.

## 🔮 Future Improvements

- Add conversation history.
- Build an interactive terminal chatbot.
- Implement error handling.
- Compare response latency between normal and streaming calls.

---

**Author:** Prajwal K P

**Project:** First LLM API – Gemini Python SDK