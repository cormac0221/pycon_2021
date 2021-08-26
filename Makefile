# PYTHON_DIR := ~/.pyenv/versions/3.7.10/bin/python3
PYTHON_DIR := /Users/i.derkach/.pyenv/shims/python3

DB := postgresql://postgres:postgres@localhost/db

init-pip:
	$(PYTHON_DIR) -m venv .venv
	.venv/bin/python -m pip install -r requirements.txt

init-poetry:
	$(PYTHON_DIR) -m venv .venv
	poetry install

update-requirements:
	poetry export --without-hashes  > requirements.txt


prepare-db:
	docker-compose down -v
	docker-compose up -d db

run-db:
	DB_URL=$(DB) python db/utils/db_tools.py
