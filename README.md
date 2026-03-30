# 🤖 AI-Powered Web App/Game Generator (Streamlit + n8n)

## 🚀 Project Overview

This project enables users to generate simple web applications or games using a text prompt. The system leverages **Streamlit, n8n workflows, and Large Language Models (LLMs)** to automatically create executable Python applications.

Users can describe their idea, and the system generates **Streamlit-compatible code**, which can be executed instantly within the interface.

---

## 🎯 Objective

To automate application development by converting user ideas into functional applications using AI, reducing the need for manual coding.

---

## 🛠️ Tech Stack

### Frontend

* **Streamlit** – Interactive UI for input, code generation, and execution

### Backend / Workflow Automation

* **n8n** – Handles workflow automation and API integration

### AI Component

* **LLMs** (OpenAI / Gemini / Mistral / Groq) – Generates application code

---

## ⚙️ Key Features

* ✨ Generate applications using simple text prompts
* 🎮 Generate basic games (e.g., pygame-based)
* ▶️ Run generated applications instantly
* 🔗 Integration with n8n webhook for automation
* 💻 Dynamic Python code generation and execution

---

## 🔄 System Workflow

1. User enters a description (e.g., *“Create a calculator”*)
2. Streamlit sends the request to **n8n webhook**
3. n8n processes the request using an **LLM**
4. LLM generates **Streamlit-compatible Python code**
5. Code is returned to Streamlit
6. Code is stored (e.g., `generated_app.py`)
7. User runs the app within Streamlit

---

## 🧩 n8n Workflow

* **Webhook Trigger** → Receives user prompt
* **LLM Processing Node** → Generates code
* **Response Node** → Sends generated code back

---

## 📥 Input & Output

### Input

User prompt examples:

* "Create a calculator"
* "Build a small game"
* "Make a task manager app"

### Output

* Fully functional **Streamlit application code**
* Executable app within the interface

---

## 📸 Screenshots

(Add screenshots of UI, generated code, and output here)

---

## 🔗 GitHub Repository

(Add your repo link here)

---

## 💡 Future Enhancements

* Add **code validation & error handling**
* Support **multiple programming frameworks**
* Improve UI/UX with templates
* Add **user authentication & history tracking**
* Deploy on **cloud (AWS / Streamlit Cloud)**

---

## 🧠 Key Learnings

* Integration of **AI + automation workflows**
* Real-time **code generation using LLMs**
* Building **end-to-end AI-powered applications**
* Working with **Streamlit deployment**

---

## ⚡ One-Line Summary

> AI-powered system that generates and runs applications from user prompts using Streamlit, n8n, and LLMs.
