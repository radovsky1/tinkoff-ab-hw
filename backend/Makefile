.PHONY: lint
lint: # Lint code
	flake8 --exclude tests ./app
	mypy --exclude tests ./app
	black --line-length 79 --skip-string-normalization --check ./app

.PHONY: run
run: # Run the backend
	uvicorn app.main:app --reload

.PHONY: docs
docs: # Open swagger docs
	open http://localhost:8000/docs

.PHONY: install
install: # Install dependencies
	pip install -r ./requirements.txt

.PHONY: migrate_apply
migrate_apply: # Apply migrations
	docker-compose exec web alembic upgrade head

.PHONY: migrate_downgrade
migrate_downgrade: # Downgrade migrations
	docker-compose exec web alembic downgrade -1


