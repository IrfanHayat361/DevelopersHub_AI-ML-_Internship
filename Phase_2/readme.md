# AI & Machine Learning Projects Portfolio

This repository contains three end-to-end machine learning and AI systems demonstrating practical implementation of NLP, predictive modeling, and Retrieval-Augmented Generation (RAG).

All projects are built with production-oriented structure and focus on performance, modularity, and real-world deployment readiness.

---

#  BERT-Based News Classification System

## Overview

An end-to-end text classification system built using a fine-tuned BERT model on the AG News dataset. The model classifies news articles into predefined categories with high accuracy.

## Key Features

- Fine-tuned BERT model
- Transformer-based NLP pipeline
- CPU training optimization (8GB RAM constraint)
- HuggingFace Transformers integration
- Model serialization and deployment-ready structure
- Gradio / Streamlit deployment interface

## Technologies Used

- Python
- HuggingFace Transformers
- PyTorch
- Scikit-learn
- Pandas / NumPy
- Gradio / Streamlit

## Skills Demonstrated

- Transfer learning with transformers
- Tokenization and attention mechanisms
- Model fine-tuning under hardware constraints
- Performance optimization
- Deployment of NLP systems

---

#  Telco Customer Churn Prediction Pipeline

## Overview

A complete machine learning pipeline to predict customer churn using structured telecom data. The project demonstrates feature preprocessing, model selection, hyperparameter tuning, and exportable pipeline design.

## Key Features

- Scikit-learn Pipeline + ColumnTransformer
- Automated preprocessing
- Hyperparameter tuning with GridSearchCV
- Model evaluation and metrics comparison
- Exportable model using joblib
- Clean, production-ready notebook structure

## Technologies Used

- Python
- Scikit-learn
- Pandas / NumPy
- Matplotlib / Seaborn
- Joblib

## Skills Demonstrated

- End-to-end ML pipeline construction
- Feature engineering
- Model validation
- Cross-validation and hyperparameter tuning
- Production model serialization

---

#  Local Context-Aware RAG Chatbot

## Overview

A fully local Retrieval-Augmented Generation (RAG) chatbot that retrieves relevant information from a vectorized knowledge base and maintains conversational memory across interactions.

This system runs entirely on open-source tools without any paid APIs.

## Architecture

User Query  
→ FAISS Vector Search  
→ Context Retrieval  
→ Prompt Injection  
→ Local FLAN-T5 Generation  
→ Conversation Memory Update  

## Key Features

- Document chunking
- Sentence-transformer embeddings
- FAISS vector database
- Manual conversational memory handling
- Local HuggingFace LLM (FLAN-T5)
- Fully offline and free

## Technologies Used

- Python
- FAISS
- HuggingFace Transformers
- Sentence-Transformers
- LangChain (Core + Community modules)
- PyTorch

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector similarity search
- Embedding generation
- Context injection strategies
- Prompt engineering
- Local LLM inference

---


