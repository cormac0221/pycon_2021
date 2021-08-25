init:
	~/.pyenv/versions/3.7.10/bin/python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install poetry
	.venv/bin/poetry install
