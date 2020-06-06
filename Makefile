
test:
	poetry run pytest

lint:
	flake8 pyfunctory/

format:
	black pyfunctory/

setup:
	poetry install && pre-commit install
