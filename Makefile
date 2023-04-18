.PHONY: lint
lint: # Lint code
	flake8 --exclude tests ./backend
	mypy --exclude tests ./backend
	black --line-length 79 --skip-string-normalization --check ./backend

.PHONY: run
run: # Run the backend
	uvicorn backend.main:app --reload

.PHONY: docs
docs: # Open swagger docs
	open http://localhost:8000/docs

.PHONY: install
install: # Install dependencies
	pip install -r backend/requirements.txt