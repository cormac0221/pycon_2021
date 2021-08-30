import re
from typing import Any, List, Optional, Tuple, Type, Union

import sqlalchemy as sa
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Mapper, Query, Session, scoped_session, sessionmaker
from sqlalchemy_utils import generic_repr

convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}
metadata = MetaData(naming_convention=convention)


def classname_to_tablename(name: str) -> str:
    result: List[str] = []

    last_index = 0
    for match in re.finditer(r'(?P<abbreviation>[A-Z]+(?![a-z]))|(?P<word>[A-Za-z][a-z]+)|(?P<digit>\d+)', name):
        if match.start() != last_index:
            raise ValueError(f'Could not translate class name "{name}" to table name')

        last_index = match.end()
        result.append(match.group().lower())

    return '_'.join(result)


@as_declarative(metadata=metadata)
@generic_repr
class BaseTable:
    @declared_attr
    def __tablename__(cls) -> Optional[str]:  # noqa
        return classname_to_tablename(cls.__name__)  # type: ignore  #pylint: disable=E1101

    id = sa.Column(sa.Integer(), primary_key=True)
    created_at = sa.Column(sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now())


def _get_query_cls(mapper: Union[Tuple[Type[Any], ...], Mapper], session: Session) -> Query:
    if mapper:
        m = mapper
        if isinstance(m, tuple):
            m = mapper[0]
        if isinstance(m, Mapper):
            m = m.entity

        try:
            return m.__query_cls__(mapper, session)
        except AttributeError:
            pass

    return Query(mapper, session)


current_session = scoped_session(sessionmaker())
