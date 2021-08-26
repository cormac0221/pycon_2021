PYTHON_DIR := ~/.pyenv/versions/3.7.10/bin/python3

DB := postgresql://postgres:postgres@localhost/db

init:
	$(PYTHON_DIR) -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install poetry
	.venv/bin/poetry install

prepare-db:
	docker-compose down -v
	docker-compose up -d db

run-db:
	DB_URL=$(DB) python db/utils/db_tools.py

run-admin:
	DB_URL=$(DB) python admin/app.py