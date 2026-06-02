# 📄 PDF RAG Assistant using LlamaIndex, ChromaDB & Ollama

A Retrieval-Augmented Generation (RAG) application that allows users to chat with PDF documents using local Large Language Models (LLMs).

Built using **LlamaIndex**, **ChromaDB**, **HuggingFace Embeddings**, **Ollama**, **Mistral**, and **Streamlit**.

---

## 🚀 Project Overview

Traditional LLMs cannot access your private documents.

This project solves that problem using **Retrieval-Augmented Generation (RAG)**.

The system:

1. Reads PDF documents
2. Extracts text
3. Converts text into vector embeddings
4. Stores embeddings in a vector database
5. Retrieves relevant chunks when a question is asked
6. Uses a Large Language Model (Mistral) to generate answers

This enables users to ask natural language questions about PDF documents.

---

## 🏗️ System Architecture

```text
PDF Document
      │
      ▼
Text Extraction (PyMuPDF)
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
(BAAI/bge-small-en-v1.5)
      │
      ▼
ChromaDB Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Relevant Context
      │
      ▼
Mistral (Ollama)
      │
      ▼
Final Response
```

---

## 🛠️ Tech Stack

| Component           | Technology             |
| ------------------- | ---------------------- |
| Framework           | LlamaIndex             |
| LLM                 | Mistral (Ollama)       |
| Vector Database     | ChromaDB               |
| Embeddings          | BAAI/bge-small-en-v1.5 |
| PDF Parsing         | PyMuPDF                |
| Frontend            | Streamlit              |
| Environment Manager | UV                     |
| Language            | Python                 |

---

## 📂 Project Structure

```text
1st_RAG/
│
├── data/
│   └── Place your PDFs here
│
├── src/
│   ├── config.py
│   ├── ingest.py
│   └── query.py
│
├── vector_store/
│
├── app.py
│
├── README.md
├── pyproject.toml
└── uv.lock
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git

cd REPOSITORY_NAME
```

---

## 2️⃣ Create Virtual Environment

Using UV:

```bash
uv venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
uv sync
```

Or manually:

```bash
uv add llama-index
uv add chromadb
uv add llama-index-vector-stores-chroma
uv add sentence-transformers
uv add llama-index-embeddings-huggingface
uv add streamlit
uv add pymupdf
uv add ollama
uv add llama-index-llms-ollama
```

---

# 🤖 Install Ollama

Download and install:

https://ollama.com

Verify:

```bash
ollama --version
```

---

## Download Mistral

```bash
ollama pull mistral
```

Test:

```bash
ollama run mistral
```

Example:

```text
>>> What is Machine Learning?
```

---

# 📄 Add Your PDF

Place your PDF inside:

```text
data/
```

Example:

```text
data/
│
└── research_paper.pdf
```

---

# 🧠 Create Vector Database

Run:

```bash
cd src

python ingest.py
```

What happens:

* PDF is loaded
* Text is extracted
* Embeddings are generated
* ChromaDB stores vectors

Expected output:

```text
Loading PDFs...

Reading: research_paper.pdf

Creating embeddings...

Vector Database Created Successfully
```

---

# 💬 Terminal Chat Mode

Run:

```bash
cd src

python query.py
```

Example:

```text
Ask Question:
```

Questions:

```text
Summarize this document

What are the main findings?

Who is the author?
```

---

# 🌐 Streamlit Dashboard

Run:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

Features:

* Chat Interface
* PDF Question Answering
* Conversational Experience
* Local LLM Inference

---

# 🔎 Example Queries

```text
Summarize the document

What is the document about?

List important topics

Explain chapter 3

What are the key findings?

Give me a concise overview
```

---

# 📈 Future Improvements

* Multi-PDF Support
* Source Citations
* PDF Upload from UI
* Chat History
* Conversation Memory
* Hybrid Search
* Reranking
* Groq Integration
* Research Assistant Mode

---

# 🎯 Learning Outcomes

This project demonstrates understanding of:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Embedding Models
* Similarity Search
* Local LLM Deployment
* PDF Processing
* Streamlit Applications
* LlamaIndex Framework

---

# 👨‍💻 Author

Harjot Singh

B.Tech Artificial Intelligence & Machine Learning

Thapar Institute of Engineering & Technology

GitHub: https://github.com/Harjotsingh0311

LinkedIn: https://linkedin.com/in/harjot-singh-0311h

---

## ⭐ If you found this project useful, consider giving it a star.
