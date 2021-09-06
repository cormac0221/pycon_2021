from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy.orm import joinedload

from admin.app import Individual
from db import create_session


class Income(BaseModel):
    month: str
    sum: int


class IndividInfo(BaseModel):
    name: str
    family_name: str
    forname: Optional[str]
    inn: int

    income: List[Income]


class UserNotFoundError(Exception):
    pass


def get_individ_info(inn: int) -> Optional[IndividInfo]:
    with create_session() as session:
        individ = (
            session.query(Individual).options(joinedload(Individual.income)).filter(Individual.inn == inn)
        ).one_or_none()

        if individ is None:
            raise UserNotFoundError

        incomes = []
        for income in individ.income:
            incomes.append(Income(month=income.month, sum=income.sum))

        return IndividInfo(
            inn=individ.inn,
            name=individ.name,
            family_name=individ.family_name,
            forname=individ.forname,
            income=incomes
        )
