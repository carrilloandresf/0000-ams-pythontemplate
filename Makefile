.PHONY: up down logs build ps run-local

up:
docker compose up -d --build

build:
docker compose build

down:
docker compose down

logs:
docker compose logs -f api

ps:
docker compose ps

run-local:
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
