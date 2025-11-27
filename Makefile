.PHONY: up down build logs test

build:
	docker-compose build

up:
	docker-compose up -d

logs:
	docker-compose logs -f app

down:
	docker-compose down

test:
	pytest
