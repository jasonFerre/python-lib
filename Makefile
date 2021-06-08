install:
	poetry install

run-tests:
	poetry run pytest

build:
	poetry build

release-prod:
	poetry config pypi-token.pypi ${PYPI_TOKEN}
	poetry publish -n