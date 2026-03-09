---

# AI-Based Smart Classroom

An **AI-powered Smart Classroom System** that combines a **RAG-based doubt assistant** with **AI-generated questions from teacher lectures**.

The system helps students resolve doubts using an AI chatbot and also allows teachers to record lectures. The recorded lecture audio is converted into text using **Fast Whisper**, and an **LLM generates questions from the lecture content** for students to answer.

This project is built using **React, FastAPI, Flask, LangChain, FAISS, Gemini, Ollama, and MongoDB**.

---

---
Overview

Traditional classrooms often make it difficult for students to clarify doubts instantly or revise lectures effectively. This project aims to solve that by combining speech recognition, LLMs, and web technologies.

The system allows teachers to record their lectures, automatically convert them into text, and generate questions based on the lecture content. Students can then attempt these questions to reinforce learning.
---

#  Features

### AI Doubt Assistant (RAG)

Students can ask doubts related to course content. The system retrieves relevant information from the knowledge base using **FAISS vector search** and generates answers using **Google Gemini**.

---

### Lecture Audio Processing

Teachers can record lecture audio. The system processes the lecture and extracts meaningful content.

---

### Speech-to-Text

Lecture audio is converted into text using **Fast Whisper**.

---

### AI Question Generation

The lecture transcript is given to an **LLM (via Ollama)** which generates questions based on the lecture.

---

### Student Question Practice

Generated questions are displayed on the student page where students can attempt answers.

---

### Doubt Escalation System

If the chatbot cannot find the answer in the knowledge base, it returns:

```
sorry i couldnot find it i will send it to teacher
```

The question is automatically stored in **MongoDB** for the teacher dashboard.

---

# System Architecture

## Doubt Assistant Pipeline

```
Student Question
       │
       ▼
React Chat Interface
       │
       ▼
Flask RAG Backend
       │
       ▼
FAISS Vector Search
       │
       ▼
Google Gemini LLM
       │
       ├── Answer Found → Return Answer
       │
       └── Answer Not Found
              │
              ▼
MongoDB
              │
              ▼
Teacher Dashboard
```

---

## Lecture Question Generation Pipeline

```
Teacher Lecture Audio
        │
        ▼
Fast Whisper
(Speech → Text)
        │
        ▼
Lecture Transcript
        │
        ▼
Ollama LLM
        │
        ▼
Generated Questions
        │
        ▼
Student Interface
```

---

# 🛠 Tech Stack

## Frontend

* React
* Vite
* Axios
* React Router DOM

---

## Backend (AI APIs)

* Python
* Flask
* FastAPI
* LangChain
* LangChain Community
* LangChain Google GenAI

---

## AI / ML Components

* Google Gemini (`gemini-2.5-flash`)
* Ollama (Local LLM)
* Fast Whisper (Speech Recognition)
* FAISS Vector Database
* HuggingFace Sentence Transformers

---

## Admin Server

* Node.js
* Express.js
* Mongoose

---

## Database

* MongoDB

---

# Project Structure

```
AI-Based-Smart-Class-Room
│
├── Backend
│   │
│   ├── Final_RAG_Backend
│   │   ├── ProjectRag.py        # RAG chatbot implementation
│   │   ├── Rag_Backend.py       # FastAPI backend for lecture question generation
│   │   ├── TextTranscribe.py    # Fast Whisper transcription
│   │   ├── test_case.txt
│   │
│   ├── RAG_Model
│   │
│   ├── Rag_backend
│
├── Frontend
│
└── README.md
```

---

# Backend Setup

Install required Python dependencies:

```bash
pip install flask flask-cors fastapi langchain langchain-community langchain-google-genai faiss-cpu sentence-transformers faster-whisper
```

---

# Add Gemini API Key

Inside the backend code:

```python
apikey = "YOUR_GOOGLE_API_KEY"
```

---

# 🌐 API Endpoints

## RAG Chat API

```
POST /Senddata
```

Request

```json
{
 "datas": "What is React?"
}
```

Response

```json
{
 "result": "React is a JavaScript library for building UI"
}
```

---

## Lecture Question Generation

FastAPI endpoint:

```
POST /generate-questions
```

Workflow:

1️⃣ Teacher uploads lecture audio
2️⃣ Fast Whisper converts audio → text
3️⃣ Transcript sent to Ollama
4️⃣ Questions generated
5️⃣ Questions displayed on student page

---

# Frontend Setup

Install dependencies

```bash
npm install
```

Run the frontend

```bash
npm run dev
```

---

# Teacher Dashboard

Teachers can view unanswered student doubts.

Data is stored in **MongoDB**.

Database:

```
question_Db
```

Collection:

```
questions
```

---

# Auto Escalation Flow

```
Student asks question
        │
        ▼
RAG searches knowledge base
        │
        ├── Answer found → Return AI answer
        │
        └── Answer NOT found
                │
                ▼
Fallback message
                │
                ▼
Save question to MongoDB
                │
                ▼
Teacher Dashboard
```

---

#  Future Improvements

* AI evaluation for student answers
* Lecture summarization
* Authentication system
* Real-time classroom analytics
* Multi-language lecture transcription
* PDF / document knowledge upload

---
