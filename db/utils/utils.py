from contextlib import contextmanager
from typing import Any, Iterator
from sqlalchemy.orm import Session


@contextmanager
def create_session(session: Any = Session, **kwargs: Any) -> Iterator[Session]:
    """Provide a transactional scope around a series of operations."""
    new_session = session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()
