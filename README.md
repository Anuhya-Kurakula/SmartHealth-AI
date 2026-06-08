# 🏥 SmartHealth AI

An AI-powered **Multi-Tool Health Awareness Assistant** built using **Django, React, RAG, FAISS, Groq LLM, and Agent-Based Tool Routing**.

SmartHealth AI provides reliable health awareness information using WHO documents, persistent memory, multiple healthcare tools, multilingual voice interaction, and conversational AI.

---

# 🚀 Features

## 🔍 Retrieval-Augmented Generation (RAG)

* FAISS Vector Database
* WHO health document retrieval
* Context-aware answer generation
* Source attribution

---

## 🧠 Conversation Memory

Maintains context across follow-up questions.

Example:

```text
User: What is migraine?
User: How is it treated?
```

---

## 💾 Persistent Database Memory

* SQLite-based chat storage
* Previous conversation retrieval
* Memory survives server restart

---

# 🤖 Multi-Tool Agent System

SmartHealth AI uses an Agent Router to automatically select the appropriate tool.

### ✅ RAG Tool

Answers health-related questions from WHO documents.

### ✅ BMI Calculator Tool

Example:

```text
BMI for 70kg and 170cm
```

### ✅ Calculator Tool

Example:

```text
25 + 40
```

### ✅ Medicine Information Tool

Examples:

```text
Tell me about Metformin
Uses of Aspirin
Side effects of Amoxicillin
```

### ✅ Symptom Checker Tool

Example:

```text
I have fever and headache
```

### ✅ Health Tips Tool

Example:

```text
Give me health tips
```

### ✅ Disease Prevention Tool

Example:

```text
How can dengue be prevented?
```

### ✅ Nutrition Tool

Example:

```text
Foods rich in iron
```

### ✅ Exercise Recommendation Tool

Example:

```text
Exercises for weight loss
```

### ✅ Water Intake Calculator

Example:

```text
Water intake for 70kg
```

### ✅ Database Memory Tool

Stores and retrieves previous conversations.

---

# ⚙️ Agent Executor + Tool Router

Automatically routes user queries to the correct tool.

---

# 📊 Dashboard Analytics

Displays:

* Total Chats
* Recent Conversations

---

# 🌙 User Interface Features

### Dark Mode Support

* Light Theme
* Dark Theme

### Sample Questions

Quick-access predefined questions.

### Recent Questions

Displays previously asked questions.

---

# 🎤 Voice Features

## Speech-to-Text

Supports browser speech recognition.

## Text-to-Speech

Reads responses aloud.

## Multilingual Support

Supported Languages:

* English 🇺🇸
* Telugu 🇮🇳
* Hindi 🇮🇳

---

# 📄 Chat Export

Supports:

* PDF Export
* TXT Export

---

# 📈 RAG Evaluation

Uses RAGAS metrics:

* Faithfulness
* Answer Relevancy

---

# 🛠 Tech Stack

## Frontend

* React
* Vite
* CSS

## Backend

* Django
* Python

## AI Stack

* Groq API
* Llama 3.3 70B Versatile
* LangChain
* FAISS
* Sentence Transformers
* HuggingFace Embeddings

## Database

* SQLite

---

# 📂 Project Structure

```text
SmartHealth-AI/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── App.jsx
│   └── App.css
│
├── backend/
│   ├── chatbot/
│   ├── core/
│   └── manage.py
│
├── agents/
│   ├── agent_executor.py
│   ├── tool_router.py
│   └── tools/
│
├── rag/
│   ├── generation/
│   ├── memory/
│   ├── rewriting/
│   ├── reranking/
│   ├── evaluation/
│   └── pipeline.py
│
├── vectorstore/
├── documents/
├── screenshots/
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/Anuhya-Kurakula/SmartHealth-AI.git
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### Run Backend

```bash
python manage.py runserver
```

Backend:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🧪 Sample Questions

## Health Questions

```text
What is dengue?
What are the symptoms of malaria?
What is first aid?
How can dengue be prevented?
```

## BMI Tool

```text
BMI for 70kg and 170cm
```

## Medicine Tool

```text
Tell me about Metformin
```

## Exercise Tool

```text
Exercises for weight loss
```

## Nutrition Tool

```text
Foods rich in iron
```

---

# 🏗 Architecture

```text
User
↓
React Frontend
↓
Django Backend
↓
Agent Router
↓
Multiple Tools
↓
Groq + FAISS + SQLite
```

---

# 🔮 Future Enhancements

* LangGraph Multi-Agent Architecture
* User Authentication
* Docker Deployment
* Appointment Scheduling
* Health Risk Prediction

---

# 👨‍💻 Developed By

**Anuhya Kurakula**

---

# 📜 License

MIT License
