from typer import echo


def create_all() -> None:
    from db import metadata
    from db.utils.settings import DBSettings

    db_settings = DBSettings()

    db_settings.setup_db()
    echo('creating')
    metadata.create_all()
    echo('complete!')


if __name__ == "__main__":
    create_all()
