# AI Kubernetes Troubleshooting Agent

A documentation-first, portfolio-ready project for building an on-demand AI troubleshooting system for Kubernetes clusters.

## Project overview

This project explores how to combine:
- Kubernetes cluster inspection
- incident evidence collection
- LLM-based reasoning
- clear diagnosis and remediation guidance

It is designed as an on-demand investigation workflow, not as a Kubernetes controller or operator.

## Why this project matters

Modern DevOps and SRE teams often need fast answers during incidents. This system aims to reduce time to diagnosis by combining cluster telemetry with AI reasoning in a structured workflow.

## Core architecture

Frontend
  -> FastAPI backend (orchestrator)
  -> Kubernetes investigation layer
  -> AI reasoning layer
  -> diagnosis and suggested fix
  -> frontend diagnosis view

## Recommended stack

- Frontend: React or a lightweight web UI
- Backend: FastAPI
- Kubernetes access: Python Kubernetes client
- LLM: Azure OpenAI GPT-4.1
- Storage: optional PostgreSQL or Redis for history and caching
- Deployment: Docker and Kubernetes for later stages

## What the first version will do

- inspect pod health and restarts
- inspect deployments and statefulsets
- review recent Kubernetes events
- collect logs from failing workloads
- generate a structured incident diagnosis
- recommend next steps and fixes

## Repository structure

- [docs/architecture.md](docs/architecture.md) — system design and component responsibilities
- [docs/implementation-plan.md](docs/implementation-plan.md) — phased implementation roadmap
- [docs/api-spec.md](docs/api-spec.md) — backend API contract

## End-to-end flow

1. User clicks Investigate Cluster.
2. The frontend sends a request to the backend.
3. The backend collects cluster evidence.
4. The investigation layer summarizes the incident context.
5. The AI layer produces a diagnosis and remediation plan.
6. The result is shown to the user.

## Safety and design principles

- read-only investigation first
- human approval before any write actions
- RBAC-based cluster access
- secret redaction in logs
- audit-friendly request logging

## Development roadmap

- Phase 1: backend skeleton and health endpoint
- Phase 2: Kubernetes evidence collection
- Phase 3: AI reasoning integration
- Phase 4: frontend diagnosis experience
- Phase 5: production hardening and history tracking

## GitHub showcase note

This repository is structured as a clean, documentation-first portfolio project suitable for showcasing DevOps, Kubernetes, and AI integration skills on GitHub.
## Quick start

1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```
2. Build and run the full stack:
   ```bash
   docker compose up --build
   ```
3. Open the app:
   - Frontend: http://localhost:3000
   - Backend health: http://localhost:8000/health

## Project structure

- backend/ — FastAPI service with health endpoint and placeholder investigation modules
- frontend/ — Next.js app with a minimal homepage
- docs/ — architecture and implementation documentation
- prompts/ — project setup prompt and future task prompts
## Next step

Once you share your GitHub repository link, I can prepare and push this repository content to it directly.
