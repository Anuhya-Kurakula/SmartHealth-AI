# 🏥 SmartHealth AI

An AI-powered **Multi-Tool Health Awareness Assistant** built using **Django, React, Groq LLM, RAG Architecture, FAISS, and Agent-Based Tool Routing**.

SmartHealth AI provides reliable health awareness information through multiple healthcare tools, conversational AI, multilingual voice interaction, and intelligent query routing.

---

# 🌐 Live Demo

### Frontend (Vercel)

https://smart-health-ai-lilac.vercel.app

### Backend API (Render)

https://smarthealth-ai-1.onrender.com

### Sample API Test

https://smarthealth-ai-1.onrender.com/api/chat/?question=health%20tips

---

# 🚀 Features

## 🤖 AI-Powered Health Assistant

* Groq LLM Integration
* Conversational Health Support
* Intelligent Query Routing
* Source-Based Responses

---

## 🧠 Agent-Based Tool Routing

SmartHealth AI automatically routes user questions to the appropriate tool.

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

### ✅ Web Search Tool

Supports current and latest information queries.

Example:

```text
Latest health news
Who is WHO Director General?
```

---

# 📚 Retrieval-Augmented Generation (RAG)

Implemented RAG architecture using:

* FAISS Vector Database
* LangChain
* HuggingFace Embeddings
* Sentence Transformers
* Query Rewriting
* Document Reranking
* Source Attribution

### RAG Pipeline

```text
User Question
      ↓
Query Rewriter
      ↓
FAISS Retrieval
      ↓
Reranking
      ↓
Context Generation
      ↓
Groq LLM
      ↓
Final Response
```

> Note: Full RAG pipeline is implemented and tested locally. Current cloud deployment uses Groq fallback mode for stability on free-tier infrastructure.

---

# 🧠 Memory System

### Conversation Memory

Maintains context during conversations.

Example:

```text
User: What is migraine?
User: How is it treated?
```

### Persistent Database Memory

* SQLite Chat Storage
* Previous Conversation Retrieval
* Persistent Chat History

---

# 📊 Dashboard Analytics

Displays:

* Total Chats
* Recent Conversations
* Chat History

---

# 🎤 Voice Features

## Speech-to-Text

Supports browser speech recognition.

## Text-to-Speech

Reads AI responses aloud.

## Multilingual Support

Supported Languages:

* English 🇺🇸
* Telugu 🇮🇳
* Hindi 🇮🇳

---

# 🌙 User Interface Features

* Dark Mode
* Light Mode
* Sample Questions
* Recent Questions
* Chat History
* Voice Interaction

---

# 📈 RAG Evaluation

Implemented RAG evaluation using:

* Faithfulness
* Answer Relevancy

---

# 🛠 Technologies Used

## Frontend

* React.js
* Vite
* JavaScript
* HTML
* CSS

## Backend

* Django
* Django REST Framework
* Django CORS Headers
* WhiteNoise
* Gunicorn

## AI Stack

* Groq API
* Llama 3.3 70B Versatile
* LangChain
* FAISS
* HuggingFace Embeddings
* Sentence Transformers

## Database

* SQLite

## Deployment

* Vercel
* Render

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
SmartHealth-AI/
│
├── backend/
│   │
│   ├── agents/
│   │   ├── agent_executor.py
│   │   ├── tool_router.py
│   │   ├── rag_tool.py
│   │   └── tools/
│   │       ├── bmi_tool.py
│   │       ├── calculator_tool.py
│   │       ├── health_tools.py
│   │       └── web_search_tool.py
│   │
│   ├── chatbot/
│   ├── core/
│   ├── survey/
│   │
│   ├── rag/
│   │   ├── ingestion/
│   │   ├── retrieval/
│   │   ├── reranking/
│   │   ├── rewriting/
│   │   ├── generation/
│   │   ├── memory/
│   │   ├── evaluation/
│   │   └── pipeline.py
│   │
│   ├── vectorstore/
│   │   └── faiss_index/
│   │
│   ├── voice/
│   │
│   ├── requirements.txt
│   └── manage.py
│
├── frontend/
│   │
│   ├── src/
│   │   ├── api/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── README.md
└── .gitignore
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

python manage.py migrate

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

```text
What is dengue?
What are the symptoms of malaria?
How can dengue be prevented?
Give me health tips
Foods rich in iron
Exercises for weight loss
Tell me about Metformin
BMI for 70kg and 170cm
```

---

# 🏗 System Architecture

```text
User
 ↓
React Frontend
 ↓
Django REST API
 ↓
Agent Router
 ↓
Tool Selection
 ↓
Groq LLM / RAG Pipeline
 ↓
SQLite Memory
 ↓
Response
```

