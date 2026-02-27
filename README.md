# 🚀 YouTube AI Research Assistant (Telegram Bot)

A production-ready Telegram bot that summarizes YouTube videos and answers contextual questions using a Semantic RAG architecture powered by Ollama.

---

## 📌 Project Overview

This bot acts as a personal AI research assistant for YouTube videos.

Users can:
- Send a YouTube link
- Receive a structured summary
- Ask contextual follow-up questions
- Switch response language (English / Hindi)

The system uses semantic retrieval (embeddings-based RAG) to ensure answers are grounded strictly in transcript content.

---

## 🏗 Architecture Overview

### 🔁 System Flow

Telegram → Controller Layer → Transcript Layer → Chunking → Embedding Retrieval → LLM (Ollama) → Response

---

### 🧠 Core Components

#### 1️⃣ Telegram Controller Layer (`main.py`)
- Handles user messages
- Manages sessions per user
- Supports `/start` and `/language` commands

#### 2️⃣ Transcript Layer (`transcript.py`)
- Extracts video ID
- Fetches transcript using `youtube-transcript-api`
- Preserves timestamps

#### 3️⃣ Chunking Layer (`rag_engine.py`)
- Splits transcript into manageable chunks
- Preserves timestamp context

#### 4️⃣ Semantic Retrieval Layer (`embedding_engine.py`)
- Generates embeddings using `nomic-embed-text`
- Computes cosine similarity
- Retrieves top relevant chunks
- Reduces hallucination risk

#### 5️⃣ LLM Layer (`llm.py`)
- Uses Ollama (llama3 model)
- Context-limited prompting
- Strict language enforcement

---

## ✨ Features

- ✅ Structured summary:
  - 🎥 Title  
  - 📌 5 Key Points  
  - ⏱ Important Timestamps  
  - 🧠 Core Insight  

- ✅ Contextual Q&A grounded in transcript
- ✅ Semantic RAG (embedding-based retrieval)
- ✅ Multi-language support (English + Hindi)
- ✅ Multi-user session management
- ✅ Local inference (no API cost)

---

## ⚙ Setup Instructions
![Image Alt](https://github.com/HarshaPachcha/youtube-ai-research-assistant/blob/1439164da024027438b30bfe3b07b5669c231784/Screen%20Shots/Screenshot%202026-02-27%20112431.png)
![Image Alt](https://github.com/HarshaPachcha/youtube-ai-research-assistant/blob/e0f50af65c9198a26c163b417a7f359bfe5081ed/Screen%20Shots/Screenshot%202026-02-27%20112450.png)
![Image Alt](https://github.com/HarshaPachcha/youtube-ai-research-assistant/blob/e0f50af65c9198a26c163b417a7f359bfe5081ed/Screen%20Shots/Screenshot%202026-02-27%20112509.png)
![Image Alt](https://github.com/HarshaPachcha/youtube-ai-research-assistant/blob/e0f50af65c9198a26c163b417a7f359bfe5081ed/Screen%20Shots/Screenshot%202026-02-27%20112538.png)
![Image Alt](https://github.com/HarshaPachcha/youtube-ai-research-assistant/blob/e0f50af65c9198a26c163b417a7f359bfe5081ed/Screen%20Shots/Screenshot%202026-02-27%20112601.png)
![Image Alt](https://github.com/HarshaPachcha/youtube-ai-research-assistant/blob/09c31485b4ec0cbd6050054eeb6aca9a5c51b168/Screen%20Shots/Screenshot%202026-02-27%20115059.png)
### 1️⃣ Clone Repository

```bash
git clone https://github.com/HarshaPachcha/youtube-ai-research-assistant.git
cd youtube-ai-research-assistant

![Image Alt](https://github.com/HarshaPachcha/youtube-ai-research-assistant/blob/1439164da024027438b30bfe3b07b5669c231784/Screen%20Shots/Screenshot%202026-02-27%20112431.png)
