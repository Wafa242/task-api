Write-Host "=== Deploying Task-API ===" -ForegroundColor Cyan; docker pull wafabousnina24/task-api:latest; docker compose down; docker compose up -d; docker compose ps
