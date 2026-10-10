# Personal RAG Application

A personal Retrieval-Augmented Generation (RAG) application that builds an intelligent knowledge base from professional information such as a CV, certifications, GitHub projects, LinkedIn profile, and portfolio website.

The system retrieves relevant information from the stored knowledge base and uses an LLM to generate grounded answers about the person's professional background.

---

## Project Overview

This project was developed as a RAG application that can answer questions about Sara Allan's professional experience, projects, skills, education, and certifications.

The system follows a simple RAG pipeline:

```text
Professional Documents
        ↓
Document Loading
        ↓
Text Chunking
        ↓
HuggingFace Embeddings
        ↓
FAISS Vector Database
        ↓
Similarity Search
        ↓
Relevant Context
        ↓
PromptTemplate
        ↓
OpenRouter LLM
        ↓
Generated Answer
