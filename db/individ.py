import sqlalchemy as sa
import sqlalchemy.orm as so

from db.utils.base import BaseTable


class Individual(BaseTable):
    """Даненые о физическом лице"""

    name = sa.Column(sa.Text, nullable=False, doc='Имя')
    family_name = sa.Column(sa.Text, nullable=False, doc='Фамилия')
    forname = sa.Column(sa.Text, doc='Отчество')
    birth_date = sa.Column(sa.Date, nullable=False, doc='Дата рождения')
    inn = sa.Column(sa.Integer, nullable=False, unique=True, doc='ИНН в РФ')


class TaxableIncome(BaseTable):
    """Данные о доходах"""

    month = sa.Column(sa.Text, nullable=False, doc='Месяц')
    sum = sa.Column(sa.Integer, nullable=False, doc='Сумма дохода')

    individual_id = sa.Column(
        sa.Integer(), sa.ForeignKey(Individual.id, ondelete='CASCADE'), index=True, nullable=False
    )
    individual = so.relationship(Individual, backref='income')
