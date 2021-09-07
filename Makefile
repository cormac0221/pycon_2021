PYTHON_DIR := ~/.pyenv/versions/3.7.10/bin/python3
VENV = .venv
DB := postgresql://postgres:postgres@localhost/db

CODE = \
    admin \
    api \
    db

JOBS ?= 4

init:
	$(PYTHON_DIR) -m venv .venv
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install poetry
	$(VENV)/bin/poetry install

prepare-db:
	docker-compose down -v
	docker-compose up -d db

run-db:
	DB_URL=$(DB) python db/utils/db_tools.py

run-admin:
	DB_URL=$(DB) python admin/app.py

run-api:
	DB_URL=$(DB) python api/app.py

lint:
	$(VENV)/bin/black --check $(CODE)
	$(VENV)/bin/flake8 --jobs $(JOBS) --statistics $(CODE)
	$(VENV)/bin/mypy --config-file mypy.ini $(CODE)

pretty:
	$(VENV)/bin/black --target-version py37 --skip-string-normalization $(CODE)
	$(VENV)/bin/isort $(CODE)
	$(VENV)/bin/unify --in-place --recursive $(CODE)
