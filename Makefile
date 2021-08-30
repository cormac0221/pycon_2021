PYTHON_DIR := ~/.pyenv/versions/3.7.10/bin/python3
VENV = .venv
DB := postgresql://postgres:postgres@localhost/db

init:
	$(PYTHON_DIR) -m venv .venv
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install poetry
	$(VENV)/bin/poetry install

prepare-db:
	docker-compose down -v
	docker-compose up -d db

pretty:
	$(VENV)/bin/black --target-version py37
	$(VENV)/bin/unify

run-db:
	DB_URL=$(DB) python db/utils/db_tools.py

run-admin:
	DB_URL=$(DB) python admin/app.py

run-api:
	DB_URL=$(DB) python api/app.py
