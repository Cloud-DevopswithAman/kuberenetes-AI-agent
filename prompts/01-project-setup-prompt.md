# 01-prompt-project-setup

## Context
We are building an AI Kubernetes Troubleshooting Agent.

Architecture:

Frontend
  -> FastAPI Backend (Orchestrator)
  -> Kubernetes Investigation Layer
  -> AI Kubernetes Agent
  -> LLM Reasoning
  -> Root Cause + Suggested Fix
  -> Frontend Diagnosis

This is an on-demand troubleshooting system.

## Goal
Set up the project foundation.

Create:
- FastAPI backend
- Next.js frontend
- Docker setup
- Environment variables
- Basic folder structure
- Health endpoint

Do not implement Kubernetes logic or AI yet.

## Tech Stack
Backend:
- FastAPI
- Python 3.12+
- Uvicorn
- Pydantic
- Loguru
- HTTPX

Frontend:
- Next.js
- TypeScript
- Tailwind CSS
- Axios
- React Query

Infrastructure:
- Docker
- Docker Compose

## Project Structure
Create a monorepo:

ai-kubernetes-agent/

├── backend/
├── frontend/
├── docs/
├── prompts/
├── docker-compose.yml
└── README.md

## Expected Result
I should be able to run:

```bash
docker compose up --build
```

Access:
- http://localhost:3000
- http://localhost:8000/health
