# Local Context-Aware RAG Chatbot

## Overview

This project implements a fully local, context-aware chatbot using Retrieval-Augmented Generation (RAG).  
The chatbot retrieves relevant information from a vectorized document store and maintains conversational memory across interactions.

The system is built entirely with open-source tools and runs without any paid APIs.

---

## Features

- Context-aware conversational memory
- Retrieval-Augmented Generation (RAG)
- FAISS vector database
- Sentence-transformer embeddings
- Local FLAN-T5 language model
- Fully offline and free
- Modular and extensible architecture

---

## Architecture

User Query  
→ Vector Similarity Search (FAISS)  
→ Context Injection  
→ Local LLM Generation (FLAN-T5)  
→ Conversation Memory Update  
→ Response  

---

## Technologies Used

- Python
- FAISS
- HuggingFace Transformers
- Sentence-Transformers
- LangChain (Core + Community modules)
- PyTorch

---

## How It Works

1. Documents are split into chunks.
2. Each chunk is converted into vector embeddings.
3. FAISS stores and indexes these embeddings.
4. On user query:
   - Relevant chunks are retrieved.
   - Retrieved context is injected into the prompt.
   - The local language model generates an answer.
5. Conversation history is maintained manually for context continuity.

---

## Installation

Install dependencies:

```bash
pip install langchain langchain-community langchain-text-splitters \
faiss-cpu sentence-transformers transformers accelerate torch
