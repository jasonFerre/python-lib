install:
	pip install --upgrade pip poetry
	poetry install

test:
	poetry run pytest

format:
	poetry run isort .
	poetry run black .

lint: format
	poetry run flake8 

build:
	poetry build

release-prod:
	poetry config pypi-token.pypi ${PYPI_TOKEN}
	poetry publish -n