# Task API - DevOps Pipeline

A containerized Flask REST API with pytest, Docker, and GitHub Actions CI/CD.

## Architecture
Developer -> GitHub (develop) -> GitHub Actions (Flake8 + Pytest) -> Docker Hub -> Docker Compose

## Endpoints
- GET /health
- GET /tasks
- POST /tasks
- PUT /tasks/<id>
- DELETE /tasks/<id>

## Run
docker compose up -d
