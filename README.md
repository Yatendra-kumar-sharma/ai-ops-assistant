# AI Ops Assistant

AI Ops Assistant is a work-in-progress system for learning how real AI-powered backend systems are built.

It combines:
- Python AI service (FastAPI)
- Java Spring Boot backend
- LLM APIs (OpenAI / local models)
- RAG-based retrieval (planned)
- Basic evaluation system (planned)

The goal is to understand how to design and build production-style AI systems.

---

## Architecture

User → Java Backend → Python AI Service → LLM / RAG → Response → Java → User

- Java backend handles APIs, auth, and orchestration
- Python service handles AI logic (RAG + LLM reasoning)

---

## Current Progress

### Done
- Monorepo structure set up
- Python environment configured (venv)
- Dependencies installed
- Python version defined (3.12.10)

### In progress
- Basic FastAPI service setup

### Next steps
- First `/chat` endpoint
- LLM integration
- RAG pipeline (Chroma)
- Java backend integration
- Evaluation system

---

## Tech Stack

- Python (FastAPI)
- Java (Spring Boot)
- ChromaDB (planned)
- OpenAI / Ollama

---

## Goal

Build a realistic AI system architecture and understand how components like RAG, LLMs, and backend orchestration work together in production systems.