---
# 🚀 Deployment

SmartHealth AI is deployed using modern cloud platforms for frontend and backend hosting.

## Frontend Deployment (Vercel)

Frontend is deployed on Vercel.

### Live URL

```text
https://smart-health-ai-lilac.vercel.app
```

### Deployment Steps

```bash
git push origin main
```

Vercel automatically detects changes and redeploys the frontend.

---

## Backend Deployment (Render)

Backend is deployed on Render.

### Live API URL

```text
https://smarthealth-ai-1.onrender.com
```

### API Test Endpoint

```text
https://smarthealth-ai-1.onrender.com/api/chat/?question=health%20tips
```

### Render Configuration

**Root Directory**

```text
backend
```

**Build Command**

```bash
pip install -r requirements.txt && python manage.py migrate
```

**Start Command**

```bash
gunicorn core.wsgi:application
```

---

## Deployment Architecture

```text
React Frontend (Vercel)
            │
            ▼
Django Backend (Render)
            │
            ▼
Agent Router
            │
 ┌──────────┼──────────┐
 │          │          │
 ▼          ▼          ▼
Tools      Groq      SQLite
            │
            ▼
      Health Responses
```

---

## Current Deployment Status

| Component            | Status                              |
| -------------------- | ----------------------------------- |
| Frontend (Vercel)    | ✅ Live                              |
| Backend (Render)     | ✅ Live                              |
| API Integration      | ✅ Working                           |
| Groq LLM             | ✅ Working                           |
| Tool Router          | ✅ Working                           |
| SQLite Database      | ✅ Working                           |
| Voice Features       | ✅ Working                           |
| RAG Architecture     | ✅ Implemented                       |
| Cloud RAG Deployment | ⚠️ Disabled for Free-Tier Stability |

---

## Notes

* The complete RAG pipeline has been implemented and tested locally.
* Current cloud deployment uses Groq fallback mode for stable performance on free-tier infrastructure.
* FAISS indexing, retrieval, reranking, and query rewriting components are included in the codebase.
 
 ----

# 🔮 Future Enhancements

* LangGraph Multi-Agent Architecture
* User Authentication
* Docker Deployment
* Appointment Scheduling
* Health Risk Prediction
* Cloud-Based Full RAG Deployment

---

# ⚠️ Challenges Faced

### 1. RAG Deployment on Cloud

**Challenge:**
Deploying the complete RAG pipeline on Render Free Tier caused issues due to HuggingFace model loading, FAISS initialization, and memory limitations.

**Solution:**
Implemented a Groq-based fallback mechanism for cloud deployment while maintaining the complete RAG architecture locally for testing and evaluation.

---

### 2. Large Dependency Management

**Challenge:**
Libraries such as FAISS, Transformers, Sentence-Transformers, and LangChain increased deployment complexity and build times.

**Solution:**
Separated core application dependencies from experimental RAG components and optimized deployment configuration.

---

### 3. Tool Routing Logic

**Challenge:**
Correctly routing user queries to the appropriate tool (BMI, Medicine, Nutrition, Symptom Checker, etc.) without conflicts.

**Solution:**
Implemented a centralized Agent Router that analyzes user intent and selects the most relevant tool automatically.

---

### 4. Frontend–Backend Integration

**Challenge:**
Connecting the React frontend hosted on Vercel with the Django backend hosted on Render.

**Solution:**
Configured API endpoints, CORS settings, and deployment URLs to enable seamless communication between services.

---

### 5. Voice Feature Compatibility

**Challenge:**
Browser speech recognition behaves differently across browsers and operating systems.

**Solution:**
Used Web Speech API with fallback handling and multilingual language support.

---

### 6. Context Preservation

**Challenge:**
Maintaining conversation context across multiple user interactions.

**Solution:**
Implemented temporary conversation memory and persistent SQLite-based chat history storage.

---

### 7. Deployment Configuration Issues

**Challenge:**
Managing environment variables, requirements files, build commands, and dependency compatibility during deployment.

**Solution:**
Configured Render and Vercel deployment settings, optimized requirements, and validated deployment workflows using GitHub integration.

---

# 📚 Key Learnings

* Retrieval-Augmented Generation (RAG) Architecture
* Vector Databases (FAISS)
* LangChain Framework
* Agent-Based AI Systems
* LLM Integration using Groq
* Django REST API Development
* React Frontend Development
* Cloud Deployment using Render and Vercel
* Full-Stack AI Application Development

----

# 👨‍💻 Developed By

**Anuhya Kurakula**

---

# 📜 License

MIT License
