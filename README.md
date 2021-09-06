## Репозиторий проекта МК Pycon 2021 "Flask-Admin, SQLAlchemy и FastAPI"

## Подготовка к МК
Что потребуется:
1. Компьютер с MacOS или Linux
2. Доступ в интернет
3. Установить Docker

Порядок действий для подготовки к МК:
1. Установить Python 3.7.10 через pyenv: https://github.com/pyenv/pyenv
2. Запустить команду: `make init`

### Начало МК
Перед началом МК запустите Docker и введите команду:

`. .venv/bin/activate`

Затем `make prepare-db` 


При ошибке импортов экспортируйте PYTHONPATH:

`export PYTHONPATH=.`
