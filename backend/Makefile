.PHONY: lint
lint: # Lint code
	flake8 --exclude tests .
	mypy --exclude tests .
	black --line-length 79 --skip-string-normalization --check .

.PHONY: run
run: # Run the backend
	uvicorn app.main:app --reload

.PHONY: docs
docs: # Open swagger docs
	open http://localhost:8000/docs

.PHONY: install
install: # Install dependencies
	pip install -r ./requirements.txt